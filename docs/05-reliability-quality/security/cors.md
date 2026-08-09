---
title: "CORS"
slug: cors
description: "How the browser relaxes the same-origin policy for cross-origin requests, why preflights happen, and the credential rules that make wildcards illegal."
keywords: ["CORS", "cross-origin resource sharing", "preflight", "OPTIONS request", "Access-Control-Allow-Origin", "credentials", "simple request", "Vary Origin", "opaque response", "CORS error"]
part: "05 · Reliability & Quality"
domain: "Security"
subcategory: "The Security Model"
difficulty: "Advanced"
reading_time_min: 16
priority: "Critical"
status: "Published"
canonical: true
last_reviewed: "2026-08-09"
prerequisites:
  - "Same-Origin Policy"
related:
  - "Same-Origin Policy"
  - "Isolation (COOP/COEP)"
next:
  - "Isolation (COOP/COEP)"
alternatives:
  - "Isolation (COOP/COEP)"
common_mistakes:
  - "anti-patterns/README.md#security"
  - "#common-mistakes"
frameworks: []
references:
  - { title: "WHATWG — Fetch Standard: CORS protocol", url: "https://fetch.spec.whatwg.org/#http-cors-protocol" }
  - { title: "MDN — Cross-Origin Resource Sharing (CORS)", url: "https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS" }
  - { title: "MDN — Access-Control-Allow-Origin", url: "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin" }
  - { title: "OWASP — CORS OriginHeaderScrutiny", url: "https://owasp.org/www-community/attacks/CORS_OriginHeaderScrutiny" }
---

# CORS

> CORS does not protect your server. It protects the *user's browser* from handing your server's responses to a page that should not read them — which is why fixing a CORS error on the client is always impossible.

**Part:** [05 · Reliability & Quality](../) · **Domain:** Security · **Priority:** Critical · **Difficulty:** Advanced · **Reading time:** ~16 min

## TL;DR

The same-origin policy stops a page from *reading* cross-origin responses. **CORS** is the server's mechanism for opting in: response headers, chiefly `Access-Control-Allow-Origin`, tell the browser it may hand the response to the calling script. Requests that could not be made with a plain HTML form — custom headers, `PUT`, `application/json` — trigger a **preflight** `OPTIONS` request that asks permission before the real request is sent. Credentials (cookies, TLS client certs) require both `credentials: "include"` on the client and `Access-Control-Allow-Credentials: true` plus a **specific** origin — never `*` — on the server. Every CORS error is a server configuration issue; nothing in the browser can be changed to fix one.

> **Recommendation:** Echo a validated origin from an allow-list, always send `Vary: Origin`, and reach for a same-origin proxy path when the allow-list starts growing.

## At a Glance

| | |
| --- | --- |
| **Use when** | A browser must read a response from a different origin — an API on another domain, a CDN font, an external service. |
| **Avoid when** | You control both sides and can serve them same-origin behind one gateway; that removes the problem instead of configuring around it. |
| **Alternatives** | [Same-origin proxy](#alternative-approaches), server-to-server calls, [COOP/COEP](#alternative-approaches) for a different isolation problem. |
| **Primary risk** | Reflecting the `Origin` header without validating it, which grants every site on the internet credentialed access. |
| **Maturity** | Stable — defined by the Fetch Standard; the Private Network Access extension is still rolling out. |

## Prerequisites

CORS is a relaxation of a rule; learn the rule first.

- [Same-Origin Policy](./same-origin-policy.md) — what an origin is and what it forbids by default.

## Overview

The protocol has three moving parts.

**1. The request carries `Origin`.** The browser sets it, and it cannot be changed by script. It is a fact about who is asking.

**2. The response grants or withholds access.**

| Header | Meaning |
| --- | --- |
| `Access-Control-Allow-Origin` | The single origin (or `*`) permitted to read this response |
| `Access-Control-Allow-Credentials` | `true` if cookies and auth headers may be sent and the response read |
| `Access-Control-Expose-Headers` | Response headers beyond the safelist that script may read |
| `Access-Control-Allow-Methods` | Methods permitted (preflight responses only) |
| `Access-Control-Allow-Headers` | Request headers permitted (preflight responses only) |
| `Access-Control-Max-Age` | How long the browser may cache the preflight result |

**3. Some requests are preflighted.** A request is "simple" — sent directly, no preflight — only if it uses `GET`, `HEAD`, or `POST`; carries only safelisted headers (`Accept`, `Accept-Language`, `Content-Language`, `Content-Type`, plus a few); and its `Content-Type` is `application/x-www-form-urlencoded`, `multipart/form-data`, or `text/plain`. Anything else — `PUT`, `DELETE`, `Authorization`, `X-Request-Id`, or `Content-Type: application/json` — triggers an `OPTIONS` preflight first.

The reason for that split is historical and precise: those are exactly the requests an HTML form could already make without JavaScript, so they add no new capability. Everything else must ask first.

Three consequences catch people out.

**A simple request is still sent.** If the response lacks the right header, the browser blocks the *reading* of the response, not the sending of the request. A `POST` that creates a record still created it; the script just cannot see the result. CORS is not a substitute for CSRF protection.

**`*` and credentials are mutually exclusive.** With `credentials: "include"`, `Access-Control-Allow-Origin: *` is rejected — the server must echo the exact origin. Likewise `Access-Control-Allow-Headers: *` does not cover `Authorization`, which must be named explicitly.

**Only a few response headers are readable by default.** `Cache-Control`, `Content-Language`, `Content-Length`, `Content-Type`, `Expires`, `Last-Modified`, `Pragma`. Anything else — `X-Total-Count`, `Location`, a rate-limit header — needs `Access-Control-Expose-Headers`, or `response.headers.get()` returns `null` with no error.

## The Problem

Two configurations dominate real incidents, and they fail in opposite directions.

The permissive one:

```js
// ❌ Reflects any origin, with credentials. Every site on the internet can read
//    authenticated responses from this API using the visitor's own cookies.
app.use((req, res, next) => {
  res.setHeader("Access-Control-Allow-Origin", req.headers.origin ?? "*");
  res.setHeader("Access-Control-Allow-Credentials", "true");
  next();
});
```

This is a full account-takeover primitive. A user visits `evil.example`, which issues `fetch("https://api.yourapp.com/me", { credentials: "include" })`. The browser attaches the user's session cookie, the server reflects `evil.example` as an allowed origin, and the attacker's script reads the response. Everything the API exposes to a logged-in user is now readable by any page that user visits.

The broken-but-safe one:

```js
// ❌ CORS "handled" — except the preflight, which is what actually fails.
app.use(cors({ origin: "https://app.example.com" }));
app.put("/api/settings", requireAuth, updateSettings);
```

The `PUT` with `Content-Type: application/json` triggers an `OPTIONS` preflight. If `requireAuth` runs on `OPTIONS` — which carries no cookies, by design — it responds `401`, and the browser reports a CORS failure with no useful detail. The team spends a day changing `fetch` options; nothing on the client can fix it.

And the caching failure, which is intermittent and therefore worst:

```js
// ❌ Echoes the origin but never sends Vary: Origin.
res.setHeader("Access-Control-Allow-Origin", allowedOrigins.has(origin) ? origin : "");
```

A CDN or shared cache stores one response with `Access-Control-Allow-Origin: https://app.example.com` and serves it to a request from `https://admin.example.com`. That user gets a header naming someone else's origin and a CORS error — or, in the reverse direction, a cached response granting access to an origin that should not have it.

## Why It Matters

CORS misconfiguration is a recurring finding in security assessments, and the severity is high because the exploit is trivial: a `fetch` from any page the victim visits.

The reason it goes wrong so often is a mismatch between the error and the cause. A CORS failure surfaces in the browser console, on the client, in the network tab — so it looks like a client problem. It never is. Teams under deadline pressure reach for the fastest thing that makes the message disappear, and the fastest thing is reflecting the origin. That fix ships, works, and is invisible until an audit.

The operational cost matters too. Every preflight is an extra round-trip before the real request, so an API called on a hot path from another origin pays double latency until `Access-Control-Max-Age` caches the result — and browsers cap that cache (Chromium at two hours, Firefox at twenty-four), and clear it whenever the request's credentials mode changes.

There is also a correctness trap that produces silent bugs rather than errors: a missing `Access-Control-Expose-Headers` makes `response.headers.get("X-Total-Count")` return `null`. No exception, no console warning — pagination just stops working, and the cause is a header that was sent but not exposed.

## Mental Model

Walk through the browser's decision for every cross-origin request.

```text
   script calls fetch("https://api.other.com/x", { … })
        │
        ├─ same origin? ──────────────► send, read freely. Done.
        │
        └─ cross origin
             │
             ├─ "simple"? (GET/HEAD/POST + safelisted headers + safe Content-Type)
             │      │
             │      ├─ YES ─► send the real request
             │      │            │
             │      │            └─ response has Access-Control-Allow-Origin matching us?
             │      │                  YES → script may read it
             │      │                  NO  → request WAS sent; response is hidden
             │      │
             │      └─ NO ──► send OPTIONS preflight (no body, no cookies)
             │                   │
             │                   ├─ 2xx + Allow-Origin/Methods/Headers cover it?
             │                   │      YES → send the real request
             │                   │      NO  → block. Real request never sent.
             │
             └─ credentials: "include"?
                    requires Allow-Credentials: true AND a specific (non-*) origin
```

Three rules to keep in hand:

1. **The response decides, not the request.** Nothing on the client can grant access.
2. **A preflight is a question about the *next* request,** sent without cookies. Authentication middleware must not answer it.
3. **Blocked reading is not blocked sending.** Simple requests reach the server regardless, which is why CSRF defenses are a separate requirement.

## Best Practices

- **Maintain an explicit allow-list** and echo the request's origin only when it is in the list. Never reflect unconditionally, and never use `*` with credentials.
- **Always send `Vary: Origin`** whenever the value of `Access-Control-Allow-Origin` depends on the request. Without it, any shared cache will serve the wrong header to someone.
- **Handle `OPTIONS` before authentication.** Preflights carry no credentials by design; auth middleware must skip them entirely.
- **Set `Access-Control-Max-Age`** to a few hours to amortize preflight cost, and remember browsers cap it.
- **Expose the headers your client reads** — pagination counts, request ids, rate-limit headers — with `Access-Control-Expose-Headers`.
- **Prefer a same-origin path.** Serving the API under `/api` on the app's own origin via a gateway removes CORS, removes preflights, and removes the whole class of misconfiguration.
- **Match origins exactly.** Compare full origin strings, never `startsWith` or a substring test — `https://app.example.com.evil.com` passes a naive check.
- **Do not treat CORS as authorization.** Keep CSRF tokens or `SameSite` cookies regardless; CORS never stopped the request from arriving.

## Trade-offs

CORS is the only mechanism for genuinely cross-origin browser access, and it costs a round-trip and a configuration surface.

**Advantages**

- Lets independent origins integrate without a proxy or shared infrastructure.
- Per-origin, per-method, per-header granularity, decided by the resource owner.
- Preflight caching amortizes the cost for repeated calls.

**Disadvantages**

- Every non-simple request pays an extra round-trip until the preflight is cached.
- Configuration lives in server or CDN config, far from the client code that depends on it.
- Error messages are deliberately vague, so debugging is slow.
- Reflecting the origin is both the easiest fix and a critical vulnerability.

| Dimension | This approach | Cost / caveat |
| --- | --- | --- |
| Performance | Simple requests are free | Preflight adds a full RTT; caching is capped and credential-mode-specific |
| Complexity | A few headers | Must be consistent across every origin, CDN, and error path |
| Maintainability | Allow-list is explicit and reviewable | Drifts as environments and preview deploys multiply |
| Failure behavior | Blocked reads are loud in the console | Missing `Expose-Headers` fails silently as `null` |

## Alternative Approaches

The real decision is whether the browser should be making a cross-origin request at all.

| Approach | Best when | Weakness | See |
| --- | --- | --- | --- |
| CORS with an allow-list | Genuinely independent origins | Preflight latency; config far from the client | (this article) |
| Same-origin reverse proxy (`/api/*`) | You control both sides | An extra hop; the gateway must be maintained | [Same-Origin Policy](./same-origin-policy.md) |
| Server-to-server call | The browser never needs the raw response | Adds a backend and hides client context | — |
| `crossorigin` on static assets | Fonts, scripts, images with SRI | Needs `Access-Control-Allow-Origin` on the CDN too | `Isolation (COOP/COEP) · Security` |
| `no-cors` opaque response | Fire-and-forget beacons, cache warming | The response is unreadable, status invisible | — |

The practical rule: **if you own both sides, make it same-origin. CORS is for integrating with systems you do not control.**

## Bad Example

An API that "supports CORS" by reflecting whatever it is told, with auth in front of the preflight.

```js
// ❌ server.js — a full credentialed-CORS vulnerability plus a broken preflight.
import express from "express";
const app = express();

app.use((req, res, next) => {
  // ❌ Reflects ANY origin, unconditionally.
  res.setHeader("Access-Control-Allow-Origin", req.headers.origin ?? "*");
  // ❌ …and permits credentials with it. Any site can read authenticated responses.
  res.setHeader("Access-Control-Allow-Credentials", "true");
  res.setHeader("Access-Control-Allow-Methods", "GET,POST,PUT,DELETE");
  res.setHeader("Access-Control-Allow-Headers", "*");   // ❌ does not cover Authorization
  // ❌ No Vary: Origin — shared caches will serve one origin's header to another.
  next();
});

// ❌ Auth runs before OPTIONS is handled; preflights carry no cookies, so they 401.
app.use(requireAuth);

app.options("*", (req, res) => res.sendStatus(204));   // ❌ never reached

app.get("/api/me", (req, res) => {
  res.setHeader("X-Total-Count", "42");                // ❌ never exposed to script
  res.json({ id: req.user.id, email: req.user.email });
});

// ❌ A naive allow-list check elsewhere in the codebase.
function isAllowed(origin) {
  return origin?.startsWith("https://app.example.com");  // ❌ matches evil subdomain tricks
}
```

```js
// ❌ client.js — trying to fix a server problem on the client.
const res = await fetch("https://api.example.com/api/settings", {
  method: "PUT",
  mode: "no-cors",                        // ❌ makes the response opaque, not accessible
  credentials: "include",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(settings),
});

console.log(res.status);                  // ❌ always 0 for an opaque response
console.log(res.headers.get("X-Total-Count"));   // ❌ null — header was never exposed
```

**What goes wrong:** reflecting `req.headers.origin` alongside `Access-Control-Allow-Credentials: true` means any page the user visits can call this API with their session cookie and read the response — `evil.example` gets the user's email, and whatever else `/api/me` and its siblings return. `Access-Control-Allow-Headers: "*"` looks permissive but does not authorize `Authorization`, which must be named explicitly, so token-authenticated preflights fail anyway. `requireAuth` is mounted before the `OPTIONS` handler, and preflights are sent without credentials by specification, so every non-simple request preflights, gets a `401`, and surfaces as an opaque CORS error that no client change can fix. The missing `Vary: Origin` means a CDN caches one origin's `Access-Control-Allow-Origin` and serves it to another, producing failures that appear and disappear with cache state. `isAllowed` uses `startsWith`, so `https://app.example.com.evil.com` passes. And on the client, `mode: "no-cors"` does not bypass anything — it opts into an opaque response with status `0` and no readable headers, which is why `X-Total-Count` is `null` twice over: not exposed, and unreadable regardless.

## Good Example

An explicit allow-list, preflight handled before authentication, exposed headers, and a same-origin proxy for the common case.

```js
// ✅ cors.js — one module owns the policy.
const ALLOWED_ORIGINS = new Set([
  "https://app.example.com",
  "https://admin.example.com",
  ...(process.env.NODE_ENV !== "production" ? ["http://localhost:5173"] : []),
]);

// ✅ Preview deployments: an exact pattern, anchored at both ends.
const PREVIEW = /^https:\/\/pr-\d+\.preview\.example\.com$/;

export function isAllowedOrigin(origin) {
  if (typeof origin !== "string") return false;
  return ALLOWED_ORIGINS.has(origin) || PREVIEW.test(origin);   // ✅ exact match, never substring
}

export function cors(req, res, next) {
  const origin = req.headers.origin;

  // ✅ Vary is sent regardless of the outcome, so caches key on Origin either way.
  res.setHeader("Vary", "Origin");

  if (!origin) return next();                 // same-origin or non-browser client
  if (!isAllowedOrigin(origin)) {
    // ✅ No CORS headers at all — the browser blocks the read; we do not advertise the policy.
    return req.method === "OPTIONS" ? res.sendStatus(403) : next();
  }

  res.setHeader("Access-Control-Allow-Origin", origin);        // ✅ specific, never *
  res.setHeader("Access-Control-Allow-Credentials", "true");
  res.setHeader("Access-Control-Expose-Headers", "X-Total-Count, X-Request-Id, X-RateLimit-Remaining");

  // ✅ Preflight is answered here, before any authentication runs.
  if (req.method === "OPTIONS") {
    res.setHeader("Access-Control-Allow-Methods", "GET, POST, PUT, PATCH, DELETE");
    res.setHeader("Access-Control-Allow-Headers", "Content-Type, Authorization, X-Request-Id");
    res.setHeader("Access-Control-Max-Age", "7200");           // ✅ 2h — the Chromium cap
    return res.sendStatus(204);
  }

  next();
}
```

```js
// ✅ server.js — order matters: CORS, then auth, then routes.
import express from "express";
import { cors } from "./cors.js";

const app = express();

app.use(cors);          // ✅ answers OPTIONS and returns before auth
app.use(requireAuth);   // ✅ never sees a preflight

app.get("/api/orders", async (req, res) => {
  const { rows, total } = await listOrders(req.user.id, req.query);
  res.setHeader("X-Total-Count", String(total));   // ✅ named in Expose-Headers above
  res.json(rows);
});

// ✅ CSRF protection is independent of CORS — the request still arrives either way.
app.use(csrfProtection({ cookie: { sameSite: "lax", secure: true, httpOnly: true } }));
```

```js
// ✅ client.js — no mode tricks; the server grants access or it does not.
export async function updateSettings(settings, { signal } = {}) {
  const res = await fetch("https://api.example.com/api/settings", {
    method: "PUT",
    credentials: "include",                         // ✅ requires a specific Allow-Origin server-side
    headers: {
      "Content-Type": "application/json",           // ✅ triggers a preflight, by design
      "X-Request-Id": crypto.randomUUID(),          // ✅ named in Allow-Headers
    },
    body: JSON.stringify(settings),
    signal,
  });

  if (!res.ok) throw new HttpError(res.status, await res.text());

  return {
    data: await res.json(),
    total: Number(res.headers.get("X-Total-Count") ?? 0),   // ✅ readable: it was exposed
  };
}
```

```nginx
# ✅ The better answer where you own both sides: no cross-origin request at all.
#    The app and the API share an origin, so CORS never enters the picture.
location /api/ {
    proxy_pass         https://api.internal.example.com/;
    proxy_set_header   Host              $host;
    proxy_set_header   X-Forwarded-For   $proxy_add_x_forwarded_for;
    proxy_set_header   X-Forwarded-Proto $scheme;
}
```

**Why it's better:** the allow-list is explicit and matched exactly — a `Set` lookup plus an anchored regex for preview deploys — so `https://app.example.com.evil.com` fails, and an unknown origin receives no CORS headers at all rather than a reflection. `Vary: Origin` is set on every path, including the rejection path, so no shared cache can ever serve one origin's grant to another. The preflight is answered inside the CORS middleware and returns before `requireAuth` runs, which removes the `401`-on-`OPTIONS` failure entirely; `Allow-Headers` names `Authorization` and `X-Request-Id` explicitly rather than relying on `*`, which does not cover them. `Expose-Headers` lists exactly the headers the client reads, so `X-Total-Count` comes back as a number instead of `null`. CSRF protection remains in place independent of CORS, acknowledging that simple requests reach the server whether or not the response can be read. And the nginx block shows the option that beats all of this: proxying the API onto the app's own origin, which eliminates preflights, latency, and the entire configuration surface for the case where you control both sides.

## Common Mistakes

See the [Security anti-patterns](../../../anti-patterns/) for the domain catalog. Concept-specific:

### Mistake: Reflecting `Origin` with credentials enabled

- **Symptom:** `Access-Control-Allow-Origin: <whatever was sent>` together with `Access-Control-Allow-Credentials: true`.
- **Why it fails:** Any site the user visits can call your API with their cookies attached and read the response. This is a complete cross-origin data-disclosure vulnerability, not a misconfiguration.
- **Fix:** Validate against an explicit allow-list and echo only matching origins; never combine reflection with credentials.

### Mistake: Authenticating the preflight

- **Symptom:** `OPTIONS` returns `401` or `403`; the browser reports a CORS error with no detail and the real request is never sent.
- **Why it fails:** Preflights are sent without credentials by specification, so any auth middleware in front of them will reject them.
- **Fix:** Handle `OPTIONS` before authentication and return `204` with the CORS headers.

### Mistake: Omitting `Vary: Origin`

- **Symptom:** Intermittent CORS failures that correlate with CDN cache hits and disappear on a hard refresh.
- **Why it fails:** A cache stores the response keyed only by URL, so one origin's `Access-Control-Allow-Origin` value is served to a request from a different origin.
- **Fix:** Send `Vary: Origin` on every response whose CORS headers depend on the request, including error and rejection paths.

### Mistake: Substring or prefix origin matching

- **Symptom:** An allow-list check using `startsWith`, `includes`, or an unanchored regex.
- **Why it fails:** `https://app.example.com.evil.com` starts with the allowed prefix, and `https://evil-app.example.com` is contained in a loose pattern.
- **Fix:** Compare complete origin strings, or use a regex anchored with `^` and `$`.

### Mistake: Expecting `mode: "no-cors"` to bypass CORS

- **Symptom:** `response.status` is `0`, the body is empty, and every header read returns `null`.
- **Why it fails:** `no-cors` does not grant access — it opts into an *opaque* response, which is deliberately unreadable and limited to simple requests.
- **Fix:** Fix the server headers. `no-cors` is only appropriate for fire-and-forget requests whose response you genuinely do not need.

### Mistake: Reading a response header that was never exposed

- **Symptom:** `response.headers.get("X-Total-Count")` is `null` even though the header is visible in DevTools.
- **Why it fails:** Only a small safelist of response headers is readable cross-origin; everything else requires `Access-Control-Expose-Headers`.
- **Fix:** List every non-safelisted header the client reads in `Access-Control-Expose-Headers`.

### Mistake: Treating CORS as CSRF protection

- **Symptom:** CSRF tokens removed "because CORS handles it."
- **Why it fails:** Simple requests are *sent* before any CORS check; only reading the response is blocked. A cross-origin `POST` still performs its side effect.
- **Fix:** Keep `SameSite` cookies and CSRF tokens; treat CORS purely as a read-access control.

## Checklist

- [ ] `Access-Control-Allow-Origin` is a specific origin from an explicit allow-list, never a blanket reflection.
- [ ] `*` is never combined with `Access-Control-Allow-Credentials: true`.
- [ ] Origin matching compares complete strings or uses anchored patterns.
- [ ] `Vary: Origin` is sent on every response whose CORS headers vary, including rejections.
- [ ] `OPTIONS` is handled before authentication and returns `204`.
- [ ] `Access-Control-Allow-Headers` names `Authorization` and every custom header explicitly.
- [ ] `Access-Control-Expose-Headers` lists every non-safelisted header the client reads.
- [ ] `Access-Control-Max-Age` is set to amortize preflight cost.
- [ ] CSRF protection exists independently of CORS.
- [ ] Preview and local development origins are handled by pattern, not by disabling the policy.
- [ ] A same-origin proxy was considered and rejected for a stated reason before configuring CORS.

## Related Articles

- [Same-Origin Policy](./same-origin-policy.md) — the default CORS relaxes, and the definition of an origin.
- [Isolation (COOP/COEP)](./) (planned) — a different cross-origin problem: process isolation rather than read access.
- [Sandboxing & Site Isolation · The Web Platform](../../00-foundations/web-platform/sandboxing-and-site-isolation.md) — why cross-origin boundaries became process boundaries.
- [HTTP/1.1 Semantics · Networking & Protocols](../../00-foundations/networking-protocols/http-1-1-semantics.md) — the request and response model CORS annotates.
- **Canonical home:** cookie attributes and `SameSite` are owned by [Cookies & Partitioned Storage · Browser APIs](../../00-foundations/browser-apis/cookies-and-partitioned-storage.md).

## References

- [WHATWG — Fetch Standard: CORS protocol](https://fetch.spec.whatwg.org/#http-cors-protocol) — the normative algorithm, including the simple-request definition.
- [MDN — Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) — header reference and worked preflight examples.
- [MDN — Access-Control-Allow-Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin) — the wildcard-and-credentials restriction in detail.
- [OWASP — CORS OriginHeaderScrutiny](https://owasp.org/www-community/attacks/CORS_OriginHeaderScrutiny) — how origin reflection is exploited in practice.

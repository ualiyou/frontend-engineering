---
title: "Sandboxing & Site Isolation"
slug: sandboxing-and-site-isolation
description: "Why the browser puts each site in its own process, what the renderer sandbox actually forbids, and how Spectre turned isolation from an optimization into a requirement."
keywords: ["site isolation", "renderer sandbox", "process per site", "Spectre", "cross-origin isolation", "iframe sandbox", "COOP", "COEP", "browsing context group", "speculative execution"]
part: "00 · Foundations"
domain: "The Web Platform"
subcategory: "Browser Internals"
difficulty: "Foundational"
reading_time_min: 11
priority: "Critical"
status: "Published"
canonical: true
last_reviewed: "2026-08-09"
prerequisites:
  - "Process & Thread Architecture"
related:
  - "Process & Thread Architecture"
  - "The Main Thread"
next:
  - "The Main Thread"
alternatives:
  - "The Main Thread"
common_mistakes:
  - "anti-patterns/README.md#the-web-platform"
  - "#common-mistakes"
frameworks: []
references:
  - { title: "Chromium — Site Isolation design", url: "https://www.chromium.org/Home/chromium-security/site-isolation/" }
  - { title: "MDN — The iframe sandbox attribute", url: "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe#sandbox" }
  - { title: "MDN — Cross-Origin-Opener-Policy", url: "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Opener-Policy" }
  - { title: "web.dev — Why you need cross-origin isolation", url: "https://web.dev/articles/why-coop-coep" }
---

# Sandboxing & Site Isolation

> The renderer is assumed to be compromised. Every security guarantee the web platform makes is built on that assumption being cheap to hold.

**Part:** [00 · Foundations](../) · **Domain:** The Web Platform · **Priority:** Critical · **Difficulty:** Foundational · **Reading time:** ~11 min

## TL;DR

A modern browser runs page content in **renderer processes** that are **sandboxed** — stripped of file, network, and device access, and allowed to reach the outside world only by asking a privileged browser process. **Site Isolation** goes further: it guarantees that documents from different sites land in *different* renderer processes, so a memory-disclosure bug in one site's renderer cannot read another site's data. This became mandatory after Spectre showed that any process able to time its own memory can read anything in its address space, which made "same process, different origin" an unenforceable boundary. The consequences reach ordinary application code through `SharedArrayBuffer` gating, the `iframe sandbox` attribute, and the COOP/COEP headers that opt a page into a stricter isolation group.

> **Recommendation:** Assume any cross-origin content you embed shares nothing with you, sandbox every third-party iframe with an explicit allow-list, and adopt cross-origin isolation only when you need the capabilities it unlocks.

## At a Glance

| | |
| --- | --- |
| **Use when** | Embedding third-party content, debugging per-frame memory cost, or enabling `SharedArrayBuffer` and precise timers. |
| **Avoid when** | You are tempted to rely on process boundaries as an application-level authorization mechanism — they are not one. |
| **Alternatives** | [The Main Thread](#alternative-approaches) for scheduling concerns; server-side rendering of untrusted content; a separate origin. |
| **Primary risk** | Assuming isolation you have not opted into — most pages are not cross-origin isolated. |
| **Maturity** | Stable — Site Isolation ships by default on desktop and modern mobile Chromium and Firefox. |

## Prerequisites

The process model comes first; isolation is a policy layered on top of it.

- [Process & Thread Architecture](./process-and-thread-architecture.md) — what a renderer process is and what lives inside it.

## Overview

Three distinct mechanisms hide behind the word "sandbox", and conflating them causes most of the confusion in this area.

| Mechanism | What it constrains | Controlled by |
| --- | --- | --- |
| **Renderer sandbox** | What a renderer process may ask the operating system for | The browser, always on |
| **Site Isolation** | Which documents may share a renderer process | The browser, plus COOP/COEP hints |
| **`iframe sandbox`** | What an embedded document may do inside its own process | You, per embed |

The **renderer sandbox** is an OS-level jail. A renderer cannot open files, bind sockets, spawn processes, or read the clipboard directly; it makes IPC calls to the privileged browser process, which validates each one. This means an attacker who achieves arbitrary code execution inside a renderer has not yet achieved anything on the machine — they must also break out of the sandbox, which is a second, much harder bug.

**Site Isolation** answers a different question: which documents share an address space? The unit is a **site** — scheme plus registrable domain, so `https://a.example.com` and `https://b.example.com` are the same site, while `https://example.com` and `https://example.org` are not. Cross-site documents get different processes; cross-origin same-site documents may still share one unless the page opts into stricter separation.

Site Isolation exists because of **Spectre**. Speculative execution lets a CPU run instructions past a mispredicted branch and leave measurable traces in the cache, so any code that can time memory access precisely can read memory it was never permitted to load — including, in a shared renderer, another origin's response bodies. No amount of same-origin checking inside the process fixes that, because the check itself is what gets speculated past. The only durable answer was to stop putting cross-site data in the same address space, and to gate the tools that make timing precise (`SharedArrayBuffer`, high-resolution `performance.now()`) behind a stronger opt-in.

That opt-in is **cross-origin isolation**, requested with two headers:

- `Cross-Origin-Opener-Policy: same-origin` — severs the `window.opener` relationship with cross-origin documents, so your browsing context group contains only same-origin pages.
- `Cross-Origin-Embedder-Policy: require-corp` (or `credentialless`) — refuses to load cross-origin subresources unless they explicitly opt in with `Cross-Origin-Resource-Policy`.

When both hold, `self.crossOriginIsolated` is `true` and the gated capabilities unlock.

## The Problem

Application code repeatedly assumes a boundary the platform does not provide — or fails to use one it does.

```html
<!-- ❌ A third-party widget with the full authority of a top-level document. -->
<iframe src="https://widgets.vendor.example/rating"></iframe>
```

That frame can navigate the top-level page (`top.location = …`), open pop-ups, trigger downloads, submit forms, and run whatever scripts the vendor ships today or is compromised into shipping tomorrow. It gets its own process under Site Isolation, so it cannot *read* your memory — but process isolation says nothing about what it may *do* through legitimate APIs.

The mirror-image mistake:

```js
// ❌ Assumes cross-origin isolation without checking, and without the headers.
const shared = new SharedArrayBuffer(1024);   // ReferenceError on most pages
const view = new Int32Array(shared);
worker.postMessage({ shared });
```

`SharedArrayBuffer` is undefined unless the document is cross-origin isolated. Code written on a locally served page with permissive headers works in development and throws in production the moment a CDN serves an asset without `Cross-Origin-Resource-Policy`.

And the subtlest one: treating a process boundary as an authorization boundary. Different processes do not mean different permissions — an iframe from your own origin runs with your origin's cookies and storage regardless of how the browser lays out memory.

## Why It Matters

Isolation is the reason a single memory-safety bug in a renderer is a severity-high issue rather than a catastrophe. Without it, one malicious ad on one page could read every cookie and response body in the tab.

For application engineers the practical consequences are three:

**Capability gating.** `SharedArrayBuffer`, unthrottled `performance.now()` resolution, and `performance.measureUserAgentSpecificMemory()` are only available to cross-origin isolated documents. Any workload that needs shared memory — WASM threads, video processing, a multithreaded engine — depends on getting COOP/COEP right, which in turn depends on every embedded resource cooperating.

**Memory cost.** Each renderer process carries tens of megabytes of fixed overhead. A page with twelve cross-site iframes is a page with up to twelve extra processes, which is why ad-heavy pages fall over on low-memory Android devices. Site Isolation makes the cost of embedding visible.

**Embedding safety.** The `sandbox` attribute is the only mechanism that constrains what embedded content may do through legitimate APIs. Skipping it means trusting every vendor's future supply chain.

## Mental Model

Picture the tab as a set of nested containers, each with a different question attached.

```text
  ┌─ Browser process ──────────────────────────────────────────────┐
  │  privileged: files, network, devices, IPC validation           │
  │                                                                │
  │   ┌─ Renderer (site: example.com) ─────┐  ┌─ Renderer (ads) ─┐ │
  │   │  sandboxed: no fs, no raw sockets  │  │  sandboxed too   │ │
  │   │                                    │  │                  │ │
  │   │  ┌ document (a.example.com) ┐      │  │  ┌ iframe doc ┐  │ │
  │   │  │  same-origin policy      │      │  │  │ sandbox="" │  │ │
  │   │  └──────────────────────────┘      │  │  └────────────┘  │ │
  │   └────────────────────────────────────┘  └──────────────────┘ │
  └────────────────────────────────────────────────────────────────┘
        ▲ Site Isolation decides this split
        ▲ COOP/COEP decide whether the group is cross-origin isolated
```

Three questions map to three layers:

1. **"Can this code touch the machine?"** — the renderer sandbox. Answer: only through validated IPC.
2. **"Can this code touch that site's memory?"** — Site Isolation. Answer: not if they are different sites.
3. **"Can this document do that action?"** — same-origin policy, `sandbox`, and Permissions Policy. Answer: whatever you allowed.

Process boundaries answer question two only. Every time you reach for isolation to solve a question-three problem, you are using the wrong tool.

## Best Practices

- **Sandbox every third-party iframe,** starting from `sandbox=""` and adding back only the tokens the embed demonstrably needs. `allow-scripts allow-same-origin` together on content you do not control effectively removes the sandbox.
- **Serve untrusted user content from a separate registrable domain,** not a subdomain. Site Isolation splits on site, so a subdomain may share a process; a different domain never does.
- **Feature-detect `crossOriginIsolated`** before touching `SharedArrayBuffer` or assuming timer precision, and ship a single-threaded fallback.
- **Adopt COOP/COEP deliberately.** Start with `Cross-Origin-Opener-Policy: same-origin-allow-popups` and COEP report-only, read the reports, then tighten. Every cross-origin image, font, and script must carry `Cross-Origin-Resource-Policy` or be loaded `credentialless`.
- **Count your processes when you count your memory.** Profile with the browser's task manager, not just the heap snapshot of one frame.
- **Never treat "different process" as "different privilege."** Authorization is an application concern that outlives any browser architecture decision.

## Trade-offs

Isolation buys a durable security boundary and pays for it in memory and integration friction.

**Advantages**

- A renderer compromise is contained to one site's data, which is what makes the platform's threat model tractable.
- Cross-origin isolation unlocks shared memory and precise timing for workloads that genuinely need them.
- `sandbox` gives per-embed control that no process model can provide.

**Disadvantages**

- Per-process overhead is real and lands hardest on low-memory devices.
- COOP/COEP adoption is all-or-nothing across every subresource, so one uncooperative CDN blocks the whole page.
- COOP severs `window.opener`, breaking OAuth pop-up flows and payment widgets that rely on it.
- Site granularity means same-site cross-origin documents may still share a process, which surprises people who reason in origins.

| Dimension | This approach | Cost / caveat |
| --- | --- | --- |
| Performance | Parallel rendering across frames; no cross-site jank | Tens of MB per extra process |
| Complexity | Sandbox attributes are declarative | COEP requires auditing every subresource |
| Maintainability | Security boundary survives refactors | Third-party breakage appears late, at integration |
| Failure behavior | Contained blast radius on a renderer bug | COOP breaks pop-up-based auth flows loudly |

## Alternative Approaches

Isolation is not the only way to contain untrusted content; it is the one the browser gives you for free.

| Approach | Best when | Weakness | See |
| --- | --- | --- | --- |
| Site Isolation + `sandbox` | Embedding third-party UI you must render | Per-frame memory cost | (this article) |
| Separate registrable domain | User-generated HTML, previews, docs | Extra DNS, certificates, and CORS setup | `Same-Origin Policy · Security` |
| Server-side sanitization, no frame | Rich text and markup you can normalize | Loses interactivity; sanitizers have bugs | `Cross-Site Scripting (XSS) · Security` |
| Web Worker | Untrusted *computation* without DOM access | Not a security boundary against Spectre alone | [The Main Thread](./) (planned) |
| No embedding at all | The integration can be a link | Worse UX | — |

The practical rule: **untrusted markup → separate domain in a sandboxed frame; untrusted computation → a worker; untrusted authority → nothing, revoke it.**

## Bad Example

A dashboard that embeds partner widgets and wants shared-memory image processing.

```html
<!-- ❌ Full-authority embeds. -->
<iframe src="https://partner-a.example/chart"></iframe>
<iframe src="https://partner-b.example/feed"
        sandbox="allow-scripts allow-same-origin"></iframe>
```

```js
// ❌ Assumes shared memory exists; no detection, no fallback.
const buffer = new SharedArrayBuffer(width * height * 4);
const pixels = new Uint8ClampedArray(buffer);
const workers = [new Worker("/filter.js"), new Worker("/filter.js")];
for (const w of workers) w.postMessage({ buffer, width, height });

// ❌ Uses process separation as a trust decision.
window.addEventListener("message", (event) => {
  // "It's in another process, so it can't be us" — not a security check.
  applyDashboardConfig(event.data);
});
```

```text
# ❌ Headers: COOP set, COEP not — cross-origin isolation never activates.
Cross-Origin-Opener-Policy: same-origin
```

**What goes wrong:** `partner-a` has no `sandbox`, so it can set `top.location` and navigate the whole dashboard away, or open pop-ups under the user's gesture. `partner-b` combines `allow-scripts` with `allow-same-origin`, which lets the framed document reach its own origin's storage *and* run script — for content you do not control, that pair reconstitutes exactly the authority the sandbox was meant to remove. The `SharedArrayBuffer` constructor throws a `ReferenceError` because only COOP is set; without `require-corp` the document is not cross-origin isolated, and the feature is not merely restricted but absent. The `message` listener accepts data from any frame or window, so any of those partners — or anything they embed — can push arbitrary configuration into the dashboard; the process boundary that prevents memory reads does nothing about messages the page voluntarily listens for.

## Good Example

The same dashboard with explicit embed authority, a real isolation opt-in, and a fallback.

```html
<!-- ✅ Minimum authority per embed, granted explicitly. -->
<iframe
  src="https://partner-a.example/chart"
  sandbox="allow-scripts"
  referrerpolicy="no-referrer"
  loading="lazy"
  title="Partner A revenue chart"></iframe>

<!-- ✅ Needs its own storage? Then it gets its own origin, not allow-same-origin. -->
<iframe
  src="https://partner-b-embed.example/feed"
  sandbox="allow-scripts allow-forms"
  referrerpolicy="no-referrer"
  loading="lazy"
  title="Partner B activity feed"></iframe>
```

```text
# ✅ Both headers, so crossOriginIsolated actually becomes true.
Cross-Origin-Opener-Policy: same-origin
Cross-Origin-Embedder-Policy: require-corp

# ✅ And every first-party subresource opts in to being embedded.
Cross-Origin-Resource-Policy: same-site
```

```js
// ✅ Detect the capability; never assume the headers landed.
export function createPixelBuffer(width, height) {
  const bytes = width * height * 4;

  if (self.crossOriginIsolated && typeof SharedArrayBuffer !== "undefined") {
    return { buffer: new SharedArrayBuffer(bytes), shared: true };
  }

  // Fallback: transferable ArrayBuffer, one worker, ownership moves rather than shares.
  return { buffer: new ArrayBuffer(bytes), shared: false };
}

export async function filterImage(width, height) {
  const { buffer, shared } = createPixelBuffer(width, height);
  const workerCount = shared ? navigator.hardwareConcurrency ?? 2 : 1;
  const workers = Array.from({ length: workerCount }, () => new Worker("/filter.js"));

  try {
    await Promise.all(
      workers.map((w, i) =>
        new Promise((resolve, reject) => {
          w.onmessage = resolve;
          w.onerror = reject;
          // Transfer only when not shared — a SharedArrayBuffer must not be transferred.
          w.postMessage({ buffer, width, height, slice: i, of: workerCount },
                        shared ? [] : [buffer]);
        }),
      ),
    );
  } finally {
    for (const w of workers) w.terminate();   // processes are not free
  }

  return buffer;
}
```

```js
// ✅ Messages are authorized by origin and shape, never by "it came from a frame".
const TRUSTED_EMBED_ORIGINS = new Set([
  "https://partner-a.example",
  "https://partner-b-embed.example",
]);

window.addEventListener("message", (event) => {
  if (!TRUSTED_EMBED_ORIGINS.has(event.origin)) return;
  if (event.source !== chartFrame.contentWindow) return;

  const parsed = EmbedMessage.safeParse(event.data);   // schema validation at the boundary
  if (!parsed.success) return;

  applyDashboardConfig(parsed.data);
});
```

**Why it's better:** each frame now carries the smallest authority that lets it work — `allow-scripts` alone cannot navigate the top-level page or open pop-ups, and the partner that needs storage got a dedicated origin instead of `allow-same-origin`, which keeps the sandbox meaningful. Both isolation headers are present, so `crossOriginIsolated` is actually true and `SharedArrayBuffer` exists; `createPixelBuffer` still feature-detects, so a single missing `Cross-Origin-Resource-Policy` on a CDN asset degrades to a slower single-worker path instead of a `ReferenceError` in production. Workers are terminated in a `finally` block, acknowledging that each one costs real memory in a world where the browser is already spending processes on isolation. And the `message` handler authorizes on origin, on source window, and on message shape — three checks that survive any future change to the browser's process model, because they never depended on it.

## Common Mistakes

See the [Web Platform anti-patterns](../../../anti-patterns/) for the domain catalog. Concept-specific:

### Mistake: `sandbox="allow-scripts allow-same-origin"` on untrusted content

- **Symptom:** A sandboxed embed can still read its own origin's cookies, call its own APIs with credentials, and escape most of what the sandbox appeared to promise.
- **Why it fails:** The combination gives the framed document both script execution and its real origin, which together reconstruct ordinary same-origin authority — including the ability to remove its own sandbox attribute if it can reach a same-origin parent.
- **Fix:** Grant `allow-same-origin` only to content you control. For third parties that need storage, host the embed on a distinct origin.

### Mistake: Setting COOP without COEP and expecting isolation

- **Symptom:** `self.crossOriginIsolated` is `false`, `SharedArrayBuffer` is undefined, and the headers "look right" in DevTools.
- **Why it fails:** Cross-origin isolation requires *both* an opener policy that closes the browsing context group and an embedder policy that vouches for every subresource. Either alone is insufficient.
- **Fix:** Add `Cross-Origin-Embedder-Policy: require-corp`, run it report-only first, and add `Cross-Origin-Resource-Policy` to first-party assets while auditing third-party ones.

### Mistake: Reasoning about isolation in origins rather than sites

- **Symptom:** Two subdomains are assumed to be in separate processes, and a memory-cost or security argument is built on that.
- **Why it fails:** Site Isolation splits on *site* — scheme plus registrable domain — so `a.example.com` and `b.example.com` may share a renderer unless the page opts into origin-keyed agent clusters.
- **Fix:** Use a distinct registrable domain when you need a hard split, or `Origin-Agent-Cluster: ?1` to request origin-level keying.

### Mistake: Treating the process boundary as an access-control boundary

- **Symptom:** A `postMessage` handler, a shared cookie, or an internal API is left unguarded because "that frame is a different process".
- **Why it fails:** Process isolation prevents unauthorized *memory reads*. It says nothing about what a document may legitimately request, message, or navigate.
- **Fix:** Authorize every message by `event.origin` and `event.source`, validate payload shape, and keep server-side authorization independent of browser architecture.

## Checklist

- [ ] Every third-party iframe has an explicit `sandbox` attribute with the minimum token set.
- [ ] `allow-scripts` and `allow-same-origin` are never combined on content you do not control.
- [ ] Untrusted user content is served from a separate registrable domain, not a subdomain.
- [ ] `SharedArrayBuffer` and precise-timer use is guarded by `self.crossOriginIsolated`, with a working fallback.
- [ ] COOP and COEP are both set if isolation is required, and COEP was rolled out report-only first.
- [ ] First-party subresources carry `Cross-Origin-Resource-Policy`; third-party ones are audited or loaded `credentialless`.
- [ ] Pop-up-based auth or payment flows were re-tested after COOP was enabled.
- [ ] `postMessage` handlers check `event.origin`, `event.source`, and payload schema.
- [ ] Per-frame process cost is measured on a low-memory device, not just on a workstation.

## Related Articles

- [Process & Thread Architecture](./process-and-thread-architecture.md) — the process model that isolation partitions.
- [The Main Thread](./) (planned) — what runs inside a single renderer, and why it is still the bottleneck.
- [Same-Origin Policy · Security](../../05-reliability-quality/security/same-origin-policy.md) — the in-process boundary that isolation reinforces rather than replaces.
- [Isolation (COOP/COEP) · Security](../../05-reliability-quality/security/) (planned) — the header-level opt-in in depth.
- **Canonical home:** what "origin" and "site" mean is owned by [Same-Origin Policy · Security](../../05-reliability-quality/security/same-origin-policy.md).

## References

- [Chromium — Site Isolation design](https://www.chromium.org/Home/chromium-security/site-isolation/) — the threat model, the site granularity decision, and the memory cost data.
- [MDN — The iframe sandbox attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe#sandbox) — the full token list and what each one restores.
- [MDN — Cross-Origin-Opener-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Opener-Policy) — browsing context groups and the opener severing rules.
- [web.dev — Why you need cross-origin isolation](https://web.dev/articles/why-coop-coep) — the Spectre background and a practical COEP rollout path.

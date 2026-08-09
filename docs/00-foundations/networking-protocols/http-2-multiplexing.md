---
title: "HTTP/2 Multiplexing"
slug: http-2-multiplexing
description: "How HTTP/2 turns one TCP connection into many concurrent streams, which HTTP/1.1 workarounds it makes obsolete, and why head-of-line blocking survives at the transport layer."
keywords: ["HTTP/2", "multiplexing", "streams", "HPACK", "head-of-line blocking", "domain sharding", "connection coalescing", "server push", "stream priority", "frames"]
part: "00 · Foundations"
domain: "Networking & Protocols"
subcategory: "HTTP"
difficulty: "Foundational"
reading_time_min: 8
priority: "Critical"
status: "Published"
canonical: true
last_reviewed: "2026-08-09"
prerequisites:
  - "HTTP/1.1 Semantics"
related:
  - "HTTP/1.1 Semantics"
  - "HTTP/3 & QUIC"
  - "Methods, Status Codes & Headers"
next:
  - "HTTP/3 & QUIC"
alternatives:
  - "HTTP/3 & QUIC"
  - "Methods, Status Codes & Headers"
common_mistakes:
  - "anti-patterns/README.md#networking-protocols"
  - "#common-mistakes"
frameworks: []
references:
  - { title: "RFC 9113 — HTTP/2", url: "https://www.rfc-editor.org/rfc/rfc9113.html" }
  - { title: "RFC 7541 — HPACK: Header Compression for HTTP/2", url: "https://www.rfc-editor.org/rfc/rfc7541.html" }
  - { title: "MDN — Evolution of HTTP", url: "https://developer.mozilla.org/en-US/docs/Web/HTTP/Evolution_of_HTTP" }
  - { title: "web.dev — Content delivery with HTTP/2", url: "https://web.dev/articles/performance-http2" }
---

# HTTP/2 Multiplexing

> HTTP/2 removed the six-connection limit and every workaround built on top of it. Most codebases deleted the limit from their mental model and kept the workarounds.

**Part:** [00 · Foundations](../) · **Domain:** Networking & Protocols · **Priority:** Critical · **Difficulty:** Foundational · **Reading time:** ~8 min

## TL;DR

HTTP/2 keeps HTTP's semantics — methods, status codes, headers — and replaces its wire format with **binary frames** carried on **streams**, many of which share a single TCP connection. Requests no longer queue behind each other at the protocol layer, so the HTTP/1.1 era practices built to dodge that queue — domain sharding, sprite sheets, inlined assets, aggressive bundling — turn from optimizations into overhead. Header compression via **HPACK** removes most of the per-request byte cost, making fine-grained requests cheap. What HTTP/2 does *not* fix is **transport-level head-of-line blocking**: one lost TCP packet still stalls every stream on that connection, which is precisely the problem HTTP/3 and QUIC exist to solve.

> **Recommendation:** Serve everything over one connection per origin, ship small cacheable chunks instead of megabyte bundles, and delete domain sharding. Reach for HTTP/3 when your users are on lossy networks.

## At a Glance

| | |
| --- | --- |
| **Use when** | Always, over TLS — it is the floor for modern delivery, not an optimization. |
| **Avoid when** | Never intentionally; but do not assume it fixes latency on lossy mobile networks. |
| **Alternatives** | [HTTP/3 & QUIC](#alternative-approaches), [HTTP/1.1](#alternative-approaches) for constrained servers. |
| **Primary risk** | Carrying HTTP/1.1 workarounds forward, where they now cost more than they save. |
| **Maturity** | Stable — universally deployed, superseded at the edge by HTTP/3 rather than replaced. |

## Prerequisites

The semantics stay the same; only the framing changes. Learn what is being framed first.

- [HTTP/1.1 Semantics](./http-1-1-semantics.md) — the request/response model HTTP/2 preserves verbatim.

## Overview

Four concepts carry all of HTTP/2's behavior.

| Concept | Role |
| --- | --- |
| **Connection** | One TCP + TLS connection per origin. Browsers open exactly one and reuse it. |
| **Stream** | An independent, bidirectional sequence of frames with its own identifier. One request/response pair per stream. |
| **Frame** | The smallest unit: `HEADERS`, `DATA`, `SETTINGS`, `RST_STREAM`, `WINDOW_UPDATE`, and others. Frames from different streams interleave freely. |
| **HPACK** | Header compression using a shared dynamic table, so repeated headers cost a few bytes instead of hundreds. |

The critical property is that frames from many streams interleave on the wire. In HTTP/1.1, a connection carries one request at a time; a browser therefore opened up to six connections per origin, and anything beyond six queued in the client. In HTTP/2, a hundred requests can be in flight on one connection, each making progress as frames arrive.

This inverts several long-standing rules:

- **Domain sharding** — splitting assets across `static1.`, `static2.` to win more parallel connections — now *hurts*. Each shard costs a DNS lookup, a TCP handshake, and a TLS negotiation, and fragments congestion control across connections that no longer needed to exist.
- **Bundling everything into one file** was a way to buy one request instead of fifty. With multiplexing, fifty requests are cheap; one giant bundle means a single-byte change invalidates the entire cache entry.
- **Inlining** small images and CSS to save round-trips trades cacheability for a saving that HPACK and multiplexing largely erased.

Browsers also perform **connection coalescing**: if two origins resolve to the same IP and the certificate covers both, they share one connection. Sharding across subdomains on the same certificate may therefore silently collapse back into one connection anyway.

Two features have effectively been retired. **Server push** was removed from Chrome and is deprecated; `103 Early Hints` with `preload` is the supported replacement. **Stream priority** as specified in RFC 7540 was rarely implemented faithfully and is deprecated in RFC 9113 in favor of the newer priority scheme.

## The Problem

A codebase carries its delivery strategy forward for years. Most of the strategies in the wild were designed against a constraint that no longer exists.

```html
<!-- ❌ Sharding for parallelism that HTTP/2 already provides. -->
<link rel="stylesheet" href="https://static1.example.com/app.css" />
<script src="https://static2.example.com/vendor.js"></script>
<img src="https://static3.example.com/hero.jpg" alt="" />
```

Each hostname costs a DNS resolution, a TCP handshake, and a TLS handshake before the first byte of content moves — roughly 2–3 extra round-trips per shard on a cold connection. On a 150 ms RTT mobile link, three shards can add most of a second before anything renders, to solve a queueing problem that disappeared.

The bundling mirror image:

```js
// ❌ One 2.4 MB bundle so there is "only one request".
export default {
  entry: "./src/index.js",
  output: { filename: "app.[contenthash].js" },
  optimization: { splitChunks: false },
};
```

Every deploy changes the hash, so returning users redownload 2.4 MB because one component moved. The request that was saved cost, at HTTP/2 prices, a few hundred compressed header bytes.

And the failure that surprises people who did modernize: on a network with 2% packet loss, an HTTP/2 page can be *slower* than HTTP/1.1 with six connections — because one lost segment stalls all hundred streams, whereas six connections lose only one sixth of the parallelism.

## Why It Matters

Delivery strategy is one of the few frontend decisions that touches every user on every visit, and it is usually set once and inherited for years.

Getting it right compounds: small, content-hashed chunks mean a deploy invalidates 40 KB instead of 2 MB, so returning users pay near-zero for most releases. Fine-grained requests also let the browser prioritize — render-blocking CSS ahead of below-the-fold images — which a single bundle makes impossible because it is one opaque stream.

Getting it wrong is invisible in development, where the RTT is a fraction of a millisecond and packet loss is zero. Sharding, over-bundling, and inlining all look free on localhost and cost real seconds on a mid-tier phone in a congested cell.

The head-of-line caveat matters for the same reason: your users' networks, not your office network, decide whether one connection is a win. Knowing that TCP-level blocking is the residual failure mode is what makes the case for HTTP/3 legible rather than cargo-culted.

## Mental Model

Picture one pipe carrying labelled fragments rather than a queue of whole messages.

```text
  HTTP/1.1 — six connections, one message each, strictly ordered
  conn 1:  [====== app.css ======][==== hero.jpg ====]
  conn 2:  [========= vendor.js =========]
  conn 3:  [== font.woff2 ==]
           ▲ request 7 waits here for a free connection

  HTTP/2 — one connection, interleaved frames
  conn 1:  [H1][H2][H3][D2][D1][D3][D2][D1][D3][D2]...
              │   │   │
              │   │   └─ stream 3: font.woff2
              │   └───── stream 2: vendor.js
              └───────── stream 1: app.css
           ▲ a lost TCP segment stalls ALL of them — head-of-line blocking
```

Three consequences follow directly:

1. **Request count stops being the metric.** Bytes, cacheability, and priority order replace it.
2. **Connection setup becomes the expensive part.** One handshake amortized over hundreds of streams; every extra origin pays it again.
3. **Loss is now a shared fate.** Streams are independent at the HTTP layer and fully dependent at the TCP layer — the gap HTTP/3 closes by moving multiplexing into QUIC, above UDP.

## Best Practices

- **Serve one origin for first-party assets.** Consolidate shards; let coalescing and reuse do the work.
- **Split bundles by change frequency,** not by an arbitrary size target. Vendor code, app shell, and route chunks have different lifetimes and belong in different cache entries.
- **Stop inlining** anything you would otherwise cache, unless it is genuinely tiny and render-blocking-critical.
- **Use `preload` and `103 Early Hints`** instead of server push. Push is deprecated and unsupported in Chrome.
- **Keep `preconnect` for third-party origins you cannot consolidate** — the handshake cost is the one thing multiplexing cannot amortize across origins.
- **Verify the protocol actually in use.** `performance.getEntriesByType("resource")[i].nextHopProtocol` reports `h2`, `h3`, or `http/1.1` per resource; a misconfigured CDN or proxy silently downgrades.
- **Measure on a lossy profile.** Throttle with packet loss, not just bandwidth, or head-of-line blocking will never appear in your numbers.

## Trade-offs

One connection buys amortized setup and unlimited concurrency, and concentrates risk in that connection.

**Advantages**

- Effectively unlimited request concurrency without client-side queueing.
- One handshake per origin instead of up to six.
- HPACK removes the per-request header tax that made small requests expensive.
- Fine-grained resources become cache-friendly and independently prioritizable.

**Disadvantages**

- TCP head-of-line blocking makes every stream share the fate of one lost packet.
- A single connection means a single congestion window; a slow start affects everything.
- Server push and RFC 7540 priorities were deprecated after being widely mis-implemented.
- Server-side cost per connection rises with stream count, and misconfigured limits cause `RST_STREAM` storms.

| Dimension | This approach | Cost / caveat |
| --- | --- | --- |
| Performance | Removes protocol-level queueing entirely | Packet loss degrades all streams together |
| Complexity | Transparent to application code | Build and cache strategy must be rethought |
| Maintainability | Smaller chunks, clearer invalidation | More build configuration to get right |
| Failure behavior | Stream errors isolate cleanly | Connection-level errors take everything down |

## Alternative Approaches

The question is which protocol carries your bytes, and every answer keeps the same HTTP semantics.

| Approach | Best when | Weakness | See |
| --- | --- | --- | --- |
| HTTP/2 over TLS | The default for stable networks | TCP head-of-line blocking | (this article) |
| [HTTP/3 & QUIC](./) (planned) | Lossy or mobile networks; frequent connection migration | UDP blocked on some corporate networks | `HTTP/3 & QUIC · Networking & Protocols` |
| HTTP/1.1 with keep-alive | Legacy proxies, simple internal services | Six-connection ceiling; no header compression | [HTTP/1.1 Semantics](./http-1-1-semantics.md) |
| Fewer, larger bundles | Very high-latency links with no loss | Destroys cache granularity | `Code Splitting · Performance Engineering` |

The practical rule: **HTTP/2 as the floor, HTTP/3 where loss is real, and never HTTP/1.1-era workarounds on either.**

## Bad Example

A build and markup shaped by 2014 constraints, served over HTTP/2.

```html
<!-- ❌ Three origins, three handshakes, for parallelism that already exists. -->
<link rel="stylesheet" href="https://static1.example.com/app.a1b2.css" />
<script src="https://static2.example.com/vendor.c3d4.js" defer></script>
<script src="https://static3.example.com/app.e5f6.js" defer></script>

<!-- ❌ Inlined to "save a request" — now uncacheable and re-sent on every page. -->
<style>/* 18 KB of critical CSS repeated in every HTML response */</style>
<img src="data:image/png;base64,iVBORw0KGgoAAAANSU..." alt="Logo" />
```

```js
// ❌ Everything in one chunk; any change invalidates all of it.
export default {
  entry: "./src/index.js",
  output: {
    filename: "app.[contenthash].js",
    publicPath: "https://static2.example.com/",
  },
  optimization: { splitChunks: false, runtimeChunk: false },
};
```

```js
// ❌ Manual request batching to reduce request count.
const queue = [];
export function loadUser(id) {
  return new Promise((resolve) => {
    queue.push({ id, resolve });
    if (queue.length === 1) setTimeout(flushBatch, 50);   // adds 50 ms to every read
  });
}
```

**What goes wrong:** the three shards force three DNS lookups plus three TCP and TLS handshakes before any asset transfers — on a 150 ms RTT link that is roughly 900 ms of pure setup, spent to avoid a queue HTTP/2 does not have. The inlined CSS and base64 logo are re-downloaded with every HTML response and can never be cached separately, so a returning user pays for them on every navigation. The single unsplit bundle means one line changed in application code invalidates the vendor library bytes too, turning a 20 KB deploy into a 2 MB redownload. And the 50 ms request-batching window adds latency to every read to conserve requests, which HPACK made cost a few hundred bytes each — the batching is now pure delay.

## Good Example

The same app shaped for multiplexed delivery, with the protocol verified rather than assumed.

```html
<!-- ✅ One first-party origin; preconnect only what cannot be consolidated. -->
<link rel="preconnect" href="https://analytics.thirdparty.example" crossorigin />

<link rel="stylesheet" href="/assets/app.a1b2.css" />
<link rel="preload" as="font" href="/assets/inter.woff2" type="font/woff2" crossorigin />

<script type="module" src="/assets/app.e5f6.js"></script>
<img src="/assets/logo.svg" alt="Example" width="120" height="32" />
```

```text
# ✅ 103 Early Hints instead of server push — supported, and cache-aware.
HTTP/2 103 Early Hints
Link: </assets/app.a1b2.css>; rel=preload; as=style
Link: </assets/inter.woff2>; rel=preload; as=font; crossorigin

HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
```

```js
// ✅ Split by change frequency so a deploy invalidates the smallest surface.
export default {
  output: { filename: "[name].[contenthash].js", publicPath: "/assets/" },
  optimization: {
    runtimeChunk: "single",                    // the runtime changes every build; isolate it
    splitChunks: {
      chunks: "all",
      cacheGroups: {
        framework: {                           // rarely changes — long-lived cache entry
          test: /[\\/]node_modules[\\/](react|react-dom|scheduler)[\\/]/,
          name: "framework",
          priority: 40,
        },
        vendor: {                              // changes on dependency bumps only
          test: /[\\/]node_modules[\\/]/,
          name: "vendor",
          priority: 30,
        },
      },
    },
  },
};
```

```js
// ✅ Individual requests, deduplicated rather than delayed.
const inFlight = new Map();

export function loadUser(id, { signal } = {}) {
  const existing = inFlight.get(id);
  if (existing) return existing;

  const promise = fetch(`/api/users/${id}`, { signal })
    .then((res) => {
      if (!res.ok) throw new Error(`User ${id}: ${res.status}`);
      return res.json();
    })
    .finally(() => inFlight.delete(id));

  inFlight.set(id, promise);
  return promise;
}

// ✅ Verify the protocol actually negotiated, per resource.
export function reportProtocolMix() {
  const counts = new Map();
  for (const entry of performance.getEntriesByType("resource")) {
    const proto = entry.nextHopProtocol || "unknown";
    counts.set(proto, (counts.get(proto) ?? 0) + 1);
  }
  if (counts.get("http/1.1")) {
    console.warn("Some resources downgraded to HTTP/1.1", Object.fromEntries(counts));
  }
  return counts;
}
```

**Why it's better:** consolidating to one first-party origin means a single handshake amortized across every asset, and `preconnect` is reserved for the third party that genuinely lives elsewhere — spending a handshake only where multiplexing cannot help. Early Hints achieves what server push was supposed to, without pushing bytes the browser already has cached. Splitting the framework, vendor, and application chunks by change frequency means a typical deploy invalidates the app chunk alone, so returning users download tens of kilobytes instead of megabytes; multiplexing makes the extra requests essentially free. Request deduplication replaces time-based batching, which removes 50 ms from every read while still collapsing duplicate work. And `reportProtocolMix` turns "we're on HTTP/2" from an assumption into a measurement, catching the misconfigured proxy or CDN edge that silently downgrades a subset of assets.

## Common Mistakes

See the [Networking & Protocols anti-patterns](../../../anti-patterns/) for the domain catalog. Concept-specific:

### Mistake: Keeping domain sharding

- **Symptom:** Assets split across `static1`, `static2`, `cdn2` hostnames; waterfall shows repeated DNS, TCP, and TLS segments before content.
- **Why it fails:** Sharding existed to defeat the six-connection-per-origin limit. HTTP/2 has no such limit, so each shard now buys nothing and costs a full connection setup — and may collapse back into one connection anyway via coalescing.
- **Fix:** Consolidate to one first-party origin; keep `preconnect` only for third parties you cannot host yourself.

### Mistake: Assuming HTTP/2 fixes head-of-line blocking

- **Symptom:** A page performs worse on a lossy mobile network after consolidating onto a single connection.
- **Why it fails:** HTTP/2 removes blocking at the HTTP layer, not at the TCP layer. One lost segment stalls delivery of every stream until retransmission completes.
- **Fix:** Enable HTTP/3, which multiplexes above UDP so loss affects only the stream whose packet was lost; measure with a loss-enabled network profile.

### Mistake: Still optimizing for request count

- **Symptom:** Time-based request batching, sprite sheets, base64-inlined images, and a single unsplit bundle.
- **Why it fails:** Each of these trades cacheability or latency for a reduction in request count, which HPACK and multiplexing made close to free. The trade no longer pays.
- **Fix:** Optimize bytes transferred and cache-hit rate instead; deduplicate requests rather than delaying them.

### Mistake: Relying on server push

- **Symptom:** Push configured at the CDN; assets arrive that the browser already had cached, and Chrome ignores it entirely.
- **Why it fails:** The server cannot know the client's cache state, so push routinely wastes bandwidth. Chrome removed support and RFC 9113 discourages it.
- **Fix:** Use `103 Early Hints` with `rel=preload`, which lets the browser apply its own cache check.

## Checklist

- [ ] First-party assets are served from a single origin; sharding has been removed.
- [ ] `nextHopProtocol` is checked in the field to confirm `h2` or `h3` rather than assumed.
- [ ] Bundles are split by change frequency, with the runtime isolated in its own chunk.
- [ ] Inlined CSS and base64 images have been re-evaluated against cacheability.
- [ ] Server push is replaced by `preload` and, where supported, `103 Early Hints`.
- [ ] `preconnect` is present for unavoidable third-party origins only.
- [ ] Request batching by timer has been replaced with deduplication.
- [ ] Performance was measured on a network profile that includes packet loss, not only bandwidth throttling.
- [ ] HTTP/3 is enabled at the edge for users on mobile networks.

## Related Articles

- [HTTP/1.1 Semantics](./http-1-1-semantics.md) — the semantics HTTP/2 preserves and the connection model it replaces.
- [HTTP/3 & QUIC](./) (planned) — moving multiplexing below HTTP to eliminate transport head-of-line blocking.
- [Methods, Status Codes & Headers](./) (planned) — the semantic layer that is identical across all three versions.
- [Code Splitting · Performance Engineering](../../05-reliability-quality/performance/code-splitting.md) — how to choose chunk boundaries once requests are cheap.
- [Resource Prefetch & Preload · Performance Engineering](../../05-reliability-quality/performance/resource-prefetch-and-preload.md) — the supported replacement for server push.
- **Canonical home:** caching semantics are owned by `HTTP & CDN Caching Model · Networking & Protocols`.

## References

- [RFC 9113 — HTTP/2](https://www.rfc-editor.org/rfc/rfc9113.html) — the current specification, including the deprecation of RFC 7540 priorities.
- [RFC 7541 — HPACK](https://www.rfc-editor.org/rfc/rfc7541.html) — the header compression scheme that makes small requests cheap.
- [MDN — Evolution of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Evolution_of_HTTP) — how the connection model changed across versions.
- [web.dev — Content delivery with HTTP/2](https://web.dev/articles/performance-http2) — which HTTP/1.1 practices to retire and why.

---
title: "Storage Quotas & Eviction"
slug: storage-quotas-and-eviction
description: "How much client storage you actually get, how the browser decides to take it back, and why 'persisted' is a request rather than a guarantee."
keywords: ["storage quota", "eviction", "StorageManager", "navigator.storage.estimate", "QuotaExceededError", "persistent storage", "best-effort storage", "origin storage", "storage pressure"]
part: "00 · Foundations"
domain: "Browser APIs"
subcategory: "Storage"
difficulty: "Foundational"
reading_time_min: 8
priority: "Critical"
status: "Published"
canonical: true
last_reviewed: "2026-08-09"
prerequisites:
  - "Web Storage"
related:
  - "Web Storage"
  - "IndexedDB"
  - "The Cache Storage API"
  - "Cookies & Partitioned Storage"
next:
  - "Intersection Observer"
alternatives:
  - "IndexedDB"
  - "The Cache Storage API"
  - "Cookies & Partitioned Storage"
common_mistakes:
  - "anti-patterns/README.md#browser-apis"
  - "#common-mistakes"
frameworks: []
references:
  - { title: "W3C — Storage Standard", url: "https://storage.spec.whatwg.org/" }
  - { title: "MDN — Storage quotas and eviction criteria", url: "https://developer.mozilla.org/en-US/docs/Web/API/Storage_API/Storage_quotas_and_eviction_criteria" }
  - { title: "MDN — StorageManager", url: "https://developer.mozilla.org/en-US/docs/Web/API/StorageManager" }
  - { title: "MDN — QuotaExceededError", url: "https://developer.mozilla.org/en-US/docs/Web/API/DOMException#quotaexceedederror" }
---

# Storage Quotas & Eviction

> Client storage is a loan, not a deposit. Every byte you write can be taken back, and the only question your code gets to answer is what happens when it is.

**Part:** [00 · Foundations](../) · **Domain:** Browser APIs · **Priority:** Critical · **Difficulty:** Foundational · **Reading time:** ~8 min

## TL;DR

Browsers pool IndexedDB, Cache Storage, Web Storage, and the origin private file system into a single per-origin **quota**, sized as a fraction of free disk rather than a fixed number. When the disk fills, the browser **evicts** whole origins — not individual records — starting with the least recently used, and it does so without asking. `navigator.storage.estimate()` tells you roughly where you stand; `navigator.storage.persist()` asks to be moved out of the best-effort pool, and the browser may simply say no. Every write can therefore fail with `QuotaExceededError`, and every read can come back empty on a profile that has never been cleared by the user.

> **Recommendation:** Treat client storage as a cache that happens to survive reloads. Request persistence when data loss is user-visible, always handle `QuotaExceededError`, and keep the server as the source of truth for anything you cannot regenerate.

## At a Glance

| | |
| --- | --- |
| **Use when** | You need to size a client cache, ship an offline mode, or store user-generated drafts locally. |
| **Avoid when** | The data is the only copy and losing it is unacceptable — that belongs on a server. |
| **Alternatives** | [IndexedDB](#alternative-approaches), [Cache Storage](#alternative-approaches), [Cookies](#alternative-approaches), server persistence. |
| **Primary risk** | Silent whole-origin eviction, discovered as "the app forgot everything" rather than as an error. |
| **Maturity** | Stable — the Storage Standard is universally implemented; the exact numbers are deliberately unspecified. |

## Prerequisites

Start with the simplest store, because its 5 MB ceiling is the first quota most engineers meet.

- [Web Storage](./web-storage.md) — the synchronous store with its own separate, much smaller limit.

## Overview

**Storage quota** is the amount of disk an origin may consume across the storage APIs the browser groups together. **Eviction** is the process by which the browser reclaims that disk when it runs short. Both are deliberately unspecified in exact numbers, because they depend on the device, the free space, and the browser's own heuristics.

The APIs that share the pooled quota:

| API | Counts against quota | Notes |
| --- | --- | --- |
| [IndexedDB](./indexeddb.md) | Yes | Usually the largest consumer. |
| [Cache Storage](./the-cache-storage-api.md) | Yes | Response bodies plus headers. |
| Origin private file system | Yes | Same pool, different access model. |
| Web Storage (`localStorage`) | Separate, ~5 MB | Reported by `estimate()` in some browsers, capped independently. |
| [Cookies](./cookies-and-partitioned-storage.md) | No | Governed by their own per-domain count and size limits. |

Two properties matter more than the numbers. First, quota is **per origin**, so `https://app.example.com` and `https://www.example.com` have separate budgets, and a third-party frame in a partitioned context gets its own again. Second, eviction is **all-or-nothing per origin**: the browser does not delete your least-important record, it deletes your origin's storage in one go.

Storage sits in one of two buckets:

- **Best-effort** — the default. Eligible for eviction under storage pressure, and cleared by "clear browsing data" without a separate prompt.
- **Persisted** — granted via `navigator.storage.persist()`. Exempt from automatic eviction under pressure; still removable by the user explicitly.

Whether a `persist()` request is granted is a browser policy decision, not an API contract. Chromium-based browsers grant it based on engagement signals — installed as a PWA, bookmarked, high site engagement, notification permission — and may resolve `false` with no user-visible prompt at all. Firefox prompts the user. Safari grants it under its own heuristics and additionally caps unused origins with a seven-day cleanup for script-writable storage on some configurations.

## The Problem

Code that assumes storage is durable fails in ways that never appear in development, because a developer's machine has free disk and a profile that is never under pressure.

```js
// ❌ Writes assume unbounded space and permanent retention.
async function cacheReport(id, rows) {
  const db = await openDb();
  const tx = db.transaction("reports", "readwrite");
  tx.objectStore("reports").put({ id, rows, cachedAt: Date.now() });
}

// ❌ Reads assume what was written is still there.
async function loadReport(id) {
  const db = await openDb();
  const tx = db.transaction("reports", "readonly");
  return request(tx.objectStore("reports").get(id));  // undefined after eviction
}
```

Three failures hide in six lines. The write has no bound, so a user who opens a thousand reports fills the origin's quota and the transaction aborts with `QuotaExceededError` — which is never caught here, because the failure surfaces on `tx.onabort` rather than on the `put` call. The read treats `undefined` as an error rather than as the expected result of eviction, so the UI shows a broken state instead of refetching. And nothing ever deletes old entries, so the cache grows monotonically until the browser deletes all of it at once.

The user-facing symptom is distinctive: everything works for weeks, then one day the app "forgets" every draft, every setting, and every cached page simultaneously — because the browser evicted the origin, not a record.

## Why It Matters

Quota is the boundary between a cache and a database, and getting it wrong costs on both sides.

Under-using it means shipping an app that refetches everything on every visit, paying network cost and latency the platform would have given you for free. Over-using it means `QuotaExceededError` on a device with a nearly full disk — which describes a large share of low-end Android phones, where free space routinely sits in the low hundreds of megabytes and quota shrinks accordingly.

The correctness stakes are higher than the performance ones. If your app stores the only copy of user work — an unsent message, an offline form, a drawing — then eviction is data loss with no error, no retry, and no way to explain it to the user afterwards. Deciding deliberately which data is regenerable and which is not is the actual engineering decision this article documents; the API surface is small enough to fit on a card.

## Mental Model

Think of the origin's storage as a single bucket with three numbers attached and one rule.

```text
             quota  ────────────────────────────────────────┐
                                                            │
  usage  ──────────────────────────┐                        │
                                   │                        │
  ┌────────────────────────────────┴────────────────────────┴───┐
  │  IndexedDB  │  Cache Storage  │  OPFS  │      headroom       │
  └─────────────────────────────────────────────────────────────┘
       best-effort  ──►  evicted whole, LRU first, under pressure
       persisted    ──►  skipped by automatic eviction
```

- **`usage`** — bytes currently attributed to the origin, padded by the browser so cross-origin size probing cannot leak information. Do not treat it as byte-exact.
- **`quota`** — the ceiling, typically a percentage of free disk (Chromium has used around 60% of total disk as a global pool with per-origin sub-limits; Firefox uses a similar proportional scheme). Numbers change between versions; never hard-code them.
- **Pressure** — when the device runs low, the browser evicts best-effort origins in least-recently-used order until it has room.

The rule that follows: **your job is not to avoid eviction, it is to survive it.** Design the read path so a cold, empty store is an ordinary state rather than an error, and eviction becomes a performance event instead of a bug report.

## Best Practices

- **Measure before you write.** Call `navigator.storage.estimate()` and refuse writes that would push you past a self-imposed fraction of quota — 80% is a workable default — rather than discovering the ceiling by hitting it.
- **Bound every cache.** Give each store a maximum entry count or byte budget and evict your own least-recently-used records. Self-eviction is the only kind you control.
- **Catch `QuotaExceededError` explicitly.** In IndexedDB it arrives on the transaction's `abort` event as `tx.error`; in Cache Storage it rejects the `put()` promise; in `localStorage` it throws synchronously.
- **Request persistence where loss is user-visible,** and log the boolean result. Never branch on the assumption that it was granted.
- **Store regenerable and irreplaceable data separately.** Different stores, different budgets, different eviction policies — so trimming the cache never touches the drafts.
- **Treat a missing record as a cache miss,** not a failure. The read path should refetch, not throw.
- **Test on a full disk.** A device with 200 MB free is a supported configuration, and the only way to see your quota path run is to reproduce it.

## Trade-offs

Caching more locally buys latency and offline capability at the cost of a larger, more fragile failure surface.

**Advantages**

- Instant reads, offline capability, and reduced server load for data that would otherwise be refetched.
- Quota scales with the device, so capable machines get a bigger cache with no configuration.
- Persisted storage genuinely removes automatic eviction for the data that needs it.

**Disadvantages**

- Every write can fail, and the failure mode differs per API.
- Eviction is whole-origin and silent, so partial-recovery strategies do not exist.
- `estimate()` is padded and coarse, so precise budgeting is impossible by design.
- `persist()` grants depend on browser heuristics you cannot query in advance or influence directly.

| Dimension | This approach | Cost / caveat |
| --- | --- | --- |
| Performance | Local reads avoid network latency entirely | Quota checks add an async call to the write path |
| Complexity | A bounded cache is ~30 lines | Every store now needs a budget and a trim policy |
| Maintainability | Explicit budgets document intent | Budgets drift from reality as payloads grow |
| Failure behavior | Cache misses degrade to refetch | Silent eviction is invisible without telemetry |

## Alternative Approaches

Quota is shared, so the real choice is *which* store to spend it in — or whether to spend it at all.

| Approach | Best when | Weakness | See |
| --- | --- | --- | --- |
| Bounded local cache with quota checks | Regenerable data you want offline or fast | You own the trim policy | (this article) |
| [IndexedDB](./indexeddb.md) unbounded | Small, well-understood datasets | Grows until eviction takes it all | `IndexedDB · Browser APIs` |
| [The Cache Storage API](./the-cache-storage-api.md) | Whole HTTP responses, service-worker driven | Only models Request/Response pairs | `The Cache Storage API · Browser APIs` |
| [Cookies](./cookies-and-partitioned-storage.md) | The server must see the value | ~4 KB, sent on every request, outside the quota pool | `Cookies & Partitioned Storage · Browser APIs` |
| Server persistence | The data is irreplaceable | Requires network and an account model | `Cache Invalidation · Data & Server State` |
| In-memory only | The value need not survive reload | Lost on navigation | `Categories of State · State Management` |

The practical rule: **regenerable → local cache with a budget; irreplaceable → server, with local storage as an accelerator.**

## Bad Example

A realistic offline cache that grows without limit and treats storage as durable.

```js
// ❌ No budget, no quota check, no error handling, no eviction policy.
const CACHE_STORE = "reports";

export async function cacheReport(id, rows) {
  const db = await openDb();
  const tx = db.transaction(CACHE_STORE, "readwrite");
  tx.objectStore(CACHE_STORE).put({ id, rows, cachedAt: Date.now() });
  // No await on tx.oncomplete, so an abort from QuotaExceededError is invisible.
}

export async function loadReport(id) {
  const db = await openDb();
  const tx = db.transaction(CACHE_STORE, "readonly");
  const row = await request(tx.objectStore(CACHE_STORE).get(id));
  if (!row) throw new Error("Report not found in cache");   // ❌ eviction becomes an error
  return row.rows;
}

// ❌ Drafts — the user's own unsaved work — share the store with disposable cache.
export async function saveDraft(draft) {
  const db = await openDb();
  const tx = db.transaction(CACHE_STORE, "readwrite");
  tx.objectStore(CACHE_STORE).put({ id: `draft:${draft.id}`, ...draft });
}

// ❌ localStorage write with no guard.
export function rememberLastView(view) {
  localStorage.setItem("lastView", JSON.stringify(view));   // throws at ~5 MB
}
```

**What goes wrong:** `cacheReport` never observes the transaction's outcome, so when the origin hits quota the transaction aborts and the write is silently lost — the UI still shows "cached". Nothing bounds the store, so after enough usage the origin exceeds its share and the browser evicts *everything*, including the drafts that share the same store, because eviction is per origin rather than per record. `loadReport` converts that eviction into a thrown error rather than a refetch, turning a recoverable cache miss into a broken screen. And `rememberLastView` writes to `localStorage` synchronously with no `try`, so a full store throws `QuotaExceededError` straight through whatever click handler called it, breaking unrelated UI.

## Good Example

The same feature with a quota check, a bounded store, separated durability tiers, and errors that mean something.

```js
// ✅ One place that knows the budget and the current usage.
const SOFT_LIMIT = 0.8;          // never consume more than 80% of quota

export async function storageHeadroom() {
  if (!navigator.storage?.estimate) {
    return { usage: 0, quota: Infinity, ratio: 0, supported: false };
  }
  const { usage = 0, quota = 0 } = await navigator.storage.estimate();
  return { usage, quota, ratio: quota ? usage / quota : 0, supported: true };
}

export async function hasRoomFor(bytes) {
  const { usage, quota, supported } = await storageHeadroom();
  if (!supported) return true;                       // can't measure, don't block
  return usage + bytes < quota * SOFT_LIMIT;
}

// ✅ Ask for persistence once, at a point where the user has shown intent.
export async function requestDurableStorage() {
  if (!navigator.storage?.persist) return false;
  if (await navigator.storage.persisted()) return true;
  const granted = await navigator.storage.persist();
  if (!granted) {
    console.info("Storage is best-effort; drafts may be evicted under pressure.");
  }
  return granted;
}
```

```js
// ✅ Separate stores: "cache" is disposable, "drafts" is user work.
const CACHE = "report-cache";
const DRAFTS = "drafts";
const MAX_CACHE_ENTRIES = 200;

export async function cacheReport(id, rows) {
  const approxBytes = JSON.stringify(rows).length * 2;   // UTF-16, close enough
  if (!(await hasRoomFor(approxBytes))) {
    await trimCache(MAX_CACHE_ENTRIES / 2);
  }

  const db = await openDb();
  const tx = db.transaction(CACHE, "readwrite");
  tx.objectStore(CACHE).put({ id, rows, lastUsed: Date.now() });

  try {
    await txDone(tx);
  } catch (err) {
    if (err?.name === "QuotaExceededError") {
      await trimCache(MAX_CACHE_ENTRIES / 2);           // make room, drop this write
      return;                                            // caching is optional by definition
    }
    throw err;
  }
}

// ✅ Our own LRU eviction, so the browser's never has to run.
async function trimCache(keep) {
  const db = await openDb();
  const tx = db.transaction(CACHE, "readwrite");
  const index = tx.objectStore(CACHE).index("by_lastUsed");

  let remaining = await request(tx.objectStore(CACHE).count());
  const cursorReq = index.openCursor();                  // ascending: oldest first

  cursorReq.onsuccess = () => {
    const cursor = cursorReq.result;
    if (!cursor || remaining <= keep) return;
    cursor.delete();
    remaining -= 1;
    cursor.continue();
  };

  await txDone(tx);
}
```

```js
// ✅ A cache miss is a normal state, not an error.
export async function loadReport(id, { fetchReport }) {
  const db = await openDb();
  const tx = db.transaction(CACHE, "readwrite");
  const store = tx.objectStore(CACHE);
  const row = await request(store.get(id));

  if (row) {
    store.put({ ...row, lastUsed: Date.now() });         // keep LRU honest
    await txDone(tx);
    return row.rows;
  }

  const rows = await fetchReport(id);                     // evicted or never cached
  await cacheReport(id, rows);
  return rows;
}

// ✅ Synchronous store, guarded — and never used for anything that matters.
export function rememberLastView(view) {
  try {
    localStorage.setItem("lastView", JSON.stringify(view));
  } catch (err) {
    if (err?.name !== "QuotaExceededError") throw err;
    localStorage.removeItem("lastView");                  // best-effort, drop it
  }
}
```

**Why it's better:** `hasRoomFor` turns quota from a cliff into a threshold, so the common path never reaches `QuotaExceededError` at all — and when it does, `cacheReport` handles it by trimming rather than propagating, because a failed cache write is not a failed operation. Splitting `CACHE` from `DRAFTS` means the trim policy can be aggressive on disposable data without ever touching user work, and requesting persistence protects the store that actually needs it. The LRU index lets eviction run in one cursor pass instead of loading every record. `loadReport` treats a missing row as a cache miss and refetches, so an evicted origin costs one network round-trip instead of a broken screen — and it refreshes `lastUsed` on read, which is what makes the LRU ordering meaningful. Finally, `rememberLastView` wraps the synchronous write so a full `localStorage` cannot break the click handler that triggered it.

## Common Mistakes

See the [Browser APIs anti-patterns](../../../anti-patterns/) for the domain catalog. Concept-specific:

### Mistake: Storing irreplaceable data in best-effort storage

- **Symptom:** Users report that unsent drafts, offline notes, or queued actions vanished, with no error in telemetry.
- **Why it fails:** Best-effort storage is evicted whole-origin under disk pressure, with no event, no prompt, and no partial recovery.
- **Fix:** Call `navigator.storage.persist()` for stores that hold user work, sync to the server as soon as connectivity allows, and treat local persistence as an accelerator rather than the record.

### Mistake: Treating `estimate()` as byte-exact

- **Symptom:** A budget calculation that "should" fit still throws `QuotaExceededError`, or a store reports usage that jumps in suspicious round numbers.
- **Why it fails:** Browsers pad and round `usage` deliberately so that a page cannot measure another origin's storage or fingerprint the device by probing exact sizes.
- **Fix:** Use `estimate()` for coarse decisions — a soft limit, a warning threshold — and always keep the `QuotaExceededError` path working.

### Mistake: Letting a cache grow without a bound

- **Symptom:** Storage usage climbs steadily over months, then drops to zero overnight.
- **Why it fails:** Without self-eviction the origin eventually crosses the browser's threshold, and the browser's eviction granularity is the entire origin.
- **Fix:** Give every cache a maximum entry count or byte budget, index by last use, and trim on write.

### Mistake: Assuming `QuotaExceededError` arrives where the write happened

- **Symptom:** A `try`/`catch` around an IndexedDB `put()` never fires, yet data is missing.
- **Why it fails:** `put()` only queues the request; the quota failure aborts the *transaction*, surfacing on `tx.onabort` as `tx.error`.
- **Fix:** Await transaction completion and inspect `tx.error`; for Cache Storage, catch the rejected `put()` promise; for Web Storage, catch the synchronous throw.

## Checklist

- [ ] Every persistent store has a documented maximum entry count or byte budget.
- [ ] Writes check headroom with `navigator.storage.estimate()` against a soft limit before committing large payloads.
- [ ] `QuotaExceededError` is handled at the right place for each API — transaction abort, rejected promise, or synchronous throw.
- [ ] Disposable cache data and irreplaceable user data live in separate stores with separate policies.
- [ ] `navigator.storage.persist()` is requested for stores holding user work, and the result is logged rather than assumed.
- [ ] A missing record is handled as a cache miss that refetches, never as a thrown error.
- [ ] Stores are indexed by last-used time so self-eviction is a single cursor pass.
- [ ] The app has been exercised on a device or profile with very little free disk.
- [ ] Telemetry records eviction-shaped events — an unexpectedly empty store on a returning user — so silent loss becomes visible.

## Related Articles

- [Web Storage](./web-storage.md) — the separate ~5 MB synchronous budget and its own quota errors.
- [IndexedDB](./indexeddb.md) — the largest consumer of the pooled quota, and where transaction aborts surface.
- [The Cache Storage API](./the-cache-storage-api.md) — response-level storage that shares the same budget.
- [Cookies & Partitioned Storage](./cookies-and-partitioned-storage.md) — the one store governed by its own limits rather than the quota pool.
- [Cache Invalidation · Data & Server State](../../03-application-architecture/data-server-state/cache-invalidation.md) — deciding when cached data is wrong, as opposed to gone.
- **Canonical home:** what "origin" means for storage isolation is owned by [Same-Origin Policy · Security](../../05-reliability-quality/security/same-origin-policy.md).

## References

- [W3C — Storage Standard](https://storage.spec.whatwg.org/) — the normative model for buckets, quota, and eviction.
- [MDN — Storage quotas and eviction criteria](https://developer.mozilla.org/en-US/docs/Web/API/Storage_API/Storage_quotas_and_eviction_criteria) — per-browser limits and the heuristics behind persistence grants.
- [MDN — StorageManager](https://developer.mozilla.org/en-US/docs/Web/API/StorageManager) — `estimate()`, `persist()`, and `persisted()` reference.
- [MDN — QuotaExceededError](https://developer.mozilla.org/en-US/docs/Web/API/DOMException#quotaexceedederror) — where the error surfaces for each storage API.

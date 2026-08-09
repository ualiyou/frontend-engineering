---
title: "Ephemeral vs Persistent State"
slug: ephemeral-vs-persistent-state
description: "Deciding how long each piece of state should live — the render, the session, the device, or the account — and where that lifetime is enforced."
keywords: ["ephemeral state", "persistent state", "state lifetime", "session state", "state hydration", "localStorage state", "URL state", "state restoration", "bfcache", "schema migration"]
part: "03 · Application Architecture"
domain: "State Management"
subcategory: "State Taxonomy"
difficulty: "Intermediate"
reading_time_min: 15
priority: "Critical"
status: "Published"
canonical: true
last_reviewed: "2026-08-09"
prerequisites:
  - "Categories of State"
related:
  - "Categories of State"
  - "Server vs Client State"
  - "UI vs Domain State"
next:
  - "Local State"
alternatives:
  - "Server vs Client State"
  - "UI vs Domain State"
common_mistakes:
  - "anti-patterns/README.md#state-management"
  - "#common-mistakes"
frameworks: []
references:
  - { title: "MDN — Window.sessionStorage", url: "https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage" }
  - { title: "MDN — Back/forward cache", url: "https://developer.mozilla.org/en-US/docs/Glossary/bfcache" }
  - { title: "MDN — History.state", url: "https://developer.mozilla.org/en-US/docs/Web/API/History/state" }
  - { title: "web.dev — Page lifecycle API", url: "https://developer.chrome.com/docs/web-platform/page-lifecycle-api" }
---

# Ephemeral vs Persistent State

> Every piece of state has a lifetime whether you chose one or not. The bugs come from state that outlives its meaning, and from state that dies before the user is done with it.

**Part:** [03 · Application Architecture](../) · **Domain:** State Management · **Priority:** Critical · **Difficulty:** Intermediate · **Reading time:** ~15 min

## TL;DR

State lifetime is a spectrum with five useful stops: **render**, **mount**, **navigation**, **session**, and **account**. Ephemeral state — a hover flag, an open dropdown, an in-flight animation — should die with the component and must never be written anywhere durable. Persistent state — a draft, a chosen theme, a wizard's progress — must survive a reload and therefore needs a storage medium, a serialization format, a version, and a restoration path. The common failure is putting state one stop too far in either direction: a modal that reopens after reload because someone persisted `isOpen`, or a half-written comment that vanishes because nobody persisted the draft.

> **Recommendation:** Default every value to the shortest lifetime that works, and promote deliberately. Write down which stop each value occupies; the medium follows from the lifetime, not the other way round.

## At a Glance

| | |
| --- | --- |
| **Use when** | Designing any new state, or auditing an app where "it forgot my work" and "it remembered something weird" both appear in feedback. |
| **Avoid when** | The value belongs to the server — that is a different axis entirely. |
| **Alternatives** | [Server vs Client State](#alternative-approaches) for ownership; [UI vs Domain State](#alternative-approaches) for semantics. |
| **Primary risk** | Persisted state that outlives its schema, restoring a shape the current code cannot read. |
| **Maturity** | Stable — the media (URL, `sessionStorage`, IndexedDB) are all long-settled. |

## Prerequisites

Lifetime is one axis of a taxonomy; start with the taxonomy.

- [Categories of State](./categories-of-state.md) — the full classification this article refines.

## Overview

Five lifetimes, each with a natural medium.

| Lifetime | Survives | Natural medium | Example |
| --- | --- | --- | --- |
| **Render** | Nothing — recomputed each render | A local `const`, derived value | Filtered list, formatted price |
| **Mount** | Re-renders, not unmount | Component state, a ref | Dropdown open, hover, focus ring |
| **Navigation** | Route changes within the app | URL params, router state, `history.state` | Search query, filters, current tab, pagination |
| **Session** | Reload and back/forward, not a new tab | `sessionStorage`, `history.state` | Wizard progress, scroll position, unsent form |
| **Account / device** | Everything, including new devices (account) or just this device | Server, IndexedDB, `localStorage`, cookies | Theme, drafts, feature opt-ins, consent |

Two things distinguish a persistent value from an ephemeral one beyond duration:

**It needs a schema.** Anything written to storage will be read back by a future version of your code. That makes it a serialization format with a compatibility requirement, which means a version field and a migration path — the same discipline as a database column, applied to a value someone added in an afternoon.

**It needs a restoration story.** Restoring is not just reading. A restored value may be stale (a draft for a deleted document), invalid (a filter for a removed field), unauthorized (another user's data on a shared device), or simply unwanted (a modal the user closed by reloading).

The medium also decides visibility. URL state is shareable and bookmarkable; `sessionStorage` is per-tab and invisible to other tabs; `localStorage` is shared across tabs of the same origin and fires `storage` events in the others; server state follows the account to a new device. Choosing a medium is therefore choosing who else can see the value, not only how long it lives.

One platform detail matters for the "session" tier: the **back/forward cache** (bfcache) freezes a whole page rather than tearing it down, so returning via the back button restores in-memory state with no work at all — but only if the page is bfcache-eligible, and never across a full reload.

## The Problem

Lifetime is usually inherited from whatever storage API someone reached for first, and the result is state at the wrong stop in both directions.

```ts
// ❌ Ephemeral UI state, persisted forever.
useEffect(() => {
  localStorage.setItem("ui", JSON.stringify({
    isSidebarOpen, isModalOpen, activeTooltipId, isDragging,
  }));
}, [isSidebarOpen, isModalOpen, activeTooltipId, isDragging]);
```

The user closes a modal by reloading the page — a universal instinct — and the modal comes back. `isDragging` can persist as `true` if the tab is closed mid-drag, leaving the app in a drag state on next visit with no pointer to end it. Every one of these values is meaningless outside the mount that created it.

The opposite failure loses real work:

```tsx
// ❌ A 2,000-word draft that exists only in component state.
function CommentEditor({ postId }) {
  const [body, setBody] = useState("");
  return <textarea value={body} onChange={(e) => setBody(e.target.value)} />;
}
```

An accidental navigation, a crashed tab, or an OS-level app kill on mobile discards it. There is no error, no undo, and no way to explain it.

And the schema failure, which appears months later:

```ts
// ❌ Written by v1, read by v3, with no version marker.
const saved = JSON.parse(localStorage.getItem("filters") ?? "{}");
setFilters(saved);   // { status: "open" } — but v3 expects { statuses: ["open"] }
```

The stored shape is from a release two quarters ago. `saved.statuses` is `undefined`, `.map` throws, and the app white-screens on load for exactly the users who have been around longest — the ones least likely to be in your test cohort, and most likely to matter.

## Why It Matters

Lifetime errors are asymmetric: one direction annoys, the other destroys.

**Over-persisting** produces uncanny behavior. The app remembers something the user expected it to forget — a filter from three weeks ago, a dismissed banner reappearing, a modal that survives a reload. Each instance is small; collectively they read as "this app is broken" because the mental model users have (reload resets things) is being violated.

**Under-persisting** loses work. A draft, a partially completed multi-step form, an offline queue of actions. On mobile this is routine rather than exceptional: the OS reclaims a backgrounded tab, and everything in memory is gone. Users do not report it as a bug; they stop trusting the app with anything long.

**Un-versioned persistence** breaks the app entirely, and does so for your longest-tenured users. A stored shape from an old release is a payload from an untrusted source as far as the current code is concerned — it deserves the same validation as an API response, and almost never gets it.

There is also a privacy dimension. `localStorage` is not cleared on logout unless you clear it, is readable by any script on the origin, and on shared devices exposes one user's drafts to the next. Deciding lifetime is therefore partly a security decision about how long data should remain readable on a device you do not control.

## Mental Model

Place every value on the ladder, then pick the medium that matches the rung.

```text
  lifetime ▲
           │
  account  │  server (source of truth)          theme, consent, saved views
           │  ─────────────────────────────────────────────────────────────
  device   │  IndexedDB / localStorage          drafts, offline queue, prefs
           │  ─────────────────────────────────────────────────────────────
  session  │  sessionStorage / history.state    wizard step, scroll, unsent form
           │  ─────────────────────────────────────────────────────────────
  nav      │  URL search params                 query, filters, tab, page
           │  ─────────────────────────────────────────────────────────────
  mount    │  component state / ref             open, hovered, focused, dragging
           │  ─────────────────────────────────────────────────────────────
  render   │  a plain const                     derived, formatted, filtered
           └────────────────────────────────────────────────────────────────►

  Rule: start at the bottom. Promote only when a concrete scenario demands it,
        and name the scenario ("survives an accidental reload") in the commit.
```

Three questions settle nearly every case:

1. **If the user reloads, should this survive?** No → mount or render. Yes → keep going.
2. **Should the user be able to send this state to a colleague as a link?** Yes → the URL. This one question resolves most filter and tab state.
3. **Should this survive on a different device?** Yes → the server. Anything else is a cache of it.

## Best Practices

- **Default to the shortest lifetime.** Promotion should be a deliberate, reviewable change, not the incidental result of importing a persistence helper.
- **Put navigation state in the URL.** Filters, sort, tab, page, and query belong there — it makes them shareable, bookmarkable, and restored by the back button for free.
- **Version every persisted shape.** Store `{ v: 2, data }`, validate on read with a schema, and migrate or discard on mismatch. Never `JSON.parse` straight into state.
- **Namespace and scope storage keys** by user and app version: `app:v2:user:${userId}:drafts`. Clear the namespace on logout.
- **Prefer `sessionStorage` for tab-scoped recovery.** It disappears when the tab closes, which is usually exactly the semantics wanted for wizard progress and scroll restoration.
- **Save drafts on a timer and on `visibilitychange`,** not on `beforeunload` — the latter is unreliable on mobile and blocks bfcache eligibility.
- **Treat restored state as untrusted input.** Validate it, check it against current data (does that document still exist?), and degrade to a default rather than throwing.
- **Give the user a way to discard.** A "restore your draft?" prompt beats silent restoration, which can be worse than losing the data when the restored content is stale.

## Trade-offs

Persistence buys resilience and charges in schema maintenance, privacy exposure, and restoration complexity.

**Advantages**

- Work survives reloads, crashes, and mobile tab reclamation.
- URL-persisted state makes application views shareable and linkable.
- Restoration removes the "start over" penalty that drives abandonment in long flows.

**Disadvantages**

- Every persisted shape becomes a compatibility surface across releases.
- Storage is finite and evictable, so persistence is best-effort unless the server holds the truth.
- Data lingers on shared devices after logout unless explicitly cleared.
- Restoration paths are hard to test — they require the "old data, new code" combination that CI rarely constructs.

| Dimension | This approach | Cost / caveat |
| --- | --- | --- |
| Performance | Reads are fast; writes can be throttled | Synchronous `localStorage` on the main thread adds jank if written per keystroke |
| Complexity | One helper can own versioning and validation | Every persisted value needs a migration story |
| Maintainability | Explicit lifetimes document intent | Schema drift is silent until a user with old data loads the app |
| Failure behavior | Graceful degradation to defaults | Unvalidated restore is a white screen for long-tenured users |

## Alternative Approaches

Lifetime is one axis; the others answer different questions about the same value.

| Approach | Best when | Weakness | See |
| --- | --- | --- | --- |
| Lifetime-first classification | Deciding where a value should live | Says nothing about who owns the truth | (this article) |
| [Server vs Client State](./server-vs-client-state.md) | The value may be authoritative elsewhere | Orthogonal to how long the client keeps it | `Server vs Client State · State Management` |
| [UI vs Domain State](./ui-vs-domain-state.md) | Separating presentation from business meaning | Does not determine storage medium | `UI vs Domain State · State Management` |
| URL as the store | Any view configuration | String-typed; length limits; needs encoding | `Client-Side Routing · Routing` |
| Server-side session | Cross-device continuity required | Round-trip cost; requires auth | — |

The practical rule: **decide ownership first (server or client), then lifetime, then medium.** Reversing that order is how `localStorage` ends up holding server data.

## Bad Example

A document editor that persists the wrong things, forgets the right ones, and never versions any of it.

```ts
// ❌ One blob, no version, no namespace, no validation.
const KEY = "appState";

export function saveEverything(state) {
  localStorage.setItem(KEY, JSON.stringify(state));
}

export function loadEverything() {
  return JSON.parse(localStorage.getItem(KEY) ?? "{}");   // ❌ throws on corrupt JSON
}
```

```tsx
// ❌ Ephemeral UI persisted; real work not persisted at all.
function Editor({ docId, userId }) {
  const [isSidebarOpen, setSidebarOpen] = useState(false);
  const [isExportModalOpen, setExportModalOpen] = useState(false);
  const [activeTab, setActiveTab] = useState("edit");
  const [body, setBody] = useState("");             // ❌ the draft — memory only

  // ❌ Writes to localStorage on every state change, synchronously, on the main thread.
  useEffect(() => {
    saveEverything({ isSidebarOpen, isExportModalOpen, activeTab, docId });
  }, [isSidebarOpen, isExportModalOpen, activeTab, docId]);

  // ❌ Restores blindly: reopens the modal, restores another user's docId.
  useEffect(() => {
    const saved = loadEverything();
    setSidebarOpen(saved.isSidebarOpen ?? false);
    setExportModalOpen(saved.isExportModalOpen ?? false);
    setActiveTab(saved.activeTab ?? "edit");
  }, []);

  // ❌ Tab is not in the URL, so it cannot be shared or restored by the back button.
  return (
    <>
      <Tabs value={activeTab} onChange={setActiveTab} />
      <textarea value={body} onChange={(e) => setBody(e.target.value)} />
      {isExportModalOpen && <ExportModal onClose={() => setExportModalOpen(false)} />}
    </>
  );
}

// ❌ beforeunload: unreliable on mobile, and disqualifies the page from bfcache.
window.addEventListener("beforeunload", () => saveEverything(currentState));
```

**What goes wrong:** the export modal reopens on every reload, so a user who reloads to escape it is trapped; `isSidebarOpen` and `activeTab` are restored from a session that may belong to a different user on a shared machine, because the key is not namespaced and is never cleared on logout. The one value worth keeping — `body`, the user's actual writing — lives only in memory, so a backgrounded mobile tab reclaimed by the OS discards it silently. `loadEverything` calls `JSON.parse` on whatever is in storage with no `try` and no schema, so a value written by an older release, or corrupted by a half-completed write, white-screens the app on load. Writing on every state change means a synchronous `localStorage` write per keystroke once `body` is added, which blocks the main thread. And the `beforeunload` listener both fails to fire reliably when a mobile OS kills the tab and makes the page ineligible for bfcache, so ordinary back-navigation gets slower in exchange for a save that does not happen.

## Good Example

Each value at a deliberate stop on the ladder, with versioned storage, validated restore, and an explicit user choice.

```ts
// ✅ One helper owns versioning, namespacing, and validation for all persisted state.
import { z } from "zod";

const APP_SCHEMA_VERSION = 3;

type Store = "session" | "device";
const backend = (store: Store) => (store === "session" ? sessionStorage : localStorage);

export function key(store: Store, userId: string, name: string) {
  return `app:v${APP_SCHEMA_VERSION}:${store}:${userId}:${name}`;
}

export function persist<T>(store: Store, userId: string, name: string, value: T) {
  try {
    backend(store).setItem(key(store, userId, name), JSON.stringify({ v: APP_SCHEMA_VERSION, value }));
  } catch (err) {
    if (err?.name !== "QuotaExceededError") throw err;   // storage is best-effort
  }
}

export function restore<T>(
  store: Store,
  userId: string,
  name: string,
  schema: z.ZodType<T>,
): T | null {
  let raw: string | null = null;
  try {
    raw = backend(store).getItem(key(store, userId, name));
  } catch {
    return null;                                          // storage disabled entirely
  }
  if (!raw) return null;

  try {
    const envelope = JSON.parse(raw);
    if (envelope?.v !== APP_SCHEMA_VERSION) {             // ✅ old shape: discard, don't crash
      backend(store).removeItem(key(store, userId, name));
      return null;
    }
    const parsed = schema.safeParse(envelope.value);      // ✅ restored data is untrusted input
    return parsed.success ? parsed.data : null;
  } catch {
    backend(store).removeItem(key(store, userId, name));
    return null;
  }
}

// ✅ Logout clears the namespace rather than leaving data on a shared device.
export function clearUserState(userId: string) {
  for (const storage of [sessionStorage, localStorage]) {
    for (const k of Object.keys(storage)) {
      if (k.includes(`:${userId}:`)) storage.removeItem(k);
    }
  }
}
```

```tsx
// ✅ Each value sits at exactly one stop on the ladder.
const DraftSchema = z.object({
  body: z.string().max(100_000),
  savedAt: z.number(),
  baseRevision: z.string(),
});

function Editor({ docId, userId, serverRevision }: EditorProps) {
  // mount lifetime — dies with the component, never persisted
  const [isSidebarOpen, setSidebarOpen] = useState(false);
  const [isExportModalOpen, setExportModalOpen] = useState(false);

  // navigation lifetime — in the URL, so it is shareable and back-button aware
  const [searchParams, setSearchParams] = useSearchParams();
  const activeTab = searchParams.get("tab") ?? "edit";
  const setActiveTab = (tab: string) =>
    setSearchParams((prev) => { prev.set("tab", tab); return prev; }, { replace: true });

  // device lifetime — the user's actual work
  const [body, setBody] = useState("");
  const [offeredDraft, setOfferedDraft] = useState<z.infer<typeof DraftSchema> | null>(null);

  // ✅ Offer restoration; never restore silently over what the server has.
  useEffect(() => {
    const draft = restore("device", userId, `draft:${docId}`, DraftSchema);
    if (!draft) return;
    if (draft.baseRevision !== serverRevision) {
      setOfferedDraft(draft);        // stale: ask, showing both timestamps
    } else if (draft.body !== body) {
      setOfferedDraft(draft);        // newer local edit: ask
    }
  }, [docId, userId, serverRevision]);

  // ✅ Throttled saves, plus one on visibilitychange — bfcache-safe.
  const saveDraft = useMemo(
    () => throttle((text: string) => {
      persist("device", userId, `draft:${docId}`, {
        body: text, savedAt: Date.now(), baseRevision: serverRevision,
      });
    }, 2_000),
    [docId, userId, serverRevision],
  );

  useEffect(() => {
    const flush = () => { if (document.visibilityState === "hidden") saveDraft.flush(); };
    document.addEventListener("visibilitychange", flush);
    return () => {
      document.removeEventListener("visibilitychange", flush);
      saveDraft.flush();
    };
  }, [saveDraft]);

  return (
    <>
      <Tabs value={activeTab} onChange={setActiveTab} />
      <textarea
        value={body}
        onChange={(e) => { setBody(e.target.value); saveDraft(e.target.value); }}
      />
      {offeredDraft && (
        <RestorePrompt
          savedAt={offeredDraft.savedAt}
          onRestore={() => { setBody(offeredDraft.body); setOfferedDraft(null); }}
          onDiscard={() => {
            localStorage.removeItem(key("device", userId, `draft:${docId}`));
            setOfferedDraft(null);
          }}
        />
      )}
      {isExportModalOpen && <ExportModal onClose={() => setExportModalOpen(false)} />}
    </>
  );
}
```

```tsx
// ✅ Session lifetime: scroll position, restored per tab, discarded when the tab closes.
function useScrollRestoration(listId: string, userId: string) {
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const el = ref.current;
    if (!el) return;

    const saved = restore("session", userId, `scroll:${listId}`, z.number().nonnegative());
    if (saved !== null) el.scrollTop = saved;

    const onScroll = throttle(() => persist("session", userId, `scroll:${listId}`, el.scrollTop), 200);
    el.addEventListener("scroll", onScroll, { passive: true });
    return () => { el.removeEventListener("scroll", onScroll); onScroll.flush?.(); };
  }, [listId, userId]);

  return ref;
}
```

**Why it's better:** the modal and sidebar stay at mount lifetime, so a reload closes them exactly as the user expects; nothing writes them anywhere. `activeTab` moved to the URL, which makes a specific view linkable and makes the back button restore it with no code at all. The draft — the only genuinely valuable state — is persisted at device lifetime, throttled to once every two seconds and flushed on `visibilitychange`, which fires reliably when a mobile OS backgrounds the tab and, unlike `beforeunload`, keeps the page bfcache-eligible. Restoration is explicit: the draft is compared against the server revision and offered rather than applied, so a stale local copy cannot silently overwrite newer server content. Every read goes through `restore`, which checks the version envelope, validates against a schema, and returns `null` on any mismatch — so a shape written by an old release degrades to "no draft" instead of a white screen. Keys are namespaced by user and version, and `clearUserState` removes them on logout, so a shared device does not leak one user's writing to the next.

## Common Mistakes

See the [State Management anti-patterns](../../../anti-patterns/) for the domain catalog. Concept-specific:

### Mistake: Persisting transient UI flags

- **Symptom:** A modal, tooltip, or drag state reappears after a reload; users reload to escape a dialog and it comes back.
- **Why it fails:** These values only mean something within the mount that created them. Outside it there is no pointer, no focus, and no interaction to complete.
- **Fix:** Keep them in component state. If a *panel's* open state should survive navigation, put that one value in the URL — not the whole UI blob.

### Mistake: Keeping user-authored content only in memory

- **Symptom:** "It lost my comment" reports, concentrated on mobile.
- **Why it fails:** Mobile operating systems reclaim backgrounded tabs without warning, and no unload event is guaranteed to fire.
- **Fix:** Throttled writes to IndexedDB or `localStorage` plus a flush on `visibilitychange`; sync to the server when connectivity allows.

### Mistake: Persisting without a version or a schema

- **Symptom:** The app white-screens on load for long-tenured users after a release that changed a stored shape.
- **Why it fails:** Stored data was written by an older version of your code and is, to the current version, untrusted input of unknown shape.
- **Fix:** Wrap values in `{ v, value }`, validate with a schema on read, and discard or migrate on mismatch.

### Mistake: Using `beforeunload` to save

- **Symptom:** Saves happen on desktop but not on mobile; navigation performance regresses.
- **Why it fails:** `beforeunload` is not fired when a mobile OS terminates a tab, and registering it disqualifies the page from the back/forward cache.
- **Fix:** Save on `visibilitychange` to `hidden`, and throttle periodic saves during editing.

### Mistake: Not scoping storage to a user

- **Symptom:** On a shared device, one account sees another's drafts, filters, or recently viewed items.
- **Why it fails:** `localStorage` is per origin, not per session or account, and nothing clears it at logout by default.
- **Fix:** Namespace keys with the user id and clear that namespace on logout; keep anything sensitive on the server.

### Mistake: Putting navigation state in storage instead of the URL

- **Symptom:** Users cannot share a filtered view; the back button does not undo a filter change.
- **Why it fails:** Storage is invisible to the address bar and to the history stack, so the two most natural sharing and undo mechanisms do nothing.
- **Fix:** Put filters, tabs, sort, and pagination in search params; use `replace` for high-frequency updates so history stays usable.

## Checklist

- [ ] Every piece of state has a documented lifetime: render, mount, navigation, session, or account.
- [ ] No transient UI flag (`isOpen`, `isHovered`, `isDragging`) is written to any storage.
- [ ] Filters, tabs, sort, query, and pagination live in the URL.
- [ ] User-authored content is persisted with throttled writes and a flush on `visibilitychange`.
- [ ] `beforeunload` is not used for saving.
- [ ] Every persisted value carries a version and is validated with a schema on read.
- [ ] A version or schema mismatch degrades to a default rather than throwing.
- [ ] Storage keys are namespaced by user and cleared on logout.
- [ ] Restoration of user content is offered rather than applied silently when it may be stale.
- [ ] `QuotaExceededError` is handled wherever writes happen.
- [ ] The "old stored data, new code" path is covered by a test, not only the fresh-install path.

## Related Articles

- [Categories of State](./categories-of-state.md) — the taxonomy this lifetime axis refines.
- [Server vs Client State](./server-vs-client-state.md) — the ownership axis; decide it before lifetime.
- [UI vs Domain State](./ui-vs-domain-state.md) — the semantic axis; usually predicts the lifetime.
- [Local State](./local-state.md) — the default rung at the bottom of the ladder.
- [Lifting State Up](./lifting-state-up.md) — changing a value's *scope* rather than its lifetime.
- **Canonical home:** storage limits and eviction are owned by [Storage Quotas & Eviction · Browser APIs](../../00-foundations/browser-apis/storage-quotas-and-eviction.md).

## References

- [MDN — Window.sessionStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage) — tab-scoped storage semantics and lifetime.
- [MDN — Back/forward cache](https://developer.mozilla.org/en-US/docs/Glossary/bfcache) — what freezes in memory, and what disqualifies a page.
- [MDN — History.state](https://developer.mozilla.org/en-US/docs/Web/API/History/state) — per-entry state that survives navigation without touching storage.
- [Chrome — Page lifecycle API](https://developer.chrome.com/docs/web-platform/page-lifecycle-api) — why `visibilitychange` is the reliable save signal.

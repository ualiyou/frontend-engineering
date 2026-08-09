---
title: "useState"
slug: usestate
description: "How React stores state per hook slot, why updaters beat direct values, and the difference between derived data and state you should never have created."
keywords: ["useState", "React state", "state updater function", "lazy initializer", "derived state", "state batching", "hook slot", "Object.is", "key remount", "React hooks"]
part: "02 · Rendering & Frameworks"
domain: "React"
subcategory: "State & Hooks"
difficulty: "Intermediate"
reading_time_min: 12
priority: "Critical"
status: "Published"
canonical: true
last_reviewed: "2026-08-09"
prerequisites:
  - "The Render Phase"
related:
  - "useReducer"
  - "The Rules of Hooks"
  - "State Batching & Updates"
next:
  - "useReducer"
  - "The Rules of Hooks"
  - "State Batching & Updates"
  - "useEffect & Synchronization"
  - "useLayoutEffect"
alternatives: []
common_mistakes:
  - "anti-patterns/README.md#react"
  - "#common-mistakes"
frameworks: ["react"]
references:
  - { title: "React — useState", url: "https://react.dev/reference/react/useState" }
  - { title: "React — You Might Not Need an Effect", url: "https://react.dev/learn/you-might-not-need-an-effect" }
  - { title: "React — Choosing the State Structure", url: "https://react.dev/learn/choosing-the-state-structure" }
  - { title: "React — Preserving and Resetting State", url: "https://react.dev/learn/preserving-and-resetting-state" }
---

# useState

> `useState` is not a variable. It is a slot in a linked list attached to a fiber, read positionally on every render — which explains every rule about it.

**Part:** [02 · Rendering & Frameworks](../) · **Domain:** React · **Priority:** Critical · **Difficulty:** Intermediate · **Reading time:** ~12 min

## TL;DR

`useState` reserves a **slot** on the component's fiber, identified by call order rather than by name. Calling the setter does not mutate anything; it enqueues an update and schedules a re-render, so the `state` variable in the current render closure keeps its old value until the next render runs. React bails out when the new value is `Object.is`-equal to the old one, which is why mutating an object in place appears to do nothing. The two decisions that matter most are **what to store** — anything computable from props or other state is not state — and **how to update it**: pass an updater function whenever the next value depends on the previous one.

> **Recommendation:** Store the minimum independent facts, derive everything else during render, and use `setX(prev => …)` by default rather than `setX(x + 1)`.

## At a Glance

| | |
| --- | --- |
| **Use when** | A component owns an independent, non-derivable value that changes over time. |
| **Avoid when** | The value is computable from props or other state, or several fields change together — use `useReducer`. |
| **Alternatives** | `useReducer` for coupled transitions, derived values during render, URL or server state for shared data. |
| **Primary risk** | Duplicated state that drifts out of sync with its source, then needs an effect to re-sync. |
| **Maturity** | Stable — the API has not changed since hooks shipped; batching behavior became universal in React 18. |

## Prerequisites

State is read and written across render boundaries, so the render model comes first.

- [The Render Phase](./the-render-phase.md) — why a render is a pure function call and what a re-render actually recomputes.

## Overview

```tsx
const [count, setCount] = useState(0);
```

Three facts explain nearly all behavior.

**Slots are positional.** React keeps a linked list of hook records on the fiber. On each render, the *n*-th `useState` call reads the *n*-th record. Nothing about the variable name is stored, which is why hooks may not be called conditionally — a skipped call shifts every subsequent slot.

**`state` is a snapshot.** Within one render, `count` is a `const` bound to the value for *that* render. Calling `setCount(1)` does not change it; it enqueues an update and schedules work. Reading `count` after the setter in the same function gives the old value, always.

**Updates are compared and batched.** React applies queued updates in order, then compares the result with `Object.is`. Equal values let React bail out of re-rendering that subtree. Multiple setter calls in the same event — and, since React 18, in promises, timeouts, and native handlers too — are batched into a single render.

Two forms of the setter:

| Form | Use when |
| --- | --- |
| `setCount(5)` | The next value is independent of the previous one. |
| `setCount(c => c + 1)` | The next value derives from the previous one, or several updates may queue together. |

Two forms of the initializer:

| Form | Behavior |
| --- | --- |
| `useState(expensiveInit())` | The expression runs on **every** render; the result is discarded after the first. |
| `useState(() => expensiveInit())` | The function runs **only** on the first render. |

Finally, state is tied to the component's position in the tree. Changing a component's `key` unmounts it and mounts a fresh one, discarding state — the supported way to reset a subtree.

## The Problem

Two failure patterns account for most `useState` bugs, and both come from treating state as a variable.

```tsx
// ❌ Reads the snapshot three times; increments once.
function Counter() {
  const [count, setCount] = useState(0);

  function handleTripleClick() {
    setCount(count + 1);   // count is 0 → enqueues 1
    setCount(count + 1);   // count is still 0 → enqueues 1
    setCount(count + 1);   // count is still 0 → enqueues 1
  }
  return <button onClick={handleTripleClick}>{count}</button>;   // becomes 1, not 3
}
```

`count` is a `const` in this render's closure. All three calls read `0`, so all three enqueue `1`. The updater form (`c => c + 1`) reads the *queued* value each time and produces `3`.

The second pattern is duplicated state:

```tsx
// ❌ fullName duplicates first + last, then needs an effect to stay correct.
function Profile({ user }) {
  const [firstName, setFirstName] = useState(user.firstName);
  const [lastName, setLastName] = useState(user.lastName);
  const [fullName, setFullName] = useState("");

  useEffect(() => {
    setFullName(`${firstName} ${lastName}`);   // ❌ extra render, and briefly wrong
  }, [firstName, lastName]);

  return <h1>{fullName}</h1>;
}
```

Every keystroke now renders twice: once with the new name and a stale `fullName`, then again after the effect. There is a visible frame where the heading is wrong, and the "source of truth" question now has two answers.

Its cousin — mirroring props into state — is worse, because it silently stops updating:

```tsx
// ❌ Initializer runs once; later prop changes are ignored.
function PriceTag({ price }) {
  const [displayPrice, setDisplayPrice] = useState(price);
  return <span>{displayPrice}</span>;   // frozen at the first price forever
}
```

## Why It Matters

State shape determines how many bugs are *possible*. Every piece of duplicated state creates a pair of values that can disagree, and every effect written to keep them in sync is a chance for them to disagree during the frame before it runs.

Concretely, the costs are:

**Correctness.** Stale-closure updates lose increments under rapid interaction — the double-click, the fast typist, the retried network callback. These bugs are timing-dependent, so they reproduce in production and not in tests.

**Performance.** Sync effects double the render count for every change and can cascade: state A triggers effect B which sets state C which triggers effect D. React can render fast, but it cannot render fewer times than you ask it to.

**Comprehensibility.** A component with eight `useState` calls has 2⁸ nominal state combinations, most of which are unreachable but none of which are *documented* as unreachable. The same logic in a reducer has a named transition per event, which is a far smaller thing to hold in your head.

## Mental Model

Picture the fiber holding an ordered list of slots, and each render reading them in sequence.

```text
  fiber (Counter)
    hooks: ┌──────────┬──────────┬──────────┐
           │ slot 0   │ slot 1   │ slot 2   │
           │ count: 3 │ name:"a" │ open:true│
           └──────────┴──────────┴──────────┘
              ▲ 1st useState  ▲ 2nd  ▲ 3rd     ← matched by CALL ORDER, not name

  setCount(c => c + 1)
      └─► enqueue update on slot 0 ──► schedule render
                                          │
   render N   : count = 3  (const, frozen for this render)
   render N+1 : count = 4  (queue applied, Object.is compared)
```

Three rules fall out of the picture:

1. **Never call hooks conditionally.** A skipped call misaligns every later slot.
2. **The setter is a message, not an assignment.** It has no effect on the current render's variables.
3. **Identity is the comparison.** `Object.is` means a mutated object is still the same object, so React bails out and nothing re-renders.

## Best Practices

- **Derive during render.** If a value can be computed from props or other state, compute it in the component body. Add `useMemo` only when profiling shows the computation matters.
- **Use the updater form by default.** `setX(prev => …)` is correct in every case where `setX(value)` is, and correct in several where it is not.
- **Lazy-initialize expensive state** with `useState(() => compute())` so the computation does not run on every render.
- **Group values that change together** into one object or a `useReducer`. Independent values stay separate.
- **Reset with `key`, not with an effect.** `<Form key={userId} />` discards state when the identity changes, in one line and with no intermediate wrong frame.
- **Store the minimum.** Selected *id* rather than selected *object*; raw input string rather than parsed value plus validity plus error.
- **Never mutate state in place.** Build a new object or array; `Object.is` on the same reference is a bail-out.

## Trade-offs

`useState` is the cheapest state primitive, and its cost is that it does not scale with the number of related values.

**Advantages**

- Minimal API; state is local, so a component is understandable in isolation.
- Automatic batching means multiple updates in one event produce one render.
- Bail-out on `Object.is` equality avoids unnecessary work for free.
- `key`-based reset gives a declarative way to discard state.

**Disadvantages**

- Independent slots do not express which combinations are valid.
- Coupled updates spread transition logic across many call sites.
- Positional slots forbid conditional hook calls, which surprises newcomers.
- Local state is invisible to siblings, so sharing requires lifting or a store.

| Dimension | This approach | Cost / caveat |
| --- | --- | --- |
| Performance | Batched updates; bail-out on equal values | Each unnecessary state adds a render path |
| Complexity | Trivial for one value | Grows combinatorially with slot count |
| Maintainability | Colocated with the component | Transitions are implicit, not named |
| Failure behavior | Stale closures produce lost updates | Silent, timing-dependent, hard to test |

## Alternative Approaches

`useState` competes with several ways of holding a changing value.

| Approach | Best when | Weakness | See |
| --- | --- | --- | --- |
| `useState` | One or two independent values | No named transitions | (this article) |
| [useReducer](./) (planned) | Several values change together; events have names | More ceremony for one boolean | `useReducer · React` |
| Derived during render | The value is computable | None — this is the default | `Categories of State · State Management` |
| URL / search params | The value should survive reload and be shareable | Serialization; string-typed | `Client-Side Routing · Routing` |
| Server state cache | The value belongs to the server | Requires a query library | [Server vs Client State · State Management](../../03-application-architecture/state-management/server-vs-client-state.md) |
| `useRef` | The value changes but must not trigger a render | Invisible to rendering | — |

The practical rule: **derivable → derive; server-owned → a query cache; coupled transitions → a reducer; a single independent fact → `useState`.**

## Bad Example

A filterable, editable user list where every derived value became state.

```tsx
// ❌ Seven slots for two independent facts.
function UserList({ users }: { users: User[] }) {
  const [query, setQuery] = useState("");
  const [filtered, setFiltered] = useState(users);          // ❌ derived
  const [count, setCount] = useState(users.length);         // ❌ derived from derived
  const [selectedUser, setSelectedUser] = useState<User | null>(null);  // ❌ full object
  const [isEmpty, setIsEmpty] = useState(false);            // ❌ derived
  const [sortDir, setSortDir] = useState<"asc" | "desc">("asc");
  const [sorted, setSorted] = useState(users);              // ❌ derived

  // ❌ Effect chain: each set triggers another render.
  useEffect(() => {
    const next = users.filter((u) => u.name.toLowerCase().includes(query.toLowerCase()));
    setFiltered(next);
    setCount(next.length);
    setIsEmpty(next.length === 0);
  }, [users, query]);

  useEffect(() => {
    setSorted([...filtered].sort((a, b) =>
      sortDir === "asc" ? a.name.localeCompare(b.name) : b.name.localeCompare(a.name),
    ));
  }, [filtered, sortDir]);

  // ❌ Reads the snapshot, so rapid clicks lose toggles.
  function toggleSort() {
    setSortDir(sortDir === "asc" ? "desc" : "asc");
  }

  // ❌ Mutates state in place — Object.is sees the same array, nothing re-renders.
  function markSeen(id: string) {
    const user = sorted.find((u) => u.id === id);
    if (user) user.seen = true;
    setSorted(sorted);
  }

  // ❌ Expensive initializer runs on every render.
  const [prefs] = useState(loadPreferencesFromStorage());

  return (
    <>
      <input value={query} onChange={(e) => setQuery(e.target.value)} />
      <button onClick={toggleSort}>Sort {sortDir}</button>
      {isEmpty ? <Empty /> : <List items={sorted} onSeen={markSeen} />}
      {selectedUser && <Detail user={selectedUser} />}
    </>
  );
}
```

**What goes wrong:** typing one character causes at least three renders — the `query` update, the first effect's three setters, then the second effect's setter — and during the first of those the list shows stale results with a new query, a visible flicker. `filtered`, `count`, `isEmpty`, and `sorted` are all computable from `users`, `query`, and `sortDir`, so four slots exist only to be re-synced, and any code path that forgets one leaves them disagreeing. `selectedUser` stores the whole object, so when `users` refreshes from the server the detail pane shows a stale copy. `toggleSort` reads the render snapshot, so two fast clicks can both read `"asc"` and produce one toggle. `markSeen` mutates an element and passes the same array reference back, so `Object.is` matches and React bails out — the change is in memory but never on screen. And `loadPreferencesFromStorage()` runs synchronously on every single render, reading `localStorage` and blocking the main thread, because the initializer was passed as a value rather than as a function.

## Good Example

The same list with two state slots, everything else derived, and updates that never read a stale snapshot.

```tsx
// ✅ Two independent facts. Everything else is computed.
function UserList({ users }: { users: User[] }) {
  const [query, setQuery] = useState("");
  const [sortDir, setSortDir] = useState<"asc" | "desc">("asc");
  const [selectedId, setSelectedId] = useState<string | null>(null);   // ✅ id, not object

  // ✅ Lazy initializer: reads storage once, not on every render.
  const [prefs] = useState(() => loadPreferencesFromStorage());

  // ✅ Derived during render — always consistent, never a stale frame.
  const visible = useMemo(() => {
    const needle = query.trim().toLowerCase();
    const matched = needle
      ? users.filter((u) => u.name.toLowerCase().includes(needle))
      : users;

    return [...matched].sort((a, b) =>
      sortDir === "asc" ? a.name.localeCompare(b.name) : b.name.localeCompare(a.name),
    );
  }, [users, query, sortDir]);

  // ✅ Plain expressions; no slot, no effect, no possibility of drift.
  const isEmpty = visible.length === 0;
  const selectedUser = selectedId ? users.find((u) => u.id === selectedId) ?? null : null;

  // ✅ Updater form: correct even when two clicks land in the same batch.
  const toggleSort = () => setSortDir((dir) => (dir === "asc" ? "desc" : "asc"));

  return (
    <>
      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        aria-label="Filter users"
      />
      <button onClick={toggleSort}>Sort {sortDir === "asc" ? "A–Z" : "Z–A"}</button>

      {isEmpty ? <Empty query={query} /> : (
        <List items={visible} onSelect={setSelectedId} density={prefs.density} />
      )}

      {/* ✅ key resets Detail's internal state when the selection changes */}
      {selectedUser && <Detail key={selectedUser.id} user={selectedUser} />}
    </>
  );
}
```

```tsx
// ✅ Immutable updates, and an updater that reads the queued value.
function useSeenSet() {
  const [seen, setSeen] = useState<ReadonlySet<string>>(() => new Set());

  const markSeen = useCallback((id: string) => {
    setSeen((prev) => {
      if (prev.has(id)) return prev;          // ✅ same reference → React bails out
      const next = new Set(prev);             // ✅ new reference → re-render
      next.add(id);
      return next;
    });
  }, []);

  return [seen, markSeen] as const;
}
```

```tsx
// ✅ When several values genuinely change together, one slot with a named transition.
type Selection =
  | { status: "none" }
  | { status: "one"; id: string }
  | { status: "range"; from: string; to: string };

function useSelection() {
  const [selection, setSelection] = useState<Selection>({ status: "none" });

  return {
    selection,
    clear: () => setSelection({ status: "none" }),
    select: (id: string) => setSelection({ status: "one", id }),
    extendTo: (to: string) =>
      setSelection((prev) =>
        prev.status === "one" ? { status: "range", from: prev.id, to } : prev,
      ),
  };
}
```

**Why it's better:** the component holds three independent facts instead of seven, and `visible`, `isEmpty`, and `selectedUser` are recomputed during render, so there is no frame in which they disagree with `query` — the flicker is gone along with both effects. Storing `selectedId` rather than the user object means a server refresh flows through automatically, because the lookup happens on every render. `toggleSort`'s updater form reads the queued value, so two clicks in the same batch produce two toggles rather than one. `markSeen` returns the previous `Set` when nothing changed, which lets React bail out for free, and a new `Set` when it did, which guarantees the re-render — the two halves of `Object.is` used deliberately instead of accidentally. The lazy initializer moves the `localStorage` read off every render. And modelling `Selection` as a discriminated union makes the invalid combinations — a range with no start, a selected id while "none" — unrepresentable, which is what several independent booleans could never express.

## Common Mistakes

See the [React anti-patterns](../../../anti-patterns/) for the domain catalog. Concept-specific:

### Mistake: Reading state to compute the next state

- **Symptom:** Rapid clicks or fast typing lose updates; a counter increments once when it should increment three times.
- **Why it fails:** `state` is a `const` frozen for the current render. Every setter call in the same event reads the same stale value, so later calls overwrite earlier ones with the same result.
- **Fix:** Use the updater form `setX(prev => …)`, which receives the value with all queued updates already applied.

### Mistake: Storing values that can be derived

- **Symptom:** `useEffect` calls whose only job is to `setState` from other state, and a visible frame with inconsistent data.
- **Why it fails:** Derived state creates a second source of truth that must be re-synced after every change, and the sync always lands one render late.
- **Fix:** Compute the value in the component body. Add `useMemo` only if profiling shows the computation is expensive.

### Mistake: Mutating state in place

- **Symptom:** Data changes in the debugger but the UI does not update.
- **Why it fails:** React compares with `Object.is`. A mutated array or object is the same reference, so the update is treated as a no-op and the render is skipped.
- **Fix:** Produce a new object, array, `Map`, or `Set`; return the previous reference deliberately when you *want* the bail-out.

### Mistake: Passing a computed value as the initializer

- **Symptom:** An expensive parse, `localStorage` read, or date computation runs on every render even though its result is used once.
- **Why it fails:** `useState(expensive())` evaluates the argument on every render; React discards the result after the first.
- **Fix:** Pass a function — `useState(() => expensive())` — so it runs on mount only.

### Mistake: Syncing props into state with an effect

- **Symptom:** A component ignores prop changes, or updates one render late with a flash of the old value.
- **Why it fails:** The initializer runs only on mount, and an effect that copies props into state renders twice and is briefly wrong in between.
- **Fix:** Use the prop directly if the value is not independently editable; if it must be resettable, change the component's `key` so React remounts it with fresh state.

## Checklist

- [ ] Every state slot holds a fact that cannot be computed from props or other state.
- [ ] Updates that depend on the previous value use the updater form.
- [ ] No `useEffect` exists solely to copy one piece of state into another.
- [ ] Objects and arrays in state are replaced, never mutated.
- [ ] Expensive initial values are wrapped in a function.
- [ ] Selections and references store ids, not snapshots of objects.
- [ ] Values that change together live in one object, a reducer, or a discriminated union.
- [ ] Resetting a subtree is done with `key`, not with an effect.
- [ ] Hooks are called unconditionally, at the top level, in a stable order.
- [ ] Invalid combinations of state are unrepresentable, not merely unreachable.

## Related Articles

- [The Render Phase](./the-render-phase.md) — why the state variable is a snapshot and what a re-render recomputes.
- [The Commit Phase](./the-commit-phase.md) — when the DOM actually reflects the new state.
- [Reconciliation & Diffing](./reconciliation-and-diffing.md) — how `key` decides whether state is preserved or discarded.
- [Keys & List Reconciliation](./keys-and-list-reconciliation.md) — the same mechanism applied to lists.
- [useReducer](./) (planned) — named transitions for state that changes together.
- [Categories of State · State Management](../../03-application-architecture/state-management/categories-of-state.md) — deciding what deserves to be state at all.
- **Canonical home:** server-owned data is owned by [Server vs Client State · State Management](../../03-application-architecture/state-management/server-vs-client-state.md).

## References

- [React — useState](https://react.dev/reference/react/useState) — API reference, updater semantics, and the lazy initializer.
- [React — You Might Not Need an Effect](https://react.dev/learn/you-might-not-need-an-effect) — the canonical argument against derived state.
- [React — Choosing the State Structure](https://react.dev/learn/choosing-the-state-structure) — grouping, minimizing, and avoiding duplication.
- [React — Preserving and Resetting State](https://react.dev/learn/preserving-and-resetting-state) — how position and `key` determine state identity.

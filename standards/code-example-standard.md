# Code Example Standard

The rules every code sample in **Frontend Engineering** obeys. Examples are the repository's proof of work: they turn reasoning into something a reader can run, review, and trust. A sloppy example discredits a correct argument, so the bar is high — a Good Example must read like code that already passed review in a serious production repository.

This standard defines the hard requirements. The [quality levels](./article-quality.md#example-quality-levels) (A/B/C) decide *how much* of this applies to a given snippet; a **Level A** example applies all of it.

## Table of contents

- [Baseline versions](#baseline-versions)
- [Language and typing](#language-and-typing)
- [Formatting](#formatting)
- [Imports](#imports)
- [Folder structure](#folder-structure)
- [Naming](#naming)
- [Comments](#comments)
- [Error handling](#error-handling)
- [Accessibility](#accessibility)
- [Performance](#performance)
- [No unnecessary abstractions](#no-unnecessary-abstractions)
- [The example checklist](#the-example-checklist)

## Baseline versions

One table, one source of truth. When these move, update this table and nothing else — articles inherit the baseline and only name a version inline when their behavior depends on it.

| Tool | Baseline | Rule |
| --- | --- | --- |
| **React** | 19.x | Function components and hooks only. No class components except in an article specifically about them. Assume the modern JSX transform (no `import React` needed for JSX). |
| **TypeScript** | 5.6+ | `strict: true` is assumed for every snippet. Examples must type-check under strict mode. |
| **Node.js** | 20 LTS or newer | For any Node-side or tooling snippet. |
| **Package manager** | pnpm | Commands use `pnpm`; note npm/yarn equivalents only when they differ meaningfully. |
| **Module system** | ESM | `import`/`export`. No CommonJS `require` unless the article is about interop. |
| **Target** | Evergreen browsers | Baseline-supported web APIs. Note when a feature needs a polyfill or has limited support. |

**Version discipline.** Do not scatter version numbers through prose. Name a version *only* where the behavior would be wrong without it (for example, "`use` unwraps promises as of React 19"). Everywhere else, rely on this baseline so articles age without per-line edits. This is the [evergreen](./evergreen-policy.md) rule applied to code.

## Language and typing

- **TypeScript for all application and component code.** Plain JavaScript only when the article is specifically about a JS-level concept, and even then prefer typed.
- **Strict mode assumed.** No implicit `any`. If a snippet needs `any`, it is either wrong or the article is *about* `any` — say which.
- **No `@ts-ignore` / `@ts-expect-error`** in a Good Example. In a Bad Example it may appear as the very thing being criticized, commented as such.
- **Prefer `type` for unions and function types, `interface` for object shapes that may be extended** — but consistency within a file matters more than the rule; pick one and hold it.
- **Type the boundaries.** Function parameters, return types of exported functions, and external data (fetch responses, form input) are explicitly typed or validated. Internal inference is fine.
- **Model impossible states as unrepresentable.** Prefer discriminated unions over booleans-that-shouldn't-coexist (`{ status: 'loading' } | { status: 'error'; error: Error }`, not `{ loading: boolean; error: Error | null }`).

## Formatting

- **Prettier defaults are the law.** 2-space indent, semicolons, single quotes in TS/JS, trailing commas (`all`), ~80–100 col width. Do not hand-format against Prettier.
- **ESLint clean.** No unused vars, no unreachable code, no floating promises. A Good Example produces zero lint errors.
- **One statement per line.** No clever one-liners that hide control flow.
- **Blank lines separate logical blocks**, not every line. Group related statements.
- **Fenced code blocks are always language-tagged:** ` ```tsx `, ` ```ts `, ` ```css `, ` ```html `, ` ```bash `, ` ```json `. An untagged fence fails lint and review.
- Use `tsx` for JSX-containing samples, `ts` for pure TypeScript.

## Imports

- **Order and group:** (1) Node/standard built-ins, (2) external packages, (3) internal absolute imports (`@/…`), (4) relative imports (`./…`, `../…`), (5) type-only imports, (6) styles/assets last. A blank line between groups.
- **`import type` for type-only imports.** Keeps them erasable and intent clear.
- **Named imports over default** where the library offers both, for grep-ability — except where the ecosystem convention is default (`import React`, framework entrypoints).
- **No wildcard `import * as`** unless the API genuinely requires it (namespaces).
- **Real, resolvable specifiers.** No `from 'your-utils'` placeholders in a Good Example; if a helper is referenced, either define it or make its origin obvious. Placeholder imports are allowed only in Level C fragments and must look like placeholders.
- **No side-effect imports** hidden mid-file; put unavoidable ones (`import './polyfill'`) at the top with a comment.

## Folder structure

When an example spans more than one file (recipes, multi-file illustrations), show the tree first, then the files, and follow the repository's **feature-first** convention:

```text
feature-name/
├─ index.ts            # public surface of the feature (barrel, thin)
├─ FeatureName.tsx     # component (PascalCase, matches export)
├─ use-feature-name.ts # hook (kebab file, camelCase export `useFeatureName`)
├─ feature-name.ts     # pure logic / helpers
├─ feature-name.types.ts
└─ feature-name.test.ts
```

- **Colocate by feature, not by type.** Hooks, components, and tests for one feature live together; do not scatter into global `hooks/`, `components/`, `utils/` unless genuinely shared.
- **Files kebab-case; the default export's identity drives the component filename** (`InvoiceTable.tsx` exporting `InvoiceTable`). Non-component files stay kebab-case (`use-invoice-table.ts`).
- **One primary export per file.** A barrel `index.ts` re-exports the public surface; internals stay unexported.
- **Tests sit next to source** as `*.test.ts(x)`.
- Keep this consistent with the repository-wide rules in [`naming-conventions.md`](./naming-conventions.md).

## Naming

- **Components:** `PascalCase` (`InvoiceTable`). **Hooks:** `useCamelCase` (`useInvoiceTotals`). **Functions/variables:** `camelCase`. **Types/interfaces:** `PascalCase`. **Constants:** `UPPER_SNAKE` only for true module-level constants; otherwise `camelCase`.
- **Boolean names read as predicates:** `isLoading`, `hasError`, `canSubmit`, `shouldRetry`.
- **Event handlers:** `handleX` for the implementation, `onX` for the prop (`onSubmit={handleSubmit}`).
- **No abbreviations that aren't industry-standard.** `request` not `req` (except idiomatic `req`/`res` in Node handlers), `button` not `btn`, `index` not `idx` (loop `i` is fine).
- **Domain names, not placeholders.** `user`, `invoice`, `cartItems` — never `foo`, `data2`, `temp`, `obj`. Names are the cheapest documentation.
- **Names say purpose, not type.** `users` not `userArray`, `total` not `totalNumber`.

## Comments

- Governed by [`writing-style.md`](./writing-style.md#code-comments): comment the **why**, mark the **teaching line**, no `TODO`/commented-out code in Good Examples.
- **Every Bad Example marks the failing line** with a `// ❌` comment naming the failure.
- **Every Good Example marks the critical fix** with a `// ✅` comment.
- Do not narrate obvious code. A comment that restates the line is deleted.

## Error handling

Non-negotiable for **Level A**. Its absence is the actual bug in most real-world code, so an example that skips it is teaching the wrong lesson.

- **Every async operation handles rejection.** No unhandled promises, no `.then()` without a `.catch()` or `try/catch` around `await`.
- **Cancellation and cleanup.** Fetches use `AbortController`; subscriptions, timers, and listeners are torn down (effect cleanup, `finally`). Show the cleanup — it is the point.
- **Distinguish expected from unexpected failures.** Expected (validation, 404, offline) is handled and surfaced to the user; unexpected is thrown or reported, not swallowed.
- **No empty `catch`.** A caught error is handled, rethrown, or logged with context — never silently dropped.
- **Typed errors at boundaries.** Narrow `unknown` in `catch`; validate external data (e.g. with a schema) before trusting its shape.
- **User-facing error states** are rendered, not left to a blank screen — accessible error messaging (see below).

## Accessibility

Required whenever the example renders UI (**Level A**, and Level B when the point touches UI).

- **Semantic HTML first.** `button` for actions, `a` for navigation, `label` tied to every input, real headings, lists for lists. A `div` with an `onClick` is a Bad Example unless the article is about that mistake.
- **Keyboard operable.** Everything usable with a pointer is usable with a keyboard; focus order is logical; focus is visible; focus is managed across dialogs and route changes.
- **ARIA only to fill gaps** native semantics cannot, and correctly (`aria-live` for async status, `aria-invalid` + `aria-describedby` for form errors). No redundant or wrong ARIA.
- **Labels and names.** Every interactive element has an accessible name; icons-only controls carry `aria-label`.
- **Respect user preferences** where relevant (`prefers-reduced-motion` for animation examples).
- Consistent with the accessibility articles under `docs/04-interface-engineering/accessibility/`.

## Performance

- **Correct first, fast second — but not wasteful.** Do not add memoization, virtualization, or workers speculatively; add them when the example is *about* them or the naive version is genuinely and visibly costly, and say why.
- **Name the cost you are avoiding.** "This memo skips a re-render per keystroke" — a performance choice without a stated reason is cargo-culting and fails review.
- **No accidental O(n²)** or per-render allocation presented as fine. If a Bad Example has one, that is the lesson; if a Good Example does, it is a bug.
- **Measure claims.** Any "this is faster" is backed by a mechanism (fewer renders, one fewer round-trip) or a reproducible measurement, never a vibe.
- **Cleanup is performance too.** Leaked listeners and timers are performance defects; see error handling.

## No unnecessary abstractions

The most common way a well-meaning example goes wrong. Prefer the boring, direct version.

- **Inline until it repeats.** Do not extract a hook, a wrapper, a factory, or a generic until there are at least two real call sites. One use does not justify an abstraction.
- **No indirection without a name for what it buys.** A wrapper that only forwards props, a `utils` layer over one function, a config object for one option — delete it.
- **No premature generalization.** Solve the case in front of you. A `<GenericTable<T>>` in an article about one table hides the point behind type gymnastics.
- **No design patterns for their own sake.** Factories, providers, and HOCs appear only when the trade-off article justifies them.
- **Fewer files, fewer layers, fewer concepts** — as long as clarity holds. The simplest code that handles production correctly is the target. This mirrors the repository's bias toward the direct solution.
- The test: **could a reader delete a layer and lose nothing?** If yes, it should not be in the example.

## The example checklist

For every Good Example (Level A). Level B relaxes only the orthogonal-concern items; it never relaxes correctness, types, or safety.

- [ ] Language-tagged fence; TypeScript, strict-clean, no `any`/`@ts-ignore`.
- [ ] Prettier- and ESLint-clean; imports grouped and real.
- [ ] Domain names, correct casing conventions.
- [ ] Every async path handles rejection; cancellation and cleanup shown.
- [ ] No empty catch; external data validated at the boundary.
- [ ] Semantic HTML; keyboard-operable; accessible names and error states (if it renders UI).
- [ ] Performance choices justified with a stated cost; no speculative optimization.
- [ ] No abstraction without ≥2 real call sites; no dead indirection.
- [ ] The teaching line is commented (`✅`/`❌`); no `TODO` or commented-out code.
- [ ] It would pass review in a real production repo.

---

**Next:** [`article-quality.md`](./article-quality.md) — where A/B/C levels are defined · [`diagram-guide.md`](./diagram-guide.md) — visuals for the "How It Works" section · [`naming-conventions.md`](./naming-conventions.md) — repository-wide naming.

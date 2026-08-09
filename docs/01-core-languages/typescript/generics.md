---
title: "Generics"
slug: generics
description: "Type parameters as functions over types — when a generic earns its place, when it is a disguised `any`, and the rule for how many parameters a signature should have."
keywords: ["TypeScript generics", "type parameters", "type inference", "generic functions", "type argument inference", "generic components", "unnecessary generics", "type-level functions"]
part: "01 · Core Languages"
domain: "TypeScript"
subcategory: "Composition"
difficulty: "Foundational"
reading_time_min: 8
priority: "Critical"
status: "Published"
canonical: true
last_reviewed: "2026-08-09"
prerequisites:
  - "Unions & Intersections"
  - "Structural Typing"
related:
  - "Unions & Intersections"
  - "Generic Constraints"
  - "Indexed Access & keyof"
next:
  - "Generic Constraints"
alternatives:
  - "Generic Constraints"
  - "Indexed Access & keyof"
common_mistakes:
  - "anti-patterns/README.md#typescript"
  - "#common-mistakes"
frameworks: []
references:
  - { title: "TypeScript Handbook — Generics", url: "https://www.typescriptlang.org/docs/handbook/2/generics.html" }
  - { title: "TypeScript Handbook — Type Inference", url: "https://www.typescriptlang.org/docs/handbook/type-inference.html" }
  - { title: "TypeScript Release Notes — const type parameters", url: "https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-0.html#const-type-parameters" }
  - { title: "TypeScript Handbook — Variance annotations", url: "https://www.typescriptlang.org/docs/handbook/2/generics.html#variance-annotations" }
---

# Generics

> A type parameter is a function from types to types. If a parameter appears in only one position, that function is constant — and a constant function is not doing anything.

**Part:** [01 · Core Languages](../) · **Domain:** TypeScript · **Priority:** Critical · **Difficulty:** Foundational · **Reading time:** ~8 min

## TL;DR

**Generics** let a signature relate types to each other instead of naming them: `identity<T>(x: T): T` says *whatever comes in comes out*, which no concrete annotation can express. The rule that decides whether a generic is pulling its weight is simple — a type parameter must appear **at least twice**, once to be inferred from and once to be used. A parameter appearing only in the return position is an unsafe cast wearing a costume; one appearing only in a single argument position could have been a plain union or `unknown`. Inference does most of the work at call sites, so well-designed generics are invisible to callers and only become visible when they are wrong.

> **Recommendation:** Write the concrete function first, then extract a type parameter only when a caller-visible relationship exists between inputs and outputs. Delete any parameter that appears once.

## At a Glance

| | |
| --- | --- |
| **Use when** | A function's output type depends on its input type, or a container must preserve its element type. |
| **Avoid when** | The parameter appears once; the relationship can be expressed by a union or overloads. |
| **Alternatives** | [Unions & Intersections](#alternative-approaches), overloads, `unknown` plus narrowing. |
| **Primary risk** | Return-position-only parameters, which let callers assert any type with no check. |
| **Maturity** | Stable — the core feature since TypeScript 0.9; `const` type parameters arrived in 5.0. |

## Prerequisites

Generics compose types, so you need the type relationships they compose over.

- [Structural Typing](./structural-typing.md) — why a type parameter can be satisfied by any compatible shape.
- [Unions & Intersections](./unions-and-intersections.md) — the alternative to a type parameter, and often the better one.

## Overview

A generic declares **type parameters** that are filled in — usually inferred — at each use site.

```ts
function first<T>(items: readonly T[]): T | undefined {
  return items[0];
}

first([1, 2, 3]);        // T inferred as number  → number | undefined
first(["a", "b"]);       // T inferred as string  → string | undefined
```

`T` appears twice: once inside the parameter type, where TypeScript infers it, and once in the return type, where it is used. That is what makes the signature more informative than `(items: unknown[]) => unknown`.

Inference works by matching the argument's type against the parameter's type structurally, then picking the best common candidate. Three controls modify it:

| Control | Effect |
| --- | --- |
| **Constraints** (`T extends X`) | Restrict what may be substituted, and give the body access to `X`'s members. |
| **Defaults** (`T = X`) | Supply a type when inference has nothing to work with. |
| **`const` type parameters** (`<const T>`) | Infer literal types and readonly tuples rather than widening to `string`/`number`/array. |

Two properties trip people up. First, TypeScript widens literals during inference unless the position is `const`-modified or the target is constrained to something narrow: `first(["a", "b"])` infers `string`, not `"a" | "b"`. Second, a type parameter is **not** an escape hatch — `function get<T>(key: string): T` compiles, infers `T` as `unknown` when uncalled with explicit arguments, and lets every call site claim whatever type it likes. That signature is `as T` with extra steps.

Generic *types* (as opposed to generic functions) work the same way, and variance annotations (`in`, `out`) let you state whether a parameter is used in input or output position when TypeScript's structural inference would be slow or ambiguous.

## The Problem

Generics get reached for as a way to silence the compiler, which inverts their purpose.

```ts
// ❌ T appears only in the return position — this is an unchecked assertion.
async function fetchJson<T>(url: string): Promise<T> {
  const res = await fetch(url);
  return res.json();
}

const user = await fetchJson<User>("/api/users/1");
// `user` is typed User. Nothing verified that the server sent a User.
```

The compiler is now confident about a value it has never seen. When the API changes a field name, TypeScript reports nothing and the failure appears as `undefined` in a template three layers away.

The mirror-image mistake is a parameter that never varies:

```ts
// ❌ T appears once, in an argument position. It buys nothing.
function logAll<T>(items: T[]): void {
  for (const item of items) console.log(item);
}
```

`(items: unknown[]) => void` is the same function with a simpler signature. The generic adds a name the reader must track for no gain.

And the over-parameterized version, which is the most common shape in real codebases:

```ts
// ❌ Four parameters, three of which are inferred from the same place.
function mapRecord<
  TInput extends Record<string, unknown>,
  TKey extends keyof TInput,
  TValue extends TInput[TKey],
  TOutput,
>(input: TInput, fn: (value: TValue, key: TKey) => TOutput): Record<TKey, TOutput> {
  // …
}
```

Inference now has four unknowns to solve simultaneously; when a call site fails, the error names all four and points at none of them.

## Why It Matters

Generics are how a type system expresses *relationships*, and relationships are what make types worth having. Without them, every reusable container degrades to `any` at its boundary and the type checker stops protecting anything that passes through.

The failure modes have different costs. A **missing** generic produces friction: callers cast, `as` proliferates, and the casts are where the real bugs hide. An **unsound** generic — the return-position-only kind — is worse, because it produces false confidence: the editor autocompletes fields that may not exist, so the mistake is invisible in review and only appears at runtime.

There is also a maintenance dimension. Over-parameterized signatures are the leading cause of unreadable TypeScript errors, and unreadable errors train teams to reach for `any`. Keeping type parameters to the minimum that expresses the relationship is therefore an ergonomics decision as much as a correctness one — a signature nobody can debug is a signature nobody will keep.

## Mental Model

Read a generic signature as a question: *what does the caller learn from the arguments?*

```text
   function pick<T, K extends keyof T>(obj: T, keys: K[]): Pick<T, K>
                 │  │                       │        │          │  │
                 │  └── inferred from ──────┘        │          │  │
                 └───── inferred from ───────────────┘          │  │
                                                                │  │
                        used in the result ─────────────────────┘──┘

   Each parameter must be inferable (appear in an argument)
   AND useful (appear in the return or another parameter).
```

Apply three checks to any generic you write:

1. **Count the appearances.** Fewer than two? Delete the parameter.
2. **Is it inferable?** If a caller must write the type argument explicitly every time, the relationship is not being derived from anything — consider an overload or a concrete type.
3. **Would `unknown` plus narrowing be honest?** If the value's real type is not known until runtime, say so with `unknown` and validate, rather than promising a type the compiler cannot check.

## Best Practices

- **Write the concrete version first,** then generalize only where a real second use exists. Speculative generality costs more than duplication.
- **Enforce the two-appearance rule.** One appearance means the parameter should be a concrete type, a union, or `unknown`.
- **Never type a network boundary with a caller-supplied parameter.** Return `unknown` and validate with a schema; the parsed output type comes from the schema, not the caller.
- **Constrain parameters** so the body can use them and the error messages improve. `T extends object` documents intent that bare `T` does not.
- **Name parameters descriptively** once there is more than one — `TItem`, `TKey`, `TResult` — and keep `T` only for a single obvious parameter.
- **Reach for `const` type parameters** when literal or tuple preservation matters, instead of asking callers to write `as const`.
- **Prefer inference to explicit type arguments.** If every call site passes them, redesign the signature.

## Trade-offs

Type parameters buy expressiveness and charge for it in error legibility and compile time.

**Advantages**

- Relationships between inputs and outputs are expressed once and checked everywhere.
- Callers get precise types with no annotation, because inference does the work.
- Containers and utilities stay reusable without degrading to `any`.

**Disadvantages**

- Each parameter multiplies the inference search space and the size of the error messages.
- Deeply generic code compiles more slowly and can hit instantiation-depth limits.
- Generics are easy to misuse as assertions, which is worse than having no types.
- Variance surprises appear where a parameter is used in both input and output positions.

| Dimension | This approach | Cost / caveat |
| --- | --- | --- |
| Performance | No runtime cost — types are erased | Compile time grows with parameter count and depth |
| Complexity | One signature replaces many overloads | Errors become harder to read past ~3 parameters |
| Maintainability | Refactors propagate through types | Public generic signatures are hard to change compatibly |
| Failure behavior | Mismatches caught at compile time | Return-only parameters catch nothing at all |

## Alternative Approaches

A type parameter is one of several ways to express "this works for more than one type".

| Approach | Best when | Weakness | See |
| --- | --- | --- | --- |
| Generic function | Output type depends on input type | Error legibility degrades with parameter count | (this article) |
| [Unions & Intersections](./unions-and-intersections.md) | A small, closed set of accepted types | Does not preserve which member came in | `Unions & Intersections · TypeScript` |
| Overloads | A few discrete input/output pairings | Duplication; implementation signature is unchecked | — |
| `unknown` + narrowing | The type is genuinely unknown until runtime | Callers must narrow | `unknown, never & any · TypeScript` |
| Schema-derived types | Data crosses a trust boundary | Requires a schema library | `Schema-Inferred Types · Forms & Validation` |

The practical rule: **relationship between argument and result → generic; closed set of options → union; unknown at runtime → `unknown` plus validation.**

## Bad Example

A data-fetching layer where generics are used as assertions and the signatures over-parameterize.

```ts
// ❌ T is a promise from the caller, not a fact about the response.
async function api<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(path, init);
  return res.json() as T;                       // ❌ unchecked cast
}

// ❌ T appears once; the generic adds nothing over `unknown[]`.
function countBy<T>(items: T[], predicate: (item: any) => boolean): number {
  return items.filter(predicate).length;        // ❌ `any` erases the parameter anyway
}

// ❌ Four parameters solving for one relationship.
function selectFields<
  TRow extends Record<string, unknown>,
  TKeys extends readonly (keyof TRow)[],
  TResult extends Pick<TRow, TKeys[number]>,
  TFallback = undefined,
>(rows: TRow[], keys: TKeys, fallback?: TFallback): (TResult | TFallback)[] {
  // …
}

// Usage
const user = await api<User>("/api/users/1");
console.log(user.displayName.toUpperCase());     // ❌ runtime TypeError when the API renames it
```

**What goes wrong:** `api<T>` places `T` only in the return type, so every call site chooses its own answer and the compiler agrees unconditionally — `as T` with a friendlier syntax. When the server renames `displayName` to `name`, nothing fails to compile and the error surfaces as `Cannot read properties of undefined` in production. `countBy` declares `T` and then immediately discards it by typing the predicate's parameter as `any`, so the type parameter is decorative and the predicate is unchecked. `selectFields` asks inference to solve four unknowns at once, one of which (`TResult`) is fully determined by the other two and should not be a parameter at all — a mismatched call produces an error mentioning all four, which is the kind of message that ends with someone adding `as any`.

## Good Example

The same layer with parameters that are inferred and used, validation at the boundary, and the minimum number of unknowns.

```ts
// ✅ The network boundary returns unknown; the type comes from a schema, not the caller.
import { z } from "zod";

async function api(path: string, init?: RequestInit): Promise<unknown> {
  const res = await fetch(path, init);
  if (!res.ok) throw new HttpError(res.status, path);
  return res.json();
}

// ✅ TSchema is inferred from the argument and used in the return — two appearances.
export async function apiAs<TSchema extends z.ZodTypeAny>(
  schema: TSchema,
  path: string,
  init?: RequestInit,
): Promise<z.infer<TSchema>> {
  const raw = await api(path, init);
  const parsed = schema.safeParse(raw);
  if (!parsed.success) {
    throw new ResponseShapeError(path, parsed.error.issues);
  }
  return parsed.data;
}
```

```ts
// ✅ One parameter, inferred from `items`, used in the predicate. No `any`.
export function countBy<TItem>(
  items: readonly TItem[],
  predicate: (item: TItem, index: number) => boolean,
): number {
  let count = 0;
  for (let i = 0; i < items.length; i++) {
    if (predicate(items[i], i)) count += 1;
  }
  return count;
}

// ✅ Two parameters, both inferable; the result type is computed, not parameterized.
export function selectFields<TRow extends object, const TKeys extends readonly (keyof TRow)[]>(
  rows: readonly TRow[],
  keys: TKeys,
): Pick<TRow, TKeys[number]>[] {
  return rows.map((row) => {
    const out = {} as Pick<TRow, TKeys[number]>;
    for (const key of keys) out[key] = row[key];
    return out;
  });
}
```

```ts
// ✅ Call sites need no type arguments; inference derives everything.
const User = z.object({
  id: z.string(),
  name: z.string(),
  createdAt: z.coerce.date(),
});

const user = await apiAs(User, "/api/users/1");
//    ^? { id: string; name: string; createdAt: Date }

const overdue = countBy(invoices, (invoice) => invoice.dueAt < new Date());
//                                 ^? Invoice — inferred, not annotated

const summaries = selectFields(users, ["id", "name"]);
//    ^? Pick<User, "id" | "name">[]  — const parameter preserved the literal keys
```

**Why it's better:** `apiAs` moves the type from the caller's imagination to a schema that actually runs, so a renamed API field throws a `ResponseShapeError` naming the path and the issue rather than surfacing as `undefined` three components later; `TSchema` is inferred from the first argument and used in the return, satisfying the two-appearance rule honestly. `countBy` types the predicate's parameter as `TItem` rather than `any`, so the callback body is checked and the parameter earns its keep. `selectFields` drops from four type parameters to two by *computing* the result with `Pick<TRow, TKeys[number]>` instead of parameterizing it, which halves the inference search space and makes failures name the argument that is actually wrong. The `const` modifier on `TKeys` preserves the literal key names without asking callers to write `as const`, so the result type is `Pick<User, "id" | "name">` rather than `Pick<User, keyof User>`.

## Common Mistakes

See the [TypeScript anti-patterns](../../../anti-patterns/) for the domain catalog. Concept-specific:

### Mistake: A type parameter that appears only in the return type

- **Symptom:** `function get<T>(key: string): T`, called as `get<User>("user")`, with full autocomplete on a value nobody checked.
- **Why it fails:** Nothing constrains `T`, so the caller is asserting rather than the compiler inferring. It is `as T` with a signature that looks safe.
- **Fix:** Return `unknown` and validate, or derive the return type from an argument — a schema, a key of a known map, a parser function.

### Mistake: A type parameter that appears only once in an argument

- **Symptom:** `function log<T>(value: T): void`.
- **Why it fails:** The parameter has nothing to relate to, so it carries no information. `unknown` says the same thing more clearly.
- **Fix:** Replace with `unknown`, or with a constrained concrete type if the body needs members.

### Mistake: Weakening a parameter with `any` inside the signature

- **Symptom:** A generic function whose callback parameters are typed `any`, so the callback body is unchecked.
- **Why it fails:** The type parameter is inferred and then immediately discarded; the generic is documentation, not enforcement.
- **Fix:** Thread the parameter through every position it belongs in — callbacks included.

### Mistake: Parameterizing a type that could be computed

- **Symptom:** A signature with a `TResult extends …` parameter whose constraint fully determines it from the other parameters.
- **Why it fails:** Inference must solve for a variable that has exactly one solution, which slows checking and produces errors naming irrelevant parameters.
- **Fix:** Write the derived type directly in the return position — `Pick<T, K>`, `T[K]`, `ReturnType<F>` — and delete the parameter.

## Checklist

- [ ] Every type parameter appears at least twice in the signature.
- [ ] No type parameter appears only in the return type.
- [ ] Callers do not need to pass explicit type arguments at ordinary call sites.
- [ ] `any` does not appear anywhere inside a generic signature.
- [ ] Result types that can be computed (`Pick`, indexed access, `ReturnType`) are computed rather than parameterized.
- [ ] Parameters are constrained where the body relies on members.
- [ ] Data crossing a trust boundary is typed from a runtime schema, not a caller-supplied parameter.
- [ ] Parameters have descriptive names once there is more than one.
- [ ] `const` type parameters are used where literal or tuple preservation matters.

## Related Articles

- [Structural Typing](./structural-typing.md) — why any compatible shape satisfies a type parameter.
- [Unions & Intersections](./unions-and-intersections.md) — the simpler alternative when the set of types is closed.
- [Assignability](./assignability.md) — the relation that decides whether an inferred candidate is acceptable.
- [Generic Constraints](./) (planned) — `extends` clauses, defaults, and how they steer inference.
- [Indexed Access & keyof](./) (planned) — computing result types instead of parameterizing them.
- **Canonical home:** runtime validation of external data is owned by [Schema Validation · Forms & Validation](../../03-application-architecture/forms-validation/schema-validation.md).

## References

- [TypeScript Handbook — Generics](https://www.typescriptlang.org/docs/handbook/2/generics.html) — parameters, constraints, defaults, and variance annotations.
- [TypeScript Handbook — Type Inference](https://www.typescriptlang.org/docs/handbook/type-inference.html) — how candidates are collected and the best common type chosen.
- [TypeScript 5.0 — const type parameters](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-0.html#const-type-parameters) — preserving literal and tuple types at call sites.
- [TypeScript Handbook — Variance annotations](https://www.typescriptlang.org/docs/handbook/2/generics.html#variance-annotations) — `in` and `out` for parameters used in both positions.

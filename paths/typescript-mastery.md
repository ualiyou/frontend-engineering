# TypeScript Mastery — Learning Path

> An engineer who wants to model domains precisely and use the type system to its full power.

**Level:** Advanced · **Required:** 50 articles (~8.3 h) · **Optional:** 13 articles (~3.0 h)

Difficulty of required articles: Foundational 35 · Intermediate 12 · Advanced 3.

Follow the sections in order. Articles link into [`docs/`](../docs/); each shows its difficulty and estimated reading time. Full prerequisites for any article are in its domain's `graph.json` (see [GRAPH.md](../GRAPH.md)).

## Milestones

1. Reason about structural typing, assignability, and variance
2. Write conditional, mapped, and template-literal types
3. Model domains so illegal states are unrepresentable
4. Achieve end-to-end type safety across the network boundary

## Expected skills

By completing the required articles you should be able to:

- Type-level programming and inference control
- Sound domain modeling with the type system
- Typing third-party code and ambient declarations
- End-to-end type safety from schema to UI

## Required articles

### TypeScript

- [Structural Typing](../docs/01-core-languages/typescript/structural-typing.md) · Foundational · 8 min
- [Assignability](../docs/01-core-languages/typescript/assignability.md) · Foundational · 8 min
- [unknown, never & any](../docs/01-core-languages/typescript/unknown-never-and-any.md) · Foundational · 8 min
- [Literal & Unit Types](../docs/01-core-languages/typescript/literal-and-unit-types.md) · Foundational · 8 min
- [Unions & Intersections](../docs/01-core-languages/typescript/unions-and-intersections.md) · Foundational · 8 min
- [Generics](../docs/01-core-languages/typescript/generics.md) · Foundational · 8 min
- [Generic Constraints](../docs/01-core-languages/typescript/generic-constraints.md) · Foundational · 8 min
- [Indexed Access & keyof](../docs/01-core-languages/typescript/indexed-access-and-keyof.md) · Foundational · 8 min
- [Conditional Types](../docs/01-core-languages/typescript/conditional-types.md) · Intermediate · 12 min
- [Mapped Types](../docs/01-core-languages/typescript/mapped-types.md) · Intermediate · 12 min
- [Template Literal Types](../docs/01-core-languages/typescript/template-literal-types.md) · Intermediate · 12 min
- [infer & Type Extraction](../docs/01-core-languages/typescript/infer-and-type-extraction.md) · Intermediate · 12 min
- [Type Inference](../docs/01-core-languages/typescript/type-inference.md) · Foundational · 8 min
- [Control-Flow Narrowing](../docs/01-core-languages/typescript/control-flow-narrowing.md) · Foundational · 8 min
- [Type Guards & Predicates](../docs/01-core-languages/typescript/type-guards-and-predicates.md) · Foundational · 8 min
- [Discriminated Unions](../docs/01-core-languages/typescript/discriminated-unions.md) · Foundational · 8 min
- [Variance](../docs/01-core-languages/typescript/variance.md) · Intermediate · 12 min
- [Unsoundness & Escape Hatches](../docs/01-core-languages/typescript/unsoundness-and-escape-hatches.md) · Intermediate · 15 min
- [Strictness Flags](../docs/01-core-languages/typescript/strictness-flags.md) · Intermediate · 12 min
- [Declaration Files](../docs/01-core-languages/typescript/declaration-files.md) · Foundational · 8 min
- [Module Augmentation](../docs/01-core-languages/typescript/module-augmentation.md) · Foundational · 8 min
- [Typing Third-Party Code](../docs/01-core-languages/typescript/typing-third-party-code.md) · Foundational · 8 min
- [Branded & Nominal Types](../docs/01-core-languages/typescript/branded-and-nominal-types.md) · Foundational · 8 min
- [Exhaustiveness](../docs/01-core-languages/typescript/exhaustiveness.md) · Foundational · 8 min
- [Illegal States Unrepresentable](../docs/01-core-languages/typescript/illegal-states-unrepresentable.md) · Foundational · 11 min

### JavaScript

- [Primitives & Wrappers](../docs/01-core-languages/javascript/primitives-and-wrappers.md) · Foundational · 8 min
- [Coercion & Conversion](../docs/01-core-languages/javascript/coercion-and-conversion.md) · Foundational · 8 min
- [Equality & Comparison](../docs/01-core-languages/javascript/equality-and-comparison.md) · Foundational · 8 min
- [null, undefined & Nullish](../docs/01-core-languages/javascript/null-undefined-and-nullish.md) · Foundational · 8 min
- [Property Descriptors](../docs/01-core-languages/javascript/property-descriptors.md) · Foundational · 8 min
- [The Prototype Chain](../docs/01-core-languages/javascript/the-prototype-chain.md) · Foundational · 8 min
- [Inheritance Patterns](../docs/01-core-languages/javascript/inheritance-patterns.md) · Foundational · 8 min
- [Proxies & Reflect](../docs/01-core-languages/javascript/proxies-and-reflect.md) · Foundational · 8 min
- [Higher-Order Functions](../docs/01-core-languages/javascript/higher-order-functions.md) · Foundational · 8 min
- [Currying & Partial Application](../docs/01-core-languages/javascript/currying-and-partial-application.md) · Foundational · 11 min
- [Composition](../docs/01-core-languages/javascript/composition.md) · Foundational · 8 min
- [Iterators & Iterables](../docs/01-core-languages/javascript/iterators-and-iterables.md) · Foundational · 8 min
- [Generators](../docs/01-core-languages/javascript/generators.md) · Foundational · 8 min
- [Async Iterators](../docs/01-core-languages/javascript/async-iterators.md) · Foundational · 8 min
- [ES Modules](../docs/01-core-languages/javascript/es-modules.md) · Foundational · 8 min
- [Dynamic Import](../docs/01-core-languages/javascript/dynamic-import.md) · Foundational · 8 min
- [Module Resolution Semantics](../docs/01-core-languages/javascript/module-resolution-semantics.md) · Foundational · 11 min
- [Symbols & Well-Known Symbols](../docs/01-core-languages/javascript/symbols-and-well-known-symbols.md) · Intermediate · 15 min
- [Reflection](../docs/01-core-languages/javascript/reflection.md) · Intermediate · 12 min
- [Tagged Templates](../docs/01-core-languages/javascript/tagged-templates.md) · Intermediate · 12 min

### Forms & Validation

- [Schema-Inferred Types](../docs/03-application-architecture/forms-validation/schema-inferred-types.md) · Intermediate · 12 min
- [Shared Client/Server Schemas](../docs/03-application-architecture/forms-validation/shared-client-server-schemas.md) · Intermediate · 15 min

### API Design & Contracts

- [End-to-End Type Safety (tRPC)](../docs/03-application-architecture/api-design/end-to-end-type-safety-trpc.md) · Advanced · 19 min
- [Code Generation from Schemas](../docs/03-application-architecture/api-design/code-generation-from-schemas.md) · Advanced · 19 min
- [Contract Testing](../docs/03-application-architecture/api-design/contract-testing.md) · Advanced · 16 min

## Optional articles

### Frontend Architecture

- [Separation of Concerns](../docs/03-application-architecture/architecture/separation-of-concerns.md) · Intermediate · 12 min
- [Layered Architecture](../docs/03-application-architecture/architecture/layered-architecture.md) · Intermediate · 12 min
- [Module Boundaries](../docs/03-application-architecture/architecture/module-boundaries.md) · Intermediate · 12 min
- [Dependency Direction & Inversion](../docs/03-application-architecture/architecture/dependency-direction-and-inversion.md) · Intermediate · 15 min

### Build Systems & Tooling

- [Transpilation & Targets](../docs/06-engineering-systems/build-tooling/transpilation-and-targets.md) · Advanced · 16 min
- [Source-to-Source Compilers](../docs/06-engineering-systems/build-tooling/source-to-source-compilers.md) · Advanced · 16 min
- [AST Transforms & Plugins](../docs/06-engineering-systems/build-tooling/ast-transforms-and-plugins.md) · Advanced · 16 min

### React

- [memo, useMemo, useCallback](../docs/02-rendering-frameworks/react/memo-usememo-usecallback.md) · Intermediate · 12 min
- [Referential Stability](../docs/02-rendering-frameworks/react/referential-stability.md) · Intermediate · 12 min
- [The React Compiler Model](../docs/02-rendering-frameworks/react/the-react-compiler-model.md) · Intermediate · 12 min

### State Management

- [Computed Values](../docs/03-application-architecture/state-management/computed-values.md) · Intermediate · 12 min
- [Selectors & Memoized Selectors](../docs/03-application-architecture/state-management/selectors-and-memoized-selectors.md) · Intermediate · 15 min
- [Store Shape & Normalization](../docs/03-application-architecture/state-management/store-shape-and-normalization.md) · Intermediate · 15 min

---

[← All learning paths](./) · [Knowledge Map](../KNOWLEDGE_MAP.md) · [Dependency Graph](../GRAPH.md)

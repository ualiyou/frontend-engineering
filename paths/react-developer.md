# React Developer — Learning Path

> A developer who knows JavaScript and wants to build production React applications.

**Level:** Intermediate · **Required:** 116 articles (~25.1 h) · **Optional:** 35 articles (~7.7 h)

Difficulty of required articles: Intermediate 109 · Advanced 7.

Follow the sections in order. Articles link into [`docs/`](../docs/); each shows its difficulty and estimated reading time. Full prerequisites for any article are in its domain's `graph.json` (see [GRAPH.md](../GRAPH.md)).

## Milestones

1. Master hooks, effects, and the rendering/commit model
2. Choose the right state category (server, client, URL, form)
3. Cache and mutate server data with revalidation and optimistic updates
4. Structure routes, layouts, and route-level data loading
5. Design clean, composable component APIs

## Expected skills

By completing the required articles you should be able to:

- Idiomatic, performant React with modern patterns
- Correct separation of server vs client state
- Data fetching, caching, and mutations
- Component and routing architecture

## Required articles

### React

- [Elements vs Components](../docs/02-rendering-frameworks/react/elements-vs-components.md) · Intermediate · 12 min
- [JSX Semantics](../docs/02-rendering-frameworks/react/jsx-semantics.md) · Intermediate · 12 min
- [Composition & Children](../docs/02-rendering-frameworks/react/composition-and-children.md) · Intermediate · 12 min
- [The Render Phase](../docs/02-rendering-frameworks/react/the-render-phase.md) · Intermediate · 12 min
- [Reconciliation & Diffing](../docs/02-rendering-frameworks/react/reconciliation-and-diffing.md) · Intermediate · 12 min
- [Keys & List Reconciliation](../docs/02-rendering-frameworks/react/keys-and-list-reconciliation.md) · Intermediate · 12 min
- [The Commit Phase](../docs/02-rendering-frameworks/react/the-commit-phase.md) · Intermediate · 12 min
- [useState](../docs/02-rendering-frameworks/react/usestate.md) · Intermediate · 12 min
- [useReducer](../docs/02-rendering-frameworks/react/usereducer.md) · Intermediate · 12 min
- [The Rules of Hooks](../docs/02-rendering-frameworks/react/the-rules-of-hooks.md) · Intermediate · 12 min
- [State Batching & Updates](../docs/02-rendering-frameworks/react/state-batching-and-updates.md) · Intermediate · 12 min
- [useEffect & Synchronization](../docs/02-rendering-frameworks/react/useeffect-and-synchronization.md) · Intermediate · 15 min
- [useLayoutEffect](../docs/02-rendering-frameworks/react/uselayouteffect.md) · Intermediate · 12 min
- [Effect Cleanup & Dependencies](../docs/02-rendering-frameworks/react/effect-cleanup-and-dependencies.md) · Intermediate · 15 min
- [Refs & useRef](../docs/02-rendering-frameworks/react/refs-and-useref.md) · Intermediate · 12 min
- [Error Boundaries](../docs/02-rendering-frameworks/react/error-boundaries.md) · Intermediate · 12 min
- [Context & Providers](../docs/02-rendering-frameworks/react/context-and-providers.md) · Intermediate · 12 min
- [Context Performance](../docs/02-rendering-frameworks/react/context-performance.md) · Intermediate · 12 min
- [useContext Patterns](../docs/02-rendering-frameworks/react/usecontext-patterns.md) · Intermediate · 12 min
- [Concurrent Rendering](../docs/02-rendering-frameworks/react/concurrent-rendering.md) · Advanced · 16 min
- [Transitions & useTransition](../docs/02-rendering-frameworks/react/transitions-and-usetransition.md) · Advanced · 19 min
- [useDeferredValue](../docs/02-rendering-frameworks/react/usedeferredvalue.md) · Advanced · 16 min
- [Suspense](../docs/02-rendering-frameworks/react/suspense.md) · Advanced · 16 min
- [Server Components](../docs/02-rendering-frameworks/react/server-components.md) · Advanced · 16 min
- [Server Actions](../docs/02-rendering-frameworks/react/server-actions.md) · Advanced · 16 min
- [The RSC Payload & Boundaries](../docs/02-rendering-frameworks/react/the-rsc-payload-and-boundaries.md) · Advanced · 19 min
- [memo, useMemo, useCallback](../docs/02-rendering-frameworks/react/memo-usememo-usecallback.md) · Intermediate · 12 min
- [Referential Stability](../docs/02-rendering-frameworks/react/referential-stability.md) · Intermediate · 12 min
- [The React Compiler Model](../docs/02-rendering-frameworks/react/the-react-compiler-model.md) · Intermediate · 12 min
- [Custom Hooks](../docs/02-rendering-frameworks/react/custom-hooks.md) · Intermediate · 12 min
- [Portals](../docs/02-rendering-frameworks/react/portals.md) · Intermediate · 12 min
- [Higher-Order Components](../docs/02-rendering-frameworks/react/higher-order-components.md) · Intermediate · 12 min
- [Children Manipulation](../docs/02-rendering-frameworks/react/children-manipulation.md) · Intermediate · 12 min

### Rendering Architectures

- [The CSR Model](../docs/02-rendering-frameworks/rendering-architectures/the-csr-model.md) · Intermediate · 12 min
- [The App Shell Pattern](../docs/02-rendering-frameworks/rendering-architectures/the-app-shell-pattern.md) · Intermediate · 12 min
- [Client-Side Data Loading](../docs/02-rendering-frameworks/rendering-architectures/client-side-data-loading.md) · Intermediate · 12 min
- [The SSR Model](../docs/02-rendering-frameworks/rendering-architectures/the-ssr-model.md) · Intermediate · 12 min
- [Hydration](../docs/02-rendering-frameworks/rendering-architectures/hydration.md) · Intermediate · 12 min
- [Selective & Progressive Hydration](../docs/02-rendering-frameworks/rendering-architectures/selective-and-progressive-hydration.md) · Intermediate · 15 min
- [Hydration Mismatches](../docs/02-rendering-frameworks/rendering-architectures/hydration-mismatches.md) · Intermediate · 12 min
- [The Server/Client Boundary](../docs/02-rendering-frameworks/rendering-architectures/the-server-client-boundary.md) · Intermediate · 12 min
- [Islands Architecture](../docs/02-rendering-frameworks/rendering-architectures/islands-architecture.md) · Intermediate · 12 min
- [Resumability vs Hydration](../docs/02-rendering-frameworks/rendering-architectures/resumability-vs-hydration.md) · Intermediate · 12 min
- [Edge vs Origin Rendering](../docs/02-rendering-frameworks/rendering-architectures/edge-vs-origin-rendering.md) · Intermediate · 12 min

### Routing

- [Client-Side Routing](../docs/02-rendering-frameworks/routing/client-side-routing.md) · Intermediate · 12 min
- [File-Based & Server Routing](../docs/02-rendering-frameworks/routing/file-based-and-server-routing.md) · Intermediate · 15 min
- [Hybrid Routing](../docs/02-rendering-frameworks/routing/hybrid-routing.md) · Intermediate · 12 min
- [Route Matching & Params](../docs/02-rendering-frameworks/routing/route-matching-and-params.md) · Intermediate · 12 min
- [Nested Routes & Layouts](../docs/02-rendering-frameworks/routing/nested-routes-and-layouts.md) · Intermediate · 12 min
- [Parallel & Intercepting Routes](../docs/02-rendering-frameworks/routing/parallel-and-intercepting-routes.md) · Intermediate · 15 min
- [The URL as State](../docs/02-rendering-frameworks/routing/the-url-as-state.md) · Intermediate · 12 min
- [Route Loaders & Dependencies](../docs/02-rendering-frameworks/routing/route-loaders-and-dependencies.md) · Intermediate · 15 min
- [Deferred & Streaming Route Data](../docs/02-rendering-frameworks/routing/deferred-and-streaming-route-data.md) · Intermediate · 15 min
- [Route Actions & Mutations](../docs/02-rendering-frameworks/routing/route-actions-and-mutations.md) · Intermediate · 12 min
- [Navigation & Linking](../docs/02-rendering-frameworks/routing/navigation-and-linking.md) · Intermediate · 12 min
- [Transitions & Pending UI](../docs/02-rendering-frameworks/routing/transitions-and-pending-ui.md) · Intermediate · 12 min
- [Scroll Restoration](../docs/02-rendering-frameworks/routing/scroll-restoration.md) · Intermediate · 12 min
- [Route Prefetching](../docs/02-rendering-frameworks/routing/route-prefetching.md) · Intermediate · 12 min
- [Route-Based Code Splitting](../docs/02-rendering-frameworks/routing/route-based-code-splitting.md) · Intermediate · 12 min
- [Route Guards & Redirects](../docs/02-rendering-frameworks/routing/route-guards-and-redirects.md) · Intermediate · 12 min

### State Management

- [Categories of State](../docs/03-application-architecture/state-management/categories-of-state.md) · Intermediate · 12 min
- [Server vs Client State](../docs/03-application-architecture/state-management/server-vs-client-state.md) · Intermediate · 12 min
- [UI vs Domain State](../docs/03-application-architecture/state-management/ui-vs-domain-state.md) · Intermediate · 12 min
- [Ephemeral vs Persistent State](../docs/03-application-architecture/state-management/ephemeral-vs-persistent-state.md) · Intermediate · 15 min
- [Local State](../docs/03-application-architecture/state-management/local-state.md) · Intermediate · 12 min
- [Lifting State Up](../docs/03-application-architecture/state-management/lifting-state-up.md) · Intermediate · 12 min
- [Global State](../docs/03-application-architecture/state-management/global-state.md) · Intermediate · 12 min
- [Colocation vs Centralization](../docs/03-application-architecture/state-management/colocation-vs-centralization.md) · Intermediate · 15 min
- [Computed Values](../docs/03-application-architecture/state-management/computed-values.md) · Intermediate · 12 min
- [Selectors & Memoized Selectors](../docs/03-application-architecture/state-management/selectors-and-memoized-selectors.md) · Intermediate · 15 min
- [Store Shape & Normalization](../docs/03-application-architecture/state-management/store-shape-and-normalization.md) · Intermediate · 15 min
- [The Reducer Pattern](../docs/03-application-architecture/state-management/the-reducer-pattern.md) · Intermediate · 12 min
- [Unidirectional Data Flow](../docs/03-application-architecture/state-management/unidirectional-data-flow.md) · Intermediate · 12 min
- [Event Sourcing & Commands](../docs/03-application-architecture/state-management/event-sourcing-and-commands.md) · Intermediate · 12 min
- [Modeling UI with State Machines](../docs/03-application-architecture/state-management/modeling-ui-with-state-machines.md) · Intermediate · 15 min

### Data & Server State

- [Fetch-on-Render vs Render-as-You-Fetch](../docs/03-application-architecture/data-server-state/fetch-on-render-vs-render-as-you-fetch.md) · Intermediate · 15 min
- [Parallel vs Waterfall Requests](../docs/03-application-architecture/data-server-state/parallel-vs-waterfall-requests.md) · Intermediate · 15 min
- [Request Deduplication](../docs/03-application-architecture/data-server-state/request-deduplication.md) · Intermediate · 12 min
- [Data Prefetching](../docs/03-application-architecture/data-server-state/data-prefetching.md) · Intermediate · 12 min
- [Cache Keys & Query Identity](../docs/03-application-architecture/data-server-state/cache-keys-and-query-identity.md) · Intermediate · 15 min
- [Staleness & Revalidation](../docs/03-application-architecture/data-server-state/staleness-and-revalidation.md) · Intermediate · 12 min
- [Cache Invalidation](../docs/03-application-architecture/data-server-state/cache-invalidation.md) · Intermediate · 12 min
- [Background Refetching](../docs/03-application-architecture/data-server-state/background-refetching.md) · Intermediate · 12 min
- [Mutation Lifecycle](../docs/03-application-architecture/data-server-state/mutation-lifecycle.md) · Intermediate · 12 min
- [Optimistic Updates](../docs/03-application-architecture/data-server-state/optimistic-updates.md) · Intermediate · 12 min
- [Rollback & Conflict Resolution](../docs/03-application-architecture/data-server-state/rollback-and-conflict-resolution.md) · Intermediate · 15 min
- [Pagination](../docs/03-application-architecture/data-server-state/pagination.md) · Intermediate · 12 min
- [Infinite & Cursor Loading](../docs/03-application-architecture/data-server-state/infinite-and-cursor-loading.md) · Intermediate · 12 min
- [List Virtualization](../docs/03-application-architecture/data-server-state/list-virtualization.md) · Intermediate · 12 min

### Component & Interaction Design

- [Prop Design & Contracts](../docs/04-interface-engineering/component-design/prop-design-and-contracts.md) · Intermediate · 12 min
- [Composition vs Configuration](../docs/04-interface-engineering/component-design/composition-vs-configuration.md) · Intermediate · 15 min
- [Polymorphic Components (as)](../docs/04-interface-engineering/component-design/polymorphic-components-as.md) · Intermediate · 15 min
- [Slots & Children APIs](../docs/04-interface-engineering/component-design/slots-and-children-apis.md) · Intermediate · 12 min
- [Headless Components](../docs/04-interface-engineering/component-design/headless-components.md) · Intermediate · 12 min
- [Controlled vs Uncontrolled Pattern](../docs/04-interface-engineering/component-design/controlled-vs-uncontrolled-pattern.md) · Intermediate · 15 min
- [Compound Components](../docs/04-interface-engineering/component-design/compound-components.md) · Intermediate · 12 min
- [Render Props](../docs/04-interface-engineering/component-design/render-props.md) · Intermediate · 12 min
- [Pointer & Mouse Interaction](../docs/04-interface-engineering/component-design/pointer-and-mouse-interaction.md) · Intermediate · 15 min
- [Drag & Drop](../docs/04-interface-engineering/component-design/drag-and-drop.md) · Intermediate · 12 min
- [Hover, Press & Long-Press States](../docs/04-interface-engineering/component-design/hover-press-and-long-press-states.md) · Intermediate · 15 min
- [Gesture Handling](../docs/04-interface-engineering/component-design/gesture-handling.md) · Intermediate · 12 min
- [Loading & Skeleton States](../docs/04-interface-engineering/component-design/loading-and-skeleton-states.md) · Intermediate · 12 min
- [Empty States](../docs/04-interface-engineering/component-design/empty-states.md) · Intermediate · 12 min
- [Error & Retry States](../docs/04-interface-engineering/component-design/error-and-retry-states.md) · Intermediate · 12 min
- [Disabled & Busy States](../docs/04-interface-engineering/component-design/disabled-and-busy-states.md) · Intermediate · 12 min

### Forms & Validation

- [Controlled Inputs](../docs/03-application-architecture/forms-validation/controlled-inputs.md) · Intermediate · 12 min
- [Uncontrolled Inputs & Refs](../docs/03-application-architecture/forms-validation/uncontrolled-inputs-and-refs.md) · Intermediate · 12 min
- [Form Libraries & State Models](../docs/03-application-architecture/forms-validation/form-libraries-and-state-models.md) · Intermediate · 15 min
- [Field Arrays & Dynamic Fields](../docs/03-application-architecture/forms-validation/field-arrays-and-dynamic-fields.md) · Intermediate · 15 min
- [Client-Side Validation Strategies](../docs/03-application-architecture/forms-validation/client-side-validation-strategies.md) · Intermediate · 15 min
- [Schema Validation](../docs/03-application-architecture/forms-validation/schema-validation.md) · Intermediate · 12 min
- [Async & Server Validation](../docs/03-application-architecture/forms-validation/async-and-server-validation.md) · Intermediate · 12 min
- [Cross-Field Validation](../docs/03-application-architecture/forms-validation/cross-field-validation.md) · Intermediate · 12 min
- [Error Messaging](../docs/03-application-architecture/forms-validation/error-messaging.md) · Intermediate · 12 min
- [Inline vs Submit Validation](../docs/03-application-architecture/forms-validation/inline-vs-submit-validation.md) · Intermediate · 15 min
- [Dirty, Touched & Submit State](../docs/03-application-architecture/forms-validation/dirty-touched-and-submit-state.md) · Intermediate · 15 min

## Optional articles

### Reactivity & Framework Models

- [Signals & Fine-Grained Reactivity](../docs/02-rendering-frameworks/reactivity-models/signals-and-fine-grained-reactivity.md) · Advanced · 19 min
- [The Virtual DOM](../docs/02-rendering-frameworks/reactivity-models/the-virtual-dom.md) · Advanced · 16 min
- [Compiled Reactivity](../docs/02-rendering-frameworks/reactivity-models/compiled-reactivity.md) · Advanced · 16 min
- [Push-Based vs Dirty Checking](../docs/02-rendering-frameworks/reactivity-models/push-based-vs-dirty-checking.md) · Advanced · 19 min
- [Observables](../docs/02-rendering-frameworks/reactivity-models/observables.md) · Advanced · 16 min
- [Atoms & Derived Values](../docs/02-rendering-frameworks/reactivity-models/atoms-and-derived-values.md) · Advanced · 16 min
- [Effects & Reactions](../docs/02-rendering-frameworks/reactivity-models/effects-and-reactions.md) · Advanced · 16 min
- [Declarative vs Imperative UI](../docs/02-rendering-frameworks/reactivity-models/declarative-vs-imperative-ui.md) · Advanced · 19 min
- [Data Binding Models](../docs/02-rendering-frameworks/reactivity-models/data-binding-models.md) · Advanced · 16 min
- [Framework Comparison Axes](../docs/02-rendering-frameworks/reactivity-models/framework-comparison-axes.md) · Advanced · 16 min

### TypeScript

- [Structural Typing](../docs/01-core-languages/typescript/structural-typing.md) · Foundational · 8 min
- [Assignability](../docs/01-core-languages/typescript/assignability.md) · Foundational · 8 min
- [unknown, never & any](../docs/01-core-languages/typescript/unknown-never-and-any.md) · Foundational · 8 min
- [Literal & Unit Types](../docs/01-core-languages/typescript/literal-and-unit-types.md) · Foundational · 8 min
- [Type Inference](../docs/01-core-languages/typescript/type-inference.md) · Foundational · 8 min
- [Control-Flow Narrowing](../docs/01-core-languages/typescript/control-flow-narrowing.md) · Foundational · 8 min
- [Type Guards & Predicates](../docs/01-core-languages/typescript/type-guards-and-predicates.md) · Foundational · 8 min
- [Discriminated Unions](../docs/01-core-languages/typescript/discriminated-unions.md) · Foundational · 8 min

### Testing & Quality

- [The Testing Pyramid/Trophy](../docs/05-reliability-quality/testing/the-testing-pyramid-trophy.md) · Intermediate · 12 min
- [What to Test & Coverage Goals](../docs/05-reliability-quality/testing/what-to-test-and-coverage-goals.md) · Intermediate · 15 min
- [Test Doubles (mocks, stubs, fakes)](../docs/05-reliability-quality/testing/test-doubles-mocks-stubs-fakes.md) · Intermediate · 15 min
- [Rendering & Querying](../docs/05-reliability-quality/testing/rendering-and-querying.md) · Intermediate · 12 min
- [User-Event Simulation](../docs/05-reliability-quality/testing/user-event-simulation.md) · Intermediate · 12 min
- [Accessibility-Tree Assertions](../docs/05-reliability-quality/testing/accessibility-tree-assertions.md) · Intermediate · 15 min

### Performance Engineering

- [Rendering Cost & Re-renders](../docs/05-reliability-quality/performance/rendering-cost-and-re-renders.md) · Intermediate · 15 min
- [Long Tasks & Main-Thread Work](../docs/05-reliability-quality/performance/long-tasks-and-main-thread-work.md) · Intermediate · 15 min
- [Debounce, Throttle & Scheduling](../docs/05-reliability-quality/performance/debounce-throttle-and-scheduling.md) · Intermediate · 15 min
- [Offloading to Workers](../docs/05-reliability-quality/performance/offloading-to-workers.md) · Intermediate · 12 min

### Accessibility

- [WCAG Principles (POUR)](../docs/04-interface-engineering/accessibility/wcag-principles-pour.md) · Intermediate · 12 min
- [Conformance Levels](../docs/04-interface-engineering/accessibility/conformance-levels.md) · Intermediate · 12 min
- [The ARIA Model](../docs/04-interface-engineering/accessibility/the-aria-model.md) · Intermediate · 12 min
- [Accessible Name Computation](../docs/04-interface-engineering/accessibility/accessible-name-computation.md) · Intermediate · 15 min
- [WAI-ARIA Widget Patterns](../docs/04-interface-engineering/accessibility/wai-aria-widget-patterns.md) · Intermediate · 12 min
- [Accessible Forms](../docs/04-interface-engineering/accessibility/accessible-forms.md) · Intermediate · 12 min
- [Live Regions & Announcements](../docs/04-interface-engineering/accessibility/live-regions-and-announcements.md) · Intermediate · 15 min

---

[← All learning paths](README.md) · [Knowledge Map](../KNOWLEDGE_MAP.md) · [Dependency Graph](../GRAPH.md)

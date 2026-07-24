# Frontend Architect — Learning Path

> An engineer responsible for the structure, boundaries, and long-term evolution of a frontend system.

**Level:** Advanced · **Required:** 151 articles (~35.4 h) · **Optional:** 29 articles (~7.9 h)

Difficulty of required articles: Foundational 3 · Intermediate 102 · Advanced 40 · Staff 6.

Follow the sections in order. Articles link into [`docs/`](../docs/); each shows its difficulty and estimated reading time. Full prerequisites for any article are in its domain's `graph.json` (see [GRAPH.md](../GRAPH.md)).

## Milestones

1. Define module boundaries and dependency direction that scale
2. Choose rendering and data-fetching boundaries deliberately
3. Design API contracts and a versioned design system
4. Structure a monorepo with package and build architecture
5. Record and defend architectural decisions

## Expected skills

By completing the required articles you should be able to:

- System structure, boundaries, and dependency management
- Rendering, state, and data architecture
- Design-system and package architecture
- Trade-off analysis and technical direction

## Required articles

### Frontend Architecture

- [Separation of Concerns](../docs/03-application-architecture/architecture/separation-of-concerns.md) · Intermediate · 12 min
- [Layered Architecture](../docs/03-application-architecture/architecture/layered-architecture.md) · Intermediate · 12 min
- [Module Boundaries](../docs/03-application-architecture/architecture/module-boundaries.md) · Intermediate · 12 min
- [Dependency Direction & Inversion](../docs/03-application-architecture/architecture/dependency-direction-and-inversion.md) · Intermediate · 15 min
- [Feature-Based Structure](../docs/03-application-architecture/architecture/feature-based-structure.md) · Intermediate · 12 min
- [Domain-Driven Frontend](../docs/03-application-architecture/architecture/domain-driven-frontend.md) · Intermediate · 12 min
- [Colocation Principles](../docs/03-application-architecture/architecture/colocation-principles.md) · Intermediate · 12 min
- [Micro-Frontends](../docs/03-application-architecture/architecture/micro-frontends.md) · Advanced · 16 min
- [Module Federation](../docs/03-application-architecture/architecture/module-federation.md) · Advanced · 16 min
- [Shared Kernel & Contracts](../docs/03-application-architecture/architecture/shared-kernel-and-contracts.md) · Advanced · 16 min
- [Rendering Boundaries](../docs/03-application-architecture/architecture/rendering-boundaries.md) · Intermediate · 12 min
- [Data-Fetching Boundaries](../docs/03-application-architecture/architecture/data-fetching-boundaries.md) · Intermediate · 12 min
- [Client/Server Split](../docs/03-application-architecture/architecture/client-server-split.md) · Intermediate · 12 min
- [Architectural Decision Records](../docs/03-application-architecture/architecture/architectural-decision-records.md) · Intermediate · 15 min
- [Trade-off Analysis](../docs/03-application-architecture/architecture/trade-off-analysis.md) · Intermediate · 12 min
- [Evolutionary Architecture](../docs/03-application-architecture/architecture/evolutionary-architecture.md) · Intermediate · 12 min

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
- [Store-Based Libraries](../docs/03-application-architecture/state-management/store-based-libraries.md) · Intermediate · 12 min
- [Atom-Based Libraries](../docs/03-application-architecture/state-management/atom-based-libraries.md) · Intermediate · 12 min
- [Proxy-Based Reactivity](../docs/03-application-architecture/state-management/proxy-based-reactivity.md) · Intermediate · 12 min

### Data & Server State

- [Fetch-on-Render vs Render-as-You-Fetch](../docs/03-application-architecture/data-server-state/fetch-on-render-vs-render-as-you-fetch.md) · Intermediate · 15 min
- [Parallel vs Waterfall Requests](../docs/03-application-architecture/data-server-state/parallel-vs-waterfall-requests.md) · Intermediate · 15 min
- [Request Deduplication](../docs/03-application-architecture/data-server-state/request-deduplication.md) · Intermediate · 12 min
- [Data Prefetching](../docs/03-application-architecture/data-server-state/data-prefetching.md) · Intermediate · 12 min
- [Cache Keys & Query Identity](../docs/03-application-architecture/data-server-state/cache-keys-and-query-identity.md) · Intermediate · 15 min
- [Staleness & Revalidation](../docs/03-application-architecture/data-server-state/staleness-and-revalidation.md) · Intermediate · 12 min
- [Cache Invalidation](../docs/03-application-architecture/data-server-state/cache-invalidation.md) · Intermediate · 12 min
- [Background Refetching](../docs/03-application-architecture/data-server-state/background-refetching.md) · Intermediate · 12 min
- [Normalizing Server Responses](../docs/03-application-architecture/data-server-state/normalizing-server-responses.md) · Intermediate · 15 min
- [Client-Side Relations](../docs/03-application-architecture/data-server-state/client-side-relations.md) · Intermediate · 12 min
- [Derived Server Data](../docs/03-application-architecture/data-server-state/derived-server-data.md) · Intermediate · 12 min
- [Retries & Backoff](../docs/03-application-architecture/data-server-state/retries-and-backoff.md) · Intermediate · 12 min
- [Loading & Error States](../docs/03-application-architecture/data-server-state/loading-and-error-states.md) · Intermediate · 12 min
- [Offline & Local-First Sync](../docs/03-application-architecture/data-server-state/offline-and-local-first-sync.md) · Intermediate · 12 min

### API Design & Contracts

- [REST](../docs/03-application-architecture/api-design/rest.md) · Advanced · 16 min
- [GraphQL](../docs/03-application-architecture/api-design/graphql.md) · Advanced · 16 min
- [RPC](../docs/03-application-architecture/api-design/rpc.md) · Advanced · 16 min
- [Realtime & Subscriptions](../docs/03-application-architecture/api-design/realtime-and-subscriptions.md) · Advanced · 16 min
- [Resource & Schema Design](../docs/03-application-architecture/api-design/resource-and-schema-design.md) · Advanced · 16 min
- [Versioning Strategies](../docs/03-application-architecture/api-design/versioning-strategies.md) · Advanced · 16 min
- [Pagination & Filtering Conventions](../docs/03-application-architecture/api-design/pagination-and-filtering-conventions.md) · Advanced · 19 min
- [Error Contract Design](../docs/03-application-architecture/api-design/error-contract-design.md) · Advanced · 16 min
- [End-to-End Type Safety (tRPC)](../docs/03-application-architecture/api-design/end-to-end-type-safety-trpc.md) · Advanced · 19 min
- [Code Generation from Schemas](../docs/03-application-architecture/api-design/code-generation-from-schemas.md) · Advanced · 19 min
- [Contract Testing](../docs/03-application-architecture/api-design/contract-testing.md) · Advanced · 16 min
- [Backend-for-Frontend](../docs/03-application-architecture/api-design/backend-for-frontend.md) · Advanced · 16 min
- [API Gateways & Aggregation](../docs/03-application-architecture/api-design/api-gateways-and-aggregation.md) · Advanced · 16 min
- [Response Shaping](../docs/03-application-architecture/api-design/response-shaping.md) · Advanced · 16 min

### Rendering Architectures

- [The CSR Model](../docs/02-rendering-frameworks/rendering-architectures/the-csr-model.md) · Intermediate · 12 min
- [The App Shell Pattern](../docs/02-rendering-frameworks/rendering-architectures/the-app-shell-pattern.md) · Intermediate · 12 min
- [Client-Side Data Loading](../docs/02-rendering-frameworks/rendering-architectures/client-side-data-loading.md) · Intermediate · 12 min
- [The SSR Model](../docs/02-rendering-frameworks/rendering-architectures/the-ssr-model.md) · Intermediate · 12 min
- [Hydration](../docs/02-rendering-frameworks/rendering-architectures/hydration.md) · Intermediate · 12 min
- [Selective & Progressive Hydration](../docs/02-rendering-frameworks/rendering-architectures/selective-and-progressive-hydration.md) · Intermediate · 15 min
- [Hydration Mismatches](../docs/02-rendering-frameworks/rendering-architectures/hydration-mismatches.md) · Intermediate · 12 min
- [Static Site Generation](../docs/02-rendering-frameworks/rendering-architectures/static-site-generation.md) · Intermediate · 12 min
- [Incremental Static Regeneration](../docs/02-rendering-frameworks/rendering-architectures/incremental-static-regeneration.md) · Intermediate · 15 min
- [On-Demand Revalidation](../docs/02-rendering-frameworks/rendering-architectures/on-demand-revalidation.md) · Intermediate · 12 min
- [Streaming SSR](../docs/02-rendering-frameworks/rendering-architectures/streaming-ssr.md) · Advanced · 16 min
- [Progressive Rendering & Flushing](../docs/02-rendering-frameworks/rendering-architectures/progressive-rendering-and-flushing.md) · Advanced · 19 min
- [Out-of-Order Streaming](../docs/02-rendering-frameworks/rendering-architectures/out-of-order-streaming.md) · Advanced · 16 min
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

### Design Systems

- [Design Primitives](../docs/04-interface-engineering/design-systems/design-primitives.md) · Intermediate · 12 min
- [Spacing & Layout Scales](../docs/04-interface-engineering/design-systems/spacing-and-layout-scales.md) · Intermediate · 12 min
- [Elevation & Surfaces](../docs/04-interface-engineering/design-systems/elevation-and-surfaces.md) · Intermediate · 12 min
- [Token Architecture](../docs/04-interface-engineering/design-systems/token-architecture.md) · Intermediate · 12 min
- [Semantic Token Layers](../docs/04-interface-engineering/design-systems/semantic-token-layers.md) · Intermediate · 12 min
- [Token Transformation & Distribution](../docs/04-interface-engineering/design-systems/token-transformation-and-distribution.md) · Intermediate · 15 min
- [Light/Dark & Color Modes](../docs/04-interface-engineering/design-systems/light-dark-and-color-modes.md) · Intermediate · 12 min
- [Multi-Brand Theming](../docs/04-interface-engineering/design-systems/multi-brand-theming.md) · Intermediate · 12 min
- [Runtime vs Build-Time Theming](../docs/04-interface-engineering/design-systems/runtime-vs-build-time-theming.md) · Intermediate · 15 min
- [Contribution Model](../docs/04-interface-engineering/design-systems/contribution-model.md) · Intermediate · 12 min
- [Versioning & Deprecation](../docs/04-interface-engineering/design-systems/versioning-and-deprecation.md) · Intermediate · 12 min
- [Breaking Changes & Migration](../docs/04-interface-engineering/design-systems/breaking-changes-and-migration.md) · Intermediate · 15 min
- [Usage Guidelines](../docs/04-interface-engineering/design-systems/usage-guidelines.md) · Intermediate · 12 min
- [Living Docs & Playgrounds](../docs/04-interface-engineering/design-systems/living-docs-and-playgrounds.md) · Intermediate · 12 min
- [Adoption & Coverage Metrics](../docs/04-interface-engineering/design-systems/adoption-and-coverage-metrics.md) · Intermediate · 15 min

### Package Architecture

- [Dependency Resolution](../docs/06-engineering-systems/package-architecture/dependency-resolution.md) · Advanced · 16 min
- [Lockfiles & Determinism](../docs/06-engineering-systems/package-architecture/lockfiles-and-determinism.md) · Advanced · 16 min
- [Node Modules & Hoisting Models](../docs/06-engineering-systems/package-architecture/node-modules-and-hoisting-models.md) · Advanced · 19 min
- [Exports Map & Entry Points](../docs/06-engineering-systems/package-architecture/exports-map-and-entry-points.md) · Advanced · 16 min
- [Module Formats (ESM/CJS/UMD)](../docs/06-engineering-systems/package-architecture/module-formats-esm-cjs-umd.md) · Advanced · 19 min
- [Conditional & Dual Exports](../docs/06-engineering-systems/package-architecture/conditional-and-dual-exports.md) · Advanced · 16 min
- [Types Distribution](../docs/06-engineering-systems/package-architecture/types-distribution.md) · Advanced · 16 min
- [Semantic Versioning](../docs/06-engineering-systems/package-architecture/semantic-versioning.md) · Advanced · 16 min
- [Release Automation & Changelogs](../docs/06-engineering-systems/package-architecture/release-automation-and-changelogs.md) · Advanced · 19 min
- [Provenance & Signing](../docs/06-engineering-systems/package-architecture/provenance-and-signing.md) · Advanced · 16 min
- [Peer Dependencies](../docs/06-engineering-systems/package-architecture/peer-dependencies.md) · Advanced · 16 min
- [Bundling vs Externalizing](../docs/06-engineering-systems/package-architecture/bundling-vs-externalizing.md) · Advanced · 16 min
- [Dependency Hygiene & Updates](../docs/06-engineering-systems/package-architecture/dependency-hygiene-and-updates.md) · Advanced · 19 min

### Build Systems & Tooling

- [The Dependency Graph](../docs/06-engineering-systems/build-tooling/the-dependency-graph.md) · Intermediate · 12 min
- [Bundler Models](../docs/06-engineering-systems/build-tooling/bundler-models.md) · Intermediate · 12 min
- [Entry Points & Output](../docs/06-engineering-systems/build-tooling/entry-points-and-output.md) · Intermediate · 12 min
- [Tree Shaking](../docs/06-engineering-systems/build-tooling/tree-shaking.md) · Intermediate · 12 min
- [Dead Code Elimination](../docs/06-engineering-systems/build-tooling/dead-code-elimination.md) · Intermediate · 12 min
- [Chunking & Split Points](../docs/06-engineering-systems/build-tooling/chunking-and-split-points.md) · Intermediate · 12 min
- [Scope Hoisting](../docs/06-engineering-systems/build-tooling/scope-hoisting.md) · Intermediate · 12 min

### Developer Experience & Workflow

- [Monorepo Architecture](../docs/06-engineering-systems/developer-experience/monorepo-architecture.md) · Intermediate · 12 min
- [Task Orchestration & Pipelines](../docs/06-engineering-systems/developer-experience/task-orchestration-and-pipelines.md) · Intermediate · 15 min
- [Workspace Dependency Graphs](../docs/06-engineering-systems/developer-experience/workspace-dependency-graphs.md) · Intermediate · 15 min
- [Remote Caching & Affected Builds](../docs/06-engineering-systems/developer-experience/remote-caching-and-affected-builds.md) · Intermediate · 15 min
- [CI Pipeline Design](../docs/06-engineering-systems/developer-experience/ci-pipeline-design.md) · Intermediate · 12 min
- [Build & Test Automation](../docs/06-engineering-systems/developer-experience/build-and-test-automation.md) · Intermediate · 12 min
- [Deployment Automation](../docs/06-engineering-systems/developer-experience/deployment-automation.md) · Intermediate · 12 min
- [Pipeline Caching & Speed](../docs/06-engineering-systems/developer-experience/pipeline-caching-and-speed.md) · Intermediate · 12 min

### TypeScript

- [Variance](../docs/01-core-languages/typescript/variance.md) · Intermediate · 12 min
- [Unsoundness & Escape Hatches](../docs/01-core-languages/typescript/unsoundness-and-escape-hatches.md) · Intermediate · 15 min
- [Strictness Flags](../docs/01-core-languages/typescript/strictness-flags.md) · Intermediate · 12 min
- [Branded & Nominal Types](../docs/01-core-languages/typescript/branded-and-nominal-types.md) · Foundational · 8 min
- [Exhaustiveness](../docs/01-core-languages/typescript/exhaustiveness.md) · Foundational · 8 min
- [Illegal States Unrepresentable](../docs/01-core-languages/typescript/illegal-states-unrepresentable.md) · Foundational · 11 min

### Engineering Practices

- [Abstraction & Leaky Abstractions](../docs/08-craft-leadership/engineering-practices/abstraction-and-leaky-abstractions.md) · Advanced · 19 min
- [Coupling & Cohesion](../docs/08-craft-leadership/engineering-practices/coupling-and-cohesion.md) · Advanced · 16 min
- [SOLID for Frontend](../docs/08-craft-leadership/engineering-practices/solid-for-frontend.md) · Advanced · 16 min
- [YAGNI & Simplicity](../docs/08-craft-leadership/engineering-practices/yagni-and-simplicity.md) · Advanced · 16 min
- [API & Interface Stability](../docs/08-craft-leadership/engineering-practices/api-and-interface-stability.md) · Advanced · 16 min
- [Backward Compatibility](../docs/08-craft-leadership/engineering-practices/backward-compatibility.md) · Advanced · 16 min
- [Deprecation Strategy](../docs/08-craft-leadership/engineering-practices/deprecation-strategy.md) · Advanced · 16 min

### Systems Thinking & Leadership

- [Trade-off Analysis](../docs/08-craft-leadership/systems-thinking-leadership/trade-off-analysis.md) · Staff · 20 min
- [Decision-Making Under Uncertainty](../docs/08-craft-leadership/systems-thinking-leadership/decision-making-under-uncertainty.md) · Staff · 23 min
- [Build vs Buy](../docs/08-craft-leadership/systems-thinking-leadership/build-vs-buy.md) · Staff · 20 min
- [Technical Design & RFCs](../docs/08-craft-leadership/systems-thinking-leadership/technical-design-and-rfcs.md) · Staff · 20 min
- [Setting Standards & Guardrails](../docs/08-craft-leadership/systems-thinking-leadership/setting-standards-and-guardrails.md) · Staff · 23 min
- [Driving Consistency at Scale](../docs/08-craft-leadership/systems-thinking-leadership/driving-consistency-at-scale.md) · Staff · 23 min

## Optional articles

### Security

- [Same-Origin Policy](../docs/05-reliability-quality/security/same-origin-policy.md) · Advanced · 16 min
- [CORS](../docs/05-reliability-quality/security/cors.md) · Advanced · 16 min
- [Isolation (COOP/COEP)](../docs/05-reliability-quality/security/isolation-coop-coep.md) · Advanced · 16 min

### Performance Engineering

- [Performance Budgets](../docs/05-reliability-quality/performance/performance-budgets.md) · Intermediate · 12 min
- [Regression Prevention & CI Gates](../docs/05-reliability-quality/performance/regression-prevention-and-ci-gates.md) · Intermediate · 15 min
- [Caching for Performance (cross-layer)](../docs/05-reliability-quality/performance/caching-for-performance-cross-layer.md) · Intermediate · 15 min

### Delivery & Infrastructure

- [Static Hosting](../docs/06-engineering-systems/delivery-infrastructure/static-hosting.md) · Advanced · 16 min
- [Server & SSR Hosting](../docs/06-engineering-systems/delivery-infrastructure/server-and-ssr-hosting.md) · Advanced · 16 min
- [Serverless Functions](../docs/06-engineering-systems/delivery-infrastructure/serverless-functions.md) · Advanced · 16 min
- [Edge Runtimes](../docs/06-engineering-systems/delivery-infrastructure/edge-runtimes.md) · Advanced · 16 min
- [CDN Architecture](../docs/06-engineering-systems/delivery-infrastructure/cdn-architecture.md) · Advanced · 16 min
- [Edge Compute & Routing](../docs/06-engineering-systems/delivery-infrastructure/edge-compute-and-routing.md) · Advanced · 16 min
- [Immutable Asset URLs](../docs/06-engineering-systems/delivery-infrastructure/immutable-asset-urls.md) · Advanced · 16 min
- [Environment Configuration](../docs/06-engineering-systems/delivery-infrastructure/environment-configuration.md) · Advanced · 16 min
- [Secrets Management](../docs/06-engineering-systems/delivery-infrastructure/secrets-management.md) · Advanced · 16 min
- [Feature Configuration](../docs/06-engineering-systems/delivery-infrastructure/feature-configuration.md) · Advanced · 16 min
- [Deployment Strategies (canary, blue-green)](../docs/06-engineering-systems/delivery-infrastructure/deployment-strategies-canary-blue-green.md) · Advanced · 19 min
- [Rollbacks & Kill Switches](../docs/06-engineering-systems/delivery-infrastructure/rollbacks-and-kill-switches.md) · Advanced · 16 min
- [Feature Flags](../docs/06-engineering-systems/delivery-infrastructure/feature-flags.md) · Advanced · 16 min
- [Progressive Delivery & Experiments](../docs/06-engineering-systems/delivery-infrastructure/progressive-delivery-and-experiments.md) · Advanced · 19 min
- [Scaling & Capacity](../docs/06-engineering-systems/delivery-infrastructure/scaling-and-capacity.md) · Advanced · 16 min
- [Cost Optimization](../docs/06-engineering-systems/delivery-infrastructure/cost-optimization.md) · Advanced · 16 min
- [Uptime & Health Checks](../docs/06-engineering-systems/delivery-infrastructure/uptime-and-health-checks.md) · Advanced · 16 min

### Observability & Reliability

- [Structured Logging](../docs/05-reliability-quality/observability/structured-logging.md) · Advanced · 16 min
- [Frontend Tracing & Spans](../docs/05-reliability-quality/observability/frontend-tracing-and-spans.md) · Advanced · 16 min
- [Custom Metrics & Events](../docs/05-reliability-quality/observability/custom-metrics-and-events.md) · Advanced · 16 min
- [On-Call & Alerting](../docs/05-reliability-quality/observability/on-call-and-alerting.md) · Staff · 20 min
- [Postmortems & RCA](../docs/05-reliability-quality/observability/postmortems-and-rca.md) · Staff · 20 min
- [Error Budgets & SLOs](../docs/05-reliability-quality/observability/error-budgets-and-slos.md) · Staff · 20 min

---

[← All learning paths](README.md) · [Knowledge Map](../KNOWLEDGE_MAP.md) · [Dependency Graph](../GRAPH.md)

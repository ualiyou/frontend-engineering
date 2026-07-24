# Testing Specialist — Learning Path

> An engineer who owns test strategy, quality gates, and confidence in shipping.

**Level:** Intermediate · **Required:** 57 articles (~12.3 h) · **Optional:** 15 articles (~3.5 h)

Difficulty of required articles: Intermediate 51 · Advanced 6.

Follow the sections in order. Articles link into [`docs/`](../docs/); each shows its difficulty and estimated reading time. Full prerequisites for any article are in its domain's `graph.json` (see [GRAPH.md](../GRAPH.md)).

## Milestones

1. Design a testing strategy across the pyramid/trophy
2. Write behavior-focused unit and component tests
3. Mock networks and test integration and data flows
4. Build reliable E2E and visual-regression suites
5. Gate quality in CI and tame flakiness

## Expected skills

By completing the required articles you should be able to:

- Test strategy and the right test at the right level
- Behavior-over-implementation testing
- Reliable E2E, visual, and contract testing
- Quality gates in CI and flakiness control

## Required articles

### Testing & Quality

- [The Testing Pyramid/Trophy](../docs/05-reliability-quality/testing/the-testing-pyramid-trophy.md) · Intermediate · 12 min
- [What to Test & Coverage Goals](../docs/05-reliability-quality/testing/what-to-test-and-coverage-goals.md) · Intermediate · 15 min
- [Test Doubles (mocks, stubs, fakes)](../docs/05-reliability-quality/testing/test-doubles-mocks-stubs-fakes.md) · Intermediate · 15 min
- [Pure Logic Testing](../docs/05-reliability-quality/testing/pure-logic-testing.md) · Intermediate · 12 min
- [Testing Hooks & Utilities](../docs/05-reliability-quality/testing/testing-hooks-and-utilities.md) · Intermediate · 12 min
- [Property-Based Testing](../docs/05-reliability-quality/testing/property-based-testing.md) · Intermediate · 12 min
- [Rendering & Querying](../docs/05-reliability-quality/testing/rendering-and-querying.md) · Intermediate · 12 min
- [User-Event Simulation](../docs/05-reliability-quality/testing/user-event-simulation.md) · Intermediate · 12 min
- [Accessibility-Tree Assertions](../docs/05-reliability-quality/testing/accessibility-tree-assertions.md) · Intermediate · 15 min
- [Testing with Real Providers](../docs/05-reliability-quality/testing/testing-with-real-providers.md) · Intermediate · 15 min
- [Network Mocking](../docs/05-reliability-quality/testing/network-mocking.md) · Intermediate · 12 min
- [Testing State & Data Flows](../docs/05-reliability-quality/testing/testing-state-and-data-flows.md) · Intermediate · 12 min
- [E2E User Flows](../docs/05-reliability-quality/testing/e2e-user-flows.md) · Intermediate · 12 min
- [Cross-Browser Testing](../docs/05-reliability-quality/testing/cross-browser-testing.md) · Intermediate · 12 min
- [Visual Regression Testing](../docs/05-reliability-quality/testing/visual-regression-testing.md) · Intermediate · 12 min
- [Flakiness & Determinism](../docs/05-reliability-quality/testing/flakiness-and-determinism.md) · Intermediate · 12 min
- [Test Performance & Parallelism](../docs/05-reliability-quality/testing/test-performance-and-parallelism.md) · Intermediate · 15 min
- [Test Maintenance](../docs/05-reliability-quality/testing/test-maintenance.md) · Intermediate · 12 min

### React

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

### Component & Interaction Design

- [Headless Components](../docs/04-interface-engineering/component-design/headless-components.md) · Intermediate · 12 min
- [Controlled vs Uncontrolled Pattern](../docs/04-interface-engineering/component-design/controlled-vs-uncontrolled-pattern.md) · Intermediate · 15 min
- [Compound Components](../docs/04-interface-engineering/component-design/compound-components.md) · Intermediate · 12 min
- [Render Props](../docs/04-interface-engineering/component-design/render-props.md) · Intermediate · 12 min
- [Loading & Skeleton States](../docs/04-interface-engineering/component-design/loading-and-skeleton-states.md) · Intermediate · 12 min
- [Empty States](../docs/04-interface-engineering/component-design/empty-states.md) · Intermediate · 12 min
- [Error & Retry States](../docs/04-interface-engineering/component-design/error-and-retry-states.md) · Intermediate · 12 min
- [Disabled & Busy States](../docs/04-interface-engineering/component-design/disabled-and-busy-states.md) · Intermediate · 12 min

### API Design & Contracts

- [End-to-End Type Safety (tRPC)](../docs/03-application-architecture/api-design/end-to-end-type-safety-trpc.md) · Advanced · 19 min
- [Code Generation from Schemas](../docs/03-application-architecture/api-design/code-generation-from-schemas.md) · Advanced · 19 min
- [Contract Testing](../docs/03-application-architecture/api-design/contract-testing.md) · Advanced · 16 min

### Developer Experience & Workflow

- [Linting](../docs/06-engineering-systems/developer-experience/linting.md) · Intermediate · 12 min
- [Formatting](../docs/06-engineering-systems/developer-experience/formatting.md) · Intermediate · 12 min
- [Type Checking in CI](../docs/06-engineering-systems/developer-experience/type-checking-in-ci.md) · Intermediate · 12 min
- [CI Pipeline Design](../docs/06-engineering-systems/developer-experience/ci-pipeline-design.md) · Intermediate · 12 min
- [Build & Test Automation](../docs/06-engineering-systems/developer-experience/build-and-test-automation.md) · Intermediate · 12 min
- [Deployment Automation](../docs/06-engineering-systems/developer-experience/deployment-automation.md) · Intermediate · 12 min
- [Pipeline Caching & Speed](../docs/06-engineering-systems/developer-experience/pipeline-caching-and-speed.md) · Intermediate · 12 min
- [Codemods & Migrations](../docs/06-engineering-systems/developer-experience/codemods-and-migrations.md) · Intermediate · 12 min
- [Scaffolding & Generators](../docs/06-engineering-systems/developer-experience/scaffolding-and-generators.md) · Intermediate · 12 min
- [Git Hooks & Pre-commit](../docs/06-engineering-systems/developer-experience/git-hooks-and-pre-commit.md) · Intermediate · 12 min

### Accessibility

- [Automated Auditing](../docs/04-interface-engineering/accessibility/automated-auditing.md) · Intermediate · 12 min
- [Manual & AT Testing](../docs/04-interface-engineering/accessibility/manual-and-at-testing.md) · Intermediate · 12 min

### Observability & Reliability

- [Client Error Capture](../docs/05-reliability-quality/observability/client-error-capture.md) · Advanced · 16 min
- [Source Maps & Symbolication](../docs/05-reliability-quality/observability/source-maps-and-symbolication.md) · Advanced · 19 min
- [Error Grouping & Alerting](../docs/05-reliability-quality/observability/error-grouping-and-alerting.md) · Advanced · 16 min

## Optional articles

### Forms & Validation

- [Client-Side Validation Strategies](../docs/03-application-architecture/forms-validation/client-side-validation-strategies.md) · Intermediate · 15 min
- [Schema Validation](../docs/03-application-architecture/forms-validation/schema-validation.md) · Intermediate · 12 min
- [Async & Server Validation](../docs/03-application-architecture/forms-validation/async-and-server-validation.md) · Intermediate · 12 min
- [Cross-Field Validation](../docs/03-application-architecture/forms-validation/cross-field-validation.md) · Intermediate · 12 min

### Performance Engineering

- [Performance Budgets](../docs/05-reliability-quality/performance/performance-budgets.md) · Intermediate · 12 min
- [Regression Prevention & CI Gates](../docs/05-reliability-quality/performance/regression-prevention-and-ci-gates.md) · Intermediate · 15 min
- [Caching for Performance (cross-layer)](../docs/05-reliability-quality/performance/caching-for-performance-cross-layer.md) · Intermediate · 15 min

### Security

- [Cross-Site Scripting (XSS)](../docs/05-reliability-quality/security/cross-site-scripting-xss.md) · Advanced · 16 min
- [DOM-Based XSS](../docs/05-reliability-quality/security/dom-based-xss.md) · Advanced · 16 min
- [HTML/Template Injection](../docs/05-reliability-quality/security/html-template-injection.md) · Advanced · 16 min
- [Sanitization & Encoding](../docs/05-reliability-quality/security/sanitization-and-encoding.md) · Advanced · 16 min

### State Management

- [The Reducer Pattern](../docs/03-application-architecture/state-management/the-reducer-pattern.md) · Intermediate · 12 min
- [Unidirectional Data Flow](../docs/03-application-architecture/state-management/unidirectional-data-flow.md) · Intermediate · 12 min
- [Event Sourcing & Commands](../docs/03-application-architecture/state-management/event-sourcing-and-commands.md) · Intermediate · 12 min
- [Modeling UI with State Machines](../docs/03-application-architecture/state-management/modeling-ui-with-state-machines.md) · Intermediate · 15 min

---

[← All learning paths](README.md) · [Knowledge Map](../KNOWLEDGE_MAP.md) · [Dependency Graph](../GRAPH.md)

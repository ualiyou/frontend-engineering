# Anti-Patterns Catalog

> The signature mistakes for each domain, in **symptom → why it fails → fix** form. Every article's `common_mistakes` links here (`anti-patterns/README.md#<domain>`) alongside its own in-article **Common Mistakes** section. This is the shared home for cross-cutting pitfalls so articles link the canonical entry instead of re-explaining it. As articles are written, promote a recurring pitfall into its own file under `anti-patterns/` and point the link at it.

## How this connects to the linking model

`Common Mistakes` is one of the five relation types defined in [`INTERNAL_LINKING.md`](../INTERNAL_LINKING.md). Each article carries two mistake links: the **domain entry below** (shared, catalog-owned) and the article's own `#common-mistakes` section (specific to that concept). Keep the domain entry to genuinely cross-cutting mistakes; keep concept-specific ones in the article.

## Domains

<a id="browser-apis"></a>

### Browser APIs

- **Feature-detecting by user-agent string instead of capability.** *Why it fails:* UA sniffing breaks the moment a browser changes its string or a new engine ships. *Fix:* Detect the capability directly (`'IntersectionObserver' in window`) and progressively enhance.
- **Never disconnecting observers or clearing timers.** *Why it fails:* Observers and timers hold references to detached DOM, leaking memory over a long session. *Fix:* Disconnect in teardown; tie lifetimes to component unmount / `AbortController`.
- **Assuming a permission is granted instead of querying it.** *Why it fails:* Storage, notifications, and sensors can be denied or evicted; blind use throws. *Fix:* Query permission state, handle denial as a first-class path, and degrade gracefully.

<a id="computer-science-for-frontend"></a>

### Computer Science for Frontend

- **Choosing a data structure by habit, not access pattern.** *Why it fails:* Linear scans over arrays where a Map is needed turn O(1) lookups into O(n) hot loops. *Fix:* Match structure to the dominant operation; measure with realistic sizes.
- **Ignoring amortized vs worst-case cost.** *Why it fails:* A cheap average hides a pathological resize/rehash that janks one frame badly. *Fix:* Reason about worst case for anything on the render path; batch and pre-size.
- **Mutating shared state instead of modeling change explicitly.** *Why it fails:* Aliased mutation makes diffing and time-travel impossible and hides bugs. *Fix:* Use immutable updates / structural sharing; model transitions as a state machine.

<a id="networking-protocols"></a>

### Networking & Protocols

- **Treating every request as independent of the cache.** *Why it fails:* Re-fetching immutable assets wastes RTTs and bandwidth on every navigation. *Fix:* Set correct `Cache-Control`/validators; version URLs for immutable content.
- **Waterfalling requests that could be parallel or preconnected.** *Why it fails:* Serial dependency chains multiply latency by round trips. *Fix:* Preconnect critical origins, parallelize independent fetches, use priority hints.
- **Picking WebSocket when SSE or polling would do.** *Why it fails:* A stateful socket adds reconnect, backpressure, and scaling cost you may not need. *Fix:* Choose the lightest transport that meets the real-time requirement.

<a id="runtime-execution"></a>

### Runtime & Execution

- **Writing megamorphic code that deopts the JIT.** *Why it fails:* Shape-unstable objects and polymorphic call sites defeat inline caches. *Fix:* Keep object shapes stable; avoid adding/deleting properties on hot objects.
- **Blocking the main thread with long synchronous tasks.** *Why it fails:* Tasks over ~50ms freeze input and animation. *Fix:* Chunk work, yield to the scheduler, or offload to a worker.
- **Ignoring retained references that defeat GC.** *Why it fails:* Closures over large structures and stray listeners keep memory alive forever. *Fix:* Break references on teardown; audit with heap snapshots.

<a id="the-web-platform"></a>

### The Web Platform

- **Fighting the document lifecycle instead of using its events.** *Why it fails:* Work started before parse or after bfcache restore runs at the wrong time. *Fix:* Hook the correct lifecycle event; treat bfcache restore as a real navigation.
- **Layout thrashing by interleaving reads and writes.** *Why it fails:* Alternating style reads and DOM writes forces synchronous reflow each iteration. *Fix:* Batch reads, then writes; use `requestAnimationFrame` for visual updates.
- **Assuming a single global environment.** *Why it fails:* Workers, iframes, and multiple realms don't share your globals or prototypes. *Fix:* Pass data across boundaries explicitly; never rely on cross-realm identity.

<a id="css-visual-systems"></a>

### CSS & Visual Systems

- **Specificity wars won with `!important`.** *Why it fails:* Escalating overrides make the cascade unpredictable and impossible to refactor. *Fix:* Flatten specificity; use layers/tokens and a single source of truth for styles.
- **Hard-coded magic numbers instead of tokens/relative units.** *Why it fails:* Pixel constants break theming, density, and responsive scaling. *Fix:* Consume design tokens and logical/relative units; centralize scale.
- **Layout built on floats/absolute hacks instead of flin/grid.** *Why it fails:* Brittle positioning collapses under content or locale changes. *Fix:* Use Flexbox/Grid and logical properties; let content drive size.

<a id="html-document-semantics"></a>

### HTML & Document Semantics

- **Div-soup where semantic elements exist.** *Why it fails:* Non-semantic markup loses built-in a11y, SEO, and default behavior. *Fix:* Use the right element (`button`, `nav`, `main`, headings) before reaching for ARIA.
- **ARIA bolted on to paper over bad markup.** *Why it fails:* Redundant or wrong ARIA is worse than none and misleads assistive tech. *Fix:* First rule of ARIA: use native semantics; add ARIA only for gaps.
- **Broken heading order and missing landmarks.** *Why it fails:* Screen-reader and SEO navigation depend on a coherent outline. *Fix:* Keep one H1 and a logical heading hierarchy; label landmarks.

<a id="javascript"></a>

### JavaScript

- **Relying on `==` and implicit coercion.** *Why it fails:* Loose equality and coercion produce surprising truthiness bugs. *Fix:* Use `===`, explicit conversion, and nullish operators.
- **Unhandled promise rejections and floating async.** *Why it fails:* Fire-and-forget async swallows errors and races. *Fix:* Await or `.catch()` every promise; cancel with `AbortController`.
- **Closures capturing stale or oversized state.** *Why it fails:* Captured variables leak memory or read outdated values. *Fix:* Capture the minimum; recreate handlers when dependencies change.

<a id="typescript"></a>

### TypeScript

- **`any` and unchecked casts as escape hatches.** *Why it fails:* `any` disables the type system exactly where risk is highest. *Fix:* Prefer `unknown` + narrowing; make illegal states unrepresentable.
- **Types that lie about runtime shape.** *Why it fails:* Casting API responses without validation gives false safety. *Fix:* Validate at the boundary (schema) and derive types from it.
- **Over-engineered generics nobody can read.** *Why it fails:* Excessive conditional/mapped types hurt inference and DX. *Fix:* Reach for the simplest type that captures the constraint.

<a id="react"></a>

### React

- **`useEffect` used as a data/derivation dumping ground.** *Why it fails:* Effects for derived state cause extra renders and sync bugs. *Fix:* Derive during render; use effects only for external synchronization.
- **Unstable references breaking memoization.** *Why it fails:* New object/function identities each render defeat `memo`/deps. *Fix:* Stabilize with `useMemo`/`useCallback` or lift state; trust the compiler where available.
- **Keys by index on reorderable lists.** *Why it fails:* Index keys reuse the wrong DOM/state on insert or reorder. *Fix:* Key by stable domain id.

<a id="reactivity-framework-models"></a>

### Reactivity & Framework Models

- **Assuming one framework's mental model applies to another.** *Why it fails:* Fine-grained signals and VDOM diffing have different update rules. *Fix:* Learn each model's reactivity boundary before optimizing.
- **Creating reactive dependencies you don't read.** *Why it fails:* Over-tracking triggers needless recomputation. *Fix:* Read only what a computation depends on; keep derivations pure.
- **Mutating reactive state outside the tracked path.** *Why it fails:* Untracked mutation desyncs the view. *Fix:* Update through the framework's reactive API.

<a id="rendering-architectures"></a>

### Rendering Architectures

- **Shipping everything client-side by default.** *Why it fails:* Blank-screen hydration hurts TTFB, SEO, and low-end devices. *Fix:* Choose SSR/SSG/streaming/edge per route from real constraints.
- **Hydration mismatch between server and client render.** *Why it fails:* Divergent output throws and re-renders the whole tree. *Fix:* Keep render deterministic; guard client-only branches.
- **Blocking the shell on non-critical data.** *Why it fails:* One slow query delays the whole page. *Fix:* Stream and defer non-critical regions.

<a id="routing"></a>

### Routing

- **Auth/route guards enforced only on the client.** *Why it fails:* Client-only guards are trivially bypassed. *Fix:* Enforce on the server/loader; treat client guards as UX only.
- **Losing scroll/focus on navigation.** *Why it fails:* SPA navigation breaks back-button and a11y expectations. *Fix:* Restore scroll and move focus to the new view.
- **State in ad-hoc globals instead of the URL.** *Why it fails:* Unshareable, un-bookmarkable, history-breaking state. *Fix:* Encode navigable state in the URL.

<a id="api-design-contracts"></a>

### API Design & Contracts

- **No versioning or contract, so clients break silently.** *Why it fails:* Unannounced shape changes break consumers in production. *Fix:* Version contracts; validate against a shared schema.
- **Over-/under-fetching baked into endpoints.** *Why it fails:* Rigid payloads force N+1 calls or waste bytes. *Fix:* Shape responses to real needs; consider field selection.
- **Errors returned as 200 with a body flag.** *Why it fails:* Hidden failures defeat retries, monitoring, and caching. *Fix:* Use correct status codes and a consistent error contract.

<a id="frontend-architecture"></a>

### Frontend Architecture

- **Big-ball-of-mud with no module boundaries.** *Why it fails:* Everything imports everything; change ripples everywhere. *Fix:* Define boundaries and dependency direction; enforce with lint rules.
- **Premature abstraction / speculative generality.** *Why it fails:* Frameworks-for-one-caller add cost with no payoff. *Fix:* Abstract on the third repetition, not the first.
- **Shared mutable singletons as a coupling backdoor.** *Why it fails:* Global state hides dependencies and breaks testing. *Fix:* Inject dependencies; keep modules pure at the edges.

<a id="data-server-state"></a>

### Data & Server State

- **Treating server cache as client state.** *Why it fails:* Duplicating server data in local stores causes staleness and races. *Fix:* Use a server-state cache (query lib) as the source of truth.
- **Optimistic updates without rollback.** *Why it fails:* A failed mutation leaves the UI lying. *Fix:* Pair optimistic writes with rollback and reconciliation.
- **Waterfalled queries and no cache keys.** *Why it fails:* Serial requests and cache misses tank perceived speed. *Fix:* Parallelize, set stable keys, and prefetch on intent.

<a id="forms-validation"></a>

### Forms & Validation

- **Validation only on the client.** *Why it fails:* Client checks are advisory; the server is the trust boundary. *Fix:* Validate on both sides from one shared schema.
- **Uncontrolled re-render storms on every keystroke.** *Why it fails:* Re-rendering the whole form per key hurts large forms. *Fix:* Isolate fields; validate on blur/submit where possible.
- **Inaccessible error messaging.** *Why it fails:* Errors not linked to inputs are invisible to AT. *Fix:* Associate messages with `aria-describedby` and move focus to the first error.

<a id="state-management"></a>

### State Management

- **Putting everything in one global store.** *Why it fails:* God-stores couple unrelated features and re-render broadly. *Fix:* Keep state local by default; lift only what's shared.
- **Prop drilling vs context misused.** *Why it fails:* Both extremes hurt: drilling is noisy, context re-renders too widely. *Fix:* Scope context narrowly; select slices to limit renders.
- **Derived state stored instead of computed.** *Why it fails:* Duplicated derived values drift out of sync. *Fix:* Compute derivations; store only the minimal source.

<a id="accessibility"></a>

### Accessibility

- **Keyboard users locked out.** *Why it fails:* Mouse-only handlers and missing focus traps exclude keyboard/AT users. *Fix:* Support full keyboard operation and visible focus.
- **Color contrast and meaning-by-color-alone.** *Why it fails:* Low contrast and color-only signals fail WCAG and many users. *Fix:* Meet contrast ratios; pair color with text/icon.
- **Testing a11y only with automated tools.** *Why it fails:* Automated checks catch ~a third of issues. *Fix:* Add manual keyboard and screen-reader passes.

<a id="animation-motion"></a>

### Animation & Motion

- **Animating layout properties instead of transform/opacity.** *Why it fails:* Animating width/top forces layout+paint every frame. *Fix:* Animate `transform`/`opacity`; promote with care.
- **Ignoring `prefers-reduced-motion`.** *Why it fails:* Motion can cause nausea and vestibular harm. *Fix:* Honor the reduced-motion preference.
- **Long main-thread animations that jank.** *Why it fails:* JS-driven animation competes with rendering. *Fix:* Use compositor-friendly animations / Web Animations API.

<a id="component-interaction-design"></a>

### Component & Interaction Design

- **Missing loading/empty/error/disabled states.** *Why it fails:* Happy-path-only components break on real data. *Fix:* Design all states explicitly; make busy/disabled clear.
- **Boolean-prop explosion instead of composition.** *Why it fails:* Dozens of flags create untestable combinatorics. *Fix:* Compose smaller components; prefer slots/children.
- **Uncontrolled/controlled ambiguity.** *Why it fails:* Mixing the two causes lost input and warnings. *Fix:* Pick one contract and document it.

<a id="design-systems"></a>

### Design Systems

- **Forking components instead of extending tokens.** *Why it fails:* Copy-paste variants drift and multiply maintenance. *Fix:* Vary via tokens/props; keep one source component.
- **Tokens that encode raw values, not intent.** *Why it fails:* `blue-500` everywhere can't be re-themed. *Fix:* Use semantic tokens (`color-action`) mapped to primitives.
- **No adoption metrics.** *Why it fails:* You can't manage coverage you don't measure. *Fix:* Track adoption and deprecate old patterns deliberately.

<a id="observability-reliability"></a>

### Observability & Reliability

- **Logging everything and alerting on nothing actionable.** *Why it fails:* Noise buries signal; on-call fatigue sets in. *Fix:* Alert on SLO burn, not raw errors; make logs structured.
- **No error budget, so reliability is a vibe.** *Why it fails:* Without budgets, reliability vs velocity has no referee. *Fix:* Define SLOs and error budgets; let them gate releases.
- **Client errors invisible to the team.** *Why it fails:* Unmonitored front-end errors fail silently for users. *Fix:* Capture and sample front-end errors with context.

<a id="performance-engineering"></a>

### Performance Engineering

- **Optimizing without measuring first.** *Why it fails:* Guesswork optimizes the wrong thing and adds complexity. *Fix:* Profile with real traces/field data; fix the biggest cost.
- **Shipping large JS bundles eagerly.** *Why it fails:* Unused code delays interactivity on every load. *Fix:* Code-split, lazy-load, and budget bundle size.
- **Ignoring the cross-layer cache story.** *Why it fails:* Redundant work across network/memory/render. *Fix:* Cache at the right layer; invalidate on stable keys.

<a id="security"></a>

### Security

- **Trusting client input / rendering unsanitized HTML.** *Why it fails:* XSS via `innerHTML`/`dangerouslySetInnerHTML` is the classic breach. *Fix:* Sanitize/escape output; set a strict CSP.
- **Tokens in `localStorage` exposed to XSS.** *Why it fails:* Any script can exfiltrate them. *Fix:* Prefer httpOnly cookies with CSRF defense.
- **Client-side authorization as the only gate.** *Why it fails:* Anything enforced only in the browser is bypassable. *Fix:* Enforce authz on the server; the client is UX.

<a id="testing-quality"></a>

### Testing & Quality

- **Testing implementation details, not behavior.** *Why it fails:* Refactors break tests that assert internals. *Fix:* Test observable behavior from the user's perspective.
- **Over-mocking until tests prove nothing.** *Why it fails:* Mocks that mirror the code pass while prod fails. *Fix:* Mock at boundaries; favor integration coverage for critical flows.
- **Flaky tests tolerated.** *Why it fails:* Flake erodes trust and hides real failures. *Fix:* Fix or quarantine flakes; remove timing races.

<a id="build-systems-tooling"></a>

### Build Systems & Tooling

- **Non-deterministic or cache-busted builds.** *Why it fails:* Unstable output defeats caching and reproducibility. *Fix:* Make builds deterministic; key caches on real inputs.
- **One giant bundle, no boundaries.** *Why it fails:* No tree-shaking or splitting inflates output. *Fix:* Configure splitting, side-effect flags, and analysis.
- **Config sprawl copied between projects.** *Why it fails:* Drifted configs cause 'works on my machine'. *Fix:* Centralize shared config; pin toolchain versions.

<a id="delivery-infrastructure"></a>

### Delivery & Infrastructure

- **Deploys with no rollback path.** *Why it fails:* A bad release with no exit means extended outage. *Fix:* Ship behind flags; keep instant rollback.
- **No health checks / readiness gating.** *Why it fails:* Traffic hits instances before they're ready. *Fix:* Add health/readiness probes to the rollout.
- **Big-bang releases instead of progressive rollout.** *Why it fails:* All-at-once blast radius is the whole userbase. *Fix:* Canary/percentage rollouts with monitoring.

<a id="developer-experience-workflow"></a>

### Developer Experience & Workflow

- **Skipping pre-commit checks locally.** *Why it fails:* Broken code reaches CI and blocks others. *Fix:* Run format/lint/type/test in fast git hooks.
- **Slow feedback loops tolerated.** *Why it fails:* Minutes-long rebuilds destroy flow. *Fix:* Invest in incremental builds and caching.
- **Undocumented tribal setup.** *Why it fails:* Onboarding takes days and breaks silently. *Fix:* Automate and document environment setup.

<a id="package-architecture"></a>

### Package Architecture

- **Dependency sprawl and unpinned versions.** *Why it fails:* Transitive bloat and surprise breakage. *Fix:* Audit deps, pin/lock versions, remove the unused.
- **Publishing without clear entry/exports/types.** *Why it fails:* Consumers get broken imports or no types. *Fix:* Define `exports`, types, and side-effect flags.
- **Ignoring semver in a shared package.** *Why it fails:* Silent breaking changes ripple to consumers. *Fix:* Follow semver; changeset every public change.

<a id="graphics-immersive"></a>

### Graphics & Immersive

- **Rebuilding the scene/allocating every frame.** *Why it fails:* GC pressure and redundant uploads tank FPS. *Fix:* Reuse buffers/geometry; update only what changed.
- **Ignoring device/context loss.** *Why it fails:* WebGL/WebGPU contexts can be lost at any time. *Fix:* Handle context-loss and restore resources.
- **No fallback for unsupported hardware.** *Why it fails:* Immersive features exclude low-end/denied devices. *Fix:* Detect support and degrade gracefully.

<a id="internationalization-localization"></a>

### Internationalization & Localization

- **Concatenating translated strings.** *Why it fails:* Word order and grammar differ per locale. *Fix:* Use message formatting with placeholders/plurals.
- **Assuming LTR, ASCII, and fixed widths.** *Why it fails:* RTL, CJK, and long translations break layout. *Fix:* Use logical properties; test RTL and long strings.
- **Hard-coding date/number/currency formats.** *Why it fails:* Formats vary by locale and cause misreads. *Fix:* Use `Intl` APIs and locale data.

<a id="progressive-cross-platform-web"></a>

### Progressive & Cross-Platform Web

- **Service worker that caches too aggressively.** *Why it fails:* Users get stuck on stale assets with no update path. *Fix:* Version caches and ship an update/activation flow.
- **Assuming online / ignoring offline states.** *Why it fails:* Feature breaks on flaky networks. *Fix:* Design offline-first with sync and clear status.
- **Native bridge trusted blindly.** *Why it fails:* Injected bridges are an attack and coupling surface. *Fix:* Validate bridge messages; keep the boundary thin.

<a id="engineering-practices"></a>

### Engineering Practices

- **Big-bang rewrites over incremental change.** *Why it fails:* Long-lived branches diverge and never land. *Fix:* Strangler-fig incrementally behind flags.
- **Removing APIs with no deprecation path.** *Why it fails:* Consumers break without warning. *Fix:* Deprecate with timelines, warnings, and migration docs.
- **Review theater instead of real review.** *Why it fails:* Rubber-stamped PRs let defects through. *Fix:* Review for correctness and design, not just style.

<a id="systems-thinking-leadership"></a>

### Systems Thinking & Leadership

- **Local optimization that harms the whole.** *Why it fails:* Team-level wins can create system-level bottlenecks. *Fix:* Optimize for the end-to-end outcome and feedback loops.
- **Innovation with no stability guardrails (or vice-versa).** *Why it fails:* All-new breaks trust; all-stable stagnates. *Fix:* Balance with explicit budgets and reversible bets.
- **Decisions with no recorded rationale.** *Why it fails:* Context is lost; the same debates recur. *Fix:* Record trade-offs (ADRs) so decisions are legible.

## Promoted anti-pattern pages

Recurring pitfalls that appear across multiple articles get their own file, in **symptom → why it fails → fix** form, linking back to the canonical article that documents the correct approach.

- [Treating server cache as client state](./server-cache-as-client-state.md) — Data & Server State.
- [Optimistic update without rollback](./optimistic-update-without-rollback.md) — Data & Server State.
- [Client-only validation](./client-only-validation.md) — Forms & Validation.
- [Validation re-render storm](./validation-rerender-storm.md) — Forms & Validation.
- [Inaccessible error messaging](./inaccessible-error-messaging.md) — Forms & Validation.

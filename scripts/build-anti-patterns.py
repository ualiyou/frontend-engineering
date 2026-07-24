#!/usr/bin/env python3
"""Generate anti-patterns/README.md — the domain-level pitfalls catalog that
every article's `common_mistakes` links into. Anchors are explicit so links
resolve identically on GitHub and in the validator."""
import os, glob, json, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def slug(dom): return re.sub(r"[^a-z0-9]+", "-", dom.lower()).strip("-")

# ordered domain list from the graphs (keeps Part order)
domains = [json.load(open(f))["domain"] for f in sorted(glob.glob(os.path.join(ROOT,"docs","*","*","graph.json")))]

# domain -> list of (mistake, why it fails, fix)
P = {
 "Browser APIs": [
  ("Feature-detecting by user-agent string instead of capability", "UA sniffing breaks the moment a browser changes its string or a new engine ships.", "Detect the capability directly (`'IntersectionObserver' in window`) and progressively enhance."),
  ("Never disconnecting observers or clearing timers", "Observers and timers hold references to detached DOM, leaking memory over a long session.", "Disconnect in teardown; tie lifetimes to component unmount / `AbortController`."),
  ("Assuming a permission is granted instead of querying it", "Storage, notifications, and sensors can be denied or evicted; blind use throws.", "Query permission state, handle denial as a first-class path, and degrade gracefully."),
 ],
 "Computer Science for Frontend": [
  ("Choosing a data structure by habit, not access pattern", "Linear scans over arrays where a Map is needed turn O(1) lookups into O(n) hot loops.", "Match structure to the dominant operation; measure with realistic sizes."),
  ("Ignoring amortized vs worst-case cost", "A cheap average hides a pathological resize/rehash that janks one frame badly.", "Reason about worst case for anything on the render path; batch and pre-size."),
  ("Mutating shared state instead of modeling change explicitly", "Aliased mutation makes diffing and time-travel impossible and hides bugs.", "Use immutable updates / structural sharing; model transitions as a state machine."),
 ],
 "Networking & Protocols": [
  ("Treating every request as independent of the cache", "Re-fetching immutable assets wastes RTTs and bandwidth on every navigation.", "Set correct `Cache-Control`/validators; version URLs for immutable content."),
  ("Waterfalling requests that could be parallel or preconnected", "Serial dependency chains multiply latency by round trips.", "Preconnect critical origins, parallelize independent fetches, use priority hints."),
  ("Picking WebSocket when SSE or polling would do", "A stateful socket adds reconnect, backpressure, and scaling cost you may not need.", "Choose the lightest transport that meets the real-time requirement."),
 ],
 "Runtime & Execution": [
  ("Writing megamorphic code that deopts the JIT", "Shape-unstable objects and polymorphic call sites defeat inline caches.", "Keep object shapes stable; avoid adding/deleting properties on hot objects."),
  ("Blocking the main thread with long synchronous tasks", "Tasks over ~50ms freeze input and animation.", "Chunk work, yield to the scheduler, or offload to a worker."),
  ("Ignoring retained references that defeat GC", "Closures over large structures and stray listeners keep memory alive forever.", "Break references on teardown; audit with heap snapshots."),
 ],
 "The Web Platform": [
  ("Fighting the document lifecycle instead of using its events", "Work started before parse or after bfcache restore runs at the wrong time.", "Hook the correct lifecycle event; treat bfcache restore as a real navigation."),
  ("Layout thrashing by interleaving reads and writes", "Alternating style reads and DOM writes forces synchronous reflow each iteration.", "Batch reads, then writes; use `requestAnimationFrame` for visual updates."),
  ("Assuming a single global environment", "Workers, iframes, and multiple realms don't share your globals or prototypes.", "Pass data across boundaries explicitly; never rely on cross-realm identity."),
 ],
 "CSS & Visual Systems": [
  ("Specificity wars won with `!important`", "Escalating overrides make the cascade unpredictable and impossible to refactor.", "Flatten specificity; use layers/tokens and a single source of truth for styles."),
  ("Hard-coded magic numbers instead of tokens/relative units", "Pixel constants break theming, density, and responsive scaling.", "Consume design tokens and logical/relative units; centralize scale."),
  ("Layout built on floats/absolute hacks instead of flin/grid", "Brittle positioning collapses under content or locale changes.", "Use Flexbox/Grid and logical properties; let content drive size."),
 ],
 "HTML & Document Semantics": [
  ("Div-soup where semantic elements exist", "Non-semantic markup loses built-in a11y, SEO, and default behavior.", "Use the right element (`button`, `nav`, `main`, headings) before reaching for ARIA."),
  ("ARIA bolted on to paper over bad markup", "Redundant or wrong ARIA is worse than none and misleads assistive tech.", "First rule of ARIA: use native semantics; add ARIA only for gaps."),
  ("Broken heading order and missing landmarks", "Screen-reader and SEO navigation depend on a coherent outline.", "Keep one H1 and a logical heading hierarchy; label landmarks."),
 ],
 "JavaScript": [
  ("Relying on `==` and implicit coercion", "Loose equality and coercion produce surprising truthiness bugs.", "Use `===`, explicit conversion, and nullish operators."),
  ("Unhandled promise rejections and floating async", "Fire-and-forget async swallows errors and races.", "Await or `.catch()` every promise; cancel with `AbortController`."),
  ("Closures capturing stale or oversized state", "Captured variables leak memory or read outdated values.", "Capture the minimum; recreate handlers when dependencies change."),
 ],
 "TypeScript": [
  ("`any` and unchecked casts as escape hatches", "`any` disables the type system exactly where risk is highest.", "Prefer `unknown` + narrowing; make illegal states unrepresentable."),
  ("Types that lie about runtime shape", "Casting API responses without validation gives false safety.", "Validate at the boundary (schema) and derive types from it."),
  ("Over-engineered generics nobody can read", "Excessive conditional/mapped types hurt inference and DX.", "Reach for the simplest type that captures the constraint."),
 ],
 "React": [
  ("`useEffect` used as a data/derivation dumping ground", "Effects for derived state cause extra renders and sync bugs.", "Derive during render; use effects only for external synchronization."),
  ("Unstable references breaking memoization", "New object/function identities each render defeat `memo`/deps.", "Stabilize with `useMemo`/`useCallback` or lift state; trust the compiler where available."),
  ("Keys by index on reorderable lists", "Index keys reuse the wrong DOM/state on insert or reorder.", "Key by stable domain id."),
 ],
 "Reactivity & Framework Models": [
  ("Assuming one framework's mental model applies to another", "Fine-grained signals and VDOM diffing have different update rules.", "Learn each model's reactivity boundary before optimizing."),
  ("Creating reactive dependencies you don't read", "Over-tracking triggers needless recomputation.", "Read only what a computation depends on; keep derivations pure."),
  ("Mutating reactive state outside the tracked path", "Untracked mutation desyncs the view.", "Update through the framework's reactive API."),
 ],
 "Rendering Architectures": [
  ("Shipping everything client-side by default", "Blank-screen hydration hurts TTFB, SEO, and low-end devices.", "Choose SSR/SSG/streaming/edge per route from real constraints."),
  ("Hydration mismatch between server and client render", "Divergent output throws and re-renders the whole tree.", "Keep render deterministic; guard client-only branches."),
  ("Blocking the shell on non-critical data", "One slow query delays the whole page.", "Stream and defer non-critical regions."),
 ],
 "Routing": [
  ("Auth/route guards enforced only on the client", "Client-only guards are trivially bypassed.", "Enforce on the server/loader; treat client guards as UX only."),
  ("Losing scroll/focus on navigation", "SPA navigation breaks back-button and a11y expectations.", "Restore scroll and move focus to the new view."),
  ("State in ad-hoc globals instead of the URL", "Unshareable, un-bookmarkable, history-breaking state.", "Encode navigable state in the URL."),
 ],
 "API Design & Contracts": [
  ("No versioning or contract, so clients break silently", "Unannounced shape changes break consumers in production.", "Version contracts; validate against a shared schema."),
  ("Over-/under-fetching baked into endpoints", "Rigid payloads force N+1 calls or waste bytes.", "Shape responses to real needs; consider field selection."),
  ("Errors returned as 200 with a body flag", "Hidden failures defeat retries, monitoring, and caching.", "Use correct status codes and a consistent error contract."),
 ],
 "Frontend Architecture": [
  ("Big-ball-of-mud with no module boundaries", "Everything imports everything; change ripples everywhere.", "Define boundaries and dependency direction; enforce with lint rules."),
  ("Premature abstraction / speculative generality", "Frameworks-for-one-caller add cost with no payoff.", "Abstract on the third repetition, not the first."),
  ("Shared mutable singletons as a coupling backdoor", "Global state hides dependencies and breaks testing.", "Inject dependencies; keep modules pure at the edges."),
 ],
 "Data & Server State": [
  ("Treating server cache as client state", "Duplicating server data in local stores causes staleness and races.", "Use a server-state cache (query lib) as the source of truth."),
  ("Optimistic updates without rollback", "A failed mutation leaves the UI lying.", "Pair optimistic writes with rollback and reconciliation."),
  ("Waterfalled queries and no cache keys", "Serial requests and cache misses tank perceived speed.", "Parallelize, set stable keys, and prefetch on intent."),
 ],
 "Forms & Validation": [
  ("Validation only on the client", "Client checks are advisory; the server is the trust boundary.", "Validate on both sides from one shared schema."),
  ("Uncontrolled re-render storms on every keystroke", "Re-rendering the whole form per key hurts large forms.", "Isolate fields; validate on blur/submit where possible."),
  ("Inaccessible error messaging", "Errors not linked to inputs are invisible to AT.", "Associate messages with `aria-describedby` and move focus to the first error."),
 ],
 "State Management": [
  ("Putting everything in one global store", "God-stores couple unrelated features and re-render broadly.", "Keep state local by default; lift only what's shared."),
  ("Prop drilling vs context misused", "Both extremes hurt: drilling is noisy, context re-renders too widely.", "Scope context narrowly; select slices to limit renders."),
  ("Derived state stored instead of computed", "Duplicated derived values drift out of sync.", "Compute derivations; store only the minimal source."),
 ],
 "Accessibility": [
  ("Keyboard users locked out", "Mouse-only handlers and missing focus traps exclude keyboard/AT users.", "Support full keyboard operation and visible focus."),
  ("Color contrast and meaning-by-color-alone", "Low contrast and color-only signals fail WCAG and many users.", "Meet contrast ratios; pair color with text/icon."),
  ("Testing a11y only with automated tools", "Automated checks catch ~a third of issues.", "Add manual keyboard and screen-reader passes."),
 ],
 "Animation & Motion": [
  ("Animating layout properties instead of transform/opacity", "Animating width/top forces layout+paint every frame.", "Animate `transform`/`opacity`; promote with care."),
  ("Ignoring `prefers-reduced-motion`", "Motion can cause nausea and vestibular harm.", "Honor the reduced-motion preference."),
  ("Long main-thread animations that jank", "JS-driven animation competes with rendering.", "Use compositor-friendly animations / Web Animations API."),
 ],
 "Component & Interaction Design": [
  ("Missing loading/empty/error/disabled states", "Happy-path-only components break on real data.", "Design all states explicitly; make busy/disabled clear."),
  ("Boolean-prop explosion instead of composition", "Dozens of flags create untestable combinatorics.", "Compose smaller components; prefer slots/children."),
  ("Uncontrolled/controlled ambiguity", "Mixing the two causes lost input and warnings.", "Pick one contract and document it."),
 ],
 "Design Systems": [
  ("Forking components instead of extending tokens", "Copy-paste variants drift and multiply maintenance.", "Vary via tokens/props; keep one source component."),
  ("Tokens that encode raw values, not intent", "`blue-500` everywhere can't be re-themed.", "Use semantic tokens (`color-action`) mapped to primitives."),
  ("No adoption metrics", "You can't manage coverage you don't measure.", "Track adoption and deprecate old patterns deliberately."),
 ],
 "Observability & Reliability": [
  ("Logging everything and alerting on nothing actionable", "Noise buries signal; on-call fatigue sets in.", "Alert on SLO burn, not raw errors; make logs structured."),
  ("No error budget, so reliability is a vibe", "Without budgets, reliability vs velocity has no referee.", "Define SLOs and error budgets; let them gate releases."),
  ("Client errors invisible to the team", "Unmonitored front-end errors fail silently for users.", "Capture and sample front-end errors with context."),
 ],
 "Performance Engineering": [
  ("Optimizing without measuring first", "Guesswork optimizes the wrong thing and adds complexity.", "Profile with real traces/field data; fix the biggest cost."),
  ("Shipping large JS bundles eagerly", "Unused code delays interactivity on every load.", "Code-split, lazy-load, and budget bundle size."),
  ("Ignoring the cross-layer cache story", "Redundant work across network/memory/render.", "Cache at the right layer; invalidate on stable keys."),
 ],
 "Security": [
  ("Trusting client input / rendering unsanitized HTML", "XSS via `innerHTML`/`dangerouslySetInnerHTML` is the classic breach.", "Sanitize/escape output; set a strict CSP."),
  ("Tokens in `localStorage` exposed to XSS", "Any script can exfiltrate them.", "Prefer httpOnly cookies with CSRF defense."),
  ("Client-side authorization as the only gate", "Anything enforced only in the browser is bypassable.", "Enforce authz on the server; the client is UX."),
 ],
 "Testing & Quality": [
  ("Testing implementation details, not behavior", "Refactors break tests that assert internals.", "Test observable behavior from the user's perspective."),
  ("Over-mocking until tests prove nothing", "Mocks that mirror the code pass while prod fails.", "Mock at boundaries; favor integration coverage for critical flows."),
  ("Flaky tests tolerated", "Flake erodes trust and hides real failures.", "Fix or quarantine flakes; remove timing races."),
 ],
 "Build Systems & Tooling": [
  ("Non-deterministic or cache-busted builds", "Unstable output defeats caching and reproducibility.", "Make builds deterministic; key caches on real inputs."),
  ("One giant bundle, no boundaries", "No tree-shaking or splitting inflates output.", "Configure splitting, side-effect flags, and analysis."),
  ("Config sprawl copied between projects", "Drifted configs cause 'works on my machine'.", "Centralize shared config; pin toolchain versions."),
 ],
 "Delivery & Infrastructure": [
  ("Deploys with no rollback path", "A bad release with no exit means extended outage.", "Ship behind flags; keep instant rollback."),
  ("No health checks / readiness gating", "Traffic hits instances before they're ready.", "Add health/readiness probes to the rollout."),
  ("Big-bang releases instead of progressive rollout", "All-at-once blast radius is the whole userbase.", "Canary/percentage rollouts with monitoring."),
 ],
 "Developer Experience & Workflow": [
  ("Skipping pre-commit checks locally", "Broken code reaches CI and blocks others.", "Run format/lint/type/test in fast git hooks."),
  ("Slow feedback loops tolerated", "Minutes-long rebuilds destroy flow.", "Invest in incremental builds and caching."),
  ("Undocumented tribal setup", "Onboarding takes days and breaks silently.", "Automate and document environment setup."),
 ],
 "Package Architecture": [
  ("Dependency sprawl and unpinned versions", "Transitive bloat and surprise breakage.", "Audit deps, pin/lock versions, remove the unused."),
  ("Publishing without clear entry/exports/types", "Consumers get broken imports or no types.", "Define `exports`, types, and side-effect flags."),
  ("Ignoring semver in a shared package", "Silent breaking changes ripple to consumers.", "Follow semver; changeset every public change."),
 ],
 "Graphics & Immersive": [
  ("Rebuilding the scene/allocating every frame", "GC pressure and redundant uploads tank FPS.", "Reuse buffers/geometry; update only what changed."),
  ("Ignoring device/context loss", "WebGL/WebGPU contexts can be lost at any time.", "Handle context-loss and restore resources."),
  ("No fallback for unsupported hardware", "Immersive features exclude low-end/denied devices.", "Detect support and degrade gracefully."),
 ],
 "Internationalization & Localization": [
  ("Concatenating translated strings", "Word order and grammar differ per locale.", "Use message formatting with placeholders/plurals."),
  ("Assuming LTR, ASCII, and fixed widths", "RTL, CJK, and long translations break layout.", "Use logical properties; test RTL and long strings."),
  ("Hard-coding date/number/currency formats", "Formats vary by locale and cause misreads.", "Use `Intl` APIs and locale data."),
 ],
 "Progressive & Cross-Platform Web": [
  ("Service worker that caches too aggressively", "Users get stuck on stale assets with no update path.", "Version caches and ship an update/activation flow."),
  ("Assuming online / ignoring offline states", "Feature breaks on flaky networks.", "Design offline-first with sync and clear status."),
  ("Native bridge trusted blindly", "Injected bridges are an attack and coupling surface.", "Validate bridge messages; keep the boundary thin."),
 ],
 "Engineering Practices": [
  ("Big-bang rewrites over incremental change", "Long-lived branches diverge and never land.", "Strangler-fig incrementally behind flags."),
  ("Removing APIs with no deprecation path", "Consumers break without warning.", "Deprecate with timelines, warnings, and migration docs."),
  ("Review theater instead of real review", "Rubber-stamped PRs let defects through.", "Review for correctness and design, not just style."),
 ],
 "Systems Thinking & Leadership": [
  ("Local optimization that harms the whole", "Team-level wins can create system-level bottlenecks.", "Optimize for the end-to-end outcome and feedback loops."),
  ("Innovation with no stability guardrails (or vice-versa)", "All-new breaks trust; all-stable stagnates.", "Balance with explicit budgets and reversible bets."),
  ("Decisions with no recorded rationale", "Context is lost; the same debates recur.", "Record trade-offs (ADRs) so decisions are legible."),
 ],
}

lines = []
lines.append("# Anti-Patterns Catalog\n")
lines.append("> The signature mistakes for each domain, in **symptom → why it fails → fix** form. "
             "Every article's `common_mistakes` links here (`anti-patterns/README.md#<domain>`) alongside its own "
             "in-article **Common Mistakes** section. This is the shared home for cross-cutting pitfalls so articles "
             "link the canonical entry instead of re-explaining it. As articles are written, promote a recurring "
             "pitfall into its own file under `anti-patterns/` and point the link at it.\n")
lines.append("## How this connects to the linking model\n")
lines.append("`Common Mistakes` is one of the five relation types defined in "
             "[`INTERNAL_LINKING.md`](../INTERNAL_LINKING.md). Each article carries two mistake links: the "
             "**domain entry below** (shared, catalog-owned) and the article's own `#common-mistakes` section "
             "(specific to that concept). Keep the domain entry to genuinely cross-cutting mistakes; keep concept-"
             "specific ones in the article.\n")
lines.append("## Domains\n")
for dom in domains:
    s = slug(dom)
    lines.append(f'<a id="{s}"></a>\n')
    lines.append(f"### {dom}\n")
    for mistake, why, fix in P.get(dom, []):
        lines.append(f"- **{mistake}.** *Why it fails:* {why} *Fix:* {fix}")
    lines.append("")

os.makedirs(os.path.join(ROOT, "anti-patterns"), exist_ok=True)
open(os.path.join(ROOT, "anti-patterns", "README.md"), "w").write("\n".join(lines) + "\n")
print("wrote anti-patterns/README.md for", len(domains), "domains; covered:", sum(1 for d in domains if d in P))

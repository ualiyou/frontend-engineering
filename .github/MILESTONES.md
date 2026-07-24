# Milestones

Frontend Engineering ships in versioned releases. Because it is a knowledge base, a "release" is a tagged snapshot of the content at a coherent level of completeness — readers can cite a version, and the changelog records what was added. Create these as GitHub Milestones and assign issues/PRs to them; the *Target release* field on the [project board](PROJECT_BOARD.md) mirrors them.

Article counts reference the [Article Inventory](../ARTICLE_INVENTORY.md).

---

## v0.1 — Foundation

**Goals.** Establish everything needed for others to contribute confidently: structure, standards, governance, and the full professional GitHub surface.

**Deliverables.**

- Repository structure, knowledge map, taxonomy, dependency graph, learning paths, article inventory, template, and cross-link strategy (done).
- Complete community layer: README, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, SUPPORT, GOVERNANCE, issue/PR templates, CODEOWNERS, FUNDING, CITATION.
- Label system, project board, milestones, topics, social preview, and CI workflows.

**Completion criteria.**

- A new contributor can go from "interested" to "merged PR" using only in-repo docs.
- All community-health files show green in GitHub's *Insights → Community Standards*.
- CI runs on every PR (lint, links, spelling, frontmatter).

---

## v0.2 — Core Articles

**Goals.** Seed the critical-priority Parts with high-value, peer-reviewed articles so the knowledge base is genuinely useful, not just scaffolded.

**Deliverables.**

- At least **3–5 published articles per domain** in Parts 00–03 and 05 (the Critical-priority Parts).
- Each article passes two-stage review and has synced `graph.json` + frontmatter.
- Domain index READMEs list their published articles.

**Completion criteria.**

- ≥ 40 published articles concentrated in the critical Parts.
- Every published article has resolved internal cross-links (no dangling typed relations).
- No domain in Parts 00–03 is empty.

---

## v0.3 — Examples

**Goals.** Attach minimal, runnable code to the reasoning so decisions are demonstrable, not just described.

**Deliverables.**

- `examples/` populated with focused illustrations tied to published articles.
- An example-validation workflow that builds/type-checks example code.
- Each relevant article links to its example(s) and vice versa.

**Completion criteria.**

- Every "Good Example / Bad Example" pair in a Critical-Part article has a corresponding runnable example where code is non-trivial.
- Example validation passes in CI.

---

## v0.4 — Recipes

**Goals.** Provide end-to-end solutions to recurring, cross-topic problems that a single article cannot cover.

**Deliverables.**

- `recipes/` populated with multi-step solutions (e.g. "choose and wire a data-fetching + caching strategy").
- Recipes cross-link to the articles whose decisions they compose.

**Completion criteria.**

- ≥ 10 published recipes, each referencing ≥ 2 articles.
- Each recipe states its assumptions, trade-offs, and when not to use it.

---

## v0.5 — Anti-patterns

**Goals.** Document the pitfalls that cause problems at scale, with honest "when this is actually fine" caveats.

**Deliverables.**

- `anti-patterns/` populated across domains, each with the failure mode, the cost at scale, the fix, and the exceptions.
- Anti-patterns linked from the "Common Mistakes" typed relation of related articles.

**Completion criteria.**

- ≥ 15 documented anti-patterns spanning at least 6 domains.
- Every anti-pattern is referenced by at least one article's cross-links.

---

## v1.0 — Stable

**Goals.** Reach a coherent, broadly useful, and maintainable first stable edition with a sustainable review cadence.

**Deliverables.**

- Meaningful coverage across **all nine Parts** (no empty domains).
- Cross-cutting decision guides connecting topics (e.g. "rendering strategy selection," "state strategy selection").
- A documented maintenance cadence and a stable release/versioning process.

**Completion criteria.**

- ≥ 120 published articles, ≥ 6 decision guides, examples/recipes/anti-patterns integrated via cross-links.
- Zero broken internal links; all frontmatter/graph metadata valid in CI.
- A published review schedule so entries stay current.

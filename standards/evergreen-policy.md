# Evergreen Policy

How **Frontend Engineering** stays true over years. "Evergreen" is a promise the repository makes to its readers: the guidance you find here has been kept current, not left to rot. This document defines the mechanisms that make that promise keepable at 1000+ documents — versioning, deprecation, review cadence, and how the repository absorbs breaking changes and framework churn without rewriting itself constantly.

The core idea, from [`content-framework.md`](./content-framework.md): **separate the timeless from the timely**, so the timely part can be refreshed cheaply while the timeless part stands.

## Table of contents

- [What "evergreen" means here](#what-evergreen-means-here)
- [Versioning policy](#versioning-policy)
- [Review frequency](#review-frequency)
- [Deprecation policy](#deprecation-policy)
- [Breaking changes](#breaking-changes)
- [Framework updates](#framework-updates)
- [Archived articles](#archived-articles)
- [Migration guides](#migration-guides)
- [The freshness contract](#the-freshness-contract)

## What "evergreen" means here

Not "never changes" — **"the core stays true while the surface is maintained on a schedule."** An article is evergreen when:

- Its thesis is anchored to a durable *problem*, not a tool.
- Its timeless parts (mental model, trade-off, failure mode) are separated in the prose from its timely parts (API names, version numbers, library picks), so the latter can be updated in isolation.
- It carries a `last_reviewed` date that has been renewed within its review window.

An old article that has not been reviewed is **not** evergreen; it is stale and flagged as such by the [freshness metric](./quality-metrics.md).

## Versioning policy

Two distinct version concepts, kept separate:

**1. Repository releases** (already in use). The repository ships citable snapshots (`v0.1`, `v0.2`, … `v1.0`) per [`.github/MILESTONES.md`](../.github/MILESTONES.md). A release is how a reader cites a stable state of the whole knowledge base.

**2. Article content version** (the optional `version` frontmatter field). Each article carries `MAJOR.MINOR`:

- **MINOR bump** — a correction, clarification, refreshed version pin, or added reference that does **not** change the recommendation. `1.2 → 1.3`.
- **MAJOR bump** — the *decision changed*: the recommendation, the mental model, or the trade-off balance is materially different. `1.3 → 2.0`. A MAJOR bump re-enters the [review pipeline](./review-process.md) at technical review, at least.
- **Slug is immutable across versions.** A new version updates the same file at the same URL; readers always land on the current thinking. If the *concept* changes so much it is a different article, create a new slug and deprecate the old one (below) — do not silently repurpose a URL.
- **`last_reviewed` moves on every bump;** `version` moves only on a content change (a pure re-review that confirms "still correct" bumps `last_reviewed` alone).

Adopt `version` when an article first publishes; before that it is simply absent.

## Review frequency

Every published article is re-verified on a cadence set by its **volatility**, not a single global timer — pinning React internals goes stale faster than explaining the box model.

| Volatility tier | Examples | Review window |
| --- | --- | --- |
| **High** | Framework-version-specific behavior, tooling config, "current best library for X" | every **6 months** |
| **Medium** | Framework-aware patterns, API-coupled techniques | every **12 months** |
| **Low** | Language fundamentals, browser platform, CS concepts, durable architecture trade-offs | every **24 months** |

- **The clock is `last_reviewed`.** An article whose `last_reviewed` is older than its window is **overdue** and surfaces in the freshness report; overdue articles are triaged first in maintenance.
- **Volatility is inferred, then curated:** `frameworks` non-empty and version pins present ⇒ High by default; framework-agnostic language/platform ⇒ Low; author/maintainer can override with a one-line reason.
- **A review is a real check**, not a date bump: re-verify the claims, re-run or re-read the examples against the current [baseline](./code-example-standard.md#baseline-versions), confirm links resolve, then set `last_reviewed`.

## Deprecation policy

An article is **deprecated** when its recommendation is no longer the right default but the content still has readers arriving at its URL from links and search. Deprecation is graceful, never a silent deletion.

- **Set `status: Deprecated`** and add a **deprecation banner** at the very top — an admonition stating what changed, when, and the replacement:

  ```markdown
  > [!WARNING]
  > **Deprecated (2026-07).** This approach is superseded by
  > [Server Components for Data Loading](./server-components-data-loading.md).
  > Kept for readers maintaining existing systems; do not adopt for new work.
  ```

- **Keep the URL alive.** Inbound links must not break; the page stays, clearly marked, and points forward.
- **Point to the replacement** and, if the migration is non-trivial, to a [migration guide](#migration-guides).
- **Deprecated articles leave active learning paths** and stop being offered as `next`/`alternatives`, but remain reachable.
- A deprecated article is reviewed less often (it is frozen guidance) but is **archived** once its audience of maintainers has plausibly moved on.

## Breaking changes

When the world changes underneath an article — a framework removes an API, a spec changes behavior, a recommended library is abandoned:

1. **Assess blast radius.** Which articles cite the changed thing? `grep` the version pins and references; the graph relations show the neighborhood.
2. **Classify each affected article:** does only the *timely* layer need updating (MINOR: refresh the pin and example), or did the *decision* change (MAJOR: re-review, possibly deprecate)?
3. **Prefer a surgical edit to a rewrite.** Because timeless and timely are separated in the prose, most breaking changes touch a few sentences and one example, not the thesis.
4. **Batch by change, not by article** where a single upstream change hits many pages, so the reasoning is applied consistently.
5. **Record it.** A breaking upstream change that shifts a recommendation is worth a decision record (ADR, see [`naming-conventions.md`](./naming-conventions.md#decision-records-adrs)) so future readers know *why* the guidance moved.

## Framework updates

Framework releases are the most frequent source of churn, so the policy is deliberately restrained:

- **The baseline lives in one place** — [`code-example-standard.md`](./code-example-standard.md#baseline-versions). A framework upgrade updates that table; articles inherit it and are only touched where behavior actually differs.
- **Do not chase every minor release.** Update the baseline on meaningful majors or when a widely-used API's behavior changes. A patch release rarely warrants any content change.
- **Version-pin only where behavior depends on the version** (the [evergreen rule](./content-framework.md#how-framework-specific-advice-is-handled)); everywhere else stay version-free so the article survives the upgrade untouched.
- **A framework's new feature does not automatically become a recommendation.** It is evaluated on its trade-offs, in the relevant article, the same as any option — new is not a synonym for better.
- **We never publish framework release notes.** "What's new in vN" is [forbidden content](./content-framework.md#what-must-never-appear); the durable *decision* a new feature enables may warrant an article, the announcement never does.

## Archived articles

**Archived** is the terminal state: the guidance is no longer relevant to any current reader (the technology is dead, or the decision no longer arises).

- **Set `status: Archived`** and move the file to an `archive/` area (or clearly mark it) while **keeping the URL resolvable** for historical and citation integrity.
- **Archived articles are excluded** from freshness scoring, learning paths, and all typed relations, but remain in the repository's history — we do not rewrite the past.
- **Archive rather than delete.** Deletion breaks links and erases the record of why a decision was once made; archiving preserves both.
- An archived article carries a one-line header explaining why it was archived and the date.

## Migration guides

When a recommendation changes in a way that leaves readers with existing code to move:

- **A migration guide is its own document** (a recipe-style file), linked from both the deprecated article and its replacement.
- **Named for the move:** `migrating-from-x-to-y.md` (see [`naming-conventions.md`](./naming-conventions.md)).
- **It is a decision aid, not just steps:** it states *whether* to migrate (the trade-off), *when* it is worth it, and *how* to do it incrementally with a rollback path — consistent with the repository's decisions-not-tutorials stance.
- Migration guides carry the same review cadence as High-volatility articles until the old approach is fully archived.

## The freshness contract

Every reader can trust that:

1. A **`Published`** article has been reviewed within its volatility window — or it is flagged **overdue**, visibly.
2. A **`Deprecated`** article tells you, at the top, what to use instead.
3. **No URL breaks.** Deprecated and archived pages stay reachable and point forward.
4. **The current thinking lives at the canonical URL** — you never have to guess which version is authoritative.
5. **Freshness is measured, not assumed** — the [freshness score](./quality-metrics.md#freshness-score) makes the contract auditable.

---

**Next:** [`review-process.md`](./review-process.md) — Stage 9 maintenance in the pipeline · [`quality-metrics.md`](./quality-metrics.md) — the freshness score · [`metadata-schema.md`](./metadata-schema.md) — `version`, `status`, and `last_reviewed`.

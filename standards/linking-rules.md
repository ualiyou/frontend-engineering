# Internal Linking Rules

How articles reference each other and the rest of the repository. The **five in-graph relations** (prerequisites, next, related, alternatives, common mistakes) are fully specified in [`INTERNAL_LINKING.md`](../INTERNAL_LINKING.md) — that document is canonical and this one does not restate it. This file adds the **authoring rules and the cross-collection references** (recipes, examples, anti-patterns, case studies, learning paths) that sit outside the article-to-article graph, so every kind of link in the repository has one written rule.

## Table of contents

- [The two link families](#the-two-link-families)
- [Universal link rules](#universal-link-rules)
- [The five typed article relations](#the-five-typed-article-relations)
- [Cross-collection references](#cross-collection-references)
- [Anti-pattern references](#anti-pattern-references)
- [Recipe references](#recipe-references)
- [Example references](#example-references)
- [Case study references](#case-study-references)
- [Learning path references](#learning-path-references)
- [The canonical-home rule](#the-canonical-home-rule)

## The two link families

Every link in an article is one of two kinds:

1. **Typed graph relations** — article-to-article edges that live in `graph.json`, are mirrored into frontmatter, and are validated by tooling. There are exactly five, defined in [`INTERNAL_LINKING.md`](../INTERNAL_LINKING.md). They power reading order, difficulty tiers, and the "what next / what instead" navigation.
2. **Cross-collection references** — links from an article into the other collections (`anti-patterns/`, `recipes/`, `examples/`, case studies, `paths/`). These are *not* part of the acyclic reading graph; they are supporting references. This document governs them.

Keeping the two families distinct is what keeps the reading graph small and acyclic while still letting an article point at everything a reader needs.

## Universal link rules

Apply to every link, both families.

- **Descriptive text, never a bare URL or "click here."** The link text names the destination.
- **Relative paths in-repo; absolute `https://` only for external sources.**
- **Link the canonical home of a concept; never re-explain it** (see the last section).
- **Same-domain article:** `[Text](./slug.md)`. **Cross-domain:** `[Text](../../<part>/<domain>/slug.md)`, and in prose name it `Article · Domain`.
- **No dead links** — CI (`scripts/validate-links.py`, the dead-link workflow) enforces this; genuine external exceptions go in [`.lycheeignore`](../.lycheeignore).
- **Deep-link to a heading** using its exact generated anchor (`./file.md#the-problem`).

## The five typed article relations

Summarized here for orientation only; the full model, cardinalities, and invariants are in [`INTERNAL_LINKING.md`](../INTERNAL_LINKING.md).

| Relation | Answers | Section | Frontmatter |
| --- | --- | --- | --- |
| **Prerequisites** | what to read before | `## Prerequisites` | `prerequisites` |
| **Next Articles** | where to go after | `## Next Articles` | `next` (derived) |
| **Related Articles** | what sits alongside | `## Related Articles` | `related` |
| **Alternative Approaches** | what to use instead | `## Alternative Approaches` | `alternatives` |
| **Common Mistakes** | how it goes wrong | `## Common Mistakes` | `common_mistakes` |

**Authoring rules that matter most:**

- **Prerequisites are the minimum that gates comprehension** — not every tangentially useful page. The set is a DAG and must stay acyclic.
- **Next is derived** (inverse of prerequisites), capped at 5. Fix a prerequisite rather than hand-editing `next`.
- **Related stays small (~3)** or it becomes a dumping ground.
- **Alternatives are true substitutes**, symmetric, each with an honest "wins when / weak when" in the Alternative Approaches table. `[]` is a valid, honest answer.
- **Common Mistakes links two targets:** the domain's anti-pattern catalog entry and the article's own `#common-mistakes` anchor.

## Cross-collection references

These four collections are referenced *from* articles but are not article-to-article graph edges. Each has a home directory and a reference convention.

| Collection | Home | What it holds | Referenced from |
| --- | --- | --- | --- |
| Anti-patterns | [`anti-patterns/`](../anti-patterns/) | Documented pitfalls, per domain and per named pattern | Common Mistakes section |
| Recipes | [`recipes/`](../recipes/) | End-to-end solutions to recurring problems | Good Example / Real-World Usage / See also |
| Examples | [`examples/`](../examples/) | Minimal, focused single-point illustrations | inline / How It Works |
| Case studies | `docs/**/case-studies/` (when present) | Applied narratives of a decision in a real system | Real-World Usage |
| Learning paths | [`paths/`](../paths/) | Curated role-based journeys across the map | (paths link to articles, not vice versa) |

## Anti-pattern references

- **Every article's Common Mistakes section links the domain's entry** in the shared catalog: `[the domain's anti-patterns](../../../anti-patterns/#<domain>)`, plus its own `#common-mistakes` anchor. This is a required typed relation (`common_mistakes`).
- **A recurring pitfall is promoted** from an inline mistake into its own file under `anti-patterns/` once it appears across multiple articles; links then point at that canonical file.
- **Anti-pattern files link back** to the canonical article that documents the correct approach ("the right way is described in …").
- The catalog is generated by `scripts/build-anti-patterns.py` with stable per-domain anchors — do not hand-edit anchors that links depend on.

## Recipe references

- **A recipe is an end-to-end solution**, not a concept. Articles reference a recipe from **Real-World Usage** or a "See also" line when a reader who understands the decision now wants a complete worked implementation: `[Recipe: Debounced Autocomplete with Cancellation](../../../recipes/debounced-autocomplete.md)`.
- **Recipes reference the articles they apply** in their own frontmatter/intro ("this recipe applies *Optimistic Updates* and *Cache Invalidation*"), so the concept remains canonical in the article and the recipe stays a consumer of it.
- **A recipe never becomes the canonical home of a concept** — if it starts explaining *why*, that reasoning belongs in an article and the recipe links to it.

## Example references

- **Examples illustrate one point** and are referenced inline or from **How It Works** where a minimal snippet aids the mental model: `[minimal example](../../../examples/abort-on-unmount.tsx)`.
- Prefer inlining a Level C fragment directly in the article for a small idea; link to `examples/` only when the snippet is large enough to distract from the prose.
- Examples do not carry reasoning; they carry code. The reasoning stays in the article.

## Case study references

Case studies do not yet exist as a collection; this defines the convention for when they are added.

- **A case study is a narrative:** "how team X applied decision Y in system Z, and what happened." It lives under the owning domain as `docs/<part>/<domain>/case-studies/<slug>.md`.
- **Articles reference case studies from Real-World Usage** as concrete evidence: `[Case study: Migrating a 200k-line app off global state](./case-studies/global-state-migration.md)`.
- **A case study links back to every article whose decision it exercises**, and names the versions/context so a reader can judge transferability.
- Case studies are dated and reviewed like articles; an undated case study is an anecdote, not a reference.

## Learning path references

- **Paths link to articles; articles do not link to paths.** A [`paths/`](../paths/) file curates an ordered journey across the map for a role; keeping the dependency one-way stops the article graph from coupling to editorial journeys.
- **A path references each step as a normal article link**, in reading order, with a one-line reason it belongs in that path.
- **When an article is renamed or moved, the paths that include it are updated** in the same change (link validation catches breakage).
- Paths draw their order from, and stay consistent with, the prerequisite DAG in [`GRAPH.md`](../GRAPH.md) — a path should never ask a reader to read B before its prerequisite A.

## The canonical-home rule

The single rule under all of the above: **every concept is explained in exactly one place, and everywhere else links to it.** A prerequisite, an alternative, a recipe, a case study — none of them re-explain a concept that has a home; they link the home. This is what keeps the graph acyclic, the content non-redundant, and a rename a one-file change instead of a hundred. When you find yourself explaining something a second time, stop and link the first.

---

**Next:** [`INTERNAL_LINKING.md`](../INTERNAL_LINKING.md) — the canonical five-relation model · [`metadata-schema.md`](./metadata-schema.md) — the frontmatter arrays · [`naming-conventions.md`](./naming-conventions.md) — how link targets are named.

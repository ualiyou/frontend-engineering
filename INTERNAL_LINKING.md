# Internal Linking Strategy

> How every article in **Frontend Engineering** connects to every other article. This document defines the wiki's link model: the five relation types each article carries, what each one means, how they are directed and bounded, the invariants that keep the graph trustworthy, and how the baseline is generated and then refined by authors. It is the companion design doc to [`GRAPH.md`](GRAPH.md) (the schema and reading order) and [`KNOWLEDGE_MAP.md`](KNOWLEDGE_MAP.md) (the taxonomy).

## Goal: behave like an engineering wiki

A reference wiki is not a linear book. A reader arrives at any article from search, follows a chain to fill a gap, compares an approach against its rivals, and leaves knowing what to read next. To support that, **every article is a node with five typed outbound relations**, so a reader can always move in the direction they need:

| Relation | Question it answers | Direction |
| --- | --- | --- |
| **Prerequisites** | "What must I understand *before* this?" | backward (up the dependency DAG) |
| **Next Articles** | "Where do I go *after* this?" | forward (down the dependency DAG) |
| **Related Articles** | "What sits *alongside* this?" | undirected (see-also) |
| **Alternative Approaches** | "What could I use *instead* of this?" | lateral (substitutes) |
| **Common Mistakes** | "How does this go *wrong*, and how do I spot it?" | outward (into the anti-pattern catalog) |

Together these turn 651 standalone pages into a navigable knowledge graph.

## The five relation types

### 1. Prerequisites — the dependency spine

The articles a reader should understand first. This is the load-bearing relation: it is a **directed acyclic graph (DAG)**, and it drives the recommended reading order (`order` in `graph.json`) and the difficulty tiers. Cross-domain prerequisites are written `Article · Domain`.

- **Cardinality:** 0–3 typically. A foundational root has none; most articles have 1–2.
- **Invariant:** acyclic. If A is a prerequisite of B, B can never be (transitively) a prerequisite of A.
- **Rule:** link the *minimum* set that genuinely gates comprehension, not every tangentially useful page.

### 2. Next Articles — the forward path

The exact **inverse of Prerequisites**: if X lists P as a prerequisite, then P lists X as a Next Article. This guarantees the two relations never disagree — a reader going forward retraces, in reverse, the chain someone else went backward through. It gives every article a "where to next" without hand-maintenance.

- **Cardinality:** capped at **5** most-relevant successors (by global reading order). Highly foundational nodes have many dependents; the cap keeps the list scannable while the full fan-out remains derivable from the DAG.
- **Continuity fallback:** a domain's final article has no dependents, so its Next points to the next article by reading order that is **not** already one of its own prerequisites — so no article is ever a dead end, and a Next edge never points backward into the reader's own ancestry.
- **Invariant:** every Next edge is either a true inverse-prerequisite edge or a forward continuity edge; it never creates a cycle.

### 3. Related Articles — see-also

Closely connected articles that are neither strictly before nor after: sibling concepts, complementary techniques, the same idea from another angle. Undirected and associative — the "you might also want" shelf. Kept small (≈3) so it stays meaningful rather than becoming a dumping ground.

### 4. Alternative Approaches — substitutes

The *other* viable ways to solve the same problem — the heart of trade-off thinking (Redux vs. Zustand vs. Jotai; REST vs. GraphQL; CSS Grid vs. Flexbox for a given layout). An Alternative competes with this article for the same job; a Related article merely neighbors it.

- **Baseline derivation:** two articles in the same topic (subcategory) are candidate alternatives when they **share the same prerequisite set** and neither depends on the other — i.e., they branch from the same starting point as parallel choices. Many articles legitimately have **none** (they are the only approach to their concept); an empty list is a valid, honest answer.
- **Symmetry invariant:** if A is an alternative of B, B is an alternative of A.
- **Authoring:** the generated set is a *candidate* list. When writing an article, prune any that are not true substitutes and add cross-topic rivals the structure can't see, then mirror the change in `graph.json`. Each alternative belongs in the article's **Alternatives & Comparisons** table with an honest "wins when / weak when."

### 5. Common Mistakes — the anti-patterns edge

Where this concept goes wrong in real code, in **symptom → why it fails → fix** form, so a reviewer can catch it and not just admire the good version. Modeled as *internal links*, not restated prose, so pitfalls live in one canonical place:

- Every article links to **two** targets: its domain's entry in the shared [`anti-patterns/`](anti-patterns/README.md) catalog (cross-cutting mistakes for the whole domain) and the article's own `## Common Mistakes` section (specific to this concept).
- As a pitfall recurs across articles, promote it into its own file under `anti-patterns/` and point the link there — the same "link the canonical home, never re-explain" rule the whole wiki follows.

## Where the links live

The **source of truth is each domain's `graph.json`.** Every node now carries five relation arrays:

```json
{
  "title": "Promises",
  "slug": "promises.md",
  "subcategory": "Asynchrony",
  "order": 164,
  "difficulty": "Foundational",
  "reading_time_min": 8,
  "prerequisites": ["The Callback Model", "Iterators & Iterables"],
  "related": ["The Callback Model", "async / await", "Cancellation & AbortController"],
  "next": ["async / await"],
  "alternatives": ["async / await", "Cancellation & AbortController"],
  "common_mistakes": ["anti-patterns/README.md#javascript", "#common-mistakes"]
}
```

Each article's Markdown **frontmatter mirrors these arrays**, and the body renders them as real Markdown links in the fixed sections defined by [`templates/article-template.md`](templates/article-template.md): *Prerequisites*, *Next Articles*, *Alternative Approaches*, *Common Mistakes*, and *Related Articles*. The rule is unchanged: **link the canonical home for a concept; never restate it.** Same-domain links use `[Text](./slug.md)`; cross-domain use `[Text](../../<part>/<domain>/slug.md)` and name it `Article · Domain` in prose.

A human-readable view of all five relations for every article is generated into [`INTERNAL_LINKS.md`](INTERNAL_LINKS.md).

## Reference convention

A link target is written as the bare **`Title`** when that title is globally unique, and as **`Title · Domain`** when the title exists in more than one domain (only *Trade-off Analysis* today). This matches the existing prerequisites/related data exactly, so nothing about how you write a reference changes.

## Generation and maintenance

The baseline is generated, then refined by authors — the same policy already applied to prerequisites and related edges.

- **`scripts/build-links.py`** reads all 35 `graph.json` files and derives `next`, `alternatives`, and `common_mistakes` deterministically from the existing prerequisite DAG and taxonomy. It is idempotent: re-running reproduces byte-identical output.
- **`scripts/build-anti-patterns.py`** generates the [`anti-patterns/`](anti-patterns/README.md) catalog with stable per-domain anchors that the `common_mistakes` links resolve to.
- **`scripts/validate-links.py`** enforces every invariant and must pass in CI:
  1. every reference resolves to a real node,
  2. the prerequisite graph is acyclic,
  3. `next` is sound — every edge is an inverse-prerequisite or a forward continuity edge, never pointing into the reader's own ancestry, capped at 5,
  4. no self-links,
  5. alternatives are symmetric,
  6. every `common_mistakes` catalog anchor exists.

When you write an article, edit its `graph.json` node and matching frontmatter, then run `build-links.py` (to refresh the inverse `next` edges) and `validate-links.py` before opening a PR. Adding or removing an article means updating the counts in [`GRAPH.md`](GRAPH.md).

## Design principles, in one place

1. **One source of truth.** Relations live in `graph.json`; frontmatter and prose mirror it; nothing is hand-synced twice without a check.
2. **Directions, not just links.** Backward (prerequisites), forward (next), lateral (alternatives), alongside (related), and outward (mistakes) are distinct so navigation has intent.
3. **Derive what you can, curate what you must.** `next` is a pure inverse and needs no curation; `alternatives` and `common_mistakes` ship as honest baselines that authors sharpen.
4. **Canonical homes.** Every concept is explained in exactly one place; everywhere else links to it. This keeps the graph acyclic, small, and accurate.
5. **No dead ends.** Every article offers a forward move and a way to compare, so a reader can always keep going.

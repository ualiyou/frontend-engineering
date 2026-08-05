<!--
============================================================================
 Frontend Engineering — Standard Article Template  (v2)
============================================================================
HOW TO USE
- Copy this file into the correct docs/<part>/<domain>/ folder (find it via the
  Knowledge Map) and rename it to the kebab-case form of the title,
  e.g. optimistic-updates.md.
- Fill in EVERY section and every frontmatter field. Do not delete sections.
  If a section genuinely does not apply, keep the heading and write one line
  explaining why (e.g. "No framework-specific behavior — pure DOM API").
- Keep the focus on engineering DECISIONS, patterns, and trade-offs — never a
  tutorial. Explain *why*, then *how*.
- Mirror the frontmatter into the domain's graph.json (difficulty, reading
  time, prerequisites, related, order) and keep the two in sync.
- See CONTRIBUTING.md for standards, naming, and review criteria, and
  templates/README.md for how each section maps to our eight goals.

AUTHORING RULES (delete this block before publishing)
- Exactly one H1 (# Title), matching frontmatter `title`.
- Put the primary keyword in the title, the description, and the first 100
  words. Write descriptive, question-shaped H2s — they are your SEO surface.
- Every cross-reference is a Markdown link. Same-domain: [Text](./slug.md).
  Cross-domain: [Text](../../<part>/<domain>/slug.md) and, in prose, name it
  as `Article · Domain`. Link the canonical home for a concept, never restate.
- Both code examples must be realistic and runnable — real error handling and
  edge cases, not toy snippets. Tag every fence with a language.
- US English. Prose over slides. One topic per file.
============================================================================
-->

<!-- markdownlint-disable MD007 MD032 -->
---
title: "Title in Human-Readable Title Case"
slug: kebab-case-slug
description: "150–160 character meta description that states the concept and the payoff. Leads with the primary keyword. This is the SEO snippet and the social preview."
keywords: ["primary keyword", "secondary keyword", "synonym or related term"]
part: "03 · Application Architecture"
domain: "Data & Server State"
subcategory: "Topic group from the domain README"
difficulty: "Intermediate"        # Foundational | Intermediate | Advanced | Staff
reading_time_min: 12
priority: "Critical"              # inherited from the Part
status: "Planned"                # Planned | Draft | In Review | Published
canonical: true                  # true = this file is the concept's one canonical home
last_reviewed: "2026-07-23"
prerequisites:                   # article titles; cross-domain as "Article · Domain"
  - "Prerequisite Article"
  - "Cross-Domain Prerequisite · JavaScript"
related:                         # closely connected articles (see-also, undirected)
  - "Related Article"
next:                            # read AFTER this — inverse of another article's prerequisites (≤5)
  - "Follow-on Article"
alternatives:                    # substitutes: other approaches to the SAME problem ([] if none)
  - "Competing Approach"
common_mistakes:                 # links into the anti-pattern catalog + this article's own section
  - "anti-patterns/README.md#data-server-state"
  - "#common-mistakes"
frameworks: ["react"]           # [] if framework-agnostic; name versions when behavior depends on them
og_image: "assets/slug-diagram.svg"   # optional social/OG image; omit if none
---
<!-- markdownlint-enable MD007 MD032 -->

# Title

> One-sentence summary of the decision or pattern this article documents — what it is and the payoff, in plain language.

**Part:** [03 · Application Architecture](../) · **Domain:** Data & Server State · **Priority:** Critical · **Difficulty:** Intermediate · **Reading time:** ~12 min

## TL;DR

Three to five sentences a busy engineer can act on without reading further. State the concept, the single most important trade-off, and the default recommendation. If a reader takes only this section away, they should still make the right call.

> **Recommendation:** State the defensible default in one line — "Use X when Y; prefer Z below N."

## At a Glance

| | |
| --- | --- |
| **Use when** | The two or three signals that make this the right choice. |
| **Avoid when** | The conditions where it adds cost or risk. |
| **Alternatives** | [Alternative A](#alternative-approaches), [Alternative B](#alternative-approaches) |
| **Primary risk** | The one failure mode to watch for. |
| **Maturity** | Stable / Emerging / Contested. |

## Prerequisites

What to read first, as links, so a newcomer can follow the dependency chain. Use `Article · Domain` in prose for cross-domain links.

- [Prerequisite Article](./prerequisite-article.md) — why it's needed here in a few words.
- [Cross-Domain Prerequisite](../../01-core-languages/javascript/cross-domain-prerequisite.md) (`· JavaScript`) — what it establishes.

## Overview

Define the pattern, technique, or decision in a few sentences, leading with the primary keyword. State the context in which it applies so a reader can tell at a glance whether this article is relevant to them. Draw the boundary: what this is, and what it is often confused with.

## The Problem

Describe the concrete engineering problem this addresses — including the failure modes, symptoms, or pain that arise without a deliberate approach. Ground it in a scenario a reader will recognize from a real codebase.

## Why It Matters

Explain the impact on real systems: maintainability, performance, correctness, security, accessibility, team velocity, user experience, or cost. Connect the abstract problem to consequences a team actually feels.

## How It Works

The mental model and mechanism. Explain how the pattern behaves step by step — enough that the reader can reason about new situations, not just copy code. A diagram belongs here (store it in `assets/` and give it descriptive alt text).

<!-- Optional: a small, focused illustrative snippet of the core idea. Full examples go in the Bad/Good sections below. -->

## When To Use

The conditions, signals, or system characteristics that make this approach the right choice. Be specific — thresholds, scale, team shape, data shape — not "when it makes sense."

## When NOT To Use

The situations where this approach adds unnecessary complexity, hurts performance, or is otherwise the wrong fit. Point to the alternative that wins in each case, linking to it.

## Common Mistakes

The `Common Mistakes` relation (see [`INTERNAL_LINKING.md`](../INTERNAL_LINKING.md)). The mistakes that show up around this concept, so a reader can spot them in review. For each: the symptom (what the code or behavior looks like), why it fails at scale, and the fix. This heading is the anchor the article's `common_mistakes` link points at (`#common-mistakes`); keep it. For cross-cutting pitfalls, link the domain's entry in the shared catalog: [`anti-patterns/README.md#<domain>`](../../../anti-patterns/). Promote a recurring pitfall into its own file under `anti-patterns/` and link it here.

### Mistake: Name the smell

- **Symptom:** What you see in the diff or in production.
- **Why it fails:** The mechanism by which it breaks, especially under load, concurrency, or growth.
- **Fix:** The corrected approach, linked to the relevant section or article.

### Mistake: Name the second smell

- **Symptom:** …
- **Why it fails:** …
- **Fix:** …

## Bad Example

An incorrect or naive approach as it commonly appears in the wild. Show realistic code, then explain specifically what goes wrong and why — tie it back to the common mistakes above.

```ts
// ❌ Naive approach — realistic, not a toy. Comment the exact line where it breaks.
```

**What goes wrong:** Name the failure mode explicitly (race condition, stale cache, memory leak, unhandled rejection, a11y break, N+1 request…).

## Good Example

A production-ready approach. The code handles errors, edge cases, cancellation, and cleanup as production code would. Explain why this version resolves the problems shown above.

```ts
// ✅ Production-ready — error handling, edge cases, and cleanup included.
```

**Why it's better:** Connect each change back to the specific problem it removes.

## Trade-offs

State advantages *and* disadvantages honestly; the recommendation must follow from them. Name what you trade away and the conditions under which the balance flips.

**Advantages**

- …

**Disadvantages**

- …

| Dimension | This approach | Cost / caveat |
| --- | --- | --- |
| Performance | … | … |
| Complexity | … | … |
| Maintainability | … | … |
| Failure behavior | … | … |

## Alternative Approaches

The `Alternative Approaches` relation (see [`INTERNAL_LINKING.md`](../INTERNAL_LINKING.md)): the other viable ways to solve the *same* problem and when each wins — the heart of the decision. An alternative *competes* with this article for the same job (unlike a Related article, which merely neighbors it). Keep the comparison honest, link each alternative to its own article, and mirror this list in the `alternatives` array in frontmatter and `graph.json`. If this concept has no true substitute, write one line saying so and leave `alternatives: []`.

| Approach | Best when | Weakness | See |
| --- | --- | --- | --- |
| This pattern | … | … | (this article) |
| [Alternative A](../../<part>/<domain>/alternative-a.md) | … | … | `Alternative A · Domain` |
| [Alternative B](../../<part>/<domain>/alternative-b.md) | … | … | `Alternative B · Domain` |

## Production Notes

What it takes to run this in production. Cover the relevant subset and delete lines that truly don't apply:

- **Performance & scale:** costs at 10×/100× data or traffic; where it degrades.
- **Observability:** what to log, the metric or trace that tells you it's working, the signal that it isn't.
- **Testing:** how to test this well (and what's flaky if you test it wrong).
- **Security & privacy:** injection, trust boundaries, data handling — if relevant.
- **Accessibility:** keyboard, focus, assistive-tech implications — if relevant.
- **Rollout & migration:** how to adopt incrementally and how to back out.

## Real-World Usage

Where this pattern shows up in production systems, libraries, or well-known codebases, and how teams apply it at scale. Name specific libraries/APIs and versions when behavior depends on them.

## Checklist

A practical checklist a reader can apply to their own code before shipping.

- [ ] …
- [ ] …
- [ ] …

## FAQ

Short answers to the questions engineers actually search for. Each question is a real query; each answer is two or three sentences. Great for learning and for search-result snippets.

**Q: Common question phrased as someone would search it?**
A: Direct, self-contained answer.

**Q: Second common question?**
A: Direct answer.

## Next Articles

The `Next Articles` relation (see [`INTERNAL_LINKING.md`](../INTERNAL_LINKING.md)): where to go *after* this, forward down the dependency graph. These are the articles that list this one as a prerequisite (its inverse), plus the natural continuation. Mirror the `next` array in frontmatter and `graph.json`; it is regenerated from prerequisites by `scripts/build-links.py`, so prefer fixing a prerequisite over hand-editing `next`.

- [Follow-on Article](./follow-on-article.md) — what it unlocks next.
- [Continuation](./continuation.md) — the natural next step in the path.

## Related Articles

The `Related Articles` relation: sibling concepts to explore alongside this one (see-also, neither strictly before nor after). Link the canonical home for each concept; never re-explain it here.

- [Related Article](./related-article.md) — how it connects.
- **Canonical home:** if this concept is owned elsewhere, say so and link it (e.g. "Caching is owned by `HTTP & CDN Caching Model · Networking & Protocols`").

## References

Primary sources — official docs, specifications, and authoritative write-ups. Prefer primary sources; the article must stand on its own without them.

- [Title](https://example.com) — short note on what it covers.

<!--
GRAPH SYNC — keep the domain's graph.json entry identical to this frontmatter:
{ "title", "slug", "subcategory", "order", "difficulty", "reading_time_min",
  "prerequisites": [...], "related": [...], "next": [...],
  "alternatives": [...], "common_mistakes": [...] }
After editing prerequisites/alternatives, run scripts/build-links.py (refreshes
the inverse `next` edges) and scripts/validate-links.py. Update GRAPH.md counts
if you add or remove an article. Every edge must point to an existing node and
the prerequisite graph must stay acyclic. See INTERNAL_LINKING.md for the model.
-->

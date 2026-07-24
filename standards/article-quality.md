# Article Quality Standard

The mandatory quality bar for every article in **Frontend Engineering**. This document turns the [content philosophy](./content-framework.md) into a concrete, enforceable checklist: the required sections, the **acceptance criteria** each must meet, and the **example quality levels** that govern how much rigor a code sample carries.

An article merges only when **every** required section is present and **every** acceptance criterion is met. Reviewers check against this file; see [`review-process.md`](./review-process.md).

> **Relationship to the template.** The canonical structure lives in [`templates/article-template.md`](../templates/article-template.md), which contributors copy. This file is the *specification* that template implements — it defines what each section must contain and how a reviewer decides it passes. If the template and this file ever diverge, fix the template.

## Table of contents

- [The required-section model](#the-required-section-model)
- [Section-by-section acceptance criteria](#section-by-section-acceptance-criteria)
- [Example quality levels (A / B / C)](#example-quality-levels)
- [The pre-merge checklist](#the-pre-merge-checklist)

## The required-section model

Every article carries the sections below, in this order. The middle column maps the **concept** each section covers (the vocabulary used in planning and review) to the **actual heading** used in the file, so there is exactly one source of truth for structure.

| Required concept | Heading in the article | Required? |
| --- | --- | --- |
| One-line summary | `>` blockquote under the H1 | Always |
| TL;DR + Recommendation | `## TL;DR` (+ `Recommendation` callout) | Always |
| At-a-glance decision table | `## At a Glance` | Always |
| Prerequisites | `## Prerequisites` | Always |
| **Overview** | `## Overview` | Always |
| **Problem** | `## The Problem` | Always |
| Engineering context / why it matters | `## Why It Matters` | Always |
| **Mental Model** | `## How It Works` | Always |
| Engineering context: when to apply | `## When To Use` / `## When NOT To Use` | Always |
| **Common Mistakes** | `## Common Mistakes` | Always |
| **Bad Example** | `## Bad Example` | Always |
| **Good Example** / Solution | `## Good Example` | Always |
| **Trade-offs** | `## Trade-offs` | Always |
| Alternative approaches | `## Alternative Approaches` | Always |
| **Performance / Accessibility / Security** considerations | `## Production Notes` | Always (a11y & perf always; security when applicable) |
| Real-world usage | `## Real-World Usage` | Always |
| **Checklist** | `## Checklist` | Always |
| FAQ | `## FAQ` | Always |
| Next reading | `## Next Articles` | Always |
| Related articles | `## Related Articles` | Always |
| **Further Reading + References** | `## References` | Always |

**Non-applicable sections are not deleted.** Keep the heading and write one line explaining why it does not apply (for example, under Production Notes: "No accessibility surface — this is a build-time transform with no rendered output"). A deleted section fails review; an honest one-line "not applicable" passes.

Security is the one *conditionally-populated* concern: it lives inside Production Notes and is **required whenever the topic touches** untrusted input, authentication, authorization, storage of sensitive data, `dangerouslySetInnerHTML`/raw HTML, URLs, redirects, third-party scripts, or serialization. When none of those apply, the security line states that explicitly.

## Section-by-section acceptance criteria

Each section passes only if it meets **all** of its criteria.

### One-line summary (blockquote under H1)

- One sentence, plain language, states the decision and its payoff.
- Contains the primary keyword. Readable on its own out of context.

### TL;DR + Recommendation

- Three to five sentences; a reader who stops here still makes the right call.
- States the concept, the single most important trade-off, and the default.
- Exactly one `Recommendation` callout, one line, **conditional** ("Use X when Y; prefer Z below N"). No unconditional recommendation.

### At a Glance

- A five-row table: **Use when**, **Avoid when**, **Alternatives** (as links), **Primary risk**, **Maturity** (Stable / Emerging / Contested).
- Each cell is scannable in seconds — a phrase, not a paragraph.
- Alternatives link to their own articles.

### Prerequisites

- Lists what to read first, each as a real link to its canonical home.
- Cross-domain links use the `Article · Domain` form in prose.
- Mirrors the `prerequisites` frontmatter and `graph.json`; the prerequisite graph stays acyclic.
- Empty only if the topic is genuinely foundational; then say so in one line.

### Overview

- Defines the pattern/decision in a few sentences, **primary keyword in the first 100 words**.
- Draws the boundary: what this is and what it is commonly confused with.
- States the context in which it applies, so a reader can self-select in or out.

### The Problem

- A concrete engineering problem, grounded in a scenario from a real codebase.
- Names the failure modes, symptoms, or pain that appear without a deliberate approach.
- Does not yet propose the solution — that is later. This section earns the solution.

### Why It Matters (engineering context)

- Connects the problem to consequences a team feels: correctness, performance, maintainability, security, accessibility, velocity, cost.
- Specific, not generic — names the actual impact, not "it's important."

### How It Works (mental model)

- Builds a mental model the reader can apply to situations the article never mentions.
- Explains the mechanism step by step, not just the API surface.
- Includes a diagram when the mechanism is non-trivial (see [`diagram-guide.md`](./diagram-guide.md)), stored in `assets/` with descriptive alt text.
- A reader who finishes this section can predict behavior in a new case.

### When To Use / When NOT To Use

- **Use:** specific signals — thresholds, scale, data shape, team shape — not "when it makes sense."
- **Not:** situations where it adds cost or risk, each pointing to the alternative that wins there.

### Common Mistakes

- At least two mistakes, each as **Symptom → Why it fails → Fix**.
- The `Why it fails` names the mechanism, especially under load, concurrency, or growth.
- Links the domain's entry in [`anti-patterns/`](../anti-patterns/README.md); recurring pitfalls are promoted to their own anti-pattern file.
- The heading is the anchor `#common-mistakes` that the frontmatter `common_mistakes` points at — do not rename it.

### Bad Example

- Realistic code a competent engineer would actually write — **not a strawman**.
- Language-tagged fence; the failing line is marked with a comment.
- Followed by a `What goes wrong` line naming the failure mode explicitly (race, stale cache, leak, unhandled rejection, a11y break, N+1…).
- Meets **Level B or higher** rigor for the parts that matter to the point (see levels below).

### Good Example (the solution)

- Production-ready: handles errors, edge cases, cancellation, and cleanup as real code would.
- Language-tagged fence; **Level A** rigor (see below).
- Followed by a `Why it's better` line tying each change to the specific problem it removes.
- Directly resolves the Bad Example — same scenario, corrected.

### Trade-offs

- **Advantages and disadvantages** listed with comparable depth. A thin disadvantages list fails.
- A cost table across at least: Performance, Complexity, Maintainability, Failure behavior.
- The Recommendation in the TL;DR is *derivable* from this section.
- Names the flip conditions — where the balance reverses.

### Alternative Approaches

- Each true substitute gets **Best when / Weakness / link** to its own article.
- Honest, no strawmen. Mirrors the `alternatives` frontmatter and `graph.json`.
- If there is no real substitute, one line says so and `alternatives: []`.

### Production Notes (performance, accessibility, security, operations)

- **Performance & scale:** behavior at 10×/100× data or traffic; where it degrades. Quantified where possible. **Always required.**
- **Accessibility:** keyboard, focus, ARIA, assistive-tech implications, or an explicit one-line "no accessibility surface" with the reason. **Always required.**
- **Security & privacy:** injection, trust boundaries, auth, data handling — **required whenever the trigger list above applies**; otherwise an explicit one-line "no security-relevant surface." Insecure snippets appear only as labeled Bad Examples.
- **Observability:** what to log, the signal that it works and the signal it doesn't — where relevant.
- **Testing:** how to test it well and what is flaky if tested wrong — where relevant.
- **Rollout & migration:** how to adopt incrementally and back out — where relevant.

### Real-World Usage

- Names specific libraries, APIs, or codebases where the pattern lives, with versions when behavior depends on them.
- Describes how teams apply it at scale, not just that they do.

### Checklist

- Actionable items a reader ticks against their own code before shipping.
- Each item is verifiable (a reviewer could check it), not a platitude.

### FAQ

- At least three questions, each phrased as a real search query, each answered in two or three self-contained sentences.

### Next Articles / Related Articles

- **Next:** forward down the dependency graph — articles that list this one as a prerequisite, plus the natural continuation. Regenerated by `scripts/build-links.py`; fix a prerequisite rather than hand-editing.
- **Related:** sibling concepts, see-also, linking canonical homes and never re-explaining.
- Both mirror frontmatter and `graph.json`. See [`INTERNAL_LINKING.md`](../INTERNAL_LINKING.md).

### References (further reading)

- Primary sources first: specifications, official docs, authoritative write-ups.
- Each link carries a short note on what it covers.
- The article stands **without** following any of them; references are for provenance and depth, not to complete the argument.
- No dead links (CI checks this) and no paywalled-only sources as the sole support for a claim.

## Example quality levels

Not every snippet needs to be deployable, but every snippet must declare what it is. Three levels; each has a required rigor and a place it is allowed.

### Level A — Production-ready

The bar for **every Good Example** and every `recipes/` sample.

- Full error handling, cancellation, cleanup, and edge cases.
- Correct types; no `any` escape hatches except where the article is about that escape hatch.
- Accessible by default (labels, roles, focus, keyboard) when it renders UI.
- No console noise, no `TODO`, no commented-out code.
- Would pass review in a real production repository. Meets [`code-example-standard.md`](./code-example-standard.md) in full.
- **Use for:** Good Examples, recipes, anything a reader might copy into production.

### Level B — Educational

Focused on one teaching point; production concerns present where they bear on that point.

- Correct and runnable, but may omit orthogonal production concerns (for example, a snippet teaching memoization need not wire up full i18n) — provided the omission does not hide the very risk being taught.
- Error handling and cleanup are included **whenever they are part of the lesson or would change the outcome**; only truly orthogonal concerns may be trimmed.
- Types present and correct.
- **Use for:** Bad Examples (which must be realistic enough to be tempting), most `examples/` snippets, mid-article illustrative fragments.

### Level C — Minimal

A signature, shape, or fragment illustrating an idea in isolation.

- May be a partial snippet (a type signature, a config line, a three-line shape) that does not run standalone.
- Must still be **syntactically valid** and correctly typed, and must never model an unsafe or misleading pattern as if it were complete.
- Clearly a fragment — never presented as something to copy wholesale.
- **Use for:** the small snippet inside "How It Works," type signatures, config excerpts, "the shape looks like this" illustrations.

**Rule:** when in doubt, level up. A Good Example is never below Level A. A Bad Example is never below Level B (a strawman below B teaches nothing). Levels describe *rigor for the point being made* — they are never an excuse for insecure or broken code presented as correct.

## The pre-merge checklist

Copy this into the pull request. Every box must be checked (or marked N/A with a reason) before review approval.

- [ ] One decision, one topic, one canonical home.
- [ ] Every required section present; non-applicable ones kept with a one-line reason.
- [ ] Primary keyword in title, description, and first 100 words.
- [ ] TL;DR is act-on-able alone; exactly one conditional Recommendation.
- [ ] Bad Example is realistic (Level B+); Good Example is production-ready (Level A).
- [ ] Both examples language-tagged, with the teaching line commented.
- [ ] Trade-offs symmetric; cost table present; recommendation derivable from it.
- [ ] Alternatives honest, each linked; mirrors `alternatives`.
- [ ] Performance and accessibility addressed; security addressed or explicitly N/A with reason.
- [ ] All five typed relations point to existing canonical homes (prereqs, next, related, alternatives, common mistakes).
- [ ] Frontmatter complete and mirrored into `graph.json` (see [`metadata-schema.md`](./metadata-schema.md)).
- [ ] References are primary sources; no dead links.
- [ ] US English; prose over slides; voice matches [`writing-style.md`](./writing-style.md).
- [ ] `last_reviewed` set to today; `status` correct.
- [ ] `scripts/validate-frontmatter.py`, `scripts/validate-links.py`, Markdown lint, and spell check pass.

---

**Next:** [`code-example-standard.md`](./code-example-standard.md) — the rules Level A enforces · [`review-process.md`](./review-process.md) — who checks this and when · [`content-framework.md`](./content-framework.md) — why these sections exist.

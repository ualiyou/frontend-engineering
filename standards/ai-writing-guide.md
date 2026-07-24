# AI Writing Guide

Rules for generating documentation with AI assistance in **Frontend Engineering**. AI can draft, restructure, and accelerate — but it also fabricates confidently, drifts from house style, and invents citations. This guide exists so that AI-assisted output meets the *exact same* bar as human-written output, with extra guards against the specific ways machine generation fails.

**The governing principle:** AI is a drafting tool operated by an accountable human author. AI output enters the [review pipeline](./review-process.md) with **no shortcuts and no exemptions**. A human author signs their name to it and is responsible for every claim.

## Table of contents

- [Non-negotiable principles](#non-negotiable-principles)
- [Allowed assumptions](#allowed-assumptions)
- [Required references](#required-references)
- [Code generation](#code-generation)
- [Fact checking](#fact-checking)
- [Hallucination prevention](#hallucination-prevention)
- [Consistency](#consistency)
- [Self-review](#self-review)
- [Revision workflow](#revision-workflow)
- [Output format](#output-format)
- [The AI author's checklist](#the-ai-authors-checklist)

## Non-negotiable principles

1. **No unverified claim ships.** Every factual statement is traced to a primary source or a reproducible test by a human before publish. "The model said so" is never a source.
2. **No fabricated citations, benchmarks, or APIs.** A link must resolve and must say what the article claims. An API must exist in the named version. A number must be reproducible.
3. **Same pipeline, same gates.** AI drafts still pass technical review, editorial review, example validation, and fact check — by a human other than the operator where the process requires it.
4. **A human is accountable.** The `authors` field names a person, not a model. That person owns the correctness.
5. **Disclose when it matters.** Where a repository policy or a reviewer asks, note that a draft was AI-assisted; it changes the scrutiny, not the standard.

## Allowed assumptions

What an AI drafter may take as given without re-deriving:

- **The house standards** — [`content-framework.md`](./content-framework.md), [`writing-style.md`](./writing-style.md), [`article-quality.md`](./article-quality.md), [`code-example-standard.md`](./code-example-standard.md), [`markdown-guide.md`](./markdown-guide.md). These are the operating constraints; follow them literally.
- **The baseline versions** in [`code-example-standard.md`](./code-example-standard.md#baseline-versions). Assume React 19 / strict TypeScript 5.6+ unless the article overrides.
- **The taxonomy and graph** — the article's place in the [Knowledge Map](../KNOWLEDGE_MAP.md) and its typed relations are inputs, not things to invent.
- **The reader** — a working mid-to-senior frontend engineer. Do not explain fundamentals the audience has (that would be tutorial content), and do not assume knowledge the prerequisites do not establish.

What an AI drafter may **not** assume:

- **That its training data is current.** Versions, API surfaces, library recommendations, and browser support must be checked against live primary sources, not recalled.
- **That a plausible-sounding API exists.** Plausibility is not existence.
- **That a remembered benchmark is real.** Numbers are reproduced or removed.
- **Facts about the present world** (latest versions, what shipped, who maintains what) — these are researched, never recalled.

## Required references

- **Every non-obvious factual claim carries a primary source** gathered during research, not appended afterward to justify a sentence.
- **Prefer specifications and official docs** (MDN, the WHATWG/W3C specs, framework docs, TC39 proposals) over blog posts; prefer a blog post from a primary author over a secondary summary.
- **A reference must be *read*, not just linked.** The cited page must actually contain the claim. Confirming this is part of research and is re-confirmed at [fact check](#fact-checking).
- **The article stands without its references** (self-containment). References are for provenance and depth.
- **No reference is invented.** If a source cannot be found for a claim, the claim is cut or reframed as clearly-labeled reasoning, never dressed up with a fake citation.

## Code generation

AI-generated code is guilty until proven correct — it compiles-in-the-head convincingly and fails in practice.

- **Meets [`code-example-standard.md`](./code-example-standard.md) in full.** Level A for Good Examples: strict types, error handling, cancellation, cleanup, accessibility, no needless abstraction.
- **Type-checked and run before publish.** Generated code is compiled under strict TypeScript and executed (or at minimum type-checked) by the human author — never shipped on the model's assurance.
- **No hallucinated APIs, props, hooks, or imports.** Every identifier is verified to exist in the baseline version. A method that "should" exist but doesn't is the single most common AI code failure — check each one.
- **The Bad Example is a *real* mistake**, realistic enough to tempt a competent engineer, with a genuine failure — not a strawman the model invented to have something to contrast.
- **No placeholder imports or `// ... rest of implementation`** in a Good Example. If it is presented as complete, it is complete.
- **Comments follow the house rule** — why, not what; mark the teaching line.

## Fact checking

This is the stage AI writing most needs and most tempts skipping. It is mandatory.

- **Independent human verification** of every checkable claim and citation, per [`review-process.md` Stage 7](./review-process.md#stage-7--fact-check).
- **Version claims** are checked against the actual release ("`use` is React 19+" — verify, don't recall).
- **Every link opened and confirmed** to support its sentence; dead or drifted links removed.
- **Numbers reproduced** or deleted. A benchmark without a runnable method is a liability.
- **The checker is not the operator** of the model for that draft, wherever the process allows — a second set of eyes catches confident nonsense the first missed.

## Hallucination prevention

Concrete tactics, not just a warning:

- **Prefer retrieval over recall.** Pull the current docs (for example via a docs tool or the primary source) and write from what they say, rather than from what the model remembers.
- **Name the source inline while drafting**, then verify; an unsourced sentence is a flag to check, not to keep.
- **Constrain to the baseline.** Generating against a fixed, known version shrinks the space for invented APIs.
- **Diff against reality.** Cross-check API names, prop names, and signatures against the actual type definitions or docs — not against confidence.
- **When unsure, say so or stop.** "I could not verify this" is a correct output; a fabricated fact is not. The article omits what cannot be verified rather than guessing.
- **Treat suspiciously round or convenient numbers as unverified** until reproduced.
- **Reject prose that sounds authoritative but cites nothing** — fluency is not evidence.

## Consistency

AI drift — subtle vocabulary and structure changes across a session — is corrosive at scale. Counter it:

- **One term per concept**, matching the ecosystem's spelling and the repository's existing usage. Do not let the model introduce synonyms mid-article (see [`writing-style.md`](./writing-style.md#terminology)).
- **Structure matches the template exactly** — same sections, same order, same heading casing. No invented sections, no renamed ones.
- **Voice matches the house style** — no marketing register, no "simply/just," sentence-case headings, prose over slides. The [banned-words list](./writing-style.md#banned-and-discouraged-words) is a hard filter over AI output, which trends toward exactly those words.
- **Reuse canonical homes** — link existing articles for established concepts instead of letting the model re-explain them (which it will, verbosely).
- **Frontmatter conforms to [`metadata-schema.md`](./metadata-schema.md)** — snake_case, valid enums, mirrored into `graph.json`.

## Self-review

Before a human ever sees the draft, the AI author performs a structured self-review pass and reports the result — a first-line filter, never a replacement for human review.

- **Re-read against the [pre-merge checklist](./article-quality.md#the-pre-merge-checklist)** item by item and state, per item, pass or the specific gap.
- **Flag every claim it could not verify** explicitly, so the human checks those first.
- **List every API/identifier used** and confirm each against the baseline, or mark it unverified.
- **Scan its own output for banned words** and marketing register, and remove them.
- **Check trade-off symmetry** — is the disadvantages section as substantive as the advantages? AI tends to under-argue costs.
- **Confirm the recommendation is derivable** from the stated trade-offs, not asserted.
- The self-review is *reported*, not hidden: the human author receives the list of self-identified gaps and unverified claims.

## Revision workflow

- **Small, reviewable changes.** Regenerate a section, not the whole file, so diffs stay legible and a reviewer can see exactly what changed.
- **Preserve verified content.** Do not let a regeneration silently rewrite already-reviewed, already-fact-checked prose; scope the change.
- **Every revision re-enters the relevant gate** — regenerated code re-validates; a changed claim re-fact-checks; a changed recommendation re-triggers technical review and may bump the article's [MAJOR version](./evergreen-policy.md#versioning-policy).
- **Track what changed and why** in the pull request, so review is targeted and the maintenance record stays honest.

## Output format

- **A complete article file** following [`templates/article-template.md`](../templates/article-template.md): frontmatter first, one H1, every required section, footer nav.
- **Valid, lint-clean Markdown** per [`markdown-guide.md`](./markdown-guide.md) — language-tagged fences, correct admonition syntax, blank lines around blocks.
- **Frontmatter and `graph.json` node** produced together and mirrored.
- **No meta-commentary in the file** — no "Here is the article," no "As an AI," no notes-to-reviewer left in prose (those go in the pull-request description).
- **US English, prose over slides.**

## The AI author's checklist

Attach to the pull request alongside the standard [pre-merge checklist](./article-quality.md#the-pre-merge-checklist):

- [ ] Every factual claim traced to a read primary source; unverifiable claims cut, not guessed.
- [ ] Every API/identifier confirmed to exist in the baseline version.
- [ ] Code type-checked and run (or type-checked) by a human; Level A for the Good Example.
- [ ] Bad Example is a real, tempting mistake — not a strawman.
- [ ] No fabricated links, benchmarks, or numbers; every link opened and confirmed.
- [ ] Banned words and marketing register removed; one term per concept.
- [ ] Structure, headings, and frontmatter match the template and schema exactly.
- [ ] Trade-offs symmetric; recommendation derivable.
- [ ] Self-review reported, with unverified claims flagged for the human checker.
- [ ] A named human author owns this and it enters the normal review pipeline.

---

**Next:** [`review-process.md`](./review-process.md) — the gates AI output still passes · [`article-quality.md`](./article-quality.md) — the bar · [`writing-style.md`](./writing-style.md) — the voice AI must match.

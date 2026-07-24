# Content Framework

The definitive content system for **Frontend Engineering**. This document defines the philosophy every article obeys, from a single page to the ten-thousandth. It is the constitution of the knowledge base: the other files in [`standards/`](./README.md) are the statutes that implement it.

If a rule elsewhere in `standards/` ever contradicts this document, this document wins, and the contradiction is a bug to be fixed.

> **Scope.** This file answers *why* and *what for*. The mechanics — sections, tone, code, metadata, review — live in the sibling standards files. Read this once to understand the intent; consult the others while writing.

## Table of contents

- [Mission in one sentence](#mission-in-one-sentence)
- [The documentation philosophy](#the-documentation-philosophy)
- [What makes a great engineering article](#what-makes-a-great-engineering-article)
- [What makes an article evergreen](#what-makes-an-article-evergreen)
- [What must never appear](#what-must-never-appear)
- [How to present engineering trade-offs](#how-to-present-engineering-trade-offs)
- [How opinionated this repository is](#how-opinionated-this-repository-is)
- [How framework-specific advice is handled](#how-framework-specific-advice-is-handled)
- [The nine invariants](#the-nine-invariants)

## Mission in one sentence

Capture the **durable reasoning behind frontend engineering decisions** — the problem, the options, the trade-offs, and a defensible recommendation — so that a working engineer can make the right call under real constraints, years after the article was written.

Everything below serves that sentence.

## The documentation philosophy

We document **decisions, not instructions**. A tutorial answers "how do I make this work?" and expires when the API changes. A decision record answers "which approach should I choose, and what am I trading away?" and stays valuable as long as the trade-off exists — which is usually far longer than any framework version.

Five principles follow from this:

1. **Reasoning over recipes.** The `why` is the product. Code exists to make the reasoning concrete, not to be copied blindly.
2. **Honesty over advocacy.** Every recommendation states its costs. An article that only sells its recommendation has failed, even if the recommendation is correct.
3. **Durability over currency.** We optimize for the guidance still being true in five years, not for being first to cover this week's release.
4. **Transfer over specificity.** We prefer concepts that survive a framework migration. Framework detail is included where it changes the decision, and clearly fenced when it does.
5. **Self-containment over link-chasing.** A reader understands the article without opening a single reference. References exist for depth and provenance, not to complete the argument.

## What makes a great engineering article

A great article in this repository has all of the following. Any one missing makes it merely adequate.

- **It answers a decision a real engineer faces.** The title maps to a question someone types into a search bar at 2pm under deadline. If no one has to *decide* anything, it belongs in reference docs, not here.
- **It front-loads the payoff.** A busy staff engineer gets the recommendation and the single most important trade-off from the TL;DR alone, without scrolling.
- **It builds a mental model, not a memory.** The reader can reason about a situation the article never mentioned, because they understand the mechanism — not because they memorized steps.
- **It shows both failure and success.** A realistic bad example (the version that ships in real codebases) sits beside a production-ready good example, and the difference is explained line by line.
- **Its trade-offs are symmetric.** Advantages and disadvantages get equal rigor. The recommendation is *derived* from the trade-offs, not asserted before them.
- **Its code is production-grade.** Error handling, cancellation, cleanup, edge cases, and accessibility are present because their absence is the actual bug in most real code.
- **It links its neighborhood.** Prerequisites, alternatives, next steps, related concepts, and known anti-patterns are all one click away, each pointing at the canonical home of that concept.
- **It is falsifiable.** Claims are specific enough to be wrong. "This is faster" is not a claim; "this removes one render per keystroke, measured with the React Profiler" is.
- **It ages well.** Strip the version numbers and the guidance still holds. Where it cannot, the version-bound part is explicitly marked as such.

## What makes an article evergreen

Evergreen is not "never edited." It is **"the core stays true while the surface is maintained."** An article earns evergreen status by construction:

- **Anchor to the problem, not the tool.** "Synchronizing server state with the UI" outlives "using `useEffect` to fetch data." The problem is permanent; the tool is a footnote.
- **Separate the timeless from the timely.** The mental model, the trade-off, and the failure mode change slowly. API names, version numbers, and library recommendations change quickly. Keep them in different sentences so the timely part can be updated without rewriting the timeless part.
- **Name versions where behavior depends on them, and only there.** A version number is a maintenance liability; spend it only when the behavior would be wrong without it.
- **Cite primary sources.** Specifications and official docs move slower and break less than blog posts. Prefer them.
- **Prefer concepts that have already survived a cycle.** Reactivity, caching, invalidation, memoization, and hydration predate every current framework and will outlive them.
- **Carry a `last_reviewed` date.** Evergreen is a claim that must be re-verified on a schedule (see [`evergreen-policy.md`](./evergreen-policy.md)). An unreviewed article is not evergreen; it is merely old.

## What must never appear

These are hard exclusions. A pull request containing any of them is rejected regardless of quality.

- **Tutorials and "getting started" walkthroughs.** Step-by-step "now install X, now run Y" content. We assume working familiarity.
- **Restated framework documentation.** If MDN or the React docs already say it, link them; do not paraphrase them. We add the *decision*, not the reference.
- **Marketing and hype.** No "blazing fast," "game-changing," "simply," "just," "effortless," or superlatives without a measurement behind them. See [`writing-style.md`](./writing-style.md).
- **Unqualified opinion.** A recommendation without stated trade-offs. Every "prefer X" carries "because Y, at the cost of Z."
- **News and announcements.** Release notes, changelog summaries, "what's new in vN." Durable principles only.
- **Toy code.** Snippets that skip error handling, ignore cleanup, or would never survive code review. If it wouldn't pass review in a real repo, it fails here.
- **Unsafe examples presented as safe.** Any snippet that would introduce an XSS, injection, auth, or data-loss vulnerability if copied. Insecure code appears *only* in a Bad Example, clearly labeled as the mistake.
- **Plagiarism.** Copied prose or code from books, courses, or copyrighted articles. Short attributed quotes in References only.
- **Fabricated facts, benchmarks, or citations.** A number without a reproducible source, or a link to a page that does not say what the article claims. See [`ai-writing-guide.md`](./ai-writing-guide.md).
- **Absolute claims.** "Always," "never," "the only way," "everyone knows" — engineering is contextual. State the context in which the claim holds.

## How to present engineering trade-offs

Trade-offs are the reason this repository exists. They are presented, never hidden:

1. **State both sides with equal weight.** List advantages and disadvantages in comparable detail. If the disadvantages section is thin, the analysis is incomplete, not the technique perfect.
2. **Make the recommendation follow from the analysis.** The reader should reach the recommendation before you state it, because the trade-offs pointed there. If they wouldn't, the recommendation is unsupported.
3. **Name the flip conditions.** Every default has a boundary. State the scale, data shape, team size, or constraint at which the recommendation reverses. "Use X below ~10k rows; above that, Y" beats "X is usually fine."
4. **Compare against real alternatives.** Each alternative gets an honest "best when" and "weakness," and links to its own article. Straw-man alternatives are dishonest and forbidden.
5. **Quantify what can be quantified.** Prefer "one extra network round-trip" over "slower," "O(n) re-renders" over "less efficient." Reserve prose for trade-offs that resist numbers.
6. **Distinguish cost types.** Runtime performance, developer complexity, maintenance burden, and failure behavior are different axes; a technique can win one and lose another. Use the trade-off table to keep them separate.

The canonical container for this is the **Trade-offs** section plus its cost table, and the **Alternative Approaches** table, both defined in [`article-quality.md`](./article-quality.md).

## How opinionated this repository is

**Opinionated with its reasons on the table.** We are not neutral — a reference that refuses to recommend is useless to someone who has to ship today. But every opinion is earned:

- We give a **defensible default** for each decision, stated plainly (the `Recommendation` callout).
- The default is **always conditional**: it names the context where it holds and the context where it flips.
- We **respect the reader's judgment**: the alternatives are documented well enough that a reader with different constraints can confidently choose differently.
- We change our defaults when the evidence changes, and we record the change (see the deprecation and versioning rules in [`evergreen-policy.md`](./evergreen-policy.md)).

The stance to emulate: **TypeScript's handbook** (strong recommendations, clear reasons, escape hatches documented), not a vendor blog (one answer, no costs) and not a neutral wiki (every option, no guidance).

## How framework-specific advice is handled

The repository is **framework-aware but not framework-bound**.

- **Default to the transferable concept.** Lead with the idea that survives a framework change; introduce framework specifics only where they change the decision.
- **Fence the framework-bound parts.** When behavior depends on a framework, say which framework and which version, in that sentence. A reader on a different stack must be able to see exactly what applies to them and what does not.
- **React is the primary worked example, not the subject.** Where a concrete framework helps, we use React (and TypeScript) because it is the most common stack of our audience — but the article's *thesis* must not depend on React unless the topic is React itself.
- **Declare the assumption in frontmatter.** The `frameworks` field lists what an article assumes (`[]` when agnostic). This is machine-readable so readers and tooling can filter.
- **Never let a framework's marketing set the frame.** We evaluate a framework's approach on its trade-offs, the same as any other option, including its costs.
- **Version-pin only where it matters.** Name a version when the behavior would be wrong without it; otherwise stay version-free so the article ages better.

## The nine invariants

These hold for **every** document in the repository, forever. They are the checksum of the whole system; tooling and review both enforce them.

1. **One decision per file.** One topic, one canonical home. If it grows a second thesis, split it.
2. **Every section present.** The mandatory structure in [`article-quality.md`](./article-quality.md) is filled; a non-applicable section keeps its heading and states why in one line.
3. **Both examples, both realistic.** A production-grade Good Example and a realistic Bad Example, each language-tagged and runnable.
4. **Trade-offs symmetric, recommendation derived.** As above.
5. **Every cross-reference is a typed link to a canonical home.** Prerequisites, next, related, alternatives, common mistakes — never a re-explanation. See [`INTERNAL_LINKING.md`](../INTERNAL_LINKING.md).
6. **Frontmatter complete and mirrored into `graph.json`.** See [`metadata-schema.md`](./metadata-schema.md).
7. **Primary sources cited.** The article stands without them, but they are present for provenance and depth.
8. **US English, prose over slides.** Complete sentences carry the reasoning; lists and tables only where they scan better.
9. **Reviewed and dated.** A `last_reviewed` date, set by a real review against the checklist, per [`review-process.md`](./review-process.md).

---

**Next:** [`writing-style.md`](./writing-style.md) — the voice that carries all of the above · [`article-quality.md`](./article-quality.md) — the mandatory structure · [`standards/README.md`](./README.md) — the full standards index.

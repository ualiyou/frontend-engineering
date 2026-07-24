# Documentation Health Metrics

How **Frontend Engineering** measures its own quality. At 1000+ documents, "it's good" is not auditable and "a reviewer checked it" does not scale. This document defines **measurable health metrics** — each with an explicit scoring rule — so the state of the knowledge base is a number a maintainer can track, a report CI can generate, and a target a contributor can hit.

The metrics exist to *surface* problems, not to game. A high score is necessary, never sufficient; a human still owns correctness. Use them to find the weakest articles and the drifting trends, not to rubber-stamp.

## Table of contents

- [How scoring works](#how-scoring-works)
- [Completeness score](#completeness-score)
- [Accuracy score](#accuracy-score)
- [Readability score](#readability-score)
- [Cross-link coverage](#cross-link-coverage)
- [Reference coverage](#reference-coverage)
- [Freshness score](#freshness-score)
- [Code quality score](#code-quality-score)
- [Maintenance score](#maintenance-score)
- [The composite health score](#the-composite-health-score)
- [Repository-level metrics](#repository-level-metrics)
- [Known tooling gaps](#known-tooling-gaps)

## How scoring works

- **Each metric is 0–100.** Higher is better. Most are computed per article; some are repository-level.
- **Two kinds of check:** *automatable* (a script can compute it — structure, links, frontmatter, freshness, lint) and *judged* (a reviewer scores it — accuracy, readability, trade-off honesty). Automatable metrics run in CI; judged metrics are set at [review](./review-process.md) and stored.
- **A publishable article needs ≥ 85 on every metric** and passes all hard gates regardless of score. Scores below threshold block or flag.
- **Scores are recorded** (in the article's review record / a generated report), so trends are visible over time, not just at a point.

## Completeness score

*Automatable.* Is every required part present and non-empty?

- **What it measures:** presence and substance of the [mandatory sections](./article-quality.md#the-required-section-model) and all required frontmatter fields.
- **Scoring:** start at 100. Subtract **8** per missing required section; subtract **4** per section that is present but empty or a single filler sentence where content is expected (a legitimate one-line "not applicable" does **not** count as empty); subtract **5** per missing required frontmatter field; subtract **10** if the frontmatter does not mirror `graph.json`.
- **Threshold:** 100 to publish — completeness is binary in spirit. Anything less means a section is missing.
- **Source:** extends `scripts/validate-frontmatter.py`; a section-presence check should be added (see [known gaps](#known-tooling-gaps)).

## Accuracy score

*Judged, at technical review and fact check.* Is it *true*?

- **What it measures:** correctness of claims, honesty and symmetry of trade-offs, validity of the mental model, correct version pinning, and citation integrity.
- **Scoring rubric (reviewer assigns):**
  - **100–90:** every claim verified against a primary source; trade-offs symmetric; recommendation derivable; versions correct.
  - **89–70:** minor unverified claims or a thin disadvantages section; no factual errors.
  - **69–50:** a claim could not be verified, or the trade-off analysis is one-sided.
  - **< 50:** a factual error, a fabricated citation, or a strawman alternative — **blocks publish**.
- **Threshold:** ≥ 90 to publish. Accuracy is the metric the [fact-check gate](./review-process.md#stage-7--fact-check) defends; it never ships below 90.

## Readability score

*Mostly automatable, reviewer-adjusted.* Can the target reader follow it efficiently?

- **What it measures:** sentence and paragraph length, presence of the front-loaded TL;DR, heading structure, absence of [banned marketing words](./writing-style.md#banned-and-discouraged-words), prose-over-slides balance.
- **Scoring:** start at 100. Subtract **3** per banned word; subtract **5** if average sentence length exceeds ~28 words or paragraphs routinely exceed ~5 sentences; subtract **5** if reasoning is delivered as bullet lists instead of prose; subtract **5** for missing/weak TL;DR; subtract **3** per heading-hierarchy violation. A reviewer may adjust ±10 for clarity a script can't see.
- **Calibrated to the audience** (mid-to-senior engineers) — not a general-reader grade level. Precision beats simplicity.
- **Threshold:** ≥ 85.

## Cross-link coverage

*Automatable.* Is the article properly wired into the graph?

- **What it measures:** presence and validity of the five typed relations and their two-way integrity.
- **Scoring:** start at 100. Subtract **10** per required relation array that is absent (not `[]` — absent); subtract **15** per link that does not resolve to an existing node; subtract **10** if `alternatives` is non-symmetric; subtract **10** if the prerequisite graph would become cyclic; subtract **5** if `next` is hand-edited out of sync with the derived inverse. An honest empty `alternatives: []` is **not** penalized.
- **Threshold:** ≥ 85, and **zero** unresolved links (that's a hard gate too).
- **Source:** `scripts/validate-links.py` already enforces the invariants; this metric turns its pass/fail into a graded coverage number.

## Reference coverage

*Automatable presence + judged quality.* Are claims backed by sources?

- **What it measures:** whether the article cites primary sources, whether the links resolve, and (judged) whether the references are primary and actually support their claims.
- **Scoring:** start at 100. Subtract **20** if the References section is empty on an article making external claims; subtract **10** per dead reference link; subtract **5** per reference that is a secondary source where a primary one exists; subtract **10** (reviewer, at fact check) if a cited source does not support the sentence it backs.
- **Self-containment caveat:** the article must stand *without* the references — so "few references" is fine for a purely reasoning-based article; "unsupported external claims" is not.
- **Threshold:** ≥ 85; **zero** dead links (hard gate via the dead-link workflow).

## Freshness score

*Automatable.* Has it been reviewed within its window?

- **What it measures:** age of `last_reviewed` against the article's [volatility window](./evergreen-policy.md#review-frequency) (High 6mo / Medium 12mo / Low 24mo).
- **Scoring:** **100** if reviewed within the window; decays linearly to **50** at 2× the window; **< 50** (flagged **overdue**) beyond that. A `Deprecated` article with a current banner scores as fresh; an `Archived` article is excluded.
- **Threshold:** ≥ 85 keeps an article in good standing; below that it enters the maintenance queue. Freshness is the one metric that *decays on its own* — an untouched article's score falls with time, which is the point.
- **Source:** computed from `last_reviewed` + inferred/curated volatility; drives the repository freshness report.

## Code quality score

*Automatable + judged.* Do the examples meet the bar?

- **What it measures:** the Good Example at [Level A](./article-quality.md#example-quality-levels) and the Bad Example's realism, per [`code-example-standard.md`](./code-example-standard.md).
- **Scoring:** start at 100. Subtract **20** if the Good Example does not type-check under strict TypeScript; subtract **15** for missing error handling/cleanup where it matters; subtract **10** for an untagged fence; subtract **10** per `any`/`@ts-ignore` in a Good Example; subtract **10** for a UI example with no accessibility; subtract **10** for a speculative/unjustified abstraction; subtract **15** (reviewer) if the Bad Example is a strawman.
- **Threshold:** ≥ 90 — examples are the repository's proof of work and hold a high bar.
- **Source:** lint/type-check in CI where snippets are extractable; reviewer for realism and a11y.

## Maintenance score

*Automatable, repository- and article-level.* How maintainable is this in the long run?

- **What it measures:** signals that predict future cost: number of hard-coded version pins, count of inbound links (blast radius of a change), whether it has a deprecation/migration path when needed, open unresolved content-correction issues against it, and time-since-last-touch relative to inbound traffic.
- **Scoring:** start at 100. Subtract **3** per version pin beyond the ones behavior genuinely requires; subtract **10** if a `Deprecated` article lacks a replacement link; subtract **5** per open unaddressed content-correction issue older than one review cycle; subtract **5** if the article is a high-inbound-degree node past its freshness window (its staleness affects many others).
- **Threshold:** ≥ 85. A low maintenance score is an early warning, not a publish blocker on its own.

## The composite health score

A single number per article, for triage — the **minimum** of the eight, not the average:

```text
health = min(completeness, accuracy, readability, cross_link,
             reference, freshness, code_quality, maintenance)
```

We take the **minimum deliberately**: an article is only as healthy as its weakest dimension. A brilliantly written, well-linked article with a fabricated claim is not "92 average" — it is broken, and the minimum says so. Triage worst-first by composite score.

## Repository-level metrics

Beyond per-article scores, track the health of the whole:

- **Coverage:** published articles ÷ planned articles in the [inventory](../ARTICLE_INVENTORY.md), per Part — where are the gaps?
- **Overdue rate:** share of published articles past their freshness window — is maintenance keeping up?
- **Graph integrity:** unresolved links, cycles, orphan nodes (target: **zero**, enforced by CI).
- **Deprecation debt:** count of `Deprecated` articles without migration guides.
- **Correction latency:** median time from a content-correction issue to a fix.
- **Score distribution:** the histogram of composite scores — a healthy repository has a tight, high distribution, not a high average hiding a long tail.

## Known tooling gaps

The metrics above describe the target system; some checks are enforced today and some need building. Tracked honestly here so the gap is visible:

- **Section-presence check** — extend `validate-frontmatter.py` (or add a script) to verify every mandatory section heading is present, feeding the Completeness score.
- **`reading_time` vs `reading_time_min`** — the current validator requires a key literally named `reading_time` while the schema and template use `reading_time_min`; reconcile the validator to `reading_time_min` (noted in [`metadata-schema.md`](./metadata-schema.md#validation-and-the-graph-mirror)).
- **Snippet extraction + type-check in CI** — compile fenced `ts`/`tsx` blocks under strict TypeScript so the Code Quality score is automated, not just reviewer-judged.
- **Freshness report** — a scheduled job that computes freshness from `last_reviewed` + volatility and lists overdue articles.
- **Banned-word linter** — a check that flags the [marketing register](./writing-style.md#banned-and-discouraged-words) automatically, feeding Readability.

Until each is automated, the corresponding metric is scored at review by a human against the rules above — the standard is the same; only the enforcement mechanism differs.

---

**Next:** [`review-process.md`](./review-process.md) — where judged scores are set · [`evergreen-policy.md`](./evergreen-policy.md) — the freshness window · [`article-quality.md`](./article-quality.md) — the bar the scores measure against.

# Contributing to Frontend Engineering

Thank you for your interest in contributing. This repository is a long-term, peer-reviewed knowledge base for frontend engineering decisions and patterns. Its value depends on consistency, accuracy, and clear reasoning — so please read this guide before opening a pull request.

By participating, you agree to uphold our [Code of Conduct](CODE_OF_CONDUCT.md).

## Your first contribution

New here? The best entry points are:

- Issues labeled [`good first issue`](https://github.com/ualiyou/frontend-engineering/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) — small, well-scoped tasks.
- Issues labeled [`help wanted`](https://github.com/ualiyou/frontend-engineering/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22) — where maintainers actively want contributors.
- **Content corrections** — spot an error in an article? Open a *Content correction* issue or send a fix directly. These are high-value and low-risk.

Not sure where something fits? Open an issue and ask, or start a [Discussion](https://github.com/ualiyou/frontend-engineering/discussions).

## What We Accept

- New articles that document an engineering decision, pattern, or trade-off, following the standard template.
- Improvements to existing articles: correcting inaccuracies, strengthening trade-off analysis, adding references, clarifying prose.
- Documented anti-patterns with a clear explanation of why they fail at scale.
- Focused examples or recipes that support an existing or accompanying article.
- Fixes to structure, links, typos, and formatting.

## What We Do Not Accept

- Tutorials or "getting started" walkthroughs.
- Content that merely restates or links to official framework documentation.
- Opinion pieces without trade-off analysis or references.
- Framework-version announcements or news.
- Copy-pasted content from other sources (see [Licensing and Originality](#licensing-and-originality)).

## How to Contribute

1. **Open an issue first** for any new article or substantial change, using the matching [issue template](.github/ISSUE_TEMPLATE). This lets maintainers confirm scope and avoid duplicate work. Small fixes (typos, broken links) can go straight to a pull request.
2. **Fork the repository** and create a branch from `main` (see [Naming Conventions](#naming-conventions)).
3. **Write your entry** using the [article template](templates/article-template.md). Do not remove sections; if a section does not apply, explain why in one line rather than deleting it.
4. **Place the file** in the correct directory (see [Documentation Standards](#documentation-standards)).
5. **Self-review** against the [Review Criteria](#review-criteria) checklist.
6. **Open a pull request** and fill out the [pull request template](.github/PULL_REQUEST_TEMPLATE.md) completely.
7. **Respond to review feedback.** Entries are merged once they meet the standards below and receive maintainer approval.

## Documentation Standards

The full content framework lives in [`standards/`](standards/): the [content philosophy](standards/content-framework.md), the [tone of voice](standards/writing-style.md), the [article quality checklist](standards/article-quality.md), the [code](standards/code-example-standard.md) and [diagram](standards/diagram-guide.md) rules, the [review pipeline](standards/review-process.md), the [evergreen policy](standards/evergreen-policy.md), the [AI writing rules](standards/ai-writing-guide.md), and the [health metrics](standards/quality-metrics.md). New and returning contributors should start with the [contributor writing guide](standards/contributor-writing-guide.md). The essentials are summarized below.

- **Every article follows [`templates/article-template.md`](templates/article-template.md).** The section order is fixed so readers and reviewers know what to expect.
- **Keep graph metadata in sync.** Each article has an entry in its domain's `graph.json` (difficulty, reading time, prerequisites, related, order). Update that entry when you add or change an article, and mirror it in the article's frontmatter. See [GRAPH.md](GRAPH.md).
- **Reasoning over instruction.** Explain *why*, not just *how*. Always include the trade-offs.
- **Show both sides.** Each article must include a "Bad Example" and a "Good Example" with runnable, realistic code — not toy snippets that ignore error handling or edge cases.
- **Be framework-honest.** Where a pattern is framework-specific, say so. Prefer concepts that transfer; when using a specific library, name the version if behavior depends on it.
- **Keep it self-contained.** A reader should understand the entry without following external links, though references should be provided for depth.
- **Cite sources.** Use the References section for official docs, specifications, and authoritative write-ups.
- **Prose, not slides.** Write in complete sentences and paragraphs. Use lists only where they genuinely aid scanning.
- **One topic per file.** If an article grows to cover several decisions, split it.
- **Language:** US English. Use fenced code blocks with a language tag for every snippet.

### Placement

| Content type | Location |
| --- | --- |
| A decision, pattern, or trade-off article | `docs/<part>/<domain>/` (find the domain via the [Knowledge Map](KNOWLEDGE_MAP.md)) |
| A documented pitfall | `anti-patterns/` |
| A minimal code illustration for one point | `examples/` |
| An end-to-end solution to a recurring problem | `recipes/` |
| Diagrams and images | `assets/` |

## Naming Conventions

- **Files and folders:** lowercase `kebab-case`. Example: `docs/03-application-architecture/state-management/server-vs-client-state.md`.
- **Article filenames** describe the topic, not the format: `optimistic-updates.md`, not `article-3.md` or `Optimistic_Updates.md`.
- **Branches:** `<type>/<short-description>`, where `type` is one of `docs`, `fix`, `chore`, or `refactor`. Example: `docs/react-render-props-tradeoffs`.
- **Commits:** use [Conventional Commits](https://www.conventionalcommits.org/). Example: `docs(react): add article on colocation of state`.
- **Assets:** name by the article they support, e.g. `assets/rendering-strategies-diagram.svg`.
- **Titles:** the `# Title` in an article should be human-readable Title Case; the filename is its kebab-case form.

## Pull Request Guidelines

- **One logical change per pull request.** Do not bundle an unrelated fix with a new article.
- **Fill out the pull request template** completely, including which section(s) the change affects and any linked issue.
- **Keep diffs reviewable.** Large articles are fine; unrelated reformatting of other files is not.
- **Link the issue** the pull request resolves (`Closes #123`) when applicable.
- **Pass automated checks** (Markdown lint, link validity, spelling, frontmatter) before requesting review. See [`.github/workflows/`](.github/workflows).
- **Be responsive.** Pull requests with no author activity for an extended period may be closed and can be reopened later.
- **Squash on merge.** Maintainers squash to keep history clean; write a clear pull request title.

## Review Criteria

Reviewers evaluate each contribution against the following. All must hold for an article to be merged.

- **Correctness:** claims are accurate and, where relevant, supported by references or reproducible reasoning.
- **Completeness:** every template section is present and meaningfully filled in.
- **Trade-off honesty:** advantages *and* disadvantages are stated; the recommendation follows from them.
- **Both examples present:** a realistic "Bad Example" and a production-ready "Good Example," both correct and runnable.
- **Scope discipline:** the entry stays on one topic and does not drift into tutorial territory.
- **Clarity:** prose is clear, concise, and free of unexplained jargon.
- **Placement and naming:** the file is in the right directory and follows naming conventions.
- **Originality:** the content is original and properly attributed (see below).
- **Durability:** the guidance is likely to remain valid beyond the next framework release.

## Licensing and Originality

By contributing, you agree that your contribution is your own original work and that it is licensed under this repository's [MIT License](LICENSE). Do not paste content from books, paid courses, or copyrighted articles. Short, attributed quotes and links to sources are welcome in the References section.

## Related documents

- [Standards](standards/) — the content framework every document follows.
- [Code of Conduct](CODE_OF_CONDUCT.md) — community standards.
- [Governance](GOVERNANCE.md) — roles, decision-making, and the RFC process.
- [Support](SUPPORT.md) — where to ask what.
- [Security Policy](SECURITY.md) — reporting unsafe example code or tooling risk.
- [Label reference](.github/LABELS.md) — how work is categorized.
- [Milestones](.github/MILESTONES.md) and [Project board](.github/PROJECT_BOARD.md) — how work is planned and tracked.

## Questions

Open an issue with the `type: question` label or start a [discussion](https://github.com/ualiyou/frontend-engineering/discussions). Maintainers are happy to help you shape a contribution before you invest time writing it.

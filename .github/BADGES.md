# Badges

Badges communicate project health at a glance — but only when each one *earns its place*. The rule: a badge must answer a question a visitor actually has ("Is it maintained? Is CI green? What license?"). Everything else is clutter and is deliberately omitted.

## Recommended (in README, in this order)

| Badge | Answers | Markdown |
| --- | --- | --- |
| License | "Can I use this?" | `[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)` |
| CI status | "Is the content valid right now?" | `[![CI](https://github.com/ualiyou/frontend-engineering/actions/workflows/ci.yml/badge.svg)](../../actions)` |
| Content checks | "Do links/spelling/frontmatter pass?" | Combine into the CI badge above, or one per workflow if you prefer granularity |
| Articles published | "How much is actually here?" | `[![Articles](https://img.shields.io/badge/dynamic/json?label=articles&query=$.count&url=...)]()` *(needs a small endpoint or a generated shields JSON — see note)* |
| Contributions welcome | "Can I contribute?" | `[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)` |
| Code of Conduct | "Is this a healthy community?" | `[![Code of Conduct](https://img.shields.io/badge/code%20of%20conduct-Contributor%20Covenant-ff69b4.svg)](CODE_OF_CONDUCT.md)` |
| Last commit | "Is it alive?" | `[![Last commit](https://img.shields.io/github/last-commit/ualiyou/frontend-engineering)](../../commits)` |
| Stars | Social proof (optional) | `[![Stars](https://img.shields.io/github/stars/ualiyou/frontend-engineering?style=social)](../../stargazers)` |

## Deliberately avoided

- **Downloads / npm version** — this repo publishes no package.
- **Build passing *and* separate lint/test/coverage badges** — redundant; fold sub-checks into one CI badge.
- **"Made with love", "PRs welcome" duplicates, framework logos** — decorative noise.
- **Coverage %** — meaningless for a docs repo; there is no code coverage to report.

## Note on the "Articles published" badge

Because content is Markdown, there is no built-in count. Two clean options:

1. A CI step writes `badges/articles.json` (`{"schemaVersion":1,"label":"articles","message":"42","color":"blue"}`) and the README uses shields' *endpoint* badge pointing at the raw file.
2. Skip it until v0.2, when the number is worth showing.

Keep the total badge count at **5–7**. If adding one pushes past that, remove a weaker one first.

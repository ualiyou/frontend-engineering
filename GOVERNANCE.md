# Governance

How decisions are made in Frontend Engineering. This model is intentionally lightweight for the project's current stage and will formalize as the contributor base grows.

## Roles

- **Reader / User** — anyone who uses the knowledge base. No obligations.
- **Contributor** — anyone who opens an issue or pull request. Bound by the [Code of Conduct](CODE_OF_CONDUCT.md).
- **Reviewer** — a trusted contributor who reviews pull requests in a domain. Reviewers have a track record of quality contributions and reviews.
- **Domain maintainer** — owns one or more top-level Parts (see [`CODEOWNERS`](.github/CODEOWNERS)); has merge rights within their area and sets domain-level editorial standards.
- **Lead maintainer** — sets overall direction, breaks ties, manages releases, and administers the repository.

## Decision-making

- **Editorial (content) changes** — a single domain maintainer's approval is enough to merge, provided CI passes and the [Review Criteria](CONTRIBUTING.md#review-criteria) are met.
- **Structural changes** — anything touching the knowledge map, taxonomy, templates, tooling, or governance requires a **Request for Comments (RFC)**: open an issue with the `type: rfc` label describing the change and its rationale. An RFC needs approval from **two maintainers** and no sustained, unresolved objection after **7 days**.
- **Ties** are broken by the lead maintainer.

## Becoming a maintainer

There is no application. Contribute consistently, review others' work well, and demonstrate good editorial judgment. An existing maintainer will propose you, and the maintainer group confirms by lazy consensus. New maintainers are added to [`CODEOWNERS`](.github/CODEOWNERS) and [`MAINTAINERS.md`] when that file is introduced.

## Maintainers

| Area | Maintainer |
| --- | --- |
| Lead maintainer | @alidevjs |
| All Parts (interim) | @alidevjs |

As domains find dedicated owners, this table and [`CODEOWNERS`](.github/CODEOWNERS) will be updated.

## Code of Conduct enforcement

The lead maintainer is responsible for enforcement per [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md). Reports are handled confidentially.

## Changing this document

Governance changes follow the RFC process above.

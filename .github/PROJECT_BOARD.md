# Project Board

Frontend Engineering is tracked in a single **GitHub Project (v2)** named **"Frontend Engineering — Content Pipeline."** Unlike a code project, content moves through *research* and *two review stages* before it ships, so the board models an editorial pipeline rather than a sprint.

Create it under the repo's **Projects** tab → New project → Board layout, then add the columns and fields below.

## Columns (Status field)

| # | Column | A card enters when… | A card leaves when… |
| --- | --- | --- | --- |
| 1 | **Backlog** | An article/idea is accepted (`status: accepted`) but unstarted | Someone commits to researching it |
| 2 | **Research** | An author is gathering sources, prior art, and framing | The outline and trade-off axes are settled |
| 3 | **Writing** | Draft is actively being written against the template | A complete draft exists and a PR is opened |
| 4 | **Technical Review** | PR open; a domain maintainer checks correctness, trade-off honesty, runnable examples | Technical concerns are resolved |
| 5 | **Editorial Review** | Prose, clarity, structure, naming, and cross-links are checked | Editorial pass is approved |
| 6 | **Ready** | Approved and merged into `main`; queued for the next release tag | Included in a tagged release |
| 7 | **Published** | Part of a released version and linked from its domain index | — (terminal, unless it ages) |
| 8 | **Needs Update** | A published entry is flagged stale (`status: needs update`) | Re-enters Research/Writing to be refreshed |
| 9 | **Archived** | Superseded, merged into another article, or deliberately retired | — (terminal) |

The two-stage review (Technical → Editorial) is what separates a hobby wiki from a professional reference: correctness and craft are reviewed by different lenses.

## Custom fields

| Field | Type | Values |
| --- | --- | --- |
| Status | Single select | The nine columns above |
| Part | Single select | 00–08 (the nine Parts) |
| Difficulty | Single select | starter · intermediate · advanced |
| Priority | Single select | critical · high · medium · low |
| Type | Single select | article · anti-pattern · example · recipe · correction · tooling |
| Target release | Single select | v0.1 · v0.2 · v0.3 · v0.4 · v0.5 · v1.0 |
| Reading time | Number | minutes |

## Recommended saved views

- **Editorial queue** — filter `Status: Technical Review, Editorial Review`, grouped by Part. What maintainers work from.
- **By release** — board grouped by *Target release*. Progress toward each milestone.
- **By domain** — table grouped by *Part*, to spot thin domains.
- **Stale** — filter `Status: Needs Update`, sorted oldest first.
- **Good first issues** — filter label `good first issue`. For newcomers.

## Automation (Project → Workflows)

- Item added to project → set **Status = Backlog**.
- Issue/PR closed as completed → set **Status = Published** (or Ready if not yet released).
- PR merged → set **Status = Ready**.
- Label `status: needs update` added → set **Status = Needs Update**.
- Label `status: needs review` added → set **Status = Technical Review**.

Keep automation rules in the Project's built-in workflow settings; they cannot live in the repo, so this file documents them.

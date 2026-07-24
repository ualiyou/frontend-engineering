# Label System

A scalable, grouped label taxonomy for Frontend Engineering. Labels use a `group: value` naming convention so they read clearly, filter cleanly, and stay legible as the repository grows. Colors are consistent within a group so the issue list is scannable at a glance.

The machine-readable source of truth is [`labels.yml`](labels.yml), applied automatically by the [Label sync workflow](workflows/label-sync.yml). **Edit `labels.yml`, not the GitHub UI**, so labels never drift.

## Type — what kind of work this is (blue family)

| Label | Color | Meaning |
| --- | --- | --- |
| `type: article` | `#1d76db` | A new decision/trade-off article |
| `type: correction` | `#1d76db` | Fixing an inaccuracy or broken link |
| `type: enhancement` | `#5391d6` | Improvement to repo structure/tooling/templates |
| `type: anti-pattern` | `#0b4f9c` | A documented pitfall |
| `type: example` | `#5391d6` | A minimal code illustration |
| `type: recipe` | `#5391d6` | An end-to-end solution |
| `type: question` | `#84b6eb` | A question about content |
| `type: rfc` | `#0b4f9c` | Structural change requiring an RFC |

## Priority — urgency / order (red → gray gradient)

| Label | Color | Meaning |
| --- | --- | --- |
| `priority: critical` | `#b60205` | Blocks others or is factually wrong in a high-traffic entry |
| `priority: high` | `#d93f0b` | Should be picked up soon |
| `priority: medium` | `#fbca04` | Normal queue |
| `priority: low` | `#c5def5` | Nice to have; no timeline |

## Difficulty — effort for a contributor (green → purple)

| Label | Color | Meaning |
| --- | --- | --- |
| `difficulty: starter` | `#0e8a16` | Small, well-scoped, minimal context needed |
| `difficulty: intermediate` | `#a2eeef` | Requires domain familiarity |
| `difficulty: advanced` | `#5319e7` | Deep expertise or cross-cutting reasoning |

## Status — where it is in the pipeline (yellow / orange)

| Label | Color | Meaning |
| --- | --- | --- |
| `status: triage` | `#fef2c0` | Newly opened, not yet assessed |
| `status: accepted` | `#c2e0c6` | Scope confirmed; ready to be worked |
| `status: in progress` | `#fbca04` | Actively being worked |
| `status: needs review` | `#d4c5f9` | Awaiting technical or editorial review |
| `status: needs update` | `#e99695` | Merged content that has gone stale |
| `status: blocked` | `#000000` | Blocked on a dependency |
| `status: on hold` | `#cccccc` | Deliberately paused |

## Area — which Part of the knowledge map (teal family)

| Label | Color | Meaning |
| --- | --- | --- |
| `area: foundations` | `#006b75` | 00 · Foundations |
| `area: core-languages` | `#0e7c7b` | 01 · Core Languages |
| `area: rendering-frameworks` | `#0e7c7b` | 02 · Rendering & Frameworks |
| `area: app-architecture` | `#128a7d` | 03 · Application Architecture |
| `area: interface-engineering` | `#128a7d` | 04 · Interface Engineering |
| `area: reliability-quality` | `#1a998a` | 05 · Reliability & Quality |
| `area: engineering-systems` | `#1a998a` | 06 · Engineering Systems |
| `area: platform-reach` | `#20b2aa` | 07 · Platform Reach |
| `area: craft-leadership` | `#20b2aa` | 08 · Craft & Leadership |
| `area: tooling` | `#5eb1a8` | CI, scripts, workflows |
| `area: meta` | `#5eb1a8` | Governance, templates, repo docs |

## Community & contribution (accent colors)

| Label | Color | Meaning |
| --- | --- | --- |
| `good first issue` | `#7057ff` | Ideal for first-time contributors |
| `help wanted` | `#008672` | Maintainers actively want help here |
| `documentation` | `#0075ca` | Docs about the repo itself (not knowledge content) |
| `community` | `#c2e0c6` | Events, governance, onboarding |
| `discussion` | `#d876e3` | Needs conversation before action |

## Resolution (why closed)

| Label | Color | Meaning |
| --- | --- | --- |
| `duplicate` | `#cfd3d7` | Already tracked elsewhere |
| `wontfix` | `#ffffff` | Out of scope by decision |
| `stale` | `#795548` | Auto-flagged by the stale workflow |
| `invalid` | `#e6e6e6` | Not actionable as reported |

## Conventions

- **One `type:` per issue** (required). Everything else is optional but encouraged.
- **`area:` on every content issue** so domain maintainers can filter their queue.
- Use `good first issue` **and** `difficulty: starter` together — the first drives GitHub's discovery surfaces, the second is for internal filtering.
- Prefer adding a new `area:` label over inventing a new group.

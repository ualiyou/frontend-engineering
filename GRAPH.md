# Dependency Graph

> The learning-dependency graph over every article in the [Knowledge Map](KNOWLEDGE_MAP.md). For each node (article) it defines the five internal-linking relations — **prerequisites**, **next**, **related**, **alternatives**, **common_mistakes** — plus a **recommended reading order**, a **difficulty tier**, and an **estimated reading time**. The per-node data is machine-readable in each domain's `graph.json`; this file documents the model and the top-level reading path. The relation semantics, invariants, and generation pipeline are specified in [`INTERNAL_LINKING.md`](INTERNAL_LINKING.md); a per-article view of all relations is in [`INTERNAL_LINKS.md`](INTERNAL_LINKS.md).

**Nodes:** 651 articles · **Total estimated reading time:** ~8459 min (~141 h)

## Node schema (`graph.json`)

Each domain folder contains a `graph.json` with one entry per article:

```json
{
  "title": "memo, useMemo, useCallback",
  "slug": "memo-usememo-usecallback.md",
  "subcategory": "Optimization",
  "order": 123,
  "difficulty": "Advanced",
  "reading_time_min": 16,
  "prerequisites": [
    "The Render Phase",
    "Concurrent Rendering"
  ],
  "related": [
    "Referential Stability",
    "The React Compiler Model"
  ],
  "next": [
    "Referential Stability"
  ],
  "alternatives": [
    "The React Compiler Model"
  ],
  "common_mistakes": [
    "anti-patterns/README.md#react",
    "#common-mistakes"
  ]
}
```text

`order` is the global recommended reading position. `prerequisites`, `related`, `next`, and `alternatives` reference article titles; a cross-domain reference is written as `Article · Domain`. `common_mistakes` holds links: the domain's entry in the [`anti-patterns/`](anti-patterns/README.md) catalog and the article's own `#common-mistakes` section.

### The five relations

| Field | Meaning | Direction | Bound | Source |
| --- | --- | --- | --- | --- |
| `prerequisites` | read before | backward (DAG) | ~0–3 | authored; the load-bearing spine |
| `next` | read after | forward (DAG) | ≤5 | **generated** as the inverse of `prerequisites` |
| `related` | see-also | undirected | ~3 | authored |
| `alternatives` | substitutes for the same problem | lateral | ≤4 | generated baseline (same-topic, same-prereq peers), author-refined |
| `common_mistakes` | pitfalls | outward | 2 | generated (domain catalog anchor + in-article section) |

Regenerate `next`/`alternatives`/`common_mistakes` with `scripts/build-links.py` and check invariants with `scripts/validate-links.py`. `next` is always kept consistent with `prerequisites`: if X lists P as a prerequisite, P lists X in `next` (capped, with a forward continuity fallback for domain-terminal articles so no page is a dead end).

## Difficulty tiers

| Tier | Meaning | Base time |
| --- | --- | --- |
| Foundational | Assumes no prior article in the graph | 8 min |
| Intermediate | Assumes the domain's foundations | 12 min |
| Advanced | Assumes cross-domain context | 16 min |
| Staff | Judgment / leadership, few hard prerequisites | 20 min |

Reading time = tier base + 3 min for compound topics. Tier is derived from the article's Part, domain, and subcategory (see `references` in the generator).

Distribution: Foundational 169 · Intermediate 288 · Advanced 160 · Staff 34.

## Cross-domain dependency DAG

Each domain declares the domains it builds on. Prerequisites for a domain's entry article point into these:

```text
Computer Science for Frontend  ←  — (root)
The Web Platform  ←  Computer Science for Frontend
Runtime & Execution  ←  The Web Platform
Browser APIs  ←  The Web Platform
Networking & Protocols  ←  The Web Platform
HTML & Document Semantics  ←  The Web Platform
CSS & Visual Systems  ←  The Web Platform
JavaScript  ←  Computer Science for Frontend, Runtime & Execution
TypeScript  ←  JavaScript
Rendering Architectures  ←  The Web Platform, Networking & Protocols
React  ←  JavaScript, Rendering Architectures, HTML & Document Semantics
Reactivity & Framework Models  ←  JavaScript, Rendering Architectures
Routing  ←  Rendering Architectures, Browser APIs
Frontend Architecture  ←  React, TypeScript
State Management  ←  React, JavaScript
Data & Server State  ←  Networking & Protocols, React, State Management
Forms & Validation  ←  React, TypeScript, State Management
API Design & Contracts  ←  Networking & Protocols, TypeScript
Component & Interaction Design  ←  React, CSS & Visual Systems
Design Systems  ←  CSS & Visual Systems, Component & Interaction Design
Accessibility  ←  HTML & Document Semantics, Component & Interaction Design
Animation & Motion  ←  CSS & Visual Systems, The Web Platform
Performance Engineering  ←  The Web Platform, Runtime & Execution, Networking & Protocols
Security  ←  Networking & Protocols, Browser APIs
Testing & Quality  ←  React, JavaScript
Observability & Reliability  ←  Performance Engineering, Delivery & Infrastructure
Build Systems & Tooling  ←  JavaScript, Package Architecture
Package Architecture  ←  JavaScript
Developer Experience & Workflow  ←  Build Systems & Tooling, Testing & Quality
Delivery & Infrastructure  ←  Build Systems & Tooling, Networking & Protocols
Internationalization & Localization  ←  CSS & Visual Systems, JavaScript
Progressive & Cross-Platform Web  ←  Browser APIs, Networking & Protocols, Performance Engineering
Graphics & Immersive  ←  The Web Platform, Runtime & Execution
Engineering Practices  ←  Frontend Architecture, Testing & Quality
Systems Thinking & Leadership  ←  Frontend Architecture, Engineering Practices
```

## Recommended reading order (top level)

Read Parts 00→08 in order; within each Part, domains in the sequence below. Per-article order is the `order` field in `graph.json`.

| # | Domain | Part | Articles | ~Time |
| --- | --- | --- | --- | --- |
| 1 | Computer Science for Frontend | 00 | 18 | 156 min |
| 2 | The Web Platform | 00 | 18 | 156 min |
| 3 | Runtime & Execution | 00 | 18 | 243 min |
| 4 | Browser APIs | 00 | 23 | 199 min |
| 5 | Networking & Protocols | 00 | 19 | 170 min |
| 6 | HTML & Document Semantics | 01 | 16 | 128 min |
| 7 | CSS & Visual Systems | 01 | 29 | 250 min |
| 8 | JavaScript | 01 | 31 | 275 min |
| 9 | TypeScript | 01 | 25 | 234 min |
| 10 | Rendering Architectures | 02 | 17 | 225 min |
| 11 | React | 02 | 33 | 436 min |
| 12 | Reactivity & Framework Models | 02 | 10 | 169 min |
| 13 | Routing | 02 | 16 | 204 min |
| 14 | Frontend Architecture | 03 | 16 | 210 min |
| 15 | State Management | 03 | 18 | 231 min |
| 16 | Data & Server State | 03 | 20 | 255 min |
| 17 | Forms & Validation | 03 | 16 | 213 min |
| 18 | API Design & Contracts | 03 | 14 | 233 min |
| 19 | Component & Interaction Design | 04 | 16 | 207 min |
| 20 | Design Systems | 04 | 15 | 192 min |
| 21 | Accessibility | 04 | 19 | 237 min |
| 22 | Animation & Motion | 04 | 14 | 168 min |
| 23 | Performance Engineering | 05 | 22 | 303 min |
| 24 | Security | 05 | 24 | 387 min |
| 25 | Testing & Quality | 05 | 18 | 231 min |
| 26 | Observability & Reliability | 05 | 15 | 255 min |
| 27 | Build Systems & Tooling | 06 | 16 | 216 min |
| 28 | Package Architecture | 06 | 13 | 220 min |
| 29 | Developer Experience & Workflow | 06 | 23 | 285 min |
| 30 | Delivery & Infrastructure | 06 | 17 | 278 min |
| 31 | Internationalization & Localization | 07 | 16 | 265 min |
| 32 | Progressive & Cross-Platform Web | 07 | 15 | 246 min |
| 33 | Graphics & Immersive | 07 | 14 | 283 min |
| 34 | Engineering Practices | 08 | 20 | 335 min |
| 35 | Systems Thinking & Leadership | 08 | 17 | 364 min |

## How this graph is maintained

This is the generated baseline graph (v1): prerequisites and related edges are derived from the taxonomy's structure and the cross-domain DAG above, and the `next`, `alternatives`, and `common_mistakes` edges are derived from those by `scripts/build-links.py`. As articles are written, each may refine its own `prerequisites`/`related`/`alternatives` in `graph.json` and mirror them in the article's frontmatter; rerun `build-links.py` to refresh the inverse `next` edges and `validate-links.py` to enforce the invariants. The invariants are that the prerequisite graph stays acyclic, every edge points to an existing node, `next` never contradicts `prerequisites`, and `alternatives` stays symmetric. See [`INTERNAL_LINKING.md`](INTERNAL_LINKING.md) for the full model.

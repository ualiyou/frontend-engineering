---
layout: home
title: Frontend Engineering
titleTemplate: Engineering decisions, not tutorials
description: A peer-reviewed knowledge base of frontend engineering patterns, trade-offs, and production-ready practices — framework-aware, not framework-bound.

hero:
  name: Frontend Engineering
  text: Engineering decisions, not tutorials
  tagline: Stop re-litigating frontend decisions from scratch. Find the trade-offs, choose deliberately, and ship the decision your future team can defend.
  image:
    src: /logo.svg
    alt: Frontend Engineering
  actions:
    - theme: brand
      text: Start with a decision
      link: /docs/03-application-architecture/data-server-state/
    - theme: alt
      text: Knowledge Map
      link: /KNOWLEDGE_MAP
    - theme: alt
      text: GitHub
      link: https://github.com/ualiyou/frontend-engineering

features:
  - title: Trade-offs, stated honestly
    details: Every article names what you give up, when the balance flips, and which alternative wins in each case — then makes a defensible recommendation.
  - title: Production code, not toys
    details: Each pattern ships a naive version, a corrected version, and a production version with error handling, cancellation, and accessibility included.
  - title: A dependency graph, not a blog
    details: Prerequisites, next steps, alternatives, and common mistakes are typed links between articles, validated in CI so the map never lies.
  - title: Framework-aware, not framework-bound
    details: Concepts are owned once and cross-linked. Framework specifics are called out with versions where behavior depends on them.
---

## Where to start

- **Working on data fetching or caching?** [Data & Server State](/docs/03-application-architecture/data-server-state/) is the most complete domain — request identity, staleness, mutations, pagination, and resilience.
- **Deciding where state should live?** [State Management](/docs/03-application-architecture/state-management/) starts with the classification that makes the rest of the decisions mechanical.
- **Chasing a performance problem?** [Performance Engineering](/docs/05-reliability-quality/performance/) covers the critical rendering path, Core Web Vitals, and code splitting.
- **Want the whole picture?** The [Knowledge Map](/KNOWLEDGE_MAP) lays out nine Parts and 35 domains; the [Article Inventory](/ARTICLE_INVENTORY) lists every article with its status, difficulty, and prerequisites.

## What this is not

Not a tutorial site, not a framework comparison scoreboard, and not a link dump. Articles are reviewed against the [standards](/standards/), carry explicit prerequisites, and are expected to stay useful for years — so anything that only makes sense inside one release cycle does not belong here.

Contributions are welcome: read [CONTRIBUTING](/CONTRIBUTING) for the article template, the review criteria, and how the link graph is validated.

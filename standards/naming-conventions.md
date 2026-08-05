# Naming Conventions

Naming rules for every artifact in **Frontend Engineering** — files, folders, images, examples, recipes, anti-patterns, case studies, and decision records. Names are the cheapest and most durable form of consistency: a good scheme means a reader (or a script) can predict where a thing lives and what it is called without being told. These rules extend and formalize the naming section in [`CONTRIBUTING.md`](../CONTRIBUTING.md).

The governing rule everywhere: **lowercase `kebab-case`, descriptive of the topic, stable once published.**

## Table of contents

- [The one rule](#the-one-rule)
- [Files](#files)
- [Folders](#folders)
- [Images and assets](#images-and-assets)
- [Examples](#examples)
- [Recipes](#recipes)
- [Anti-patterns](#anti-patterns)
- [Case studies](#case-studies)
- [Decision records (ADRs)](#decision-records-adrs)
- [Branches and commits](#branches-and-commits)
- [Anchors and slugs](#anchors-and-slugs)
- [Reserved and special names](#reserved-and-special-names)

## The one rule

`lowercase-kebab-case`, no spaces, no underscores, no camelCase, ASCII only, `.md` extension for prose. A filename describes the **topic**, not the format or a sequence number: `optimistic-updates.md`, never `article-3.md`, `Optimistic_Updates.md`, or `final-v2.md`.

Two properties matter most: **descriptive** (a reader knows the content from the name) and **stable** (the name is a URL and a link target; once published it does not change, because changing it breaks every inbound link and the concept's canonical identity).

## Files

- **Article files:** `<slug>.md`, kebab-case, matching the frontmatter `slug`. `server-vs-client-state.md`, `cache-invalidation-strategies.md`.
- **Slug = topic, in words a reader would search.** Prefer the noun phrase of the concept: `render-props.md`, not `advanced-react-pattern-2.md`.
- **No versions, dates, or status in filenames.** `status` and `version` live in frontmatter; a file named `-old`, `-new`, `-v2`, or `-draft` is a smell.
- **One primary topic per file** (the [one-decision-per-file](./content-framework.md#the-nine-invariants) invariant). Splitting a file creates two well-named files, never `part-1` / `part-2`.
- **Index files are `README.md`** (uppercase, by GitHub convention) in every directory that needs an overview.
- **Meta/root docs are `SCREAMING_SNAKE.md`** by established repository convention (`KNOWLEDGE_MAP.md`, `GRAPH.md`, `INTERNAL_LINKING.md`, `CONTRIBUTING.md`). New root-level meta docs follow that pattern; **files inside `standards/` are kebab-case** (`article-quality.md`) because they are a cohesive set, not top-level community docs.

## Folders

- **`kebab-case`, matching the taxonomy** in the [Knowledge Map](../KNOWLEDGE_MAP.md).
- **Parts are numbered, zero-padded, with the number a stable prefix:** `00-foundations`, `01-core-languages`, … `08-craft-leadership`. The number encodes reading gradient and never changes.
- **Domains are unnumbered kebab-case** under their Part: `data-server-state`, `state-management`, `html-semantics`.
- **Do not introduce a new top-level folder** without a governance decision — the fixed set (`docs/`, `paths/`, `examples/`, `recipes/`, `anti-patterns/`, `templates/`, `assets/`, `scripts/`, `standards/`, `.github/`) is the repository's shape.
- **Sub-collections within a domain** (e.g. `case-studies/`) are kebab-case folders inside the domain directory.

## Images and assets

- **Named for the article they support:** `<article-slug>-<what-it-shows>.<ext>` in `assets/`. `optimistic-updates-sequence.svg`, `rendering-strategies-comparison.svg`.
- **Prefer `.svg`** for diagrams and line art (diffable, scalable, accessible); `.png` only for UI screenshots; never `.jpg` for diagrams.
- **No generic names** (`diagram.svg`, `image1.png`, `screenshot.png`) — the name says which article and which figure.
- **Branding assets** live in `assets/branding/` and keep their established names (`logo.svg`, `banner.svg`, `social-preview.svg`).
- Inline Mermaid needs no file (see [`diagram-guide.md`](./diagram-guide.md)); only exported/hand-authored graphics get filenames.

## Examples

- **Location:** [`examples/`](../examples/), a minimal illustration of a single point.
- **Named for the concept and the point:** `abort-on-unmount.tsx`, `discriminated-union-state.ts`. Include the extension of the language shown.
- **Multi-file examples** get a kebab-case folder: `examples/debounced-search/` containing files named per the feature-first structure in [`code-example-standard.md`](./code-example-standard.md#folder-structure) (`DebouncedSearch.tsx`, `use-debounced-search.ts`).
- Component files inside an example are `PascalCase.tsx` (matching the export); hooks and logic files are `kebab-case.ts`.

## Recipes

- **Location:** [`recipes/`](../recipes/), an end-to-end solution to a recurring problem.
- **Named for the problem solved, as a task:** `infinite-scroll-with-restoration.md`, `optimistic-form-submission.md` — verb-or-outcome oriented, because a recipe is about *doing*, whereas an article is about *deciding*.
- **Multi-file recipes** get a folder `recipes/<recipe-slug>/` with a `README.md` entry point and source files following the code standard's structure.

## Anti-patterns

- **Location:** [`anti-patterns/`](../anti-patterns/).
- **Named for the smell, plainly:** `use-effect-as-data-fetcher.md`, `prop-drilling.md`, `index-as-key.md` — name the mistake so it is greppable and memorable.
- **Do not name by the fix** (`avoid-prop-drilling.md`) — name the anti-pattern itself; the file explains why it fails and links the correct approach.
- Per-domain catalog anchors are generated (`#javascript`, `#data-server-state`); do not hand-author anchor names that links depend on.

## Case studies

- **Location:** `docs/<part>/<domain>/case-studies/<slug>.md`.
- **Named for the system and the decision:** `global-state-migration.md`, `ssr-adoption-at-scale.md` — concrete and specific, since a case study is one story, not a category.
- **Anonymize where required**, but keep the name descriptive of the *situation*, not a placeholder (`legacy-app-migration.md`, not `case-1.md`).

## Decision records (ADRs)

For decisions about the repository itself (structure, tooling, policy) — the output of the RFC process in [`GOVERNANCE.md`](../GOVERNANCE.md). ADRs do not exist as a collection yet; this defines the convention for when they are added.

- **Location:** `docs/decisions/` or `.github/adr/` (choose one at adoption; prefer `docs/decisions/`).
- **Named `NNNN-kebab-title.md`** with a zero-padded, monotonically increasing number: `0001-adopt-mermaid-for-diagrams.md`, `0002-snake-case-frontmatter.md`.
- **The number is permanent and never reused**, even if the ADR is later superseded (superseding ADRs link back: "supersedes 0002").
- **Title is the decision, not the topic:** `0003-cap-next-links-at-five.md`.

## Branches and commits

- **Branches:** `<type>/<short-description>`, `type` ∈ `docs` | `fix` | `chore` | `refactor`. `docs/optimistic-updates`, `fix/broken-graph-link`.
- **Commits:** [Conventional Commits](https://www.conventionalcommits.org/). `docs(data-server-state): add optimistic updates article`, `fix(links): repair cross-domain reference in promises`.
- **Scope is the domain or subsystem** in kebab-case, matching folder names.

## Anchors and slugs

- **A `slug` never changes once published** — it is the article's identity and its URL. A concept that outgrows its slug gets a *new* article, with the old one deprecated per the [evergreen policy](./evergreen-policy.md), not a renamed file.
- **Heading anchors are GitHub-generated** from heading text (lowercased, spaces → hyphens, punctuation stripped). Because other files deep-link to them, **treat published heading text as stable** (see [`writing-style.md`](./writing-style.md#headings)).
- **Cross-domain reference names** are `Article · Domain` only when a title is ambiguous across domains; otherwise the bare `Title`. See [`INTERNAL_LINKING.md`](../INTERNAL_LINKING.md).

## Reserved and special names

- **`README.md`** — directory index (uppercase).
- **`.gitkeep`** — placeholder to keep an empty directory tracked; removed once the directory has content.
- **`graph.json`** — the per-domain relation source of truth; one per domain, never renamed.
- **`_to_delete/`** — staging area for removal; nothing is authored here and nothing links into it.
- **Leading-underscore or dot-prefixed names** are for tooling/meta only, never for content.

---

**Next:** [`metadata-schema.md`](./metadata-schema.md) — where `slug` is declared · [`linking-rules.md`](./linking-rules.md) — how these names become links · [`content-framework.md`](./content-framework.md) — the one-topic-per-file invariant.

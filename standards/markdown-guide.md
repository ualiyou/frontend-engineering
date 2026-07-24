# Markdown Standard

The formatting rules for every Markdown file in **Frontend Engineering**. Consistent Markdown is what lets 1000+ files feel like one book: the same heading rhythm, the same admonitions, the same link style, page after page. These rules are enforced by [`.markdownlint.jsonc`](../.markdownlint.jsonc) where possible and by review otherwise.

We write **CommonMark + GitHub Flavored Markdown (GFM)**, and nothing that depends on a specific renderer's extensions beyond GFM.

## Table of contents

- [Headings](#headings)
- [Lists](#lists)
- [Tables](#tables)
- [Blockquotes](#blockquotes)
- [Admonitions](#admonitions)
- [Callouts](#callouts)
- [Code blocks](#code-blocks)
- [Images](#images)
- [Links](#links)
- [Horizontal rules](#horizontal-rules)
- [Footnotes](#footnotes)
- [Whitespace and line rules](#whitespace-and-line-rules)

## Headings

- **ATX style only** (`##`), never Setext (underlined). A space after the hashes.
- **Exactly one H1** per file, the title, at the top (after frontmatter).
- **Never skip levels** — H2 → H3 → H4, no H2 → H4.
- **Sentence case** for all headings except the H1 title (Title Case). See [`writing-style.md`](./writing-style.md#headings).
- **Blank line before and after** every heading (required for correct rendering).
- **No trailing punctuation** except `?`. No emoji in headings.
- **Unique heading text within a file** — duplicate headings produce colliding anchors and break deep links.
- Headings are anchors other files link to; treat their text as stable API once published.

## Lists

- **A blank line before every list** (CommonMark requires it — without it the list renders as a paragraph).
- **`-` for unordered lists**, consistently (not `*` or `+`).
- **`1.` for ordered lists;** you may keep every marker `1.` (auto-numbered) or number them sequentially, but be consistent within a list.
- **Two-space indent** for nested items; a blank line before a nested list.
- **List items are phrases or sentences, punctuated consistently:** if one item ends with a period, all do.
- **Use lists for genuinely parallel items only.** Do not convert an argument into bullets — that hides the logical connectives. Prose carries reasoning; lists carry enumerations. (This is a content rule from [`writing-style.md`](./writing-style.md), enforced in review.)
- **Task lists** (`- [ ]`) are for the article's Checklist section and pull-request checklists only.

## Tables

- **GFM pipe tables.** Header row, delimiter row, then data.
- **Always include a header row**; a table without headers should be a list.
- **Align the delimiter to intent** (`:---` left, `:---:` center, `---:` right) — default left; right-align numeric columns.
- **Keep cells short** — a phrase, not a paragraph. If a cell needs a paragraph, the content is not tabular.
- **Escape pipes** inside cells as `\|`, and put inline code/links inside cells normally.
- **Do not use tables for layout** — only for genuinely tabular data (comparisons, trade-off matrices, field references).
- Source alignment (padding columns to equal width in the raw file) is nice but not required; content correctness is.

## Blockquotes

- **`>` for quotations and for the article's one-line summary** under the H1.
- **Blank line before and after.**
- Do not use blockquotes for emphasis of ordinary text — that is what bold or an admonition is for.
- Multi-line quotes prefix every line with `>`; a blank quoted line is a bare `>`.

## Admonitions

Because plain GitHub Markdown has limited native callout support, we standardize on **GitHub's alert syntax** (a blockquote whose first line is a typed marker), which renders as a styled admonition on GitHub and degrades gracefully to a labeled blockquote everywhere else. The *when and voice* rules are in [`writing-style.md`](./writing-style.md#warnings-notes-and-tips-admonitions); this is the syntax.

```markdown
> [!NOTE]
> Context the reader can act on but should not skip. Neutral tone.

> [!TIP]
> A non-obvious, correct improvement or shortcut.

> [!WARNING]
> A real risk of a bug, data loss, security hole, or a11y break. Reserve it.
```

- **Only these three types** map to GitHub alerts: `NOTE`, `TIP`, `WARNING`. (`IMPORTANT` and `CAUTION` also render but we do not use them — `WARNING` covers risk, `NOTE` covers everything else — to keep the vocabulary small.)
- **The `Recommendation` callout** (the article's default) is a plain bold-led blockquote, not a `[!TYPE]` alert, so it is visually distinct from risk admonitions:

```markdown
> **Recommendation:** Use server state for shared data; keep ephemeral UI state local.
```

- **One to three sentences** per admonition; **never nest**; **never hide** an example's only code inside one.
- **Blank line before and after** the whole block.

## Callouts

"Callout" is our umbrella word for the visually-set-apart devices above. The complete, closed set is: the **one-line summary** (`>` under H1), the **Recommendation** (bold-led `>`), the **At a Glance** table, and the three **admonitions**. There is no other callout style — do not invent boxed asides, emoji banners, or horizontal-rule-fenced notes. A small, fixed vocabulary is what keeps 1000 files consistent.

## Code blocks

- **Fenced, never indented.** Triple backticks with a language tag on every block: ` ```tsx `, ` ```ts `, ` ```css `, ` ```html `, ` ```bash `, ` ```json `, ` ```mermaid `, ` ```text ` (for trees/output with no language).
- **A language tag is mandatory** — an untagged fence fails lint and review.
- **Blank line before and after** the block.
- **Inline code in backticks** for identifiers, filenames, flags, keys, and values in prose.
- **Do not put a code block inside a list item's flow** in a way that breaks numbering; if a step needs a block, place it indented under the item with surrounding blank lines, or restructure.
- Code content rules (types, error handling, naming, comments) live in [`code-example-standard.md`](./code-example-standard.md); this is only about the fence.

## Images

- **Every image has descriptive alt text** stating what it shows, not "image" or "diagram of X." See [`diagram-guide.md`](./diagram-guide.md#accessibility-and-alt-text).
- **Relative paths into `assets/`**: `![Alt describing the content](../../../assets/<slug>-<what>.svg)`.
- **Prefer SVG** for diagrams and line art; PNG only for UI screenshots.
- **Name by the article** they support (see [`naming-conventions.md`](./naming-conventions.md)).
- **No image carries information the prose omits** — images illustrate; text is the source of truth (accessibility + durability).
- Provide width via HTML `<img>` only when necessary (e.g. logos); prefer plain Markdown otherwise.

## Links

- **Descriptive link text**, never "click here" or a bare URL in prose. The text names the destination: `[the internal-linking model](../INTERNAL_LINKING.md)`.
- **Relative links for anything in-repo** (articles, assets, standards); absolute `https://` only for external sources.
- **Same-domain article links:** `[Text](./slug.md)`. **Cross-domain:** `[Text](../../<part>/<domain>/slug.md)` and, in prose, name it as `Article · Domain`. This is the [internal-linking](../INTERNAL_LINKING.md) contract.
- **Link the canonical home of a concept, never re-explain it.**
- **Deep links** to a heading use its exact GitHub-generated anchor (`./file.md#the-problem`).
- **No dead links** — CI (`scripts/validate-links.py` and the dead-link workflow) enforces this; add intentional external exceptions to [`.lycheeignore`](../.lycheeignore).
- **Reference-style links** are allowed for repeated URLs but inline is the default for readability.

## Horizontal rules

- **`---` on its own line, with a blank line before and after.**
- Use sparingly: to separate frontmatter, and as the single divider before an article's footer nav block. Do not scatter rules between every section — headings already separate content.
- Never use `***` or `___`; `---` only, for one consistent style.

## Footnotes

- **GFM footnotes are allowed but rarely needed.** Prefer a References entry or an inline parenthetical to a footnote.
- Syntax: `text[^1]` … and later `[^1]: the note.`
- **Use for a genuine aside or citation** that would break the sentence's flow — not as a dumping ground. If a footnote carries load-bearing reasoning, promote it into the prose.
- Number footnotes with meaningful labels (`[^abort]`) rather than bare integers where it aids maintenance.

## Whitespace and line rules

- **One sentence or one clause per source line is encouraged** (semantic line breaks) — it makes diffs readable — but hard-wrapping mid-sentence to a column is not required. Do not fight the linter over wrap width in prose.
- **A single trailing newline** at end of file; no trailing whitespace on lines (except the two-space hard break, which we avoid — use real paragraph breaks).
- **No consecutive blank lines** (max one).
- **Frontmatter** (`---` delimited YAML) is the first thing in every article, no blank line before it. See [`metadata-schema.md`](./metadata-schema.md).
- Files pass `markdownlint` with the repository config and `cspell` with [`cspell.json`](../cspell.json). Add new proper nouns to the dictionary rather than disabling the rule.

---

**Next:** [`writing-style.md`](./writing-style.md) — the voice inside the formatting · [`metadata-schema.md`](./metadata-schema.md) — the frontmatter block · [`diagram-guide.md`](./diagram-guide.md) — Mermaid and image specifics.

# Writing Style

The voice of **Frontend Engineering**. Every article should read as if it came from the same careful author — the way the React docs, the TypeScript handbook, and MDN each read as one voice despite many contributors. This document is how we get there.

The target voice, in one line: **a senior engineer explaining a decision to a peer — precise, calm, and honest, with nothing to sell.**

## Table of contents

- [The voice in one paragraph](#the-voice-in-one-paragraph)
- [Wording](#wording)
- [Banned and discouraged words](#banned-and-discouraged-words)
- [Sentence length and rhythm](#sentence-length-and-rhythm)
- [Headings](#headings)
- [Code comments](#code-comments)
- [Examples](#examples)
- [Terminology](#terminology)
- [Capitalization](#capitalization)
- [Emphasis](#emphasis)
- [Warnings, notes, and tips](#warnings-notes-and-tips-admonitions)
- [Person, tense, and voice](#person-tense-and-voice)
- [A worked before/after](#a-worked-beforeafter)

## The voice in one paragraph

Write like you are reviewing a colleague's design doc: direct, specific, and generous with reasoning. Prefer the plain word to the fancy one, the short sentence to the long one, and the measured claim to the confident one. Never sell. The reader is a competent engineer; respect their time by leading with the point, and respect their intelligence by showing the trade-offs instead of hiding them. When you are unsure, say so and say why. When you recommend, give the reason in the same breath.

## Wording

- **Plain over ornate.** "use" not "utilize," "before" not "prior to," "so" not "in order to," "about" not "with respect to."
- **Concrete over abstract.** Name the mechanism. "This triggers a re-render on every keystroke" beats "this has performance implications."
- **Active over passive**, unless the actor is genuinely irrelevant. "The reducer updates the store," not "the store is updated."
- **Verbs over nominalizations.** "decide" not "make a decision," "fails" not "results in a failure."
- **Cut hedges and filler.** Delete "basically," "essentially," "of course," "as we all know," "it's worth noting that," "in today's world." If a sentence survives deletion of its first four words, delete them.
- **No filler intensifiers.** "very," "really," "quite," "extremely" add nothing to technical prose. A measurement adds everything.
- **Say the hard part.** If a technique is error-prone, write "this is easy to get wrong" — do not soften it into "requires care."

## Banned and discouraged words

**Banned** (marketing register — never in prose):

> blazing fast · lightning fast · game-changer · revolutionary · seamless · effortless · magical · powerful · robust (as filler) · cutting-edge · next-generation · supercharge · unlock · delight · simply · just (as in "just do X") · obviously · trivially · everyone knows

**Discouraged** (usually a symptom of vague thinking — replace with specifics):

> fast/slow → *quantify* · good/bad → *state the criterion* · modern/legacy → *name the version or year* · best practice → *name the practice and its reason* · scalable → *scales along which axis, to what* · clean → *say what property you mean* · a lot / many → *give a number or order of magnitude*

"Simply" and "just" are called out specifically: they tell a struggling reader the thing they find hard is trivial, which is both untrue and unkind. Delete them.

## Sentence length and rhythm

- **Aim for 15–25 words per sentence** on average. Vary deliberately: a short sentence lands a point; a longer one carries a chain of reasoning.
- **One idea per sentence.** If a sentence has two `and`s joining independent clauses, it is probably two sentences.
- **Paragraphs are 2–5 sentences**, each making one move in the argument. A one-sentence paragraph is fine for emphasis.
- **Front-load the point.** Topic sentence first, support after. The reader should be able to read only the first sentence of each paragraph and still follow the thread.
- **Prose carries reasoning; lists carry enumerations.** Do not turn an argument into bullet points to look organized — that hides the logical connectives (*because*, *therefore*, *unless*) that are the argument. Use a list only for genuinely parallel items.

## Headings

- **Sentence case, not Title Case,** for section headings: "When not to use," not "When Not To Use." (The article's H1 title is the one exception — it is Title Case, matching frontmatter `title`.)
- **Exactly one H1 per file,** the title. Never skip a level (no H2 → H4).
- **Question-shaped or noun-phrase headings.** "How does invalidation work?" or "Invalidation model" — both scan and both help search. Avoid single vague words like "Details" or "More."
- **Headings are signposts, not suspense.** State what the section concludes, not just its topic, where you can: "Prefer server state for shared data" beats "Server state."
- **No punctuation at the end** except a question mark. No trailing colons.
- **Stable headings.** Once published, a heading is an anchor other articles link to; changing it breaks links. Treat heading text as an API (see [`INTERNAL_LINKING.md`](../INTERNAL_LINKING.md)).

## Code comments

- **Comment the *why*, not the *what*.** The code says what; the comment says why this way and not the obvious other way. `// debounce to avoid a request per keystroke` — good. `// set the value` — noise, delete it.
- **Mark the teaching point.** In examples, a comment pins the exact line that matters: `// ❌ race: this resolves after the newer request` or `// ✅ AbortController cancels the stale fetch`.
- **Full sentences, capitalized, no trailing period** for single-line comments; periods for multi-sentence blocks. Be consistent within a file.
- **No commented-out code** in examples. If it shouldn't run, it shouldn't be there.
- **No apologies or TODOs in published examples.** `// TODO: handle errors` is a failing example — handle them.
- **Comments are prose too.** All the wording rules above apply inside comments: plain, specific, no marketing.

## Examples

- **Realistic, not toy.** An example is a scene from a real codebase: real names, real error handling, real edge cases. See [`code-example-standard.md`](./code-example-standard.md) for the hard rules; this section is about *tone*.
- **Minimal but complete.** Show the smallest code that still handles what production must handle. Remove anything not serving the point — but "handles errors" is always serving the point.
- **Domain-neutral, non-cutesy names.** `user`, `invoice`, `searchResults` — not `foo`, `bar`, `thingy`, `doStuff`. Names teach.
- **The Bad Example is genuinely tempting.** It must be the mistake a competent engineer actually makes, not a strawman no one would write. If the bad example is obviously bad, it teaches nothing.
- **Explain the diff.** After each example, one short paragraph connects the code to the reasoning: what goes wrong / why this is better. Never let code stand unexplained.

## Terminology

- **One term per concept, for the life of the article.** Pick "server state" or "remote state" and never switch. Silent synonyms make readers wonder if you mean something new.
- **Define on first use** if the term is non-obvious, then use it freely. Link the canonical article rather than re-defining a term that has its own home.
- **Use the ecosystem's real names, spelled the ecosystem's way:** JavaScript, TypeScript, npm, ESLint, Node.js, React, Vite, WebSocket, URL, API, HTTP, CSS, HTML, ARIA. See the capitalization list below.
- **Prefer the specific term to the buzzword.** "memoization" not "performance optimization," "cache invalidation" not "data freshness handling."
- **Avoid coining terms.** If a widely used name exists, use it. If you must name something new, say so explicitly and define it.
- Keep the shared spellings in [`cspell.json`](../cspell.json) authoritative — add new proper nouns there so CI passes.

## Capitalization

- **Product and technology names as their owners write them:** JavaScript, TypeScript, React, Node.js, Next.js, npm (lowercase), pnpm (lowercase), ESLint, Prettier, Vite, Vitest, Playwright, GraphQL, WebSocket, JSON, HTML, CSS, DOM, URL, API, HTTP(S), ARIA, WCAG, CI, SSR, CSR, RSC.
- **Sentence case for headings and table headers.**
- **Title Case only for the article H1 title.**
- **Do not capitalize for emphasis.** Never write "This is REQUIRED" — use `**required**` or an admonition.
- **Code identifiers keep their real casing** and go in backticks: `useEffect`, `AbortController`, `queryClient`, `--force`.
- **Acronyms uppercase** (API, DOM, CSS) unless the canonical spelling is lower (npm, iOS).

## Emphasis

- **Bold for the load-bearing phrase** a scanning reader must not miss — one per paragraph at most. Overused bold reads as shouting and stops working.
- **Italics for a defined term on first mention** or a light contrastive stress (*server* state versus *client* state).
- **Backticks for anything from a keyboard:** identifiers, filenames, flags, keys, values, package names, HTTP methods.
- **Never underline** (reads as a link) and **never ALL CAPS** for emphasis.
- **Do not stack** bold+italic for ordinary emphasis; reserve it for nothing (it looks frantic).
- If everything is emphasized, nothing is. Default to plain text and let structure carry weight.

## Warnings, notes, and tips (admonitions)

We use a small, fixed set of admonitions. Definitions and exact Markdown syntax live in [`markdown-guide.md`](./markdown-guide.md#admonitions); this section governs *when* and *in what voice* to use each.

- **Note** — context a reader can act on but not skip safely. Neutral tone. Use for a caveat, a scope boundary, or a clarification. Do not use for asides that could just be a sentence.
- **Tip** — a non-obvious improvement or shortcut that is genuinely useful and correct. Not a place for opinion; if it is a recommendation, it belongs in the Trade-offs or Recommendation, not a tip.
- **Warning** — a real risk of a bug, data loss, security hole, or accessibility break. Reserve it. State the risk, the trigger, and the fix, in that order. A warning that fires on a minor style preference trains readers to ignore warnings.
- **Recommendation** — the article's defensible default (the blockquote after the TL;DR). One line, conditional. Exactly one per article.

Rules for all admonitions: **use sparingly** (more than one warning per screen means none of them are read), keep each to **one to three sentences**, never nest them, and never put a code block's only copy inside one (it hurts copyability and accessibility).

## Person, tense, and voice

- **Address the reader as "you."** "You'll get a stale value on the second render." Warm and direct.
- **Refer to the author as "we"** for repository conventions ("we recommend," "we don't cover tutorials") — it is a collective, reviewed voice, not a personal blog.
- **Present tense** for how things behave: "the effect runs after paint," not "the effect will run."
- **No first-person singular.** This is not a personal essay; there is no "I."
- **Describe behavior, not intent of the machine.** "The scheduler batches these updates," not "React wants to batch these."

## A worked before/after

**Before** (marketing, vague, passive, over-emphasized):

> In today's modern web, **performance is absolutely CRITICAL**. Luckily, memoization is a super powerful technique that can be utilized to make your components blazing fast. It's basically just wrapping things in `useMemo` and you're good to go!

**After** (plain, specific, honest, calm):

> Memoization trades memory and a little complexity for fewer recomputations. Wrapping a value in `useMemo` skips recomputing it when its dependencies are unchanged — useful when the computation is expensive *and* runs often. It is not free: each memo adds a dependency array to maintain and a cache to hold, so applying it everywhere usually costs more than it saves.

The second version says what happens, when it helps, and what it costs — and sells nothing.

---

**Next:** [`article-quality.md`](./article-quality.md) — the structure this voice fills · [`markdown-guide.md`](./markdown-guide.md) — formatting and admonition syntax · [`content-framework.md`](./content-framework.md) — the philosophy behind the voice.

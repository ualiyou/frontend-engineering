---
title: "The Box Model"
slug: the-box-model
description: "What `width` actually measures, why `border-box` became the default everyone sets, and how margin collapsing and logical properties change the geometry."
keywords: ["CSS box model", "box-sizing", "border-box", "content-box", "margin collapsing", "logical properties", "inline-size", "padding", "border", "intrinsic sizing"]
part: "01 · Core Languages"
domain: "CSS & Visual Systems"
subcategory: "Box & Formatting"
difficulty: "Foundational"
reading_time_min: 8
priority: "Critical"
status: "Published"
canonical: true
last_reviewed: "2026-08-09"
prerequisites:
  - "Specificity"
related:
  - "Formatting Contexts"
  - "Stacking Contexts & z-index"
  - "Containment & content-visibility"
next:
  - "Formatting Contexts"
  - "Stacking Contexts & z-index"
  - "Containment & content-visibility"
  - "Normal Flow"
  - "Flexbox"
alternatives: []
common_mistakes:
  - "anti-patterns/README.md#css-visual-systems"
  - "#common-mistakes"
frameworks: []
references:
  - { title: "CSS Box Model Module Level 3", url: "https://www.w3.org/TR/css-box-3/" }
  - { title: "CSS Box Sizing Module Level 3", url: "https://www.w3.org/TR/css-sizing-3/" }
  - { title: "MDN — The box model", url: "https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model" }
  - { title: "MDN — CSS logical properties and values", url: "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_logical_properties_and_values" }
---

# The Box Model

> `width: 300px` does not mean the element is 300 pixels wide. It means one of two different things, and CSS shipped with the less useful one as the default.

**Part:** [01 · Core Languages](../) · **Domain:** CSS & Visual Systems · **Priority:** Critical · **Difficulty:** Foundational · **Reading time:** ~8 min

## TL;DR

Every element is a nested set of rectangles — **content**, **padding**, **border**, **margin** — and `box-sizing` decides which of them `width` and `height` measure. The default, `content-box`, sizes the innermost rectangle, so adding padding or a border makes the element *bigger* than the number you wrote. `border-box` sizes out to the border edge, which is what almost everyone means, which is why a universal `box-sizing: border-box` reset is near-universal practice. Margins sit outside the box entirely, do not participate in `width`, and **collapse** between adjacent block-level siblings in normal flow — a rule that survives in flow layout and vanishes in flex and grid.

> **Recommendation:** Set `box-sizing: border-box` globally, size with logical properties (`inline-size`, `padding-inline`), and use `gap` rather than margins for spacing inside flex and grid containers.

## At a Glance

| | |
| --- | --- |
| **Use when** | Always — every layout decision resolves through this geometry. |
| **Avoid when** | Never; but prefer intrinsic sizing (`min-content`, `fit-content`) over fixed dimensions where you can. |
| **Alternatives** | None — this is the geometry itself. Layout *models* on top of it are covered by Formatting Contexts. |
| **Primary risk** | Mixed `box-sizing` across a codebase, producing off-by-a-border bugs that only appear at certain widths. |
| **Maturity** | Stable — the model is decades old; logical properties are the modern surface. |

## Prerequisites

You need to know which rule wins before you can reason about the geometry it produces.

- [Specificity](./specificity.md) — why a component's `padding` sometimes loses to a reset you forgot about.

## Overview

Four rectangles, from the inside out:

| Box | What it holds | Counted by `width` when… |
| --- | --- | --- |
| **Content box** | Text, replaced content, child boxes | Always |
| **Padding box** | Content + `padding` | `box-sizing: border-box` |
| **Border box** | Padding + `border-width` | `box-sizing: border-box` |
| **Margin box** | Border + `margin` | Never |

With the default `box-sizing: content-box`:

```css
.card { width: 300px; padding: 20px; border: 2px solid; }
/* Rendered border-box width: 300 + 20*2 + 2*2 = 344px */
```

With `border-box`:

```css
.card { box-sizing: border-box; width: 300px; padding: 20px; border: 2px solid; }
/* Rendered border-box width: 300px. Content box shrinks to 256px. */
```

The second is what people mean when they say "300 wide", and it composes: a `width: 50%` sibling pair with padding still totals 100%, which `content-box` cannot do without `calc()` gymnastics.

Margins behave differently from the other three. They are outside the box, they can be negative, they can be `auto` (which is how `margin-inline: auto` centers), and in **normal flow** adjacent vertical margins **collapse** to the larger of the two rather than summing. Collapsing happens between siblings, between a parent and its first or last child when nothing separates them, and through empty blocks. It does not happen in flex containers, grid containers, or across a border, padding, or `overflow` other than `visible`.

**Logical properties** re-express the model in writing-mode-relative terms: `inline-size`/`block-size` instead of `width`/`height`, `padding-inline`/`padding-block` instead of `padding-left`/`right`/`top`/`bottom`. In a right-to-left or vertical writing mode the physical mapping flips automatically, which is the difference between a layout that translates and one that must be re-authored.

## The Problem

The default box model makes composition arithmetic rather than declarative, and the workarounds accumulate.

```css
/* ❌ Two columns that should fill the row — and do not. */
.column {
  width: 50%;
  padding: 16px;
  border: 1px solid #ddd;
  float: left;
}
```

Each column's border-box width is `50% + 34px`, so the pair overflows by 68 pixels and the second column drops below the first. The historical fixes were all bad: remove the padding and add an inner wrapper element, switch to `calc(50% - 34px)` and update it every time the design changes, or apply the padding to a child instead — three ways to encode a magic number in a stylesheet.

The margin problem is subtler because the code looks correct:

```css
/* ❌ Expecting 32px of separation. */
.section { margin-bottom: 16px; }
.section + .section { margin-top: 16px; }
```

The two margins collapse to 16px, not 32. And the reverse surprise:

```css
/* ❌ Expecting the container to be pushed down by its child's margin. */
.container { background: #eee; }
.container > h2:first-child { margin-top: 24px; }
```

The child's top margin escapes the container and pushes the *container* down, leaving the grey background starting 24 pixels lower than intended — because nothing (no border, no padding, no `overflow` change) separates parent from child.

## Why It Matters

Box geometry is the substrate every other layout feature sits on, so an error here does not stay local — it propagates outward through every ancestor until something clips or overflows.

The practical costs are three. **Composition breaks:** a component authored with `content-box` cannot be dropped into a percentage-based grid without arithmetic, so component libraries either mandate a reset or ship with padding pushed onto inner wrapper elements, which doubles the DOM. **Responsive behavior degrades:** magic-number `calc()` widths are correct at exactly one padding value, so a design tweak silently produces horizontal overflow at some viewport width — usually the narrowest one, on the device least likely to be tested. **Internationalization stalls:** physical properties (`margin-left`, `padding-right`) must all be found and flipped to support a right-to-left locale, and any one missed produces a visibly broken layout.

Margin collapsing matters for a different reason: it is the one part of the model that behaves *inconsistently by design*, applying in flow layout and not in flex or grid. Spacing systems built on margins therefore change behavior when a container's `display` changes, which makes refactoring risky in a way `gap`-based spacing is not.

## Mental Model

Read the box from the inside out, and remember which edge each property moves.

```text
   ┌─────────── margin box (transparent, collapses, can be negative) ─┐
   │                                                                  │
   │   ┌──────── border box  ◄── box-sizing: border-box sizes here ─┐ │
   │   │                                                            │ │
   │   │   ┌──── padding box ────────────────────────────────────┐  │ │
   │   │   │                                                     │  │ │
   │   │   │   ┌ content box ◄── box-sizing: content-box sizes ┐ │  │ │
   │   │   │   │            here (the CSS default)             │ │  │ │
   │   │   │   └───────────────────────────────────────────────┘ │  │ │
   │   │   └─────────────────────────────────────────────────────┘  │ │
   │   └────────────────────────────────────────────────────────────┘ │
   └──────────────────────────────────────────────────────────────────┘
```

Three rules to keep in hand:

1. **`box-sizing` chooses which edge `width` names.** Nothing else changes.
2. **Margins are not part of any size you can set.** `width` never includes them; `outline` and `box-shadow` are likewise outside the geometry and never affect layout.
3. **Collapsing is a flow-layout rule.** Flex items, grid items, floats, absolutely positioned boxes, and anything establishing a new block formatting context do not collapse margins.

## Best Practices

- **Reset `box-sizing` globally** with the inheritable pattern, so a component can opt out locally without a `!important` fight.
- **Prefer logical properties** — `inline-size`, `padding-block`, `margin-inline` — from the start. Retrofitting them is a full-stylesheet audit.
- **Use `gap` for spacing between siblings** in flex and grid. It never collapses, never leaks out of the container, and needs no `:last-child` exception.
- **Prefer intrinsic sizing keywords** (`min-content`, `max-content`, `fit-content`) and `min()`/`max()`/`clamp()` over fixed pixel widths.
- **Reach for `min-inline-size: 0`** when a flex item refuses to shrink — flex items default to `min-width: auto`, which is a sizing rule people blame on the box model.
- **Never encode padding into a `calc()` width.** If you are writing `calc(50% - 32px)`, `border-box` was the answer.
- **Check the computed box in DevTools**, not the declared one. The box model panel shows the four rectangles as rendered.

## Trade-offs

`border-box` and `gap`-based spacing trade a small amount of flexibility for predictable composition.

**Advantages**

- Percentage widths compose with padding and borders without arithmetic.
- Component styles survive being dropped into unfamiliar containers.
- `gap` removes the entire class of collapsing and last-child bugs.
- Logical properties make right-to-left support a configuration change rather than a rewrite.

**Disadvantages**

- `border-box` makes the *content* width implicit, which occasionally matters for text measurement and intrinsic sizing.
- A global reset can surprise third-party widgets that assume `content-box`.
- Logical properties are less familiar in review, and some tooling still reasons in physical terms.
- `gap` requires a flex or grid container, so it does not apply to plain flow content.

| Dimension | This approach | Cost / caveat |
| --- | --- | --- |
| Performance | Identical — geometry cost is unchanged | None |
| Complexity | Removes `calc()` arithmetic from sizing | One more reset rule to understand |
| Maintainability | Padding changes stop breaking layouts | Mixed models in one codebase is worse than either alone |
| Failure behavior | Overflow becomes rare and obvious | Third-party CSS may fight the global reset |

## Alternative Approaches

There is no substitute for the box model itself. The real choice is how you *express* size and spacing within it.

| Approach | Best when | Weakness | See |
| --- | --- | --- | --- |
| `border-box` + logical properties | Default for all new work | Content width becomes implicit | (this article) |
| `content-box` + `calc()` | Interoperating with legacy CSS you cannot change | Magic numbers; breaks on design changes | — |
| Intrinsic sizing (`fit-content`, `min-content`) | Content-driven components | Harder to reason about in a rigid grid | [Formatting Contexts](./) (planned) |
| `gap` in flex/grid | Spacing between siblings | Requires a flex or grid container | [Flexbox](./) (planned) |
| Margins for spacing | Flow content, prose | Collapsing rules; last-child exceptions | — |

The practical rule: **`border-box` everywhere, `gap` inside layout containers, margins only in prose flow.**

## Bad Example

A card grid written against the default box model, with margin-based spacing.

```css
/* ❌ No box-sizing reset; every component compensates individually. */
.grid { width: 100%; }

.card {
  width: 33.333%;
  float: left;
  padding: 20px;
  border: 1px solid #ddd;
  margin-right: 16px;          /* ❌ physical property; breaks in RTL */
  margin-bottom: 24px;
}

.card:last-child { margin-right: 0; }   /* ❌ exception rule, wrong on every row but the last */

.card__title {
  margin-top: 16px;            /* ❌ collapses out of the card, moving the card itself */
  font-size: 1.25rem;
}

.card--wide {
  width: calc(66.666% - 42px); /* ❌ magic number = 20*2 + 1*2 = 42, encoded by hand */
}

.card__body {
  height: 120px;               /* ❌ fixed height; content-box, so padding overflows it */
  padding: 12px;
  overflow: hidden;            /* ❌ hides the symptom rather than fixing the cause */
}
```

**What goes wrong:** each `.card` renders at `33.333% + 42px`, so three per row overflow the container and wrap to two — the classic "why is my third column on the next line" bug, visible only once padding was added. The `margin-right` exception targets `:last-child`, which is the last card overall rather than the last of each row, so every row but the final one is misaligned. `.card__title`'s top margin collapses through the card's top edge — the card has padding, so in fact it does *not* collapse here, which is worse: the rule works or breaks depending on whether a padding value elsewhere is zero, making it fragile in a way that is invisible in review. `.card--wide` hard-codes 42 pixels derived from the padding and border, so the day a designer changes padding to 24px the layout silently overflows. And `.card__body`'s fixed `height` measures the content box, so 24 pixels of padding push the rendered height to 144px and `overflow: hidden` quietly clips real content.

## Good Example

The same grid with a global reset, logical properties, `gap`, and intrinsic sizing.

```css
/* ✅ Inheritable reset — components can opt out locally without !important. */
html { box-sizing: border-box; }
*, *::before, *::after { box-sizing: inherit; }

/* ✅ Spacing is the container's job, not each child's. */
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(16rem, 1fr));
  gap: 1.5rem 1rem;            /* block gap, inline gap — no collapsing, no exceptions */
}

.card {
  padding: 1.25rem;
  border: 1px solid var(--color-border);
  border-radius: 0.5rem;
  /* No width: the grid track sizes it. No margins: gap handles separation. */

  display: flex;
  flex-direction: column;
  gap: 0.75rem;                /* replaces every child margin inside the card */
}

.card--wide {
  grid-column: span 2;          /* ✅ expressed in tracks, not arithmetic */
}

.card__title {
  font-size: 1.25rem;
  margin-block: 0;              /* ✅ logical, and zero because gap owns the spacing */
}

.card__body {
  min-block-size: 7.5rem;       /* ✅ minimum, not fixed — content can grow */
  /* border-box means padding is inside this measurement */
}
```

```css
/* ✅ Logical properties throughout, so RTL is a document attribute, not a rewrite. */
.card__actions {
  display: flex;
  gap: 0.5rem;
  margin-block-start: auto;     /* pins actions to the bottom of the flex column */
  padding-inline-start: 0;
}

.card__badge {
  /* Physical would be margin-left; logical flips automatically under dir="rtl". */
  margin-inline-start: 0.5rem;
  padding-inline: 0.5rem;
  padding-block: 0.125rem;
}

/* ✅ Escape hatch: the one place content-box is genuinely wanted. */
.measure-ruler {
  box-sizing: content-box;      /* measuring text width; padding must not count */
  inline-size: 60ch;
}
```

```css
/* ✅ Fluid sizing without media queries or magic numbers. */
.container {
  inline-size: min(100% - 2rem, 72rem);   /* full width minus gutters, capped */
  margin-inline: auto;                     /* the modern centering idiom */
}

.card__thumbnail {
  inline-size: 100%;
  aspect-ratio: 16 / 9;                    /* no height arithmetic at all */
  object-fit: cover;
}
```

**Why it's better:** the inheritable reset makes `border-box` universal while leaving `.measure-ruler` a clean local opt-out — the one case where measuring the content box is actually correct. The grid owns spacing through `gap`, which never collapses and needs no `:last-child` exception, so rows align regardless of how many cards there are. Nothing hard-codes a width: `minmax(16rem, 1fr)` sizes tracks intrinsically, and `.card--wide` spans tracks rather than deriving a percentage minus a padding sum, so changing the card padding cannot break the grid. `min-block-size` replaces the fixed height, so content that runs long expands instead of being clipped, and `aspect-ratio` removes height arithmetic from the thumbnail entirely. Every directional property is logical, so `dir="rtl"` on the document flips the layout without touching the stylesheet.

## Common Mistakes

See the [CSS anti-patterns](../../../anti-patterns/) for the domain catalog. Concept-specific:

### Mistake: Encoding padding and borders into a `calc()` width

- **Symptom:** Widths like `calc(50% - 34px)` that break the moment a designer adjusts spacing.
- **Why it fails:** The arithmetic hard-codes values that live in another declaration, so the two drift apart silently. Nothing in the tooling links them.
- **Fix:** `box-sizing: border-box`, and let the percentage mean the rendered width.

### Mistake: Spacing siblings with margins inside a flex or grid container

- **Symptom:** `:last-child { margin-right: 0 }` exceptions, and spacing that changes when a container's `display` changes.
- **Why it fails:** Margins do not collapse in flex or grid, so they double at boundaries and require exception rules; and the same stylesheet behaves differently if the container reverts to flow layout.
- **Fix:** Use `gap`, which is defined per container and applies only between items.

### Mistake: Setting a fixed `height` on a padded box

- **Symptom:** Content clipped by a few pixels, or an unexpected scrollbar inside a component.
- **Why it fails:** Under `content-box`, `height` excludes padding, so the rendered box is taller than declared; under `border-box`, the content area shrinks and long content overflows.
- **Fix:** Use `min-block-size` so the box can grow, or `aspect-ratio` when the shape matters more than the number.

### Mistake: Using physical properties in a product that will be localized

- **Symptom:** A right-to-left locale renders with icons, padding, and alignment mirrored incorrectly.
- **Why it fails:** `margin-left`, `padding-right`, `text-align: left` are absolute directions that do not follow the writing mode.
- **Fix:** Author with logical properties from the start; `margin-inline-start`, `padding-inline`, `text-align: start`.

## Checklist

- [ ] A global `box-sizing: border-box` reset is in place, using the inheritable pattern.
- [ ] No sizing declaration subtracts padding or border values by hand in `calc()`.
- [ ] Spacing between siblings uses `gap` wherever a flex or grid container exists.
- [ ] No `:last-child` margin exceptions remain.
- [ ] Fixed `height` is replaced by `min-block-size`, `aspect-ratio`, or intrinsic sizing where content can vary.
- [ ] Directional properties are logical (`inline`/`block`), not physical (`left`/`right`).
- [ ] Layouts have been checked with `dir="rtl"` on the document element.
- [ ] Flex items that must shrink have `min-inline-size: 0` where the `auto` minimum blocks them.
- [ ] The rendered box was verified in the DevTools box model panel, not inferred from the declaration.

## Related Articles

- [Specificity](./specificity.md) — which declaration wins when a reset and a component disagree.
- [Inheritance & Initial Values](./inheritance-and-initial-values.md) — why the `box-sizing: inherit` reset pattern works.
- [Custom Properties](./custom-properties.md) — expressing spacing scales as tokens rather than literals.
- [Formatting Contexts](./) (planned) — what happens *between* boxes once their geometry is settled.
- [Stacking Contexts & z-index](./) (planned) — the other geometry that composes unexpectedly.
- **Canonical home:** layout-driven reflow cost is owned by [The Critical Rendering Path · Performance Engineering](../../05-reliability-quality/performance/the-critical-rendering-path.md).

## References

- [CSS Box Model Module Level 3](https://www.w3.org/TR/css-box-3/) — normative definitions of the four boxes and margin collapsing.
- [CSS Box Sizing Module Level 3](https://www.w3.org/TR/css-sizing-3/) — `box-sizing`, intrinsic sizing keywords, and the `auto` minimum size rule.
- [MDN — The box model](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model) — worked examples of both sizing modes.
- [MDN — CSS logical properties and values](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_logical_properties_and_values) — the full physical-to-logical mapping.

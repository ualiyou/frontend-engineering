---
title: "Role, Name, State"
slug: role-name-state
description: "The three facts assistive technology needs from every interactive element, where each comes from, and how to verify them instead of guessing."
keywords: ["role name state", "accessibility tree", "ARIA role", "accessible name", "aria-expanded", "aria-pressed", "WCAG 4.1.2", "screen reader", "accessible state", "semantic HTML"]
part: "04 · Interface Engineering"
domain: "Accessibility"
subcategory: "The Accessibility Tree"
difficulty: "Intermediate"
reading_time_min: 12
priority: "High"
status: "Published"
canonical: true
last_reviewed: "2026-08-09"
prerequisites:
  - "WCAG Principles (POUR)"
related:
  - "The Tree & Assistive Tech"
  - "Screen Reader Behavior"
next:
  - "The Tree & Assistive Tech"
  - "Screen Reader Behavior"
  - "Keyboard Navigation"
  - "Focus Management"
  - "Focus Order & Tab Trapping"
alternatives: []
common_mistakes:
  - "anti-patterns/README.md#accessibility"
  - "#common-mistakes"
frameworks: []
references:
  - { title: "WCAG 2.2 — 4.1.2 Name, Role, Value", url: "https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html" }
  - { title: "W3C — Accessible Name and Description Computation 1.2", url: "https://www.w3.org/TR/accname-1.2/" }
  - { title: "W3C — ARIA Authoring Practices Guide", url: "https://www.w3.org/WAI/ARIA/apg/" }
  - { title: "W3C — ARIA in HTML", url: "https://www.w3.org/TR/html-aria/" }
---

# Role, Name, State

> Assistive technology does not see your component. It sees three facts about it — what it is, what it is called, and what condition it is in — and everything else is invisible.

**Part:** [04 · Interface Engineering](../) · **Domain:** Accessibility · **Priority:** High · **Difficulty:** Intermediate · **Reading time:** ~12 min

## TL;DR

Every interactive element must expose a **role** (what kind of thing it is), an **accessible name** (what to call it), and its **state** (pressed, expanded, checked, disabled, selected, invalid). This is the substance of WCAG 4.1.2, and native HTML supplies all three for free — `<button>` is `role=button`, its text content is the name, `disabled` is the state. Problems begin when a `<div>` takes over the job: the role must be declared, the name must be constructed, the state must be maintained in ARIA attributes, and keyboard behavior must be reimplemented. The reliable check is not reading the markup but reading the **accessibility tree**, which is what assistive technology actually consumes.

> **Recommendation:** Use the native element whose role you want. When you cannot, supply role, name, state, *and* keyboard behavior together — three out of four is a control that announces correctly and cannot be operated.

## At a Glance

| | |
| --- | --- |
| **Use when** | Building or reviewing any interactive control, custom or native. |
| **Avoid when** | Never — but avoid *adding ARIA* to elements whose native semantics already say the right thing. |
| **Alternatives** | Native HTML elements, which provide all three implicitly. |
| **Primary risk** | State declared once and never updated, so the announced condition diverges from the visual one. |
| **Maturity** | Stable — ARIA 1.2 and AccName 1.2 are settled; support differences persist between screen readers. |

## Prerequisites

The success criteria come first; this article is the mechanics of satisfying one of them.

- [WCAG Principles (POUR)](./wcag-principles-pour.md) — where 4.1.2 sits under Robust, and what conformance requires.

## Overview

Three facts, three sources.

| Fact | Question it answers | Native source | ARIA override |
| --- | --- | --- | --- |
| **Role** | What kind of control is this? | The element itself (`<button>`, `<a href>`, `<input type=checkbox>`) | `role="…"` |
| **Name** | What is it called? | Content, `<label>`, `alt`, `title` | `aria-label`, `aria-labelledby` |
| **State** | What condition is it in now? | `disabled`, `checked`, `open`, `required` | `aria-pressed`, `aria-expanded`, `aria-checked`, `aria-disabled`, `aria-selected`, `aria-invalid` |

A fourth fact — **value** — applies to controls that hold one: `aria-valuenow` on a slider, the text content of a text field. WCAG names the criterion "Name, Role, Value" for that reason.

**Name computation** follows a defined precedence, and knowing the order prevents most surprises:

1. `aria-labelledby` (concatenating the referenced elements' text)
2. `aria-label`
3. Native labelling — `<label for>`, `alt`, `<caption>`, `<legend>`, `<figcaption>`
4. Element content
5. `title` (last resort; not announced by every screen reader in every context)

`aria-label` *replaces* visible content, which is why an icon-plus-text button labelled `aria-label="Save"` announces "Save" even though it reads "Save changes" on screen — and why voice-control users saying "click Save changes" fail to activate it. The rule that follows is **the accessible name must contain the visible label** (WCAG 2.5.3, Label in Name).

**State** must be maintained, not merely declared. `aria-expanded="false"` written once in a template and never updated is worse than nothing: it asserts a condition that becomes false the moment the user opens the panel.

Finally, `role` changes only what is *announced*, never what the element *does*. `<div role="button">` does not become focusable, does not respond to Enter or Space, and does not fire on keyboard activation. Those are three separate additions.

## The Problem

The typical custom control gets one fact right and silently omits the others.

```html
<!-- ❌ Looks like a button; is a div. -->
<div class="btn" onclick="save()">
  <svg aria-hidden="true"><use href="#icon-save" /></svg>
</div>
```

The accessibility tree sees a generic container with no name and no role. A screen reader user tabbing through the page never reaches it, because a `<div>` is not focusable. A user who somehow lands on it hears nothing useful. The icon is `aria-hidden`, correctly — but nothing replaced the name it hid.

Half-fixing it is common:

```html
<!-- ❌ Role and name, no keyboard, no state. -->
<div role="button" aria-label="Save" class="btn" onclick="save()">
  <svg aria-hidden="true"><use href="#icon-save" /></svg>
</div>
```

Now it announces correctly and still cannot be operated: no `tabindex`, so it is unreachable by keyboard, and no Enter/Space handler, so it would do nothing if it were.

The state failure is the most common of all:

```html
<!-- ❌ aria-expanded is static; the panel toggles. -->
<button aria-expanded="false" onclick="panel.hidden = !panel.hidden">
  Filters
</button>
<div id="panel" hidden>…</div>
```

Everything is right on first render. After the first click, the panel is open and the button still announces "collapsed" — for the rest of the session. This is worse than omitting the attribute, because the user is now being told something false rather than nothing.

## Why It Matters

For a screen reader, keyboard, or voice-control user, these three facts *are* the interface. A control with no role is skipped; a control with no name is announced as "button" with no indication of what it does; a control with wrong state gives the user an incorrect model of the page they are operating.

The consequences compound in ordinary flows. A toggle whose `aria-pressed` never changes gives no feedback that the action succeeded, so the user presses it again — and turns the setting back off. A disclosure whose `aria-expanded` is stale means the user cannot tell whether content appeared, so they search the page for it. A form field whose invalid state is conveyed only by a red border is, to a screen reader user, a form that submitted and did nothing.

There is also a legal and organizational dimension: 4.1.2 is a Level A criterion, which means it is in scope for essentially every accessibility requirement anywhere — EN 301 549, Section 508, the European Accessibility Act. Failures here are among the most commonly cited in audits precisely because custom controls are so common.

And there is a cheaper argument. Native elements supply all three facts, plus keyboard behavior, plus focus management, plus forced-colors support, for zero lines of code. Most of this work exists because someone chose a `<div>`.

## Mental Model

Read every control as a sentence the screen reader will speak.

```text
   <button aria-pressed="true">Bold</button>
      │              │           │
      │              │           └── NAME   → "Bold"
      │              └────────────── STATE  → "pressed"
      └───────────────────────────── ROLE   → "toggle button"

   Announced: "Bold, toggle button, pressed"

   A custom control needs FOUR things, not three:
     role      → what it is          (role="button")
     name      → what it is called   (content or aria-label)
     state     → its condition       (aria-pressed, kept in sync)
     behavior  → focusable + keyboard handlers  ← the one people forget
```

Two habits catch nearly everything:

1. **Say the sentence aloud** when you write the markup. If it does not describe the control, something is missing.
2. **Read the accessibility tree, not the DOM.** DevTools shows the computed role, name, and state; that is the ground truth, and it frequently differs from what the markup suggests.

## Best Practices

- **Use the native element.** `<button>`, `<a href>`, `<input>`, `<select>`, `<details>`, `<dialog>` bring role, name, state, keyboard, and focus behavior together and cannot fall out of sync.
- **Prefer content over `aria-label`.** A visible text label is the accessible name automatically, is translated by the page's own localization, and satisfies Label in Name for voice control.
- **When you must use `aria-label`, include the visible text** — `aria-label="Save changes"` for a button reading "Save changes", not `aria-label="Save"`.
- **Derive state from the same source as the visuals.** One variable drives both the class and the ARIA attribute; two variables will diverge.
- **Hide decorative graphics** with `aria-hidden="true"`, and give the *control* the name — never leave an icon-only button unnamed.
- **Pair every custom role with its keyboard contract** from the ARIA Authoring Practices Guide: `role="button"` needs `tabindex="0"`, Enter, and Space; `role="tab"` needs arrow-key navigation and roving tabindex.
- **Prefer `disabled` to `aria-disabled`** unless the control must stay focusable so a user can discover why it is unavailable.
- **Verify with the accessibility tree and one real screen reader.** Automated checks catch missing names; they cannot catch a name that is wrong or a state that never updates.

## Trade-offs

Native semantics are cheaper and less flexible; ARIA is more flexible and entirely your responsibility.

**Advantages of native elements**

- Role, name, state, keyboard, and focus behavior arrive together and stay consistent.
- Forced-colors mode, high-contrast themes, and platform conventions work without extra CSS.
- Impossible to forget an update, because the browser maintains the state.

**Disadvantages / costs of ARIA-built controls**

- Every attribute is a manual synchronization point with the visual state.
- Keyboard interaction must be implemented, tested, and maintained per pattern.
- Screen reader support for less common roles varies, so behavior differs across combinations.
- Incorrect ARIA overrides correct native semantics, making things worse than no ARIA at all.

| Dimension | This approach | Cost / caveat |
| --- | --- | --- |
| Performance | Negligible either way | Live regions and frequent state changes can be chatty |
| Complexity | Native: near zero | Custom: role + name + state + keyboard, per pattern |
| Maintainability | Native cannot desynchronize | ARIA state must be re-checked on every refactor |
| Failure behavior | Native degrades gracefully | Wrong ARIA is actively misleading, not merely absent |

## Alternative Approaches

The question is always *how* the three facts get exposed, not *whether*.

| Approach | Best when | Weakness | See |
| --- | --- | --- | --- |
| Native HTML element | Always, if a matching element exists | Limited styling on a few controls (`<select>`, `<progress>`) | (this article) |
| Native element, restyled | The default look is the only obstacle | Some controls resist styling; test forced-colors mode | [The ARIA Model](./the-aria-model.md) |
| Native + minimal ARIA | The pattern has no native equivalent state (`aria-expanded` on a button) | One more attribute to keep in sync | `The ARIA Model · Accessibility` |
| Full ARIA pattern | No native element exists (tabs, combobox, treegrid) | Whole keyboard contract is yours | `The Tree & Assistive Tech · Accessibility` |
| A headless component library | The team lacks time to implement APG patterns correctly | Dependency; still needs naming and testing | `Component Design · Component & Interaction Design` |

The practical rule: **native element first; ARIA only to add what the platform has no way to express.**

## Bad Example

A filter panel with a toggle, a disclosure, and a tab set, all built from `<div>`s.

```tsx
// ❌ Four controls, ten accessibility defects.
function FilterPanel({ filters, activeTab }: Props) {
  const [isOpen, setOpen] = useState(false);
  const [starred, setStarred] = useState(false);

  return (
    <section>
      {/* ❌ No role, not focusable, no keyboard, aria-expanded never updated */}
      <div className="disclosure" aria-expanded="false" onClick={() => setOpen(!isOpen)}>
        <svg aria-hidden="true"><use href="#chevron" /></svg>
        Filters
      </div>

      {isOpen && (
        <div>
          {/* ❌ Icon-only, no name at all, and pressed state conveyed only by a class */}
          <div
            className={starred ? "toggle toggle--on" : "toggle"}
            onClick={() => setStarred(!starred)}
          >
            <svg aria-hidden="true"><use href="#star" /></svg>
          </div>

          {/* ❌ role without keyboard support or roving tabindex */}
          <div role="tablist">
            {["Open", "Closed"].map((tab) => (
              <div key={tab} role="tab" onClick={() => selectTab(tab)}>
                {tab}
              </div>
            ))}
          </div>

          {/* ❌ aria-label replaces the visible text with something different */}
          <button aria-label="Apply" onClick={apply}>
            Apply filters
          </button>

          {/* ❌ Error shown visually only; the input never reports invalid */}
          <label htmlFor="min">Minimum</label>
          <input id="min" value={filters.min} onChange={onMin} />
          {filters.minError && <span className="error">{filters.minError}</span>}
        </div>
      )}
    </section>
  );
}
```

**What goes wrong:** the disclosure is a `<div>` with no `role` and no `tabindex`, so keyboard users never reach it, and its hard-coded `aria-expanded="false"` becomes a lie the instant it is clicked with a mouse. The star toggle has no name, no role, and no `aria-pressed` — a screen reader user hears nothing, and even a sighted mouse user gets no confirmation announced. The tablist declares roles but implements none of the tab keyboard contract: no arrow-key movement, no roving `tabindex`, no `aria-selected`, and no `aria-controls`, so the pattern announces as tabs and behaves as unreachable text. The Apply button's `aria-label="Apply"` shadows its visible "Apply filters", which breaks voice control — saying "click Apply filters" does not match the accessible name. And the invalid field carries no `aria-invalid` and no `aria-describedby`, so the error text is visually adjacent and programmatically unrelated; a screen reader user submits, hears nothing, and has no way to know which field failed.

## Good Example

The same panel built from native elements, with state derived from one source and the full keyboard contract where ARIA was unavoidable.

```tsx
// ✅ Native <button> everywhere a button is meant; state derived from one variable.
function FilterPanel({ filters, onApply }: Props) {
  const [isOpen, setOpen] = useState(false);
  const [starred, setStarred] = useState(false);
  const panelId = useId();

  return (
    <section aria-labelledby={`${panelId}-heading`}>
      <h2 id={`${panelId}-heading`}>Filters</h2>

      {/* ✅ Role, name, state, and keyboard all come from <button>; state is derived. */}
      <button
        type="button"
        aria-expanded={isOpen}              // ✅ same variable as the render below
        aria-controls={`${panelId}-body`}
        onClick={() => setOpen((open) => !open)}
      >
        <svg aria-hidden="true" focusable="false"><use href="#chevron" /></svg>
        {isOpen ? "Hide filters" : "Show filters"}
      </button>

      <div id={`${panelId}-body`} hidden={!isOpen}>
        {/* ✅ Icon-only, so the name is explicit — and it describes the control, not the icon. */}
        <button
          type="button"
          aria-pressed={starred}
          aria-label="Only starred items"
          onClick={() => setStarred((on) => !on)}
        >
          <svg aria-hidden="true" focusable="false"><use href="#star" /></svg>
        </button>

        <MinimumField value={filters.min} error={filters.minError} />

        {/* ✅ Visible text is the accessible name — Label in Name satisfied for voice control. */}
        <button type="button" onClick={onApply}>Apply filters</button>
      </div>
    </section>
  );
}
```

```tsx
// ✅ Invalid state is programmatic, not just visual, and the message is associated.
function MinimumField({ value, error, onChange }: FieldProps) {
  const id = useId();
  const errorId = `${id}-error`;

  return (
    <div>
      <label htmlFor={id}>Minimum</label>
      <input
        id={id}
        type="number"
        inputMode="numeric"
        value={value}
        onChange={onChange}
        aria-invalid={error ? true : undefined}       // ✅ omitted, not "false", when valid
        aria-describedby={error ? errorId : undefined}
      />
      {error && (
        <p id={errorId} className="error">
          {error}
        </p>
      )}
    </div>
  );
}
```

```tsx
// ✅ Tabs have no native element, so the full APG contract is implemented explicitly.
function Tabs({ tabs, selected, onSelect }: TabsProps) {
  const baseId = useId();
  const refs = useRef<(HTMLButtonElement | null)[]>([]);

  function onKeyDown(event: React.KeyboardEvent, index: number) {
    const last = tabs.length - 1;
    const next = {
      ArrowRight: index === last ? 0 : index + 1,
      ArrowLeft: index === 0 ? last : index - 1,
      Home: 0,
      End: last,
    }[event.key];

    if (next === undefined) return;
    event.preventDefault();
    onSelect(tabs[next].id);
    refs.current[next]?.focus();                    // ✅ selection follows focus, APG default
  }

  return (
    <>
      <div role="tablist" aria-label="Filter status">
        {tabs.map((tab, i) => {
          const isSelected = tab.id === selected;
          return (
            <button
              key={tab.id}
              ref={(el) => { refs.current[i] = el; }}
              type="button"
              role="tab"
              id={`${baseId}-tab-${tab.id}`}
              aria-selected={isSelected}              // ✅ state, derived from `selected`
              aria-controls={`${baseId}-panel-${tab.id}`}
              tabIndex={isSelected ? 0 : -1}          // ✅ roving tabindex: one stop for the set
              onClick={() => onSelect(tab.id)}
              onKeyDown={(e) => onKeyDown(e, i)}
            >
              {tab.label}
            </button>
          );
        })}
      </div>

      {tabs.map((tab) => (
        <div
          key={tab.id}
          role="tabpanel"
          id={`${baseId}-panel-${tab.id}`}
          aria-labelledby={`${baseId}-tab-${tab.id}`}
          hidden={tab.id !== selected}
          tabIndex={0}                                // ✅ panel is reachable for scrolling
        >
          {tab.content}
        </div>
      ))}
    </>
  );
}
```

**Why it's better:** the disclosure and the toggle are `<button>` elements, so role, focusability, Enter/Space activation, and forced-colors rendering all arrive for free, and `aria-expanded={isOpen}` reads the same variable that decides whether the panel renders — the two cannot drift apart. The star toggle carries `aria-pressed`, so the state change is announced rather than merely coloured, and its `aria-label` names the *control's purpose* rather than the icon. The Apply button uses visible text as its name, so voice control works and Label in Name is satisfied with no attribute at all. `MinimumField` sets `aria-invalid` and points `aria-describedby` at the error, so the message is announced with the field instead of floating unattached — and `aria-invalid` is omitted rather than set to `"false"` when valid, avoiding a redundant announcement. Tabs, which have no native element, implement the whole APG contract: arrow, Home, and End navigation, a roving `tabindex` so the set is one tab stop, `aria-selected` derived from the same `selected` value that hides the panels, and `aria-controls`/`aria-labelledby` linking each tab to its panel in both directions.

## Common Mistakes

See the [Accessibility anti-patterns](../../../anti-patterns/) for the domain catalog. Concept-specific:

### Mistake: State declared once and never updated

- **Symptom:** `aria-expanded="false"` or `aria-pressed="false"` in the template, unchanged after interaction.
- **Why it fails:** The attribute asserts a condition that the code no longer maintains, so assistive technology reports the opposite of what is on screen — worse than reporting nothing.
- **Fix:** Bind the attribute to the same variable that drives the visual state, so a single source of truth updates both.

### Mistake: `role` without behavior

- **Symptom:** `<div role="button">` that keyboard users cannot reach or activate.
- **Why it fails:** `role` changes only what is announced. Focusability, Enter/Space activation, and disabled semantics are separate additions the browser supplies for `<button>` and for nothing else.
- **Fix:** Use `<button>`. If a custom role is unavoidable, add `tabindex="0"` and the keyboard handlers the ARIA Authoring Practices Guide specifies for that role.

### Mistake: `aria-label` that does not contain the visible text

- **Symptom:** Voice control users say the visible label and nothing happens; screen reader users hear a different word than sighted users read.
- **Why it fails:** `aria-label` replaces the computed name entirely, so voice-control matching against the visible string fails. This is a WCAG 2.5.3 (Label in Name) failure.
- **Fix:** Prefer visible content as the name. When a label is required, include the visible text verbatim within it.

### Mistake: Icon-only controls with no name

- **Symptom:** A screen reader announces "button" with no further information.
- **Why it fails:** `aria-hidden="true"` on the icon — which is correct — leaves the control with no content to compute a name from.
- **Fix:** Give the *control* an `aria-label` or visually hidden text describing its action, never the icon.

### Mistake: Conveying validity or selection only visually

- **Symptom:** A red border or a highlighted row, with nothing in the accessibility tree.
- **Why it fails:** Colour and position are not exposed to assistive technology, so the state does not exist for anyone not looking at the screen.
- **Fix:** `aria-invalid` plus `aria-describedby` for errors; `aria-selected`, `aria-current`, or `aria-checked` for selection, always derived from the same state that drives the styling.

### Mistake: Adding ARIA to elements that already have the right semantics

- **Symptom:** `<button role="button">`, `<nav role="navigation">`, `<input type="checkbox" role="checkbox">`.
- **Why it fails:** It is redundant at best, and at worst a typo overrides correct native semantics with an incorrect role, which no automated tool will flag.
- **Fix:** Follow the first rule of ARIA — do not use ARIA where native HTML already says the same thing.

## Checklist

- [ ] Every interactive element is a native control unless no native equivalent exists.
- [ ] Every control has a non-empty accessible name, verified in the accessibility tree rather than inferred from markup.
- [ ] Icon-only controls carry a label describing the action, and the icon itself is `aria-hidden`.
- [ ] Every `aria-label` contains the visible text verbatim.
- [ ] Every state attribute is bound to the same variable that drives the visual state.
- [ ] `aria-expanded`, `aria-pressed`, `aria-selected`, and `aria-checked` change on interaction — verified by interacting, not by reading code.
- [ ] Every custom role implements the keyboard contract from the ARIA Authoring Practices Guide.
- [ ] Composite widgets use a roving `tabindex` so the set is a single tab stop.
- [ ] Invalid fields set `aria-invalid` and associate the message with `aria-describedby`.
- [ ] No redundant ARIA duplicates native semantics.
- [ ] The component has been operated with a keyboard only, and heard in at least one real screen reader.

## Related Articles

- [The ARIA Model](./the-aria-model.md) — how roles, states, and properties compose, and the rules for applying them.
- [Accessible Name Computation](./accessible-name-computation.md) — the full precedence order and its edge cases.
- [WCAG Principles (POUR)](./wcag-principles-pour.md) — where 4.1.2 sits and what Level A requires.
- [Conformance Levels](./conformance-levels.md) — the A / AA / AAA distinction this criterion falls under.
- [The Tree & Assistive Tech](./) (planned) — how the browser builds the tree these facts are read from.
- **Canonical home:** semantic document structure is owned by [Sectioning & Landmarks · HTML & Document Semantics](../../01-core-languages/html-semantics/sectioning-and-landmarks.md).

## References

- [WCAG 2.2 — 4.1.2 Name, Role, Value](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html) — the normative criterion and its failure conditions.
- [W3C — Accessible Name and Description Computation 1.2](https://www.w3.org/TR/accname-1.2/) — the exact precedence used to compute a name.
- [W3C — ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) — keyboard contracts for every composite pattern.
- [W3C — ARIA in HTML](https://www.w3.org/TR/html-aria/) — which roles and attributes are permitted on which elements.

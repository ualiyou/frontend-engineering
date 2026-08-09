---
title: "Controlled Inputs"
slug: controlled-inputs
description: "When React owns an input's value, what that costs per keystroke, and how to keep the DOM as the source of truth without losing control of the form."
keywords: ["controlled inputs", "React forms", "uncontrolled inputs", "value and onChange", "form state", "input lag", "cursor jump", "defaultValue", "FormData", "composition events"]
part: "03 · Application Architecture"
domain: "Forms & Validation"
subcategory: "Form State"
difficulty: "Intermediate"
reading_time_min: 12
priority: "Critical"
status: "Published"
canonical: true
last_reviewed: "2026-08-09"
prerequisites:
  - "Elements vs Components · React"
  - "Structural Typing · TypeScript"
  - "Categories of State · State Management"
related:
  - "Uncontrolled Inputs & Refs"
  - "Form Libraries & State Models"
  - "Field Arrays & Dynamic Fields"
next:
  - "Uncontrolled Inputs & Refs"
  - "Form Libraries & State Models"
  - "Field Arrays & Dynamic Fields"
  - "Client-Side Validation Strategies"
  - "Schema Validation"
alternatives: []
common_mistakes:
  - "anti-patterns/README.md#forms-validation"
  - "#common-mistakes"
frameworks: ["react"]
references:
  - { title: "React — <input>", url: "https://react.dev/reference/react-dom/components/input" }
  - { title: "React — Controlled and uncontrolled components", url: "https://react.dev/learn/sharing-state-between-components#controlled-and-uncontrolled-components" }
  - { title: "MDN — FormData", url: "https://developer.mozilla.org/en-US/docs/Web/API/FormData" }
  - { title: "MDN — Constraint validation", url: "https://developer.mozilla.org/en-US/docs/Web/HTML/Constraint_validation" }
---

# Controlled Inputs

> A controlled input is a claim that your state is the truth and the DOM is a projection of it. Every bug in this area comes from the claim being false for one frame.

**Part:** [03 · Application Architecture](../) · **Domain:** Forms & Validation · **Priority:** Critical · **Difficulty:** Intermediate · **Reading time:** ~12 min

## TL;DR

A **controlled input** passes `value` and `onChange`, making React state the single source of truth: the DOM never holds a value React did not put there. That buys derived UI — live formatting, dependent fields, character counters, disabled submit buttons — and charges a re-render per keystroke plus the responsibility of never dropping a character. An **uncontrolled input** uses `defaultValue` and lets the DOM own the value, read at submit time with `FormData` or a ref, which is faster and simpler but cannot drive UI that must change as the user types. The right default is **uncontrolled for most fields, controlled for the few that feed something else on screen.**

> **Recommendation:** Start uncontrolled with `FormData` at submit. Promote a field to controlled only when something else on the page must react to it before submit.

## At a Glance

| | |
| --- | --- |
| **Use when** | A field's value drives other UI live — formatting, dependent options, counters, instant validation. |
| **Avoid when** | The value is only needed at submit; large forms where every keystroke would re-render a wide tree. |
| **Alternatives** | [Uncontrolled inputs](#alternative-approaches) with `FormData`, form libraries with subscriptions, hybrid per-field control. |
| **Primary risk** | Cursor jumps and dropped characters from transforming the value inside `onChange`. |
| **Maturity** | Stable — the pattern is as old as React; `FormData` and Actions have made uncontrolled more attractive again. |

## Prerequisites

Controlling an input is a state-ownership decision expressed through props.

- [Elements vs Components · React](../../02-rendering-frameworks/react/elements-vs-components.md) — what a prop change actually does to the DOM node.
- [Categories of State · State Management](../state-management/categories-of-state.md) — deciding whether form input is state you should own at all.
- [Structural Typing · TypeScript](../../01-core-languages/typescript/structural-typing.md) — typing field values and change handlers precisely.

## Overview

Three modes exist, and mixing them accidentally is the source of the warnings everyone has seen.

| Mode | Props | Source of truth |
| --- | --- | --- |
| **Controlled** | `value` + `onChange` | React state |
| **Uncontrolled** | `defaultValue` (optional) | The DOM node |
| **Broken** | `value` without `onChange` | Neither — the field is read-only and React warns |

When an input is controlled, React sets the DOM `value` property after every render. If your state did not change in response to a keystroke, React writes the old value back and the character disappears. That is the entire mechanism behind "my input won't accept typing".

The value is **always a string** for text inputs. Numbers, dates, and currencies arrive as strings and must be parsed at a boundary; storing a parsed number in state and rendering it back breaks intermediate states like `"1."` or `"-"`.

React also normalizes some DOM behavior worth knowing:

- `onChange` fires on every input event, not on blur — it is the DOM's `input` event, not the DOM's `change` event.
- Checkboxes and radios use `checked`, not `value`.
- `<select multiple>` takes an array; `<textarea>` takes `value` rather than children.
- A field that starts `undefined` and later receives a string switches from uncontrolled to controlled, producing a warning and, sometimes, a lost value.

Since React 19, `<form action={fn}>` receives a `FormData` object directly, which makes the uncontrolled path first-class rather than a fallback.

## The Problem

The naive controlled input works until the value needs shaping.

```tsx
// ❌ Formatting inside onChange moves the cursor to the end on every keystroke.
function PhoneField() {
  const [phone, setPhone] = useState("");

  return (
    <input
      value={phone}
      onChange={(e) => setPhone(formatPhone(e.target.value))}   // "(555) 12" 
    />
  );
}
```

Typing in the middle of an existing number inserts a character, the formatter rewrites the whole string, React sets `value`, and the browser places the caret at the end. The user's next keystroke lands in the wrong place. Editing an existing phone number becomes impossible.

The numeric variant loses characters instead:

```tsx
// ❌ Parsing to a number makes intermediate states unrepresentable.
const [price, setPrice] = useState(0);

<input value={price} onChange={(e) => setPrice(Number(e.target.value))} />
```

The user types `1`, then `.` — `Number("1.")` is `1`, React renders `"1"`, the decimal point vanishes. Typing `-` gives `NaN`, which renders as `"NaN"` in the field. Neither is recoverable by the user.

And the scale problem, which appears later:

```tsx
// ❌ One state object for 40 fields: every keystroke re-renders the entire form.
const [form, setForm] = useState(initialValues);

<input
  value={form.addressLine1}
  onChange={(e) => setForm({ ...form, addressLine1: e.target.value })}
/>
```

Each character allocates a new object, re-renders all forty fields, and re-runs any validation memoized on the whole object. On a mid-tier phone with a rich form this produces visible input lag — the keystroke appears tens of milliseconds after the key was pressed.

## Why It Matters

Text entry is the interaction users notice most. Rendering a list 20 ms late is invisible; a character appearing 80 ms late is felt immediately, and a cursor that jumps makes a field unusable rather than merely slow.

The correctness stakes are equally concrete. A controlled input that drops characters loses user data with no error — the classic case is IME composition, where typing Japanese, Korean, or Chinese produces intermediate composition text that a `value`-rewriting handler destroys mid-word. Users of those languages hit it on the first attempt; a test suite typing ASCII never will.

There is an architectural dimension too. Controlling a field is a decision to duplicate the DOM's state into React's, and duplication is the thing that has to be kept in sync. Choosing uncontrolled where possible reduces the number of values that can disagree — with the trade-off that you cannot read the value before submit without reaching for the DOM.

Finally, this decision determines what your form costs. Controlled fields with a single state object are `O(fields)` work per keystroke; per-field state or an uncontrolled form is `O(1)`. On large forms that is the difference between smooth typing and a support ticket.

## Mental Model

Ask who holds the value between keystrokes.

```text
  CONTROLLED                              UNCONTROLLED
  ──────────                              ────────────
  keypress                                keypress
     │                                       │
     ▼                                       ▼
  DOM input event                         DOM updates its own value
     │                                       │
     ▼                                       └──► (React knows nothing)
  onChange → setState
     │
     ▼
  re-render → React writes value back      submit
     │                                       │
     ▼                                       ▼
  DOM shows React's value                  new FormData(form) reads everything

  If setState is skipped or transforms the value,
  React writes back something else and the keystroke is lost or the caret moves.
```

Two rules follow:

1. **Never transform the value on the way into state.** Store what the user typed. Format for display on blur, or in a separate presentation layer.
2. **Control the narrowest thing that needs controlling.** One field, not the whole form; and only when something else on screen depends on it live.

## Best Practices

- **Default to uncontrolled.** `defaultValue` plus `new FormData(event.currentTarget)` at submit covers most forms with zero re-renders.
- **Store raw strings.** Parse at the boundary — on submit or on blur — not on every keystroke.
- **Keep state per field, not per form,** when you do control. `useState` per input, or a form library with per-field subscriptions, keeps the re-render scoped.
- **Format on blur, validate on blur, show errors after touch.** Typing is not the moment to tell someone their email is invalid.
- **Guard IME composition** with `onCompositionStart`/`onCompositionEnd` if you transform values at all.
- **Never leave `value` as `undefined`.** Use `value={x ?? ""}` so the field cannot flip from uncontrolled to controlled.
- **Use the platform's constraint validation** (`required`, `type="email"`, `pattern`, `min`) as the first layer; it is free, accessible, and works before JavaScript loads.
- **Debounce the consumer, not the input.** The field updates instantly; the expensive search it triggers is what gets debounced.

## Trade-offs

Control buys live derivation and pays in renders and in edge cases the DOM used to handle for you.

**Advantages**

- The value is available during render, so dependent UI is trivially correct.
- Programmatic changes — reset, prefill, sync from elsewhere — are ordinary state updates.
- Validation state and value stay consistent because they are computed together.
- Testing is straightforward: assert on state, not on DOM properties.

**Disadvantages**

- A re-render per keystroke, whose cost scales with how much the value's owner renders.
- Caret position, IME composition, and browser autofill all become your problem.
- Intermediate values (`"1."`, `"-"`, `"+44 "`) must be representable in state.
- Uncontrolled-to-controlled transitions produce warnings and lost values.

| Dimension | This approach | Cost / caveat |
| --- | --- | --- |
| Performance | Fine for a few fields | `O(fields)` per keystroke if state is one object |
| Complexity | Derived UI is simple | Caret and IME handling is not |
| Maintainability | One source of truth | Duplicates what the DOM already tracks |
| Failure behavior | Dropped keystrokes, jumping cursor | Silent; invisible to ASCII-only testing |

## Alternative Approaches

Every option below solves "how does the app learn the field's value".

| Approach | Best when | Weakness | See |
| --- | --- | --- | --- |
| Controlled per field | A few fields drive live UI | Re-render per keystroke | (this article) |
| [Uncontrolled + `FormData`](./) (planned) | Values needed only at submit | No live derivation | `Uncontrolled Inputs & Refs · Forms & Validation` |
| [Form library with subscriptions](./form-libraries-and-state-models.md) | Large forms, arrays, cross-field rules | A dependency and its mental model | `Form Libraries & State Models · Forms & Validation` |
| Server Actions with `FormData` | Progressive enhancement matters | Round-trip for feedback | `Client-Side Validation Strategies · Forms & Validation` |
| Native constraint validation | Simple required/format rules | Limited messaging control | [Error Messaging](./error-messaging.md) |

The practical rule: **uncontrolled by default, controlled per field where live derivation is required, a library once cross-field rules appear.**

## Bad Example

A checkout form where every field is controlled through one state object and values are transformed on input.

```tsx
// ❌ One object, forty fields, transformation in onChange.
function Checkout() {
  const [form, setForm] = useState({
    email: "", phone: "", cardNumber: "", amount: 0, country: undefined,
  });
  const [errors, setErrors] = useState({});

  // ❌ New object per keystroke → every field re-renders.
  const update = (field: string, value: unknown) =>
    setForm((prev) => ({ ...prev, [field]: value }));

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={form.email}
        onChange={(e) => {
          update("email", e.target.value);
          // ❌ Validating on every keystroke: "j" is not a valid email, so the
          // user is told they are wrong from the first character they type.
          setErrors((p) => ({ ...p, email: isEmail(e.target.value) ? null : "Invalid email" }));
        }}
      />
      {errors.email && <span>{errors.email}</span>}

      {/* ❌ Reformatting on input → caret jumps to the end mid-edit. */}
      <input
        value={form.phone}
        onChange={(e) => update("phone", formatPhone(e.target.value))}
      />

      {/* ❌ Parsing to a number → "1." and "-" are unrepresentable. */}
      <input
        value={form.amount}
        onChange={(e) => update("amount", Number(e.target.value))}
      />

      {/* ❌ value starts undefined → uncontrolled, then controlled. React warns. */}
      <select value={form.country} onChange={(e) => update("country", e.target.value)}>
        <option value="us">United States</option>
        <option value="de">Germany</option>
      </select>

      {/* ❌ Card number transformed with spaces on every keystroke. */}
      <input
        value={form.cardNumber}
        onChange={(e) => update("cardNumber", groupDigits(e.target.value))}
        autoComplete="cc-number"
      />
    </form>
  );
}
```

**What goes wrong:** every keystroke allocates a new form object and re-renders all forty fields plus their validation, which on a mid-tier phone is tens of milliseconds of work per character — felt as lag. The phone and card fields reformat the value inside `onChange`, so React writes a different string back to the DOM and the browser moves the caret to the end; editing the middle of an existing number is impossible, and an IME user's in-progress composition is destroyed on every keypress. The amount field parses to a number, so `"1."` renders as `"1"` and the decimal point cannot be typed, while `"-"` becomes `NaN` and renders as the literal text `NaN`. The `country` select starts as `undefined`, making it uncontrolled on first render and controlled on the second — React logs a warning and, in some browsers, the initial selection is lost. And validating email on every keystroke means the user sees "Invalid email" from the first character, which trains them to ignore the message entirely.

## Good Example

Uncontrolled by default, controlled only where live derivation is needed, with formatting on blur.

```tsx
// ✅ The form is uncontrolled; FormData reads it at submit.
export function Checkout({ onSubmit }: { onSubmit: (values: CheckoutValues) => void }) {
  const [errors, setErrors] = useState<Record<string, string>>({});

  function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const data = new FormData(event.currentTarget);

    // ✅ One parse/validate boundary for the whole form.
    const parsed = CheckoutSchema.safeParse(Object.fromEntries(data));
    if (!parsed.success) {
      setErrors(fieldErrors(parsed.error));
      return;
    }
    setErrors({});
    onSubmit(parsed.data);
  }

  return (
    <form onSubmit={handleSubmit} noValidate={false}>
      {/* ✅ Native constraints first: free, accessible, works without JS. */}
      <Field label="Email" error={errors.email}>
        <input
          name="email"
          type="email"
          required
          autoComplete="email"
          defaultValue=""
          aria-invalid={Boolean(errors.email)}
        />
      </Field>

      <Field label="Phone" error={errors.phone}>
        <PhoneInput name="phone" />
      </Field>

      <Field label="Amount" error={errors.amount}>
        <AmountInput name="amount" currency="USD" />
      </Field>

      <button type="submit">Pay</button>
    </form>
  );
}
```

```tsx
// ✅ Controlled, because it formats — but it stores the RAW string and only
//    reformats on blur, so the caret never moves while typing.
function PhoneInput({ name }: { name: string }) {
  const [raw, setRaw] = useState("");
  const composing = useRef(false);

  return (
    <input
      name={name}
      type="tel"
      inputMode="tel"
      autoComplete="tel"
      value={raw}
      onCompositionStart={() => { composing.current = true; }}
      onCompositionEnd={(e) => {
        composing.current = false;
        setRaw(e.currentTarget.value);        // ✅ accept the composed result whole
      }}
      onChange={(e) => setRaw(e.target.value)} // ✅ store exactly what was typed
      onBlur={(e) => {
        if (composing.current) return;
        setRaw(formatPhone(e.target.value));   // ✅ format once, when editing stops
      }}
    />
  );
}
```

```tsx
// ✅ Numeric field: state is a string, so "1.", "-", and "" are all representable.
function AmountInput({ name, currency }: { name: string; currency: string }) {
  const [text, setText] = useState("");

  // ✅ Derived during render — no second state slot to drift.
  const parsed = text.trim() === "" ? null : Number(text);
  const isValid = parsed !== null && Number.isFinite(parsed) && parsed >= 0;

  return (
    <>
      <input
        name={name}
        inputMode="decimal"
        value={text}
        onChange={(e) => setText(e.target.value)}
        aria-describedby={`${name}-preview`}
      />
      {/* ✅ The reason this field is controlled at all: live derived UI. */}
      <output id={`${name}-preview`}>
        {isValid
          ? new Intl.NumberFormat(undefined, { style: "currency", currency }).format(parsed)
          : "—"}
      </output>
    </>
  );
}
```

```tsx
// ✅ Live search: the input stays instant; only the expensive consumer is deferred.
function CountryPicker({ name }: { name: string }) {
  const [query, setQuery] = useState("");
  const deferredQuery = useDeferredValue(query);          // ✅ input never waits
  const matches = useMemo(() => searchCountries(deferredQuery), [deferredQuery]);

  return (
    <>
      <input
        value={query}                                     // ✅ value is never undefined
        onChange={(e) => setQuery(e.target.value)}
        role="combobox"
        aria-expanded={matches.length > 0}
        aria-controls={`${name}-listbox`}
        autoComplete="off"
      />
      <ul id={`${name}-listbox`} role="listbox">
        {matches.map((c) => (
          <li key={c.code} role="option" aria-selected={false}>{c.name}</li>
        ))}
      </ul>
      <input type="hidden" name={name} value={matches[0]?.code ?? ""} />
    </>
  );
}
```

**Why it's better:** the form itself is uncontrolled, so typing in any ordinary field costs zero renders and `FormData` collects every value in one place at submit — where a single schema parse produces both typed values and field errors. Only three fields are controlled, and each has a reason: the phone field formats, the amount field renders a live currency preview, the country field filters a list. `PhoneInput` stores the raw string and formats on blur, so the caret stays where the user put it, and the composition handlers mean an IME user's in-progress text is never rewritten mid-word. `AmountInput` keeps state as a string, so `"1."` and `"-"` survive, and derives validity during render rather than storing it in a second slot that could drift. `CountryPicker` keeps the input instantaneous while `useDeferredValue` lets the expensive filtered list lag by a frame — debouncing the consumer instead of the field. Every `value` has a defined string, so no input ever flips between controlled and uncontrolled.

## Common Mistakes

See the [Forms & Validation anti-patterns](../../../anti-patterns/) for the domain catalog. Concept-specific:

### Mistake: Transforming the value inside `onChange`

- **Symptom:** The caret jumps to the end of the field when editing anywhere but the end; IME input produces garbled text.
- **Why it fails:** React writes the transformed string back to the DOM, and setting `value` moves the caret to the end. Composition text is replaced before the user finishes the character.
- **Fix:** Store the raw input, format on blur or in a separate display element, and guard with `onCompositionStart`/`onCompositionEnd` if you must transform earlier.

### Mistake: Storing a parsed number instead of the typed string

- **Symptom:** Users cannot type a decimal point, a leading minus, or a trailing zero; the field sometimes shows `NaN`.
- **Why it fails:** Intermediate states like `"1."` and `"-"` have no numeric representation, so parsing round-trips them into something else.
- **Fix:** Keep state as a string, derive the parsed number during render, and validate at the submit boundary.

### Mistake: One state object for the entire form

- **Symptom:** Visible input lag on large forms, especially on mobile; profiler shows every field re-rendering per keystroke.
- **Why it fails:** A new object identity invalidates every consumer, so the render cost scales with field count rather than staying constant.
- **Fix:** Per-field state, an uncontrolled form read at submit, or a library with per-field subscriptions.

### Mistake: `value={possiblyUndefined}`

- **Symptom:** React warns that a component is changing an uncontrolled input to be controlled; an initial value is lost.
- **Why it fails:** `undefined` makes React treat the input as uncontrolled; when a string arrives later the input switches modes mid-life.
- **Fix:** `value={x ?? ""}`, and make the initial state an empty string rather than `undefined`.

### Mistake: Validating on every keystroke

- **Symptom:** "Invalid email" appears after the first character; users learn to ignore inline errors.
- **Why it fails:** A partially typed value is almost always invalid, so the message is noise for the entire duration of typing.
- **Fix:** Validate on blur and on submit; after the first failed submit, revalidate on change so corrections are acknowledged immediately.

## Checklist

- [ ] Fields are uncontrolled unless something on screen depends on their value before submit.
- [ ] Controlled fields store the raw string; parsing and formatting happen at boundaries.
- [ ] No `onChange` handler rewrites the value it was given.
- [ ] Composition events are handled wherever values are transformed.
- [ ] `value` is never `undefined`; `value={x ?? ""}` is used.
- [ ] Controlled state is per field, not one object for the whole form.
- [ ] Native constraint attributes (`required`, `type`, `pattern`, `min`) are present as the first validation layer.
- [ ] `name` and `autoComplete` are set so browser autofill and `FormData` both work.
- [ ] Validation runs on blur and submit, not on every keystroke.
- [ ] Expensive consumers are deferred or debounced; the input itself never is.
- [ ] The form has been tested with an IME and with browser autofill, not only with ASCII typing.

## Related Articles

- [Form Libraries & State Models](./form-libraries-and-state-models.md) — when per-field subscriptions and arrays justify a dependency.
- [Schema Validation](./schema-validation.md) — the single parse boundary the submit handler delegates to.
- [Schema-Inferred Types](./schema-inferred-types.md) — deriving field value types from the same schema.
- [Error Messaging](./error-messaging.md) — what to say once a field is invalid, and when to say it.
- [Uncontrolled Inputs & Refs](./) (planned) — the `FormData` path in depth.
- [Categories of State · State Management](../state-management/categories-of-state.md) — whether the value is state you should own at all.
- **Canonical home:** hook mechanics are owned by [useState · React](../../02-rendering-frameworks/react/usestate.md).

## References

- [React — `<input>`](https://react.dev/reference/react-dom/components/input) — controlled and uncontrolled props, and the mode-switch warning.
- [React — Controlled and uncontrolled components](https://react.dev/learn/sharing-state-between-components#controlled-and-uncontrolled-components) — the ownership framing.
- [MDN — FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData) — reading an entire form without controlling any field.
- [MDN — Constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Constraint_validation) — the native validation layer to build on.

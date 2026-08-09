---
title: "Coercion & Conversion"
slug: coercion-and-conversion
description: "The three abstract operations behind every implicit type change in JavaScript, and how to make conversion explicit at boundaries so it never surprises you."
keywords: ["type coercion", "type conversion", "ToPrimitive", "ToNumber", "ToString", "valueOf", "Symbol.toPrimitive", "implicit conversion", "JavaScript type system", "Number vs parseInt"]
part: "01 · Core Languages"
domain: "JavaScript"
subcategory: "Runtime Types"
difficulty: "Foundational"
reading_time_min: 8
priority: "Critical"
status: "Published"
canonical: true
last_reviewed: "2026-08-09"
prerequisites:
  - "Primitives & Wrappers"
related:
  - "Primitives & Wrappers"
  - "Equality & Comparison"
  - "null, undefined & Nullish"
next:
  - "Equality & Comparison"
alternatives:
  - "Equality & Comparison"
  - "null, undefined & Nullish"
common_mistakes:
  - "anti-patterns/README.md#javascript"
  - "#common-mistakes"
frameworks: []
references:
  - { title: "ECMA-262 — Type Conversion", url: "https://tc39.es/ecma262/#sec-type-conversion" }
  - { title: "MDN — Type coercion", url: "https://developer.mozilla.org/en-US/docs/Glossary/Type_coercion" }
  - { title: "MDN — Symbol.toPrimitive", url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/toPrimitive" }
  - { title: "MDN — Number() constructor", url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/Number" }
---

# Coercion & Conversion

> JavaScript's coercion rules are not arbitrary. They are three small algorithms applied consistently — and the surprises come from not knowing which one an operator invokes.

**Part:** [01 · Core Languages](../) · **Domain:** JavaScript · **Priority:** Critical · **Difficulty:** Foundational · **Reading time:** ~8 min

## TL;DR

**Conversion** is what you ask for (`Number(x)`, `String(x)`); **coercion** is what the language does on your behalf when an operator needs a different type. Both run the same three abstract operations: `ToPrimitive`, `ToNumber`, and `ToString`. `ToPrimitive` is the one that surprises people — it calls `Symbol.toPrimitive`, then `valueOf`, then `toString` in an order that depends on a *hint*, which is why `[] + {}` and `{} + []` differ and why `new Date() + 1` produces a string while `new Date() - 1` produces a number. The fix is not to memorize the table but to convert explicitly at boundaries, so coercion never runs where you did not intend it.

> **Recommendation:** Parse and validate at the edges of your system, use `===` inside it, and reach for `Number()`, `String()`, and `Boolean()` explicitly rather than `+x`, `x + ""`, or `!!x`.

## At a Glance

| | |
| --- | --- |
| **Use when** | Handling any untyped input — URL params, form values, JSON, `localStorage`, environment variables. |
| **Avoid when** | Relying on implicit coercion inside business logic; convert once at the boundary instead. |
| **Alternatives** | [Equality & Comparison](#alternative-approaches) for the comparison half; schema validation for structured input. |
| **Primary risk** | `NaN` and `"[object Object]"` propagating silently through calculations and into the UI. |
| **Maturity** | Stable — the rules have not changed since ES5 and will not change. |

## Prerequisites

You need to know what the seven primitive types are before you can reason about conversions between them.

- [Primitives & Wrappers](./primitives-and-wrappers.md) — the value types, and the objects the language temporarily wraps them in.

## Overview

Three abstract operations do all the work.

| Operation | Called by | Produces |
| --- | --- | --- |
| **`ToPrimitive(input, hint)`** | Any operator needing a primitive from an object | A primitive |
| **`ToNumber(input)`** | `-`, `*`, `/`, `%`, `**`, unary `+`, relational operators | A number (possibly `NaN`) |
| **`ToString(input)`** | Template literals, `String()`, property keys, `+` when either side is a string | A string |

`ToPrimitive` takes a **hint** — `"number"`, `"string"`, or `"default"` — and tries methods in an order determined by it:

- hint `"string"` → `Symbol.toPrimitive` → `toString` → `valueOf`
- hint `"number"` or `"default"` → `Symbol.toPrimitive` → `valueOf` → `toString`

Most operators pass `"number"`. Template literals and `String()` pass `"string"`. The `+` operator and `==` pass `"default"`, which behaves like `"number"` for every built-in except `Date`, whose `Symbol.toPrimitive` treats `"default"` as `"string"`. That single exception explains the classic puzzle:

```js
const d = new Date(0);
d + 1;   // "Thu Jan 01 1970 00:00:00 GMT+00001"  — hint "default" → string
d - 1;   // -1                                     — hint "number" → 0, then 0 - 1
```

`ToNumber` on strings trims whitespace, accepts numeric literals including hex and exponent forms, maps `""` to `0`, and yields `NaN` for anything else. On `null` it gives `0`; on `undefined`, `NaN`. `Boolean` conversion is simpler: exactly eight falsy values — `false`, `0`, `-0`, `0n`, `""`, `null`, `undefined`, `NaN` — and everything else is truthy, including `[]`, `{}`, `"0"`, and `"false"`.

The `+` operator is the only arithmetic operator with a string branch: it runs `ToPrimitive` on both operands with hint `"default"`, and if *either* result is a string it concatenates; otherwise it adds numerically.

## The Problem

Untyped input crosses into typed logic without anyone deciding where the conversion happens.

```js
// ❌ Values from the URL are strings; nothing here says so.
const params = new URLSearchParams(location.search);
const page = params.get("page");        // "2"
const perPage = params.get("perPage");  // "20"

const offset = page * perPage;          // 40  — works by accident
const nextPage = page + 1;              // "21" — concatenation, silently wrong
const total = offset + perPage;         // "4020" — worse
```

Every line here is coercion, and only some of it does what the author meant. `*` coerces both sides with `ToNumber`, so `offset` is right. `+` sees a string on the left and concatenates, so `nextPage` is `"21"` — a value that will keep working through further string operations and surface as a wrong page number three screens later.

The `NaN` propagation problem is worse because it is silent:

```js
// ❌ One missing field turns the whole calculation into NaN.
const amount = Number(row.amount);   // undefined → NaN
const tax = amount * 0.2;            // NaN
const total = amount + tax;          // NaN
element.textContent = `$${total.toFixed(2)}`;   // "$NaN"
```

`NaN` is contagious: every arithmetic operation involving it produces `NaN`, and `NaN !== NaN`, so naive equality checks never catch it. The error surfaces in the UI, far from the missing field that caused it.

And the object case:

```js
// ❌ An object used as a key, or concatenated.
const cache = {};
cache[{ id: 1 }] = "a";
cache[{ id: 2 }] = "b";
Object.keys(cache);   // ["[object Object]"] — one key, second write clobbers the first
```

## Why It Matters

Coercion bugs are uniquely expensive because they do not throw. A `TypeError` stops execution at the point of the mistake; a coercion bug produces a plausible-looking wrong value that travels.

The cost shows up in three places. **In money and quantities**, where `"19.99" + "5.00"` becomes `"19.995.00"` and a total is displayed to a user or, worse, submitted. **In persistence**, where `localStorage.setItem("count", 0)` stores the string `"0"` and `if (localStorage.getItem("count"))` is truthy on the way back, because `"0"` is a non-empty string. **In comparisons**, where `==` runs coercion before comparing, so `"" == 0`, `"0" == false`, and `null == undefined` are all true while `null == 0` is false — a set of rules that no one reconstructs correctly under review pressure.

The deeper reason to care is architectural. Deciding *where* conversion happens is a design decision: a system with explicit parse-at-the-boundary discipline has a small, testable set of conversion sites; a system that relies on implicit coercion has one at every operator, and no way to enumerate them.

## Mental Model

Every implicit conversion answers one question: *what primitive does this operator need?*

```text
   value ──► operator asks for a type
               │
               ├─ needs a primitive from an object?
               │     ToPrimitive(value, hint)
               │       hint "string"  → Symbol.toPrimitive → toString  → valueOf
               │       hint "number"  → Symbol.toPrimitive → valueOf   → toString
               │       hint "default" → same as "number" (except Date → string)
               │
               ├─ needs a number?   ToNumber   →  "" → 0, null → 0, undefined → NaN
               ├─ needs a string?   ToString   →  null → "null", [1,2] → "1,2"
               └─ needs a boolean?  ToBoolean  →  8 falsy values, everything else true
```

Two habits follow:

1. **Know which hint your operator sends.** `+` sends `"default"`; everything else arithmetic sends `"number"`; template literals send `"string"`.
2. **Convert once, at the boundary.** After the edge of your system, every value should already be the type it claims to be — at which point coercion has nothing left to do.

## Best Practices

- **Parse at the boundary.** URL params, form fields, `localStorage`, JSON, and environment variables are strings; convert them once, immediately, with validation.
- **Use `Number()` for whole-value conversion and `parseInt`/`parseFloat` only for prefix parsing.** `Number("12px")` is `NaN`; `parseInt("12px")` is `12`. Choose the one whose failure mode you want.
- **Check `Number.isNaN` (not global `isNaN`)** after any conversion that can fail, and `Number.isFinite` when `Infinity` is also invalid.
- **Prefer `String(x)` over `x + ""` and `` `${x}` ``** when the intent is conversion — `String(Symbol())` works where the others throw.
- **Use `??` rather than `||` for defaults** when `0` and `""` are legitimate values.
- **Never rely on `==`.** Use `===`, with the single idiomatic exception of `x == null` to test for `null` or `undefined` together.
- **Implement `Symbol.toPrimitive` on value objects** you define — money, durations, coordinates — so their coercion behavior is intentional instead of inherited from `Object.prototype.toString`.

## Trade-offs

Explicit conversion at boundaries costs a little ceremony and removes an entire class of silent failure.

**Advantages**

- Conversion sites become enumerable, reviewable, and testable.
- Failures surface at the edge, where the offending input is still in scope.
- Downstream code can assume types, which makes TypeScript annotations honest.

**Disadvantages**

- More code at boundaries than `+x` or `!!x`.
- Requires discipline: a single unparsed path reintroduces the problem.
- Validation libraries add a dependency and a schema to maintain.

| Dimension | This approach | Cost / caveat |
| --- | --- | --- |
| Performance | Negligible — conversions are cheap | Schema validation adds real cost on hot paths |
| Complexity | One clear conversion layer | Boundary code grows |
| Maintainability | Type assumptions documented in one place | Must be enforced, not just intended |
| Failure behavior | Errors at the edge with context | Requires deciding what "invalid" should do |

## Alternative Approaches

Explicit conversion competes with a few other ways of handling untyped input.

| Approach | Best when | Weakness | See |
| --- | --- | --- | --- |
| Explicit conversion + guards | Small boundaries, few fields | Manual; easy to miss a path | (this article) |
| Schema validation (Zod, Valibot) | Structured payloads, forms, APIs | Dependency, schema maintenance | `Schema Validation · Forms & Validation` |
| TypeScript alone | Internal code with trusted inputs | Erased at runtime; does not validate external data | `Assignability · TypeScript` |
| Relying on coercion | Never, in production code | Silent wrong values | — |

The practical rule: **structured input → schema validation; scalar input → explicit conversion with a guard; internal values → types, never coercion.**

## Bad Example

A checkout summary built from URL params and a form, relying on implicit coercion throughout.

```js
// ❌ Everything is a string, and nothing says so.
function renderSummary() {
  const params = new URLSearchParams(location.search);
  const qty = params.get("qty");                    // "3" | null
  const unitPrice = document.querySelector("#price").value;   // "19.99"
  const discount = localStorage.getItem("discount");           // "0" | null

  const subtotal = qty * unitPrice;                 // coerced; NaN if qty is null
  const afterDiscount = subtotal - discount;        // "0" → 0; null → 0. Accidentally fine.
  const shipping = afterDiscount > 50 ? 0 : 4.99;

  // ❌ + concatenates because shipping is a number but afterDiscount may be a string
  const total = afterDiscount + shipping;

  // ❌ "0" is truthy, so a zero discount renders the banner
  if (discount) showDiscountBanner(discount);

  // ❌ == comparison with coercion
  if (qty == 1) label.textContent = "1 item";

  document.querySelector("#total").textContent = "$" + total.toFixed(2);
}
```

**What goes wrong:** if `qty` is absent, `params.get` returns `null`, `null * "19.99"` is `NaN`, and every subsequent value is `NaN` — ending in a `TypeError` on `toFixed` or a rendered `"$NaN"`. `discount` is the string `"0"` when a user has no discount, which is truthy, so the banner appears advertising a zero discount. `afterDiscount - discount` happens to work because `-` always coerces to number, which trains the author to trust `+` too, where it does not. `qty == 1` passes for `"1"`, `1`, `true`, and `[1]` — coincidentally right here and a landmine the moment the source changes. And the whole calculation runs on values whose types depend on whether a query parameter was present, which no test that supplies the parameter will ever catch.

## Good Example

The same summary with a single conversion layer, explicit failure handling, and a value object that defines its own coercion.

```js
// ✅ One place that turns untyped input into typed values, with failures visible.
function toInteger(raw, { min = 0, max = Number.MAX_SAFE_INTEGER, fallback }) {
  const n = Number(raw);                     // "" → 0, "3px" → NaN, null → 0
  if (raw === null || raw === "" || !Number.isInteger(n) || n < min || n > max) {
    if (fallback === undefined) {
      throw new RangeError(`Expected an integer in [${min}, ${max}], received ${String(raw)}`);
    }
    return fallback;
  }
  return n;
}

function toMoneyCents(raw, { fallback } = {}) {
  const n = Number(raw);
  if (!Number.isFinite(n) || n < 0) {
    if (fallback === undefined) throw new RangeError(`Invalid amount: ${String(raw)}`);
    return fallback;
  }
  return Math.round(n * 100);                // integer cents — no float arithmetic on money
}
```

```js
// ✅ A value object whose coercion behavior is declared, not inherited.
class Money {
  #cents;

  constructor(cents) {
    if (!Number.isInteger(cents)) throw new TypeError("Money takes integer cents");
    this.#cents = cents;
  }

  static fromInput(raw, opts) { return new Money(toMoneyCents(raw, opts)); }

  plus(other) { return new Money(this.#cents + other.#cents); }
  times(n)    { return new Money(Math.round(this.#cents * n)); }
  get cents() { return this.#cents; }

  // ✅ Explicit: numeric contexts get cents, string contexts get a formatted amount.
  [Symbol.toPrimitive](hint) {
    if (hint === "number") return this.#cents;
    return new Intl.NumberFormat(undefined, {
      style: "currency",
      currency: "USD",
    }).format(this.#cents / 100);
  }
}
```

```js
// ✅ Below the boundary, every value already has the type it claims.
function renderSummary({ search, priceInput, storage }) {
  const params = new URLSearchParams(search);

  const qty = toInteger(params.get("qty"), { min: 1, max: 999, fallback: 1 });
  const unitPrice = Money.fromInput(priceInput.value);
  const discount = Money.fromInput(storage.getItem("discount"), { fallback: 0 });

  const subtotal = unitPrice.times(qty);
  const afterDiscount = new Money(Math.max(0, subtotal.cents - discount.cents));
  const shipping = new Money(afterDiscount.cents > 5000 ? 0 : 499);
  const total = afterDiscount.plus(shipping);

  // ✅ Zero is a number, and zero is falsy only where we mean it to be.
  if (discount.cents > 0) showDiscountBanner(discount);

  // ✅ Strict equality on a value we know is a number.
  label.textContent = qty === 1 ? "1 item" : `${qty} items`;

  // ✅ Template literal invokes Symbol.toPrimitive with hint "string" — formatted currency.
  document.querySelector("#total").textContent = `${total}`;
}
```

**Why it's better:** `toInteger` and `toMoneyCents` are the only places in the module where an untyped value becomes a typed one, so the conversion surface is three lines instead of every operator. Each rejects invalid input loudly or takes an explicit fallback, so a missing `qty` produces `1` by decision rather than `NaN` by accident. Money is stored as integer cents, which removes both float rounding and the string-concatenation risk from every arithmetic step. `Money` declares `Symbol.toPrimitive`, so a template literal formats it and a numeric context yields cents — coercion still happens, but its behavior was authored rather than inherited. The discount check tests `cents > 0` instead of truthiness, so a legitimate zero no longer renders a banner, and `qty === 1` compares two values that are known numbers.

## Common Mistakes

See the [JavaScript anti-patterns](../../../anti-patterns/#javascript) for the domain catalog. Concept-specific:

### Mistake: Treating `"0"`, `""`, or `"false"` as falsy

- **Symptom:** A stored preference of `0` or an empty string silently falls back to a default, or a `"false"` flag enables a feature.
- **Why it fails:** Only the empty string is falsy among strings. `"0"` and `"false"` are non-empty strings and therefore truthy.
- **Fix:** Convert before testing — `Number(raw) > 0`, `raw === "true"` — and use `??` for defaults so legitimate zeros survive.

### Mistake: Using `parseInt` where `Number` was meant

- **Symptom:** `"12px"` becomes `12`, and a malformed input passes validation.
- **Why it fails:** `parseInt` parses a *prefix* and stops at the first invalid character; `Number` requires the whole string to be numeric and returns `NaN` otherwise.
- **Fix:** Use `Number()` when the entire value must be numeric, and reserve `parseInt`/`parseFloat` for genuine prefix parsing with an explicit radix.

### Mistake: Checking for `NaN` with `==` or global `isNaN`

- **Symptom:** A `NaN` check never fires, or a non-numeric string is wrongly reported as `NaN`.
- **Why it fails:** `NaN !== NaN` by specification, so equality never matches. Global `isNaN` coerces its argument first, so `isNaN("foo")` is `true` even though `"foo"` is a string, not `NaN`.
- **Fix:** `Number.isNaN(value)`, which does not coerce, or `Number.isFinite(value)` when `Infinity` should also be rejected.

### Mistake: Letting objects reach `+` or a property key

- **Symptom:** `"[object Object]"` in the UI, or an object-keyed map that only ever has one entry.
- **Why it fails:** Property keys and string concatenation run `ToString`, and the default `Object.prototype.toString` returns `"[object Object]"` for every plain object.
- **Fix:** Use a `Map` for object keys, serialize deliberately for display, and define `Symbol.toPrimitive` or `toString` on value objects you own.

## Checklist

- [ ] Every external input — query params, form values, storage, JSON, env — is converted at a single, identifiable boundary.
- [ ] Conversions that can fail are followed by `Number.isNaN` or `Number.isFinite` guards.
- [ ] `Number()` and `parseInt` are chosen deliberately, and `parseInt` always passes a radix.
- [ ] Defaults use `??` rather than `||` wherever `0` or `""` is a valid value.
- [ ] `==` appears nowhere except the `x == null` idiom.
- [ ] Money and quantities are stored as integers, not floats built from strings.
- [ ] Value objects define `Symbol.toPrimitive` (or `toString`) rather than inheriting `"[object Object]"`.
- [ ] Object keys use `Map` when the key is not already a string or symbol.
- [ ] Tests cover the missing-input and malformed-input paths, not only the happy path.

## Related Articles

- [Primitives & Wrappers](./primitives-and-wrappers.md) — the value types conversion moves between, and the autoboxing that hides it.
- [Equality & Comparison](./) (planned) — the comparison operators and the coercion `==` performs before comparing.
- [null, undefined & Nullish](./) (planned) — the two absent values and how each converts.
- [Schema Validation · Forms & Validation](../../03-application-architecture/forms-validation/schema-validation.md) — declarative conversion and validation for structured input.
- **Canonical home:** compile-time type relationships are owned by [Assignability · TypeScript](../typescript/assignability.md).

## References

- [ECMA-262 — Type Conversion](https://tc39.es/ecma262/#sec-type-conversion) — the normative `ToPrimitive`, `ToNumber`, and `ToString` algorithms.
- [MDN — Type coercion](https://developer.mozilla.org/en-US/docs/Glossary/Type_coercion) — which operators coerce and to what.
- [MDN — Symbol.toPrimitive](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/toPrimitive) — declaring conversion behavior on your own objects.
- [MDN — Number() constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/Number) — exact string-to-number parsing rules.

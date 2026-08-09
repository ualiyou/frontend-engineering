---
title: "Test Doubles (mocks, stubs, fakes)"
slug: test-doubles-mocks-stubs-fakes
description: "The five kinds of test double, which one each dependency deserves, and why mocking what you do not own produces tests that pass while production breaks."
keywords: ["test doubles", "mocks", "stubs", "fakes", "spies", "dummy", "mock service worker", "don't mock what you don't own", "test isolation", "over-mocking"]
part: "05 · Reliability & Quality"
domain: "Testing & Quality"
subcategory: "Strategy"
difficulty: "Intermediate"
reading_time_min: 15
priority: "Critical"
status: "Published"
canonical: true
last_reviewed: "2026-08-09"
prerequisites:
  - "The Testing Pyramid/Trophy"
related:
  - "The Testing Pyramid/Trophy"
  - "What to Test & Coverage Goals"
next:
  - "Pure Logic Testing"
alternatives:
  - "What to Test & Coverage Goals"
common_mistakes:
  - "anti-patterns/README.md#testing-quality"
  - "#common-mistakes"
frameworks: []
references:
  - { title: "Martin Fowler — Mocks Aren't Stubs", url: "https://martinfowler.com/articles/mocksArentStubs.html" }
  - { title: "Martin Fowler — Test Double", url: "https://martinfowler.com/bliki/TestDouble.html" }
  - { title: "Mock Service Worker — Philosophy", url: "https://mswjs.io/docs/philosophy" }
  - { title: "Vitest — Mocking", url: "https://vitest.dev/guide/mocking" }
---

# Test Doubles (mocks, stubs, fakes)

> A mock asserts that a call happened. A fake makes the call work. The first tests your code's plumbing; the second tests its behavior — and only one of them survives a refactor.

**Part:** [05 · Reliability & Quality](../) · **Domain:** Testing & Quality · **Priority:** Critical · **Difficulty:** Intermediate · **Reading time:** ~15 min

## TL;DR

"Mock" is used for five distinct things: **dummy** (a value that fills a parameter), **stub** (returns canned answers), **spy** (records calls, real behavior intact), **mock** (asserts on the calls it expected), and **fake** (a working, simplified implementation). The choice determines what breaks when you refactor: stubs and fakes verify **state** — what your code produced — while mocks verify **interactions** — which functions it called, in what order. Interaction assertions are coupled to implementation, so a rename or a reordering fails a test even though behavior is unchanged. The strongest rule in this area is **don't mock what you don't own**: replace third-party clients at the *protocol* boundary (HTTP, the DOM, the clock), not at their API surface, or your test asserts your guess about the library rather than the library.

> **Recommendation:** Default to a fake at the network boundary and real code everywhere else. Reserve mocks for verifying side effects that have no observable state — an analytics event, an email send.

## At a Glance

| | |
| --- | --- |
| **Use when** | A dependency is slow, non-deterministic, expensive, or has side effects you must not trigger. |
| **Avoid when** | The real implementation is fast and deterministic — use it, and get a stronger test for free. |
| **Alternatives** | Real implementations, in-memory databases, contract tests, dependency injection. |
| **Primary risk** | A test suite that passes against a fiction, because the double drifted from the real thing. |
| **Maturity** | Stable — the vocabulary is Meszaros/Fowler; the tooling (MSW, fake timers) is mature. |

## Prerequisites

Which double to use follows from which layer of the pyramid you are testing.

- [The Testing Pyramid/Trophy](./the-testing-pyramid-trophy.md) — where isolation is worth its cost and where it is not.

## Overview

Five kinds, in order of how much they know.

| Double | Behavior | Verifies | Typical use |
| --- | --- | --- | --- |
| **Dummy** | Nothing; never used | — | Filling a required parameter |
| **Stub** | Returns canned values | State | "The API returns 500 — what does the UI show?" |
| **Spy** | Real behavior + call record | State (and calls, if needed) | "Did we log the error *and* still render?" |
| **Mock** | Pre-programmed expectations | Interactions | "Was `sendEmail` called exactly once with this address?" |
| **Fake** | Working, simplified implementation | State | In-memory repository, MSW handler, fake clock |

The distinction that matters in practice is **state verification versus interaction verification**.

```js
// State verification — asserts on the outcome.
const repo = new InMemoryUserRepo([{ id: "1", name: "Ada" }]);
await renameUser(repo, "1", "Ada L.");
expect(await repo.get("1")).toEqual({ id: "1", name: "Ada L." });

// Interaction verification — asserts on the calls.
const repo = { get: vi.fn(), save: vi.fn() };
await renameUser(repo, "1", "Ada L.");
expect(repo.save).toHaveBeenCalledWith({ id: "1", name: "Ada L." });
```

Both pass today. Change `renameUser` to use a single `update()` call instead of `get` plus `save`, with identical observable behavior, and the second test fails while the first still passes. That is the whole trade: interaction tests are coupled to *how*, state tests to *what*.

**Don't mock what you don't own** follows from this. When you stub `axios.get` or a payment SDK's client method, you encode your belief about that library's contract into the test. If the belief is wrong — a changed default, a different error shape, a new required field — the test still passes and production still breaks. Replacing the dependency one level lower, at the protocol it speaks, avoids that: MSW intercepts real HTTP, so your actual client library runs, with its real serialization, retries, and error handling.

**Fakes are the underused option.** An in-memory repository implementing the same interface as the real one gives you speed and determinism *and* state verification. It costs more to write and needs a contract test to prove it still matches — but it is the double that does not lie about behavior.

## The Problem

Over-mocking produces a suite that is fast, green, and worthless.

```js
// ❌ Every collaborator mocked. What is left under test?
vi.mock("../api/client");
vi.mock("../store/cart");
vi.mock("../analytics");
vi.mock("../format/currency");

test("checkout submits the order", async () => {
  apiClient.post.mockResolvedValue({ data: { orderId: "o_1" } });
  cartStore.getTotal.mockReturnValue(4999);
  formatCurrency.mockReturnValue("$49.99");

  render(<Checkout />);
  await userEvent.click(screen.getByRole("button", { name: "Pay" }));

  expect(apiClient.post).toHaveBeenCalledWith("/orders", {
    total: 4999,
    items: expect.any(Array),
  });
});
```

Nothing real ran. The currency formatter — where a rounding bug would live — was replaced by a mock returning a hard-coded string. The store's total calculation was replaced. The API client's serialization, error handling, and retry logic were replaced. The test asserts that the component calls a function that no longer exists in the test environment, with arguments the test itself supplied.

Now change `apiClient.post` to `apiClient.request({ method: "POST" })` with identical behavior: the test fails. Change the server to require a `currency` field: the test passes, production 400s.

The drift problem is the other half:

```js
// ❌ A stub encoding a guess about the real API's error shape.
apiClient.get.mockRejectedValue({ status: 404, message: "Not found" });

// The real client throws:  HttpError { response: { status: 404, data: { error: … } } }
// So the component's `err.response.status` check is never exercised.
```

The error-handling branch is covered according to the coverage report and has never been run against a shape the real client produces.

## Why It Matters

Test doubles decide what your suite is actually verifying, which is a different question from what it appears to verify.

**Confidence.** A suite built on interaction assertions tells you the code calls the functions it calls. It cannot tell you the feature works. Teams discover this after a refactor: two hundred tests go red, none of them because behavior changed, and the team learns that red does not mean broken. That is the point at which a test suite stops being a safety net.

**Refactor cost.** Mocks pin the implementation. Every internal change requires updating tests that assert internals, so the suite makes exactly the change it should be enabling more expensive. Fakes and stubs at a stable boundary do not: the boundary is the contract, and the contract is what you did not want to change anyway.

**False security.** The most expensive failure mode is a test that passes against a fiction. A stubbed error shape that does not match the real one means an error path is "covered" and untested. This produces production incidents in exactly the code paths the team believed were verified.

**Speed is real, though.** Doubles exist because network calls, timers, and third-party SDKs make tests slow and flaky, and a slow suite is a suite people stop running. The goal is not fewer doubles but *doubles at the right boundary* — where the contract is stable enough that the double stays honest.

## Mental Model

Push the double down to the lowest stable boundary and use the real thing above it.

```text
   ┌─ component / hook under test ────────────────┐
   │   REAL                                       │
   ├─ your own modules (store, format, validate) ─┤
   │   REAL — fast and deterministic already      │
   ├─ your API client (fetch wrapper, SDK) ───────┤
   │   REAL — this is the code you want exercised │
   ├─ the protocol boundary ──────────────────────┤
   │   ◄── DOUBLE HERE (MSW intercepts HTTP)      │
   └─ network / clock / random / storage ─────────┘
       ◄── DOUBLE HERE (fake timers, seeded RNG)

   Higher doubles  = faster, more isolated, less true
   Lower doubles   = slower, more integrated, more true
```

Three questions choose the double:

1. **Does the test care what came back?** → stub or fake.
2. **Does the test care that something was *sent* and nothing observable resulted?** (analytics, email, logging) → mock or spy.
3. **Do I own this interface?** No → double the protocol underneath it, not the interface itself.

## Best Practices

- **Fake the network, not the client.** Mock Service Worker (or equivalent) intercepts real requests, so your actual fetch wrapper, headers, serialization, and error handling all execute.
- **Use the real implementation whenever it is fast and deterministic.** Formatters, validators, reducers, and pure functions never need doubles.
- **Prefer state verification.** Assert on rendered output or returned data; assert on calls only when there is no observable state to assert on.
- **Give fakes a contract test.** One test runs the same suite against both the fake and the real implementation, so drift is caught at the boundary rather than in production.
- **Fake the clock explicitly** with `vi.useFakeTimers()` / `jest.useFakeTimers()`, and restore it in teardown. Time is the most common source of flakiness.
- **Keep doubles in one place per boundary** — a `handlers.ts` for HTTP, a `testDoubles.ts` for repositories — so drift is visible and fixable in one edit.
- **Reset between tests.** `restoreMocks`, `clearMocks`, and MSW's `resetHandlers` prevent order-dependent suites.
- **Assert the error shape you actually get.** Build stubbed errors from the same constructor the real code throws.

## Trade-offs

Doubles buy speed and determinism, and pay in fidelity and maintenance.

**Advantages**

- Tests run in milliseconds without network, database, or third-party availability.
- Error paths, timeouts, and rate limits become easy to exercise deterministically.
- Side effects with real-world cost — emails, charges, notifications — are safely suppressed.
- Fakes give both speed and behavioral truth, which no other double does.

**Disadvantages**

- Every double is a second implementation that can drift from the first.
- Interaction assertions couple tests to implementation details.
- Heavy mocking hollows out a test until it verifies only its own setup.
- Fakes cost real effort to write and must be maintained alongside the real thing.

| Dimension | This approach | Cost / caveat |
| --- | --- | --- |
| Performance | Milliseconds instead of seconds | A fake that is too clever becomes slow and buggy itself |
| Complexity | Stubs are trivial | Fakes are a parallel implementation |
| Maintainability | Boundary doubles survive refactors | Interaction mocks break on every internal change |
| Failure behavior | Deterministic and reproducible | Green against a fiction is the worst possible outcome |

## Alternative Approaches

Doubles compete with strategies that remove the need for them.

| Approach | Best when | Weakness | See |
| --- | --- | --- | --- |
| Fake at the protocol boundary (MSW) | Anything that talks HTTP | Handlers must track the real API | (this article) |
| Real implementation | Fast, deterministic, no side effects | Impossible for network, time, randomness | [Pure Logic Testing](./pure-logic-testing.md) |
| In-memory fake behind an interface | You own the interface (repositories, caches) | A second implementation to maintain | — |
| Contract tests | Two teams own two sides of an API | Requires coordination and a shared broker | — |
| End-to-end against a real environment | Final confidence before release | Slow, flaky, expensive; a few, not many | `The Testing Pyramid/Trophy · Testing & Quality` |

The practical rule: **real code by default; a fake at the protocol boundary; a mock only for side effects with no observable result.**

## Bad Example

A checkout test where every dependency is mocked and every assertion is about a call.

```tsx
// ❌ checkout.test.tsx — mocks all the way down.
vi.mock("../api/client");
vi.mock("../store/cart");
vi.mock("../lib/analytics");
vi.mock("../format/currency");
vi.mock("../hooks/useUser");

import { apiClient } from "../api/client";
import { cartStore } from "../store/cart";
import { track } from "../lib/analytics";
import { formatCurrency } from "../format/currency";

test("checkout pays", async () => {
  // ❌ Guessing the client's success shape.
  apiClient.post.mockResolvedValue({ data: { orderId: "o_1" } });
  cartStore.getItems.mockReturnValue([{ sku: "a", qty: 2, price: 1999 }]);
  cartStore.getTotal.mockReturnValue(3998);
  formatCurrency.mockReturnValue("$39.98");        // ❌ the real bug would live here

  render(<Checkout />);
  await userEvent.click(screen.getByRole("button", { name: "Pay" }));

  // ❌ Asserting on calls, not on what the user sees.
  expect(apiClient.post).toHaveBeenCalledTimes(1);
  expect(apiClient.post).toHaveBeenCalledWith("/orders", {
    items: [{ sku: "a", qty: 2, price: 1999 }],
    total: 3998,
  });
  expect(track).toHaveBeenCalledWith("checkout_completed");
});

test("checkout shows an error", async () => {
  // ❌ A shape the real client never throws.
  apiClient.post.mockRejectedValue({ status: 500, message: "boom" });

  render(<Checkout />);
  await userEvent.click(screen.getByRole("button", { name: "Pay" }));

  expect(apiClient.post).toHaveBeenCalled();       // ❌ asserts nothing about the UI
});

// ❌ Real timers: a retry with backoff makes this take 8 seconds, or flake.
test("checkout retries", async () => {
  apiClient.post
    .mockRejectedValueOnce({ status: 503 })
    .mockResolvedValueOnce({ data: { orderId: "o_2" } });

  render(<Checkout />);
  await userEvent.click(screen.getByRole("button", { name: "Pay" }));
  await waitFor(() => expect(apiClient.post).toHaveBeenCalledTimes(2), { timeout: 10_000 });
});
```

**What goes wrong:** with five modules mocked, the only real code executing is `Checkout`'s JSX. The currency formatter — the single most likely place for a rounding or locale bug — returns a hard-coded string, so a broken formatter ships green. The total is supplied by the test rather than computed, so a cart-calculation bug is invisible. `apiClient.post` is stubbed at the client's API surface, so the client's own serialization, header construction, and error normalization never run; when the server later requires a `currency` field, the test still passes because the test itself defined the payload. The error test asserts that a mock was called and says nothing about what the user sees — a component that swallows the error and renders a blank screen passes. The rejected value `{ status: 500 }` is not the shape the real client throws, so the component's real error branch is never exercised despite being reported as covered. And the retry test uses real timers, so it either takes eight seconds or flakes under CI load.

## Good Example

Real code everywhere except the protocol boundary, with a fake for owned interfaces and mocks only for fire-and-forget side effects.

```ts
// ✅ test/handlers.ts — one place describing what the server does.
import { http, HttpResponse } from "msw";
import { setupServer } from "msw/node";

export const handlers = [
  http.post("/orders", async ({ request }) => {
    const body = await request.json();
    if (!body.currency) {
      return HttpResponse.json({ error: "currency is required" }, { status: 400 });
    }
    return HttpResponse.json({ orderId: "o_1", total: body.total }, { status: 201 });
  }),
];

export const server = setupServer(...handlers);
```

```ts
// ✅ test/setup.ts — deterministic by default, restored between tests.
import { afterAll, afterEach, beforeAll, vi } from "vitest";
import { server } from "./handlers";

beforeAll(() => server.listen({ onUnhandledRequest: "error" }));  // ✅ surprises fail loudly
afterEach(() => {
  server.resetHandlers();
  vi.restoreAllMocks();
  vi.useRealTimers();
});
afterAll(() => server.close());
```

```tsx
// ✅ checkout.test.tsx — real client, real store, real formatter.
import { http, HttpResponse } from "msw";
import { server } from "./test/handlers";
import { track } from "../lib/analytics";

vi.mock("../lib/analytics");     // ✅ the ONE double: a side effect with no observable state

test("shows a confirmation with the real formatted total", async () => {
  render(<Checkout initialCart={[{ sku: "a", qty: 2, price: 1999 }]} />);

  await userEvent.click(screen.getByRole("button", { name: "Pay" }));

  // ✅ State verification: what the user actually sees, computed by real code.
  expect(await screen.findByText("Order confirmed")).toBeVisible();
  expect(screen.getByText("$39.98")).toBeVisible();    // real formatter, real total

  // ✅ Interaction verification, but only for the effect with no visible outcome.
  expect(track).toHaveBeenCalledWith("checkout_completed", { orderId: "o_1" });
});

test("surfaces a server error to the user", async () => {
  server.use(
    http.post("/orders", () =>
      HttpResponse.json({ error: "Card declined" }, { status: 402 }),
    ),
  );

  render(<Checkout initialCart={[{ sku: "a", qty: 1, price: 1999 }]} />);
  await userEvent.click(screen.getByRole("button", { name: "Pay" }));

  // ✅ The real client's real error path produced this.
  expect(await screen.findByRole("alert")).toHaveTextContent("Card declined");
  expect(screen.getByRole("button", { name: "Pay" })).toBeEnabled();   // recoverable
});

test("retries a 503 without waiting in real time", async () => {
  vi.useFakeTimers({ shouldAdvanceTime: true });     // ✅ backoff is instant

  let attempts = 0;
  server.use(
    http.post("/orders", () => {
      attempts += 1;
      return attempts === 1
        ? new HttpResponse(null, { status: 503 })
        : HttpResponse.json({ orderId: "o_2" }, { status: 201 });
    }),
  );

  render(<Checkout initialCart={[{ sku: "a", qty: 1, price: 1999 }]} />);
  await userEvent.click(screen.getByRole("button", { name: "Pay" }));

  await vi.advanceTimersByTimeAsync(5_000);
  expect(await screen.findByText("Order confirmed")).toBeVisible();
  expect(attempts).toBe(2);
});
```

```ts
// ✅ A fake for an interface you DO own, plus a contract test proving it still matches.
export class InMemoryOrderRepo implements OrderRepo {
  #orders = new Map<string, Order>();

  async save(order: Order) { this.#orders.set(order.id, structuredClone(order)); }
  async get(id: string)    { return this.#orders.get(id) ?? null; }
  async listFor(userId: string) {
    return [...this.#orders.values()].filter((o) => o.userId === userId);
  }
}

// ✅ One suite, two implementations — the fake cannot drift silently.
describe.each([
  ["in-memory", () => new InMemoryOrderRepo()],
  ["postgres", () => new PostgresOrderRepo(testDb)],
])("OrderRepo contract: %s", (_name, create) => {
  test("returns null for an unknown id", async () => {
    expect(await create().get("missing")).toBeNull();
  });

  test("listFor is scoped to the user", async () => {
    const repo = create();
    await repo.save(makeOrder({ id: "1", userId: "u1" }));
    await repo.save(makeOrder({ id: "2", userId: "u2" }));
    expect(await repo.listFor("u1")).toHaveLength(1);
  });
});
```

**Why it's better:** the only mocked module is analytics — a side effect with no observable result, which is precisely the case interaction verification exists for. Everything else runs for real: the cart total is computed, the currency formatter formats, and the API client performs an actual `fetch` that MSW intercepts at the protocol level, so serialization, headers, and error normalization are all exercised. Because the handler validates the request body, a missing `currency` field fails the test the same way it would fail in production, instead of passing because the test supplied the payload. The error test asserts on what the user sees — an alert with the server's message and a still-enabled button — which a component that swallows the error cannot pass. Fake timers make the backoff instant, removing both the eight-second runtime and the flake. `onUnhandledRequest: "error"` means any request the handlers do not describe fails loudly rather than silently hitting the network. And the `InMemoryOrderRepo` is validated by the same contract suite as the real repository, so the fake is proven to behave like the thing it replaces rather than assumed to.

## Common Mistakes

See the [Testing & Quality anti-patterns](../../../anti-patterns/) for the domain catalog. Concept-specific:

### Mistake: Mocking what you do not own

- **Symptom:** `vi.mock("axios")`, a stubbed SDK client, a hand-written fake of a third-party response.
- **Why it fails:** The test encodes your belief about the library's contract. If the belief is wrong — or becomes wrong after an upgrade — the test still passes while production breaks.
- **Fix:** Double the protocol underneath the library (HTTP via MSW, the clock via fake timers) so the real library executes.

### Mistake: Asserting on calls when there is observable state

- **Symptom:** `expect(save).toHaveBeenCalledWith(...)` as the only assertion in a test.
- **Why it fails:** The test is pinned to how the code achieves the result, so a behavior-preserving refactor fails it — and a broken result with the right call passes it.
- **Fix:** Assert on the rendered output or the returned data. Use interaction assertions only for effects with no observable state.

### Mistake: Mocking your own fast, pure modules

- **Symptom:** `vi.mock` on formatters, validators, reducers, or selectors.
- **Why it fails:** These are exactly the modules whose bugs a test should catch, and they cost nothing to run for real.
- **Fix:** Delete the mock. If the module is slow, that is a design problem to fix rather than to hide.

### Mistake: Stubbing an error shape the real code never produces

- **Symptom:** `mockRejectedValue({ status: 500 })` when the real client throws an `HttpError` with a nested `response`.
- **Why it fails:** The component's real error branch is never executed, so it is reported as covered and is in fact untested.
- **Fix:** Produce errors through the real path — an MSW handler returning the status — or construct them with the same class the production code throws.

### Mistake: Doubles that leak between tests

- **Symptom:** Tests pass alone and fail in suite, or pass in one order and fail in another.
- **Why it fails:** Mock return values, handler overrides, and fake timers persist unless explicitly reset.
- **Fix:** Reset in `afterEach` — `restoreAllMocks`, `resetHandlers`, `useRealTimers` — and enable `restoreMocks` in the runner config.

### Mistake: Using real timers with retries or debounces

- **Symptom:** Tests that take seconds and flake under CI load.
- **Why it fails:** Backoff and debounce delays are real wall-clock waits, and CI machines are slower and more variable than laptops.
- **Fix:** Fake timers, advancing time explicitly; assert the number of attempts rather than waiting for them.

## Checklist

- [ ] The network is faked at the protocol boundary, not at the client's API surface.
- [ ] No third-party module you do not own is mocked directly.
- [ ] Your own pure, fast modules run for real in every test.
- [ ] Assertions target observable state; interaction assertions exist only where no state is observable.
- [ ] Stubbed errors are constructed the way the real code constructs them.
- [ ] Fakes of owned interfaces are covered by a contract test that also runs against the real implementation.
- [ ] Timers are faked wherever retries, debounces, or polling are involved.
- [ ] Mocks and handlers are reset in `afterEach`; the suite passes in a randomized order.
- [ ] Unhandled requests fail the test rather than reaching the network.
- [ ] Handlers and doubles live in one shared place per boundary, not inline in each test file.

## Related Articles

- [The Testing Pyramid/Trophy](./the-testing-pyramid-trophy.md) — which layer justifies which degree of isolation.
- [What to Test & Coverage Goals](./what-to-test-and-coverage-goals.md) — why a covered line and a tested behavior are different things.
- [Pure Logic Testing](./pure-logic-testing.md) — the tests that need no doubles at all.
- [Retries & Backoff · Data & Server State](../../03-application-architecture/data-server-state/retries-and-backoff.md) — the behavior fake timers make testable.
- **Canonical home:** request-level caching behavior is owned by [Cache Invalidation · Data & Server State](../../03-application-architecture/data-server-state/cache-invalidation.md).

## References

- [Martin Fowler — Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html) — the state-versus-interaction distinction in full.
- [Martin Fowler — Test Double](https://martinfowler.com/bliki/TestDouble.html) — the five-way taxonomy and its origins in Meszaros.
- [Mock Service Worker — Philosophy](https://mswjs.io/docs/philosophy) — the argument for doubling the protocol rather than the client.
- [Vitest — Mocking](https://vitest.dev/guide/mocking) — module mocking, spies, fake timers, and reset semantics.

# Anti-Pattern: Treating Server Cache as Client State

**Domain:** [Data & Server State](./README.md#data-server-state) · **The right way:** [Cache Keys & Query Identity](../docs/03-application-architecture/data-server-state/cache-keys-and-query-identity.md), [Fetch-on-Render vs Render-as-You-Fetch](../docs/03-application-architecture/data-server-state/fetch-on-render-vs-render-as-you-fetch.md)

Server data is a *cache* of state that lives on the server; it is stale the moment you fetch it. This anti-pattern copies fetched data into local React state (`useState`/`useReducer`/a global store) and treats that copy as the source of truth — reintroducing every problem a server-state cache exists to solve.

## Symptom

A `useEffect` fetches, then stores the result in `useState`; components read and mutate that local copy.

```tsx
// ❌ The server response is copied into client state and manually managed.
function InvoiceList() {
  const [invoices, setInvoices] = useState<Invoice[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/invoices')
      .then((response) => response.json())
      .then((data) => {
        setInvoices(data);
        setLoading(false);
      });
    // No cancellation, no error state, no dedupe, no staleness — all hand-rolled.
  }, []);

  // ...and now every other component that needs invoices fetches its own copy.
}
```

## Why it fails

Server state and client state have different natures. Client state (a modal's open flag, a form's draft) is owned by the UI and has one authoritative copy. Server state is owned elsewhere, shared across components, and can change without the client knowing. Modeling it as client state means you hand-build — badly, and separately in each component — the things a query cache gives you for free: request deduplication, caching across mounts, background revalidation, staleness tracking, retry, and cancellation.

The concrete failures pile up fast. Two components that need invoices fetch twice because there's no shared cache keyed by identity. A `useEffect` with no cleanup leaks requests and races on unmount. There's no `staleTime`, so either data is never refreshed or it's refetched on every mount with no coordination. Updating after a mutation means manually threading `setInvoices` through props or a global store, which drifts from the server. None of this is a bug you *wrote*; it's the absence of a cache, reconstructed one missing feature at a time.

## Fix

Use a server-state cache (TanStack Query) as the source of truth, keyed by identity. Components read from the cache; nobody copies the data into local state.

```tsx
// ✅ One cache, keyed by identity; dedupe, staleness, retry, and cancellation
// are handled. Every component reads the same entry.
function InvoiceList() {
  const { data: invoices, isPending, isError } = useQuery({
    queryKey: ['invoices', 'list'],
    queryFn: ({ signal }) => fetchInvoices(signal),
    staleTime: 30_000,
  });

  if (isPending) return <p>Loading…</p>;
  if (isError) return <p role="alert">Couldn’t load invoices.</p>;
  return <ul>{invoices.map((invoice) => <li key={invoice.id}>{invoice.number}</li>)}</ul>;
}
```

Keep genuinely client-owned state (form drafts, UI toggles) in React state; keep server-owned state in the cache. Never mirror one into the other.

## See also

- Canonical articles: [Cache Keys & Query Identity](../docs/03-application-architecture/data-server-state/cache-keys-and-query-identity.md), [Fetch-on-Render vs Render-as-You-Fetch](../docs/03-application-architecture/data-server-state/fetch-on-render-vs-render-as-you-fetch.md)
- Example: [Query key factory](../examples/query-key-factory.ts)

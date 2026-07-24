# Recipe: Paginated Query with Prefetch on Intent

A paginated list that keeps the current page on screen while the next loads, prefetches the next page before the user asks for it, and warms each row's detail route on hover — so paging and drilling in both feel instant.

This recipe applies [Fetch-on-Render vs Render-as-You-Fetch](../docs/03-application-architecture/data-server-state/fetch-on-render-vs-render-as-you-fetch.md), [Cache Keys & Query Identity](../docs/03-application-architecture/data-server-state/cache-keys-and-query-identity.md), and [Staleness & Revalidation](../docs/03-application-architecture/data-server-state/staleness-and-revalidation.md).

## Stack

React 19, TypeScript 5.x, Vite, TanStack Query v5, Tailwind CSS v4, pnpm.

## The problem it solves

Naive pagination clears the list to a spinner on every page change and only starts loading the next page when the user clicks Next — a full round trip of waiting per page. This recipe uses `placeholderData` to keep the previous page visible during the fetch, prefetches the next page as soon as the current one loads, and warms detail routes on hover, turning most navigations into cache hits.

## File structure

```text
features/invoice-list/
├─ invoice-keys.ts          # key factory (list by page + detail)
├─ use-invoice-page.ts      # paginated query + next-page prefetch
├─ InvoiceListPage.tsx      # UI with keep-previous-page + hover prefetch
└─ invoice-list.test.tsx
```

## 1. Keys

Pagination is part of identity, so the page is in the key.

```ts
// invoice-keys.ts
import { queryOptions, keepPreviousData } from '@tanstack/react-query';

export interface Page<T> {
  items: T[];
  page: number;
  totalPages: number;
}
export interface Invoice {
  id: string;
  number: string;
  customer: string;
}

export const invoiceKeys = {
  all: ['invoices'] as const,
  lists: () => [...invoiceKeys.all, 'list'] as const,
  page: (page: number) => [...invoiceKeys.lists(), { page }] as const,
  details: () => [...invoiceKeys.all, 'detail'] as const,
  detail: (id: string) => [...invoiceKeys.details(), id] as const,
};

async function fetchInvoicePage(page: number, signal: AbortSignal): Promise<Page<Invoice>> {
  const response = await fetch(`/api/invoices?page=${page}`, { signal });
  if (!response.ok) throw new Error(`Failed to load page ${page} (${response.status})`);
  return (await response.json()) as Page<Invoice>;
}

export const invoicePageQuery = (page: number) =>
  queryOptions({
    queryKey: invoiceKeys.page(page),
    queryFn: ({ signal }) => fetchInvoicePage(page, signal),
    // Keep the previous page's data visible while the next one loads.
    placeholderData: keepPreviousData,
    staleTime: 30_000,
  });

async function fetchInvoice(id: string, signal: AbortSignal): Promise<Invoice> {
  const response = await fetch(`/api/invoices/${id}`, { signal });
  if (!response.ok) throw new Error(`Failed to load invoice ${id} (${response.status})`);
  return (await response.json()) as Invoice;
}

export const invoiceDetailQuery = (id: string) =>
  queryOptions({
    queryKey: invoiceKeys.detail(id),
    queryFn: ({ signal }) => fetchInvoice(id, signal),
    staleTime: 30_000,
  });
```

## 2. The paginated query + next-page prefetch

```ts
// use-invoice-page.ts
import { useEffect } from 'react';
import { useQuery, useQueryClient } from '@tanstack/react-query';
import { invoicePageQuery } from './invoice-keys';

export function useInvoicePage(page: number) {
  const queryClient = useQueryClient();
  const query = useQuery(invoicePageQuery(page));

  // As soon as the current page is known, warm the next one so Next is instant.
  useEffect(() => {
    if (query.data && page < query.data.totalPages) {
      void queryClient.prefetchQuery(invoicePageQuery(page + 1));
    }
  }, [queryClient, page, query.data]);

  return query;
}
```

## 3. The UI

Keep-previous-page avoids the spinner-per-page flash; `isPlaceholderData` dims the list subtly while the real page loads. Hovering a row warms its detail route.

```tsx
// InvoiceListPage.tsx
import { useState } from 'react';
import { useQueryClient } from '@tanstack/react-query';
import { invoiceDetailQuery, type Invoice } from './invoice-keys';
import { useInvoicePage } from './use-invoice-page';

export function InvoiceListPage() {
  const [page, setPage] = useState(1);
  const queryClient = useQueryClient();
  const { data, isPending, isError, isPlaceholderData } = useInvoicePage(page);

  if (isPending) return <p>Loading invoices…</p>;
  if (isError) return <p role="alert">Couldn’t load invoices.</p>;

  return (
    <div>
      <ul className={isPlaceholderData ? 'opacity-60 transition-opacity' : ''}>
        {data.items.map((invoice: Invoice) => (
          <li key={invoice.id}>
            <a
              href={`/invoices/${invoice.id}`}
              onMouseEnter={() => queryClient.prefetchQuery(invoiceDetailQuery(invoice.id))}
              onFocus={() => queryClient.prefetchQuery(invoiceDetailQuery(invoice.id))}
            >
              {invoice.number} — {invoice.customer}
            </a>
          </li>
        ))}
      </ul>

      <nav className="mt-4 flex items-center gap-3" aria-label="Pagination">
        <button
          type="button"
          onClick={() => setPage((current) => Math.max(1, current - 1))}
          disabled={page === 1}
          className="rounded border px-3 py-1 disabled:opacity-50"
        >
          Previous
        </button>
        <span aria-live="polite">Page {data.page} of {data.totalPages}</span>
        <button
          type="button"
          // Next is usually a cache hit thanks to the prefetch.
          onClick={() => setPage((current) => Math.min(data.totalPages, current + 1))}
          disabled={page >= data.totalPages}
          className="rounded border px-3 py-1 disabled:opacity-50"
        >
          Next
        </button>
      </nav>
    </div>
  );
}
```

## Testing

Assert that (1) changing page keeps the previous items visible until the new page resolves (`isPlaceholderData`), (2) the next page is prefetched into the cache after the current loads, and (3) hovering a row populates its detail key. Mock fetch per page and inspect the query cache.

## Why this feels instant

The page is part of the key, so each page caches independently and revisits are free within `staleTime`. `keepPreviousData` removes the empty-flash on page change. The next page is fetched before it's requested, and detail routes are warmed on hover — so the common paths (Next, click a row) hit an already-populated cache instead of waiting on the network.

## Related

- Articles: [Fetch-on-Render vs Render-as-You-Fetch](../docs/03-application-architecture/data-server-state/fetch-on-render-vs-render-as-you-fetch.md), [Cache Keys & Query Identity](../docs/03-application-architecture/data-server-state/cache-keys-and-query-identity.md).
- Examples: [Query key factory](../examples/query-key-factory.ts), [Render-as-you-fetch loader](../examples/render-as-you-fetch-loader.tsx).

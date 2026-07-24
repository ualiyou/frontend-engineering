// render-as-you-fetch-loader.tsx
//
// Start the request at the navigation boundary (a route loader), then read it
// from the cache with useSuspenseQuery. The component never owns fetch timing,
// so there is no render→fetch waterfall and the loading boundary is intentional.
//
// Illustrates: Fetch-on-Render vs Render-as-You-Fetch.

import {
  QueryClient,
  queryOptions,
  useSuspenseQuery,
} from '@tanstack/react-query';

interface Invoice {
  id: string;
  number: string;
  customer: string;
  amountCents: number;
}

async function fetchInvoice(id: string, signal: AbortSignal): Promise<Invoice> {
  const response = await fetch(`/api/invoices/${id}`, { signal });
  if (!response.ok) {
    throw new Error(
      response.status === 404
        ? `Invoice ${id} not found`
        : `Failed to load invoice ${id} (${response.status})`,
    );
  }
  return (await response.json()) as Invoice;
}

// One query definition, shared by the loader and the component.
const invoiceDetailQuery = (id: string) =>
  queryOptions({
    queryKey: ['invoices', 'detail', id],
    queryFn: ({ signal }) => fetchInvoice(id, signal),
    staleTime: 30_000,
  });

// Loader: runs when the route matches, before InvoiceDetail mounts. Returns once
// the data is cached, or throws to the route's error element on failure.
export function invoiceDetailLoader(queryClient: QueryClient, id: string) {
  return queryClient.ensureQueryData(invoiceDetailQuery(id));
}

// Component: a guaranteed cache hit because the loader warmed the exact key.
export function InvoiceDetail({ id }: { id: string }) {
  const { data: invoice } = useSuspenseQuery(invoiceDetailQuery(id));

  return (
    <article>
      <h1>{invoice.number}</h1>
      <p>{invoice.customer}</p>
      <p>{(invoice.amountCents / 100).toLocaleString(undefined, {
        style: 'currency',
        currency: 'USD',
      })}</p>
    </article>
  );
}

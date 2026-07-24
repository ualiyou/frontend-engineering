// query-key-factory.ts
//
// A typed query-key factory: one source of truth for a resource's cache identity.
// Reads, prefetches, and invalidations all import from here, so keys cannot drift
// between call sites. Keys are ordered general → specific to enable prefix
// invalidation (invalidate every list with one call, or one detail with another).
//
// Illustrates: Cache Keys & Query Identity.

import { queryOptions } from '@tanstack/react-query';

export interface InvoiceFilters {
  status?: 'draft' | 'sent' | 'paid';
  customerId?: string;
}

export interface Invoice {
  id: string;
  number: string;
  customer: string;
  amountCents: number;
  status: 'draft' | 'sent' | 'paid';
}

// The factory. `as const` gives literal tuples, so TypeScript tracks the exact
// key shape and autocompletes each level.
export const invoiceKeys = {
  all: ['invoices'] as const,
  lists: () => [...invoiceKeys.all, 'list'] as const,
  list: (filters: InvoiceFilters) => [...invoiceKeys.lists(), filters] as const,
  details: () => [...invoiceKeys.all, 'detail'] as const,
  detail: (id: string) => [...invoiceKeys.details(), id] as const,
};

async function fetchInvoices(
  filters: InvoiceFilters,
  signal: AbortSignal,
): Promise<Invoice[]> {
  const params = new URLSearchParams();
  if (filters.status) params.set('status', filters.status);
  if (filters.customerId) params.set('customerId', filters.customerId);

  const response = await fetch(`/api/invoices?${params}`, { signal });
  if (!response.ok) {
    throw new Error(`Failed to load invoices (${response.status})`);
  }
  return (await response.json()) as Invoice[];
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

// Bind each key to its fetcher so a component cannot pair the right key with the
// wrong request. Loaders and components share these objects for render-as-you-fetch.
export const invoiceListQuery = (filters: InvoiceFilters) =>
  queryOptions({
    queryKey: invoiceKeys.list(filters),
    queryFn: ({ signal }) => fetchInvoices(filters, signal),
  });

export const invoiceDetailQuery = (id: string) =>
  queryOptions({
    queryKey: invoiceKeys.detail(id),
    queryFn: ({ signal }) => fetchInvoice(id, signal),
  });

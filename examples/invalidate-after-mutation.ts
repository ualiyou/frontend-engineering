// invalidate-after-mutation.ts
//
// Precise, prefix-scoped invalidation after a write. Invalidate exactly what the
// change can affect — every list (the item may move between filters) and the one
// detail — never the whole cache. Targets come from the key factory.
//
// Illustrates: Cache Invalidation.

import { QueryClient } from '@tanstack/react-query';

interface InvoiceFilters {
  status?: 'draft' | 'sent' | 'paid';
  customerId?: string;
}

const invoiceKeys = {
  all: ['invoices'] as const,
  lists: () => [...invoiceKeys.all, 'list'] as const,
  list: (filters: InvoiceFilters) => [...invoiceKeys.lists(), filters] as const,
  details: () => [...invoiceKeys.all, 'detail'] as const,
  detail: (id: string) => [...invoiceKeys.details(), id] as const,
};

// After an edit: refresh every filtered list and the one changed detail. Awaited
// so a caller can keep a pending state until the data is genuinely current.
export async function invalidateAfterInvoiceEdit(
  queryClient: QueryClient,
  changedId: string,
): Promise<void> {
  await Promise.all([
    queryClient.invalidateQueries({ queryKey: invoiceKeys.lists() }),
    queryClient.invalidateQueries({ queryKey: invoiceKeys.detail(changedId) }),
  ]);
}

// After a delete: the detail no longer exists, so remove it outright (a refetch
// would 404), then refresh the lists so the row disappears everywhere.
export async function reconcileAfterInvoiceDelete(
  queryClient: QueryClient,
  deletedId: string,
): Promise<void> {
  queryClient.removeQueries({ queryKey: invoiceKeys.detail(deletedId) });
  await queryClient.invalidateQueries({ queryKey: invoiceKeys.lists() });
}

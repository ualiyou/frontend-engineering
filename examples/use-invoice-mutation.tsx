// use-invoice-mutation.tsx
//
// A write through useMutation with the full lifecycle handled: isPending gates
// the submit control (no double submit), the error is a rendered state (not
// swallowed), and onSettled reconciles the cache whether the write succeeded or
// failed.
//
// Illustrates: Mutation Lifecycle.

import { useMutation, useQueryClient } from '@tanstack/react-query';

const invoiceKeys = {
  all: ['invoices'] as const,
  lists: () => [...invoiceKeys.all, 'list'] as const,
};

interface InvoiceDraft {
  customer: string;
  amountCents: number;
}

interface Invoice extends InvoiceDraft {
  id: string;
  status: 'draft' | 'sent' | 'paid';
}

async function createInvoice(draft: InvoiceDraft): Promise<Invoice> {
  const response = await fetch('/api/invoices', {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify(draft),
  });
  if (response.status === 422) {
    const problem = (await response.json()) as { message: string };
    throw new Error(problem.message);
  }
  if (!response.ok) {
    throw new Error(`Failed to create invoice (${response.status})`);
  }
  return (await response.json()) as Invoice;
}

export function CreateInvoiceButton({
  draft,
  onCreated,
}: {
  draft: InvoiceDraft;
  onCreated: (invoice: Invoice) => void;
}) {
  const queryClient = useQueryClient();
  const mutation = useMutation({
    mutationFn: createInvoice,
    onSuccess: (invoice) => onCreated(invoice),
    onSettled: () => queryClient.invalidateQueries({ queryKey: invoiceKeys.lists() }),
  });

  return (
    <div>
      <button
        type="button"
        onClick={() => mutation.mutate(draft)}
        disabled={mutation.isPending}
      >
        {mutation.isPending ? 'Creating…' : 'Create invoice'}
      </button>
      {mutation.isError && <p role="alert">{mutation.error.message}</p>}
    </div>
  );
}

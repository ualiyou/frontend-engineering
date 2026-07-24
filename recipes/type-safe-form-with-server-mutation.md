# Recipe: Type-Safe Form with Server Mutation

An end-to-end create form where one Zod schema drives client validation, the TypeScript types, and the server check; React Hook Form manages state; TanStack Query runs the write; and server-side validation errors map back onto the right fields, accessibly.

This recipe applies [Schema Validation](../docs/03-application-architecture/forms-validation/schema-validation.md), [Schema-Inferred Types](../docs/03-application-architecture/forms-validation/schema-inferred-types.md), [Error Messaging](../docs/03-application-architecture/forms-validation/error-messaging.md), [Form Libraries & State Models](../docs/03-application-architecture/forms-validation/form-libraries-and-state-models.md), and [Mutation Lifecycle](../docs/03-application-architecture/data-server-state/mutation-lifecycle.md). Those articles explain *why*; this recipe is the *how*, wired together.

## Stack

React 19, TypeScript 5.x, Vite, TanStack Query v5, React Hook Form, Zod, Tailwind CSS v4, pnpm.

## The problem it solves

A create form has three hard requirements that are usually met inconsistently: the same rules must hold on the client and the server, the write must not double-submit or swallow errors, and validation failures — including ones only the server can detect, like a duplicate email — must land on the correct field and be announced to assistive tech. Doing each ad hoc produces drift and inaccessible errors. This recipe wires them from one schema.

## File structure

```text
features/create-invoice/
├─ invoice-schema.ts        # the one schema; client + server import it
├─ use-create-invoice.ts    # the mutation hook (lifecycle + server-error mapping)
├─ CreateInvoiceForm.tsx    # RHF form with accessible, associated errors
└─ create-invoice.test.tsx  # (see Testing)
```

## 1. The shared schema

One schema is the source of truth for rules, messages, and types. The server imports the same file.

```ts
// invoice-schema.ts
import { z } from 'zod';

export const invoiceSchema = z.object({
  customer: z.string().min(1, 'Customer is required'),
  // Number input arrives as a string; coerce at the boundary.
  amountCents: z.coerce.number().int().positive('Amount must be greater than zero'),
  dueDate: z.string().date('Enter a valid date'),
});

// Two ends because of the coercion: input for the form, output for the handler.
export type InvoiceInput = z.input<typeof invoiceSchema>;
export type InvoiceOutput = z.output<typeof invoiceSchema>;

// The shape the server returns for a validation failure — a list of field issues.
export interface ServerValidationError {
  message: string;
  issues: { path: (string | number)[]; message: string }[];
}
```

## 2. The mutation hook

The hook owns the lifecycle and translates a server 422 into field errors the form can display. It takes a `setError` callback so it stays UI-agnostic.

```ts
// use-create-invoice.ts
import { useMutation, useQueryClient } from '@tanstack/react-query';
import type { InvoiceOutput, ServerValidationError } from './invoice-schema';

const invoiceKeys = {
  all: ['invoices'] as const,
  lists: () => [...invoiceKeys.all, 'list'] as const,
};

interface Invoice extends InvoiceOutput {
  id: string;
  status: 'draft' | 'sent' | 'paid';
}

// Thrown for an expected, field-level server rejection so onError can map it.
class InvoiceValidationError extends Error {
  constructor(public readonly server: ServerValidationError) {
    super(server.message);
    this.name = 'InvoiceValidationError';
  }
}

async function createInvoice(input: InvoiceOutput): Promise<Invoice> {
  const response = await fetch('/api/invoices', {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify(input),
  });

  if (response.status === 422) {
    throw new InvoiceValidationError((await response.json()) as ServerValidationError);
  }
  if (!response.ok) {
    throw new Error(`Failed to create invoice (${response.status})`);
  }
  return (await response.json()) as Invoice;
}

export function useCreateInvoice(options: {
  onCreated: (invoice: Invoice) => void;
  // Maps a server field issue back onto the form; wired to RHF's setError.
  setFieldError: (field: keyof InvoiceOutput, message: string) => void;
}) {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: createInvoice,
    onSuccess: (invoice) => options.onCreated(invoice),
    onError: (error) => {
      if (error instanceof InvoiceValidationError) {
        // Expected: place each server issue on its field.
        for (const issue of error.server.issues) {
          const field = issue.path[0];
          if (typeof field === 'string') {
            options.setFieldError(field as keyof InvoiceOutput, issue.message);
          }
        }
      }
      // Unexpected errors fall through to the form's root error UI.
    },
    onSettled: () => queryClient.invalidateQueries({ queryKey: invoiceKeys.lists() }),
  });
}
```

## 3. The form

React Hook Form with `zodResolver`, three-generic typing for the transform, accessible field errors, focus-to-first-error, and a root error region for unexpected failures.

```tsx
// CreateInvoiceForm.tsx
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { invoiceSchema, type InvoiceInput, type InvoiceOutput } from './invoice-schema';
import { useCreateInvoice } from './use-create-invoice';

export function CreateInvoiceForm({ onCreated }: { onCreated: (id: string) => void }) {
  const {
    register,
    handleSubmit,
    setError,
    setFocus,
    formState: { errors, isSubmitting },
  } = useForm<InvoiceInput, unknown, InvoiceOutput>({
    resolver: zodResolver(invoiceSchema),
    defaultValues: { customer: '', amountCents: '', dueDate: '' },
  });

  const mutation = useCreateInvoice({
    onCreated: (invoice) => onCreated(invoice.id),
    setFieldError: (field, message) => setError(field, { message }),
  });

  return (
    <form
      noValidate
      className="flex flex-col gap-4"
      onSubmit={handleSubmit(
        (values) => mutation.mutate(values),
        (fieldErrors) => {
          const first = Object.keys(fieldErrors)[0] as keyof InvoiceOutput | undefined;
          if (first) setFocus(first);
        },
      )}
    >
      {/* Root error for unexpected failures (network, 500). */}
      {mutation.isError && !mutation.error.name?.includes('Validation') && (
        <p role="alert" className="text-red-600">
          Something went wrong. Please try again.
        </p>
      )}

      <div className="flex flex-col gap-1">
        <label htmlFor="customer" className="font-medium">Customer</label>
        <input
          id="customer"
          className="rounded border px-3 py-2 aria-[invalid=true]:border-red-500"
          aria-invalid={errors.customer ? true : undefined}
          aria-describedby={errors.customer ? 'customer-error' : undefined}
          {...register('customer')}
        />
        {errors.customer && (
          <span id="customer-error" role="alert" className="text-sm text-red-600">
            {errors.customer.message}
          </span>
        )}
      </div>

      <div className="flex flex-col gap-1">
        <label htmlFor="amountCents" className="font-medium">Amount (cents)</label>
        <input
          id="amountCents"
          inputMode="numeric"
          className="rounded border px-3 py-2 aria-[invalid=true]:border-red-500"
          aria-invalid={errors.amountCents ? true : undefined}
          aria-describedby={errors.amountCents ? 'amountCents-error' : undefined}
          {...register('amountCents')}
        />
        {errors.amountCents && (
          <span id="amountCents-error" role="alert" className="text-sm text-red-600">
            {errors.amountCents.message}
          </span>
        )}
      </div>

      <div className="flex flex-col gap-1">
        <label htmlFor="dueDate" className="font-medium">Due date</label>
        <input
          id="dueDate"
          type="date"
          className="rounded border px-3 py-2 aria-[invalid=true]:border-red-500"
          aria-invalid={errors.dueDate ? true : undefined}
          aria-describedby={errors.dueDate ? 'dueDate-error' : undefined}
          {...register('dueDate')}
        />
        {errors.dueDate && (
          <span id="dueDate-error" role="alert" className="text-sm text-red-600">
            {errors.dueDate.message}
          </span>
        )}
      </div>

      <button
        type="submit"
        disabled={isSubmitting}
        className="rounded bg-blue-600 px-4 py-2 font-medium text-white disabled:opacity-50"
      >
        {isSubmitting ? 'Creating…' : 'Create invoice'}
      </button>
    </form>
  );
}
```

## 4. The server (same schema)

```ts
// server: create-invoice-handler.ts
import { invoiceSchema } from '../features/create-invoice/invoice-schema';

export async function createInvoiceHandler(rawBody: unknown): Promise<Response> {
  const result = invoiceSchema.safeParse(rawBody);
  if (!result.success) {
    // Same issue shape the client maps onto fields.
    return Response.json(
      {
        message: 'Validation failed',
        issues: result.error.issues.map((issue) => ({
          path: issue.path,
          message: issue.message,
        })),
      },
      { status: 422 },
    );
  }
  const invoice = await persistInvoice(result.data);
  return Response.json(invoice, { status: 201 });
}

declare function persistInvoice(input: unknown): Promise<{ id: string }>;
```

## Testing

Test the seams, not the library: (1) client validation blocks submit and shows the message; (2) a mocked 422 maps its issues onto the right fields and moves focus; (3) a success calls `onCreated` and invalidates the list. Use Testing Library with a mocked fetch and a `QueryClientProvider` with `retry: false`.

## Why this holds up

The rules live once, in `invoice-schema.ts`, so the client and server can't disagree and the types can't drift. The mutation gates double-submits (`isPending`), never swallows errors, and reconciles the list (`onSettled`). Server-only failures land on their fields through the same issue shape the client already renders, and every error is associated and announced. Adding a field is a one-line schema change that flows to validation, types, the server, and the form.

## Related

- Articles: [Schema Validation](../docs/03-application-architecture/forms-validation/schema-validation.md), [Mutation Lifecycle](../docs/03-application-architecture/data-server-state/mutation-lifecycle.md), [Error Messaging](../docs/03-application-architecture/forms-validation/error-messaging.md).
- Examples: [Zod resolver form](../examples/zod-resolver-form.tsx), [Invoice mutation hook](../examples/use-invoice-mutation.tsx), [Accessible field error](../examples/accessible-field-error.tsx).

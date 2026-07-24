# Anti-Pattern: Client-Only Validation

**Domain:** [Forms & Validation](./README.md#forms-validation) · **The right way:** [Schema Validation](../docs/03-application-architecture/forms-validation/schema-validation.md)

Client-side validation is a user-experience affordance: it gives fast feedback and stops obvious mistakes before a round trip. It is *not* a security or integrity boundary. This anti-pattern treats the client check as sufficient and lets the server persist whatever it receives.

## Symptom

The form validates thoroughly, but the server handler reads the request body and writes it without re-validating.

```ts
// ❌ The server trusts the client. Anyone bypassing the form (curl, a script,
// a modified client) can write invalid or malicious data.
export async function createInvoiceHandler(request: Request): Promise<Response> {
  const body = await request.json();
  const invoice = await db.invoices.insert(body); // no validation
  return Response.json(invoice, { status: 201 });
}
```

## Why it fails

Client code runs on the user's machine and can be skipped entirely. The validation in the form protects nobody who doesn't use the form: a direct API call, a replayed request, a browser with JavaScript disabled, or a malicious actor all reach the server with unvalidated input. The server is the only place validation is enforceable, because it's the only place you control. Relying on the client means your real constraints — the ones that keep the database consistent and safe — are optional.

It also drifts. When the server *does* eventually add its own validation, it's usually written independently from the client's rules, so the two disagree: the client accepts a value the server rejects (confusing 400s after a clean submit) or vice versa. Two hand-maintained rule sets for the same data guarantee divergence.

## Fix

Validate on the server with the *same schema* the client uses. Share one schema module; the client resolver and the server handler both consume it, so the rules are identical by construction.

```ts
// ✅ Same schema as the form. The trust boundary enforces the real rules.
import { invoiceSchema } from '../shared/invoice-schema';

export async function createInvoiceHandler(request: Request): Promise<Response> {
  const result = invoiceSchema.safeParse(await request.json());
  if (!result.success) {
    return Response.json(
      { message: 'Validation failed', issues: result.error.issues },
      { status: 422 },
    );
  }
  const invoice = await db.invoices.insert(result.data); // result.data is typed + valid
  return Response.json(invoice, { status: 201 });
}
```

Return the issues in a shape the client already understands so server-detected failures (a duplicate email, a stale record) can map back onto the right fields. Keep the client validation too — it's still the fast feedback layer — but treat the server as the authority.

## See also

- Canonical article: [Schema Validation](../docs/03-application-architecture/forms-validation/schema-validation.md)
- Recipe: [Type-safe form with server mutation](../recipes/type-safe-form-with-server-mutation.md)
- Example: [Zod resolver form](../examples/zod-resolver-form.tsx)

// schema-inferred-types.ts
//
// Deriving types from a schema instead of hand-writing them. With no transform,
// z.infer is enough. With a transform (coercion, default), the input and output
// types diverge and you need z.input / z.output to type each end of a form.
//
// Illustrates: Schema-Inferred Types.

import { z } from 'zod';

// No transforms: input and output coincide, so z.infer alone is correct.
export const contactSchema = z.object({
  name: z.string().min(1, 'Required'),
  email: z.string().email('Enter a valid email'),
});
export type ContactValues = z.infer<typeof contactSchema>;
// ContactValues = { name: string; email: string }

// Transforms: coercion and a default make the two ends differ.
export const donationSchema = z.object({
  amount: z.coerce.number().positive('Enter an amount greater than zero'),
  tier: z.enum(['bronze', 'silver', 'gold']).default('bronze'),
});

// What you pass IN: amount is a raw string|number, tier can be omitted.
export type DonationInput = z.input<typeof donationSchema>;
// What comes OUT after validation: amount is a number, tier is present.
export type DonationOutput = z.output<typeof donationSchema>; // === z.infer

// Variant types come from schema methods, then inference — never a hand-written
// parallel type.
export const donationPatchSchema = donationSchema.partial();
export type DonationPatchOutput = z.output<typeof donationPatchSchema>;

// Runtime side of the same schema: safeParse returns typed data or issues.
export function parseDonation(raw: unknown):
  | { ok: true; value: DonationOutput }
  | { ok: false; issues: z.ZodIssue[] } {
  const result = donationSchema.safeParse(raw);
  return result.success
    ? { ok: true, value: result.data }
    : { ok: false, issues: result.error.issues };
}

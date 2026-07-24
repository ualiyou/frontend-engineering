// zod-resolver-form.tsx
//
// One Zod schema wired into React Hook Form via zodResolver. The schema owns the
// rules and messages; the resolver maps each issue to its field by path; the
// form's type is inferred from the schema so it can't drift.
//
// Illustrates: Schema Validation.

import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';

// One declaration: rules, messages, and cross-field check all live here.
const signupSchema = z
  .object({
    email: z.string().email('Enter a valid email'),
    password: z.string().min(8, 'At least 8 characters'),
    confirm: z.string(),
  })
  .refine((values) => values.password === values.confirm, {
    message: 'Passwords do not match',
    path: ['confirm'],
  });

type SignupValues = z.infer<typeof signupSchema>;

export function SignupForm({ onSignup }: { onSignup: (values: SignupValues) => Promise<void> }) {
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<SignupValues>({ resolver: zodResolver(signupSchema) });

  return (
    <form onSubmit={handleSubmit(onSignup)} noValidate>
      <label htmlFor="email">Email</label>
      <input
        id="email"
        type="email"
        aria-invalid={errors.email ? true : undefined}
        aria-describedby={errors.email ? 'email-error' : undefined}
        {...register('email')}
      />
      {errors.email && <span id="email-error" role="alert">{errors.email.message}</span>}

      <label htmlFor="password">Password</label>
      <input
        id="password"
        type="password"
        aria-invalid={errors.password ? true : undefined}
        aria-describedby={errors.password ? 'password-error' : undefined}
        {...register('password')}
      />
      {errors.password && (
        <span id="password-error" role="alert">{errors.password.message}</span>
      )}

      <label htmlFor="confirm">Confirm password</label>
      <input
        id="confirm"
        type="password"
        aria-invalid={errors.confirm ? true : undefined}
        aria-describedby={errors.confirm ? 'confirm-error' : undefined}
        {...register('confirm')}
      />
      {errors.confirm && (
        <span id="confirm-error" role="alert">{errors.confirm.message}</span>
      )}

      <button type="submit" disabled={isSubmitting}>Sign up</button>
    </form>
  );
}

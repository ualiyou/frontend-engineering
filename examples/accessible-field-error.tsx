// accessible-field-error.tsx
//
// A field component that exposes a validation error on all four channels: visual
// text, state (aria-invalid), association (aria-describedby → message id), and
// announcement (role="alert"). The form moves focus to the first error on a
// failed submit. Every form built from this component is accessible by default.
//
// Illustrates: Error Messaging.

import { useForm } from 'react-hook-form';
import type { FieldError, UseFormRegisterReturn } from 'react-hook-form';

function FormField({
  name,
  label,
  type = 'text',
  error,
  registration,
}: {
  name: string;
  label: string;
  type?: string;
  error?: FieldError;
  registration: UseFormRegisterReturn;
}) {
  const errorId = `${name}-error`;
  return (
    <div>
      <label htmlFor={name}>{label}</label>
      <input
        id={name}
        type={type}
        aria-invalid={error ? true : undefined}
        aria-describedby={error ? errorId : undefined}
        {...registration}
      />
      {error && (
        <span id={errorId} role="alert">
          {error.message}
        </span>
      )}
    </div>
  );
}

interface SignInValues {
  email: string;
  password: string;
}

export function SignInForm({ onSignIn }: { onSignIn: (values: SignInValues) => Promise<void> }) {
  const {
    register,
    handleSubmit,
    setFocus,
    formState: { errors, isSubmitting },
  } = useForm<SignInValues>();

  return (
    <form
      noValidate
      onSubmit={handleSubmit(onSignIn, (fieldErrors) => {
        // Send the user straight to the first invalid field.
        const first = Object.keys(fieldErrors)[0] as keyof SignInValues | undefined;
        if (first) setFocus(first);
      })}
    >
      <FormField
        name="email"
        label="Email"
        type="email"
        error={errors.email}
        registration={register('email', { required: 'Enter your email' })}
      />
      <FormField
        name="password"
        label="Password"
        type="password"
        error={errors.password}
        registration={register('password', { required: 'Enter your password' })}
      />
      <button type="submit" disabled={isSubmitting}>Sign in</button>
    </form>
  );
}

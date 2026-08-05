# Anti-Pattern: Inaccessible Error Messaging

**Domain:** [Forms & Validation](./#forms-validation) · **The right way:** [Error Messaging](../docs/03-application-architecture/forms-validation/error-messaging.md)

The validation is correct and the errors are shown — as a red border and a loose message. But nothing ties the message to its field, nothing announces it, and focus never moves. To a screen-reader or keyboard user, the error is invisible, and the form is a dead end.

## Symptom

Error text rendered near a field with no `aria-invalid`, no `aria-describedby`, no announcement, and no focus management.

```tsx
// ❌ Visible only to sighted mouse users. A screen reader never learns the field
// is invalid, and focus stays on the submit button after a failed submit.
<input id="email" {...register('email', { required: 'Required' })} />
{errors.email && <span style={{ color: 'red' }}>{errors.email.message}</span>}
```

## Why it fails

An error must be exposed on every channel a user might rely on, not just the visual one. Color communicates nothing to someone who can't perceive it or who uses a screen reader. A message that exists in the DOM but isn't programmatically associated with its field isn't read when the field gets focus. A message that appears after submit, while focus is on the button, isn't announced at all. And leaving focus on the button forces keyboard users to hunt blindly for a problem they can't see. The form is fully functional for the developer testing it visually and completely broken for others — which is why this ships so often and fails WCAG 3.3.1 (Error Identification, Level A).

## Fix

Expose the error on all four channels: state, association, announcement, and focus.

```tsx
// ✅ aria-invalid (state), aria-describedby → id (association), role="alert"
// (announcement), and setFocus on failed submit (navigation).
<input
  id="email"
  type="email"
  aria-invalid={errors.email ? true : undefined}
  aria-describedby={errors.email ? 'email-error' : undefined}
  {...register('email')}
/>
{errors.email && <span id="email-error" role="alert">{errors.email.message}</span>}
```

```tsx
// On a failed submit, move focus to the first invalid field (or an error summary).
handleSubmit(onValid, (fieldErrors) => {
  const first = Object.keys(fieldErrors)[0] as keyof Values | undefined;
  if (first) setFocus(first);
});
```

Write messages as actionable text ("Enter a valid email", not "Invalid"), never conveyed by color or icon alone. Build this into a shared field component so every form is accessible by construction rather than field by field.

## See also

- Canonical article: [Error Messaging](../docs/03-application-architecture/forms-validation/error-messaging.md)
- Example: [Accessible field error](../examples/accessible-field-error.tsx)
- Related domain: [Accessibility](../docs/04-interface-engineering/accessibility/)

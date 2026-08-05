# Anti-Pattern: Validation Re-Render Storm

**Domain:** [Forms & Validation](./#forms-validation) · **The right way:** [Form Libraries & State Models](../docs/03-application-architecture/forms-validation/form-libraries-and-state-models.md)

A large form re-renders every field (and re-runs validation on all of them) on every keystroke, because its values live in controlled React state or are mirrored there. Typing lags, and the reflex fix — memoizing every field — treats the symptom, not the model.

## Symptom

Every field is controlled with `useState`, or an uncontrolled library's values are copied into `useState` / read with a top-level `watch()`.

```tsx
// ❌ Top-level watch() subscribes to every field, so each keystroke re-renders
// the whole form and re-validates everything.
function SettingsForm() {
  const { register, watch } = useForm();
  const values = watch(); // subscribes to all fields
  return (
    <form>
      <input {...register('displayName')} />
      {/* forty more fields, all re-rendering on every character typed */}
      <Preview values={values} />
    </form>
  );
}
```

## Why it fails

The controlled model makes React the source of truth for each value, so every change is a `setState` that re-renders — fine for one input, quadratically painful across dozens. When validation runs on change, each keystroke also re-validates every field. The profiler shows hundreds of renders per second of typing on a big form, and the input visibly lags. Reaching for `React.memo` and `useMemo` on every field adds complexity to fight a cost the state model created; it never fully wins, because the re-render source is structural.

Adopting React Hook Form and then mirroring its values into `useState`, or reading them with a top-level `watch()`, reintroduces exactly this cost — it's controlled-per-keystroke behavior with extra indirection, slower than the library's intended path.

## Fix

Use the uncontrolled model with the grain of the library: `register` for the fast path (no re-render while typing), and scope live-value subscriptions to the smallest component that needs them.

```tsx
// ✅ register keeps typing off the render path; the one live-value consumer is
// isolated so only it re-renders.
import { useForm, useWatch, type Control } from 'react-hook-form';

function NamePreview({ control }: { control: Control<Values> }) {
  const displayName = useWatch({ control, name: 'displayName' });
  return <p aria-live="polite">{displayName}</p>;
}

function SettingsForm() {
  const { register, control } = useForm<Values>();
  return (
    <form>
      <input {...register('displayName')} />
      {/* many more register()ed fields — none re-render on keystroke */}
      <NamePreview control={control} />
    </form>
  );
}
```

Validate on blur or submit (`mode: 'onBlur'`) rather than on every change, and never mirror form values into separate `useState`. The form then scales to dozens of fields without per-field memoization.

## See also

- Canonical article: [Form Libraries & State Models](../docs/03-application-architecture/forms-validation/form-libraries-and-state-models.md)
- Example: [Register vs Controller](../examples/rhf-register-vs-controller.tsx)

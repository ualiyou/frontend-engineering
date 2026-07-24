// rhf-register-vs-controller.tsx
//
// The two ways to wire a field in React Hook Form. `register` is the uncontrolled
// fast path — native inputs, no re-render per keystroke. `Controller` bridges a
// component that must be controlled (here a custom select), deliberately paying
// controlled cost for that one field.
//
// Illustrates: Form Libraries & State Models.

import { useForm, Controller, type Control } from 'react-hook-form';

interface OrderValues {
  reference: string; // native input — register
  priority: 'low' | 'normal' | 'high'; // custom control — Controller
}

// A third-party-style component that only accepts value/onChange (no ref), so it
// cannot be `register`ed and needs the Controller bridge.
function PrioritySelect({
  value,
  onChange,
}: {
  value: OrderValues['priority'];
  onChange: (value: OrderValues['priority']) => void;
}) {
  const options: OrderValues['priority'][] = ['low', 'normal', 'high'];
  return (
    <div role="radiogroup" aria-label="Priority">
      {options.map((option) => (
        <button
          key={option}
          type="button"
          role="radio"
          aria-checked={value === option}
          onClick={() => onChange(option)}
        >
          {option}
        </button>
      ))}
    </div>
  );
}

function PriorityField({ control }: { control: Control<OrderValues> }) {
  return (
    <Controller
      control={control}
      name="priority"
      render={({ field }) => (
        <PrioritySelect value={field.value} onChange={field.onChange} />
      )}
    />
  );
}

export function OrderForm() {
  const {
    register,
    handleSubmit,
    control,
    formState: { errors, isSubmitting },
  } = useForm<OrderValues>({ defaultValues: { reference: '', priority: 'normal' } });

  return (
    <form onSubmit={handleSubmit((values) => submitOrder(values))}>
      {/* Fast path: native input via register, no re-render while typing. */}
      <label htmlFor="reference">Reference</label>
      <input id="reference" {...register('reference', { required: 'Required' })} />
      {errors.reference && <span role="alert">{errors.reference.message}</span>}

      {/* Controlled bridge: this one field re-renders on change, by design. */}
      <PriorityField control={control} />

      <button type="submit" disabled={isSubmitting}>Create order</button>
    </form>
  );
}

declare function submitOrder(values: OrderValues): void;

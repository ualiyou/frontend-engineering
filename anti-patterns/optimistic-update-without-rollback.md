# Anti-Pattern: Optimistic Update Without Rollback

**Domain:** [Data & Server State](./README.md#data-server-state) · **The right way:** [Optimistic Updates](../docs/03-application-architecture/data-server-state/optimistic-updates.md)

An optimistic update writes an expected result into the cache before the server confirms it, so the UI feels instant. This anti-pattern keeps the instant write but omits the rollback — so when the write fails, the UI keeps showing a change that never happened.

## Symptom

`onMutate` applies a cache change, but there is no `onError` that restores the prior value, and often no `cancelQueries` either.

```tsx
// ❌ Instant, but nothing undoes the change when the server rejects it.
useMutation({
  mutationFn: toggleStar,
  onMutate: (taskId: string) => {
    queryClient.setQueryData(['tasks', 'detail', taskId], (old: Task | undefined) =>
      old ? { ...old, starred: !old.starred } : old,
    );
  },
});
```

## Why it fails

The optimistic write is a bet that the mutation will succeed. When the bet loses — the user is briefly offline, the server returns 4xx/5xx, a validation rule rejects the change — nothing reverts the cache. The UI shows the user's action as successful, then a later background refetch silently overwrites it with the server's real value. The result is the maddening "flaky connection randomly loses my taps" bug: actions appear to work and then vanish, with no error and no explanation. Because you moved the correctness guarantee off the server and into your code, omitting the rollback means the guarantee simply doesn't exist.

Skipping `cancelQueries` compounds it: a refetch already in flight can resolve *after* your optimistic write and clobber it immediately, causing a visible flicker even on the success path.

## Fix

Implement the full cycle: cancel outgoing refetches, snapshot the previous value, apply the optimistic change, restore the snapshot on error, and reconcile on settle.

```tsx
// ✅ Snapshot enables a real rollback; cancel closes the overwrite race.
useMutation({
  mutationFn: toggleStar,
  onMutate: async (taskId: string) => {
    await queryClient.cancelQueries({ queryKey: ['tasks', 'detail', taskId] });
    const previous = queryClient.getQueryData<Task>(['tasks', 'detail', taskId]);
    queryClient.setQueryData<Task>(['tasks', 'detail', taskId], (old) =>
      old ? { ...old, starred: !old.starred } : old,
    );
    return { previous };
  },
  onError: (_error, taskId, context) => {
    if (context?.previous) {
      queryClient.setQueryData(['tasks', 'detail', taskId], context.previous);
    }
  },
  onSettled: (_data, _error, taskId) =>
    queryClient.invalidateQueries({ queryKey: ['tasks', 'detail', taskId] }),
});
```

Make the rollback visible with an accessible message so the reversion reads as a handled failure, not a glitch. And reserve optimism for frequent, low-stakes, near-always-successful writes; for rare or high-stakes writes, prefer the plain pending-then-invalidate flow.

## See also

- Canonical article: [Optimistic Updates](../docs/03-application-architecture/data-server-state/optimistic-updates.md)
- Recipe: [Optimistic list mutation with rollback](../recipes/optimistic-list-mutation.md)
- Example: [Optimistic update with rollback](../examples/optimistic-update-with-rollback.tsx)

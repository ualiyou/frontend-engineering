# Recipe: Optimistic List Mutation with Rollback

A list where items can be toggled and reordered with zero perceived latency, using optimistic cache writes that roll back on failure and reconcile with the server on settle.

This recipe applies [Optimistic Updates](../docs/03-application-architecture/data-server-state/optimistic-updates.md), [Mutation Lifecycle](../docs/03-application-architecture/data-server-state/mutation-lifecycle.md), [Cache Invalidation](../docs/03-application-architecture/data-server-state/cache-invalidation.md), and [Cache Keys & Query Identity](../docs/03-application-architecture/data-server-state/cache-keys-and-query-identity.md).

## Stack

React 19, TypeScript 5.x, Vite, TanStack Query v5, Tailwind CSS v4, pnpm.

## The problem it solves

Toggling an item in a list should feel instant, not wait a round trip per tap. But an optimistic write that isn't rolled back leaves the UI showing a change the server rejected — the "flaky connection silently loses my taps" bug. This recipe implements the full cancel → snapshot → write → rollback → reconcile cycle on a list cache, with an accessible failure message when a rollback happens.

## File structure

```text
features/task-list/
├─ task-keys.ts            # the key factory
├─ use-toggle-task.ts      # optimistic toggle mutation on the list entry
├─ TaskList.tsx            # the list UI + failure announcer
└─ task-list.test.tsx
```

## 1. Keys

```ts
// task-keys.ts
export interface TaskFilters {
  projectId: string;
  done?: boolean;
}

export const taskKeys = {
  all: ['tasks'] as const,
  lists: () => [...taskKeys.all, 'list'] as const,
  list: (filters: TaskFilters) => [...taskKeys.lists(), filters] as const,
};

export interface Task {
  id: string;
  title: string;
  done: boolean;
}
```

## 2. The optimistic mutation

The write updates one item inside the cached list array. `onMutate` cancels, snapshots the whole list, and flips the item; `onError` restores the snapshot and reports the failure; `onSettled` invalidates to pull the server's truth.

```ts
// use-toggle-task.ts
import { useMutation, useQueryClient } from '@tanstack/react-query';
import { taskKeys, type Task, type TaskFilters } from './task-keys';

async function toggleTaskDone(input: { id: string; done: boolean }): Promise<Task> {
  const response = await fetch(`/api/tasks/${input.id}`, {
    method: 'PATCH',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify({ done: input.done }),
  });
  if (!response.ok) {
    throw new Error(`Failed to update task (${response.status})`);
  }
  return (await response.json()) as Task;
}

export function useToggleTask(filters: TaskFilters, onFailure: (message: string) => void) {
  const queryClient = useQueryClient();
  const listKey = taskKeys.list(filters);

  return useMutation({
    mutationFn: toggleTaskDone,
    onMutate: async ({ id, done }) => {
      await queryClient.cancelQueries({ queryKey: listKey });
      const previous = queryClient.getQueryData<Task[]>(listKey);
      queryClient.setQueryData<Task[]>(listKey, (old) =>
        old?.map((task) => (task.id === id ? { ...task, done } : task)),
      );
      return { previous };
    },
    onError: (_error, _variables, context) => {
      if (context?.previous) {
        queryClient.setQueryData(listKey, context.previous);
      }
      onFailure('Couldn’t update the task — please try again.');
    },
    onSettled: () => {
      void queryClient.invalidateQueries({ queryKey: taskKeys.lists() });
    },
  });
}
```

## 3. The list UI

The checkbox reflects the (optimistic) cache immediately. A polite live region announces a rollback so a reversion reads as handled, not as a glitch.

```tsx
// TaskList.tsx
import { useState } from 'react';
import { useQuery } from '@tanstack/react-query';
import { taskKeys, type Task, type TaskFilters } from './task-keys';
import { useToggleTask } from './use-toggle-task';

export function TaskList({ filters }: { filters: TaskFilters }) {
  const [failureMessage, setFailureMessage] = useState<string | null>(null);

  const { data: tasks, isPending, isError } = useQuery({
    queryKey: taskKeys.list(filters),
    queryFn: async ({ signal }) => {
      const response = await fetch(`/api/tasks?projectId=${filters.projectId}`, { signal });
      if (!response.ok) throw new Error(`Failed to load tasks (${response.status})`);
      return (await response.json()) as Task[];
    },
  });

  const toggle = useToggleTask(filters, setFailureMessage);

  if (isPending) return <p>Loading tasks…</p>;
  if (isError) return <p role="alert">Couldn’t load tasks.</p>;

  return (
    <div>
      <p aria-live="polite" className="sr-only">{failureMessage}</p>
      <ul className="flex flex-col gap-2">
        {tasks.map((task) => (
          <li key={task.id} className="flex items-center gap-2">
            <input
              id={`task-${task.id}`}
              type="checkbox"
              checked={task.done}
              onChange={(event) =>
                toggle.mutate({ id: task.id, done: event.target.checked })
              }
            />
            <label htmlFor={`task-${task.id}`} className={task.done ? 'line-through' : ''}>
              {task.title}
            </label>
          </li>
        ))}
      </ul>
    </div>
  );
}
```

## Testing

Force the mutation to reject and assert the item reverts to its prior state and the failure message is announced. Assert that `cancelQueries` is honored by starting a background refetch and confirming it doesn't clobber the optimistic value. Run with `retry: false`.

## Pitfalls this avoids

Skipping `cancelQueries` lets an in-flight refetch overwrite the optimistic value (intermittent flicker). Skipping the `onError` restore is the [no-rollback anti-pattern](../anti-patterns/optimistic-update-without-rollback.md). Snapshotting the item instead of the list makes reconciliation miss reordering. All three are handled here.

## Related

- Articles: [Optimistic Updates](../docs/03-application-architecture/data-server-state/optimistic-updates.md), [Cache Invalidation](../docs/03-application-architecture/data-server-state/cache-invalidation.md).
- Example: [Optimistic update with rollback](../examples/optimistic-update-with-rollback.tsx).

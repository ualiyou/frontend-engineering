// optimistic-update-with-rollback.tsx
//
// The complete optimistic-update shape: cancel outgoing refetches, snapshot the
// previous value, apply the optimistic change, restore the snapshot on error, and
// reconcile with the server on settle. Removing any step reintroduces a bug.
//
// Illustrates: Optimistic Updates.

import { useMutation, useQueryClient } from '@tanstack/react-query';

const taskKeys = {
  all: ['tasks'] as const,
  detail: (id: string) => [...taskKeys.all, 'detail', id] as const,
};

interface Task {
  id: string;
  title: string;
  starred: boolean;
}

async function toggleStar(taskId: string): Promise<Task> {
  const response = await fetch(`/api/tasks/${taskId}/star`, { method: 'PATCH' });
  if (!response.ok) {
    throw new Error(`Failed to toggle star (${response.status})`);
  }
  return (await response.json()) as Task;
}

export function useToggleStar(onFailure: (message: string) => void) {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: toggleStar,
    onMutate: async (taskId) => {
      // 1. Cancel so a settling refetch can't overwrite the optimistic value.
      await queryClient.cancelQueries({ queryKey: taskKeys.detail(taskId) });
      // 2. Snapshot for rollback.
      const previous = queryClient.getQueryData<Task>(taskKeys.detail(taskId));
      // 3. Apply the optimistic change.
      queryClient.setQueryData<Task>(taskKeys.detail(taskId), (old) =>
        old ? { ...old, starred: !old.starred } : old,
      );
      return { previous };
    },
    onError: (_error, taskId, context) => {
      // Restore the snapshot: undo the change the server rejected.
      if (context?.previous) {
        queryClient.setQueryData(taskKeys.detail(taskId), context.previous);
      }
      onFailure('Couldn’t update the task — please try again.');
    },
    onSettled: (_data, _error, taskId) => {
      // Reconcile with the server's authoritative value.
      void queryClient.invalidateQueries({ queryKey: taskKeys.detail(taskId) });
    },
  });
}

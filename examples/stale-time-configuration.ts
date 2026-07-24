// stale-time-configuration.ts
//
// staleTime encodes how fast data changes. One global default removes the worst
// refetch chattiness; per-query overrides match each cache entry to its real
// volatility. gcTime (memory retention) is left at the default.
//
// Illustrates: Staleness & Revalidation.

import { QueryClient, queryOptions } from '@tanstack/react-query';

export const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      // Most screens tolerate 30s of staleness; this removes the default
      // per-focus / per-remount refetch on every query.
      staleTime: 30_000,
      gcTime: 5 * 60_000,
      retry: 2,
    },
  },
});

interface Currency {
  code: string;
  symbol: string;
}
interface Profile {
  id: string;
  displayName: string;
}
interface OrderBook {
  symbol: string;
  bids: [number, number][];
  asks: [number, number][];
}

async function getJson<T>(url: string, signal: AbortSignal): Promise<T> {
  const response = await fetch(url, { signal });
  if (!response.ok) throw new Error(`Request failed: ${url} (${response.status})`);
  return (await response.json()) as T;
}

// Reference data: changes a few times a year. Trust it for the session and
// invalidate explicitly on the rare admin edit.
export const currencyListQuery = () =>
  queryOptions({
    queryKey: ['reference', 'currencies'],
    queryFn: ({ signal }) => getJson<Currency[]>('/api/currencies', signal),
    staleTime: Infinity,
  });

// User data: changes occasionally; minutes of staleness is fine.
export const userProfileQuery = (userId: string) =>
  queryOptions({
    queryKey: ['users', 'profile', userId],
    queryFn: ({ signal }) => getJson<Profile>(`/api/users/${userId}`, signal),
    staleTime: 5 * 60_000,
  });

// Volatile data: near-real-time. Short window plus interval revalidation.
export const orderBookQuery = (symbol: string) =>
  queryOptions({
    queryKey: ['markets', 'order-book', symbol],
    queryFn: ({ signal }) => getJson<OrderBook>(`/api/markets/${symbol}/book`, signal),
    staleTime: 1_000,
    refetchInterval: 2_000,
  });

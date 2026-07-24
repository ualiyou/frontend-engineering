# Data & Server State

> Fetching, caching, and modeling server data on the client.

**Part:** [03 · Application Architecture](../) · **Priority:** Critical

## Taxonomy

Second-level groups and their articles. Each article is a standalone entry following [the template](../../../templates/article-template.md); its filename is the kebab-case form of the title.

### Fetching Strategies

- Fetch-on-Render vs Render-as-You-Fetch
- Parallel vs Waterfall Requests
- Request Deduplication
- Data Prefetching

### Server-State Cache

- Cache Keys & Query Identity
- Staleness & Revalidation
- Cache Invalidation
- Background Refetching

### Mutations

- Mutation Lifecycle
- Optimistic Updates
- Rollback & Conflict Resolution

### Large Data Sets

- Pagination
- Infinite & Cursor Loading
- List Virtualization

### Data Modeling

- Normalizing Server Responses
- Client-Side Relations
- Derived Server Data

### Resilience

- Retries & Backoff
- Loading & Error States
- Offline & Local-First Sync

_Index only. One canonical home per concept — overlapping ideas are owned here and cross-linked from other domains, never duplicated._

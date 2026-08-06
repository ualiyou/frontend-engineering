# Article Inventory

> The complete article inventory for **Frontend Engineering**, generated from the taxonomy in [`KNOWLEDGE_MAP.md`](KNOWLEDGE_MAP.md) and the per-article metadata in each domain's `graph.json`. Every article below is a leaf of the four-level hierarchy **Part → Domain → Topic → Article**.

## Summary

- **Total articles:** 651
- **Parts:** 9 · **Domains:** 35
- **Total estimated reading time:** ~8459 min (~141 h)
- **Total expected code examples:** ~1816
- **Difficulty distribution:** Foundational 169 · Intermediate 288 · Advanced 160 · Staff 34
- **Status:** 60 Published · 591 Planned.

### Column reference

| Column | Meaning |
| --- | --- |
| **Title** | Article title (the leaf concept). |
| **Slug** | Stable file name under the domain folder. |
| **Category** | Domain — the folder the article lives in. |
| **Subcategory** | Topic — the grouping within the domain. |
| **Priority** | Inherited from the Part (Critical / High / Medium). |
| **Difficulty** | Foundational / Intermediate / Advanced / Staff. |
| **Est. Reading Time** | Estimated minutes to read. |
| **Prerequisites** | Articles to read first (`Article · Domain` denotes a cross-domain prerequisite). |
| **Related Articles** | Closely connected articles. |
| **Expected Code Examples** | Planning estimate of code snippets, derived from difficulty tier (Foundational 2, Intermediate 3, Advanced 4, Staff 1; leadership topics carry fewer). |
| **Status** | Authoring status — `Published` or `Planned`. |

---

## 00 · Foundations  ·  Priority: Critical  ·  96 articles

### Browser APIs  (23 articles · ~199 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Web Storage | `web-storage.md` | Browser APIs | Storage | Critical | Foundational | 8 min | Process & Thread Architecture · The Web Platform | IndexedDB; The Cache Storage API; Cookies & Partitioned Storage; Storage Quotas & Eviction | 2 | Published |
| IndexedDB | `indexeddb.md` | Browser APIs | Storage | Critical | Foundational | 8 min | Web Storage | Web Storage; The Cache Storage API; Cookies & Partitioned Storage; Storage Quotas & Eviction | 2 | Planned |
| The Cache Storage API | `the-cache-storage-api.md` | Browser APIs | Storage | Critical | Foundational | 8 min | Web Storage | Web Storage; IndexedDB; Cookies & Partitioned Storage; Storage Quotas & Eviction | 2 | Planned |
| Cookies & Partitioned Storage | `cookies-and-partitioned-storage.md` | Browser APIs | Storage | Critical | Foundational | 11 min | Web Storage | Web Storage; IndexedDB; The Cache Storage API; Storage Quotas & Eviction | 2 | Planned |
| Storage Quotas & Eviction | `storage-quotas-and-eviction.md` | Browser APIs | Storage | Critical | Foundational | 8 min | Web Storage | Web Storage; IndexedDB; The Cache Storage API; Cookies & Partitioned Storage | 2 | Planned |
| Intersection Observer | `intersection-observer.md` | Browser APIs | Observers | Critical | Foundational | 8 min | Web Storage | Resize Observer; Mutation Observer; Performance Observer | 2 | Planned |
| Resize Observer | `resize-observer.md` | Browser APIs | Observers | Critical | Foundational | 8 min | Intersection Observer; Web Storage | Intersection Observer; Mutation Observer; Performance Observer | 2 | Planned |
| Mutation Observer | `mutation-observer.md` | Browser APIs | Observers | Critical | Foundational | 8 min | Intersection Observer; Web Storage | Intersection Observer; Resize Observer; Performance Observer | 2 | Planned |
| Performance Observer | `performance-observer.md` | Browser APIs | Observers | Critical | Foundational | 8 min | Intersection Observer; Web Storage | Intersection Observer; Resize Observer; Mutation Observer | 2 | Planned |
| Media Capture & Streams | `media-capture-and-streams.md` | Browser APIs | Device & Media | Critical | Foundational | 8 min | Intersection Observer | The Clipboard API; File & File System Access; Geolocation & Sensors; Notifications & Permissions | 2 | Planned |
| The Clipboard API | `the-clipboard-api.md` | Browser APIs | Device & Media | Critical | Foundational | 8 min | Media Capture & Streams; Intersection Observer | Media Capture & Streams; File & File System Access; Geolocation & Sensors; Notifications & Permissions | 2 | Planned |
| File & File System Access | `file-and-file-system-access.md` | Browser APIs | Device & Media | Critical | Foundational | 8 min | Media Capture & Streams; Intersection Observer | Media Capture & Streams; The Clipboard API; Geolocation & Sensors; Notifications & Permissions | 2 | Planned |
| Geolocation & Sensors | `geolocation-and-sensors.md` | Browser APIs | Device & Media | Critical | Foundational | 8 min | Media Capture & Streams; Intersection Observer | Media Capture & Streams; The Clipboard API; File & File System Access; Notifications & Permissions | 2 | Planned |
| Notifications & Permissions | `notifications-and-permissions.md` | Browser APIs | Device & Media | Critical | Foundational | 11 min | Media Capture & Streams; Intersection Observer | Media Capture & Streams; The Clipboard API; File & File System Access; Geolocation & Sensors | 2 | Planned |
| The History API | `the-history-api.md` | Browser APIs | Navigation & History | Critical | Foundational | 8 min | Media Capture & Streams | The Navigation API; URL & URLSearchParams | 2 | Planned |
| The Navigation API | `the-navigation-api.md` | Browser APIs | Navigation & History | Critical | Foundational | 8 min | The History API; Media Capture & Streams | The History API; URL & URLSearchParams | 2 | Planned |
| URL & URLSearchParams | `url-and-urlsearchparams.md` | Browser APIs | Navigation & History | Critical | Foundational | 8 min | The History API; Media Capture & Streams | The History API; The Navigation API | 2 | Planned |
| Timers & requestIdleCallback | `timers-and-requestidlecallback.md` | Browser APIs | Timing & Scheduling | Critical | Foundational | 11 min | The History API | requestAnimationFrame; The Scheduler API (postTask) | 2 | Planned |
| requestAnimationFrame | `requestanimationframe.md` | Browser APIs | Timing & Scheduling | Critical | Foundational | 8 min | Timers & requestIdleCallback; The History API | Timers & requestIdleCallback; The Scheduler API (postTask) | 2 | Planned |
| The Scheduler API (postTask) | `the-scheduler-api-posttask.md` | Browser APIs | Timing & Scheduling | Critical | Foundational | 11 min | Timers & requestIdleCallback; The History API | Timers & requestIdleCallback; requestAnimationFrame | 2 | Planned |
| Feature Detection | `feature-detection.md` | Browser APIs | Capability Model | Critical | Foundational | 8 min | Timers & requestIdleCallback | Permissions Policy; Progressive Enhancement Strategy | 2 | Planned |
| Permissions Policy | `permissions-policy.md` | Browser APIs | Capability Model | Critical | Foundational | 8 min | Feature Detection; Timers & requestIdleCallback | Feature Detection; Progressive Enhancement Strategy | 2 | Planned |
| Progressive Enhancement Strategy | `progressive-enhancement-strategy.md` | Browser APIs | Capability Model | Critical | Foundational | 11 min | Feature Detection; Timers & requestIdleCallback | Feature Detection; Permissions Policy | 2 | Planned |

### Computer Science for Frontend  (18 articles · ~156 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Trees & the DOM as a Tree | `trees-and-the-dom-as-a-tree.md` | Computer Science for Frontend | Data Structures | Critical | Foundational | 8 min | — | Graphs & Dependency Modeling; Hash Maps & Sets; Stacks & Queues; Linked & Persistent Lists | 2 | Published |
| Graphs & Dependency Modeling | `graphs-and-dependency-modeling.md` | Computer Science for Frontend | Data Structures | Critical | Foundational | 11 min | Trees & the DOM as a Tree | Trees & the DOM as a Tree; Hash Maps & Sets; Stacks & Queues; Linked & Persistent Lists | 2 | Planned |
| Hash Maps & Sets | `hash-maps-and-sets.md` | Computer Science for Frontend | Data Structures | Critical | Foundational | 8 min | Trees & the DOM as a Tree | Trees & the DOM as a Tree; Graphs & Dependency Modeling; Stacks & Queues; Linked & Persistent Lists | 2 | Planned |
| Stacks & Queues | `stacks-and-queues.md` | Computer Science for Frontend | Data Structures | Critical | Foundational | 8 min | Trees & the DOM as a Tree | Trees & the DOM as a Tree; Graphs & Dependency Modeling; Hash Maps & Sets; Linked & Persistent Lists | 2 | Planned |
| Linked & Persistent Lists | `linked-and-persistent-lists.md` | Computer Science for Frontend | Data Structures | Critical | Foundational | 8 min | Trees & the DOM as a Tree | Trees & the DOM as a Tree; Graphs & Dependency Modeling; Hash Maps & Sets; Stacks & Queues | 2 | Planned |
| Tree Diffing Algorithms | `tree-diffing-algorithms.md` | Computer Science for Frontend | Algorithms | Critical | Foundational | 8 min | Trees & the DOM as a Tree | Traversal (DFS, BFS); Searching & Filtering; Sorting & Comparators; Memoization & Dynamic Programming | 2 | Planned |
| Traversal (DFS, BFS) | `traversal-dfs-bfs.md` | Computer Science for Frontend | Algorithms | Critical | Foundational | 8 min | Tree Diffing Algorithms; Trees & the DOM as a Tree | Tree Diffing Algorithms; Searching & Filtering; Sorting & Comparators; Memoization & Dynamic Programming | 2 | Planned |
| Searching & Filtering | `searching-and-filtering.md` | Computer Science for Frontend | Algorithms | Critical | Foundational | 8 min | Tree Diffing Algorithms; Trees & the DOM as a Tree | Tree Diffing Algorithms; Traversal (DFS, BFS); Sorting & Comparators; Memoization & Dynamic Programming | 2 | Planned |
| Sorting & Comparators | `sorting-and-comparators.md` | Computer Science for Frontend | Algorithms | Critical | Foundational | 8 min | Tree Diffing Algorithms; Trees & the DOM as a Tree | Tree Diffing Algorithms; Traversal (DFS, BFS); Searching & Filtering; Memoization & Dynamic Programming | 2 | Planned |
| Memoization & Dynamic Programming | `memoization-and-dynamic-programming.md` | Computer Science for Frontend | Algorithms | Critical | Foundational | 11 min | Tree Diffing Algorithms; Trees & the DOM as a Tree | Tree Diffing Algorithms; Traversal (DFS, BFS); Searching & Filtering; Sorting & Comparators | 2 | Planned |
| Big-O for UI Operations | `big-o-for-ui-operations.md` | Computer Science for Frontend | Complexity & Cost | Critical | Foundational | 8 min | Tree Diffing Algorithms | Amortized Cost & Batching; Space vs Time Trade-offs | 2 | Planned |
| Amortized Cost & Batching | `amortized-cost-and-batching.md` | Computer Science for Frontend | Complexity & Cost | Critical | Foundational | 8 min | Big-O for UI Operations; Tree Diffing Algorithms | Big-O for UI Operations; Space vs Time Trade-offs | 2 | Planned |
| Space vs Time Trade-offs | `space-vs-time-trade-offs.md` | Computer Science for Frontend | Complexity & Cost | Critical | Foundational | 8 min | Big-O for UI Operations; Tree Diffing Algorithms | Big-O for UI Operations; Amortized Cost & Batching | 2 | Planned |
| Immutability & Structural Sharing | `immutability-and-structural-sharing.md` | Computer Science for Frontend | Modeling Change | Critical | Foundational | 11 min | Big-O for UI Operations | Finite State Machines; Statecharts & Hierarchical States | 2 | Planned |
| Finite State Machines | `finite-state-machines.md` | Computer Science for Frontend | Modeling Change | Critical | Foundational | 8 min | Immutability & Structural Sharing; Big-O for UI Operations | Immutability & Structural Sharing; Statecharts & Hierarchical States | 2 | Planned |
| Statecharts & Hierarchical States | `statecharts-and-hierarchical-states.md` | Computer Science for Frontend | Modeling Change | Critical | Foundational | 11 min | Immutability & Structural Sharing; Big-O for UI Operations | Immutability & Structural Sharing; Finite State Machines | 2 | Planned |
| Concurrency vs Parallelism | `concurrency-vs-parallelism.md` | Computer Science for Frontend | Execution Models | Critical | Foundational | 8 min | Immutability & Structural Sharing | Determinism & Idempotency | 2 | Planned |
| Determinism & Idempotency | `determinism-and-idempotency.md` | Computer Science for Frontend | Execution Models | Critical | Foundational | 8 min | Concurrency vs Parallelism; Immutability & Structural Sharing | Concurrency vs Parallelism | 2 | Planned |

### Networking & Protocols  (19 articles · ~170 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| HTTP/1.1 Semantics | `http-1-1-semantics.md` | Networking & Protocols | HTTP | Critical | Foundational | 8 min | Process & Thread Architecture · The Web Platform | HTTP/2 Multiplexing; HTTP/3 & QUIC; Methods, Status Codes & Headers | 2 | Published |
| HTTP/2 Multiplexing | `http-2-multiplexing.md` | Networking & Protocols | HTTP | Critical | Foundational | 8 min | HTTP/1.1 Semantics | HTTP/1.1 Semantics; HTTP/3 & QUIC; Methods, Status Codes & Headers | 2 | Planned |
| HTTP/3 & QUIC | `http-3-and-quic.md` | Networking & Protocols | HTTP | Critical | Foundational | 8 min | HTTP/1.1 Semantics | HTTP/1.1 Semantics; HTTP/2 Multiplexing; Methods, Status Codes & Headers | 2 | Planned |
| Methods, Status Codes & Headers | `methods-status-codes-and-headers.md` | Networking & Protocols | HTTP | Critical | Foundational | 11 min | HTTP/1.1 Semantics | HTTP/1.1 Semantics; HTTP/2 Multiplexing; HTTP/3 & QUIC | 2 | Planned |
| The HTTP Cache | `the-http-cache.md` | Networking & Protocols | Transport Caching | Critical | Foundational | 8 min | HTTP/1.1 Semantics | Cache-Control & Validators (ETag); CDN Caching Model; Vary & Cache Keys | 2 | Planned |
| Cache-Control & Validators (ETag) | `cache-control-and-validators-etag.md` | Networking & Protocols | Transport Caching | Critical | Foundational | 11 min | The HTTP Cache; HTTP/1.1 Semantics | The HTTP Cache; CDN Caching Model; Vary & Cache Keys | 2 | Planned |
| CDN Caching Model | `cdn-caching-model.md` | Networking & Protocols | Transport Caching | Critical | Foundational | 8 min | The HTTP Cache; HTTP/1.1 Semantics | The HTTP Cache; Cache-Control & Validators (ETag); Vary & Cache Keys | 2 | Planned |
| Vary & Cache Keys | `vary-and-cache-keys.md` | Networking & Protocols | Transport Caching | Critical | Foundational | 8 min | The HTTP Cache; HTTP/1.1 Semantics | The HTTP Cache; Cache-Control & Validators (ETag); CDN Caching Model | 2 | Planned |
| Connection Lifecycle (DNS, TLS) | `connection-lifecycle-dns-tls.md` | Networking & Protocols | Connection & Latency | Critical | Foundational | 11 min | The HTTP Cache | Latency, Bandwidth & RTT; Preconnect & Priority Hints | 2 | Planned |
| Latency, Bandwidth & RTT | `latency-bandwidth-and-rtt.md` | Networking & Protocols | Connection & Latency | Critical | Foundational | 8 min | Connection Lifecycle (DNS, TLS); The HTTP Cache | Connection Lifecycle (DNS, TLS); Preconnect & Priority Hints | 2 | Planned |
| Preconnect & Priority Hints | `preconnect-and-priority-hints.md` | Networking & Protocols | Connection & Latency | Critical | Foundational | 11 min | Connection Lifecycle (DNS, TLS); The HTTP Cache | Connection Lifecycle (DNS, TLS); Latency, Bandwidth & RTT | 2 | Planned |
| WebSocket | `websocket.md` | Networking & Protocols | Real-Time Protocols | Critical | Foundational | 8 min | Connection Lifecycle (DNS, TLS) | Server-Sent Events; WebRTC & Data Channels; Long Polling & Fallbacks | 2 | Planned |
| Server-Sent Events | `server-sent-events.md` | Networking & Protocols | Real-Time Protocols | Critical | Foundational | 8 min | WebSocket; Connection Lifecycle (DNS, TLS) | WebSocket; WebRTC & Data Channels; Long Polling & Fallbacks | 2 | Planned |
| WebRTC & Data Channels | `webrtc-and-data-channels.md` | Networking & Protocols | Real-Time Protocols | Critical | Foundational | 8 min | WebSocket; Connection Lifecycle (DNS, TLS) | WebSocket; Server-Sent Events; Long Polling & Fallbacks | 2 | Planned |
| Long Polling & Fallbacks | `long-polling-and-fallbacks.md` | Networking & Protocols | Real-Time Protocols | Critical | Foundational | 8 min | WebSocket; Connection Lifecycle (DNS, TLS) | WebSocket; Server-Sent Events; WebRTC & Data Channels | 2 | Planned |
| JSON & Streaming JSON | `json-and-streaming-json.md` | Networking & Protocols | Data Formats | Critical | Foundational | 8 min | WebSocket | Binary Formats (Protobuf, MessagePack); Multipart & Form Encoding; Transport Compression (gzip, brotli) | 2 | Planned |
| Binary Formats (Protobuf, MessagePack) | `binary-formats-protobuf-messagepack.md` | Networking & Protocols | Data Formats | Critical | Foundational | 11 min | JSON & Streaming JSON; WebSocket | JSON & Streaming JSON; Multipart & Form Encoding; Transport Compression (gzip, brotli) | 2 | Planned |
| Multipart & Form Encoding | `multipart-and-form-encoding.md` | Networking & Protocols | Data Formats | Critical | Foundational | 8 min | JSON & Streaming JSON; WebSocket | JSON & Streaming JSON; Binary Formats (Protobuf, MessagePack); Transport Compression (gzip, brotli) | 2 | Planned |
| Transport Compression (gzip, brotli) | `transport-compression-gzip-brotli.md` | Networking & Protocols | Data Formats | Critical | Foundational | 11 min | JSON & Streaming JSON; WebSocket | JSON & Streaming JSON; Binary Formats (Protobuf, MessagePack); Multipart & Form Encoding | 2 | Planned |

### Runtime & Execution  (18 articles · ~243 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Parsing & Bytecode | `parsing-and-bytecode.md` | Runtime & Execution | Engine Internals | Critical | Intermediate | 12 min | Process & Thread Architecture · The Web Platform | JIT Compilation & Deoptimization; Hidden Classes & Shapes; Inline Caches | 3 | Published |
| JIT Compilation & Deoptimization | `jit-compilation-and-deoptimization.md` | Runtime & Execution | Engine Internals | Critical | Intermediate | 15 min | Parsing & Bytecode | Parsing & Bytecode; Hidden Classes & Shapes; Inline Caches | 3 | Planned |
| Hidden Classes & Shapes | `hidden-classes-and-shapes.md` | Runtime & Execution | Engine Internals | Critical | Intermediate | 12 min | Parsing & Bytecode | Parsing & Bytecode; JIT Compilation & Deoptimization; Inline Caches | 3 | Planned |
| Inline Caches | `inline-caches.md` | Runtime & Execution | Engine Internals | Critical | Intermediate | 12 min | Parsing & Bytecode | Parsing & Bytecode; JIT Compilation & Deoptimization; Hidden Classes & Shapes | 3 | Planned |
| The Call Stack | `the-call-stack.md` | Runtime & Execution | Execution Context | Critical | Intermediate | 12 min | Parsing & Bytecode | Async Stack Frames & Continuations; Stack Traces & Debug Symbols | 3 | Planned |
| Async Stack Frames & Continuations | `async-stack-frames-and-continuations.md` | Runtime & Execution | Execution Context | Critical | Intermediate | 15 min | The Call Stack; Parsing & Bytecode | The Call Stack; Stack Traces & Debug Symbols | 3 | Planned |
| Stack Traces & Debug Symbols | `stack-traces-and-debug-symbols.md` | Runtime & Execution | Execution Context | Critical | Intermediate | 15 min | The Call Stack; Parsing & Bytecode | The Call Stack; Async Stack Frames & Continuations | 3 | Planned |
| The Memory Model & the Heap | `the-memory-model-and-the-heap.md` | Runtime & Execution | Memory Management | Critical | Intermediate | 15 min | The Call Stack | Garbage Collection Strategies; Retained Memory & Leak Detection; Weak References & Finalizers | 3 | Planned |
| Garbage Collection Strategies | `garbage-collection-strategies.md` | Runtime & Execution | Memory Management | Critical | Intermediate | 15 min | The Memory Model & the Heap; The Call Stack | The Memory Model & the Heap; Retained Memory & Leak Detection; Weak References & Finalizers | 3 | Planned |
| Retained Memory & Leak Detection | `retained-memory-and-leak-detection.md` | Runtime & Execution | Memory Management | Critical | Intermediate | 15 min | The Memory Model & the Heap; The Call Stack | The Memory Model & the Heap; Garbage Collection Strategies; Weak References & Finalizers | 3 | Planned |
| Weak References & Finalizers | `weak-references-and-finalizers.md` | Runtime & Execution | Memory Management | Critical | Intermediate | 15 min | The Memory Model & the Heap; The Call Stack | The Memory Model & the Heap; Garbage Collection Strategies; Retained Memory & Leak Detection | 3 | Planned |
| Web Workers | `web-workers.md` | Runtime & Execution | Multithreading | Critical | Intermediate | 12 min | The Memory Model & the Heap | Shared Workers & Message Passing; SharedArrayBuffer & Atomics; Worklets | 3 | Planned |
| Shared Workers & Message Passing | `shared-workers-and-message-passing.md` | Runtime & Execution | Multithreading | Critical | Intermediate | 15 min | Web Workers; The Memory Model & the Heap | Web Workers; SharedArrayBuffer & Atomics; Worklets | 3 | Planned |
| SharedArrayBuffer & Atomics | `sharedarraybuffer-and-atomics.md` | Runtime & Execution | Multithreading | Critical | Intermediate | 15 min | Web Workers; The Memory Model & the Heap | Web Workers; Shared Workers & Message Passing; Worklets | 3 | Planned |
| Worklets | `worklets.md` | Runtime & Execution | Multithreading | Critical | Intermediate | 12 min | Web Workers; The Memory Model & the Heap | Web Workers; Shared Workers & Message Passing; SharedArrayBuffer & Atomics | 3 | Planned |
| WebAssembly Fundamentals | `webassembly-fundamentals.md` | Runtime & Execution | Beyond JavaScript | Critical | Intermediate | 12 min | Web Workers | JS ↔ Wasm Interop; Polyglot Runtime Targets | 3 | Planned |
| JS ↔ Wasm Interop | `js-wasm-interop.md` | Runtime & Execution | Beyond JavaScript | Critical | Intermediate | 12 min | WebAssembly Fundamentals; Web Workers | WebAssembly Fundamentals; Polyglot Runtime Targets | 3 | Planned |
| Polyglot Runtime Targets | `polyglot-runtime-targets.md` | Runtime & Execution | Beyond JavaScript | Critical | Intermediate | 12 min | WebAssembly Fundamentals; Web Workers | WebAssembly Fundamentals; JS ↔ Wasm Interop | 3 | Planned |

### The Web Platform  (18 articles · ~156 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Process & Thread Architecture | `process-and-thread-architecture.md` | The Web Platform | Browser Internals | Critical | Foundational | 11 min | Trees & the DOM as a Tree · Computer Science for Frontend | Sandboxing & Site Isolation; The Main Thread | 2 | Published |
| Sandboxing & Site Isolation | `sandboxing-and-site-isolation.md` | The Web Platform | Browser Internals | Critical | Foundational | 11 min | Process & Thread Architecture | Process & Thread Architecture; The Main Thread | 2 | Planned |
| The Main Thread | `the-main-thread.md` | The Web Platform | Browser Internals | Critical | Foundational | 8 min | Process & Thread Architecture | Process & Thread Architecture; Sandboxing & Site Isolation | 2 | Planned |
| HTML Parsing & DOM Construction | `html-parsing-and-dom-construction.md` | The Web Platform | The Rendering Pipeline | Critical | Foundational | 11 min | Process & Thread Architecture | Style Calculation; Layout & Reflow; Paint & Layerization; Compositing | 2 | Planned |
| Style Calculation | `style-calculation.md` | The Web Platform | The Rendering Pipeline | Critical | Foundational | 8 min | HTML Parsing & DOM Construction; Process & Thread Architecture | HTML Parsing & DOM Construction; Layout & Reflow; Paint & Layerization; Compositing | 2 | Planned |
| Layout & Reflow | `layout-and-reflow.md` | The Web Platform | The Rendering Pipeline | Critical | Foundational | 8 min | HTML Parsing & DOM Construction; Process & Thread Architecture | HTML Parsing & DOM Construction; Style Calculation; Paint & Layerization; Compositing | 2 | Planned |
| Paint & Layerization | `paint-and-layerization.md` | The Web Platform | The Rendering Pipeline | Critical | Foundational | 8 min | HTML Parsing & DOM Construction; Process & Thread Architecture | HTML Parsing & DOM Construction; Style Calculation; Layout & Reflow; Compositing | 2 | Planned |
| Compositing | `compositing.md` | The Web Platform | The Rendering Pipeline | Critical | Foundational | 8 min | HTML Parsing & DOM Construction; Process & Thread Architecture | HTML Parsing & DOM Construction; Style Calculation; Layout & Reflow; Paint & Layerization | 2 | Planned |
| The DOM as an Abstraction | `the-dom-as-an-abstraction.md` | The Web Platform | Object Models | Critical | Foundational | 8 min | HTML Parsing & DOM Construction | The CSSOM; The Render Tree | 2 | Planned |
| The CSSOM | `the-cssom.md` | The Web Platform | Object Models | Critical | Foundational | 8 min | The DOM as an Abstraction; HTML Parsing & DOM Construction | The DOM as an Abstraction; The Render Tree | 2 | Planned |
| The Render Tree | `the-render-tree.md` | The Web Platform | Object Models | Critical | Foundational | 8 min | The DOM as an Abstraction; HTML Parsing & DOM Construction | The DOM as an Abstraction; The CSSOM | 2 | Planned |
| Tasks & the Callback Queue | `tasks-and-the-callback-queue.md` | The Web Platform | The Event Loop | Critical | Foundational | 8 min | The DOM as an Abstraction | Microtasks & the Job Queue; Rendering & rAF Timing; Long Tasks & Starvation | 2 | Planned |
| Microtasks & the Job Queue | `microtasks-and-the-job-queue.md` | The Web Platform | The Event Loop | Critical | Foundational | 8 min | Tasks & the Callback Queue; The DOM as an Abstraction | Tasks & the Callback Queue; Rendering & rAF Timing; Long Tasks & Starvation | 2 | Planned |
| Rendering & rAF Timing | `rendering-and-raf-timing.md` | The Web Platform | The Event Loop | Critical | Foundational | 8 min | Tasks & the Callback Queue; The DOM as an Abstraction | Tasks & the Callback Queue; Microtasks & the Job Queue; Long Tasks & Starvation | 2 | Planned |
| Long Tasks & Starvation | `long-tasks-and-starvation.md` | The Web Platform | The Event Loop | Critical | Foundational | 8 min | Tasks & the Callback Queue; The DOM as an Abstraction | Tasks & the Callback Queue; Microtasks & the Job Queue; Rendering & rAF Timing | 2 | Planned |
| Origins & Sites | `origins-and-sites.md` | The Web Platform | The Origin Model | Critical | Foundational | 8 min | Tasks & the Callback Queue | URL Anatomy; Document Lifecycle & bfcache | 2 | Planned |
| URL Anatomy | `url-anatomy.md` | The Web Platform | The Origin Model | Critical | Foundational | 8 min | Origins & Sites; Tasks & the Callback Queue | Origins & Sites; Document Lifecycle & bfcache | 2 | Planned |
| Document Lifecycle & bfcache | `document-lifecycle-and-bfcache.md` | The Web Platform | The Origin Model | Critical | Foundational | 11 min | Origins & Sites; Tasks & the Callback Queue | Origins & Sites; URL Anatomy | 2 | Planned |

---

## 01 · Core Languages  ·  Priority: Critical  ·  101 articles

### CSS & Visual Systems  (29 articles · ~250 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Specificity | `specificity.md` | CSS & Visual Systems | The Cascade | Critical | Foundational | 8 min | Process & Thread Architecture · The Web Platform | Inheritance & Initial Values; Cascade Layers (@layer); Custom Properties | 2 | Published |
| Inheritance & Initial Values | `inheritance-and-initial-values.md` | CSS & Visual Systems | The Cascade | Critical | Foundational | 11 min | Specificity | Specificity; Cascade Layers (@layer); Custom Properties | 2 | Published |
| Cascade Layers (@layer) | `cascade-layers-layer.md` | CSS & Visual Systems | The Cascade | Critical | Foundational | 8 min | Specificity | Specificity; Inheritance & Initial Values; Custom Properties | 2 | Published |
| Custom Properties | `custom-properties.md` | CSS & Visual Systems | The Cascade | Critical | Foundational | 8 min | Specificity | Specificity; Inheritance & Initial Values; Cascade Layers (@layer) | 2 | Published |
| The Box Model | `the-box-model.md` | CSS & Visual Systems | Box & Formatting | Critical | Foundational | 8 min | Specificity | Formatting Contexts; Stacking Contexts & z-index; Containment & content-visibility | 2 | Planned |
| Formatting Contexts | `formatting-contexts.md` | CSS & Visual Systems | Box & Formatting | Critical | Foundational | 8 min | The Box Model; Specificity | The Box Model; Stacking Contexts & z-index; Containment & content-visibility | 2 | Planned |
| Stacking Contexts & z-index | `stacking-contexts-and-z-index.md` | CSS & Visual Systems | Box & Formatting | Critical | Foundational | 11 min | The Box Model; Specificity | The Box Model; Formatting Contexts; Containment & content-visibility | 2 | Planned |
| Containment & content-visibility | `containment-and-content-visibility.md` | CSS & Visual Systems | Box & Formatting | Critical | Foundational | 11 min | The Box Model; Specificity | The Box Model; Formatting Contexts; Stacking Contexts & z-index | 2 | Planned |
| Normal Flow | `normal-flow.md` | CSS & Visual Systems | Layout Systems | Critical | Foundational | 8 min | The Box Model | Flexbox; Grid & Subgrid; Positioning & Sticky; Intrinsic Sizing | 2 | Planned |
| Flexbox | `flexbox.md` | CSS & Visual Systems | Layout Systems | Critical | Foundational | 8 min | Normal Flow; The Box Model | Normal Flow; Grid & Subgrid; Positioning & Sticky; Intrinsic Sizing | 2 | Planned |
| Grid & Subgrid | `grid-and-subgrid.md` | CSS & Visual Systems | Layout Systems | Critical | Foundational | 8 min | Normal Flow; The Box Model | Normal Flow; Flexbox; Positioning & Sticky; Intrinsic Sizing | 2 | Planned |
| Positioning & Sticky | `positioning-and-sticky.md` | CSS & Visual Systems | Layout Systems | Critical | Foundational | 8 min | Normal Flow; The Box Model | Normal Flow; Flexbox; Grid & Subgrid; Intrinsic Sizing | 2 | Planned |
| Intrinsic Sizing | `intrinsic-sizing.md` | CSS & Visual Systems | Layout Systems | Critical | Foundational | 8 min | Normal Flow; The Box Model | Normal Flow; Flexbox; Grid & Subgrid; Positioning & Sticky | 2 | Planned |
| Media Queries | `media-queries.md` | CSS & Visual Systems | Responsive Design | Critical | Foundational | 8 min | Normal Flow | Container Queries; Fluid Type & Space; Viewport & Responsive Units | 2 | Planned |
| Container Queries | `container-queries.md` | CSS & Visual Systems | Responsive Design | Critical | Foundational | 8 min | Media Queries; Normal Flow | Media Queries; Fluid Type & Space; Viewport & Responsive Units | 2 | Planned |
| Fluid Type & Space | `fluid-type-and-space.md` | CSS & Visual Systems | Responsive Design | Critical | Foundational | 8 min | Media Queries; Normal Flow | Media Queries; Container Queries; Viewport & Responsive Units | 2 | Planned |
| Viewport & Responsive Units | `viewport-and-responsive-units.md` | CSS & Visual Systems | Responsive Design | Critical | Foundational | 11 min | Media Queries; Normal Flow | Media Queries; Container Queries; Fluid Type & Space | 2 | Planned |
| Font Loading & FOUT/FOIT | `font-loading-and-fout-foit.md` | CSS & Visual Systems | Typography | Critical | Foundational | 8 min | Media Queries | Type Scale & Rhythm; Text Overflow & Truncation | 2 | Planned |
| Type Scale & Rhythm | `type-scale-and-rhythm.md` | CSS & Visual Systems | Typography | Critical | Foundational | 8 min | Font Loading & FOUT/FOIT; Media Queries | Font Loading & FOUT/FOIT; Text Overflow & Truncation | 2 | Planned |
| Text Overflow & Truncation | `text-overflow-and-truncation.md` | CSS & Visual Systems | Typography | Critical | Foundational | 8 min | Font Loading & FOUT/FOIT; Media Queries | Font Loading & FOUT/FOIT; Type Scale & Rhythm | 2 | Planned |
| Color Spaces & Gamut | `color-spaces-and-gamut.md` | CSS & Visual Systems | Color | Critical | Foundational | 8 min | Font Loading & FOUT/FOIT | Color Functions & Mixing; Perceptual Contrast & Readability | 2 | Planned |
| Color Functions & Mixing | `color-functions-and-mixing.md` | CSS & Visual Systems | Color | Critical | Foundational | 8 min | Color Spaces & Gamut; Font Loading & FOUT/FOIT | Color Spaces & Gamut; Perceptual Contrast & Readability | 2 | Planned |
| Perceptual Contrast & Readability | `perceptual-contrast-and-readability.md` | CSS & Visual Systems | Color | Critical | Foundational | 11 min | Color Spaces & Gamut; Font Loading & FOUT/FOIT | Color Spaces & Gamut; Color Functions & Mixing | 2 | Planned |
| Naming Methodologies | `naming-methodologies.md` | CSS & Visual Systems | Styling Architecture | Critical | Foundational | 8 min | Color Spaces & Gamut | Scoping & Isolation; Utility-First Styling; CSS-in-JS Models; Zero-Runtime / Compiled CSS | 2 | Planned |
| Scoping & Isolation | `scoping-and-isolation.md` | CSS & Visual Systems | Styling Architecture | Critical | Foundational | 8 min | Naming Methodologies; Color Spaces & Gamut | Naming Methodologies; Utility-First Styling; CSS-in-JS Models; Zero-Runtime / Compiled CSS | 2 | Planned |
| Utility-First Styling | `utility-first-styling.md` | CSS & Visual Systems | Styling Architecture | Critical | Foundational | 8 min | Naming Methodologies; Color Spaces & Gamut | Naming Methodologies; Scoping & Isolation; CSS-in-JS Models; Zero-Runtime / Compiled CSS | 2 | Planned |
| CSS-in-JS Models | `css-in-js-models.md` | CSS & Visual Systems | Styling Architecture | Critical | Foundational | 8 min | Naming Methodologies; Color Spaces & Gamut | Naming Methodologies; Scoping & Isolation; Utility-First Styling; Zero-Runtime / Compiled CSS | 2 | Planned |
| Zero-Runtime / Compiled CSS | `zero-runtime-compiled-css.md` | CSS & Visual Systems | Styling Architecture | Critical | Foundational | 11 min | Naming Methodologies; Color Spaces & Gamut | Naming Methodologies; Scoping & Isolation; Utility-First Styling; CSS-in-JS Models | 2 | Planned |
| Consuming Design Tokens | `consuming-design-tokens.md` | CSS & Visual Systems | Styling Architecture | Critical | Foundational | 8 min | Naming Methodologies; Color Spaces & Gamut | Naming Methodologies; Scoping & Isolation; Utility-First Styling; CSS-in-JS Models | 2 | Planned |

### HTML & Document Semantics  (16 articles · ~128 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| The Document Outline | `the-document-outline.md` | HTML & Document Semantics | Document Structure | Critical | Foundational | 8 min | Process & Thread Architecture · The Web Platform | Sectioning & Landmarks; Headings Hierarchy; Tables & Data Semantics | 2 | Published |
| Sectioning & Landmarks | `sectioning-and-landmarks.md` | HTML & Document Semantics | Document Structure | Critical | Foundational | 8 min | The Document Outline | The Document Outline; Headings Hierarchy; Tables & Data Semantics | 2 | Published |
| Headings Hierarchy | `headings-hierarchy.md` | HTML & Document Semantics | Document Structure | Critical | Foundational | 8 min | The Document Outline | The Document Outline; Sectioning & Landmarks; Tables & Data Semantics | 2 | Published |
| Tables & Data Semantics | `tables-and-data-semantics.md` | HTML & Document Semantics | Document Structure | Critical | Foundational | 8 min | The Document Outline | The Document Outline; Sectioning & Landmarks; Headings Hierarchy | 2 | Planned |
| Native Form Controls | `native-form-controls.md` | HTML & Document Semantics | Interactive Elements | Critical | Foundational | 8 min | The Document Outline | Buttons, Links & Actions; Dialog, Details & Popover; The Contenteditable Model | 2 | Planned |
| Buttons, Links & Actions | `buttons-links-and-actions.md` | HTML & Document Semantics | Interactive Elements | Critical | Foundational | 8 min | Native Form Controls; The Document Outline | Native Form Controls; Dialog, Details & Popover; The Contenteditable Model | 2 | Planned |
| Dialog, Details & Popover | `dialog-details-and-popover.md` | HTML & Document Semantics | Interactive Elements | Critical | Foundational | 8 min | Native Form Controls; The Document Outline | Native Form Controls; Buttons, Links & Actions; The Contenteditable Model | 2 | Planned |
| The Contenteditable Model | `the-contenteditable-model.md` | HTML & Document Semantics | Interactive Elements | Critical | Foundational | 8 min | Native Form Controls; The Document Outline | Native Form Controls; Buttons, Links & Actions; Dialog, Details & Popover | 2 | Planned |
| Responsive Images (srcset) | `responsive-images-srcset.md` | HTML & Document Semantics | Embedded Content | Critical | Foundational | 8 min | Native Form Controls | Audio & Video; Iframes & Embedding; Inline SVG | 2 | Planned |
| Audio & Video | `audio-and-video.md` | HTML & Document Semantics | Embedded Content | Critical | Foundational | 8 min | Responsive Images (srcset); Native Form Controls | Responsive Images (srcset); Iframes & Embedding; Inline SVG | 2 | Planned |
| Iframes & Embedding | `iframes-and-embedding.md` | HTML & Document Semantics | Embedded Content | Critical | Foundational | 8 min | Responsive Images (srcset); Native Form Controls | Responsive Images (srcset); Audio & Video; Inline SVG | 2 | Planned |
| Inline SVG | `inline-svg.md` | HTML & Document Semantics | Embedded Content | Critical | Foundational | 8 min | Responsive Images (srcset); Native Form Controls | Responsive Images (srcset); Audio & Video; Iframes & Embedding | 2 | Planned |
| Head Metadata | `head-metadata.md` | HTML & Document Semantics | Metadata & Discovery | Critical | Foundational | 8 min | Responsive Images (srcset) | SEO Semantics; Open Graph & Social Cards; Structured Data (JSON-LD) | 2 | Planned |
| SEO Semantics | `seo-semantics.md` | HTML & Document Semantics | Metadata & Discovery | Critical | Foundational | 8 min | Head Metadata; Responsive Images (srcset) | Head Metadata; Open Graph & Social Cards; Structured Data (JSON-LD) | 2 | Planned |
| Open Graph & Social Cards | `open-graph-and-social-cards.md` | HTML & Document Semantics | Metadata & Discovery | Critical | Foundational | 8 min | Head Metadata; Responsive Images (srcset) | Head Metadata; SEO Semantics; Structured Data (JSON-LD) | 2 | Planned |
| Structured Data (JSON-LD) | `structured-data-json-ld.md` | HTML & Document Semantics | Metadata & Discovery | Critical | Foundational | 8 min | Head Metadata; Responsive Images (srcset) | Head Metadata; SEO Semantics; Open Graph & Social Cards | 2 | Planned |

### JavaScript  (31 articles · ~275 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Primitives & Wrappers | `primitives-and-wrappers.md` | JavaScript | Runtime Types | Critical | Foundational | 8 min | Trees & the DOM as a Tree · Computer Science for Frontend; Parsing & Bytecode · Runtime & Execution | Coercion & Conversion; Equality & Comparison; null, undefined & Nullish | 2 | Planned |
| Coercion & Conversion | `coercion-and-conversion.md` | JavaScript | Runtime Types | Critical | Foundational | 8 min | Primitives & Wrappers | Primitives & Wrappers; Equality & Comparison; null, undefined & Nullish | 2 | Planned |
| Equality & Comparison | `equality-and-comparison.md` | JavaScript | Runtime Types | Critical | Foundational | 8 min | Primitives & Wrappers | Primitives & Wrappers; Coercion & Conversion; null, undefined & Nullish | 2 | Planned |
| null, undefined & Nullish | `null-undefined-and-nullish.md` | JavaScript | Runtime Types | Critical | Foundational | 8 min | Primitives & Wrappers | Primitives & Wrappers; Coercion & Conversion; Equality & Comparison | 2 | Planned |
| Lexical Scope | `lexical-scope.md` | JavaScript | Scope & Closures | Critical | Foundational | 8 min | Primitives & Wrappers | Closures; Hoisting & TDZ; Block vs Function Scope | 2 | Published |
| Closures | `closures.md` | JavaScript | Scope & Closures | Critical | Foundational | 8 min | Lexical Scope; Primitives & Wrappers | Lexical Scope; Hoisting & TDZ; Block vs Function Scope | 2 | Published |
| Hoisting & TDZ | `hoisting-and-tdz.md` | JavaScript | Scope & Closures | Critical | Foundational | 8 min | Lexical Scope; Primitives & Wrappers | Lexical Scope; Closures; Block vs Function Scope | 2 | Planned |
| Block vs Function Scope | `block-vs-function-scope.md` | JavaScript | Scope & Closures | Critical | Foundational | 8 min | Lexical Scope; Primitives & Wrappers | Lexical Scope; Closures; Hoisting & TDZ | 2 | Planned |
| Property Descriptors | `property-descriptors.md` | JavaScript | Objects & Prototypes | Critical | Foundational | 8 min | Lexical Scope | The Prototype Chain; Inheritance Patterns; Proxies & Reflect | 2 | Planned |
| The Prototype Chain | `the-prototype-chain.md` | JavaScript | Objects & Prototypes | Critical | Foundational | 8 min | Property Descriptors; Lexical Scope | Property Descriptors; Inheritance Patterns; Proxies & Reflect | 2 | Planned |
| Inheritance Patterns | `inheritance-patterns.md` | JavaScript | Objects & Prototypes | Critical | Foundational | 8 min | Property Descriptors; Lexical Scope | Property Descriptors; The Prototype Chain; Proxies & Reflect | 2 | Planned |
| Proxies & Reflect | `proxies-and-reflect.md` | JavaScript | Objects & Prototypes | Critical | Foundational | 8 min | Property Descriptors; Lexical Scope | Property Descriptors; The Prototype Chain; Inheritance Patterns | 2 | Planned |
| Binding Rules | `binding-rules.md` | JavaScript | The `this` Model | Critical | Foundational | 8 min | Property Descriptors | call / apply / bind; Arrow Functions & Lexical this | 2 | Planned |
| call / apply / bind | `call-apply-bind.md` | JavaScript | The `this` Model | Critical | Foundational | 8 min | Binding Rules; Property Descriptors | Binding Rules; Arrow Functions & Lexical this | 2 | Planned |
| Arrow Functions & Lexical this | `arrow-functions-and-lexical-this.md` | JavaScript | The `this` Model | Critical | Foundational | 11 min | Binding Rules; Property Descriptors | Binding Rules; call / apply / bind | 2 | Planned |
| Higher-Order Functions | `higher-order-functions.md` | JavaScript | Functions | Critical | Foundational | 8 min | Binding Rules | Currying & Partial Application; Composition | 2 | Planned |
| Currying & Partial Application | `currying-and-partial-application.md` | JavaScript | Functions | Critical | Foundational | 11 min | Higher-Order Functions; Binding Rules | Higher-Order Functions; Composition | 2 | Planned |
| Composition | `composition.md` | JavaScript | Functions | Critical | Foundational | 8 min | Higher-Order Functions; Binding Rules | Higher-Order Functions; Currying & Partial Application | 2 | Planned |
| Iterators & Iterables | `iterators-and-iterables.md` | JavaScript | Iteration Protocols | Critical | Foundational | 8 min | Higher-Order Functions | Generators; Async Iterators | 2 | Planned |
| Generators | `generators.md` | JavaScript | Iteration Protocols | Critical | Foundational | 8 min | Iterators & Iterables; Higher-Order Functions | Iterators & Iterables; Async Iterators | 2 | Planned |
| Async Iterators | `async-iterators.md` | JavaScript | Iteration Protocols | Critical | Foundational | 8 min | Iterators & Iterables; Higher-Order Functions | Iterators & Iterables; Generators | 2 | Planned |
| The Callback Model | `the-callback-model.md` | JavaScript | Asynchrony | Critical | Foundational | 8 min | Iterators & Iterables | Promises; async / await; Cancellation & AbortController | 2 | Planned |
| Promises | `promises.md` | JavaScript | Asynchrony | Critical | Foundational | 8 min | The Callback Model; Iterators & Iterables | The Callback Model; async / await; Cancellation & AbortController | 2 | Planned |
| async / await | `async-await.md` | JavaScript | Asynchrony | Critical | Foundational | 8 min | The Callback Model; Iterators & Iterables | The Callback Model; Promises; Cancellation & AbortController | 2 | Planned |
| Cancellation & AbortController | `cancellation-and-abortcontroller.md` | JavaScript | Asynchrony | Critical | Foundational | 11 min | The Callback Model; Iterators & Iterables | The Callback Model; Promises; async / await | 2 | Planned |
| ES Modules | `es-modules.md` | JavaScript | Modules | Critical | Foundational | 8 min | The Callback Model | Dynamic Import; Module Resolution Semantics | 2 | Planned |
| Dynamic Import | `dynamic-import.md` | JavaScript | Modules | Critical | Foundational | 8 min | ES Modules; The Callback Model | ES Modules; Module Resolution Semantics | 2 | Planned |
| Module Resolution Semantics | `module-resolution-semantics.md` | JavaScript | Modules | Critical | Foundational | 11 min | ES Modules; The Callback Model | ES Modules; Dynamic Import | 2 | Planned |
| Symbols & Well-Known Symbols | `symbols-and-well-known-symbols.md` | JavaScript | Metaprogramming | Critical | Intermediate | 15 min | ES Modules | Reflection; Tagged Templates | 3 | Planned |
| Reflection | `reflection.md` | JavaScript | Metaprogramming | Critical | Intermediate | 12 min | Symbols & Well-Known Symbols; ES Modules | Symbols & Well-Known Symbols; Tagged Templates | 3 | Planned |
| Tagged Templates | `tagged-templates.md` | JavaScript | Metaprogramming | Critical | Intermediate | 12 min | Symbols & Well-Known Symbols; ES Modules | Symbols & Well-Known Symbols; Reflection | 3 | Planned |

### TypeScript  (25 articles · ~234 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Structural Typing | `structural-typing.md` | TypeScript | Type Foundations | Critical | Foundational | 8 min | Primitives & Wrappers · JavaScript | Assignability; unknown, never & any; Literal & Unit Types | 2 | Published |
| Assignability | `assignability.md` | TypeScript | Type Foundations | Critical | Foundational | 8 min | Structural Typing | Structural Typing; unknown, never & any; Literal & Unit Types | 2 | Published |
| unknown, never & any | `unknown-never-and-any.md` | TypeScript | Type Foundations | Critical | Foundational | 8 min | Structural Typing | Structural Typing; Assignability; Literal & Unit Types | 2 | Published |
| Literal & Unit Types | `literal-and-unit-types.md` | TypeScript | Type Foundations | Critical | Foundational | 8 min | Structural Typing | Structural Typing; Assignability; unknown, never & any | 2 | Published |
| Unions & Intersections | `unions-and-intersections.md` | TypeScript | Composition | Critical | Foundational | 8 min | Structural Typing | Generics; Generic Constraints; Indexed Access & keyof | 2 | Published |
| Generics | `generics.md` | TypeScript | Composition | Critical | Foundational | 8 min | Unions & Intersections; Structural Typing | Unions & Intersections; Generic Constraints; Indexed Access & keyof | 2 | Planned |
| Generic Constraints | `generic-constraints.md` | TypeScript | Composition | Critical | Foundational | 8 min | Unions & Intersections; Structural Typing | Unions & Intersections; Generics; Indexed Access & keyof | 2 | Planned |
| Indexed Access & keyof | `indexed-access-and-keyof.md` | TypeScript | Composition | Critical | Foundational | 8 min | Unions & Intersections; Structural Typing | Unions & Intersections; Generics; Generic Constraints | 2 | Planned |
| Conditional Types | `conditional-types.md` | TypeScript | Type Transformation | Critical | Intermediate | 12 min | Unions & Intersections | Mapped Types; Template Literal Types; infer & Type Extraction | 3 | Planned |
| Mapped Types | `mapped-types.md` | TypeScript | Type Transformation | Critical | Intermediate | 12 min | Conditional Types; Unions & Intersections | Conditional Types; Template Literal Types; infer & Type Extraction | 3 | Planned |
| Template Literal Types | `template-literal-types.md` | TypeScript | Type Transformation | Critical | Intermediate | 12 min | Conditional Types; Unions & Intersections | Conditional Types; Mapped Types; infer & Type Extraction | 3 | Planned |
| infer & Type Extraction | `infer-and-type-extraction.md` | TypeScript | Type Transformation | Critical | Intermediate | 12 min | Conditional Types; Unions & Intersections | Conditional Types; Mapped Types; Template Literal Types | 3 | Planned |
| Type Inference | `type-inference.md` | TypeScript | Inference & Flow | Critical | Foundational | 8 min | Conditional Types | Control-Flow Narrowing; Type Guards & Predicates; Discriminated Unions | 2 | Planned |
| Control-Flow Narrowing | `control-flow-narrowing.md` | TypeScript | Inference & Flow | Critical | Foundational | 8 min | Type Inference; Conditional Types | Type Inference; Type Guards & Predicates; Discriminated Unions | 2 | Planned |
| Type Guards & Predicates | `type-guards-and-predicates.md` | TypeScript | Inference & Flow | Critical | Foundational | 8 min | Type Inference; Conditional Types | Type Inference; Control-Flow Narrowing; Discriminated Unions | 2 | Planned |
| Discriminated Unions | `discriminated-unions.md` | TypeScript | Inference & Flow | Critical | Foundational | 8 min | Type Inference; Conditional Types | Type Inference; Control-Flow Narrowing; Type Guards & Predicates | 2 | Planned |
| Variance | `variance.md` | TypeScript | Soundness & Safety | Critical | Intermediate | 12 min | Type Inference | Unsoundness & Escape Hatches; Strictness Flags | 3 | Planned |
| Unsoundness & Escape Hatches | `unsoundness-and-escape-hatches.md` | TypeScript | Soundness & Safety | Critical | Intermediate | 15 min | Variance; Type Inference | Variance; Strictness Flags | 3 | Planned |
| Strictness Flags | `strictness-flags.md` | TypeScript | Soundness & Safety | Critical | Intermediate | 12 min | Variance; Type Inference | Variance; Unsoundness & Escape Hatches | 3 | Planned |
| Declaration Files | `declaration-files.md` | TypeScript | Ambient & Interop | Critical | Foundational | 8 min | Variance | Module Augmentation; Typing Third-Party Code | 2 | Planned |
| Module Augmentation | `module-augmentation.md` | TypeScript | Ambient & Interop | Critical | Foundational | 8 min | Declaration Files; Variance | Declaration Files; Typing Third-Party Code | 2 | Planned |
| Typing Third-Party Code | `typing-third-party-code.md` | TypeScript | Ambient & Interop | Critical | Foundational | 8 min | Declaration Files; Variance | Declaration Files; Module Augmentation | 2 | Planned |
| Branded & Nominal Types | `branded-and-nominal-types.md` | TypeScript | Domain Modeling | Critical | Foundational | 8 min | Declaration Files | Exhaustiveness; Illegal States Unrepresentable | 2 | Planned |
| Exhaustiveness | `exhaustiveness.md` | TypeScript | Domain Modeling | Critical | Foundational | 8 min | Branded & Nominal Types; Declaration Files | Branded & Nominal Types; Illegal States Unrepresentable | 2 | Planned |
| Illegal States Unrepresentable | `illegal-states-unrepresentable.md` | TypeScript | Domain Modeling | Critical | Foundational | 11 min | Branded & Nominal Types; Declaration Files | Branded & Nominal Types; Exhaustiveness | 2 | Planned |

---

## 02 · Rendering & Frameworks  ·  Priority: Critical  ·  76 articles

### React  (33 articles · ~436 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Elements vs Components | `elements-vs-components.md` | React | The Component Model | Critical | Intermediate | 12 min | Primitives & Wrappers · JavaScript; The CSR Model · Rendering Architectures; The Document Outline · HTML & Document Semantics | JSX Semantics; Composition & Children | 3 | Published |
| JSX Semantics | `jsx-semantics.md` | React | The Component Model | Critical | Intermediate | 12 min | Elements vs Components | Elements vs Components; Composition & Children | 3 | Published |
| Composition & Children | `composition-and-children.md` | React | The Component Model | Critical | Intermediate | 12 min | Elements vs Components | Elements vs Components; JSX Semantics | 3 | Published |
| The Render Phase | `the-render-phase.md` | React | Rendering & Reconciliation | Critical | Intermediate | 12 min | Elements vs Components | Reconciliation & Diffing; Keys & List Reconciliation; The Commit Phase | 3 | Published |
| Reconciliation & Diffing | `reconciliation-and-diffing.md` | React | Rendering & Reconciliation | Critical | Intermediate | 12 min | The Render Phase; Elements vs Components | The Render Phase; Keys & List Reconciliation; The Commit Phase | 3 | Planned |
| Keys & List Reconciliation | `keys-and-list-reconciliation.md` | React | Rendering & Reconciliation | Critical | Intermediate | 12 min | The Render Phase; Elements vs Components | The Render Phase; Reconciliation & Diffing; The Commit Phase | 3 | Planned |
| The Commit Phase | `the-commit-phase.md` | React | Rendering & Reconciliation | Critical | Intermediate | 12 min | The Render Phase; Elements vs Components | The Render Phase; Reconciliation & Diffing; Keys & List Reconciliation | 3 | Planned |
| useState | `usestate.md` | React | State & Hooks | Critical | Intermediate | 12 min | The Render Phase | useReducer; The Rules of Hooks; State Batching & Updates | 3 | Planned |
| useReducer | `usereducer.md` | React | State & Hooks | Critical | Intermediate | 12 min | useState; The Render Phase | useState; The Rules of Hooks; State Batching & Updates | 3 | Planned |
| The Rules of Hooks | `the-rules-of-hooks.md` | React | State & Hooks | Critical | Intermediate | 12 min | useState; The Render Phase | useState; useReducer; State Batching & Updates | 3 | Planned |
| State Batching & Updates | `state-batching-and-updates.md` | React | State & Hooks | Critical | Intermediate | 12 min | useState; The Render Phase | useState; useReducer; The Rules of Hooks | 3 | Planned |
| useEffect & Synchronization | `useeffect-and-synchronization.md` | React | Effects & Lifecycle | Critical | Intermediate | 15 min | useState | useLayoutEffect; Effect Cleanup & Dependencies; Refs & useRef; Error Boundaries | 3 | Planned |
| useLayoutEffect | `uselayouteffect.md` | React | Effects & Lifecycle | Critical | Intermediate | 12 min | useEffect & Synchronization; useState | useEffect & Synchronization; Effect Cleanup & Dependencies; Refs & useRef; Error Boundaries | 3 | Planned |
| Effect Cleanup & Dependencies | `effect-cleanup-and-dependencies.md` | React | Effects & Lifecycle | Critical | Intermediate | 15 min | useEffect & Synchronization; useState | useEffect & Synchronization; useLayoutEffect; Refs & useRef; Error Boundaries | 3 | Planned |
| Refs & useRef | `refs-and-useref.md` | React | Effects & Lifecycle | Critical | Intermediate | 12 min | useEffect & Synchronization; useState | useEffect & Synchronization; useLayoutEffect; Effect Cleanup & Dependencies; Error Boundaries | 3 | Planned |
| Error Boundaries | `error-boundaries.md` | React | Effects & Lifecycle | Critical | Intermediate | 12 min | useEffect & Synchronization; useState | useEffect & Synchronization; useLayoutEffect; Effect Cleanup & Dependencies; Refs & useRef | 3 | Planned |
| Context & Providers | `context-and-providers.md` | React | Context & Data | Critical | Intermediate | 12 min | useEffect & Synchronization | Context Performance; useContext Patterns | 3 | Planned |
| Context Performance | `context-performance.md` | React | Context & Data | Critical | Intermediate | 12 min | Context & Providers; useEffect & Synchronization | Context & Providers; useContext Patterns | 3 | Planned |
| useContext Patterns | `usecontext-patterns.md` | React | Context & Data | Critical | Intermediate | 12 min | Context & Providers; useEffect & Synchronization | Context & Providers; Context Performance | 3 | Planned |
| Concurrent Rendering | `concurrent-rendering.md` | React | Concurrency | Critical | Advanced | 16 min | Context & Providers | Transitions & useTransition; useDeferredValue; Suspense | 4 | Planned |
| Transitions & useTransition | `transitions-and-usetransition.md` | React | Concurrency | Critical | Advanced | 19 min | Concurrent Rendering; Context & Providers | Concurrent Rendering; useDeferredValue; Suspense | 4 | Planned |
| useDeferredValue | `usedeferredvalue.md` | React | Concurrency | Critical | Advanced | 16 min | Concurrent Rendering; Context & Providers | Concurrent Rendering; Transitions & useTransition; Suspense | 4 | Planned |
| Suspense | `suspense.md` | React | Concurrency | Critical | Advanced | 16 min | Concurrent Rendering; Context & Providers | Concurrent Rendering; Transitions & useTransition; useDeferredValue | 4 | Planned |
| Server Components | `server-components.md` | React | Server React | Critical | Advanced | 16 min | Concurrent Rendering | Server Actions; The RSC Payload & Boundaries | 4 | Planned |
| Server Actions | `server-actions.md` | React | Server React | Critical | Advanced | 16 min | Server Components; Concurrent Rendering | Server Components; The RSC Payload & Boundaries | 4 | Planned |
| The RSC Payload & Boundaries | `the-rsc-payload-and-boundaries.md` | React | Server React | Critical | Advanced | 19 min | Server Components; Concurrent Rendering | Server Components; Server Actions | 4 | Planned |
| memo, useMemo, useCallback | `memo-usememo-usecallback.md` | React | Optimization | Critical | Intermediate | 12 min | Server Components | Referential Stability; The React Compiler Model | 3 | Planned |
| Referential Stability | `referential-stability.md` | React | Optimization | Critical | Intermediate | 12 min | memo, useMemo, useCallback; Server Components | memo, useMemo, useCallback; The React Compiler Model | 3 | Planned |
| The React Compiler Model | `the-react-compiler-model.md` | React | Optimization | Critical | Intermediate | 12 min | memo, useMemo, useCallback; Server Components | memo, useMemo, useCallback; Referential Stability | 3 | Planned |
| Custom Hooks | `custom-hooks.md` | React | React Composition | Critical | Intermediate | 12 min | memo, useMemo, useCallback | Portals; Higher-Order Components; Children Manipulation | 3 | Planned |
| Portals | `portals.md` | React | React Composition | Critical | Intermediate | 12 min | Custom Hooks; memo, useMemo, useCallback | Custom Hooks; Higher-Order Components; Children Manipulation | 3 | Planned |
| Higher-Order Components | `higher-order-components.md` | React | React Composition | Critical | Intermediate | 12 min | Custom Hooks; memo, useMemo, useCallback | Custom Hooks; Portals; Children Manipulation | 3 | Planned |
| Children Manipulation | `children-manipulation.md` | React | React Composition | Critical | Intermediate | 12 min | Custom Hooks; memo, useMemo, useCallback | Custom Hooks; Portals; Higher-Order Components | 3 | Planned |

### Reactivity & Framework Models  (10 articles · ~169 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Signals & Fine-Grained Reactivity | `signals-and-fine-grained-reactivity.md` | Reactivity & Framework Models | Reactivity Paradigms | Critical | Advanced | 19 min | Primitives & Wrappers · JavaScript; The CSR Model · Rendering Architectures | The Virtual DOM; Compiled Reactivity; Push-Based vs Dirty Checking | 4 | Planned |
| The Virtual DOM | `the-virtual-dom.md` | Reactivity & Framework Models | Reactivity Paradigms | Critical | Advanced | 16 min | Signals & Fine-Grained Reactivity | Signals & Fine-Grained Reactivity; Compiled Reactivity; Push-Based vs Dirty Checking | 4 | Planned |
| Compiled Reactivity | `compiled-reactivity.md` | Reactivity & Framework Models | Reactivity Paradigms | Critical | Advanced | 16 min | Signals & Fine-Grained Reactivity | Signals & Fine-Grained Reactivity; The Virtual DOM; Push-Based vs Dirty Checking | 4 | Planned |
| Push-Based vs Dirty Checking | `push-based-vs-dirty-checking.md` | Reactivity & Framework Models | Reactivity Paradigms | Critical | Advanced | 19 min | Signals & Fine-Grained Reactivity | Signals & Fine-Grained Reactivity; The Virtual DOM; Compiled Reactivity | 4 | Planned |
| Observables | `observables.md` | Reactivity & Framework Models | Primitives | Critical | Advanced | 16 min | Signals & Fine-Grained Reactivity | Atoms & Derived Values; Effects & Reactions | 4 | Planned |
| Atoms & Derived Values | `atoms-and-derived-values.md` | Reactivity & Framework Models | Primitives | Critical | Advanced | 16 min | Observables; Signals & Fine-Grained Reactivity | Observables; Effects & Reactions | 4 | Planned |
| Effects & Reactions | `effects-and-reactions.md` | Reactivity & Framework Models | Primitives | Critical | Advanced | 16 min | Observables; Signals & Fine-Grained Reactivity | Observables; Atoms & Derived Values | 4 | Planned |
| Declarative vs Imperative UI | `declarative-vs-imperative-ui.md` | Reactivity & Framework Models | Mental Models | Critical | Advanced | 19 min | Observables | Data Binding Models; Framework Comparison Axes | 4 | Planned |
| Data Binding Models | `data-binding-models.md` | Reactivity & Framework Models | Mental Models | Critical | Advanced | 16 min | Declarative vs Imperative UI; Observables | Declarative vs Imperative UI; Framework Comparison Axes | 4 | Planned |
| Framework Comparison Axes | `framework-comparison-axes.md` | Reactivity & Framework Models | Mental Models | Critical | Advanced | 16 min | Declarative vs Imperative UI; Observables | Declarative vs Imperative UI; Data Binding Models | 4 | Planned |

### Rendering Architectures  (17 articles · ~225 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| The CSR Model | `the-csr-model.md` | Rendering Architectures | Client Rendering | Critical | Intermediate | 12 min | Process & Thread Architecture · The Web Platform; HTTP/1.1 Semantics · Networking & Protocols | The App Shell Pattern; Client-Side Data Loading | 3 | Planned |
| The App Shell Pattern | `the-app-shell-pattern.md` | Rendering Architectures | Client Rendering | Critical | Intermediate | 12 min | The CSR Model | The CSR Model; Client-Side Data Loading | 3 | Planned |
| Client-Side Data Loading | `client-side-data-loading.md` | Rendering Architectures | Client Rendering | Critical | Intermediate | 12 min | The CSR Model | The CSR Model; The App Shell Pattern | 3 | Planned |
| The SSR Model | `the-ssr-model.md` | Rendering Architectures | Server Rendering | Critical | Intermediate | 12 min | The CSR Model | Hydration; Selective & Progressive Hydration; Hydration Mismatches | 3 | Planned |
| Hydration | `hydration.md` | Rendering Architectures | Server Rendering | Critical | Intermediate | 12 min | The SSR Model; The CSR Model | The SSR Model; Selective & Progressive Hydration; Hydration Mismatches | 3 | Planned |
| Selective & Progressive Hydration | `selective-and-progressive-hydration.md` | Rendering Architectures | Server Rendering | Critical | Intermediate | 15 min | The SSR Model; The CSR Model | The SSR Model; Hydration; Hydration Mismatches | 3 | Planned |
| Hydration Mismatches | `hydration-mismatches.md` | Rendering Architectures | Server Rendering | Critical | Intermediate | 12 min | The SSR Model; The CSR Model | The SSR Model; Hydration; Selective & Progressive Hydration | 3 | Planned |
| Static Site Generation | `static-site-generation.md` | Rendering Architectures | Static & Hybrid | Critical | Intermediate | 12 min | The SSR Model | Incremental Static Regeneration; On-Demand Revalidation | 3 | Planned |
| Incremental Static Regeneration | `incremental-static-regeneration.md` | Rendering Architectures | Static & Hybrid | Critical | Intermediate | 15 min | Static Site Generation; The SSR Model | Static Site Generation; On-Demand Revalidation | 3 | Planned |
| On-Demand Revalidation | `on-demand-revalidation.md` | Rendering Architectures | Static & Hybrid | Critical | Intermediate | 12 min | Static Site Generation; The SSR Model | Static Site Generation; Incremental Static Regeneration | 3 | Planned |
| Streaming SSR | `streaming-ssr.md` | Rendering Architectures | Streaming | Critical | Advanced | 16 min | Static Site Generation | Progressive Rendering & Flushing; Out-of-Order Streaming | 4 | Planned |
| Progressive Rendering & Flushing | `progressive-rendering-and-flushing.md` | Rendering Architectures | Streaming | Critical | Advanced | 19 min | Streaming SSR; Static Site Generation | Streaming SSR; Out-of-Order Streaming | 4 | Planned |
| Out-of-Order Streaming | `out-of-order-streaming.md` | Rendering Architectures | Streaming | Critical | Advanced | 16 min | Streaming SSR; Static Site Generation | Streaming SSR; Progressive Rendering & Flushing | 4 | Planned |
| The Server/Client Boundary | `the-server-client-boundary.md` | Rendering Architectures | Boundaries & Models | Critical | Intermediate | 12 min | Streaming SSR | Islands Architecture; Resumability vs Hydration; Edge vs Origin Rendering | 3 | Planned |
| Islands Architecture | `islands-architecture.md` | Rendering Architectures | Boundaries & Models | Critical | Intermediate | 12 min | The Server/Client Boundary; Streaming SSR | The Server/Client Boundary; Resumability vs Hydration; Edge vs Origin Rendering | 3 | Planned |
| Resumability vs Hydration | `resumability-vs-hydration.md` | Rendering Architectures | Boundaries & Models | Critical | Intermediate | 12 min | The Server/Client Boundary; Streaming SSR | The Server/Client Boundary; Islands Architecture; Edge vs Origin Rendering | 3 | Planned |
| Edge vs Origin Rendering | `edge-vs-origin-rendering.md` | Rendering Architectures | Boundaries & Models | Critical | Intermediate | 12 min | The Server/Client Boundary; Streaming SSR | The Server/Client Boundary; Islands Architecture; Resumability vs Hydration | 3 | Planned |

### Routing  (16 articles · ~204 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Client-Side Routing | `client-side-routing.md` | Routing | Routing Models | Critical | Intermediate | 12 min | The CSR Model · Rendering Architectures; Web Storage · Browser APIs | File-Based & Server Routing; Hybrid Routing | 3 | Planned |
| File-Based & Server Routing | `file-based-and-server-routing.md` | Routing | Routing Models | Critical | Intermediate | 15 min | Client-Side Routing | Client-Side Routing; Hybrid Routing | 3 | Planned |
| Hybrid Routing | `hybrid-routing.md` | Routing | Routing Models | Critical | Intermediate | 12 min | Client-Side Routing | Client-Side Routing; File-Based & Server Routing | 3 | Planned |
| Route Matching & Params | `route-matching-and-params.md` | Routing | Route Structure | Critical | Intermediate | 12 min | Client-Side Routing | Nested Routes & Layouts; Parallel & Intercepting Routes; The URL as State | 3 | Planned |
| Nested Routes & Layouts | `nested-routes-and-layouts.md` | Routing | Route Structure | Critical | Intermediate | 12 min | Route Matching & Params; Client-Side Routing | Route Matching & Params; Parallel & Intercepting Routes; The URL as State | 3 | Planned |
| Parallel & Intercepting Routes | `parallel-and-intercepting-routes.md` | Routing | Route Structure | Critical | Intermediate | 15 min | Route Matching & Params; Client-Side Routing | Route Matching & Params; Nested Routes & Layouts; The URL as State | 3 | Planned |
| The URL as State | `the-url-as-state.md` | Routing | Route Structure | Critical | Intermediate | 12 min | Route Matching & Params; Client-Side Routing | Route Matching & Params; Nested Routes & Layouts; Parallel & Intercepting Routes | 3 | Planned |
| Route Loaders & Dependencies | `route-loaders-and-dependencies.md` | Routing | Route Data | Critical | Intermediate | 15 min | Route Matching & Params | Deferred & Streaming Route Data; Route Actions & Mutations | 3 | Planned |
| Deferred & Streaming Route Data | `deferred-and-streaming-route-data.md` | Routing | Route Data | Critical | Intermediate | 15 min | Route Loaders & Dependencies; Route Matching & Params | Route Loaders & Dependencies; Route Actions & Mutations | 3 | Planned |
| Route Actions & Mutations | `route-actions-and-mutations.md` | Routing | Route Data | Critical | Intermediate | 12 min | Route Loaders & Dependencies; Route Matching & Params | Route Loaders & Dependencies; Deferred & Streaming Route Data | 3 | Planned |
| Navigation & Linking | `navigation-and-linking.md` | Routing | Navigation | Critical | Intermediate | 12 min | Route Loaders & Dependencies | Transitions & Pending UI; Scroll Restoration; Route Prefetching | 3 | Planned |
| Transitions & Pending UI | `transitions-and-pending-ui.md` | Routing | Navigation | Critical | Intermediate | 12 min | Navigation & Linking; Route Loaders & Dependencies | Navigation & Linking; Scroll Restoration; Route Prefetching | 3 | Planned |
| Scroll Restoration | `scroll-restoration.md` | Routing | Navigation | Critical | Intermediate | 12 min | Navigation & Linking; Route Loaders & Dependencies | Navigation & Linking; Transitions & Pending UI; Route Prefetching | 3 | Planned |
| Route Prefetching | `route-prefetching.md` | Routing | Navigation | Critical | Intermediate | 12 min | Navigation & Linking; Route Loaders & Dependencies | Navigation & Linking; Transitions & Pending UI; Scroll Restoration | 3 | Planned |
| Route-Based Code Splitting | `route-based-code-splitting.md` | Routing | Code Organization | Critical | Intermediate | 12 min | Navigation & Linking | Route Guards & Redirects | 3 | Planned |
| Route Guards & Redirects | `route-guards-and-redirects.md` | Routing | Code Organization | Critical | Intermediate | 12 min | Route-Based Code Splitting; Navigation & Linking | Route-Based Code Splitting | 3 | Planned |

---

## 03 · Application Architecture  ·  Priority: Critical  ·  84 articles

### API Design & Contracts  (14 articles · ~233 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REST | `rest.md` | API Design & Contracts | Paradigms | Critical | Advanced | 16 min | HTTP/1.1 Semantics · Networking & Protocols; Structural Typing · TypeScript | GraphQL; RPC; Realtime & Subscriptions | 4 | Planned |
| GraphQL | `graphql.md` | API Design & Contracts | Paradigms | Critical | Advanced | 16 min | REST | REST; RPC; Realtime & Subscriptions | 4 | Planned |
| RPC | `rpc.md` | API Design & Contracts | Paradigms | Critical | Advanced | 16 min | REST | REST; GraphQL; Realtime & Subscriptions | 4 | Planned |
| Realtime & Subscriptions | `realtime-and-subscriptions.md` | API Design & Contracts | Paradigms | Critical | Advanced | 16 min | REST | REST; GraphQL; RPC | 4 | Planned |
| Resource & Schema Design | `resource-and-schema-design.md` | API Design & Contracts | Contract Design | Critical | Advanced | 16 min | REST | Versioning Strategies; Pagination & Filtering Conventions; Error Contract Design | 4 | Planned |
| Versioning Strategies | `versioning-strategies.md` | API Design & Contracts | Contract Design | Critical | Advanced | 16 min | Resource & Schema Design; REST | Resource & Schema Design; Pagination & Filtering Conventions; Error Contract Design | 4 | Planned |
| Pagination & Filtering Conventions | `pagination-and-filtering-conventions.md` | API Design & Contracts | Contract Design | Critical | Advanced | 19 min | Resource & Schema Design; REST | Resource & Schema Design; Versioning Strategies; Error Contract Design | 4 | Planned |
| Error Contract Design | `error-contract-design.md` | API Design & Contracts | Contract Design | Critical | Advanced | 16 min | Resource & Schema Design; REST | Resource & Schema Design; Versioning Strategies; Pagination & Filtering Conventions | 4 | Planned |
| End-to-End Type Safety (tRPC) | `end-to-end-type-safety-trpc.md` | API Design & Contracts | Type Safety Across the Wire | Critical | Advanced | 19 min | Resource & Schema Design | Code Generation from Schemas; Contract Testing | 4 | Planned |
| Code Generation from Schemas | `code-generation-from-schemas.md` | API Design & Contracts | Type Safety Across the Wire | Critical | Advanced | 19 min | End-to-End Type Safety (tRPC); Resource & Schema Design | End-to-End Type Safety (tRPC); Contract Testing | 4 | Planned |
| Contract Testing | `contract-testing.md` | API Design & Contracts | Type Safety Across the Wire | Critical | Advanced | 16 min | End-to-End Type Safety (tRPC); Resource & Schema Design | End-to-End Type Safety (tRPC); Code Generation from Schemas | 4 | Planned |
| Backend-for-Frontend | `backend-for-frontend.md` | API Design & Contracts | BFF & Aggregation | Critical | Advanced | 16 min | End-to-End Type Safety (tRPC) | API Gateways & Aggregation; Response Shaping | 4 | Planned |
| API Gateways & Aggregation | `api-gateways-and-aggregation.md` | API Design & Contracts | BFF & Aggregation | Critical | Advanced | 16 min | Backend-for-Frontend; End-to-End Type Safety (tRPC) | Backend-for-Frontend; Response Shaping | 4 | Planned |
| Response Shaping | `response-shaping.md` | API Design & Contracts | BFF & Aggregation | Critical | Advanced | 16 min | Backend-for-Frontend; End-to-End Type Safety (tRPC) | Backend-for-Frontend; API Gateways & Aggregation | 4 | Planned |

### Frontend Architecture  (16 articles · ~210 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Separation of Concerns | `separation-of-concerns.md` | Frontend Architecture | Structure & Boundaries | Critical | Intermediate | 12 min | Elements vs Components · React; Structural Typing · TypeScript | Layered Architecture; Module Boundaries; Dependency Direction & Inversion | 3 | Planned |
| Layered Architecture | `layered-architecture.md` | Frontend Architecture | Structure & Boundaries | Critical | Intermediate | 12 min | Separation of Concerns | Separation of Concerns; Module Boundaries; Dependency Direction & Inversion | 3 | Planned |
| Module Boundaries | `module-boundaries.md` | Frontend Architecture | Structure & Boundaries | Critical | Intermediate | 12 min | Separation of Concerns | Separation of Concerns; Layered Architecture; Dependency Direction & Inversion | 3 | Planned |
| Dependency Direction & Inversion | `dependency-direction-and-inversion.md` | Frontend Architecture | Structure & Boundaries | Critical | Intermediate | 15 min | Separation of Concerns | Separation of Concerns; Layered Architecture; Module Boundaries | 3 | Planned |
| Feature-Based Structure | `feature-based-structure.md` | Frontend Architecture | Organizing Code | Critical | Intermediate | 12 min | Separation of Concerns | Domain-Driven Frontend; Colocation Principles | 3 | Planned |
| Domain-Driven Frontend | `domain-driven-frontend.md` | Frontend Architecture | Organizing Code | Critical | Intermediate | 12 min | Feature-Based Structure; Separation of Concerns | Feature-Based Structure; Colocation Principles | 3 | Planned |
| Colocation Principles | `colocation-principles.md` | Frontend Architecture | Organizing Code | Critical | Intermediate | 12 min | Feature-Based Structure; Separation of Concerns | Feature-Based Structure; Domain-Driven Frontend | 3 | Planned |
| Micro-Frontends | `micro-frontends.md` | Frontend Architecture | Composition at Scale | Critical | Advanced | 16 min | Feature-Based Structure | Module Federation; Shared Kernel & Contracts | 4 | Planned |
| Module Federation | `module-federation.md` | Frontend Architecture | Composition at Scale | Critical | Advanced | 16 min | Micro-Frontends; Feature-Based Structure | Micro-Frontends; Shared Kernel & Contracts | 4 | Planned |
| Shared Kernel & Contracts | `shared-kernel-and-contracts.md` | Frontend Architecture | Composition at Scale | Critical | Advanced | 16 min | Micro-Frontends; Feature-Based Structure | Micro-Frontends; Module Federation | 4 | Planned |
| Rendering Boundaries | `rendering-boundaries.md` | Frontend Architecture | Cross-Cutting Boundaries | Critical | Intermediate | 12 min | Micro-Frontends | Data-Fetching Boundaries; Client/Server Split | 3 | Planned |
| Data-Fetching Boundaries | `data-fetching-boundaries.md` | Frontend Architecture | Cross-Cutting Boundaries | Critical | Intermediate | 12 min | Rendering Boundaries; Micro-Frontends | Rendering Boundaries; Client/Server Split | 3 | Planned |
| Client/Server Split | `client-server-split.md` | Frontend Architecture | Cross-Cutting Boundaries | Critical | Intermediate | 12 min | Rendering Boundaries; Micro-Frontends | Rendering Boundaries; Data-Fetching Boundaries | 3 | Planned |
| Architectural Decision Records | `architectural-decision-records.md` | Frontend Architecture | Decision-Making | Critical | Intermediate | 15 min | Rendering Boundaries | Trade-off Analysis; Evolutionary Architecture | 3 | Planned |
| Trade-off Analysis | `trade-off-analysis.md` | Frontend Architecture | Decision-Making | Critical | Intermediate | 12 min | Architectural Decision Records; Rendering Boundaries | Architectural Decision Records; Evolutionary Architecture | 3 | Planned |
| Evolutionary Architecture | `evolutionary-architecture.md` | Frontend Architecture | Decision-Making | Critical | Intermediate | 12 min | Architectural Decision Records; Rendering Boundaries | Architectural Decision Records; Trade-off Analysis | 3 | Planned |

### Data & Server State  (20 articles · ~255 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fetch-on-Render vs Render-as-You-Fetch | `fetch-on-render-vs-render-as-you-fetch.md` | Data & Server State | Fetching Strategies | Critical | Intermediate | 15 min | HTTP/1.1 Semantics · Networking & Protocols; Elements vs Components · React; Categories of State · State Management | Parallel vs Waterfall Requests; Request Deduplication; Data Prefetching | 3 | Published |
| Parallel vs Waterfall Requests | `parallel-vs-waterfall-requests.md` | Data & Server State | Fetching Strategies | Critical | Intermediate | 15 min | Fetch-on-Render vs Render-as-You-Fetch | Fetch-on-Render vs Render-as-You-Fetch; Request Deduplication; Data Prefetching | 3 | Published |
| Request Deduplication | `request-deduplication.md` | Data & Server State | Fetching Strategies | Critical | Intermediate | 12 min | Fetch-on-Render vs Render-as-You-Fetch | Fetch-on-Render vs Render-as-You-Fetch; Parallel vs Waterfall Requests; Data Prefetching | 3 | Published |
| Data Prefetching | `data-prefetching.md` | Data & Server State | Fetching Strategies | Critical | Intermediate | 12 min | Fetch-on-Render vs Render-as-You-Fetch | Fetch-on-Render vs Render-as-You-Fetch; Parallel vs Waterfall Requests; Request Deduplication | 3 | Published |
| Cache Keys & Query Identity | `cache-keys-and-query-identity.md` | Data & Server State | Server-State Cache | Critical | Intermediate | 15 min | Fetch-on-Render vs Render-as-You-Fetch | Staleness & Revalidation; Cache Invalidation; Background Refetching | 3 | Published |
| Staleness & Revalidation | `staleness-and-revalidation.md` | Data & Server State | Server-State Cache | Critical | Intermediate | 12 min | Cache Keys & Query Identity; Fetch-on-Render vs Render-as-You-Fetch | Cache Keys & Query Identity; Cache Invalidation; Background Refetching | 3 | Published |
| Cache Invalidation | `cache-invalidation.md` | Data & Server State | Server-State Cache | Critical | Intermediate | 12 min | Cache Keys & Query Identity; Fetch-on-Render vs Render-as-You-Fetch | Cache Keys & Query Identity; Staleness & Revalidation; Background Refetching | 3 | Published |
| Background Refetching | `background-refetching.md` | Data & Server State | Server-State Cache | Critical | Intermediate | 12 min | Cache Keys & Query Identity; Fetch-on-Render vs Render-as-You-Fetch | Cache Keys & Query Identity; Staleness & Revalidation; Cache Invalidation | 3 | Published |
| Mutation Lifecycle | `mutation-lifecycle.md` | Data & Server State | Mutations | Critical | Intermediate | 12 min | Cache Keys & Query Identity | Optimistic Updates; Rollback & Conflict Resolution | 3 | Published |
| Optimistic Updates | `optimistic-updates.md` | Data & Server State | Mutations | Critical | Intermediate | 12 min | Mutation Lifecycle; Cache Keys & Query Identity | Mutation Lifecycle; Rollback & Conflict Resolution | 3 | Published |
| Rollback & Conflict Resolution | `rollback-and-conflict-resolution.md` | Data & Server State | Mutations | Critical | Intermediate | 15 min | Mutation Lifecycle; Cache Keys & Query Identity | Mutation Lifecycle; Optimistic Updates | 3 | Published |
| Pagination | `pagination.md` | Data & Server State | Large Data Sets | Critical | Intermediate | 12 min | Mutation Lifecycle | Infinite & Cursor Loading; List Virtualization | 3 | Published |
| Infinite & Cursor Loading | `infinite-and-cursor-loading.md` | Data & Server State | Large Data Sets | Critical | Intermediate | 12 min | Pagination; Mutation Lifecycle | Pagination; List Virtualization | 3 | Published |
| List Virtualization | `list-virtualization.md` | Data & Server State | Large Data Sets | Critical | Intermediate | 12 min | Pagination; Mutation Lifecycle | Pagination; Infinite & Cursor Loading | 3 | Published |
| Normalizing Server Responses | `normalizing-server-responses.md` | Data & Server State | Data Modeling | Critical | Intermediate | 15 min | Pagination | Client-Side Relations; Derived Server Data | 3 | Published |
| Client-Side Relations | `client-side-relations.md` | Data & Server State | Data Modeling | Critical | Intermediate | 12 min | Normalizing Server Responses; Pagination | Normalizing Server Responses; Derived Server Data | 3 | Published |
| Derived Server Data | `derived-server-data.md` | Data & Server State | Data Modeling | Critical | Intermediate | 12 min | Normalizing Server Responses; Pagination | Normalizing Server Responses; Client-Side Relations | 3 | Published |
| Retries & Backoff | `retries-and-backoff.md` | Data & Server State | Resilience | Critical | Intermediate | 12 min | Normalizing Server Responses | Loading & Error States; Offline & Local-First Sync | 3 | Published |
| Loading & Error States | `loading-and-error-states.md` | Data & Server State | Resilience | Critical | Intermediate | 12 min | Retries & Backoff; Normalizing Server Responses | Retries & Backoff; Offline & Local-First Sync | 3 | Published |
| Offline & Local-First Sync | `offline-and-local-first-sync.md` | Data & Server State | Resilience | Critical | Intermediate | 12 min | Retries & Backoff; Normalizing Server Responses | Retries & Backoff; Loading & Error States | 3 | Planned |

### Forms & Validation  (16 articles · ~213 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Controlled Inputs | `controlled-inputs.md` | Forms & Validation | Form State | Critical | Intermediate | 12 min | Elements vs Components · React; Structural Typing · TypeScript; Categories of State · State Management | Uncontrolled Inputs & Refs; Form Libraries & State Models; Field Arrays & Dynamic Fields | 3 | Planned |
| Uncontrolled Inputs & Refs | `uncontrolled-inputs-and-refs.md` | Forms & Validation | Form State | Critical | Intermediate | 12 min | Controlled Inputs | Controlled Inputs; Form Libraries & State Models; Field Arrays & Dynamic Fields | 3 | Planned |
| Form Libraries & State Models | `form-libraries-and-state-models.md` | Forms & Validation | Form State | Critical | Intermediate | 15 min | Controlled Inputs | Controlled Inputs; Uncontrolled Inputs & Refs; Field Arrays & Dynamic Fields | 3 | Published |
| Field Arrays & Dynamic Fields | `field-arrays-and-dynamic-fields.md` | Forms & Validation | Form State | Critical | Intermediate | 15 min | Controlled Inputs | Controlled Inputs; Uncontrolled Inputs & Refs; Form Libraries & State Models | 3 | Planned |
| Client-Side Validation Strategies | `client-side-validation-strategies.md` | Forms & Validation | Validation | Critical | Intermediate | 15 min | Controlled Inputs | Schema Validation; Async & Server Validation; Cross-Field Validation | 3 | Planned |
| Schema Validation | `schema-validation.md` | Forms & Validation | Validation | Critical | Intermediate | 12 min | Client-Side Validation Strategies; Controlled Inputs | Client-Side Validation Strategies; Async & Server Validation; Cross-Field Validation | 3 | Published |
| Async & Server Validation | `async-and-server-validation.md` | Forms & Validation | Validation | Critical | Intermediate | 12 min | Client-Side Validation Strategies; Controlled Inputs | Client-Side Validation Strategies; Schema Validation; Cross-Field Validation | 3 | Planned |
| Cross-Field Validation | `cross-field-validation.md` | Forms & Validation | Validation | Critical | Intermediate | 12 min | Client-Side Validation Strategies; Controlled Inputs | Client-Side Validation Strategies; Schema Validation; Async & Server Validation | 3 | Planned |
| Schema-Inferred Types | `schema-inferred-types.md` | Forms & Validation | Type-Safe Contracts | Critical | Intermediate | 12 min | Client-Side Validation Strategies | Shared Client/Server Schemas | 3 | Published |
| Shared Client/Server Schemas | `shared-client-server-schemas.md` | Forms & Validation | Type-Safe Contracts | Critical | Intermediate | 15 min | Schema-Inferred Types; Client-Side Validation Strategies | Schema-Inferred Types | 3 | Planned |
| Error Messaging | `error-messaging.md` | Forms & Validation | Feedback & UX | Critical | Intermediate | 12 min | Schema-Inferred Types | Inline vs Submit Validation; Dirty, Touched & Submit State | 3 | Published |
| Inline vs Submit Validation | `inline-vs-submit-validation.md` | Forms & Validation | Feedback & UX | Critical | Intermediate | 15 min | Error Messaging; Schema-Inferred Types | Error Messaging; Dirty, Touched & Submit State | 3 | Planned |
| Dirty, Touched & Submit State | `dirty-touched-and-submit-state.md` | Forms & Validation | Feedback & UX | Critical | Intermediate | 15 min | Error Messaging; Schema-Inferred Types | Error Messaging; Inline vs Submit Validation | 3 | Planned |
| Composite & Custom Inputs | `composite-and-custom-inputs.md` | Forms & Validation | Complex Flows | Critical | Intermediate | 12 min | Error Messaging | Multi-Step Wizards; Autosave & Draft Persistence | 3 | Planned |
| Multi-Step Wizards | `multi-step-wizards.md` | Forms & Validation | Complex Flows | Critical | Intermediate | 12 min | Composite & Custom Inputs; Error Messaging | Composite & Custom Inputs; Autosave & Draft Persistence | 3 | Planned |
| Autosave & Draft Persistence | `autosave-and-draft-persistence.md` | Forms & Validation | Complex Flows | Critical | Intermediate | 15 min | Composite & Custom Inputs; Error Messaging | Composite & Custom Inputs; Multi-Step Wizards | 3 | Planned |

### State Management  (18 articles · ~231 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Categories of State | `categories-of-state.md` | State Management | State Taxonomy | Critical | Intermediate | 12 min | Elements vs Components · React; Primitives & Wrappers · JavaScript | Server vs Client State; UI vs Domain State; Ephemeral vs Persistent State | 3 | Published |
| Server vs Client State | `server-vs-client-state.md` | State Management | State Taxonomy | Critical | Intermediate | 12 min | Categories of State | Categories of State; UI vs Domain State; Ephemeral vs Persistent State | 3 | Published |
| UI vs Domain State | `ui-vs-domain-state.md` | State Management | State Taxonomy | Critical | Intermediate | 12 min | Categories of State | Categories of State; Server vs Client State; Ephemeral vs Persistent State | 3 | Published |
| Ephemeral vs Persistent State | `ephemeral-vs-persistent-state.md` | State Management | State Taxonomy | Critical | Intermediate | 15 min | Categories of State | Categories of State; Server vs Client State; UI vs Domain State | 3 | Planned |
| Local State | `local-state.md` | State Management | State Ownership | Critical | Intermediate | 12 min | Categories of State | Lifting State Up; Global State; Colocation vs Centralization | 3 | Published |
| Lifting State Up | `lifting-state-up.md` | State Management | State Ownership | Critical | Intermediate | 12 min | Local State; Categories of State | Local State; Global State; Colocation vs Centralization | 3 | Published |
| Global State | `global-state.md` | State Management | State Ownership | Critical | Intermediate | 12 min | Local State; Categories of State | Local State; Lifting State Up; Colocation vs Centralization | 3 | Planned |
| Colocation vs Centralization | `colocation-vs-centralization.md` | State Management | State Ownership | Critical | Intermediate | 15 min | Local State; Categories of State | Local State; Lifting State Up; Global State | 3 | Planned |
| Computed Values | `computed-values.md` | State Management | Derived State | Critical | Intermediate | 12 min | Local State | Selectors & Memoized Selectors; Store Shape & Normalization | 3 | Planned |
| Selectors & Memoized Selectors | `selectors-and-memoized-selectors.md` | State Management | Derived State | Critical | Intermediate | 15 min | Computed Values; Local State | Computed Values; Store Shape & Normalization | 3 | Planned |
| Store Shape & Normalization | `store-shape-and-normalization.md` | State Management | Derived State | Critical | Intermediate | 15 min | Computed Values; Local State | Computed Values; Selectors & Memoized Selectors | 3 | Planned |
| The Reducer Pattern | `the-reducer-pattern.md` | State Management | State Patterns | Critical | Intermediate | 12 min | Computed Values | Unidirectional Data Flow; Event Sourcing & Commands; Modeling UI with State Machines | 3 | Planned |
| Unidirectional Data Flow | `unidirectional-data-flow.md` | State Management | State Patterns | Critical | Intermediate | 12 min | The Reducer Pattern; Computed Values | The Reducer Pattern; Event Sourcing & Commands; Modeling UI with State Machines | 3 | Planned |
| Event Sourcing & Commands | `event-sourcing-and-commands.md` | State Management | State Patterns | Critical | Intermediate | 12 min | The Reducer Pattern; Computed Values | The Reducer Pattern; Unidirectional Data Flow; Modeling UI with State Machines | 3 | Planned |
| Modeling UI with State Machines | `modeling-ui-with-state-machines.md` | State Management | State Patterns | Critical | Intermediate | 15 min | The Reducer Pattern; Computed Values | The Reducer Pattern; Unidirectional Data Flow; Event Sourcing & Commands | 3 | Planned |
| Store-Based Libraries | `store-based-libraries.md` | State Management | Libraries & Models | Critical | Intermediate | 12 min | The Reducer Pattern | Atom-Based Libraries; Proxy-Based Reactivity | 3 | Planned |
| Atom-Based Libraries | `atom-based-libraries.md` | State Management | Libraries & Models | Critical | Intermediate | 12 min | Store-Based Libraries; The Reducer Pattern | Store-Based Libraries; Proxy-Based Reactivity | 3 | Planned |
| Proxy-Based Reactivity | `proxy-based-reactivity.md` | State Management | Libraries & Models | Critical | Intermediate | 12 min | Store-Based Libraries; The Reducer Pattern | Store-Based Libraries; Atom-Based Libraries | 3 | Planned |

---

## 04 · Interface Engineering  ·  Priority: High  ·  64 articles

### Accessibility  (19 articles · ~237 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| WCAG Principles (POUR) | `wcag-principles-pour.md` | Accessibility | Standards | High | Intermediate | 12 min | The Document Outline · HTML & Document Semantics; Prop Design & Contracts · Component & Interaction Design | Conformance Levels; The ARIA Model; Accessible Name Computation | 3 | Published |
| Conformance Levels | `conformance-levels.md` | Accessibility | Standards | High | Intermediate | 12 min | WCAG Principles (POUR) | WCAG Principles (POUR); The ARIA Model; Accessible Name Computation | 3 | Planned |
| The ARIA Model | `the-aria-model.md` | Accessibility | Standards | High | Intermediate | 12 min | WCAG Principles (POUR) | WCAG Principles (POUR); Conformance Levels; Accessible Name Computation | 3 | Planned |
| Accessible Name Computation | `accessible-name-computation.md` | Accessibility | Standards | High | Intermediate | 15 min | WCAG Principles (POUR) | WCAG Principles (POUR); Conformance Levels; The ARIA Model | 3 | Planned |
| Role, Name, State | `role-name-state.md` | Accessibility | The Accessibility Tree | High | Intermediate | 12 min | WCAG Principles (POUR) | The Tree & Assistive Tech; Screen Reader Behavior | 3 | Planned |
| The Tree & Assistive Tech | `the-tree-and-assistive-tech.md` | Accessibility | The Accessibility Tree | High | Intermediate | 12 min | Role, Name, State; WCAG Principles (POUR) | Role, Name, State; Screen Reader Behavior | 3 | Planned |
| Screen Reader Behavior | `screen-reader-behavior.md` | Accessibility | The Accessibility Tree | High | Intermediate | 12 min | Role, Name, State; WCAG Principles (POUR) | Role, Name, State; The Tree & Assistive Tech | 3 | Planned |
| Keyboard Navigation | `keyboard-navigation.md` | Accessibility | Keyboard & Focus | High | Intermediate | 12 min | Role, Name, State | Focus Management; Focus Order & Tab Trapping; Skip Links & Landmarks | 3 | Planned |
| Focus Management | `focus-management.md` | Accessibility | Keyboard & Focus | High | Intermediate | 12 min | Keyboard Navigation; Role, Name, State | Keyboard Navigation; Focus Order & Tab Trapping; Skip Links & Landmarks | 3 | Planned |
| Focus Order & Tab Trapping | `focus-order-and-tab-trapping.md` | Accessibility | Keyboard & Focus | High | Intermediate | 12 min | Keyboard Navigation; Role, Name, State | Keyboard Navigation; Focus Management; Skip Links & Landmarks | 3 | Planned |
| Skip Links & Landmarks | `skip-links-and-landmarks.md` | Accessibility | Keyboard & Focus | High | Intermediate | 12 min | Keyboard Navigation; Role, Name, State | Keyboard Navigation; Focus Management; Focus Order & Tab Trapping | 3 | Planned |
| Color Contrast Conformance | `color-contrast-conformance.md` | Accessibility | Perceivable UI | High | Intermediate | 12 min | Keyboard Navigation | Text Alternatives; Reduced Motion & Vestibular Safety | 3 | Planned |
| Text Alternatives | `text-alternatives.md` | Accessibility | Perceivable UI | High | Intermediate | 12 min | Color Contrast Conformance; Keyboard Navigation | Color Contrast Conformance; Reduced Motion & Vestibular Safety | 3 | Planned |
| Reduced Motion & Vestibular Safety | `reduced-motion-and-vestibular-safety.md` | Accessibility | Perceivable UI | High | Intermediate | 15 min | Color Contrast Conformance; Keyboard Navigation | Color Contrast Conformance; Text Alternatives | 3 | Planned |
| WAI-ARIA Widget Patterns | `wai-aria-widget-patterns.md` | Accessibility | Accessible Patterns | High | Intermediate | 12 min | Color Contrast Conformance | Accessible Forms; Live Regions & Announcements | 3 | Planned |
| Accessible Forms | `accessible-forms.md` | Accessibility | Accessible Patterns | High | Intermediate | 12 min | WAI-ARIA Widget Patterns; Color Contrast Conformance | WAI-ARIA Widget Patterns; Live Regions & Announcements | 3 | Planned |
| Live Regions & Announcements | `live-regions-and-announcements.md` | Accessibility | Accessible Patterns | High | Intermediate | 15 min | WAI-ARIA Widget Patterns; Color Contrast Conformance | WAI-ARIA Widget Patterns; Accessible Forms | 3 | Planned |
| Automated Auditing | `automated-auditing.md` | Accessibility | Verification | High | Intermediate | 12 min | WAI-ARIA Widget Patterns | Manual & AT Testing | 3 | Planned |
| Manual & AT Testing | `manual-and-at-testing.md` | Accessibility | Verification | High | Intermediate | 12 min | Automated Auditing; WAI-ARIA Widget Patterns | Automated Auditing | 3 | Planned |

### Animation & Motion  (14 articles · ~168 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Easing & Timing | `easing-and-timing.md` | Animation & Motion | Motion Principles | High | Intermediate | 12 min | Specificity · CSS & Visual Systems; Process & Thread Architecture · The Web Platform | Choreography & Sequencing; Purposeful Motion | 3 | Planned |
| Choreography & Sequencing | `choreography-and-sequencing.md` | Animation & Motion | Motion Principles | High | Intermediate | 12 min | Easing & Timing | Easing & Timing; Purposeful Motion | 3 | Planned |
| Purposeful Motion | `purposeful-motion.md` | Animation & Motion | Motion Principles | High | Intermediate | 12 min | Easing & Timing | Easing & Timing; Choreography & Sequencing | 3 | Planned |
| CSS Transitions | `css-transitions.md` | Animation & Motion | Techniques | High | Intermediate | 12 min | Easing & Timing | CSS Animations & Keyframes; The Web Animations API; The View Transitions API; Spring & Physics Animation | 3 | Planned |
| CSS Animations & Keyframes | `css-animations-and-keyframes.md` | Animation & Motion | Techniques | High | Intermediate | 12 min | CSS Transitions; Easing & Timing | CSS Transitions; The Web Animations API; The View Transitions API; Spring & Physics Animation | 3 | Planned |
| The Web Animations API | `the-web-animations-api.md` | Animation & Motion | Techniques | High | Intermediate | 12 min | CSS Transitions; Easing & Timing | CSS Transitions; CSS Animations & Keyframes; The View Transitions API; Spring & Physics Animation | 3 | Planned |
| The View Transitions API | `the-view-transitions-api.md` | Animation & Motion | Techniques | High | Intermediate | 12 min | CSS Transitions; Easing & Timing | CSS Transitions; CSS Animations & Keyframes; The Web Animations API; Spring & Physics Animation | 3 | Planned |
| Spring & Physics Animation | `spring-and-physics-animation.md` | Animation & Motion | Techniques | High | Intermediate | 12 min | CSS Transitions; Easing & Timing | CSS Transitions; CSS Animations & Keyframes; The Web Animations API; The View Transitions API | 3 | Planned |
| Compositor-Only Properties | `compositor-only-properties.md` | Animation & Motion | Performance | High | Intermediate | 12 min | CSS Transitions | Avoiding Layout Thrash; The FLIP Technique | 3 | Planned |
| Avoiding Layout Thrash | `avoiding-layout-thrash.md` | Animation & Motion | Performance | High | Intermediate | 12 min | Compositor-Only Properties; CSS Transitions | Compositor-Only Properties; The FLIP Technique | 3 | Planned |
| The FLIP Technique | `the-flip-technique.md` | Animation & Motion | Performance | High | Intermediate | 12 min | Compositor-Only Properties; CSS Transitions | Compositor-Only Properties; Avoiding Layout Thrash | 3 | Planned |
| Gesture-Driven Animation | `gesture-driven-animation.md` | Animation & Motion | Interaction Motion | High | Intermediate | 12 min | Compositor-Only Properties | Scroll-Linked Animation; Shared-Element Transitions | 3 | Planned |
| Scroll-Linked Animation | `scroll-linked-animation.md` | Animation & Motion | Interaction Motion | High | Intermediate | 12 min | Gesture-Driven Animation; Compositor-Only Properties | Gesture-Driven Animation; Shared-Element Transitions | 3 | Planned |
| Shared-Element Transitions | `shared-element-transitions.md` | Animation & Motion | Interaction Motion | High | Intermediate | 12 min | Gesture-Driven Animation; Compositor-Only Properties | Gesture-Driven Animation; Scroll-Linked Animation | 3 | Planned |

### Component & Interaction Design  (16 articles · ~207 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Prop Design & Contracts | `prop-design-and-contracts.md` | Component & Interaction Design | Component APIs | High | Intermediate | 12 min | Elements vs Components · React; Specificity · CSS & Visual Systems | Composition vs Configuration; Polymorphic Components (as); Slots & Children APIs | 3 | Planned |
| Composition vs Configuration | `composition-vs-configuration.md` | Component & Interaction Design | Component APIs | High | Intermediate | 15 min | Prop Design & Contracts | Prop Design & Contracts; Polymorphic Components (as); Slots & Children APIs | 3 | Planned |
| Polymorphic Components (as) | `polymorphic-components-as.md` | Component & Interaction Design | Component APIs | High | Intermediate | 15 min | Prop Design & Contracts | Prop Design & Contracts; Composition vs Configuration; Slots & Children APIs | 3 | Planned |
| Slots & Children APIs | `slots-and-children-apis.md` | Component & Interaction Design | Component APIs | High | Intermediate | 12 min | Prop Design & Contracts | Prop Design & Contracts; Composition vs Configuration; Polymorphic Components (as) | 3 | Planned |
| Headless Components | `headless-components.md` | Component & Interaction Design | Behavior Patterns | High | Intermediate | 12 min | Prop Design & Contracts | Controlled vs Uncontrolled Pattern; Compound Components; Render Props | 3 | Planned |
| Controlled vs Uncontrolled Pattern | `controlled-vs-uncontrolled-pattern.md` | Component & Interaction Design | Behavior Patterns | High | Intermediate | 15 min | Headless Components; Prop Design & Contracts | Headless Components; Compound Components; Render Props | 3 | Planned |
| Compound Components | `compound-components.md` | Component & Interaction Design | Behavior Patterns | High | Intermediate | 12 min | Headless Components; Prop Design & Contracts | Headless Components; Controlled vs Uncontrolled Pattern; Render Props | 3 | Planned |
| Render Props | `render-props.md` | Component & Interaction Design | Behavior Patterns | High | Intermediate | 12 min | Headless Components; Prop Design & Contracts | Headless Components; Controlled vs Uncontrolled Pattern; Compound Components | 3 | Planned |
| Pointer & Mouse Interaction | `pointer-and-mouse-interaction.md` | Component & Interaction Design | Interaction | High | Intermediate | 15 min | Headless Components | Drag & Drop; Hover, Press & Long-Press States; Gesture Handling | 3 | Planned |
| Drag & Drop | `drag-and-drop.md` | Component & Interaction Design | Interaction | High | Intermediate | 12 min | Pointer & Mouse Interaction; Headless Components | Pointer & Mouse Interaction; Hover, Press & Long-Press States; Gesture Handling | 3 | Planned |
| Hover, Press & Long-Press States | `hover-press-and-long-press-states.md` | Component & Interaction Design | Interaction | High | Intermediate | 15 min | Pointer & Mouse Interaction; Headless Components | Pointer & Mouse Interaction; Drag & Drop; Gesture Handling | 3 | Planned |
| Gesture Handling | `gesture-handling.md` | Component & Interaction Design | Interaction | High | Intermediate | 12 min | Pointer & Mouse Interaction; Headless Components | Pointer & Mouse Interaction; Drag & Drop; Hover, Press & Long-Press States | 3 | Planned |
| Loading & Skeleton States | `loading-and-skeleton-states.md` | Component & Interaction Design | Interface State | High | Intermediate | 12 min | Pointer & Mouse Interaction | Empty States; Error & Retry States; Disabled & Busy States | 3 | Planned |
| Empty States | `empty-states.md` | Component & Interaction Design | Interface State | High | Intermediate | 12 min | Loading & Skeleton States; Pointer & Mouse Interaction | Loading & Skeleton States; Error & Retry States; Disabled & Busy States | 3 | Planned |
| Error & Retry States | `error-and-retry-states.md` | Component & Interaction Design | Interface State | High | Intermediate | 12 min | Loading & Skeleton States; Pointer & Mouse Interaction | Loading & Skeleton States; Empty States; Disabled & Busy States | 3 | Planned |
| Disabled & Busy States | `disabled-and-busy-states.md` | Component & Interaction Design | Interface State | High | Intermediate | 12 min | Loading & Skeleton States; Pointer & Mouse Interaction | Loading & Skeleton States; Empty States; Error & Retry States | 3 | Planned |

### Design Systems  (15 articles · ~192 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Design Primitives | `design-primitives.md` | Design Systems | Foundations | High | Intermediate | 12 min | Specificity · CSS & Visual Systems; Prop Design & Contracts · Component & Interaction Design | Spacing & Layout Scales; Elevation & Surfaces | 3 | Planned |
| Spacing & Layout Scales | `spacing-and-layout-scales.md` | Design Systems | Foundations | High | Intermediate | 12 min | Design Primitives | Design Primitives; Elevation & Surfaces | 3 | Planned |
| Elevation & Surfaces | `elevation-and-surfaces.md` | Design Systems | Foundations | High | Intermediate | 12 min | Design Primitives | Design Primitives; Spacing & Layout Scales | 3 | Planned |
| Token Architecture | `token-architecture.md` | Design Systems | Tokens | High | Intermediate | 12 min | Design Primitives | Semantic Token Layers; Token Transformation & Distribution | 3 | Planned |
| Semantic Token Layers | `semantic-token-layers.md` | Design Systems | Tokens | High | Intermediate | 12 min | Token Architecture; Design Primitives | Token Architecture; Token Transformation & Distribution | 3 | Planned |
| Token Transformation & Distribution | `token-transformation-and-distribution.md` | Design Systems | Tokens | High | Intermediate | 15 min | Token Architecture; Design Primitives | Token Architecture; Semantic Token Layers | 3 | Planned |
| Light/Dark & Color Modes | `light-dark-and-color-modes.md` | Design Systems | Theming | High | Intermediate | 12 min | Token Architecture | Multi-Brand Theming; Runtime vs Build-Time Theming | 3 | Planned |
| Multi-Brand Theming | `multi-brand-theming.md` | Design Systems | Theming | High | Intermediate | 12 min | Light/Dark & Color Modes; Token Architecture | Light/Dark & Color Modes; Runtime vs Build-Time Theming | 3 | Planned |
| Runtime vs Build-Time Theming | `runtime-vs-build-time-theming.md` | Design Systems | Theming | High | Intermediate | 15 min | Light/Dark & Color Modes; Token Architecture | Light/Dark & Color Modes; Multi-Brand Theming | 3 | Planned |
| Contribution Model | `contribution-model.md` | Design Systems | Governance | High | Intermediate | 12 min | Light/Dark & Color Modes | Versioning & Deprecation; Breaking Changes & Migration | 3 | Planned |
| Versioning & Deprecation | `versioning-and-deprecation.md` | Design Systems | Governance | High | Intermediate | 12 min | Contribution Model; Light/Dark & Color Modes | Contribution Model; Breaking Changes & Migration | 3 | Planned |
| Breaking Changes & Migration | `breaking-changes-and-migration.md` | Design Systems | Governance | High | Intermediate | 15 min | Contribution Model; Light/Dark & Color Modes | Contribution Model; Versioning & Deprecation | 3 | Planned |
| Usage Guidelines | `usage-guidelines.md` | Design Systems | Adoption | High | Intermediate | 12 min | Contribution Model | Living Docs & Playgrounds; Adoption & Coverage Metrics | 3 | Planned |
| Living Docs & Playgrounds | `living-docs-and-playgrounds.md` | Design Systems | Adoption | High | Intermediate | 12 min | Usage Guidelines; Contribution Model | Usage Guidelines; Adoption & Coverage Metrics | 3 | Planned |
| Adoption & Coverage Metrics | `adoption-and-coverage-metrics.md` | Design Systems | Adoption | High | Intermediate | 15 min | Usage Guidelines; Contribution Model | Usage Guidelines; Living Docs & Playgrounds | 3 | Planned |

---

## 05 · Reliability & Quality  ·  Priority: Critical  ·  79 articles

### Observability & Reliability  (15 articles · ~255 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Client Error Capture | `client-error-capture.md` | Observability & Reliability | Error Tracking | Critical | Advanced | 16 min | Core Web Vitals (LCP, INP, CLS) · Performance Engineering; Static Hosting · Delivery & Infrastructure | Source Maps & Symbolication; Error Grouping & Alerting | 4 | Planned |
| Source Maps & Symbolication | `source-maps-and-symbolication.md` | Observability & Reliability | Error Tracking | Critical | Advanced | 19 min | Client Error Capture | Client Error Capture; Error Grouping & Alerting | 4 | Planned |
| Error Grouping & Alerting | `error-grouping-and-alerting.md` | Observability & Reliability | Error Tracking | Critical | Advanced | 16 min | Client Error Capture | Client Error Capture; Source Maps & Symbolication | 4 | Planned |
| RUM & Field Vitals | `rum-and-field-vitals.md` | Observability & Reliability | Real-User Monitoring | Critical | Advanced | 16 min | Client Error Capture | Session Replay; Sampling Strategies | 4 | Planned |
| Session Replay | `session-replay.md` | Observability & Reliability | Real-User Monitoring | Critical | Advanced | 16 min | RUM & Field Vitals; Client Error Capture | RUM & Field Vitals; Sampling Strategies | 4 | Planned |
| Sampling Strategies | `sampling-strategies.md` | Observability & Reliability | Real-User Monitoring | Critical | Advanced | 16 min | RUM & Field Vitals; Client Error Capture | RUM & Field Vitals; Session Replay | 4 | Planned |
| Structured Logging | `structured-logging.md` | Observability & Reliability | Instrumentation | Critical | Advanced | 16 min | RUM & Field Vitals | Frontend Tracing & Spans; Custom Metrics & Events | 4 | Planned |
| Frontend Tracing & Spans | `frontend-tracing-and-spans.md` | Observability & Reliability | Instrumentation | Critical | Advanced | 16 min | Structured Logging; RUM & Field Vitals | Structured Logging; Custom Metrics & Events | 4 | Planned |
| Custom Metrics & Events | `custom-metrics-and-events.md` | Observability & Reliability | Instrumentation | Critical | Advanced | 16 min | Structured Logging; RUM & Field Vitals | Structured Logging; Frontend Tracing & Spans | 4 | Planned |
| Analytics Events | `analytics-events.md` | Observability & Reliability | Product Telemetry | Critical | Advanced | 16 min | Structured Logging | Funnels & Conversion; Privacy-Safe Analytics | 4 | Planned |
| Funnels & Conversion | `funnels-and-conversion.md` | Observability & Reliability | Product Telemetry | Critical | Advanced | 16 min | Analytics Events; Structured Logging | Analytics Events; Privacy-Safe Analytics | 4 | Planned |
| Privacy-Safe Analytics | `privacy-safe-analytics.md` | Observability & Reliability | Product Telemetry | Critical | Advanced | 16 min | Analytics Events; Structured Logging | Analytics Events; Funnels & Conversion | 4 | Planned |
| On-Call & Alerting | `on-call-and-alerting.md` | Observability & Reliability | Incident Response | Critical | Staff | 20 min | Analytics Events | Postmortems & RCA; Error Budgets & SLOs | 1 | Planned |
| Postmortems & RCA | `postmortems-and-rca.md` | Observability & Reliability | Incident Response | Critical | Staff | 20 min | On-Call & Alerting; Analytics Events | On-Call & Alerting; Error Budgets & SLOs | 1 | Planned |
| Error Budgets & SLOs | `error-budgets-and-slos.md` | Observability & Reliability | Incident Response | Critical | Staff | 20 min | On-Call & Alerting; Analytics Events | On-Call & Alerting; Postmortems & RCA | 1 | Planned |

### Performance Engineering  (22 articles · ~303 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Core Web Vitals (LCP, INP, CLS) | `core-web-vitals-lcp-inp-cls.md` | Performance Engineering | Metrics | Critical | Intermediate | 15 min | Process & Thread Architecture · The Web Platform; Parsing & Bytecode · Runtime & Execution; HTTP/1.1 Semantics · Networking & Protocols | Perceived vs Actual Performance; Custom Performance Metrics; Lab vs Field Measurement | 3 | Published |
| Perceived vs Actual Performance | `perceived-vs-actual-performance.md` | Performance Engineering | Metrics | Critical | Intermediate | 15 min | Core Web Vitals (LCP, INP, CLS) | Core Web Vitals (LCP, INP, CLS); Custom Performance Metrics; Lab vs Field Measurement | 3 | Planned |
| Custom Performance Metrics | `custom-performance-metrics.md` | Performance Engineering | Metrics | Critical | Intermediate | 12 min | Core Web Vitals (LCP, INP, CLS) | Core Web Vitals (LCP, INP, CLS); Perceived vs Actual Performance; Lab vs Field Measurement | 3 | Planned |
| Lab vs Field Measurement | `lab-vs-field-measurement.md` | Performance Engineering | Metrics | Critical | Intermediate | 12 min | Core Web Vitals (LCP, INP, CLS) | Core Web Vitals (LCP, INP, CLS); Perceived vs Actual Performance; Custom Performance Metrics | 3 | Planned |
| The Critical Rendering Path | `the-critical-rendering-path.md` | Performance Engineering | Loading Performance | Critical | Intermediate | 15 min | Core Web Vitals (LCP, INP, CLS) | Code Splitting; Resource Prefetch & Preload; Critical CSS & Above-the-Fold; Font & Asset Loading Strategy | 3 | Published |
| Code Splitting | `code-splitting.md` | Performance Engineering | Loading Performance | Critical | Intermediate | 12 min | The Critical Rendering Path; Core Web Vitals (LCP, INP, CLS) | The Critical Rendering Path; Resource Prefetch & Preload; Critical CSS & Above-the-Fold; Font & Asset Loading Strategy | 3 | Published |
| Resource Prefetch & Preload | `resource-prefetch-and-preload.md` | Performance Engineering | Loading Performance | Critical | Intermediate | 15 min | The Critical Rendering Path; Core Web Vitals (LCP, INP, CLS) | The Critical Rendering Path; Code Splitting; Critical CSS & Above-the-Fold; Font & Asset Loading Strategy | 3 | Published |
| Critical CSS & Above-the-Fold | `critical-css-and-above-the-fold.md` | Performance Engineering | Loading Performance | Critical | Intermediate | 15 min | The Critical Rendering Path; Core Web Vitals (LCP, INP, CLS) | The Critical Rendering Path; Code Splitting; Resource Prefetch & Preload; Font & Asset Loading Strategy | 3 | Planned |
| Font & Asset Loading Strategy | `font-and-asset-loading-strategy.md` | Performance Engineering | Loading Performance | Critical | Intermediate | 15 min | The Critical Rendering Path; Core Web Vitals (LCP, INP, CLS) | The Critical Rendering Path; Code Splitting; Resource Prefetch & Preload; Critical CSS & Above-the-Fold | 3 | Planned |
| Image Optimization | `image-optimization.md` | Performance Engineering | Asset Optimization | Critical | Intermediate | 12 min | The Critical Rendering Path | Media & Video Optimization; Bundle Size Optimization; Asset Minification & Compression | 3 | Planned |
| Media & Video Optimization | `media-and-video-optimization.md` | Performance Engineering | Asset Optimization | Critical | Intermediate | 12 min | Image Optimization; The Critical Rendering Path | Image Optimization; Bundle Size Optimization; Asset Minification & Compression | 3 | Planned |
| Bundle Size Optimization | `bundle-size-optimization.md` | Performance Engineering | Asset Optimization | Critical | Intermediate | 12 min | Image Optimization; The Critical Rendering Path | Image Optimization; Media & Video Optimization; Asset Minification & Compression | 3 | Planned |
| Asset Minification & Compression | `asset-minification-and-compression.md` | Performance Engineering | Asset Optimization | Critical | Intermediate | 15 min | Image Optimization; The Critical Rendering Path | Image Optimization; Media & Video Optimization; Bundle Size Optimization | 3 | Planned |
| Rendering Cost & Re-renders | `rendering-cost-and-re-renders.md` | Performance Engineering | Runtime Performance | Critical | Intermediate | 15 min | Image Optimization | Long Tasks & Main-Thread Work; Debounce, Throttle & Scheduling; Offloading to Workers | 3 | Planned |
| Long Tasks & Main-Thread Work | `long-tasks-and-main-thread-work.md` | Performance Engineering | Runtime Performance | Critical | Intermediate | 15 min | Rendering Cost & Re-renders; Image Optimization | Rendering Cost & Re-renders; Debounce, Throttle & Scheduling; Offloading to Workers | 3 | Planned |
| Debounce, Throttle & Scheduling | `debounce-throttle-and-scheduling.md` | Performance Engineering | Runtime Performance | Critical | Intermediate | 15 min | Rendering Cost & Re-renders; Image Optimization | Rendering Cost & Re-renders; Long Tasks & Main-Thread Work; Offloading to Workers | 3 | Planned |
| Offloading to Workers | `offloading-to-workers.md` | Performance Engineering | Runtime Performance | Critical | Intermediate | 12 min | Rendering Cost & Re-renders; Image Optimization | Rendering Cost & Re-renders; Long Tasks & Main-Thread Work; Debounce, Throttle & Scheduling | 3 | Planned |
| Memory Profiling in Practice | `memory-profiling-in-practice.md` | Performance Engineering | Memory Performance | Critical | Intermediate | 15 min | Rendering Cost & Re-renders | Long-Session Memory Growth | 3 | Planned |
| Long-Session Memory Growth | `long-session-memory-growth.md` | Performance Engineering | Memory Performance | Critical | Intermediate | 12 min | Memory Profiling in Practice; Rendering Cost & Re-renders | Memory Profiling in Practice | 3 | Planned |
| Performance Budgets | `performance-budgets.md` | Performance Engineering | Performance Culture | Critical | Intermediate | 12 min | Memory Profiling in Practice | Regression Prevention & CI Gates; Caching for Performance (cross-layer) | 3 | Planned |
| Regression Prevention & CI Gates | `regression-prevention-and-ci-gates.md` | Performance Engineering | Performance Culture | Critical | Intermediate | 15 min | Performance Budgets; Memory Profiling in Practice | Performance Budgets; Caching for Performance (cross-layer) | 3 | Planned |
| Caching for Performance (cross-layer) | `caching-for-performance-cross-layer.md` | Performance Engineering | Performance Culture | Critical | Intermediate | 15 min | Performance Budgets; Memory Profiling in Practice | Performance Budgets; Regression Prevention & CI Gates | 3 | Planned |

### Security  (24 articles · ~387 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Same-Origin Policy | `same-origin-policy.md` | Security | The Security Model | Critical | Advanced | 16 min | HTTP/1.1 Semantics · Networking & Protocols; Web Storage · Browser APIs | CORS; Isolation (COOP/COEP) | 4 | Published |
| CORS | `cors.md` | Security | The Security Model | Critical | Advanced | 16 min | Same-Origin Policy | Same-Origin Policy; Isolation (COOP/COEP) | 4 | Planned |
| Isolation (COOP/COEP) | `isolation-coop-coep.md` | Security | The Security Model | Critical | Advanced | 16 min | Same-Origin Policy | Same-Origin Policy; CORS | 4 | Planned |
| Cross-Site Scripting (XSS) | `cross-site-scripting-xss.md` | Security | Injection Attacks | Critical | Advanced | 16 min | Same-Origin Policy | DOM-Based XSS; HTML/Template Injection; Sanitization & Encoding | 4 | Planned |
| DOM-Based XSS | `dom-based-xss.md` | Security | Injection Attacks | Critical | Advanced | 16 min | Cross-Site Scripting (XSS); Same-Origin Policy | Cross-Site Scripting (XSS); HTML/Template Injection; Sanitization & Encoding | 4 | Planned |
| HTML/Template Injection | `html-template-injection.md` | Security | Injection Attacks | Critical | Advanced | 16 min | Cross-Site Scripting (XSS); Same-Origin Policy | Cross-Site Scripting (XSS); DOM-Based XSS; Sanitization & Encoding | 4 | Planned |
| Sanitization & Encoding | `sanitization-and-encoding.md` | Security | Injection Attacks | Critical | Advanced | 16 min | Cross-Site Scripting (XSS); Same-Origin Policy | Cross-Site Scripting (XSS); DOM-Based XSS; HTML/Template Injection | 4 | Planned |
| Cross-Site Request Forgery | `cross-site-request-forgery.md` | Security | Request Attacks | Critical | Advanced | 16 min | Cross-Site Scripting (XSS) | Clickjacking; Client-Edge SSRF | 4 | Planned |
| Clickjacking | `clickjacking.md` | Security | Request Attacks | Critical | Advanced | 16 min | Cross-Site Request Forgery; Cross-Site Scripting (XSS) | Cross-Site Request Forgery; Client-Edge SSRF | 4 | Planned |
| Client-Edge SSRF | `client-edge-ssrf.md` | Security | Request Attacks | Critical | Advanced | 16 min | Cross-Site Request Forgery; Cross-Site Scripting (XSS) | Cross-Site Request Forgery; Clickjacking | 4 | Planned |
| Content Security Policy | `content-security-policy.md` | Security | Content Security | Critical | Advanced | 16 min | Cross-Site Request Forgery | Trusted Types; Subresource Integrity | 4 | Planned |
| Trusted Types | `trusted-types.md` | Security | Content Security | Critical | Advanced | 16 min | Content Security Policy; Cross-Site Request Forgery | Content Security Policy; Subresource Integrity | 4 | Planned |
| Subresource Integrity | `subresource-integrity.md` | Security | Content Security | Critical | Advanced | 16 min | Content Security Policy; Cross-Site Request Forgery | Content Security Policy; Trusted Types | 4 | Planned |
| Session Management | `session-management.md` | Security | Authentication & Sessions | Critical | Advanced | 16 min | Content Security Policy | Token Types (JWT, opaque); Token Storage Trade-offs; OAuth & OIDC Flows; Client Auth (guards, refresh) | 4 | Planned |
| Token Types (JWT, opaque) | `token-types-jwt-opaque.md` | Security | Authentication & Sessions | Critical | Advanced | 16 min | Session Management; Content Security Policy | Session Management; Token Storage Trade-offs; OAuth & OIDC Flows; Client Auth (guards, refresh) | 4 | Planned |
| Token Storage Trade-offs | `token-storage-trade-offs.md` | Security | Authentication & Sessions | Critical | Advanced | 16 min | Session Management; Content Security Policy | Session Management; Token Types (JWT, opaque); OAuth & OIDC Flows; Client Auth (guards, refresh) | 4 | Planned |
| OAuth & OIDC Flows | `oauth-and-oidc-flows.md` | Security | Authentication & Sessions | Critical | Advanced | 16 min | Session Management; Content Security Policy | Session Management; Token Types (JWT, opaque); Token Storage Trade-offs; Client Auth (guards, refresh) | 4 | Planned |
| Client Auth (guards, refresh) | `client-auth-guards-refresh.md` | Security | Authentication & Sessions | Critical | Advanced | 19 min | Session Management; Content Security Policy | Session Management; Token Types (JWT, opaque); Token Storage Trade-offs; OAuth & OIDC Flows | 4 | Planned |
| Dependency Vulnerabilities | `dependency-vulnerabilities.md` | Security | Supply Chain | Critical | Advanced | 16 min | Session Management | Lockfiles & Provenance; Third-Party Script Risk | 4 | Planned |
| Lockfiles & Provenance | `lockfiles-and-provenance.md` | Security | Supply Chain | Critical | Advanced | 16 min | Dependency Vulnerabilities; Session Management | Dependency Vulnerabilities; Third-Party Script Risk | 4 | Planned |
| Third-Party Script Risk | `third-party-script-risk.md` | Security | Supply Chain | Critical | Advanced | 16 min | Dependency Vulnerabilities; Session Management | Dependency Vulnerabilities; Lockfiles & Provenance | 4 | Planned |
| Data Handling & PII | `data-handling-and-pii.md` | Security | Privacy | Critical | Advanced | 16 min | Dependency Vulnerabilities | Consent & Tracking; Regulatory Compliance | 4 | Planned |
| Consent & Tracking | `consent-and-tracking.md` | Security | Privacy | Critical | Advanced | 16 min | Data Handling & PII; Dependency Vulnerabilities | Data Handling & PII; Regulatory Compliance | 4 | Planned |
| Regulatory Compliance | `regulatory-compliance.md` | Security | Privacy | Critical | Advanced | 16 min | Data Handling & PII; Dependency Vulnerabilities | Data Handling & PII; Consent & Tracking | 4 | Planned |

### Testing & Quality  (18 articles · ~231 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| The Testing Pyramid/Trophy | `the-testing-pyramid-trophy.md` | Testing & Quality | Strategy | Critical | Intermediate | 12 min | Elements vs Components · React; Primitives & Wrappers · JavaScript | What to Test & Coverage Goals; Test Doubles (mocks, stubs, fakes) | 3 | Published |
| What to Test & Coverage Goals | `what-to-test-and-coverage-goals.md` | Testing & Quality | Strategy | Critical | Intermediate | 15 min | The Testing Pyramid/Trophy | The Testing Pyramid/Trophy; Test Doubles (mocks, stubs, fakes) | 3 | Published |
| Test Doubles (mocks, stubs, fakes) | `test-doubles-mocks-stubs-fakes.md` | Testing & Quality | Strategy | Critical | Intermediate | 15 min | The Testing Pyramid/Trophy | The Testing Pyramid/Trophy; What to Test & Coverage Goals | 3 | Planned |
| Pure Logic Testing | `pure-logic-testing.md` | Testing & Quality | Unit Testing | Critical | Intermediate | 12 min | The Testing Pyramid/Trophy | Testing Hooks & Utilities; Property-Based Testing | 3 | Published |
| Testing Hooks & Utilities | `testing-hooks-and-utilities.md` | Testing & Quality | Unit Testing | Critical | Intermediate | 12 min | Pure Logic Testing; The Testing Pyramid/Trophy | Pure Logic Testing; Property-Based Testing | 3 | Planned |
| Property-Based Testing | `property-based-testing.md` | Testing & Quality | Unit Testing | Critical | Intermediate | 12 min | Pure Logic Testing; The Testing Pyramid/Trophy | Pure Logic Testing; Testing Hooks & Utilities | 3 | Planned |
| Rendering & Querying | `rendering-and-querying.md` | Testing & Quality | Component Testing | Critical | Intermediate | 12 min | Pure Logic Testing | User-Event Simulation; Accessibility-Tree Assertions | 3 | Planned |
| User-Event Simulation | `user-event-simulation.md` | Testing & Quality | Component Testing | Critical | Intermediate | 12 min | Rendering & Querying; Pure Logic Testing | Rendering & Querying; Accessibility-Tree Assertions | 3 | Planned |
| Accessibility-Tree Assertions | `accessibility-tree-assertions.md` | Testing & Quality | Component Testing | Critical | Intermediate | 15 min | Rendering & Querying; Pure Logic Testing | Rendering & Querying; User-Event Simulation | 3 | Planned |
| Testing with Real Providers | `testing-with-real-providers.md` | Testing & Quality | Integration Testing | Critical | Intermediate | 15 min | Rendering & Querying | Network Mocking; Testing State & Data Flows | 3 | Planned |
| Network Mocking | `network-mocking.md` | Testing & Quality | Integration Testing | Critical | Intermediate | 12 min | Testing with Real Providers; Rendering & Querying | Testing with Real Providers; Testing State & Data Flows | 3 | Planned |
| Testing State & Data Flows | `testing-state-and-data-flows.md` | Testing & Quality | Integration Testing | Critical | Intermediate | 12 min | Testing with Real Providers; Rendering & Querying | Testing with Real Providers; Network Mocking | 3 | Planned |
| E2E User Flows | `e2e-user-flows.md` | Testing & Quality | End-to-End | Critical | Intermediate | 12 min | Testing with Real Providers | Cross-Browser Testing; Visual Regression Testing | 3 | Planned |
| Cross-Browser Testing | `cross-browser-testing.md` | Testing & Quality | End-to-End | Critical | Intermediate | 12 min | E2E User Flows; Testing with Real Providers | E2E User Flows; Visual Regression Testing | 3 | Planned |
| Visual Regression Testing | `visual-regression-testing.md` | Testing & Quality | End-to-End | Critical | Intermediate | 12 min | E2E User Flows; Testing with Real Providers | E2E User Flows; Cross-Browser Testing | 3 | Planned |
| Flakiness & Determinism | `flakiness-and-determinism.md` | Testing & Quality | Test Health | Critical | Intermediate | 12 min | E2E User Flows | Test Performance & Parallelism; Test Maintenance | 3 | Planned |
| Test Performance & Parallelism | `test-performance-and-parallelism.md` | Testing & Quality | Test Health | Critical | Intermediate | 15 min | Flakiness & Determinism; E2E User Flows | Flakiness & Determinism; Test Maintenance | 3 | Planned |
| Test Maintenance | `test-maintenance.md` | Testing & Quality | Test Health | Critical | Intermediate | 12 min | Flakiness & Determinism; E2E User Flows | Flakiness & Determinism; Test Performance & Parallelism | 3 | Planned |

---

## 06 · Engineering Systems  ·  Priority: High  ·  69 articles

### Build Systems & Tooling  (16 articles · ~216 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| The Dependency Graph | `the-dependency-graph.md` | Build Systems & Tooling | Module Bundling | High | Intermediate | 12 min | Primitives & Wrappers · JavaScript; Dependency Resolution · Package Architecture | Bundler Models; Entry Points & Output | 3 | Planned |
| Bundler Models | `bundler-models.md` | Build Systems & Tooling | Module Bundling | High | Intermediate | 12 min | The Dependency Graph | The Dependency Graph; Entry Points & Output | 3 | Planned |
| Entry Points & Output | `entry-points-and-output.md` | Build Systems & Tooling | Module Bundling | High | Intermediate | 12 min | The Dependency Graph | The Dependency Graph; Bundler Models | 3 | Planned |
| Transpilation & Targets | `transpilation-and-targets.md` | Build Systems & Tooling | Compilation | High | Advanced | 16 min | The Dependency Graph | Source-to-Source Compilers; AST Transforms & Plugins | 4 | Planned |
| Source-to-Source Compilers | `source-to-source-compilers.md` | Build Systems & Tooling | Compilation | High | Advanced | 16 min | Transpilation & Targets; The Dependency Graph | Transpilation & Targets; AST Transforms & Plugins | 4 | Planned |
| AST Transforms & Plugins | `ast-transforms-and-plugins.md` | Build Systems & Tooling | Compilation | High | Advanced | 16 min | Transpilation & Targets; The Dependency Graph | Transpilation & Targets; Source-to-Source Compilers | 4 | Planned |
| Tree Shaking | `tree-shaking.md` | Build Systems & Tooling | Optimization | High | Intermediate | 12 min | Transpilation & Targets | Dead Code Elimination; Chunking & Split Points; Scope Hoisting | 3 | Planned |
| Dead Code Elimination | `dead-code-elimination.md` | Build Systems & Tooling | Optimization | High | Intermediate | 12 min | Tree Shaking; Transpilation & Targets | Tree Shaking; Chunking & Split Points; Scope Hoisting | 3 | Planned |
| Chunking & Split Points | `chunking-and-split-points.md` | Build Systems & Tooling | Optimization | High | Intermediate | 12 min | Tree Shaking; Transpilation & Targets | Tree Shaking; Dead Code Elimination; Scope Hoisting | 3 | Planned |
| Scope Hoisting | `scope-hoisting.md` | Build Systems & Tooling | Optimization | High | Intermediate | 12 min | Tree Shaking; Transpilation & Targets | Tree Shaking; Dead Code Elimination; Chunking & Split Points | 3 | Planned |
| Source Maps | `source-maps.md` | Build Systems & Tooling | Developer Aids | High | Intermediate | 12 min | Tree Shaking | Hot Module Replacement; Dev Server Architecture | 3 | Planned |
| Hot Module Replacement | `hot-module-replacement.md` | Build Systems & Tooling | Developer Aids | High | Intermediate | 12 min | Source Maps; Tree Shaking | Source Maps; Dev Server Architecture | 3 | Planned |
| Dev Server Architecture | `dev-server-architecture.md` | Build Systems & Tooling | Developer Aids | High | Intermediate | 12 min | Source Maps; Tree Shaking | Source Maps; Hot Module Replacement | 3 | Planned |
| Incremental Builds | `incremental-builds.md` | Build Systems & Tooling | Build Cache | High | Advanced | 16 min | Source Maps | Persistent & Remote Cache; Cache Invalidation Keys | 4 | Planned |
| Persistent & Remote Cache | `persistent-and-remote-cache.md` | Build Systems & Tooling | Build Cache | High | Advanced | 16 min | Incremental Builds; Source Maps | Incremental Builds; Cache Invalidation Keys | 4 | Planned |
| Cache Invalidation Keys | `cache-invalidation-keys.md` | Build Systems & Tooling | Build Cache | High | Advanced | 16 min | Incremental Builds; Source Maps | Incremental Builds; Persistent & Remote Cache | 4 | Planned |

### Delivery & Infrastructure  (17 articles · ~278 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Static Hosting | `static-hosting.md` | Delivery & Infrastructure | Hosting Models | High | Advanced | 16 min | The Dependency Graph · Build Systems & Tooling; HTTP/1.1 Semantics · Networking & Protocols | Server & SSR Hosting; Serverless Functions; Edge Runtimes | 4 | Planned |
| Server & SSR Hosting | `server-and-ssr-hosting.md` | Delivery & Infrastructure | Hosting Models | High | Advanced | 16 min | Static Hosting | Static Hosting; Serverless Functions; Edge Runtimes | 4 | Planned |
| Serverless Functions | `serverless-functions.md` | Delivery & Infrastructure | Hosting Models | High | Advanced | 16 min | Static Hosting | Static Hosting; Server & SSR Hosting; Edge Runtimes | 4 | Planned |
| Edge Runtimes | `edge-runtimes.md` | Delivery & Infrastructure | Hosting Models | High | Advanced | 16 min | Static Hosting | Static Hosting; Server & SSR Hosting; Serverless Functions | 4 | Planned |
| CDN Architecture | `cdn-architecture.md` | Delivery & Infrastructure | Content Delivery | High | Advanced | 16 min | Static Hosting | Edge Compute & Routing; Immutable Asset URLs | 4 | Planned |
| Edge Compute & Routing | `edge-compute-and-routing.md` | Delivery & Infrastructure | Content Delivery | High | Advanced | 16 min | CDN Architecture; Static Hosting | CDN Architecture; Immutable Asset URLs | 4 | Planned |
| Immutable Asset URLs | `immutable-asset-urls.md` | Delivery & Infrastructure | Content Delivery | High | Advanced | 16 min | CDN Architecture; Static Hosting | CDN Architecture; Edge Compute & Routing | 4 | Planned |
| Environment Configuration | `environment-configuration.md` | Delivery & Infrastructure | Configuration | High | Advanced | 16 min | CDN Architecture | Secrets Management; Feature Configuration | 4 | Planned |
| Secrets Management | `secrets-management.md` | Delivery & Infrastructure | Configuration | High | Advanced | 16 min | Environment Configuration; CDN Architecture | Environment Configuration; Feature Configuration | 4 | Planned |
| Feature Configuration | `feature-configuration.md` | Delivery & Infrastructure | Configuration | High | Advanced | 16 min | Environment Configuration; CDN Architecture | Environment Configuration; Secrets Management | 4 | Planned |
| Deployment Strategies (canary, blue-green) | `deployment-strategies-canary-blue-green.md` | Delivery & Infrastructure | Release Management | High | Advanced | 19 min | Environment Configuration | Rollbacks & Kill Switches; Feature Flags; Progressive Delivery & Experiments | 4 | Planned |
| Rollbacks & Kill Switches | `rollbacks-and-kill-switches.md` | Delivery & Infrastructure | Release Management | High | Advanced | 16 min | Deployment Strategies (canary, blue-green); Environment Configuration | Deployment Strategies (canary, blue-green); Feature Flags; Progressive Delivery & Experiments | 4 | Planned |
| Feature Flags | `feature-flags.md` | Delivery & Infrastructure | Release Management | High | Advanced | 16 min | Deployment Strategies (canary, blue-green); Environment Configuration | Deployment Strategies (canary, blue-green); Rollbacks & Kill Switches; Progressive Delivery & Experiments | 4 | Planned |
| Progressive Delivery & Experiments | `progressive-delivery-and-experiments.md` | Delivery & Infrastructure | Release Management | High | Advanced | 19 min | Deployment Strategies (canary, blue-green); Environment Configuration | Deployment Strategies (canary, blue-green); Rollbacks & Kill Switches; Feature Flags | 4 | Planned |
| Scaling & Capacity | `scaling-and-capacity.md` | Delivery & Infrastructure | Operations | High | Advanced | 16 min | Deployment Strategies (canary, blue-green) | Cost Optimization; Uptime & Health Checks | 4 | Planned |
| Cost Optimization | `cost-optimization.md` | Delivery & Infrastructure | Operations | High | Advanced | 16 min | Scaling & Capacity; Deployment Strategies (canary, blue-green) | Scaling & Capacity; Uptime & Health Checks | 4 | Planned |
| Uptime & Health Checks | `uptime-and-health-checks.md` | Delivery & Infrastructure | Operations | High | Advanced | 16 min | Scaling & Capacity; Deployment Strategies (canary, blue-green) | Scaling & Capacity; Cost Optimization | 4 | Planned |

### Developer Experience & Workflow  (23 articles · ~285 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Monorepo Architecture | `monorepo-architecture.md` | Developer Experience & Workflow | Monorepo | High | Intermediate | 12 min | The Dependency Graph · Build Systems & Tooling; The Testing Pyramid/Trophy · Testing & Quality | Task Orchestration & Pipelines; Workspace Dependency Graphs; Remote Caching & Affected Builds | 3 | Planned |
| Task Orchestration & Pipelines | `task-orchestration-and-pipelines.md` | Developer Experience & Workflow | Monorepo | High | Intermediate | 15 min | Monorepo Architecture | Monorepo Architecture; Workspace Dependency Graphs; Remote Caching & Affected Builds | 3 | Planned |
| Workspace Dependency Graphs | `workspace-dependency-graphs.md` | Developer Experience & Workflow | Monorepo | High | Intermediate | 15 min | Monorepo Architecture | Monorepo Architecture; Task Orchestration & Pipelines; Remote Caching & Affected Builds | 3 | Planned |
| Remote Caching & Affected Builds | `remote-caching-and-affected-builds.md` | Developer Experience & Workflow | Monorepo | High | Intermediate | 15 min | Monorepo Architecture | Monorepo Architecture; Task Orchestration & Pipelines; Workspace Dependency Graphs | 3 | Planned |
| Linting | `linting.md` | Developer Experience & Workflow | Code Quality | High | Intermediate | 12 min | Monorepo Architecture | Formatting; Type Checking in CI | 3 | Planned |
| Formatting | `formatting.md` | Developer Experience & Workflow | Code Quality | High | Intermediate | 12 min | Linting; Monorepo Architecture | Linting; Type Checking in CI | 3 | Planned |
| Type Checking in CI | `type-checking-in-ci.md` | Developer Experience & Workflow | Code Quality | High | Intermediate | 12 min | Linting; Monorepo Architecture | Linting; Formatting | 3 | Planned |
| Fast Feedback Loops | `fast-feedback-loops.md` | Developer Experience & Workflow | Local Development | High | Intermediate | 12 min | Linting | Environment Consistency; Local Service Mocking | 3 | Planned |
| Environment Consistency | `environment-consistency.md` | Developer Experience & Workflow | Local Development | High | Intermediate | 12 min | Fast Feedback Loops; Linting | Fast Feedback Loops; Local Service Mocking | 3 | Planned |
| Local Service Mocking | `local-service-mocking.md` | Developer Experience & Workflow | Local Development | High | Intermediate | 12 min | Fast Feedback Loops; Linting | Fast Feedback Loops; Environment Consistency | 3 | Planned |
| Browser DevTools | `browser-devtools.md` | Developer Experience & Workflow | Debugging | High | Intermediate | 12 min | Fast Feedback Loops | Debugging Techniques; Framework DevTools | 3 | Planned |
| Debugging Techniques | `debugging-techniques.md` | Developer Experience & Workflow | Debugging | High | Intermediate | 12 min | Browser DevTools; Fast Feedback Loops | Browser DevTools; Framework DevTools | 3 | Planned |
| Framework DevTools | `framework-devtools.md` | Developer Experience & Workflow | Debugging | High | Intermediate | 12 min | Browser DevTools; Fast Feedback Loops | Browser DevTools; Debugging Techniques | 3 | Planned |
| Branching Models | `branching-models.md` | Developer Experience & Workflow | Version Control | High | Intermediate | 12 min | Browser DevTools | Commit Conventions; PR & Review Tooling | 3 | Planned |
| Commit Conventions | `commit-conventions.md` | Developer Experience & Workflow | Version Control | High | Intermediate | 12 min | Branching Models; Browser DevTools | Branching Models; PR & Review Tooling | 3 | Planned |
| PR & Review Tooling | `pr-and-review-tooling.md` | Developer Experience & Workflow | Version Control | High | Intermediate | 12 min | Branching Models; Browser DevTools | Branching Models; Commit Conventions | 3 | Planned |
| CI Pipeline Design | `ci-pipeline-design.md` | Developer Experience & Workflow | Continuous Delivery | High | Intermediate | 12 min | Branching Models | Build & Test Automation; Deployment Automation; Pipeline Caching & Speed | 3 | Planned |
| Build & Test Automation | `build-and-test-automation.md` | Developer Experience & Workflow | Continuous Delivery | High | Intermediate | 12 min | CI Pipeline Design; Branching Models | CI Pipeline Design; Deployment Automation; Pipeline Caching & Speed | 3 | Planned |
| Deployment Automation | `deployment-automation.md` | Developer Experience & Workflow | Continuous Delivery | High | Intermediate | 12 min | CI Pipeline Design; Branching Models | CI Pipeline Design; Build & Test Automation; Pipeline Caching & Speed | 3 | Planned |
| Pipeline Caching & Speed | `pipeline-caching-and-speed.md` | Developer Experience & Workflow | Continuous Delivery | High | Intermediate | 12 min | CI Pipeline Design; Branching Models | CI Pipeline Design; Build & Test Automation; Deployment Automation | 3 | Planned |
| Codemods & Migrations | `codemods-and-migrations.md` | Developer Experience & Workflow | Automation | High | Intermediate | 12 min | CI Pipeline Design | Scaffolding & Generators; Git Hooks & Pre-commit | 3 | Planned |
| Scaffolding & Generators | `scaffolding-and-generators.md` | Developer Experience & Workflow | Automation | High | Intermediate | 12 min | Codemods & Migrations; CI Pipeline Design | Codemods & Migrations; Git Hooks & Pre-commit | 3 | Planned |
| Git Hooks & Pre-commit | `git-hooks-and-pre-commit.md` | Developer Experience & Workflow | Automation | High | Intermediate | 12 min | Codemods & Migrations; CI Pipeline Design | Codemods & Migrations; Scaffolding & Generators | 3 | Planned |

### Package Architecture  (13 articles · ~220 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Dependency Resolution | `dependency-resolution.md` | Package Architecture | Package Management | High | Advanced | 16 min | Primitives & Wrappers · JavaScript | Lockfiles & Determinism; Node Modules & Hoisting Models | 4 | Planned |
| Lockfiles & Determinism | `lockfiles-and-determinism.md` | Package Architecture | Package Management | High | Advanced | 16 min | Dependency Resolution | Dependency Resolution; Node Modules & Hoisting Models | 4 | Planned |
| Node Modules & Hoisting Models | `node-modules-and-hoisting-models.md` | Package Architecture | Package Management | High | Advanced | 19 min | Dependency Resolution | Dependency Resolution; Lockfiles & Determinism | 4 | Planned |
| Exports Map & Entry Points | `exports-map-and-entry-points.md` | Package Architecture | Package Design | High | Advanced | 16 min | Dependency Resolution | Module Formats (ESM/CJS/UMD); Conditional & Dual Exports; Types Distribution | 4 | Planned |
| Module Formats (ESM/CJS/UMD) | `module-formats-esm-cjs-umd.md` | Package Architecture | Package Design | High | Advanced | 19 min | Exports Map & Entry Points; Dependency Resolution | Exports Map & Entry Points; Conditional & Dual Exports; Types Distribution | 4 | Planned |
| Conditional & Dual Exports | `conditional-and-dual-exports.md` | Package Architecture | Package Design | High | Advanced | 16 min | Exports Map & Entry Points; Dependency Resolution | Exports Map & Entry Points; Module Formats (ESM/CJS/UMD); Types Distribution | 4 | Planned |
| Types Distribution | `types-distribution.md` | Package Architecture | Package Design | High | Advanced | 16 min | Exports Map & Entry Points; Dependency Resolution | Exports Map & Entry Points; Module Formats (ESM/CJS/UMD); Conditional & Dual Exports | 4 | Planned |
| Semantic Versioning | `semantic-versioning.md` | Package Architecture | Publishing | High | Advanced | 16 min | Exports Map & Entry Points | Release Automation & Changelogs; Provenance & Signing | 4 | Planned |
| Release Automation & Changelogs | `release-automation-and-changelogs.md` | Package Architecture | Publishing | High | Advanced | 19 min | Semantic Versioning; Exports Map & Entry Points | Semantic Versioning; Provenance & Signing | 4 | Planned |
| Provenance & Signing | `provenance-and-signing.md` | Package Architecture | Publishing | High | Advanced | 16 min | Semantic Versioning; Exports Map & Entry Points | Semantic Versioning; Release Automation & Changelogs | 4 | Planned |
| Peer Dependencies | `peer-dependencies.md` | Package Architecture | Dependency Strategy | High | Advanced | 16 min | Semantic Versioning | Bundling vs Externalizing; Dependency Hygiene & Updates | 4 | Planned |
| Bundling vs Externalizing | `bundling-vs-externalizing.md` | Package Architecture | Dependency Strategy | High | Advanced | 16 min | Peer Dependencies; Semantic Versioning | Peer Dependencies; Dependency Hygiene & Updates | 4 | Planned |
| Dependency Hygiene & Updates | `dependency-hygiene-and-updates.md` | Package Architecture | Dependency Strategy | High | Advanced | 19 min | Peer Dependencies; Semantic Versioning | Peer Dependencies; Bundling vs Externalizing | 4 | Planned |

---

## 07 · Platform Reach  ·  Priority: Medium  ·  45 articles

### Graphics & Immersive  (14 articles · ~283 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| The 2D Canvas Model | `the-2d-canvas-model.md` | Graphics & Immersive | Canvas | Medium | Staff | 20 min | Process & Thread Architecture · The Web Platform; Parsing & Bytecode · Runtime & Execution | OffscreenCanvas; Text & Path Rendering | 1 | Planned |
| OffscreenCanvas | `offscreencanvas.md` | Graphics & Immersive | Canvas | Medium | Staff | 20 min | The 2D Canvas Model | The 2D Canvas Model; Text & Path Rendering | 1 | Planned |
| Text & Path Rendering | `text-and-path-rendering.md` | Graphics & Immersive | Canvas | Medium | Staff | 20 min | The 2D Canvas Model | The 2D Canvas Model; OffscreenCanvas | 1 | Planned |
| SVG Rendering & Scripting | `svg-rendering-and-scripting.md` | Graphics & Immersive | Vector | Medium | Staff | 20 min | The 2D Canvas Model | SVG Performance | 1 | Planned |
| SVG Performance | `svg-performance.md` | Graphics & Immersive | Vector | Medium | Staff | 20 min | SVG Rendering & Scripting; The 2D Canvas Model | SVG Rendering & Scripting | 1 | Planned |
| WebGL Fundamentals | `webgl-fundamentals.md` | Graphics & Immersive | GPU | Medium | Staff | 20 min | SVG Rendering & Scripting | WebGPU; Shaders & Pipelines | 1 | Planned |
| WebGPU | `webgpu.md` | Graphics & Immersive | GPU | Medium | Staff | 20 min | WebGL Fundamentals; SVG Rendering & Scripting | WebGL Fundamentals; Shaders & Pipelines | 1 | Planned |
| Shaders & Pipelines | `shaders-and-pipelines.md` | Graphics & Immersive | GPU | Medium | Staff | 20 min | WebGL Fundamentals; SVG Rendering & Scripting | WebGL Fundamentals; WebGPU | 1 | Planned |
| Data-Viz Rendering Models | `data-viz-rendering-models.md` | Graphics & Immersive | Visualization | Medium | Staff | 20 min | WebGL Fundamentals | Coordinate Systems & Scales; Large-Dataset Rendering | 1 | Planned |
| Coordinate Systems & Scales | `coordinate-systems-and-scales.md` | Graphics & Immersive | Visualization | Medium | Staff | 23 min | Data-Viz Rendering Models; WebGL Fundamentals | Data-Viz Rendering Models; Large-Dataset Rendering | 1 | Planned |
| Large-Dataset Rendering | `large-dataset-rendering.md` | Graphics & Immersive | Visualization | Medium | Staff | 20 min | Data-Viz Rendering Models; WebGL Fundamentals | Data-Viz Rendering Models; Coordinate Systems & Scales | 1 | Planned |
| WebXR | `webxr.md` | Graphics & Immersive | Immersive | Medium | Staff | 20 min | Data-Viz Rendering Models | Spatial Interaction; 3D Scene Models | 1 | Planned |
| Spatial Interaction | `spatial-interaction.md` | Graphics & Immersive | Immersive | Medium | Staff | 20 min | WebXR; Data-Viz Rendering Models | WebXR; 3D Scene Models | 1 | Planned |
| 3D Scene Models | `3d-scene-models.md` | Graphics & Immersive | Immersive | Medium | Staff | 20 min | WebXR; Data-Viz Rendering Models | WebXR; Spatial Interaction | 1 | Planned |

### Internationalization & Localization  (16 articles · ~265 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Locale Modeling & Negotiation | `locale-modeling-and-negotiation.md` | Internationalization & Localization | Locale | Medium | Advanced | 19 min | Specificity · CSS & Visual Systems; Primitives & Wrappers · JavaScript | Language Detection | 4 | Planned |
| Language Detection | `language-detection.md` | Internationalization & Localization | Locale | Medium | Advanced | 16 min | Locale Modeling & Negotiation | Locale Modeling & Negotiation | 4 | Planned |
| Number, Date & Currency Formatting | `number-date-and-currency-formatting.md` | Internationalization & Localization | Formatting | Medium | Advanced | 19 min | Locale Modeling & Negotiation | The Intl API; Relative & Duration Formatting | 4 | Planned |
| The Intl API | `the-intl-api.md` | Internationalization & Localization | Formatting | Medium | Advanced | 16 min | Number, Date & Currency Formatting; Locale Modeling & Negotiation | Number, Date & Currency Formatting; Relative & Duration Formatting | 4 | Planned |
| Relative & Duration Formatting | `relative-and-duration-formatting.md` | Internationalization & Localization | Formatting | Medium | Advanced | 19 min | Number, Date & Currency Formatting; Locale Modeling & Negotiation | Number, Date & Currency Formatting; The Intl API | 4 | Planned |
| Message Catalogs | `message-catalogs.md` | Internationalization & Localization | Translation | Medium | Advanced | 16 min | Number, Date & Currency Formatting | Translation Workflow & TMS; Interpolation & Rich Text | 4 | Planned |
| Translation Workflow & TMS | `translation-workflow-and-tms.md` | Internationalization & Localization | Translation | Medium | Advanced | 16 min | Message Catalogs; Number, Date & Currency Formatting | Message Catalogs; Interpolation & Rich Text | 4 | Planned |
| Interpolation & Rich Text | `interpolation-and-rich-text.md` | Internationalization & Localization | Translation | Medium | Advanced | 16 min | Message Catalogs; Number, Date & Currency Formatting | Message Catalogs; Translation Workflow & TMS | 4 | Planned |
| Pluralization | `pluralization.md` | Internationalization & Localization | Grammar | Medium | Advanced | 16 min | Message Catalogs | Gender & Select; Collation & Sorting | 4 | Planned |
| Gender & Select | `gender-and-select.md` | Internationalization & Localization | Grammar | Medium | Advanced | 16 min | Pluralization; Message Catalogs | Pluralization; Collation & Sorting | 4 | Planned |
| Collation & Sorting | `collation-and-sorting.md` | Internationalization & Localization | Grammar | Medium | Advanced | 16 min | Pluralization; Message Catalogs | Pluralization; Gender & Select | 4 | Planned |
| Bidirectional Text (RTL) | `bidirectional-text-rtl.md` | Internationalization & Localization | Layout | Medium | Advanced | 16 min | Pluralization | Logical Properties; Complex Scripts & Shaping | 4 | Planned |
| Logical Properties | `logical-properties.md` | Internationalization & Localization | Layout | Medium | Advanced | 16 min | Bidirectional Text (RTL); Pluralization | Bidirectional Text (RTL); Complex Scripts & Shaping | 4 | Planned |
| Complex Scripts & Shaping | `complex-scripts-and-shaping.md` | Internationalization & Localization | Layout | Medium | Advanced | 16 min | Bidirectional Text (RTL); Pluralization | Bidirectional Text (RTL); Logical Properties | 4 | Planned |
| Locale-Aware Routing | `locale-aware-routing.md` | Internationalization & Localization | Content | Medium | Advanced | 16 min | Bidirectional Text (RTL) | Cultural Adaptation | 4 | Planned |
| Cultural Adaptation | `cultural-adaptation.md` | Internationalization & Localization | Content | Medium | Advanced | 16 min | Locale-Aware Routing; Bidirectional Text (RTL) | Locale-Aware Routing | 4 | Planned |

### Progressive & Cross-Platform Web  (15 articles · ~246 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| The Service Worker Lifecycle | `the-service-worker-lifecycle.md` | Progressive & Cross-Platform Web | Service Workers | Medium | Advanced | 19 min | Web Storage · Browser APIs; HTTP/1.1 Semantics · Networking & Protocols; Core Web Vitals (LCP, INP, CLS) · Performance Engineering | Fetch Interception; Update & Activation Strategy | 4 | Planned |
| Fetch Interception | `fetch-interception.md` | Progressive & Cross-Platform Web | Service Workers | Medium | Advanced | 16 min | The Service Worker Lifecycle | The Service Worker Lifecycle; Update & Activation Strategy | 4 | Planned |
| Update & Activation Strategy | `update-and-activation-strategy.md` | Progressive & Cross-Platform Web | Service Workers | Medium | Advanced | 19 min | The Service Worker Lifecycle | The Service Worker Lifecycle; Fetch Interception | 4 | Planned |
| Runtime Caching Strategies | `runtime-caching-strategies.md` | Progressive & Cross-Platform Web | Offline | Medium | Advanced | 16 min | The Service Worker Lifecycle | Precaching & Offline Shell; Background Sync; Cache Versioning & Cleanup | 4 | Planned |
| Precaching & Offline Shell | `precaching-and-offline-shell.md` | Progressive & Cross-Platform Web | Offline | Medium | Advanced | 16 min | Runtime Caching Strategies; The Service Worker Lifecycle | Runtime Caching Strategies; Background Sync; Cache Versioning & Cleanup | 4 | Planned |
| Background Sync | `background-sync.md` | Progressive & Cross-Platform Web | Offline | Medium | Advanced | 16 min | Runtime Caching Strategies; The Service Worker Lifecycle | Runtime Caching Strategies; Precaching & Offline Shell; Cache Versioning & Cleanup | 4 | Planned |
| Cache Versioning & Cleanup | `cache-versioning-and-cleanup.md` | Progressive & Cross-Platform Web | Offline | Medium | Advanced | 16 min | Runtime Caching Strategies; The Service Worker Lifecycle | Runtime Caching Strategies; Precaching & Offline Shell; Background Sync | 4 | Planned |
| Web App Manifest | `web-app-manifest.md` | Progressive & Cross-Platform Web | Installability | Medium | Advanced | 16 min | Runtime Caching Strategies | Install Prompts & Criteria; Standalone & Display Modes | 4 | Planned |
| Install Prompts & Criteria | `install-prompts-and-criteria.md` | Progressive & Cross-Platform Web | Installability | Medium | Advanced | 16 min | Web App Manifest; Runtime Caching Strategies | Web App Manifest; Standalone & Display Modes | 4 | Planned |
| Standalone & Display Modes | `standalone-and-display-modes.md` | Progressive & Cross-Platform Web | Installability | Medium | Advanced | 16 min | Web App Manifest; Runtime Caching Strategies | Web App Manifest; Install Prompts & Criteria | 4 | Planned |
| Push Notifications | `push-notifications.md` | Progressive & Cross-Platform Web | Engagement | Medium | Advanced | 16 min | Web App Manifest | Badging & Periodic Sync | 4 | Planned |
| Badging & Periodic Sync | `badging-and-periodic-sync.md` | Progressive & Cross-Platform Web | Engagement | Medium | Advanced | 16 min | Push Notifications; Web App Manifest | Push Notifications | 4 | Planned |
| Web Views & Hybrid Apps | `web-views-and-hybrid-apps.md` | Progressive & Cross-Platform Web | Native Boundaries | Medium | Advanced | 16 min | Push Notifications | Wrapper Models (Capacitor); Web-to-Native Bridges | 4 | Planned |
| Wrapper Models (Capacitor) | `wrapper-models-capacitor.md` | Progressive & Cross-Platform Web | Native Boundaries | Medium | Advanced | 16 min | Web Views & Hybrid Apps; Push Notifications | Web Views & Hybrid Apps; Web-to-Native Bridges | 4 | Planned |
| Web-to-Native Bridges | `web-to-native-bridges.md` | Progressive & Cross-Platform Web | Native Boundaries | Medium | Advanced | 16 min | Web Views & Hybrid Apps; Push Notifications | Web Views & Hybrid Apps; Wrapper Models (Capacitor) | 4 | Planned |

---

## 08 · Craft & Leadership  ·  Priority: High  ·  37 articles

### Engineering Practices  (20 articles · ~335 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Naming | `naming.md` | Engineering Practices | Readable Code | High | Advanced | 16 min | Separation of Concerns · Frontend Architecture; The Testing Pyramid/Trophy · Testing & Quality | Function & Module Size; Comments & Intent | 1 | Planned |
| Function & Module Size | `function-and-module-size.md` | Engineering Practices | Readable Code | High | Advanced | 16 min | Naming | Naming; Comments & Intent | 1 | Planned |
| Comments & Intent | `comments-and-intent.md` | Engineering Practices | Readable Code | High | Advanced | 16 min | Naming | Naming; Function & Module Size | 1 | Planned |
| Refactoring | `refactoring.md` | Engineering Practices | Change & Debt | High | Advanced | 16 min | Naming | Managing Technical Debt; Legacy Code Strategy | 1 | Planned |
| Managing Technical Debt | `managing-technical-debt.md` | Engineering Practices | Change & Debt | High | Advanced | 16 min | Refactoring; Naming | Refactoring; Legacy Code Strategy | 1 | Planned |
| Legacy Code Strategy | `legacy-code-strategy.md` | Engineering Practices | Change & Debt | High | Advanced | 16 min | Refactoring; Naming | Refactoring; Managing Technical Debt | 1 | Planned |
| Abstraction & Leaky Abstractions | `abstraction-and-leaky-abstractions.md` | Engineering Practices | Design Principles | High | Advanced | 19 min | Refactoring | Coupling & Cohesion; SOLID for Frontend; YAGNI & Simplicity | 1 | Planned |
| Coupling & Cohesion | `coupling-and-cohesion.md` | Engineering Practices | Design Principles | High | Advanced | 16 min | Abstraction & Leaky Abstractions; Refactoring | Abstraction & Leaky Abstractions; SOLID for Frontend; YAGNI & Simplicity | 1 | Planned |
| SOLID for Frontend | `solid-for-frontend.md` | Engineering Practices | Design Principles | High | Advanced | 16 min | Abstraction & Leaky Abstractions; Refactoring | Abstraction & Leaky Abstractions; Coupling & Cohesion; YAGNI & Simplicity | 1 | Planned |
| YAGNI & Simplicity | `yagni-and-simplicity.md` | Engineering Practices | Design Principles | High | Advanced | 16 min | Abstraction & Leaky Abstractions; Refactoring | Abstraction & Leaky Abstractions; Coupling & Cohesion; SOLID for Frontend | 1 | Planned |
| Code Review as a Discipline | `code-review-as-a-discipline.md` | Engineering Practices | Review | High | Advanced | 19 min | Abstraction & Leaky Abstractions | Giving & Receiving Feedback | 1 | Planned |
| Giving & Receiving Feedback | `giving-and-receiving-feedback.md` | Engineering Practices | Review | High | Advanced | 19 min | Code Review as a Discipline; Abstraction & Leaky Abstractions | Code Review as a Discipline | 1 | Planned |
| Error-Handling Philosophy | `error-handling-philosophy.md` | Engineering Practices | Robustness | High | Advanced | 16 min | Code Review as a Discipline | Defensive vs Offensive Programming; Graceful Degradation | 1 | Planned |
| Defensive vs Offensive Programming | `defensive-vs-offensive-programming.md` | Engineering Practices | Robustness | High | Advanced | 19 min | Error-Handling Philosophy; Code Review as a Discipline | Error-Handling Philosophy; Graceful Degradation | 1 | Planned |
| Graceful Degradation | `graceful-degradation.md` | Engineering Practices | Robustness | High | Advanced | 16 min | Error-Handling Philosophy; Code Review as a Discipline | Error-Handling Philosophy; Defensive vs Offensive Programming | 1 | Planned |
| Documentation Practices | `documentation-practices.md` | Engineering Practices | Knowledge | High | Advanced | 16 min | Error-Handling Philosophy | Knowledge Sharing & Bus Factor | 1 | Planned |
| Knowledge Sharing & Bus Factor | `knowledge-sharing-and-bus-factor.md` | Engineering Practices | Knowledge | High | Advanced | 19 min | Documentation Practices; Error-Handling Philosophy | Documentation Practices | 1 | Planned |
| API & Interface Stability | `api-and-interface-stability.md` | Engineering Practices | Interfaces | High | Advanced | 16 min | Documentation Practices | Backward Compatibility; Deprecation Strategy | 1 | Planned |
| Backward Compatibility | `backward-compatibility.md` | Engineering Practices | Interfaces | High | Advanced | 16 min | API & Interface Stability; Documentation Practices | API & Interface Stability; Deprecation Strategy | 1 | Planned |
| Deprecation Strategy | `deprecation-strategy.md` | Engineering Practices | Interfaces | High | Advanced | 16 min | API & Interface Stability; Documentation Practices | API & Interface Stability; Backward Compatibility | 1 | Planned |

### Systems Thinking & Leadership  (17 articles · ~364 min)

| Title | Slug | Category | Subcategory | Priority | Difficulty | Est. Reading Time | Prerequisites | Related Articles | Expected Code Examples | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Trade-off Analysis | `trade-off-analysis.md` | Systems Thinking & Leadership | Decisions | High | Staff | 20 min | Separation of Concerns · Frontend Architecture; Naming · Engineering Practices | Decision-Making Under Uncertainty; Build vs Buy | 1 | Planned |
| Decision-Making Under Uncertainty | `decision-making-under-uncertainty.md` | Systems Thinking & Leadership | Decisions | High | Staff | 23 min | Trade-off Analysis | Trade-off Analysis; Build vs Buy | 1 | Planned |
| Build vs Buy | `build-vs-buy.md` | Systems Thinking & Leadership | Decisions | High | Staff | 20 min | Trade-off Analysis | Trade-off Analysis; Decision-Making Under Uncertainty | 1 | Planned |
| Technical Design & RFCs | `technical-design-and-rfcs.md` | Systems Thinking & Leadership | Technical Direction | High | Staff | 20 min | Trade-off Analysis | Setting Standards & Guardrails; Driving Consistency at Scale | 1 | Planned |
| Setting Standards & Guardrails | `setting-standards-and-guardrails.md` | Systems Thinking & Leadership | Technical Direction | High | Staff | 23 min | Technical Design & RFCs; Trade-off Analysis | Technical Design & RFCs; Driving Consistency at Scale | 1 | Planned |
| Driving Consistency at Scale | `driving-consistency-at-scale.md` | Systems Thinking & Leadership | Technical Direction | High | Staff | 23 min | Technical Design & RFCs; Trade-off Analysis | Technical Design & RFCs; Setting Standards & Guardrails | 1 | Planned |
| Estimation | `estimation.md` | Systems Thinking & Leadership | Planning | High | Staff | 20 min | Technical Design & RFCs | Scoping & Slicing Work; Risk Management | 1 | Planned |
| Scoping & Slicing Work | `scoping-and-slicing-work.md` | Systems Thinking & Leadership | Planning | High | Staff | 20 min | Estimation; Technical Design & RFCs | Estimation; Risk Management | 1 | Planned |
| Risk Management | `risk-management.md` | Systems Thinking & Leadership | Planning | High | Staff | 20 min | Estimation; Technical Design & RFCs | Estimation; Scoping & Slicing Work | 1 | Planned |
| Cross-Functional Partnership | `cross-functional-partnership.md` | Systems Thinking & Leadership | Collaboration | High | Staff | 23 min | Estimation | Influence Without Authority; Communicating Technical Concepts | 1 | Planned |
| Influence Without Authority | `influence-without-authority.md` | Systems Thinking & Leadership | Collaboration | High | Staff | 23 min | Cross-Functional Partnership; Estimation | Cross-Functional Partnership; Communicating Technical Concepts | 1 | Planned |
| Communicating Technical Concepts | `communicating-technical-concepts.md` | Systems Thinking & Leadership | Collaboration | High | Staff | 23 min | Cross-Functional Partnership; Estimation | Cross-Functional Partnership; Influence Without Authority | 1 | Planned |
| Mentorship | `mentorship.md` | Systems Thinking & Leadership | Growth | High | Staff | 20 min | Cross-Functional Partnership | Technical Leadership Styles | 1 | Planned |
| Technical Leadership Styles | `technical-leadership-styles.md` | Systems Thinking & Leadership | Growth | High | Staff | 23 min | Mentorship; Cross-Functional Partnership | Mentorship | 1 | Planned |
| Evaluating Technology | `evaluating-technology.md` | Systems Thinking & Leadership | Technology Strategy | High | Staff | 20 min | Mentorship | Adoption & Migration Strategy; Innovation vs Stability | 1 | Planned |
| Adoption & Migration Strategy | `adoption-and-migration-strategy.md` | Systems Thinking & Leadership | Technology Strategy | High | Staff | 23 min | Evaluating Technology; Mentorship | Evaluating Technology; Innovation vs Stability | 1 | Planned |
| Innovation vs Stability | `innovation-vs-stability.md` | Systems Thinking & Leadership | Technology Strategy | High | Staff | 20 min | Evaluating Technology; Mentorship | Evaluating Technology; Adoption & Migration Strategy | 1 | Planned |

---

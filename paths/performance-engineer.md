# Performance Engineer — Learning Path

> An engineer who owns the speed of the application across loading, runtime, and delivery.

**Level:** Advanced · **Required:** 91 articles (~19.0 h) · **Optional:** 16 articles (~3.8 h)

Difficulty of required articles: Foundational 24 · Intermediate 54 · Advanced 13.

Follow the sections in order. Articles link into [`docs/`](../docs/); each shows its difficulty and estimated reading time. Full prerequisites for any article are in its domain's `graph.json` (see [GRAPH.md](../GRAPH.md)).

## Milestones

1. Measure and interpret Core Web Vitals in lab and field
2. Optimize the critical rendering path and loading strategy
3. Diagnose runtime cost, long tasks, and memory growth
4. Tune caching across HTTP, build, and service-worker layers
5. Prevent regressions with budgets and CI gates

## Expected skills

By completing the required articles you should be able to:

- End-to-end performance profiling and diagnosis
- Loading, runtime, and memory optimization
- Cross-layer caching strategy
- A performance culture with budgets and monitoring

## Required articles

### The Web Platform

- [HTML Parsing & DOM Construction](../docs/00-foundations/web-platform/html-parsing-and-dom-construction.md) · Foundational · 11 min
- [Style Calculation](../docs/00-foundations/web-platform/style-calculation.md) · Foundational · 8 min
- [Layout & Reflow](../docs/00-foundations/web-platform/layout-and-reflow.md) · Foundational · 8 min
- [Paint & Layerization](../docs/00-foundations/web-platform/paint-and-layerization.md) · Foundational · 8 min
- [Compositing](../docs/00-foundations/web-platform/compositing.md) · Foundational · 8 min
- [Tasks & the Callback Queue](../docs/00-foundations/web-platform/tasks-and-the-callback-queue.md) · Foundational · 8 min
- [Microtasks & the Job Queue](../docs/00-foundations/web-platform/microtasks-and-the-job-queue.md) · Foundational · 8 min
- [Rendering & rAF Timing](../docs/00-foundations/web-platform/rendering-and-raf-timing.md) · Foundational · 8 min
- [Long Tasks & Starvation](../docs/00-foundations/web-platform/long-tasks-and-starvation.md) · Foundational · 8 min

### Runtime & Execution

- [Parsing & Bytecode](../docs/00-foundations/runtime-execution/parsing-and-bytecode.md) · Intermediate · 12 min
- [JIT Compilation & Deoptimization](../docs/00-foundations/runtime-execution/jit-compilation-and-deoptimization.md) · Intermediate · 15 min
- [Hidden Classes & Shapes](../docs/00-foundations/runtime-execution/hidden-classes-and-shapes.md) · Intermediate · 12 min
- [Inline Caches](../docs/00-foundations/runtime-execution/inline-caches.md) · Intermediate · 12 min
- [The Memory Model & the Heap](../docs/00-foundations/runtime-execution/the-memory-model-and-the-heap.md) · Intermediate · 15 min
- [Garbage Collection Strategies](../docs/00-foundations/runtime-execution/garbage-collection-strategies.md) · Intermediate · 15 min
- [Retained Memory & Leak Detection](../docs/00-foundations/runtime-execution/retained-memory-and-leak-detection.md) · Intermediate · 15 min
- [Weak References & Finalizers](../docs/00-foundations/runtime-execution/weak-references-and-finalizers.md) · Intermediate · 15 min
- [Web Workers](../docs/00-foundations/runtime-execution/web-workers.md) · Intermediate · 12 min
- [Shared Workers & Message Passing](../docs/00-foundations/runtime-execution/shared-workers-and-message-passing.md) · Intermediate · 15 min
- [SharedArrayBuffer & Atomics](../docs/00-foundations/runtime-execution/sharedarraybuffer-and-atomics.md) · Intermediate · 15 min
- [Worklets](../docs/00-foundations/runtime-execution/worklets.md) · Intermediate · 12 min

### Networking & Protocols

- [HTTP/1.1 Semantics](../docs/00-foundations/networking-protocols/http-1-1-semantics.md) · Foundational · 8 min
- [HTTP/2 Multiplexing](../docs/00-foundations/networking-protocols/http-2-multiplexing.md) · Foundational · 8 min
- [HTTP/3 & QUIC](../docs/00-foundations/networking-protocols/http-3-and-quic.md) · Foundational · 8 min
- [Methods, Status Codes & Headers](../docs/00-foundations/networking-protocols/methods-status-codes-and-headers.md) · Foundational · 11 min
- [The HTTP Cache](../docs/00-foundations/networking-protocols/the-http-cache.md) · Foundational · 8 min
- [Cache-Control & Validators (ETag)](../docs/00-foundations/networking-protocols/cache-control-and-validators-etag.md) · Foundational · 11 min
- [CDN Caching Model](../docs/00-foundations/networking-protocols/cdn-caching-model.md) · Foundational · 8 min
- [Vary & Cache Keys](../docs/00-foundations/networking-protocols/vary-and-cache-keys.md) · Foundational · 8 min
- [Connection Lifecycle (DNS, TLS)](../docs/00-foundations/networking-protocols/connection-lifecycle-dns-tls.md) · Foundational · 11 min
- [Latency, Bandwidth & RTT](../docs/00-foundations/networking-protocols/latency-bandwidth-and-rtt.md) · Foundational · 8 min
- [Preconnect & Priority Hints](../docs/00-foundations/networking-protocols/preconnect-and-priority-hints.md) · Foundational · 11 min
- [JSON & Streaming JSON](../docs/00-foundations/networking-protocols/json-and-streaming-json.md) · Foundational · 8 min
- [Binary Formats (Protobuf, MessagePack)](../docs/00-foundations/networking-protocols/binary-formats-protobuf-messagepack.md) · Foundational · 11 min
- [Multipart & Form Encoding](../docs/00-foundations/networking-protocols/multipart-and-form-encoding.md) · Foundational · 8 min
- [Transport Compression (gzip, brotli)](../docs/00-foundations/networking-protocols/transport-compression-gzip-brotli.md) · Foundational · 11 min

### Performance Engineering

- [Core Web Vitals (LCP, INP, CLS)](../docs/05-reliability-quality/performance/core-web-vitals-lcp-inp-cls.md) · Intermediate · 15 min
- [Perceived vs Actual Performance](../docs/05-reliability-quality/performance/perceived-vs-actual-performance.md) · Intermediate · 15 min
- [Custom Performance Metrics](../docs/05-reliability-quality/performance/custom-performance-metrics.md) · Intermediate · 12 min
- [Lab vs Field Measurement](../docs/05-reliability-quality/performance/lab-vs-field-measurement.md) · Intermediate · 12 min
- [The Critical Rendering Path](../docs/05-reliability-quality/performance/the-critical-rendering-path.md) · Intermediate · 15 min
- [Code Splitting](../docs/05-reliability-quality/performance/code-splitting.md) · Intermediate · 12 min
- [Resource Prefetch & Preload](../docs/05-reliability-quality/performance/resource-prefetch-and-preload.md) · Intermediate · 15 min
- [Critical CSS & Above-the-Fold](../docs/05-reliability-quality/performance/critical-css-and-above-the-fold.md) · Intermediate · 15 min
- [Font & Asset Loading Strategy](../docs/05-reliability-quality/performance/font-and-asset-loading-strategy.md) · Intermediate · 15 min
- [Image Optimization](../docs/05-reliability-quality/performance/image-optimization.md) · Intermediate · 12 min
- [Media & Video Optimization](../docs/05-reliability-quality/performance/media-and-video-optimization.md) · Intermediate · 12 min
- [Bundle Size Optimization](../docs/05-reliability-quality/performance/bundle-size-optimization.md) · Intermediate · 12 min
- [Asset Minification & Compression](../docs/05-reliability-quality/performance/asset-minification-and-compression.md) · Intermediate · 15 min
- [Rendering Cost & Re-renders](../docs/05-reliability-quality/performance/rendering-cost-and-re-renders.md) · Intermediate · 15 min
- [Long Tasks & Main-Thread Work](../docs/05-reliability-quality/performance/long-tasks-and-main-thread-work.md) · Intermediate · 15 min
- [Debounce, Throttle & Scheduling](../docs/05-reliability-quality/performance/debounce-throttle-and-scheduling.md) · Intermediate · 15 min
- [Offloading to Workers](../docs/05-reliability-quality/performance/offloading-to-workers.md) · Intermediate · 12 min
- [Memory Profiling in Practice](../docs/05-reliability-quality/performance/memory-profiling-in-practice.md) · Intermediate · 15 min
- [Long-Session Memory Growth](../docs/05-reliability-quality/performance/long-session-memory-growth.md) · Intermediate · 12 min
- [Performance Budgets](../docs/05-reliability-quality/performance/performance-budgets.md) · Intermediate · 12 min
- [Regression Prevention & CI Gates](../docs/05-reliability-quality/performance/regression-prevention-and-ci-gates.md) · Intermediate · 15 min
- [Caching for Performance (cross-layer)](../docs/05-reliability-quality/performance/caching-for-performance-cross-layer.md) · Intermediate · 15 min

### Build Systems & Tooling

- [The Dependency Graph](../docs/06-engineering-systems/build-tooling/the-dependency-graph.md) · Intermediate · 12 min
- [Bundler Models](../docs/06-engineering-systems/build-tooling/bundler-models.md) · Intermediate · 12 min
- [Entry Points & Output](../docs/06-engineering-systems/build-tooling/entry-points-and-output.md) · Intermediate · 12 min
- [Tree Shaking](../docs/06-engineering-systems/build-tooling/tree-shaking.md) · Intermediate · 12 min
- [Dead Code Elimination](../docs/06-engineering-systems/build-tooling/dead-code-elimination.md) · Intermediate · 12 min
- [Chunking & Split Points](../docs/06-engineering-systems/build-tooling/chunking-and-split-points.md) · Intermediate · 12 min
- [Scope Hoisting](../docs/06-engineering-systems/build-tooling/scope-hoisting.md) · Intermediate · 12 min
- [Incremental Builds](../docs/06-engineering-systems/build-tooling/incremental-builds.md) · Advanced · 16 min
- [Persistent & Remote Cache](../docs/06-engineering-systems/build-tooling/persistent-and-remote-cache.md) · Advanced · 16 min
- [Cache Invalidation Keys](../docs/06-engineering-systems/build-tooling/cache-invalidation-keys.md) · Advanced · 16 min

### Rendering Architectures

- [The SSR Model](../docs/02-rendering-frameworks/rendering-architectures/the-ssr-model.md) · Intermediate · 12 min
- [Hydration](../docs/02-rendering-frameworks/rendering-architectures/hydration.md) · Intermediate · 12 min
- [Selective & Progressive Hydration](../docs/02-rendering-frameworks/rendering-architectures/selective-and-progressive-hydration.md) · Intermediate · 15 min
- [Hydration Mismatches](../docs/02-rendering-frameworks/rendering-architectures/hydration-mismatches.md) · Intermediate · 12 min
- [Static Site Generation](../docs/02-rendering-frameworks/rendering-architectures/static-site-generation.md) · Intermediate · 12 min
- [Incremental Static Regeneration](../docs/02-rendering-frameworks/rendering-architectures/incremental-static-regeneration.md) · Intermediate · 15 min
- [On-Demand Revalidation](../docs/02-rendering-frameworks/rendering-architectures/on-demand-revalidation.md) · Intermediate · 12 min
- [Streaming SSR](../docs/02-rendering-frameworks/rendering-architectures/streaming-ssr.md) · Advanced · 16 min
- [Progressive Rendering & Flushing](../docs/02-rendering-frameworks/rendering-architectures/progressive-rendering-and-flushing.md) · Advanced · 19 min
- [Out-of-Order Streaming](../docs/02-rendering-frameworks/rendering-architectures/out-of-order-streaming.md) · Advanced · 16 min

### Data & Server State

- [Pagination](../docs/03-application-architecture/data-server-state/pagination.md) · Intermediate · 12 min
- [Infinite & Cursor Loading](../docs/03-application-architecture/data-server-state/infinite-and-cursor-loading.md) · Intermediate · 12 min
- [List Virtualization](../docs/03-application-architecture/data-server-state/list-virtualization.md) · Intermediate · 12 min

### Animation & Motion

- [Compositor-Only Properties](../docs/04-interface-engineering/animation-motion/compositor-only-properties.md) · Intermediate · 12 min
- [Avoiding Layout Thrash](../docs/04-interface-engineering/animation-motion/avoiding-layout-thrash.md) · Intermediate · 12 min
- [The FLIP Technique](../docs/04-interface-engineering/animation-motion/the-flip-technique.md) · Intermediate · 12 min

### Progressive & Cross-Platform Web

- [Runtime Caching Strategies](../docs/07-platform-reach/progressive-web/runtime-caching-strategies.md) · Advanced · 16 min
- [Precaching & Offline Shell](../docs/07-platform-reach/progressive-web/precaching-and-offline-shell.md) · Advanced · 16 min
- [Background Sync](../docs/07-platform-reach/progressive-web/background-sync.md) · Advanced · 16 min
- [Cache Versioning & Cleanup](../docs/07-platform-reach/progressive-web/cache-versioning-and-cleanup.md) · Advanced · 16 min

### Observability & Reliability

- [RUM & Field Vitals](../docs/05-reliability-quality/observability/rum-and-field-vitals.md) · Advanced · 16 min
- [Session Replay](../docs/05-reliability-quality/observability/session-replay.md) · Advanced · 16 min
- [Sampling Strategies](../docs/05-reliability-quality/observability/sampling-strategies.md) · Advanced · 16 min

## Optional articles

### Browser APIs

- [Intersection Observer](../docs/00-foundations/browser-apis/intersection-observer.md) · Foundational · 8 min
- [Resize Observer](../docs/00-foundations/browser-apis/resize-observer.md) · Foundational · 8 min
- [Mutation Observer](../docs/00-foundations/browser-apis/mutation-observer.md) · Foundational · 8 min
- [Performance Observer](../docs/00-foundations/browser-apis/performance-observer.md) · Foundational · 8 min
- [Timers & requestIdleCallback](../docs/00-foundations/browser-apis/timers-and-requestidlecallback.md) · Foundational · 11 min
- [requestAnimationFrame](../docs/00-foundations/browser-apis/requestanimationframe.md) · Foundational · 8 min
- [The Scheduler API (postTask)](../docs/00-foundations/browser-apis/the-scheduler-api-posttask.md) · Foundational · 11 min

### Graphics & Immersive

- [The 2D Canvas Model](../docs/07-platform-reach/graphics-immersive/the-2d-canvas-model.md) · Staff · 20 min
- [OffscreenCanvas](../docs/07-platform-reach/graphics-immersive/offscreencanvas.md) · Staff · 20 min
- [Text & Path Rendering](../docs/07-platform-reach/graphics-immersive/text-and-path-rendering.md) · Staff · 20 min
- [WebGL Fundamentals](../docs/07-platform-reach/graphics-immersive/webgl-fundamentals.md) · Staff · 20 min
- [WebGPU](../docs/07-platform-reach/graphics-immersive/webgpu.md) · Staff · 20 min
- [Shaders & Pipelines](../docs/07-platform-reach/graphics-immersive/shaders-and-pipelines.md) · Staff · 20 min

### Delivery & Infrastructure

- [CDN Architecture](../docs/06-engineering-systems/delivery-infrastructure/cdn-architecture.md) · Advanced · 16 min
- [Edge Compute & Routing](../docs/06-engineering-systems/delivery-infrastructure/edge-compute-and-routing.md) · Advanced · 16 min
- [Immutable Asset URLs](../docs/06-engineering-systems/delivery-infrastructure/immutable-asset-urls.md) · Advanced · 16 min

---

[← All learning paths](./) · [Knowledge Map](../KNOWLEDGE_MAP.md) · [Dependency Graph](../GRAPH.md)

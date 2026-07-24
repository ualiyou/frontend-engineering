# Knowledge Map

> The knowledge architecture of **Frontend Engineering** — a hierarchical map of the durable engineering knowledge a frontend engineer accumulates from junior to staff. This is the navigation spine of the repository, not documentation. Each leaf is a *concept* that expands into one or more articles.

## How it is organized

The repository uses a four-level hierarchy so it can grow to 1000+ articles without the root ever widening:

```text
Part  →  Domain  →  Topic  →  Article
```

- **Parts** (`docs/00…08`) are the 9 numbered top-level tracks, ordered as a learning gradient from foundations to leadership. The root stays frozen at 9 Parts by design.
- **Domains** are the folders inside each Part; each has a README index.
- **Topics** are the entries listed in each domain's README; each expands into an article.
- **Articles** are the `.md` files, each following [`templates/article-template.md`](templates/article-template.md).

Seniority is expressed by the Part ordering and by per-article `level` metadata (*Foundational / Intermediate / Advanced / Staff*), **not** by separate audience folders — so no concept is written twice.

## Priority

| Part | Priority |
| --- | --- |
| [00 · Foundations](docs/00-foundations/) | Critical |
| [01 · Core Languages](docs/01-core-languages/) | Critical |
| [02 · Rendering & Frameworks](docs/02-rendering-frameworks/) | Critical |
| [03 · Application Architecture](docs/03-application-architecture/) | Critical |
| [04 · Interface Engineering](docs/04-interface-engineering/) | High |
| [05 · Reliability & Quality](docs/05-reliability-quality/) | Critical |
| [06 · Engineering Systems](docs/06-engineering-systems/) | High |
| [07 · Platform Reach](docs/07-platform-reach/) | Medium |
| [08 · Craft & Leadership](docs/08-craft-leadership/) | High |

## The map

```text
Frontend Engineering
├── 00 · Foundations  [Critical]
│   ├── Computer Science for Frontend
│   │   ├── Data Structures for UI (trees, graphs, maps)
│   │   ├── Algorithms in Practice (diffing, traversal, search)
│   │   ├── Complexity & Cost Models
│   │   ├── Immutability & Structural Sharing
│   │   ├── Finite State Machines & Statecharts
│   │   └── Concurrency vs Parallelism
│   ├── The Web Platform
│   │   ├── Browser Architecture (processes, sandboxing)
│   │   ├── The Rendering Pipeline (style, layout, paint, composite)
│   │   ├── DOM & CSSOM as Abstractions
│   │   ├── The Event Loop & Task Queues
│   │   ├── Reflow, Repaint & Compositing Layers
│   │   └── The Origin & URL Model
│   ├── Runtime & Execution
│   │   ├── Engine Internals (JIT, hidden classes, inline caches)
│   │   ├── Call Stack & Execution Contexts
│   │   ├── Microtasks vs Macrotasks
│   │   ├── Web Workers & Off-Main-Thread Compute
│   │   ├── Memory Model, GC & Leak Analysis
│   │   └── WebAssembly & Polyglot Runtimes
│   ├── Browser APIs
│   │   ├── Storage APIs (Web Storage, IndexedDB, Cache)
│   │   ├── Observer APIs (Intersection, Resize, Mutation)
│   │   ├── Media & Capture (Media, Clipboard, File, Geolocation)
│   │   ├── Navigation, History & the URL API
│   │   ├── Timing & Scheduling APIs
│   │   └── Capability Detection & Feature Policy
│   └── Networking & Protocols
│       ├── HTTP Semantics & Evolution (1.1, 2, 3)
│       ├── HTTP & CDN Caching Model (canonical)
│       ├── Connection Lifecycle & Latency
│       ├── Real-Time Protocols (WebSocket, SSE, WebRTC)
│       ├── Serialization & Data Formats
│       └── Compression & Content Negotiation
│
├── 01 · Core Languages  [Critical]
│   ├── HTML & Document Semantics
│   │   ├── Semantic Structure & Document Outline
│   │   ├── Native Form Controls
│   │   ├── Media & Embedded Content
│   │   ├── Metadata, SEO & Social Semantics
│   │   └── Templating & Content Models
│   ├── CSS & Visual Systems
│   │   ├── Cascade, Specificity & Inheritance
│   │   ├── Box Model & Formatting Contexts
│   │   ├── Layout Systems (flow, flexbox, grid, positioning)
│   │   ├── Responsive & Adaptive Design
│   │   ├── Typography & Vertical Rhythm
│   │   ├── Color Systems & Color Spaces
│   │   ├── Containment, Layers & Stacking Contexts
│   │   ├── CSS Architecture (scoping, naming, isolation)
│   │   └── Styling Strategies (utility, CSS-in-JS, zero-runtime)
│   ├── JavaScript
│   │   ├── Types, Coercion & Equality
│   │   ├── Scope, Closures & Environment Records
│   │   ├── Prototypes & Inheritance
│   │   ├── The `this` Binding Model
│   │   ├── Objects, Descriptors & Proxies
│   │   ├── Iterators, Generators & Protocols
│   │   ├── Asynchrony (promises, async/await)
│   │   ├── Modules & the Module System
│   │   ├── Functional Programming Patterns
│   │   └── Metaprogramming & Reflection
│   └── TypeScript
│       ├── Structural Typing & Assignability
│       ├── The Type Hierarchy (top, bottom, unit types)
│       ├── Generics & Constraints
│       ├── Conditional & Mapped Types
│       ├── Inference & Narrowing
│       ├── Variance & Soundness Trade-offs
│       ├── Type-Level Programming
│       ├── Declaration Files & Ambient Types
│       └── Modeling Domains with Types
│
├── 02 · Rendering & Frameworks  [Critical]
│   ├── Rendering Architectures
│   │   ├── Client-Side Rendering
│   │   ├── Server-Side Rendering & Hydration
│   │   ├── Static Generation & Incremental Regeneration
│   │   ├── Streaming & Progressive Rendering
│   │   ├── Islands & Partial Hydration
│   │   ├── The Server/Client Boundary
│   │   ├── Resumability vs Hydration
│   │   └── Edge vs Origin Rendering
│   ├── React
│   │   ├── Component Model & Reconciliation
│   │   ├── Rendering Lifecycle & Commit Phase
│   │   ├── Hooks & the Rules of State
│   │   ├── Effects & External-System Sync
│   │   ├── Context & Dependency Propagation
│   │   ├── Concurrent Rendering & Transitions
│   │   ├── Suspense & Async UI
│   │   ├── Server Components & Server Actions
│   │   ├── Memoization & Referential Stability
│   │   ├── Refs & Imperative Escape Hatches
│   │   └── Composition Patterns (compound, slots, render props)
│   ├── Reactivity & Framework Models
│   │   ├── Signals & Fine-Grained Reactivity
│   │   ├── Virtual DOM vs Compiled Reactivity
│   │   ├── Observables & Atoms
│   │   └── Declarative UI as a Mental Model
│   └── Routing
│       ├── Routing as Architecture
│       ├── Route Matching & the URL as State
│       ├── Nested, Parallel & Layout Routing
│       ├── Data Loading at Route Boundaries
│       ├── Navigation, Transitions & Prefetching
│       └── Route-Level Code Splitting
│
├── 03 · Application Architecture  [Critical]
│   ├── Frontend Architecture
│   │   ├── Separation of Concerns & Layering
│   │   ├── Module Boundaries & Dependency Direction
│   │   ├── Feature-Based & Domain-Driven Structure
│   │   ├── Micro-Frontends & Composition at Scale
│   │   ├── Rendering & Data-Fetching Boundaries
│   │   └── Architectural Decision Records & Trade-offs
│   ├── State Management
│   │   ├── Categories of State (server, client, URL, form, UI)
│   │   ├── Local vs Global Boundaries
│   │   ├── Derived & Computed State (canonical)
│   │   ├── Reactivity Models for State (atoms, stores)
│   │   ├── Unidirectional Flow & Event Sourcing
│   │   └── State Machines for UI Logic
│   ├── Data & Server State
│   │   ├── Data-Fetching Strategies & Boundaries
│   │   ├── Server-State Caching & Invalidation (TanStack Query, SWR)
│   │   ├── Optimistic Updates & Conflict Resolution (canonical)
│   │   ├── Pagination, Infinite Loading & Virtualization
│   │   ├── Normalization & Client Data Modeling
│   │   ├── Retry, Error & Resilience Patterns
│   │   └── Local-First & Sync Engines
│   ├── Forms & Validation
│   │   ├── Form State Models (React Hook Form)
│   │   ├── Controlled vs Uncontrolled Patterns
│   │   ├── Schema Validation & Type-Safe Contracts (Zod, Valibot)
│   │   ├── Error Handling & User Feedback
│   │   ├── Complex & Composite Inputs
│   │   └── Multi-Step & Persistent Flows
│   └── API Design & Contracts
│       ├── API Paradigms (REST, GraphQL, RPC)
│       ├── Contract Design & Versioning
│       ├── End-to-End Type Safety (tRPC, codegen)
│       ├── Schema-First & Contract Testing
│       └── Backend-for-Frontend Patterns
│
├── 04 · Interface Engineering  [High]
│   ├── Component & Interaction Design
│   │   ├── Component API Design & Contracts
│   │   ├── Composition vs Configuration
│   │   ├── Polymorphism & Component Flexibility
│   │   ├── Headless & Behavior-First Components
│   │   ├── Interaction & Focus Management (canonical)
│   │   └── Interface State Modeling (loading, empty, error)
│   ├── Design Systems
│   │   ├── Foundations & Primitives
│   │   ├── Token Architecture & Semantic Layering
│   │   ├── Theming & Multi-Brand Systems
│   │   ├── Library Governance & Versioning
│   │   ├── Distribution & Adoption
│   │   └── Documentation as Contract
│   ├── Accessibility
│   │   ├── Standards & Conformance (WCAG, ARIA)
│   │   ├── The Accessibility Tree & Assistive Tech
│   │   ├── Keyboard & Focus Models
│   │   ├── Semantics, Roles & States
│   │   ├── Inclusive Interaction & Motion
│   │   └── Testing & Auditing Accessibility
│   └── Animation & Motion
│       ├── Principles of Motion Design
│       ├── Declarative vs Imperative Animation
│       ├── Compositor-Driven Performance
│       ├── Gesture & Physics-Based Interaction
│       └── Transitions & Choreography
│
├── 05 · Reliability & Quality  [Critical]
│   ├── Performance Engineering
│   │   ├── Metrics & Perceived Speed (Core Web Vitals)
│   │   ├── The Critical Rendering Path
│   │   ├── Loading Strategies (splitting, lazy, prefetch)
│   │   ├── Runtime & Rendering Cost (incl. memoization)
│   │   ├── Asset, Image & Media Optimization
│   │   ├── Memory & Long-Session Performance
│   │   ├── Profiling, Budgets & Regression Prevention
│   │   └── Caching for Performance
│   ├── Security
│   │   ├── The Browser Security Model (same-origin, isolation)
│   │   ├── XSS & Injection
│   │   ├── CSRF & Request Integrity
│   │   ├── CSP & Trusted Types
│   │   ├── Auth, Sessions & Token Storage
│   │   ├── Supply Chain & Dependency Risk
│   │   └── Privacy, Data Handling & Compliance
│   ├── Testing & Quality
│   │   ├── Testing Strategy & the Pyramid
│   │   ├── Unit & Logic Testing
│   │   ├── Component & Integration Testing
│   │   ├── End-to-End & User-Flow Testing
│   │   ├── Behavior vs Implementation Philosophy
│   │   ├── Visual & Regression Testing
│   │   ├── Contract & Type-Level Testing
│   │   └── Reliability & Flakiness Management
│   └── Observability & Reliability
│       ├── Error Monitoring & Reporting
│       ├── Real User Monitoring & Field Data
│       ├── Logging, Tracing & Instrumentation
│       ├── Analytics & Product Telemetry
│       └── Incident Response & Postmortems
│
├── 06 · Engineering Systems  [High]
│   ├── Build Systems & Tooling
│   │   ├── Module Bundling & Dependency Graphs
│   │   ├── Transpilation & Compilation Targets
│   │   ├── Tree Shaking & Dead Code Elimination
│   │   ├── Code Splitting & Chunking Strategy
│   │   ├── Compilers & AST Transformations
│   │   ├── Source Maps & Debuggability
│   │   ├── Build Caching & Incrementality
│   │   └── Build Performance
│   ├── Package Architecture
│   │   ├── Package Management & Resolution
│   │   ├── Exports, Entry Points & Module Formats
│   │   ├── Publishing, Versioning & SemVer
│   │   └── Dependency & Peer-Dependency Strategy
│   ├── Developer Experience & Workflow
│   │   ├── Monorepo Architecture & Task Orchestration
│   │   ├── Linting, Formatting & Static Analysis
│   │   ├── Local Dev & Fast Feedback Loops
│   │   ├── Debugging Techniques & Tooling
│   │   ├── Version Control & Branching Models
│   │   ├── CI/CD Pipelines
│   │   └── Automation & Codemods
│   └── Delivery & Infrastructure
│       ├── Hosting & Deployment Models
│       ├── CDNs & the Edge Runtime
│       ├── Environments, Config & Secrets
│       ├── Release Strategies (canary, blue-green, rollback)
│       ├── Feature Flags & Progressive Rollout
│       └── Cost, Scaling & Capacity
│
├── 07 · Platform Reach  [Medium]
│   ├── Internationalization & Localization
│   │   ├── Locale, Language & Regional Formatting
│   │   ├── Translation Architecture & Catalogs
│   │   ├── Pluralization, Gender & Grammar
│   │   ├── Bidirectional & Complex-Script Layout
│   │   └── Cultural & Content Adaptation
│   ├── Progressive & Cross-Platform Web
│   │   ├── Service Workers & the Offline Model
│   │   ├── Runtime Caching & App Shell
│   │   ├── Installability & Web App Manifests
│   │   ├── Background Sync & Push
│   │   └── Web-to-Native Boundaries
│   └── Graphics & Immersive
│       ├── The Canvas Rendering Model
│       ├── SVG & Vector Graphics
│       ├── GPU Rendering (WebGL, WebGPU)
│       ├── Data Visualization Foundations
│       └── Immersive Interfaces (XR, spatial)
│
└── 08 · Craft & Leadership  [High]
    ├── Engineering Practices
    │   ├── Code Readability & Naming
    │   ├── Refactoring & Technical Debt
    │   ├── Abstraction & Design Principles
    │   ├── Code Review as a Discipline
    │   ├── Error-Handling Philosophy
    │   ├── Documentation & Knowledge Sharing
    │   └── API & Interface Stability
    └── Systems Thinking & Leadership
        ├── Trade-off Analysis & Decision-Making
        ├── Technical Design & RFC Processes
        ├── Estimation, Scoping & Planning
        ├── Cross-Functional Collaboration
        ├── Mentorship & Technical Direction
        └── Evaluating & Adopting Technology
```

## Design rules (for contributors)

- **One canonical home per concept.** Caching, for example, is deliberately split across four layers that each own their article and cross-link the rest: HTTP/CDN cache (`00-foundations/networking-protocols`), server-state cache (`03-application-architecture/data-server-state`), build cache (`06-engineering-systems/build-tooling`), and service-worker runtime cache (`07-platform-reach/progressive-web`).
- **Libraries are articles, not domains.** TanStack Query, React Hook Form, Zod and the like live as articles under the durable topic they exemplify, so the map survives ecosystem churn.
- **7±2 split rule.** When a topic exceeds ~7 articles it promotes a subtopic; when a domain exceeds ~7 topics it splits. The 9 Parts do not grow.
- **Stable slugs.** Numbered prefixes order the Parts; article slugs stay stable independently so links and SEO survive reordering.

## Future expansion strategy

Growth happens at the leaves, never at the root. Nine Parts × ~4 domains × ~6 topics × ~5 articles ≈ 1,000 articles under a stable, navigable tree. New material either extends the canonical article for a concept or cross-links to it — it never re-explains. Curated learning paths (a future `paths/` index) stitch articles across domains into journeys (e.g. *becoming senior*, *rendering deep-dive*, *performance track*) without duplicating content.

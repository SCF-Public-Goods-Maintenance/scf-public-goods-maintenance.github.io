---
title: Dashboard
parent: PG Atlas Architecture
nav_order: 6
---

# Dashboard

## Overview

The PG Atlas dashboard provides public read-only access to ecosystem metrics, project details, and
dependency visualizations. The dashboard is live at [pgatlas.xyz](https://pgatlas.xyz), serving SCF
voters, project maintainers, and community observers with transparent insights into the
Stellar/Soroban public goods ecosystem.

**Current status**: Operational with eight primary pages (home, projects, repos, contributors,
rounds, graph, gitlog, about), consuming the REST API at [api.pgatlas.xyz](https://api.pgatlas.xyz).

**Architecture**:

- **React 19** with **Vite** for fast development and builds
- **TanStack Router** for type-safe routing and **TanStack Query** for data fetching/caching
- **Tailwind CSS** for styling with responsive design
- **@pg-atlas/data-sdk** TypeScript SDK for REST API consumption
- **Cytoscape.js** for interactive dependency graph visualization
- **Recharts** for data visualization
- Deployed on **DigitalOcean App Platform** as a static site

## Pages

The dashboard implements the following routes:

**Dashboard** ([pgatlas.xyz](https://pgatlas.xyz)):

- Live ecosystem health metrics (total projects, repos, dependencies)
- Risk distribution visualization (pony factor, criticality)
- Top critical projects leaderboard
- Data transparency panel documenting provenance and processing

**Projects** ([pgatlas.xyz/projects](https://pgatlas.xyz/projects)):

- Paginated list of SCF-funded projects with filtering and sorting
- Manual column filtering and sorting by criticality, pony factor, adoption score
- Search by project name
- URL state synchronization for filters and pagination

**Project Detail**
([pgatlas.xyz/projects/:canonical_id](https://pgatlas.xyz/projects/:canonical_id)):

- Detailed metrics panel (criticality score, pony factor, adoption score, active contributors)
- Associated repositories panel
- Contributors panel with commit counts
- **Sub-graph explorer** showing dependency relationships (see below)
- Dependencies panel with tabular views of dependents and dependencies

**Repos** ([pgatlas.xyz/repos](https://pgatlas.xyz/repos)):

- Paginated list of repositories with filtering and sorting
- Manual column filtering and sorting by metrics
- URL state synchronization

**Repo Detail** ([pgatlas.xyz/repos/:canonical_id](https://pgatlas.xyz/repos/:canonical_id)):

- Metrics panel showing repo-level scores
- Parent project panel (if applicable)
- Contributors panel
- **Sub-graph explorer** showing dependency relationships (see below)
- Dependencies panel

**Contributors** ([pgatlas.xyz/contributors](https://pgatlas.xyz/contributors)):

- Paginated list of contributors with search
- URL state synchronization

**Contributor Detail** ([pgatlas.xyz/contributors/:id](https://pgatlas.xyz/contributors/:id)):

- Total repos and commits across all contributions
- First and last contribution dates
- Per-repo contribution breakdown with commit counts

**Rounds** ([pgatlas.xyz/rounds](https://pgatlas.xyz/rounds)):

- List of SCF funding rounds
- Round-specific project overviews

**Round Detail** ([pgatlas.xyz/rounds/:round_id](https://pgatlas.xyz/rounds/:round_id)):

- SCF funding round overview
- Sortable/filterable project tables
- Per-project links to detail pages and Tansu proposals

**Graph** ([pgatlas.xyz/graph](https://pgatlas.xyz/graph)):

- Full ecosystem graph visualization (planned)

**Gitlog** ([pgatlas.xyz/gitlog](https://pgatlas.xyz/gitlog)):

- List of git log processing attempts
- Filter by repository
- URL state synchronization

**Gitlog Artifact Detail**
([pgatlas.xyz/gitlog/:artifact_id](https://pgatlas.xyz/gitlog/:artifact_id)):

- Processing attempt details
- Raw artifact content when available

**About** ([pgatlas.xyz/about](https://pgatlas.xyz/about)):

- Project information and documentation links

## Sub-Graph Explorer

The sub-graph explorer is an interactive dependency graph viewer implemented on both project and repo
detail pages. It provides incremental, on-demand loading of dependency relationships driven by user
interaction.

### Implementation

**Library**: **Cytoscape.js** — A graph theory library for visualization and analysis. The component
manages the Cytoscape instance imperatively via `useRef`.

**API Integration**: The explorer calls the following SDK endpoints based on page type and traversal
direction:

| Page Type | Direction    | Endpoint                      |
| --------- | ------------ | ----------------------------- |
| Project   | Dependents   | `getProjectHasDependents(id)` |
| Project   | Dependencies | `getProjectDependsOn(id)`     |
| Repo      | Dependents   | `getRepoHasDependents(id)`    |
| Repo      | Dependencies | `getRepoDependsOn(id)`        |

### User Interaction and Lazy Loading

The explorer implements incremental graph expansion through user interaction:

**Initial Load**:

1. Cytoscape instance initializes with the central focus node (current project or repo)
2. Immediate neighbors are loaded in the default "dependents" direction
3. Initial layout applied using the `cose` (Compound Spring Embedder) algorithm

**Node Expansion**:

1. User clicks on a neighbor node
2. `expandNode` function fetches neighbors of the clicked node in the current `TraversalDirection`
3. New nodes and edges added to the Cytoscape instance
4. Layout algorithm runs on the newly added nodes and their neighborhood

**Direction Toggle**:

1. User switches between "dependents" (incoming) and "dependencies" (outgoing) via toggle buttons
2. `handleDirectionChange` triggers `expandNode` for the root node in the new direction
3. Graph updates to show relationships in the selected direction

**State Management**:

- Nodes that have been expanded in a particular direction are not re-expanded
- Loading states shown during API calls
- Visual differentiation for root nodes, expanded nodes, and leaf nodes

### Styling and Visual Cues

The explorer applies distinct styling for different node types:

- **Project nodes** — Distinct color/shape
- **Repo nodes** — Different styling from projects
- **External repo nodes** — Differentiated from in-ecosystem repos
- **Root node** — Highlighted to show focus
- **Loading indicators** — Visual feedback during API calls

## Technology Stack

**Framework**: React 19 with Vite build tooling provides fast hot module replacement during
development and optimized production builds.

**Routing & State**: TanStack Router handles type-safe routing with automatic route generation and
React.lazy() code splitting. TanStack Query manages server state with automatic caching, background
refetching, and stale data management using Suspense-based data fetching.

**Data Layer**: The
[@pg-atlas/data-sdk](https://github.com/SCF-Public-Goods-Maintenance/pg-atlas-ts-sdk) TypeScript SDK
provides type-safe API access with automatic request/response validation. The `apiAdapter` and
`dashboardService` modules wrap SDK calls with error handling and fallback logic.

**Deployment**: DigitalOcean App Platform hosts the static site with automatic deployment on pushes
to the `main` branch. The dashboard is served from the Amsterdam region with CDN distribution.

### API Integration Pattern

The dashboard follows a Suspense-based data fetching pattern:

1. Page routes define data requirements via TanStack Query hooks with Suspense
2. Service layer (`src/lib/services/`) wraps SDK calls with error boundaries
3. TanStack Query handles caching, deduplication, and background updates
4. UI components render from cached data with Suspense boundaries for loading states

Example data flow:

```typescript
// Route-level data requirement with Suspense
export const Route = createFileRoute("/projects/$canonicalId")({
  loader: ({ params }) => queryClient.ensureQueryData(projectDetailQueryOptions(params.canonicalId)),
});

// Component consumes data via Suspense hook
const ProjectDetail = () => {
  const { canonicalId } = Route.useParams();
  const data = useProjectDetailSuspense(canonicalId);
  // ...render with guaranteed data
};
```

## Design Principles

The dashboard prioritizes transparency, accessibility, and explorability:

- **Fast loading** — Cached metrics via TanStack Query, lazy rendering for graphs, code splitting
- **Clear explanations** — Tooltips and help text for all metrics
- **Accessibility** — Dark/light mode support, keyboard navigation, screen-reader labels
- **Progressive disclosure** — Summary views → detail pages → interactive visualizations
- **Risk signaling** — Educational and balanced (PG Atlas is not a security scanner)
- **URL state** — Filters, sorts, and pagination synced with browser URL for shareable links

## Future Enhancements

Near-term improvements under consideration:

- **Full-graph explorer** — Ecosystem-wide graph visualization with search and filters (deferred to
  v1)
- **Export functionality** — CSV downloads for tables, PNG/SVG exports for visualizations
- **Enhanced sub-graph features** — Node search, filtering by confidence level, path highlighting
- **Time-series visualizations** — Historical metric trends on project detail pages

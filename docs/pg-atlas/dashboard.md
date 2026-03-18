---
title: Dashboard
parent: PG Atlas Architecture
nav_order: 6
---

# Dashboard

## User Stories

As a **PG maintainer**:

- I want to see my tool's criticality score, pony factor, and adoption trends so I can understand its
  ecosystem impact and prioritize maintenance.
- I want to view direct/transitive dependents (with active filters) to identify who relies on me and
  reach out for feedback/contributions.

As an **SCF voter/Pilot (Tansu round participant)**:

- I want a searchable leaderboard of PGs ranked by metrics (criticality, risk flags) so I can quickly
  evaluate proposals with objective context.
- I want to see a ranked list of public goods by criticality and adoption signals (stars, downloads,
  forks) so I can quickly spot high-leverage PGs.
- I want to filter by activity status (live / discontinued / non-responsive) to avoid funding
  abandoned projects.
- I want to drill into a specific PG's dependency graph and score breakdown to inform my NQG-weighted
  vote.

As a **dependent project team (SCF Build applicant)**:

- I want to explore the PG landscape to discover reusable tools and see their reliability scores
  before integrating.
- I want to visualize my own project's dependencies to ensure I'm building on healthy infrastructure.

As a **general community member or observer**:

- I want an intuitive overview of ecosystem health (active PG coverage, pony factor distribution, top
  critical tools) to gauge Stellar/Soroban resilience.
- I want to search/browse the full graph to understand interconnections and spot risks/gaps.

## Roles and access

- **Regular viewers (public)**: No authentication. Read-only access to leaderboard, PG detail pages,
  graph explorer, and basic filters.
- **SCF voters/Pilots**: Authenticated with a connected wallet (PG Award/SCF identity derived from
  the wallet). In addition to public views, can access voting/review tools (e.g., shortlists, review
  notes) and any reviewer-only risk metrics.
- **PG maintainers**: Authenticated with a connected wallet that is linked to the repos/PGs they
  control. In addition to public views, can see maintainer-focused panels (SBOM submission
  status/errors, data quality issues, suggested actions) for their own PGs.
- **Project teams (SCF Build applicants)**: Authenticated with a connected wallet that identifies
  their team/project. Can access a \"my project\" view that highlights their project's dependencies.

Authentication flow (high level):

- Landing page is public and includes a prominent \"Open Dashboard\" button.
- Clicking \"Open Dashboard\" triggers wallet connect; the resulting identity is mapped to one or
  more roles (regular viewer, voter/pilot, maintainer, project team).
- The dashboard surface and available actions are then tailored to the resolved roles.

## Desired UX Overview

The dashboard should be public, zero-auth (read-only), mobile-responsive, and focused on
**transparency and explorability**. Core flows:

- Landing page: High-level ecosystem summary (total active nodes, dependency coverage %, risk
  heatmap, top 10 critical PGs).
- Searchable leaderboard: Table view with filters/sort (criticality, pony factor, adoption, active
  status) and risk flags (e.g., red for `pony_factor == 1`).
- PG detail pages: Score breakdown, timeline trends (if extended), direct dependents list,
  interactive dependency subgraph visualization.
- Graph explorer: Interactive full/zoomed view (force-directed or hierarchical layout) with active
  subgraph highlighting and search/highlight nodes.

**UX principles**:

- Fast loading (cached metrics, lazy graph rendering).
- Clear tooltips/explainers for metrics (e.g., "Criticality = number of active projects depending on
  this").
- Export options (CSV for tables, PNG/SVG for graphs).
- Accessibility: Dark/light mode, keyboard navigation, screen-reader labels.
- No overload: Progressive disclosure (summary → detail → full graph).

<!-- FUTURE SELF: Wireframes or Figma link once prototyped. -->

## UI structure (pages → components → elements)

### Page types (top level)

- **Landing page**
  - Public entry point with:
    - A **hero section** (title, short paragraph on what PG Atlas is, and a prominent "Open
      Dashboard" wallet-connect button, duplicated as a primary action button in the site header,
      plus a short note that PG Atlas is open source and built for the community, with a link to the
      GitHub repositories inviting contributions).
    - A **key-metrics strip** showing a small set of headline numbers (e.g. total projects, total
      repos, number of public goods, % with recent activity) to give an at-a-glance ecosystem view.
    - A **"How it works" section** that briefly explains data sources (SBOMs, repo metadata) and how
      metrics like criticality and pony factor are derived.
    - A **role teaser section** with one-sentence summaries for voters, maintainers, project teams,
      and general viewers, each linking into the relevant dashboard view.
    - A simple **footer** with links to documentation pages (API, ingestion, storage, operations), a
      clearly labeled "Contribute on GitHub" link to the pg-atlas frontend/backend repositories, and
      governance/privacy notes.
- **Dashboard / leaderboard page**
  - Central table of public goods/projects with filters, sorts, and risk/health badges.
  - **Base surface** (visible to all authenticated roles once the wallet is connected): leaderboard
    table, global filters (e.g. project type, activity status, basic risk flags), and navigation into
    project detail pages and graph views.
  - **Voter-only sections**: when the connected wallet resolves to a voter/pilot role, show
    additional UI such as "For voters" panels (shortlists, review notes, reviewer-only risk
    annotations) that are completely hidden for other roles.
  - **Maintainer-only sections**: when the wallet is linked to one or more PGs/repos, show
    maintainer-focused widgets on the dashboard (e.g. a "My PGs" filter/preset and at-risk PG tiles)
    and maintainer tools on the project detail view (SBOM status, data quality issues, suggested
    actions).
  - **Project-team-only sections**: when the wallet maps to a project team, expose a "My project"
    area on the dashboard highlighting their own projects, dependencies, and dependency health,
    alongside the public leaderboard.
- **Project detail page**
  - Deep-dive view for a single project/PG: metrics, associated repos, dependency subgraph, and
    role-specific panels (e.g. maintainer actions, voter tools).
- **Repo detail page (optional v0.5+)**
  - **Purpose**: Lets users inspect a single repository (e.g. a package or library) as a node in the
    dependency graph—its metadata, adoption signals, and how others depend on it or what it depends
    on.
  - **Used for**: Voters checking a specific repo’s health before a decision; maintainers seeing
    their repo’s dependents and SBOM status; project teams verifying a dependency’s criticality and
    freshness before adopting it.
  - **Content**: Focused view on one repo: metadata, adoption metrics (stars, forks, downloads from
    `repos` / `external_repos`), and incoming/outgoing edges in the graph (`depends_on`).
- **Graph explorer page (v1+)**
  - Full-graph visualization with search, highlighting, and filters for exploring the ecosystem.

### React components (containers with data & state)

- **`LandingLayout`**
  - Purpose: Layout for the public landing page.
  - Scope: Renders hero section, short explanation of PG Atlas, and the "Open Dashboard" button that
    triggers wallet connect and routes to the dashboard.
- **`DashboardLayout`**
  - Purpose: Top-level shell for authenticated and unauthenticated dashboard users.
  - Scope: Handles wallet connection state, role resolution, global filters (e.g. activity status),
    and layout for leaderboard, side panels, and graph previews.
- **`ProjectsLeaderboard`**
  - Purpose: Main table of public goods / projects.
  - Scope: Fetches aggregated metrics per project from the API (criticality, adoption_score,
    activity_status, pony_factor) and pushes filter/sort state into global app state.
- **`ProjectDetailView`**
  - Purpose: Detail page for a single project/PG.
  - Scope: Fetches project row (`projects`), associated repos (`repos`), and dependency subgraph
    (`repo_vertices`, `depends_on`), and composes sections for metrics, dependencies, and
    role-specific actions.
- **`RepoDetailView` (optional)**
  - Purpose: Detail panel for a single repo.
  - Scope: Fetches repo row (`repos`) and its neighborhood in the graph (`depends_on`) and shows
    adoption and risk signals.
- **`GraphExplorer`**
  - Purpose: Encapsulate the interactive graph visualization.
  - Scope: Renders a filtered subgraph using the chosen graph library and syncs selection/hover state
    back to the rest of the dashboard.

### Concrete UI elements (data fields and interactions)

- **Leaderboard row**
  - Data:
    - `projects.display_name`, `projects.canonical_id`
    - `projects.project_type`, `projects.activity_status`
    - `projects.criticality_score`, `projects.pony_factor`, `projects.adoption_score`
    - SCF round(s) and SCF category from `projects.metadata` (see below).
    - GitHub link from `projects.git_org_url` (clickable).
    - Awarded / funded indicator (from `projects.metadata` or backend; see below).
    - Aggregated repo metrics (e.g. stars/forks/downloads from `repos` and `external_repos`).
  - Interactions:
    - Click row → navigate to `ProjectDetailView`.
    - Click GitHub link → open project's GitHub org/repo in a new tab.
    - Click badges (e.g. activity status, SCF round) → apply quick filters.
- **Project metrics panel**
  - Data:
    - Single `projects` row: `criticality_score`, `pony_factor`, `adoption_score`, `metadata`,
      `updated_at`.
    - From `projects.metadata`: SCF round(s), SCF category, GitHub link (`git_org_url`), awarded
      status; optional `description`, `website`, `x_profile`.
    - Aggregated counts: number of `repos` and `repo_vertices` associated with the project.
  - Interactions:
    - Tooltips explaining each metric.
    - Link to GitHub (from `projects.git_org_url`); optional per-repo links from `repos.repo_url`.
    - Links to underlying repos or graph nodes.
- **Dependency subgraph panel**
  - Data:
    - Subset of `repo_vertices` and `depends_on` for the selected project or repo.
  - Interactions:
    - Hover node → highlight immediate neighbors and show mini-metric tooltip.
    - Click node → focus that repo (or open `RepoDetailView` in a side panel).
- **Maintainer actions panel** (role-gated)
  - Data:
    - `sbom_submissions` rows for repos in the project (status, error_detail, submitted_at).
  - Interactions:
    - Links or buttons to (future) SBOM upload flow or to view submission logs.

### Project and repo display fields (SCF round, category, GitHub, awarded)

The dashboard would surface the following so voters and observers can see SCF context and reach code:

- **SCF round(s)** Stored in `projects.metadata.scf_submissions` as a list of objects with `round`
  and `title`. The UI can show the latest round, a "Rounds" badge, or a short list (e.g. "Round 39,
  40"). Filtering the leaderboard by round is desirable (e.g. "Show only Round 40 projects").

- **SCF category** Stored in `projects.metadata.scf_category`. Display as a label or tag on the
  leaderboard row and on the project detail page; optionally allow filter by category.

- **Link to GitHub** From `projects.git_org_url` (org or primary repo URL). Shown as a clickable
  "GitHub" link on the leaderboard and project detail. On the project detail page, per-repo links can
  use `repos.repo_url` for each repo in the project.

- **Awarded / funded status** Not yet a dedicated column. Today it can be derived from
  `projects.metadata.scf_tranche_completion` (e.g. tranche completion indicates funding received), or
  the backend can expose an explicit `awarded` (or similar) field in the API (sourced from OpenGrants
  or a future ingest). The dashboard should show a clear "Awarded" / "Funded" (or "Not awarded")
  indicator on the leaderboard and project detail once the API provides it.

## Technology Decision

**Decided (Issue #3):** **Vite with TypeScript** (`react-ts` template). The dashboard will be a
custom TypeScript frontend, consuming the RESTful FastAPI backend exclusively (no direct DB access)
and dogfooding our OpenAPI-generated TypeScript SDK.

### Rationale

- **TypeScript SDK dogfooding** — We should be the first consumers of our own SDK; a Python dashboard
  would mean catching SDK ergonomics issues only when external developers hit them.
- **Contributor accessibility** — Vite with TypeScript is a widely adopted frontend stack. To attract
  contributions (bug fixes, visualizations, accessibility, localization), lowering the barrier
  matters. The ecosystem (shadcn/ui, React Flow, Tailwind, etc.) lets us move fast and benefit from
  community momentum.
- **Build tool choice** — Vite is the better choice for this client-side app: superior development
  speed, simplicity, and smaller production bundles.
- **Scoped v0** — A static Vite app with the leaderboard and basic PG detail pages, including a
  **sub-graph explorer on PG detail pages** so voters and maintainers get a transparent breakdown of
  derived metrics (criticality, score). The **full-graph** explorer can be deferred to v1; it is not
  essential for the Q2 PG Award.

### Ownership

[KoxyG](https://github.com/KoxyG) has taken ownership: build with **Vite's `react-ts` template**.
[GitHub Issue #3](https://github.com/scf-public-goods-maintenance/scf-public-goods-maintenance.github.io/issues/3).

## Open Questions

- **Sub-graph explorer on PG detail pages:** In scope for v0 (essential for the voter user story:
  "drill into a specific PG's dependency graph and score breakdown to inform my NQG-weighted vote").
  [@aolieman](https://github.com/aolieman) and [@jaygut](https://github.com/jaygut) to be involved in
  detailing the specs.
- **Graph viz library**: Not yet decided. Research is ongoing; the chosen library must support
  interactive (incremental) loading of additional vertices and edges. This doc will be updated once a
  library is selected.
- Analytics/integration (e.g. Plausible for usage tracking).
- Host on xlm.sh? What are its limitations compared to other static site hosting options?

<!-- QUESTION FOR KoxyG: Include mockup descriptions or Mermaid UI flow here? -->

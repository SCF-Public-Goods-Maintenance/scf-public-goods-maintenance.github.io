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

As an **SCF Pilot (Tansu round participant)**:

- I want a searchable leaderboard of PGs ranked by metrics (criticality, risk flags) so I can quickly
  evaluate proposals with objective context.
- I want to open a specific PG's dependency graph and score details so I can make a data-driven
  decision when casting my vote. As a **dependent project team (SCF Build applicant)**:

- I want to explore the PG landscape to discover reusable tools and see their reliability scores
  before integrating.
- I want to see a ranked list of dependencies by criticality and adoption signals (stars, downloads,
  forks) so I can quickly spot high-leverage tools to build on.
- I want to visualize my own project's dependencies to ensure I'm building on healthy infrastructure.

As a **general community member or observer**:

- I want an intuitive overview of ecosystem health (active PG coverage, pony factor distribution, top
  critical tools) to gauge Stellar/Soroban resilience.
- I want to search/browse the full graph to understand interconnections and spot risks/gaps.

## Desired UX Overview

The dashboard should be public, zero-auth (read-only), mobile-responsive, and focused on transparency
and explorability. Core flows:

- Dashboard landing page: High-level ecosystem summary (total active nodes, dependency coverage %,
  risk heatmap, top 10 critical PGs).
- PG Award Round pages: Per-round overview of proposals (each linked to a Project), with filters/sort
  (criticality, pony factor, adoption, active status) and risk flags (e.g., red for
  `pony_factor == 1`) where data exists; landing links current and past rounds.
  - Risk signaling would be progressive and educational (not alarmist): avoid marking most projects
    as severe risk by default when `pony_factor == 1` is common in the current ecosystem baseline.
  - Would position this page as a critical lens for PG maintenance funding decisions and continuous
    improvement, while keeping overall ecosystem-health messaging balanced.
- Contributor pages: Deep view of maintainer/contributor records for self-service data review and
  voter diligence.
- PG detail pages: Score breakdown, timeline trends (if extended), direct dependents list,
  interactive dependency subgraph visualization.
- Graph explorer (later feature, v1+): Interactive full/zoomed view (force-directed or hierarchical
  layout) with active subgraph highlighting and search/highlight nodes.

**UX principles**:

- Fast loading (cached metrics, lazy graph rendering).
- Clear tooltips/explainers for metrics (e.g., "Criticality = number of active projects depending on
  this").
- Export options (CSV for tables, PNG/SVG for graphs).
- Accessibility: Dark/light mode, keyboard navigation, screen-reader labels.
- No overload: Progressive disclosure (summary → detail → full graph).

<!-- FUTURE SELF: Wireframes or Figma link once prototyped. -->

## UI Structure

This section breaks the dashboard UI into three layers: pages, components, and concrete elements. Use
it as a map from high-level user-facing screens down to the specific data fields and interactions.

### Page Types (All Navigation Levels)

- Access model:
  - Landing page is public.
  - Dashboard pages are public and accessible without wallet connection.

- **Dashboard landing page**
  - Public entry point to the dashboard experience, with:
    - A **dashboard overview header** (title, selected round or global scope, last data refresh time,
      and quick actions such as open current round page, open contributor search).
    - A **headline metrics strip** with ecosystem and builder-activity totals (e.g. total projects,
      repos, public goods, % with recent activity, active contributors in 30/90 days, recent commit
      volume, and optional data-quality coverage indicators).
    - A **current round spotlight** showing the active PG Award round with a quick summary and a
      clear link into the full round page.
    - An **all rounds index** (table or list) linking to current and historical round pages.
    - A **data transparency panel** summarizing major data sources and processing notes, with links
      to docs and inline examples of canonical vs computed/aggregated labels used in the UI.
    - A **Tansu boundary note** clarifying that voting happens on Tansu: PG Atlas v0 does not embed
      Tansu, does not show voting outcomes, and uses cross-links only (proposal list + deep links to
      Tansu, with return links back to PG Atlas project details).
- **PG Award Round page**
  - A rich overview of all **proposals** (each linked to **Project**) in a specific PG Award
    round—sortable/filterable tables, proposal summaries, and paths into project detail.
  - Voting itself happens on Tansu (out of scope for this dashboard); this page supports review and
    due diligence only.
  - The current round should be surfaced on the dashboard landing page, which should also provide a
    list or table of links to all current and past round pages.
  - Round ↔ proposal+project mappings would be maintained as YAML or JSON config files in the
    frontend repo (build-time).
  - What everyone has access to: public round tables, simple filters (like project type, activity
    status, and risk flags), plus links to project details and graph views.
- **Contributor page**
  - A rich overview of **all PG Atlas data** tied to **`contributors` rows**: identity linkage,
    contributed repos/projects, commit stats, dates, and any derived or displayed fields.
  - Contributors and maintainers use it to see what we store about them, and what is missing or
    incorrect (so they can request corrections or improved ingestion).
  - Voters use the same page to learn more about a PG maintainer’s track record, current workload,
    and recent git activity when evaluating proposals.
- **Project detail page**
  - Deep-dive view for a single project/PG: metrics, associated repos, and dependency subgraph.
- **Repo detail page**
  - **Purpose**: Lets users inspect a single repository (e.g. a package or library) as a node in the
    dependency graph—its metadata, adoption signals, and how others depend on it or what it depends
    on.
  - **Used for**: Voters checking a specific repo’s health/activity before a decision.
  - **Content**: Focused view on one repo: metadata, adoption metrics (stars, forks, downloads from
    `repos` / `external_repos`), and incoming/outgoing edges in the graph (`depends_on`).
- **Graph explorer page (v1+)**
  - Full-graph visualization with search, highlighting, and filters for exploring the ecosystem.

### React components

These are the primary stateful React containers that compose the dashboard experiences described
above. Each component maps to a key page or cross-page concern and defines where data fetching and UI
state live.

- **`DashboardLandingLayout`** (or `OverviewLayout`)
  - Purpose: Layout for the dashboard landing/overview page.
  - Scope: Renders the overview header, headline metrics, current round spotlight, all-rounds index,
    and data transparency panel; provides entry points into round and contributor views.
- **`DashboardLayout`**
  - Purpose: Shared application shell for dashboard pages.
  - Scope: Handles session/auth state, global navigation, and common UI chrome across Dashboard
    Landing, PG Award Round, Contributor, and detail views.
- **`AwardRoundPage` (or `RoundOverview`)**
  - Purpose: Per-round proposal list/overview for a single PG Award round.
  - Scope: Loads round config (YAML/JSON) for proposal⇄project mapping; fetches project metrics from
    the API; drives filters/sorts and navigation to `ProjectDetailView`.
- **`ContributorDetailView`**
  - Purpose: Contributor/maintainer overview page backed by `contributors` and `contributed_to` (and
    related API fields).
  - Scope: Surfaces stored fields, gaps, and recent activity for self-review and voter diligence.
- **`ProjectsLeaderboard`**
  - Purpose: Reusable project table (filters/sort, risk badges)—may power round pages, landing
    snippets, or global exploration depending on product scope.
  - Scope: Fetches aggregated metrics per project from the API (criticality, adoption_score,
    activity_status, pony_factor) and pushes filter/sort state into global app state.
- **`ProjectDetailView`**
  - Purpose: Detail page for a single project/PG.
  - Scope: Fetches project row (`projects`), associated repos (`repos`), dependency subgraph
    (`repo_vertices`, `depends_on`), and contributor data (`contributors`, `contributed_to`) for the
    project's repos; composes sections for metrics, dependencies, contributors, and role-specific
    actions.
- **`RepoDetailView` (optional)**
  - Purpose: Detail panel for a single repo.
  - Scope: Fetches repo row (`repos`), its neighborhood in the graph (`depends_on`), and contributors
    for this repo (`contributors` via `contributed_to`); shows adoption, risk signals, and
    contributor list.
- **`GraphExplorer`**
  - Purpose: Encapsulate the interactive graph visualization.
  - Scope: Renders a filtered subgraph using the chosen graph library and syncs selection/hover state
    back to the rest of the dashboard.

#### `AwardRoundPage` / `ProjectsLeaderboard` elements

- **Round-scoped leaderboard row**
  - Data:
    - `projects.display_name`, `projects.canonical_id`
    - `projects.project_type`, `projects.activity_status`
    - `projects.criticality_score`, `projects.pony_factor`, `projects.adoption_score`
    - SCF round(s) and SCF category from `projects.metadata` (see below).
    - GitHub link from `projects.git_org_url` (clickable).
    - Awarded / funded indicator (from `projects.metadata` or backend; see below).
    - Aggregated repo metrics (e.g. stars/forks/downloads from `repos` and `external_repos`).
    - Optional: contributor count or recent-activity indicator from `contributed_to` (e.g.
      `number_of_commits`, `last_commit_date`) aggregated across the project's repos.
  - Interactions:
    - Click row → navigate to `ProjectDetailView`.
    - Click GitHub link → open project's GitHub org/repo in a new tab.
    - Click badges (e.g. activity status, SCF round) → apply quick filters.

#### `ProjectDetailView` elements

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
    - Show a visible data-origin tag next to each rendered metric/field so users can distinguish
      canonical values vs computed/aggregated values at a glance.
    - Expose source labels in the same tag or tooltip (e.g. `Canonical - SCF (NQG)`,
      `Canonical - OpenGrants`, `Computed - PG Atlas`, `Aggregated - PG Atlas`).
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
- **Contributors panel**
  - Data:
    - From `contributors`: `id`, `name` (display only; `email_hash` is not shown for privacy).
    - From `contributed_to` (joined by `contributor_id`, `repo_id`; filter by project's repos or
      single repo): `number_of_commits`, `first_commit_date`, `last_commit_date` per contributor-repo
      pair.
  - UI: List or table of contributors for the project (or for a single repo in `RepoDetailView`),
    with commit counts and first/last commit dates; optionally sort by `number_of_commits` or
    `last_commit_date`.
  - Interactions:
    - Expand per-repo breakdown for a contributor when the view is project-scoped.

#### `ContributorDetailView` elements

- **Contributor profile and activity panel**
  - Data:
    - `contributors.id`, `contributors.name` (display only; `email_hash` remains hidden by default).
    - Joined `contributed_to` rows across repos/projects: `number_of_commits`, `first_commit_date`,
      `last_commit_date`, and repo/project associations via `repo_id`.
  - Interactions:
    - Show data-quality flags for missing or stale fields.
    - Filter by timeframe/project to evaluate current workload and recent activity.

#### `AwardRoundPage` / `ProjectDetailView` display fields

These shared project/repo display fields should be surfaced consistently across round pages and
project detail views so voters and observers can see SCF context and reach code quickly:

- **Data provenance tags (required)**
  - Every field shown on round/project pages would include a visible provenance marker:
    - `Canonical` for source-of-truth values imported from upstream systems.
    - `Computed` for derived values calculated by PG Atlas logic.
    - `Aggregated` for rollups across multiple rows/sources.
  - This requirement aligns with the transparency principle and should be applied consistently in
    both table cells and detail panels.

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
  - v0 API contract note: expose a dedicated `awarded_status` field on project responses to avoid
    ambiguous frontend inference.

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

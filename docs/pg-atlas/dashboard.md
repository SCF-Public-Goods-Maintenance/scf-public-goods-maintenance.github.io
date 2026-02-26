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

## Technology Decision

**Decided (Issue #3):** **Option C — React/Next.js** (or Vite). The dashboard will be a custom
TypeScript frontend, consuming the RESTful FastAPI backend exclusively (no direct DB access) and
dogfooding our OpenAPI-generated TypeScript SDK.

### Rationale

- **TypeScript SDK dogfooding** — We should be the first consumers of our own SDK; a Python
  dashboard would mean catching SDK ergonomics issues only when external developers hit them.
- **Contributor accessibility** — Next/TypeScript is the most widely adopted frontend stack. To
  attract contributions (bug fixes, visualizations, accessibility, localization), lowering the
  barrier matters. The ecosystem (shadcn/ui, React Flow, Tailwind, etc.) lets us move fast and
  benefit from community momentum.
- **Scoped v0** — A static Next.js app with the leaderboard and basic PG detail pages is achievable
  in the timeframe without over-engineering. The interactive graph explorer can be deferred to v1
  with a table-first approach initially.

### Ownership

[KoxyG](https://github.com/KoxyG) has taken ownership: build with **Next.js or Vite**, with team coordination to finalize and
confirm the features to include. See [GitHub Issue #3](https://github.com/scf-public-goods-maintenance/scf-public-goods-maintenance.github.io/issues/3).

## Open Questions


- Analytics/integration (e.g. Plausible for usage tracking).
- Include mockup descriptions or Mermaid UI flow in this doc?

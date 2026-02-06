---
title: Dashboard
parent: PG Atlas Architecture
nav_order: 6
---

# Dashboard

## User Stories

As a **PG maintainer**:

- I want to see my tool's criticality score, pony factor, and adoption trends so I can understand
its ecosystem impact and prioritize maintenance.
- I want to view direct/transitive dependents (with active filters) to identify who relies on me and
reach out for feedback/contributions.

As an **SCF voter/Pilot (Tansu round participant)**:

- I want a searchable leaderboard of PGs ranked by metrics (criticality, risk flags) so I can
quickly evaluate proposals with objective context.
- I want to drill into a specific PG's dependency graph and score breakdown to inform my
NQG-weighted vote.

As a **dependent project team (SCF Build applicant)**:

- I want to explore the PG landscape to discover reusable tools and see their reliability scores
before integrating.
- I want to visualize my own project's dependencies to ensure I'm building on healthy infrastructure.

As a **general community member or observer**:

- I want an intuitive overview of ecosystem health (active PG coverage, pony factor distribution,
top critical tools) to gauge Stellar/Soroban resilience.
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

## Implementation Options

We have a RESTful FastAPI backend with endpoints for nodes, scores, dependents, and bulk exports.
The dashboard consumes this API exclusively (no direct DB access).

### Option 1: Streamlit

**Description**: Build with Streamlit — rapid prototyping, data-focused, Python-only stack.

**Pros**:

- Extremely fast iteration (live reload, Python code for UI/logic).
- Built-in components for tables, charts (Altair/Plotly), search, caching.
- Graph viz via st.graphviz or pyvis integration.
- Hosting simplicity (Streamlit Community Cloud free tier or self-host).
- Low maintenance — aligns with Python backend team skills.

**Cons**:

- Limited custom UI flexibility (harder for complex interactive graph dragging/zooming).
- Mobile experience good but not pixel-perfect.
- Less "app-like" feel compared to full JS frameworks.

### Option 2: Dash

**Description**: Use Dash for interactive data apps with Plotly charts and Cytoscape.js for graph
visualization.

**Pros**:

- Superior interactive graphing (Cytoscape component native).
- Rich callbacks for dynamic filtering/search.
- Strong data table components (Dash DataTable with sorting/pagination).
- Deployable via same Python ecosystem (Gunicorn, Docker).
- Good for metric-heavy dashboards (built-in Plotly for trends/heatmaps).

**Cons**:

- Steeper learning curve than Streamlit for layout.
- Performance overhead for very large graphs (client-side rendering).
- Licensing nuance (Dash Enterprise paid; open-source core sufficient for v0).

### Option 3: Custom Build with React / Next.js

**Description**: Full custom frontend using Next.js (SSR/SSG), Tailwind CSS, and specialized
libraries (Vis.js, React-Flow, or Cytoscape.js for graphs; TanStack Table for leaderboards).

**Pros**:

- Maximum flexibility and polish (custom animations, advanced graph interactions, PWA potential).
- Best performance for large interactive graphs (WebGL options like sigma.js).
- Modern app feel, excellent mobile/responsive support.
- Static generation possible for landing/leaderboard (fast CDN hosting via Vercel/Netlify).
- Decouples frontend skills (JS/TS community contributions easier).
- Fully open-source.

**Cons**:

- Highest initial development time/effort.
- More complex deployment (unless we force a static build).
- Risk of over-engineering early features.

## Open Questions

- Prioritize speed-to-launch (Streamlit/Dash) vs. long-term polish (custom React)?
- Graph viz library choice (Cytoscape.js common across options)?
- Hosting strategy (single container vs. separate frontend/backend)?
- Analytics/integration needs (e.g., Plausible for usage tracking)?
- Can we use our own Typescript SDK (API client) with each of the options?
- Host on xlm.sh?

<!-- QUESTION FOR LEAD: Include mockup descriptions or Mermaid UI flow here? Which option leans
strongest for v0 timeline? -->

<!-- FUTURE SELF: Prototype one-pager for each option post-backend selection to compare real UX. -->

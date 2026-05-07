---
title: Extensibility
parent: PG Atlas Architecture
nav_order: 9
---

# Extensibility

## Overview

PG Atlas is designed for iterative evolution, supporting new signals, metrics, and data sources
without major rewrites. The current architecture (FastAPI + PostgreSQL + NetworkX) provides a stable
foundation for extensibility through modular components, versioned APIs, and well-defined extension
points.

**Current status**: Operational with extension patterns established in v0: registry crawler
abstraction, scheduled workflow framework, and metric computation and materialization.

**Guiding principles**:

- **Modular architecture** — Ingestion, storage, computation, API, and dashboard as loosely coupled
  components
- **Stable public interface** — API versioning strategy already communicates what is needed for a
  stable interface in v1
- **Data portability** — PostgreSQL schemas with clear migration paths
- **Community-driven growth** — PR-friendly extensions through documented patterns

## Extension Patterns

PG Atlas demonstrates extensibility through three operational patterns established during v0
development.

### Adding New Metrics

The pattern for new metric computation:

1. **Database schema** — Add materialized metric columns to `repos` and `projects` tables
2. **Computation logic** — Create task function in `pg_atlas/procrastinate/tasks.py`
3. **Database writer** — Bulk update metric values to minimize row lock contention
4. **API exposure** — Add field to response models in `pgatlas/api/models.py`
5. **Documentation** — Regenerate OpenAPI spec, release the API, and publish the TypeScript SDK

**Example**: The pony factor implementation reads from `contributed_to` edges, computes the minimum
set of contributors representing 50% of commits, and is materialized to both `repos.pony_factor` and
`projects.pony_factor` (aggregated as maximum across project repos).

### Adding Registry Crawlers

The registry crawler abstraction supports five operational ecosystems (npm, crates.io, PyPI, pub.dev,
Packagist) through a shared pattern:

1. **Abstract interface** — Inherit from base crawler class with standard methods
2. **HTTP client** — Use `httpx.AsyncClient` with retry logic and rate limiting
3. **Queue integration** — Enqueue pending packages via `registry-crawl` workflow
4. **Error handling** — Log failures and include them in the workflow's job summary

**Extension example**: Adding a new language ecosystem (e.g., Ruby gems, Go modules) requires
implementing the crawler interface and adding the ecosystem identifier to configuration.

## Future Extensions

Near-term enhancements under consideration:

### Additional Metrics

- **On-chain usage signals** — Soroban contract invocation counts, unique deployers, total value
  locked
- **Activity scoring refinement** — Replace 4-state enum with granular scoring based on commit
  recency and ecosystem engagement
- **Security indicators** — CVE feed integration, audit completion status, test coverage from CI

### Ingestion Sources

- **GitHub API data** — Issue/PR statistics, reviewer diversity, community health metrics
- **On-chain manifests** — Stellar/Soroban deployment metadata for usage tracking
- **Versioned dependency edges** — Per-release blast radius for vulnerability impact analysis

### API Enhancements

- **Trend histories** — Time-series endpoints for metric evolution
- **Transitive queries** — Blast radius calculations per package version
- **Webhooks** — Event notifications for metric changes (e.g. adoption score drops considerably)

### Dashboard Features

- **Risk heatmaps** — Visual grids showing contributor diversity vs. criticality distribution
- **Community contributions** — Pluggable visualization modules for specialized views
- **Export functionality** — CSV downloads, PNG/SVG visualization exports
- **Scope evolution**: Prioritize via working group roadmap; v1 gated on 2026 outcomes.

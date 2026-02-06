---
title: Extensibility & Migration
parent: PG Atlas Architecture
nav_order: 9
---

# Extensibility & Migration

## Overview

PG Atlas is designed for iterative evolution beyond v0, supporting new signals, metrics, and scale
without major rewrites. Extensibility focuses on modularity (abstracted layers, stable API) to
enable community contributions and future features. Migration paths preserve data and logic when
upgrading backends (e.g., from prototyping to production graph DB).

**Guiding principles**:

- **Modular architecture**: Ingestion, storage, computation, API, and dashboard as loosely coupled
components.
- **Stable public interface**: API endpoints versioned; backward compatibility for consumers
(dashboard, Tansu context).
- **Data portability**: Export/import formats (Gremlin bulk, JSON dumps) for backend swaps.
- **Community-driven growth**: PR-friendly extensions (new metrics via plugins, ingestion sources
via config).

**Long-term vision**: Evolve into a comprehensive ecosystem observatory (on-chain usage, security
scoring, predictive risk models) while remaining lightweight and transparent.

## Key Extensibility Areas

### New Metrics & Signals

- **On-chain integration**: Add user-facing classic/Soroban tx stats for usage weighting (v1+).
- **Advanced activity scoring**: Granular score replacing binary flag (commit recency, survey depth,
deployment signals).
- **Security/Quality**: CVE feeds, audit status attestation, test coverage from CI.
- **Plugin model**: Metric modules (Python classes) registered via config; computed in batch
pipeline.

<!-- STORAGE/IMPACT: New properties or side tables for additional signals (e.g., on-chain call
counts). -->

### Ingestion Extensions

- **New sources**: GH API for issue/PR stats (reviewer diversity), on-chain manifests.
- **Versioned blast radius**: Per-release dependency edges for vulnerability tracking.
- **External ecosystems**: Broader crawling (e.g. ZK libs reused in Stellar).

<!-- INGESTION CHANGE: Configurable crawlers; webhook for new event types. -->

### Storage & Backend Migration

- **Shortlist evolution**: Start with prototyping backend → migrate to JanusGraph (BerkeleyDB →
distributed Cassandra/Scylla).
- **Path**:
  1. Abstract operations (e.g., `GraphProvider` interface for traversals).
  2. Bulk export (Gremlin or SQL dump).
  3. Load into target (JanusGraph bulk loader).
- **Intermediate**: Sqlg over Postgres for Gremlin queries without full swap.

**Pros of planned migration**:

- Zero downtime (run parallel, switch API pointer).
- Data fidelity preserved.

### API & Dashboard Growth

- **New endpoints**: Transitive blast radius per version, trend histories.
- **Webhooks**: Notify on metric changes (e.g., pony factor drop).
- **Dashboard modules**: Community-submitted views (e.g., risk heatmap).

## Risks & Mitigations

- **Tech debt**: Strict abstraction enforcement; tests for provider swaps.
- **Scope creep**: Prioritize via working group roadmap; v1 gated on 2026 outcomes.
- **Contributor friction**: Clear extension guides (e.g., "add a metric" template).

## Open Questions

- Governance for new metric inclusion (working group vote vs. PR merge)?
- Timeline for first migration (post-v0 stability, or earlier for Gremlin benefits)?
- On-chain attestation for metrics (Soroban verifiable computations)?

<!-- FUTURE SELF: Draft extension guide template; benchmark migration on synthetic 10k-node graph.
-->

<!-- QUESTION FOR LEAD: Priority extensions post-v0 (on-chain usage vs. security signals)? -->

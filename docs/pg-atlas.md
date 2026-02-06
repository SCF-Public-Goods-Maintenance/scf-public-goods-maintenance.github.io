---
title: PG Atlas Architecture
nav_order: 4
has_children: true
---

# PG Atlas Architecture Documentation

Welcome to the technical architecture specification for **PG Atlas** — the metrics backbone for SCF's
Public Goods Maintenance program.

This site is under active development by the SCF Public Goods Working Group.

## Index

- [Overview & Goals](/pg-atlas/overview.md) — Defines the purpose, importance, v0 success criteria,
  scope boundaries, and open questions for PG Atlas.
- [Ingestion](/pg-atlas/ingestion.md) — Details SBOM submission workflow, shadow graph bootstrapping
  from registries, git contributor log processing, and validation strategies.
- [Storage](/pg-atlas/storage.md) — Describes the TinkerPop-compatible data model, shortlisted
  backend options (JanusGraph/BerkeleyDB, Sqlg/PostgreSQL, HugeGraph/RocksDB) with pros/cons, and
  migration considerations.
- [Metric Computation](/pg-atlas/metric-computation.md) — Explains active subgraph projection,
  criticality scoring via transitive dependents, pony factor calculation, basic adoption signals, and
  materialization approach.
- [API Layer](/pg-atlas/api.md) — Specifies RESTful FastAPI design, core endpoints for
  nodes/scores/dependencies, rate limiting, and OpenAPI documentation.
- [Dashboard](/pg-atlas/dashboard.md) — Outlines user stories, desired UX, and compares
  implementation options (Streamlit, Dash, custom React/Next.js).
- [Operations & Deployment](/pg-atlas/operations.md) — Lists requirements and compares hosting
  strategies including DigitalOcean hybrid, GitHub-maximal, xlm.sh frontend, and Fly.io.
- [Security & Privacy](/pg-atlas/security.md) — Covers privacy-first principles, personal data
  minimization, maintainer audit logging, and CIA triad measures.
- [Extensibility & Migration](/pg-atlas/extensibility.md) — Discusses modular paths for new
  metrics/signals, ingestion sources, backend migrations, and long-term evolution.

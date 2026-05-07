---
title: PG Atlas Architecture
has_children: true
nav_order: 4
---

# PG Atlas Architecture Documentation

Welcome to the technical architecture specification for **PG Atlas** — the metrics backbone for SCF's
Public Goods Maintenance program. This part of the site is updated by PG Atlas contributors.

## Index

- [Overview & Goals](pg-atlas/overview.md) — Explains the purpose of PG Atlas, its role in funding
  decisions, and its importance for ecosystem growth.
- [Ingestion](pg-atlas/ingestion.md) — Details SBOM submission workflows, automated graph
  bootstrapping, and contributor log processing.
- [Storage](pg-atlas/storage.md) — Describes the PostgreSQL-based data model with property graph
  design patterns and audit tables.
- [Metric Computation](pg-atlas/metric-computation.md) — Covers criticality scoring, pony factor
  analysis, and adoption signal computation.
- [API Layer](pg-atlas/api.md) — Specifies the FastAPI-based REST API with OpenAPI documentation for
  public access.
- [Dashboard](pg-atlas/dashboard.md) — Documents the React dashboard with Cytoscape.js sub-graph
  explorer and interactive filtering.
- [Operations & Deployment](pg-atlas/operations.md) — Lists hosting strategies, scheduled workflows,
  and operational monitoring.
- [Security & Privacy](pg-atlas/security.md) — Describes authentication, rate limiting, privacy
  measures, and audit trail strategy.
- [Extensibility](pg-atlas/extensibility.md) — Discusses extension patterns for metrics, crawlers,
  and scheduled workflows.
- [Graph Scaling](pg-atlas/graph-scaling.md) — Covers current PostgreSQL + NetworkX architecture and
  future scaling options.

---
title: PG Atlas Architecture
has_children: true
nav_order: 3
---

# PG Atlas Architecture Documentation

Welcome to the technical architecture specification for **PG Atlas** — the metrics backbone for SCF's
Public Goods Maintenance program.

This site is under active development by the SCF Public Goods Working Group.

## Index

- [Overview & Goals](pg-atlas/overview.md) — Explains the purpose of PG Atlas, its role in funding
  decisions, and its importance for ecosystem growth.
- [Ingestion](pg-atlas/ingestion.md) — Details SBOM submission workflows, automated graph
  bootstrapping, and contributor log processing.
- [Storage](pg-atlas/storage.md) — Describes the PostgreSQL-based data model, incremental updates,
  and auditability features.
- [Metric Computation](pg-atlas/metric-computation.md) — Covers criticality scoring, pony factor
  analysis, and adoption signal computation.
- [API Layer](pg-atlas/api.md) — Specifies the FastAPI-based design, endpoints, and OpenAPI
  documentation for public access.
- [Dashboard](pg-atlas/dashboard.md) — Outlines user stories, UX goals, and dashboard features for
  ecosystem transparency.
- [Operations & Deployment](pg-atlas/operations.md) — Lists hosting strategies, cost control
  measures, and deployment options.
- [Security & Privacy](pg-atlas/security.md) — Emphasizes privacy-first principles, data
  minimization, and defense-in-depth measures.
- [Extensibility & Migration](pg-atlas/extensibility.md) — Discusses modular architecture, new
  metrics, and long-term evolution paths.

---
title: API Layer
parent: PG Atlas Architecture
nav_order: 5
---

# API Layer

## Overview

The API layer exposes PG Atlas data and computed metrics to the public dashboard, Tansu voting
context, community tools, and third-party integrations. It is implemented with FastAPI, following
RESTful principles for predictability and ease of consumption.

**Key principles**:

- Read-only for v0 (no writes via public API — ingestion handled internally via webhooks/actions).
- No GraphQL — prevents expensive arbitrary queries that could overload single-machine backend.
- Resource-oriented endpoints with standard HTTP methods (primarily GET).
- Pagination, filtering, and sorting where appropriate.
- Rate limiting and caching to protect resources.
- Comprehensive OpenAPI specification auto-generated for language-agnostic access.

**Goals**:

- Enable transparent community verification of metrics.
- Provide off-chain context for Tansu rounds without on-chain dependency.
- Mitigate Python lock-in via OpenAPI docs and multi-language examples (TypeScript, Rust, Go).
- Support dashboard needs plus broader ecosystem tooling (e.g., custom scorecards, dependency
  alerts).

## Base URL & Formats

- Base: `/api/v1` (versioned for future stability).
- Response format: JSON (default); optional CSV for table structures and raw artifacts via Accept
  header.
- Error responses: Standard HTTP codes with JSON body `{ "detail": "message" }`, following FastAPI +
  Pydantic defaults.

## Authentication & Authorization (v0)

- Public read-only — no auth required.
- Future: API keys for higher rate limits or write access (admin ingestion).

## Rate Limiting

- Global: 100 requests/minute per IP (configurable).
- Burst protection via token bucket.
- Headers: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `Retry-After`.

## Core Endpoints (v0)

### Health & Metadata

- `GET /health` — Returns `{ "status": "ok", "last_computed": timestamp }`.
- `GET /metadata` — Ecosystem summary: total nodes/edges, active count, last full recompute.

### Ecosystem Projects

- `GET /projects` — List project vertices with pagination and filters.

  - Query params: `type=pg_root`, `active=true`, `search=keyword`, `limit=50`, `offset=0`.
  - Response: Paginated list with basic fields (id, display_name, type, active, latest_version,
    criticality_score, pony_factor).

- `GET /projects/{canonical_id}` — Detailed project vertex + edges view.
  - Includes: metadata, adoption signals, direct dependents and dependees.

### Dependencies

- `GET /projects/{canonical_id}/dependents` — Direct (active) dependents.

  - Query: `active=true`, `within_ecosystem=true`.

- `GET /projects/{canonical_id}/dependencies` — Direct/upstream dependencies.

  - Query: `active=true`, `within_ecosystem=true`.

- `GET /projects/{canonical_id}/blast-radius` — Transitive within-ecosystem dependents, only
  available for `type=pg_root` vertices, 404 otherwise.

### Metrics & Scores

These are early thoughts. Needs to be revisited after fleshing out use cases.

- `GET /scores` — Leaderboard of PGs sorted by composite or individual metric.

  - Query: `sort=-criticality`, `min_criticality=5`.

- `GET /scores/{canonical_id}` — Full PG Score breakdown (components JSON).

### Bulk Exports

- `GET /export/projects` — CSV/JSON dump of all nodes (cached quarterly).
- `GET /export/graph` — Simplified graph JSON (within-ecosystem nodes + edges array, for offline
  analysis).

## Caching & Performance

- Endpoint-level caching (Redis or in-memory for v0) for expensive reads (e.g., leaderboards).
- ETag/If-None-Match support for conditional requests.
- Background recompute does not block reads (serve last-known scores).

## OpenAPI & Client Generation

- Auto-documented at `/docs` (Swagger UI) and `/redoc`.
- Provide official Typescript SDK as an example of OpenAPI client generation.

## Open Questions

- Additional filters (e.g., by ecosystem, SCF project linkage)?
- Webhook for metric change notifications (post-v0)?
- Collect a list of use cases beyond the dashboard/Tansu.

<!-- FUTURE SELF: Add endpoint for pony factor raw stats once extended git parsing implemented. -->

<!-- INGESTION IMPACT: No public write endpoints in v0 — internal webhook separate from this
layer. -->

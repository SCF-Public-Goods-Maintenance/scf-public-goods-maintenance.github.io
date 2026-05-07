---
title: API Layer
parent: PG Atlas Architecture
nav_order: 5
---

# API Layer

## Overview

The PG Atlas REST API provides public access to dependency graph data, computed metrics, and
ecosystem insights. The API is live at [api.pgatlas.xyz](https://api.pgatlas.xyz/docs) with
interactive OpenAPI documentation.

**Design principles**:

- **Read-only public access** — No authentication required for reads (ingestion uses separate
  OIDC-protected endpoints)
- **REST architecture** — Resource-oriented endpoints with standard HTTP methods
- **OpenAPI-first** — Comprehensive specification auto-generated from FastAPI, enabling client
  generation
- **Rate-limited** — Per-IP limits prevent abuse while maintaining public accessibility
- **Server-side operations** — Sorting, filtering, and pagination handled by the backend
- **TypeScript SDK** — Auto-generated from OpenAPI spec at
  [pg-atlas-ts-sdk](https://github.com/SCF-Public-Goods-Maintenance/pg-atlas-ts-sdk)

For API versioning strategy and stability guarantees, see the
[API versioning documentation](https://github.com/SCF-Public-Goods-Maintenance/pg-atlas-backend/blob/main/pg_atlas/routers/api-versioning.md).

## Operational Endpoints

The complete API specification is available at [api.pgatlas.xyz/redoc](https://api.pgatlas.xyz/redoc)
and [api.pgatlas.xyz/docs](https://api.pgatlas.xyz/docs). The following describes the key endpoints
as of v0.6.0.

### Health and Metadata

**`GET /health`**

Returns the current readiness status, application version, and component health:

- `status` — `"live"` or `"ready"`
- `version` — Application version string
- `components` — Database connectivity, artifact store type, schema version

**`GET /metadata`**

Ecosystem-wide summary statistics computed on-the-fly:

```json
{
  "total_projects": 641,
  "active_projects": 407,
  "total_repos": 2721,
  "active_repos_90d": 487,
  "total_external_repos": 9675,
  "total_dependency_edges": 26096,
  "total_contributor_edges": 35407,
  "active_contributors_30d": 430,
  "active_contributors_90d": 1231,
  "last_updated": "2026-05-06T07:03:10Z"
}
```

### Projects

**`GET /projects`**

Paginated list of SCF-funded projects with optional filters and sorting:

**Query parameters**:

- `project_type` — Filter by `public-good` or `scf-project`
- `activity_status` — Filter by `live`, `in-dev`, `discontinued`, or `non-responsive`
- `search` — Case-insensitive substring match on `display_name` (max 256 chars)
- `sort` — Comma-separated `field:direction` pairs (e.g., `criticality_score:desc,display_name:asc`)
- `category` — Filter by exact project category string (max 128 chars)
- `limit` — Page size (default: 50, max: 200)
- `offset` — Pagination offset (default: 0)

**Response**: Paginated response with `items`, `total`, `limit`, and `offset`. Each item includes
`canonical_id`, `display_name`, `project_type`, `activity_status`, `category`, `git_owner_url`,
`pony_factor`, `criticality_score`, `adoption_score`, and `updated_at`.

**`GET /projects/{canonical_id}`**

Full project detail including active contributor stats and validated metadata:

- Project-level metrics (`pony_factor`, `criticality_score`, `adoption_score`)
- Active contributor counts (30-day and 90-day windows)
- Normalized `metadata` object with SCF submissions, description, website, social links, funding data

**`GET /projects/{canonical_id}/repos`**

Paginated list of repositories belonging to the specified project. Supports `limit` and `offset`
query parameters. Returns 404 if the project does not exist.

**`GET /projects/{canonical_id}/contributors`**

Paginated contributors aggregated across all repos in the project:

- `search` — Filter by contributor name
- `limit`, `offset` — Pagination controls

Returns `ProjectContributorSummary` with `total_commits_in_project` aggregated across repos.

**`GET /projects/{canonical_id}/depends-on`**

Collapsed project-level dependencies (outgoing edges). Aggregates repo-level `depends_on` edges: for
each distinct target project, returns the target project summary and the number of repo-level edges.
Self-references and edges to external repos are excluded.

**`GET /projects/{canonical_id}/has-dependents`**

Collapsed project-level reverse dependencies (incoming edges). Same aggregation as `depends-on` but
in reverse: which other projects have repos that depend on repos of this project.

### Repositories

**`GET /repos`**

Paginated list of in-ecosystem repos with optional filters and sorting:

**Query parameters**:

- `project_id` — Filter to repos belonging to a specific project (integer)
- `search` — Case-insensitive substring match on `display_name`
- `sort` — Comma-separated `field:direction` pairs (e.g., `adoption_stars:desc,display_name:asc`)
- `limit` — Page size (default: 50, max: 200)
- `offset` — Pagination offset

**`GET /repos/{canonical_id}`**

Full repo detail including:

- Parent project summary (`parent_project`)
- Contributors list with commit counts
- Releases array (PURL, version, release date)
- Outgoing and incoming dependency edge counts (`outgoing_dep_counts`, `incoming_dep_counts`)
- Active contributor counts (30-day and 90-day windows)

**`GET /repos/{canonical_id}/contributors`**

Paginated contributors for one repo with commit counts and date spans:

- `search` — Filter by contributor name
- `limit`, `offset` — Pagination controls

Returns `RepoContributorSummary` with `number_of_commits`, `first_commit_date`, `last_commit_date`.

**`GET /repos/{canonical_id}/depends-on`**

Direct dependencies (outgoing edges) for the repo. Each entry includes:

- `canonical_id`, `display_name`, `vertex_type` (`repo` or `external-repo`)
- `version_range`, `confidence` (`verified-sbom` or `inferred-shadow`)

**`GET /repos/{canonical_id}/has-dependents`**

Direct dependents (incoming edges) for the repo. Same structure as `depends-on` but in reverse
direction.

### Contributors

**`GET /contributors`**

Paginated contributor list with optional name filtering:

- `search` — Case-insensitive substring match on contributor name
- `limit`, `offset` — Pagination controls

Returns `ContributorSummary` with `id`, `name`, `email_hash`.

**`GET /contributors/{contributor_id}`**

Full contributor detail with aggregated statistics and per-repo commit activity:

- `total_repos`, `total_commits` — Aggregated counts
- `first_contribution`, `last_contribution` — Earliest and latest commit dates
- `repos` — Array of `ContributionEntry` with repo details, commit counts, and date ranges

### Audit Logs

**`GET /ingest/sbom`**

List SBOM submission records with optional filtering:

- `repository` — Filter by `repository_claim` (exact match)
- `limit`, `offset` — Pagination controls

Returns paginated `SbomSubmissionResponse` with submission status, content hash, artifact path, and
timestamps.

**`GET /ingest/sbom/{submission_id}`**

Single SBOM submission detail including raw artifact content (if available). The `raw_artifact` field
contains the full JSON text or `null` if missing from store.

**`GET /gitlog`**

List gitlog processing attempts with optional repo filter:

- `repo` — Filter by repo `canonical_id` (exact match)
- `limit`, `offset` — Pagination controls

Returns paginated `GitLogArtifactSummary` with processing status, artifact path, and timestamps.

**`GET /gitlog/{artifact_id}`**

Single gitlog processing attempt detail including raw artifact content (if available).

## Client Libraries and Integration

**TypeScript SDK**: Auto-generated from the OpenAPI specification at
[pg-atlas-ts-sdk](https://github.com/SCF-Public-Goods-Maintenance/pg-atlas-ts-sdk). The SDK provides
type-safe access to all endpoints with automatic request/response validation.

**Other languages**: The OpenAPI spec at `/openapi.json` can be used with code generators for Rust,
Go, Python, and other languages (e.g. with [openapi-generator](https://openapi-generator.tech/)).

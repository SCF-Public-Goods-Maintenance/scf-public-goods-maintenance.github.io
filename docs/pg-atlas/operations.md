---
title: Operations & Deployment
parent: PG Atlas Architecture
nav_order: 7
---

# Operations & Deployment

## Current Infrastructure

PG Atlas operates on a managed infrastructure stack optimized for simplicity, reliability, and
minimal maintenance overhead:

**Core services**:

- **DigitalOcean App Platform** — Auto-deploys FastAPI backend and the frontend static build from
  GitHub pushes to `main`, handles scaling and health checks
- **DigitalOcean Managed PostgreSQL** — Database with automated snapshots and point-in-time recovery
- **GitHub Actions** — Runs scheduled workflows for periodic tasks (bootstrap, SBOM queue, git log
  processing)
- **Filebase S3** — IPFS-backed artifact storage for SBOM and git log artifacts

**Cost profile**: Infrastructure spend around $100/month total, with most compute provided free
through GitHub Actions for open-source repositories.

## Deployment Patterns

### Backend (FastAPI)

The FastAPI backend runs on DigitalOcean App Platform with push-to-deploy automation:

- Infrastructure defined in version-controlled
  [`app.yaml`](https://github.com/SCF-Public-Goods-Maintenance/pg-atlas-backend/blob/main/app.yaml)
  App Spec
- Auto-deploys from GitHub pushes to `main` branch
- Readiness and liveness checks on `/health` endpoint with automatic restart on failures
- Horizontal scaling possible but not needed yet

**Database**:

DigitalOcean Managed PostgreSQL provides operational resilience without manual backup management:

- **Automated snapshots** — Daily backups with continuous write-ahead log archival
- **Point-in-time recovery (PITR)** — Restore to any timestamp within retention window
- **Connection pooling** — Managed at the application level, separately for FastAPI and Procrastinate

This eliminates the need for scheduled `pg_dump` backups while providing superior recovery options.

### Frontend (React Dashboard)

The React-based dashboard is hosted on DigitalOcean with automatic deployments:

- Auto-deploys from GitHub pushes to the frontend repository
- Static site generation with React consuming the REST API
- Zero-downtime deployments with automatic rollback on build failures
- CDN distribution for global low-latency access

See [Dashboard](dashboard.md) for detailed UI architecture and features.

## Background Task Processing

All periodic and queued processing runs through GitHub Actions workflows, providing free compute,
built-in audit trails, and transparent execution history. See [Ingestion](ingestion.md) for the
purpose and steps executed by these workflows.

The system uses [Procrastinate](https://procrastinate.readthedocs.io/) for asynchronous task
processing:

**Architecture**:

- PostgreSQL-backed task queue (no separate broker service required)
- Workers run in GitHub Actions workflows, not as long-running services
- `PsycopgConnector` (psycopg3) for Procrastinate; FastAPI continues using `asyncpg` via SQLAlchemy
- Both drivers access the same DigitalOcean PostgreSQL instance

**Worker execution**:

- GitHub Actions workers invoke `run_worker_async(wait=False, concurrency=N)` per queue
- Workers exit once queues are drained (required for Actions to complete rather than hang)
- Queues are processed sequentially to ensure data consistency
- Repo-scoped queueing locks prevent concurrent processing of the same repository

**Schema management**:

Procrastinate tables (`procrastinate_jobs`, `procrastinate_events`, etc.) are provisioned via Alembic
migration using the "multiple bases" pattern. The entrypoint script applies migrations automatically
on every deploy.

**Benefits**: Zero infrastructure cost for workers, elevated GitHub API rate limits, full audit trail
in GitHub Actions UI, maximum 6-hour runtime per job (sufficient for current scale).

## Observability

### Logging and Monitoring

Current observability is provided through:

- **Workflow logs** — GitHub Actions provides detailed execution logs for all scheduled workflows
- **Job summaries** — Bootstrap workflow generates statistics on graph updates and metric computation
  performance
- **Semi-structured logs** — FastAPI outputs logs to stdout, captured by DigitalOcean logging
- **Health endpoint** — `/health` endpoint monitored by App Platform for automatic restarts

This combination provides sufficient transparency for current operations. Logs and summaries are
publicly accessible through the
[workflow runs page](https://github.com/SCF-Public-Goods-Maintenance/pg-atlas-backend/actions),
aligning with community transparency goals.

### Future Enhancements

Near-term operational improvements under consideration:

- **Fully structured logs** — Currently we generate and subsequently parse our own logs; this can be
  streamlined by moving to [structlog](https://www.structlog.org/en/stable/index.html)
- **Sentry integration** — Automatic error grouping, performance tracing, and release tracking
- **Enhanced alerting** — Discord webhooks for workflow failures, API endpoint health checks
- **Metrics dashboard** — Prometheus exporter for request rates, response times, queue depths

These enhancements build on the current foundation without disrupting existing operations. Priorities
will be determined based on observed reliability patterns and community feedback.

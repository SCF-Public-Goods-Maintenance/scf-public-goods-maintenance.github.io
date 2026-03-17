---
title: Operations & Deployment
parent: PG Atlas Architecture
nav_order: 7
---

# Operations & Deployment

## Requirements

PG Atlas operations must balance simplicity, reliability, and low ongoing maintenance for a
community-driven project:

- **Push-to-deploy simplicity**: Git push to main should trigger builds/deploys without manual
  intervention.
- **Minimal DevOps overhead**: Prefer managed services over raw VMs; avoid complex orchestration
  (Kubernetes) for v0.
- **Single-machine capable**: Backend fits on one modest instance.
- **Reliable periodic jobs**: Shadow crawls, metric recomputes, adoption signal pulls, activity flag
  batch updates — scheduled (various frequencies) with logging and alerts.
- **Cost control**: Target <$100/month total; free tiers where possible.
- **GitHub-centric where feasible**: Repo already unavoidable for code/SBOM ingestion — leverage
  Actions for jobs.
- **Resilience & monitoring**: Basic health checks, logs, uptime; easy rollback.
- **Community accessibility**: Public endpoints, no heavy vendor lock-in.
- **Frontend hosting**: Static-friendly, fast CDN; at least one Stellar-native or decentralized
  option.

Security: HTTPS enforced, rate limiting, no public writes.

## Deployment

### DigitalOcean App Platform

**Description**:

- Hosted PostgreSQL with backups and horizontal scaling options.
- FastAPI container: managed PaaS, auto-deploys from GitHub push to `main`.
- Heavier tasks can be offloaded to worker containers.
- Dashboard: Static build on App Platform static site or separate.

**Pros**:

- App Platform excels at push-to-deploy with scaling and health checks.
- Infrastructure is provisioned through a version controlled `app.yml` App Spec.
- Unified billing and dashboard.
- Good logging (through add-ons) and monitoring.

**Cons**:

- Worker containers can be wasteful.

### Research: Stellar-Native Frontend (xlm.sh)

The elevator pitch:

> Unlike traditional websites hosted by trusted third parties, dWebsites are distributed across
> independently operated nodes, enhancing security, privacy, and resistance to censorship.

**Components**:

- [Soroban Domains](https://www.sorobandomains.org/) — already used for Tansu.
- [IPFS](https://ipfs.tech/) — content-addressed, distributed storage for hosting immutable static
  assets with widespread peer-to-peer distribution.
- [IPNS](https://docs.ipfs.tech/concepts/ipns/) — mutable naming layer for IPFS that provides stable,
  updatable pointers to the latest frontend release or changing content.
- [xlm.sh](https://xlm.sh/) — uses a wildcard DNS record to bridge Soroban Domains and IPFS/IPNS.

**Risks**:

- xlm.sh limitations unknown.
- Potential latency vs. traditional CDNs.
- Split hosting increases complexity slightly.

## Auxiliary Services

Auxiliary services support reliable background processing, error monitoring, and operational
visibility. For v0, we prioritize managed or lightweight options to minimize DevOps burden while
ensuring periodic jobs (shadow crawls, metric recomputes, adoption pulls) and error handling work
seamlessly.

### Task Queue & Workers

**Purpose**: Offload long-running tasks (SBOM processing, shadow crawls, full metric recomputes,
activity status batch updates) from the FastAPI request cycle.

**Components**:

- [Procrastinate](https://procrastinate.readthedocs.io/) as task queue/worker framework, using
  PostgreSQL as both broker and result backend (no separate service needed — reuses the existing
  hosted DB).
- `PsycopgConnector` (psycopg3) for the Procrastinate connection; the FastAPI app continues to use
  `asyncpg` via SQLAlchemy — both drivers access the same PostgreSQL instance.

**Deployment**:

- **Workers run in GitHub Actions** (weekly `schedule` + manual `workflow_dispatch`). This provides
  free compute for public repos, built-in run history/logs, and elevated GitHub API rate limits.
- The worker invokes `run_worker_async(wait=False, concurrency=N)` per queue so that it exits once
  the queue is drained — required for GitHub Actions to complete rather than hang.
- Queues are processed sequentially: `opengrants` first (ensures `Repo` vertices exist), then
  `package-deps`.
- Procrastinate's schema tables (`procrastinate_jobs`, etc.) are provisioned via an Alembic migration
  using the "multiple bases" pattern; `entrypoint.sh` applies it automatically on every deploy.

**Pros**: Zero additional infrastructure cost, unified PostgreSQL dependency, reliable scheduling
with full audit trail in GitHub Actions UI.

**Cons**: Maximum 6-hour runtime per Actions job; not suitable for very long-running crawls without
sharding.

### Error Monitoring & Performance Tracing

**Purpose**: Capture exceptions, performance bottlenecks (slow API endpoints, long recomputes), and
breadcrumbs for debugging.

**Options**:

- **Sentry.io SaaS** (open-source plan free for public projects): DSN integration in FastAPI,
  automatic error grouping, releases tracking.
- **Self-hosted Sentry**: Possible on Droplet but high overhead (multi-container: Postgres, Redis,
  workers) — not recommended for v0.

**Recommendation**: Start with Sentry.io free tier — zero setup beyond SDK, aligns with community
transparency.

### Additional Services

**Caching**:

- Client-side through headers.
- Cloudflare CDN/proxy for most API responses.
- For exports: Git Large File Storage (could get costly on GitHub)?

**Logging**:

- Structured JSON logs to stdout; provider capture (DigitalOcean has Betterstack or Papertrail
  add-ons).

**Monitoring & Alerts**:

- Betterstack, UptimeRobot, or Healthchecks.io for `/health` endpoint pings.
- Provider built-in metrics (DigitalOcean monitoring) or lightweight Prometheus exporter.

**Backups**:

- Database dumps (Postgres pg_dump) managed or repo artifacts.
- Automated via DigitalOcean or GitHub Actions.

<!-- FUTURE SELF: Integrate Sentry performance tracing once API endpoints stabilized. -->

## Open Questions

- Static build feasibility for interactive dashboard (client-side graph rendering size/limits)?
- Any advantages to have billing in USDC through e.g. Rozo.ai or
  [Flashback](https://www.flashback.tech/)?
- Acceptable cost threshold for managed auxiliaries?
- Alert channels (Discord webhook, email)?

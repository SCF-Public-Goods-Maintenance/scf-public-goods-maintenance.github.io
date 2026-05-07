---
title: Security & Privacy
parent: PG Atlas Architecture
nav_order: 8
---

# Security & Privacy

## Overview

PG Atlas operates with a public-first security model: all data (dependency graphs, metrics,
contributor statistics) is publicly accessible by design. Security measures focus on protecting
system integrity, preventing abuse, and maintaining contributor privacy where applicable.

**Current status**: Operational with GitHub OIDC authentication for write endpoints, IP-based rate
limiting for all endpoints, and privacy-preserving contributor data handling.

**Core principles**:

- **Public data by design** — All ecosystem metrics and dependency graphs are publicly readable
- **Write authentication** — SBOM ingestion authenticated via GitHub OIDC tokens
- **Contributor privacy** — Git log email addresses are SHA-256 hashed before storage
- **Rate limiting** — Per-IP throttling prevents API abuse
- **Input validation** — SPDX 2.3 schema validation prevents malformed submissions
- **Auditability** — All SBOM submissions logged with provenance metadata, and git log extracts are
  logged before we parse them

## Authentication & Authorization

### Read Access

All read endpoints (`/contributors`, `/metadata`,`/projects`, `/repos`) are public and require no
authentication. This aligns with the transparency goals of the SCF Public Goods Maintenance Working
Group.

### Write Access (SBOM Ingestion)

SBOM submissions to `/ingest/sbom` are authenticated using GitHub OpenID Connect (OIDC) tokens:

**Authentication flow**:

1. The [pg-atlas-sbom-action](https://github.com/SCF-Public-Goods-Maintenance/pg-atlas-sbom-action)
   requests a short-lived OIDC token from GitHub Actions
2. The token is signed with GitHub's private key (RS256) and includes claims: `repository` and
   `actor` (GitHub username)
3. PG Atlas validates the token using GitHub's public JWKS (JSON Web Key Set)
4. Token validation checks:
   - Signature matches GitHub's public key
   - Issuer is `https://token.actions.githubusercontent.com`
   - Audience matches the configured API URL (prevents token reuse)
   - Token has not expired

**Error responses**:

- `401 Unauthorized` — Missing or malformed `Authorization` header
- `403 Forbidden` — Invalid signature, expired token, or audience mismatch
- `422 Unprocessable Content` — Malformed SPDX payload

## Rate Limiting

The API implements in-memory request throttling via `ApiRateLimitMiddleware` using PyrateLimiter at
the ASGI level:

| Endpoint Category | Limit        | Window          |
| ----------------- | ------------ | --------------- |
| General endpoints | 100 requests | 1 minute per IP |
| `/health`         | 600 requests | 1 minute per IP |
| `/ingest/sbom`    | 600 requests | 1 minute per IP |

**Implementation details**:

- Requests bucketed by client IP address (resolved via `X-Forwarded-For` header)
- Exceeded limits return `429 Too Many Requests` with `Retry-After` header

## Input Validation & Integrity

### SBOM Validation

All SBOM submissions undergo strict validation:

1. **Format validation** — Must be valid SPDX 2.3 JSON
2. **Schema validation** — Structure verified against SPDX specification
3. **Denial of Service protection** — Content hash checked against previously processed submissions
4. **Provenance tracking** — Repository and actor claims from OIDC token stored in audit records

**Failure handling**:

- Invalid SBOMs return `422 Unprocessable Content` with detailed error messages
- Failed submissions create audit records with `status='failed'` and `error_detail` for triage

### SQL Injection Protection

SQLAlchemy's parameterized queries provide automatic protection against SQL injection. All database
interactions use SQLAlchemy ORM or Core expressions with bound parameters.

## Privacy Measures

### Contributor Data

Git log parsing extracts contributor statistics while preserving privacy:

- **Email hashing** — Contributor email addresses are normalized and SHA-256 hashed before storage
- **Aggregated statistics** — Only commit counts and date ranges are included in contributor details
- **Bot filtering** — Automated accounts (e.g., `[bot]` suffix, CI/CD patterns) are filtered out
  during ingestion

### User Tracking

The dashboard and API implement privacy-first analytics:

- **No cookies** — Dashboard does not set tracking cookies
- **No session storage** — API is stateless; no user sessions tracked
- **Local preferences only** — Theme/display preferences stored in browser local storage (never
  synced to server)
- **No PII collection** — No user registration, accounts, or personal data collected

## Artifact Storage & Auditability

PG Atlas implements a content-addressed artifact storage strategy for durable audit trails. Raw
submitted SBOMs and git log extracts are persisted to immutable storage with database audit records
serving as the queryable index.

**Storage architecture**:

- **Filebase S3** — IPFS-backed object storage in production providing cryptographic content
  integrity
- **Content Identifier (CID)** — Filebase returns an IPFS CID which becomes the durable reference
  stored in the database
- **SHA-256 content hash** — Computed for all artifacts enabling idempotent processing and
  deduplication

**Audit record pattern**:

Every artifact submission creates a corresponding database row with:

- **Provenance metadata** — OIDC claims (repository, actor) or other source identifiers
- **Content hash** — SHA-256 digest of raw payload bytes
- **Artifact path** — CID or storage location for retrieval
- **Processing status** — `pending`, `processed`, or `failed`
- **Error details** — Failure messages for triage when applicable
- **Timestamps** — Submission time and processing completion time

**Benefits**:

1. **Auditability** — Complete provenance trail for every submission with immutable artifacts
2. **Failure recovery** — Failed submissions retain raw artifacts for manual triage and reprocessing
3. **Idempotency** — Content-addressed storage ensures identical payloads are stored once, enabling
   safe retry semantics
4. **Decoupled lifecycle** — Artifacts are independently retrievable via IPFS gateway, decoupling
   audit retention from database schema evolution
5. **Queryable history** — Database index allows filtering by source, status, and timestamp without
   artifact retrieval

This pattern applies uniformly to SBOM submissions and git log artifacts, with schema details
documented in [Storage](storage.md).

## Future Enhancements

Near-term security improvements under consideration:

- **Sentry integration** — Automatic error grouping and security event tracking (free tier for OSS)
- **Enhanced alerting** — Discord webhooks for failed authentication attempts and rate limit breaches
- **SBOM signature verification** — Cryptographic signing of SBOM submissions beyond OIDC tokens
- **API key authentication** — Optional API keys that provide elevated rate limits to power users

These enhancements will build on the current foundation while maintaining the public-first security
model.

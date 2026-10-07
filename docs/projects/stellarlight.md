---
title: "Stellarlight"
canonical_id: daoip-5:scf:project:stellar_light
parent: Public Good Projects
proposal_issue: 74
proposer: theboycoder
category: "Ecosystem Visibility"
budget: "$40,000"
health_endpoint: "https://stellarlight.xyz/api/status"
---

# Stellarlight

<!-- markdownlint-disable MD036 -->

_stellar light is the ecosystem data layer for stellar — a single, machine-readable source of truth
for projects, code, funding, stablecoins, dev activity, partners, and builders, queryable by humans,
tools, and ai agents._

<!-- markdownlint-enable MD036 -->

|                         |                                                  |
| ----------------------- | ------------------------------------------------ |
| **Category**            | Ecosystem Visibility                             |
| **Website**             | <https://stellarlight.xyz>                       |
| **Repository**          | <https://github.com/Stellar-Light/stellarlight>  |
| **MCP server**          | <https://github.com/Stellar-Light/scout-mcp>     |
| **Agent skill**         | <https://github.com/Stellar-Light/stellar-scout> |
| **First Released**      | Jan 2026                                         |
| **Intake**              | renewal (2026q4)                                 |
| **Budget Requested**    | $40,000                                          |
| **Maintenance Reserve** | $20,000                                          |
| **Other**               | $20,000                                          |

**Repository note:** the main repository, the MCP server and the agent skill are all public under the
Stellar-Light organization, and the packages are live on npm: `@stellar-light/scout-mcp` and
`@stellar-light/api-client`.

## Project Description

<!-- markdownlint-disable MD034 -->

stellar light is the ecosystem discovery and data layer for stellar. it brings together project data,
stablecoin analytics, dev activity, github repo intelligence, the partner/anchor directory, funding
and rfp data, and ecosystem research into one platform — and, as of this quarter, exposes all of it
through a public api, an openapi spec, an mcp server, and a natural-language interface so ai agents
and developer tools can consume it directly, not just humans through a ui.

before stellar light, project information was scattered, stablecoin data required checking multiple
sources, code/repo activity had no single index, and there was no structured, authoritative data
source that an ai agent could query about the stellar ecosystem. stellar light closes those gaps.
builders find tools, code, and funded opportunities in minutes. institutions use it as a
due-diligence layer. scf reviewers track project health between rounds. and the ecosystem's emerging
ai layer now has a fresh, structured source of truth to build on.

<!-- markdownlint-enable MD034 -->

## Team & Experience

<!-- markdownlint-disable MD034 -->

Stellarlight is run by me (boxy00). i've been in the stellar ecosystem for the past 6 years,
contributing to its growth via SCF, hackathons, VC programs, events, SDF programs and more.

<!-- markdownlint-enable MD034 -->

## Retroactive Impact

<!-- markdownlint-disable MD034 -->

last quarter stellar light became a data layer agents could query. this quarter it became one they
depend on, and it started catching and fixing its own mistakes.

**raven runs on it.** raven, the ecosystem agent SDF is building, uses stellar light as its stellar
data layer and grades us in the open: 16 findings filed against our data or contract this quarter, 12
closed at the root. api usage went from 46 thousand calls in mid-july to 464 thousand by september
29, with 110 thousand in the last seven days (stellarlight.xyz/analytics). raven's team ran about
39,000 requests against us in two days of evaluations, reported three production problems (stalls,
error bodies, vector fallbacks), and all three were fixed and measured within a day: 600 requests per
minute sustained with p99 1.7 seconds and no errors. raven now runs on a metered partner key (1,200
per minute, 200,000 per day), the headers and warnings its team asked for (match mode, server timing,
retry-after, fallback reasons) ship on every answer, and the skill raven pins is checked daily
against ours.

**the code-truth layer exists.** 13,437 stellar and soroban repos are indexed and scored (about 2,300
in june), each carrying facts read from its code and pinned to a commit: interfaces, dependencies,
capabilities, toolchain, ci and tests, live mainnet usage, and a trust composite. contracts are
first-class entities (`/api/contracts`, 122 mainnet contracts with events and verification), claims
get verdicts with evidence (`/api/verify`), 899 repos carry a written knowledge note, and the CAP
registry is cross-walked into the research corpus so "which CAP added this" has a sourced answer.

**quality is measured, and it moved.** the answer-quality score on the standing question matrix went
from 59% in july to 100% from september 6 onward. the whole system is on one public dashboard,
stellarlight.xyz/quality: the score series, every guard's last verdict, the open findings with their
evidence, the lane scoreboard, and the phase plan. behind it: an improvement ledger that turns every
detector into one tracked backlog, a daily truth battery, golden evaluations after every deploy,
contract invariants in ci, 52 scheduled workflows with idempotence gates on every writer, and two
agent lanes that pick a ledger row and open a pull request on their own. 1,401 pull requests merged
this quarter (numbers 221 through 1745), and the repository went public in july.

**new registries the ecosystem did not have.** a verified real-world-asset registry (113 rows, 97
rwa.xyz tokens, 52 issuers, each re-verified on chain, from the issuer's own stellar.toml outward
where one exists, with the verification level served per row and refreshed every six hours); the
stablecoin service rebuilt on our own pipeline and domain (41 assets, six-hourly, the full price
history carried over), with pyth price feeds under evaluation for a product test with sdf; a
structured security-audit registry (64 reports); and hackathon prior-art search across every
dorahacks build.

**built for scf and sdf.** the i³ awards voting system: pilots sign an authorization with their
wallet, an anonymous relay writes the ballot on chain, ballot status follows the wallet across
devices, the pilot roster can be read straight from the scf voting contract, and the round manifest
and the published results get anchored on tansu (rehearsed end to end on a mock round). 34 nominees
and 76 pilots are loaded; the nominations round opens to pilots on sdf's go. the rfp section carries
the q3 briefs and scf round 46 as an open row, the 10 scf skills live in the marketplace, and builder
profiles show hackathon submissions.

**the partner layer.** the directory, the concierge and matching on stellar.toml fields are live and
in use (43 published partners, 21 anchors, 12 with toml-verified assets, seps and ramp types); this
is how builders and raven find partners today. the portal came out of beta on 2026-10-01 and the
first quarterly check-in reached 11 partners the same day; no partner has edited its own profile yet,
which is the q4 work, and the details are in the q3 section below.

<!-- markdownlint-enable MD034 -->

## Past Deliverables

<!-- markdownlint-disable MD034 -->

### 2026 Q3

#### Q3 D1: code + current-state intelligence layer (the raven dependency)

committed: a code-truth layer that scores live soroban/stellar repo code, matches it against docs and
CAP/protocol history, and answers code-level, current-state questions with sourced references,
exposed through the existing api/openapi/mcp/skill surfaces. measurable: code-truth endpoint live and
documented in the openapi spec, answering a defined question set with sourced references.

delivered:

- **repo code facts, pinned to commits.** every scanned repo serves `codeVerified.scannedRef` (facts
  tied to the commit they were read from, https://github.com/Stellar-Light/stellarlight/pull/830),
  `contractInterface` (exported functions, https://github.com/Stellar-Light/stellarlight/pull/796),
  `stellarDeps`, `sdkCapabilities` including x402 and mpp
  (https://github.com/Stellar-Light/stellarlight/pull/808,
  https://github.com/Stellar-Light/stellarlight/pull/817), a toolchain dimension with ci and tests
  presence (https://github.com/Stellar-Light/stellarlight/pull/864), `codeInUse` (live mainnet usage
  of the repo's contracts, https://github.com/Stellar-Light/stellarlight/pull/863), language-frontier
  capabilities and calibrated depth for python, go, kotlin and java
  (https://github.com/Stellar-Light/stellarlight/pull/868,
  https://github.com/Stellar-Light/stellarlight/pull/869), an audit-drift signal on project rows
  (https://github.com/Stellar-Light/stellarlight/pull/862) and usage-aware ranking
  (https://github.com/Stellar-Light/stellarlight/pull/871). the index grew from about 2,300 to 13,437
  scored repos.
- **contracts as first-class entities.** `GET /api/contracts` (operation `listContracts`,
  https://github.com/Stellar-Light/stellarlight/pull/891): 122 mainnet contracts with events,
  subinvocations, wasm verification and the project that owns them;
  https://github.com/Stellar-Light/stellarlight/pull/1279 stopped calling other people's contracts
  "verified".
- **claims get verdicts.** `GET /api/verify` (operation `verifyClaim`,
  https://github.com/Stellar-Light/stellarlight/pull/1057): a claim in ("is blend audited by
  certora", "is X live", "is X maintained", "is EURC issued by circle"), a supported / unsupported /
  unresolved verdict with evidence and confidence out.
- **the trust composite.** `GET /api/repos/trust`
  (https://github.com/Stellar-Light/stellarlight/pull/901) folds scan depth, usage, audit state and
  activity into one score a consumer can read.
- **knowledge notes.** the note pool went from 419 to 899 noted repos and closed to zero unnoted
  (served as `knowledgeNotes` on repo rows), with audit-drift and live-usage facts inside the notes
  (https://github.com/Stellar-Light/stellarlight/pull/865, the 2026-09-14 waves).
- **protocol history.** CAP crosswalk facts and a committed cap registry in the research corpus
  (https://github.com/Stellar-Light/stellarlight/pull/764), plus stored truth for every cap document
  row (https://github.com/Stellar-Light/stellarlight/pull/793), so "which CAP added this host
  function" resolves to a sourced document. `/api/repos/explain` answers from our own scan when
  deepwiki has no page (https://github.com/Stellar-Light/stellarlight/pull/697).
- **the defined question set.** `scripts/eval/code-truth-probes.ts` freezes what the serve paths must
  answer about scanned code (interfaces, domains, dependencies, usage, depth, contracts, the vet-idea
  and scf-pitch composites) and exits 1 on any miss; since 2026-09-30 it runs on the daily eval lane
  (https://github.com/Stellar-Light/stellarlight/pull/1743, 10 of 10 passing). a code-question
  battery is wired into the routing and consumer evaluations
  (https://github.com/Stellar-Light/stellarlight/pull/696) and mirrors raven's soroban battery topics
  (https://github.com/Stellar-Light/stellarlight/pull/844). the content-freshness guard fails ci when
  a published stellar cli command goes stale
  (https://github.com/Stellar-Light/stellarlight/pull/351).
- **for raven, the contract it routes on.** the openapi spec went from 1.2 at the start of july to
  1.9.54 (38 operations, 244 changelog entries), every discovery operation carrying the routing
  guidance raven's catalog indexes; a scorer replica of raven's own routing math
  (`scripts/eval/raven-scorer-replica.ts`) and a routing eval that asks raven real builder questions
  and checks it lands on the right operation (https://github.com/Stellar-Light/stellarlight/pull/689,
  https://github.com/Stellar-Light/stellarlight/pull/692) let us classify every routing miss from our
  side. `/api/changelog` is the consumption contract, gated so its newest entry can never name a
  field the schema lacks; the installable skill is served live and kept byte-identical with the
  mirror raven pins, checked daily (https://github.com/Stellar-Light/stellarlight/pull/708,
  https://github.com/Stellar-Light/stellarlight/pull/717). `@stellar-light/scout-mcp` had 9 releases
  and `@stellar-light/api-client` 14.
- **for raven, what it asked for in production.** a metered partner tier (1,200 requests per minute,
  200,000 per day, https://github.com/Stellar-Light/stellarlight/pull/1714) and the matching client
  release the same day; after its team's two-day load test, the three problems they reported were
  fixed within a day: stalls bounded by database and embedding timeouts and a connection-pool cap
  (https://github.com/Stellar-Light/stellarlight/pull/1721,
  https://github.com/Stellar-Light/stellarlight/pull/1728,
  https://github.com/Stellar-Light/stellarlight/pull/1729), `Retry-After` on every 503,
  `X-Scout-Match-Mode` and `Server-Timing` headers on every research response, and `meta.warnings`
  stating why a fallback happened, so an agent can tell a slow answer from a degraded one.

verify: <https://stellarlight.xyz/api/contracts?limit=5> ·
<https://stellarlight.xyz/api/verify?claim=is%20Blend%20audited%20by%20Certora> ·
<https://stellarlight.xyz/api/repos/explain?q=reflector> ·
<https://stellarlight.xyz/api/repos/search?dependsOn=soroban-sdk&limit=3> ·
<https://stellarlight.xyz/api/openapi.json> (`listContracts`, `verifyClaim`, `getRepoTrust`)

#### Q3 D2: continuous eval + improvement loop

committed: an eval harness on a regular cadence with a tracked answer-quality score that improves
over the quarter, and regressions caught before they ship (drift guard + golden evals in ci).

delivered:

- **the score moved.** the standing question matrix (engine a, 8 buckets, the mechanized successor of
  the 597-probe july audit) went 59% (2026-07-09), 82% (2026-07-11), 99% (2026-08-28), then 100% on
  every weekly run from 2026-09-06.
- **the quality dashboard.** stellarlight.xyz/quality is the public face of the loop: the score
  series above, every guard's last verdict (12 holding, 3 breached, 4 stale on 2026-09-29), the open
  findings with the evidence behind each, the consumer findings raven filed, the miss funnel, the
  lane scoreboard, and the phase plan from QUALITY.md with what shipped against each phase. the same
  data is served as json at /api/quality so an agent can read our health the way we do.
- **one backlog for every detector.** the improvement ledger
  (https://github.com/Stellar-Light/stellarlight/pull/683 to
  https://github.com/Stellar-Light/stellarlight/pull/686) normalizes every engine's findings into one
  status-tracked file, feeds raven's real questions through the gateway
  (https://github.com/Stellar-Light/stellarlight/pull/684,
  https://github.com/Stellar-Light/stellarlight/pull/687) and closes findings only through waves that
  re-check them (https://github.com/Stellar-Light/stellarlight/pull/685).
- **daily and per-deploy gates.** guard d, a daily rotating truth battery over the live api
  (https://github.com/Stellar-Light/stellarlight/pull/1047; 108 of 108 on 2026-08-29); golden
  evaluations after every production deploy (post-deploy-eval, 51 of 53 on 2026-09-26); the daily
  raven parity lane (51 pass both, 0 raven-only failures on 2026-09-29); the api-drift guard
  asserting the api, the openapi spec and the docs agree; the self-audit lane at 69 checks passing, 0
  failures on 2026-09-29.
- **invariants in ci.** QUALITY.md (https://github.com/Stellar-Light/stellarlight/pull/1058) names
  the recurring defect classes and the closure rule; three invariants run in `contract:check`: schema
  opacity (47 open maps paid down to zero, https://github.com/Stellar-Light/stellarlight/pull/1092),
  honesty-layer conformance (https://github.com/Stellar-Light/stellarlight/pull/1060) and enum
  literals; plus the contract gate (spec snapshot, generated client types, changelog coupling,
  https://github.com/Stellar-Light/stellarlight/pull/372) and the routing-surface check.
- **agent lanes.** the repair lane (https://github.com/Stellar-Light/stellarlight/pull/1559) and the
  task lane (https://github.com/Stellar-Light/stellarlight/pull/1569) pick one ledger row a day and
  open a pull request from a checkout with no production secrets; 52 scheduled workflows run (every
  file under .github/workflows with a cron), every writer with read-back and an idempotence gate.
- **third-party grading, and the loop built around it.** raven's audit filed 16 findings against
  stellar light this quarter; 12 are closed at the root (examples: count instability on wallet
  queries https://github.com/Stellar-Light/stellarlight/pull/1064, rfp fundability and stablecoin
  counts https://github.com/Stellar-Light/stellarlight/pull/955, enum drift and rwa issuer coverage
  https://github.com/Stellar-Light/stellarlight/pull/1532), 4 remain open with evidence attached. two
  guards exist only because of how raven consumes us: cross-surface consistency (the same fact must
  agree across every operation that serves it) and honest absence (an empty result must say whether
  it was checked); engine d mines raven's real questions and our api logs for the queries we miss
  (https://github.com/Stellar-Light/stellarlight/pull/452,
  https://github.com/Stellar-Light/stellarlight/pull/687); and our `meta.generatedAt`, `matchMode`
  and `counts` became judge-visible evidence in raven's own evaluation
  (https://github.com/Stellar-Light/stellarlight/pull/1062).

verify: <https://stellarlight.xyz/quality> · <https://stellarlight.xyz/api/quality> ·
<https://github.com/Stellar-Light/stellarlight/blob/main/QUALITY.md> ·
<https://github.com/Stellar-Light/stellarlight/actions/workflows/post-deploy-eval.yml> ·
<https://github.com/Stellar-Light/stellarlight/actions/workflows/raven-eval-parity.yml>

#### Q3 D3: partner portal to general availability

committed: portal out of beta, partners live with maintained profiles, concierge matching on
structured fields, and freshness check-ins sending.

delivered:

- **out of beta.** the beta label came off the directory, the concierge and the portal on 2026-10-01
  (https://github.com/Stellar-Light/stellarlight/pull/1749). what builders and raven use today: 43
  published partners (21 anchors, 5 wallets, 5 audit firms, 4 protocols, 3 infrastructure, 3 asset
  issuers, 2 tooling), each profile maintained from the partner's own stellar.toml with provenance
  (`tomlSourceUrl`, `tomlFetchedAt`, https://github.com/Stellar-Light/stellarlight/pull/831) and aged
  daily by the freshness lane (fresh, aging, stale, archived) so a stale listing is visibly stale and
  drops out of ai matching; 12 of the 21 anchors carry toml-verified fields, the other 9 publish no
  stellar.toml at all (each domain checked 2026-09-30). raven exposes the directory through
  `get_partners`.
- **concierge matching on structured fields.** the deterministic matchmaker and the concierge rank on
  assets, SEP-6/24/31, ramp types and country; official anchors missing from the directory were
  seeded from anchors.stellar.org (https://github.com/Stellar-Light/stellarlight/pull/246).
- **claim + ownership verification.** a claim is verified by construction: the claimant's mailbox has
  to sit on the listing's own domain (shared hosts excluded), and a verified claim sets the account
  email without an admin in the loop (https://github.com/Stellar-Light/stellarlight/pull/1742,
  2026-09-30). the sign-in link is the path a partner uses to change anything.
- **freshness check-ins sending.** the first quarterly check-in went out on 2026-10-01 to the 11
  published partners with a contact address on file, 10 of them in the default directory listing and
  one below its quality bar (https://github.com/Stellar-Light/stellarlight/pull/1749,
  https://github.com/Stellar-Light/stellarlight/pull/1750; 11 delivered, 0 failed): "still active and
  taking work? review your listing and update what changed", signed in with the address we mailed.
  the digest runs every monday and bundles the check-in with builder-lead alerts so a partner is
  never mailed twice; a partner with no address or a failed send is reported, not counted, and comes
  back the next week.
- **the product passes.** portal v2 with login and ai-guided maintenance
  (https://github.com/Stellar-Light/stellarlight/pull/240), the public concierge chat and weekly lead
  digest (https://github.com/Stellar-Light/stellarlight/pull/241), a real listing pipeline with claim
  requests (https://github.com/Stellar-Light/stellarlight/pull/244), directory v5
  (https://github.com/Stellar-Light/stellarlight/pull/326), personalized related partners
  (https://github.com/Stellar-Light/stellarlight/pull/345), partner logos fixed
  (https://github.com/Stellar-Light/stellarlight/pull/330); contract work in august and september:
  `getPartner` declares its full 31-field profile
  (https://github.com/Stellar-Light/stellarlight/pull/1045), the asset-issuer type
  (https://github.com/Stellar-Light/stellarlight/pull/1269), region as a typed enum with 400s instead
  of silent zeros (https://github.com/Stellar-Light/stellarlight/pull/1314,
  https://github.com/Stellar-Light/stellarlight/pull/1323), honest nulls for facts never checked
  (https://github.com/Stellar-Light/stellarlight/pull/992,
  https://github.com/Stellar-Light/stellarlight/pull/1360).

what i take from it: the value came from discovery, not from partners editing listings. no partner
has maintained its own profile yet; stellar.toml stays the source of truth, and q4 treats partner
onboarding as outreach on top of the check-in rather than more product.

verify: <https://stellarlight.xyz/partners> · <https://stellarlight.xyz/partners/chat> ·
<https://stellarlight.xyz/api/partners?type=anchor&limit=3> ·
<https://stellarlight.xyz/api/partners/matchmaker?q=USDC%20off-ramp%20mexico>

#### Q3 D4: data pipelines, freshness + ranking quality

committed: pipelines running with no significant downtime, new projects/stablecoins/repos reflected
within about a week, drift guard green, /api/status freshness current.

delivered:

- **stablecoins on our own pipeline.** the stablecoin measurement service was rebuilt in four phases
  (https://github.com/Stellar-Light/stellarlight/pull/957 to
  https://github.com/Stellar-Light/stellarlight/pull/960): own collections, a six-hourly writer, the
  api served from our own store, and the explorer on our domain, with the full price history (3,763
  rows, 18 assets, from november 2025) carried over. 41 assets tracked; usdt0's september launch
  landed the same week. we are evaluating pyth price feeds as a data source for a product test with
  sdf.
- **a verified rwa registry.** `GET /api/rwa`
  (https://github.com/Stellar-Light/stellarlight/pull/1298): 113 rows, 97 rwa.xyz tokens, 52 issuers,
  each verified on chain, from the issuer's stellar.toml outward where one exists, with the
  verification level served per row, and re-measured every six hours
  (https://github.com/Stellar-Light/stellarlight/pull/1309), with on-chain control flags
  (https://github.com/Stellar-Light/stellarlight/pull/1305) and a cross-vendor audit correction
  (https://github.com/Stellar-Light/stellarlight/pull/1302).
- **audits, hackathons, builders, dev activity.** the audit registry serves 64 reports with
  per-auditor findings extraction (https://github.com/Stellar-Light/stellarlight/pull/603);
  hackathons run on the dorahacks v1 hub api across every organizer plus curated events
  (https://github.com/Stellar-Light/stellarlight/pull/757,
  https://github.com/Stellar-Light/stellarlight/pull/914), with prior-art search over every build
  (https://github.com/Stellar-Light/stellarlight/pull/693); 233 builder profiles (2026-10-01) show
  hackathon submissions with placement (https://github.com/Stellar-Light/stellarlight/pull/931);
  electric capital snapshots refresh weekly (as of 2026-09-21).
- **research corpus.** 10,893 documents across 16 sources on 2026-10-01 (seps, caps, dev docs, the
  sdf blog, lumenloop research and news, audits, incidents, the security program, releases, the ec
  developer report); the vector index gained a source filter so every source answers semantically
  (https://github.com/Stellar-Light/stellarlight/pull/1728); exact-figure retrieval guaranteed on the
  vector path (https://github.com/Stellar-Light/stellarlight/pull/715).
- **the directory stays true.** scf pages beyond the fund's 500-row listing cap recovered 112 rows
  and 147 awards (https://github.com/Stellar-Light/stellarlight/pull/1397); 108 proven-broken links
  were routed into a repair queue (https://github.com/Stellar-Light/stellarlight/pull/1413);
  duplicate records fold under a canonical with an operator veto
  (https://github.com/Stellar-Light/stellarlight/pull/1311); repositories that no longer exist are
  stamped `gone`; one field, one writer ended the enrich and curate flip-flops
  (https://github.com/Stellar-Light/stellarlight/pull/1400). new facts land within days: spectra's
  stellar launch was reported on 2026-09-26 and the row served live status, structured products, tvl
  and nine contracts on 2026-09-28 (https://github.com/Stellar-Light/stellarlight/pull/1734).
- **pipelines that report their own failures.** the on-chain lane had been hitting stellar.expert's
  rate limit at the end of every run and reporting success; it now backs off, retries and ends red if
  a row stays stale (https://github.com/Stellar-Light/stellarlight/pull/1735); the toml parser keeps
  asset-code case (https://github.com/Stellar-Light/stellarlight/pull/1736).
- **uptime under load.** the database connection cap that caused stalls was found and fixed (pool
  cap, fail-fast timeouts, an adapter crash trapped,
  https://github.com/Stellar-Light/stellarlight/pull/1721,
  https://github.com/Stellar-Light/stellarlight/pull/1728,
  https://github.com/Stellar-Light/stellarlight/pull/1729); every 503 carries retry-after; measured
  on 2026-09-29: 600 requests per minute for a minute, 600 of 600 answered, p99 1.7 seconds. 52
  scheduled workflows run; the api-drift guard is green and every /api/status source updated on
  2026-09-29.
- **the site.** /ask, the natural-language search over projects, research and partners, is public;
  /analytics shows usage in the open (all-time and 30-day calls, the last 7 days by endpoint);
  /entities and /builders give organizations and builders their own profiles with code activity and
  link provenance (https://github.com/Stellar-Light/stellarlight/pull/911,
  https://github.com/Stellar-Light/stellarlight/pull/913); the stablecoin explorer was rebuilt on our
  domain with per-asset pages, issuer drawers and a latest-updates rail
  (https://github.com/Stellar-Light/stellarlight/pull/962 to
  https://github.com/Stellar-Light/stellarlight/pull/965).
- **discovery.** duplicate titles, missing canonicals and missing structured data fixed, 24 category
  landing pages added (2026-09-15), homepage payload cut from 566 kb to 356 kb.

verify: <https://stellarlight.xyz/api/status> · <https://stellarlight.xyz/api/rwa?limit=3> ·
<https://stellarlight.xyz/api/stablecoins> · <https://stellarlight.xyz/stablecoins> ·
<https://stellarlight.xyz/api/audits?limit=3> ·
<https://stellarlight.xyz/api/hackathons/builds?q=oracle> ·
<https://github.com/Stellar-Light/stellarlight/actions/workflows/api-drift.yml>

#### Q3 D5: scf program support, rfp + hackathon maintenance, and reporting

committed: rfps live and current, ideas + hackathon trackers current, and ecosystem reports published
over the quarter.

delivered:

- **the i³ awards.** sdf asked in july for a pilots-only voting system for the i³ awards; it is
  built, rehearsed end to end on a mock round, and open on a private ballot page: a pilot signs an
  authorization with their wallet and an anonymous relay writes the ballot on chain under a random id
  (https://github.com/Stellar-Light/stellarlight/pull/1689 to
  https://github.com/Stellar-Light/stellarlight/pull/1695); a signed cross-device ballot status so a
  pilot is recognized on any device (https://github.com/Stellar-Light/stellarlight/pull/1726);
  authorship proof kept per ballot (https://github.com/Stellar-Light/stellarlight/pull/1718) and,
  since 2026-09-30, an authorization memo that commits to a server-issued nonce so a copy of a signed
  authorization reveals nothing (https://github.com/Stellar-Light/stellarlight/pull/1744); a lane
  that reads the scf voting contract's eligible-voter list as import-ready csv
  (https://github.com/Stellar-Light/stellarlight/pull/1528); the round manifest and the published
  results anchored on tansu (https://github.com/Stellar-Light/stellarlight/pull/1635 to
  https://github.com/Stellar-Light/stellarlight/pull/1639); a daily reconcile between chain and
  record (https://github.com/Stellar-Light/stellarlight/pull/1630,
  https://github.com/Stellar-Light/stellarlight/pull/1632); an admin-only tally view of who voted for
  what, with the standings the publish lane would count (2026-10-01). status on 2026-10-01: 34
  nominees across 3 categories, 76 pilots whitelisted, and a rehearsal round open to any wallet for
  sdf's own testing before the pilots get the link.
- **rfps.** q3 rollover with the layerzero dvn and x402 bazaar briefs
  (https://github.com/Stellar-Light/stellarlight/pull/751); scf round 46 is served as an open row
  with its 2026-11-08 deadline; 16 briefs (2 open, 14 closed) alongside the round row. the scf public
  goods award is structured truth on project rows
  (https://github.com/Stellar-Light/stellarlight/pull/631) and per-round awards are official records
  (https://github.com/Stellar-Light/stellarlight/pull/759,
  https://github.com/Stellar-Light/stellarlight/pull/811).
- **ideas, skills, builders.** the ideas platform and `vet-idea` are live; the 10 scf skills sit in
  the marketplace as one service offering with two reviewer skills
  (https://github.com/Stellar-Light/stellarlight/pull/672,
  https://github.com/Stellar-Light/stellarlight/pull/707); builder profiles show hackathon
  submissions with placement (https://github.com/Stellar-Light/stellarlight/pull/931); the hackathon
  tracker is current (26 events, hackmeridian listed as upcoming).
- **reports, not met.** the six thesis reports were refreshed on 2026-08-14 and the scf funding
  analysis gained round-level data (41 rounds,
  https://github.com/Stellar-Light/stellarlight/pull/576), but no new report was published this
  quarter; the blog now also syndicates ecosystem posts from sdf and tellus through the feed sync.
  the quarter's writing went into the code-truth and quality work above, and reports are the
  shortfall in this deliverable.

verify: <https://stellarlight.xyz/api/rfps> · <https://stellarlight.xyz/ideas> ·
<https://stellarlight.xyz/skills?source=stellarlight> · <https://stellarlight.xyz/hackathons> ·
<https://github.com/Stellar-Light/stellarlight/tree/main/src/lib/awards> (the i³ voting code)

### 2026 Q2

#### The public API — 24 endpoints (live at /api/openapi.json)

built a full agent-facing rest api. the endpoints:

- **projects** — `GET /api/projects/search` (keyword + semantic project discovery, with org
  attribution
  - inline code references)
- **repos** — `GET /api/repos/search` (indexed + scored github repos), `GET /api/repos/explain`
  (source-grounded answers to deep code questions, routed to the authoritative repo)
- **research** — `GET /api/research` (vector search over the knowledge corpus with confidence scores)
- **hackathons** — `GET /api/hackathons`, `GET /api/hackathons/{slug}`, `GET /api/hackathons/compare`
  (merged curated + live DoraHacks feed)
- **builders** — `GET /api/builders` (stellar passport builder profiles)
- **partners** — `GET /api/partners`, `GET /api/partners/{slug}`, `POST /api/partners/match` (ai
  matchmaking), `POST /api/partners/assistant` (concierge), `POST /api/partners/onboard`,
  `POST /api/partners/submit-listing`
- **funding** — `GET /api/rfps` (SCF rfps / sponsor briefs)
- **analytics** — `GET /api/clusters` (topic clustering + crowdedness), `GET /api/analyze`
  (cross-ecosystem rollups), `GET /api/leaderboard` (ranked active projects + Electric Capital dev
  macro)
- **skills** — `GET /api/skills`, `GET /api/skills/{name}`
- **meta** — `GET /api/status` (health + per-source freshness), `GET /api/changelog`,
  `POST /api/feedback`

every endpoint is documented in an openapi 3.1 spec with stable operationIds and per-endpoint "use
when / not for" routing guidance, permissive CORS, and a version header — so codegen tools and ai
agents get typed access with no hand-rolled wrappers.

verify: <https://stellarlight.xyz/api/openapi.json> · sample:
<https://stellarlight.xyz/api/projects/search?q=defi> · <https://stellarlight.xyz/api/status>

#### MCP server, typed client, and installable skill

`@stellar-light/scout-mcp` — an mcp server (18 tools) published to npm, so any mcp client (claude,
cursor, etc.) can query the whole data layer. `@stellar-light/api-client` — a typed typescript sdk on
npm. `stellar-scout` — an installable skill (SKILL.md + references) for coding agents. all three have
a public home at stellarlight.xyz/scout — a landing page with one-line install commands, the full
tool reference, and worked examples so a builder or agent can go from "never heard of it" to
installed in a minute. mirrored to public repos and listed in skill registries.

verify: <https://stellarlight.xyz/scout> · <https://www.npmjs.com/package/@stellar-light/scout-mcp> ·
<https://www.npmjs.com/package/@stellar-light/api-client>

#### Skills marketplace

public catalog of ai skills, mcp servers, sdks, and tools for stellar builders at
stellarlight.xyz/skills — merges SDF's official skills.stellar.org skills, stellar light's own, and
approved community submissions, each with an install command and compatibility info. includes a
community submission flow.

verify: <https://stellarlight.xyz/skills>

#### AI systems

the ai work spans the whole platform, not one feature:

- **retrieval + routing quality work** — golden-answer evaluations, chunk hygiene, and a measured,
  reproducible improvement in how well an external ai agent routes to and answers from our data.
- **ai data-cleaning pipeline** — normalizes, de-duplicates, re-categorizes, and flags stale/broken
  data across 900+ projects so the directory stays accurate at scale.
- **semantic retrieval** — vector search (voyage embeddings) over both the research corpus and the
  project directory, with a keyword→semantic fallback.
- **per-response confidence scoring** — every answer carries a relevance + freshness + authority
  score so consumers know how much to trust it.
- **ai partner concierge** — a tool-using assistant that matches builders to partners from a
  plain-english need and is hallucination-guarded (it can only surface real, indexed partners).
- **ai-guided partner maintenance** — logged-in partners update their profile by chatting; the model
  extracts structured fields from the conversation.
- **natural-language search** (`/ask`) — one question fans out across the project directory, research
  corpus, and partner data and returns grounded, cited answers; currently in private testing.

verify: <https://stellarlight.xyz/partners> (live ai concierge) ·
<https://stellarlight.xyz/api/research?q=soroban> (semantic retrieval + confidence scores) · /ask is
in private testing (not yet public)

#### Research corpus + code intelligence

vector-searchable knowledge corpus — SEPs, SCF handbook, dev docs, papers, security audits, incident
reports — with confidence scoring, plus an indexed-and-scored github repo layer (~2,300
stellar/soroban repos ranked by freshness, traction, and SCF/hackathon/builder authority) surfaced
via /api/repos/search and inline on project pages. `/api/repos/explain` routes deep code questions to
the authoritative repo and returns a source-grounded answer.

verify: <https://stellarlight.xyz/api/research?q=soroban%20authorization> ·
<https://stellarlight.xyz/api/repos/search?q=wallet>

#### Partner / anchor data layer + self-service portal

full partner layer live at stellarlight.xyz/partners: a directory of anchors, on/off-ramps,
infrastructure, tooling, and audit firms, each enriched directly from the partner's stellar.toml
(assets, SEP-6/24/31, on/off-ramp, jurisdiction) to match the official stellar anchor directory. an
ai concierge for builder→partner matching, and a self-service portal (in beta) where partners log in,
maintain their profile through an ai-guided chat, see demand signals when builders search for them,
and get quarterly freshness check-ins. a claim flow lets companies take ownership of their listing.

verify: <https://stellarlight.xyz/partners>

#### Data sources, pipelines & freshness

integrated and kept fresh via automated pipelines: SDF entity airtable (projects + grants), the
github api (dev activity, stars, commit recency, repo metadata), goldsky (stablecoin on-chain data),
defillama (defi tvl), rwa.xyz (rwa tvl), dorahacks (live hackathons), stellar passport (builder
profiles), electric capital (developer activity), and partners' own stellar.toml files. 900+
projects, ~2,300 repos, 100+ builders, and the partner directory are refreshed on scheduled jobs,
with a `/api/status` endpoint exposing per-source freshness so consumers always know how current the
data is.

verify: <https://stellarlight.xyz/api/status>

#### Data quality + integrity

golden-answer evals, retrieval chunk hygiene, org/builder attribution ("who built X"), an "inactive"
lifecycle state so defunct projects stop ranking as active, and a daily api ⇄ openapi ⇄ docs drift
guard in CI that fails if the live api, the spec, and the docs ever disagree.

verify: <https://stellarlight.xyz/api/changelog>

#### Platform, dashboards & quality-of-life

continuous improvements to the human-facing platform across the quarter:

- **hackathon tracker** — surfaces upcoming and active stellar hackathons (merged curated + live
  dorahacks feed) and tracks post-hackathon project status (built / in progress / abandoned), giving
  scf and the ecosystem visibility into which hackathon projects turn into real products.
- **developer-activity dashboard + leaderboard** — a ranked, filterable view of active projects by
  github stars / open issues / commit recency over selectable time ranges, bundled with an electric
  capital ecosystem dev macro (monthly active devs, commit trends). the ecosystem's first automated,
  transparent view of what's actually being maintained.
- **entities & organizations** — org / company pages that roll each organization's projects, funding,
  and activity into a single profile ("who's behind what"), sorted so the most complete, active orgs
  lead.
- **project pages** — github stats, tvl charts, and blog/rss feeds embedded per project; public
  transparency + change logs on project data.
- **stablecoin explorer** — historical dashboards (14d / 90d / 1y), issuer leaderboard, and
  top-issuer breakdowns across 22+ verified stellar stablecoins (supply, market cap, holders, volume,
  defi liquidity, peg stability).
- **ideas + rfp platform** — curated project ideas and the live scf rfp section feeding builders
  directly into scf programs, with difficulty ratings, category filters, and a moderation workflow.
  this quarter we're pushing out the current (q2) round of scf rfps — keeping the section populated
  with the active briefs and surfacing them to builders (also mirrored to the scf gitbook).
- **ui/ux** — a cleaner, consistent interface across the whole site, mobile-first layouts, advanced
  filters, and navigation that connects every surface (directory, ask, partners, skills, leaderboard,
  hackathons, ideas, blog).

900+ projects and entities indexed and categorized throughout.

verify: <https://stellarlight.xyz/leaderboard> · <https://stellarlight.xyz/hackathons> ·
<https://stellarlight.xyz/entities> · <https://ideas.stellarlight.xyz> ·
<https://ideas.stellarlight.xyz/rfps>

#### Content and ecosystem reporting

thesis-driven ecosystem reports published on /blog:

- **The State of Stellar — H1 2026** — <https://stellarlight.xyz/blog/state-of-stellar-h1-2026>
- **The Stellar DeFi Landscape** — <https://stellarlight.xyz/blog/the-stellar-defi-landscape>
- **SCF Funding Analysis: The Fund Is a Rudder, Not a Faucet** —
  <https://stellarlight.xyz/blog/scf-funding-analysis-directed-capital>
- **Who Is Actually Building on Stellar — H1 2026** —
  <https://stellarlight.xyz/blog/who-is-actually-building-on-stellar-h1-2026>
- **Stablecoins on Stellar — The Issuer Layer** —
  <https://stellarlight.xyz/blog/stablecoins-on-stellar-the-issuer-layer>
- **The Stellar Hackathon Pipeline** — <https://stellarlight.xyz/blog/stellar-hackathon-pipeline>

verify: <https://stellarlight.xyz/blog>

proof: everything above is live and verifiable at stellarlight.xyz, stellarlight.xyz/partners,
stellarlight.xyz/skills, stellarlight.xyz/leaderboard, the full api spec at
stellarlight.xyz/api/openapi.json, and on npm (@stellar-light/scout-mcp, @stellar-light/api-client).
launch interview: <https://x.com/lumenloop/status/2069451377223536659>.

<!-- markdownlint-enable MD034 -->

## Proposed Impact

<!-- markdownlint-disable MD034 -->

stellar light is the data layer under stellar's ai agents. sdf's raven agent queries it through a
dedicated adapter, builds its routing catalog from our openapi spec, and reviews our contract in its
own repo whenever it changes. that dependence is public and checkable there:

- the adapter raven queries us through:
  https://github.com/stellar-experimental/stellar-raven/blob/main/src/adapters/scout.ts
- our `x-routing` metadata scored as an input to raven's catalog:
  https://github.com/stellar-experimental/stellar-raven/commit/baabc06b13ef
- a drift review on stellar light, filed by raven's ci and closed:
  https://github.com/stellar-experimental/stellar-raven/issues/215
- raven's open quality ledger on stellar light:
  https://github.com/stellar-experimental/stellar-raven/tree/main/improvements/stellar-light-scout

today the layer holds 1,133 projects, 13,602 repos, 130 contracts, 50 partners and 16,908 research
documents, and its api has answered 515,278 calls. q3 made it deep and correct. q4 keeps it that way
and makes it measurably better where people actually use it: the answers raven gives, the hackathon
and builder research teams do before they build, the scf and ecosystem project records reviewers rely
on, the code and contract facts agents cite, and the rfps builders apply to.

how q4 is built: foundations, not patches. every fact is stored once, with its evidence and the date
it was read, and every surface (the api, the mcp server, raven) reads that same stored fact.
questions are answered by one engine over those facts, so a new question becomes a new facet, not a
new endpoint with its own math. "unknown" and "none" are different answers everywhere. and any
decision a model makes is scored against human labels, and carries its probability, before it is
allowed to change a record. the hackathon data in deliverable 2 is the first piece built this way (a
facts layer, a facet registry and one analysis engine, live since 2026-10-06), and the rest of q4
follows it.

none of this starts from zero. each deliverable below says what is already shipped or in review, what
is next on the roadmap, and what we commit to measure. the roadmap items are examples, not a closed
list: a data layer has to adapt to what the ecosystem asks of it, so we pick the next piece by
measured need (raven's findings, our own improvement ledger, what sdf and scf ask for). the
measurable lines are the commitment.

the maintenance reserve of
$20,000 covers the work that arrives during the quarter whether or not we
add anything: keeping the 55 data lanes and the api contract raven builds on working, bug and
security fixes, dependency updates, releases, uptime and user support. the new work in the
deliverables below (new data, new operations, models brought into the loop) makes up the other
$20,000.

<!-- markdownlint-enable MD034 -->

## Proposed Deliverables

<!-- markdownlint-disable MD034 -->

### 1. supporting raven, and better answers through it

raven keeps changing: it moved to the stellar-experimental organization this year, and its catalog of
our operations is rebuilt from our openapi spec as it evolves. q4 keeps stellar light working through
every rewrite and release, and keeps improving what raven gets from us.

already moving: every route raven reads reports its own timing
([pr 1753](https://github.com/Stellar-Light/stellarlight/pull/1753)) and a failure an agent can act
on: a 503 with a retry time, partial results said as a field, one policy for unknown parameters
([pr 1755](https://github.com/Stellar-Light/stellarlight/pull/1755),
[pr 1783](https://github.com/Stellar-Light/stellarlight/pull/1783)); research answers pull from
several sources in one call, ranked against raven's own golden cards
([pr 1787](https://github.com/Stellar-Light/stellarlight/pull/1787)); and two research changes are in
review: jev scoring passages against raven's cards
([pr 1786](https://github.com/Stellar-Light/stellarlight/pull/1786)), and stellar.org's learn and
use-case pages joining the corpus
([pr 1788](https://github.com/Stellar-Light/stellarlight/pull/1788)).

next: fix raven's 9 open findings on stellar light (for example tvl history for projects, listing
wallets by type, soroswap's contract roles, horizon's product and contract records, and a project
search that reported zero results when a read failed); get every operation we ship into raven's
catalog with routing that lands (it carries our spec 1.9.61 today while we serve 1.9.71); measure
routing changes on a replica of raven's scorer before they ship; and close every drift review raven's
ci files on us.

ecosystem value: raven is how a growing share of the ecosystem asks questions about stellar, and its
answers about projects, code and funding are only as good as this layer. baseline (2026-10-07): 9
open findings, 1 open drift review, and raven's catalog on spec 1.9.61. measurable: every drift
review filed during q4 closed; fewer than 9 findings open at quarter end; raven's catalog on our
current spec at quarter end (conditional on raven's own sync schedule; failing that, our routing
measured on the replica); truth battery and golden-set pass rates published at the start and end of
the quarter.

### 2. hackathon and builder data v2: know the landscape before you build

the second version of our hackathon and builder data, built on stellar's own sources and open to any
agent with no sign-in. it covers 1,400 submissions from 20 dorahacks events, each stored with the
team's full write-up and refreshed daily. already live
([pr 1797](https://github.com/Stellar-Light/stellarlight/pull/1797),
[pr 1800](https://github.com/Stellar-Light/stellarlight/pull/1800),
[pr 1801](https://github.com/Stellar-Light/stellarlight/pull/1801)):

- see what's been built: search every stellar hackathon submission by meaning or keyword, filtered by
  event, track, category, library and placement, winners first.
- categories with confidence: a submission gets a category only where that category's measured
  precision is at least 0.7, and every assignment carries its precision.
- built with: the stack each submission actually uses, read from its repo's manifests, so "what do
  winners build with" has counted answers.
- spot trends: any facet counted by event or year, winners against everyone else, and what shifted
  between events.
- get feedback on your own project: from a github or dorahacks link, its facts, the closest earlier
  submissions and what is missing for scf or mainnet, with sources.
- know the event: prize tiers, rules, judging criteria and submission requirements for each
  hackathon.
- see what happened after: which teams kept shipping, which became projects, and their status and scf
  funding today.

next: linking submissions to projects through team members and deployed contracts, not just repos and
websites; outcomes per event (submitted, won, became a project, scf funded, on mainnet, active after
180 days); builder profiles with every submission, placement and what shipped after; categories read
by jev from each full write-up, kept only if they beat today's method on the same human labels; scf
program answers; [stretch] tool picks from skills and partner profiles inside the hackathon brief;
and [conditional on organizers sharing them] lists from events outside dorahacks.

ecosystem value: teams start from what was already built and what happened to it, and sdf and
organizers can see which hackathons produce lasting projects. baseline (2026-10-07): 30 submissions
linked to directory projects. measurable: the analysis and review operations in raven's catalog; a
21-question hackathon benchmark asked through raven at the start and end of the quarter, with both
results published; more submissions linked to projects at quarter end than the 30 today.

### 3. scf and ecosystem project data quality

keep every project record correct: scf awards per round verified weekly against
communityfund.stellar.org, project status backed by dated evidence (mainnet contracts, recent repo
activity, a live product), broken links repaired, duplicates merged under one canonical record, and
hackathon builds linked to the projects they became.

already moving: a daily status snapshot of every project, so "still alive 180 days after launch"
becomes measurable from dated history, with the first survival reading on 2027-03-31
([pr 1780](https://github.com/Stellar-Light/stellarlight/pull/1780)); shutdown evidence that holds
up: a hijacked or lapsed domain counts, an off-origin redirect does not
([pr 1625](https://github.com/Stellar-Light/stellarlight/pull/1625),
[pr 1626](https://github.com/Stellar-Light/stellarlight/pull/1626)); verification packets that put
weak-basis live rows in front of a human; scf award records repaired at the source: awards read from
submission records, false identity matches removed, and nine awarded projects the directory was
missing now served ([pr 1598](https://github.com/Stellar-Light/stellarlight/pull/1598),
[pr 1599](https://github.com/Stellar-Light/stellarlight/pull/1599),
[pr 1608](https://github.com/Stellar-Light/stellarlight/pull/1608)); and jev, typesafe ai's
typed-decision model, with evals built for three tasks: whether a project's website shows the product
or is shut down, parked, unrelated or a placeholder; which project types fit; and whether a repo
really builds on stellar ([pr 1781](https://github.com/Stellar-Light/stellarlight/pull/1781)). every
jev answer carries a calibrated probability, and below 0.9 it reads unknown and changes nothing.

next: jev's page verdicts on the weak-basis live rows; product and on-chain evidence for launched
projects with no public code (wallets, anchors, payment apps); and the open duplicate review queue.

ecosystem value: scf reviewers, sdf and builders use these records to judge what was funded and what
shipped, and a wrong status or a missing award misleads all of them. baseline (live api, 2026-10-02):
597 scf-awarded projects, 544 marked live, 256 of those live only because their website answers, and
219 with no activity data; the pattern-based page reader catches 57% of bad sites at 73% precision on
178 human-labelled pages. measurable: the weekly award verification running all quarter; jev's page
verdicts serving only where they beat that reader on the same labels; every scf-awarded project
carrying a dated status with the evidence behind it, and fewer than 256 resting on a website check
alone; a shorter broken-link queue at quarter end than at the start.

### 4. code and contract knowledge

the facts agents cite when they answer code questions: what each stellar repo is, how deep its
stellar use goes, which contracts it deploys, and whether they are used on mainnet.

already moving: every repo in the curated pool carries a public note read from its code, since
2026-09-14 ([pr 1593](https://github.com/Stellar-Light/stellarlight/pull/1593)), and a freshness lane
flags a note when its repo moves or is archived; code depth is graded by the kind of repo it is, so a
library no longer reads as a shallow contract
([pr 1572](https://github.com/Stellar-Light/stellarlight/pull/1572)), and the eval fixtures are
pinned to the commit their labels describe; repos that no longer exist are detected and no longer
served ([pr 1594](https://github.com/Stellar-Light/stellarlight/pull/1594)); contracts are
first-class records with live mainnet usage on repo rows; and a code-truth probe set runs on the
daily eval lane ([pr 1743](https://github.com/Stellar-Light/stellarlight/pull/1743)).

next: repos whose stellar use is not yet proven, checked by their code or by jev instead of assumed;
mainnet contract evidence joined to the projects that own it; and depth calibration re-measured as
the scanner reaches more languages.

ecosystem value: the hardest questions builders and agents ask are code-level and current-state, and
the answer is only as good as the facts under it. baseline (2026-10-07): 13,602 repos and 130
contracts. measurable: the code-truth probe set passing daily, with any regression fixed or reported;
repo-note coverage and contract counts reported at the start and end of the quarter; no repo served
after it stops existing.

### 5. a quality system that finds and fixes its own problems

the engine behind "foundations, not patches": every detector writes to one improvement ledger, and a
finding closes only when a re-check shows it fixed.

already moving: a repair lane that works one open ledger row a day and delivers it as a pull request
([pr 1559](https://github.com/Stellar-Light/stellarlight/pull/1559)); a task lane (repo notes,
claims, verification packets, gap reports) that opens one pull request per weekday
([pr 1569](https://github.com/Stellar-Light/stellarlight/pull/1569)); data lanes promoted to stage 2
only after they read back every row they write, proven twice
([pr 1577](https://github.com/Stellar-Light/stellarlight/pull/1577)); a daily rotating truth battery
over the live api; and a quality board that tells a catch from a breakage.

next: more lanes promoted to stage 2 on proven read-backs, and every detector's findings flowing into
the same ledger.

ecosystem value: a data layer this size stays correct only if it finds its own errors before its
users do. baseline (2026-10-07): 5 lanes at stage 2, 12 more eligible, 62 at stage 1. measurable:
more lanes at stage 2 at quarter end than the 5 today, each on a proven read-back; the repair and
task lanes running all quarter; the quality board current.

### 6. rfps, scf programs and partners (ongoing)

keep the rfp section current with each scf rfp round. the first job is the q4 rollover (the section
still shows the q3 briefs today); after that, each new brief is added when it is published, closed
ones are marked, and the round row stays current (scf round 46 submissions close 2026-11-08). support
the scf programs that run on stellar light data: the i³ awards 2026, whose final round is open now
and whose results are published and anchored on tansu this quarter; the scf skills in the
marketplace; and past scf proposals, searchable in the research corpus
([pr 1762](https://github.com/Stellar-Light/stellarlight/pull/1762)). keep the partner directory
current: claims verified by domain
([pr 1742](https://github.com/Stellar-Light/stellarlight/pull/1742)), stellar.toml re-reads and the
quarterly check-in ([pr 1749](https://github.com/Stellar-Light/stellarlight/pull/1749)).

ecosystem value: builders find open rfps and their deadlines where they find everything else, and
raven can answer "what can i apply for" correctly. measurable: the q4 rollover live within a week of
the q4 briefs' publication; each later brief live within a week; the round row and deadlines current
all quarter; the i³ results anchored on tansu, with the anchor recomputing to the same digest; the q4
partner check-in sent.

### 7. our skills, mcp server and api client (ongoing)

keep our own skills current with the api they teach: the stellar-scout agent skill and the 15 stellar
light skills in our skills registry, updated when an operation changes so an agent never follows a
stale instruction. the skill raven pins stays byte-identical with the one we serve, checked daily
([pr 717](https://github.com/Stellar-Light/stellarlight/pull/717),
[pr 1769](https://github.com/Stellar-Light/stellarlight/pull/1769)), and every listed skill resolves
instead of answering an error ([pr 1752](https://github.com/Stellar-Light/stellarlight/pull/1752)).
keep the mcp server (`@stellar-light/scout-mcp`) and the typed api client
(`@stellar-light/api-client`) released in step with the spec.

ecosystem value: agents learn stellar light through these skills and tools, and a stale skill sends
them to the wrong call. measurable: every skill we publish resolving and matching the current spec at
quarter end; the served skill byte-identical with raven's mirror, checked daily; the mcp server and
api client released with each spec change that touches them.

### 8. data pipelines, freshness and uptime (ongoing)

keep the 55 scheduled data lanes running (sdf airtable, github, dorahacks, defillama, rwa.xyz,
stellar.expert, partners' stellar.toml and more) and repair them when a source changes under them.
keep the api, the mcp server and metered partner keys up, with dependency and security updates, a
bounded wait on the database ([pr 1756](https://github.com/Stellar-Light/stellarlight/pull/1756)),
and a clear 503 instead of an empty answer when a read fails. turn on the dependency graph and run pg
atlas's sbom action on all three repositories in the table above, so pg atlas reads their
dependencies.

ecosystem value: data is only useful while it is fresh and correct. measurable: uptime from the
health endpoint in this page's front matter, which the program polls; the pg atlas sbom action
running on all three repositories; new projects, stablecoins and repos reflected within a week; the
state of every lane reported at quarter end.

<!-- markdownlint-enable MD034 -->

## Metrics loaded from PG Atlas

[![PG Atlas](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_light&query=%24.activity_status&label=PG+Atlas&color=914CFF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_light)
[![90d Contributors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_light&query=%24.active_contributors_90d&label=90d+Contributors&color=00B578)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_light)
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_light&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_light)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_light&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_light)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.

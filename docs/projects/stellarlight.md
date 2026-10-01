---
title: "Stellarlight"
canonical_id: daoip-5:scf:project:stellar_light
parent: Public Good Projects
proposal_issue: 74
proposer: theboycoder
category: "Ecosystem Visibility"
budget: "$40,000"
---

# Stellarlight

<!-- markdownlint-disable MD036 -->

_stellar light is the ecosystem data layer for stellar — a single, machine-readable source of truth
for projects, code, funding, stablecoins, dev activity, partners, and builders, queryable by humans,
tools, and ai agents._

<!-- markdownlint-enable MD036 -->

|                      |                                                  |
| -------------------- | ------------------------------------------------ |
| **Category**         | Ecosystem Visibility                             |
| **Website**          | <https://stellarlight.xyz>                       |
| **Repository**       | <https://github.com/Stellar-Light/stellarlight>  |
| **MCP server**       | <https://github.com/Stellar-Light/scout-mcp>     |
| **Agent skill**      | <https://github.com/Stellar-Light/stellar-scout> |
| **First Released**   | Jan 2026                                         |
| **Intake**           | renewal (2026q3)                                 |
| **Budget Requested** | $40,000                                          |

**Repository note:** the codebase has migrated to the Stellar-Light organization; the MCP server and
agent-skill repos are already public, and the main repo's public flip lands this quarter
(full-history secrets audit already clean). The packages are live on npm today:
`@stellar-light/scout-mcp` and `@stellar-light/api-client`.

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
the q3 briefs and scf round #46 as an open row, the 10 scf skills live in the marketplace, and
builder profiles show hackathon submissions.

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
  tied to the commit they were read from, #830), `contractInterface` (exported functions, #796),
  `stellarDeps`, `sdkCapabilities` including x402 and mpp (#808, #817), a toolchain dimension with ci
  and tests presence (#864), `codeInUse` (live mainnet usage of the repo's contracts, #863),
  language-frontier capabilities and calibrated depth for python, go, kotlin and java (#868, #869),
  an audit-drift signal on project rows (#862) and usage-aware ranking (#871). the index grew from
  about 2,300 to 13,437 scored repos.
- **contracts as first-class entities.** `GET /api/contracts` (operation `listContracts`, #891): 122
  mainnet contracts with events, subinvocations, wasm verification and the project that owns them;
  #1279 stopped calling other people's contracts "verified".
- **claims get verdicts.** `GET /api/verify` (operation `verifyClaim`, #1057): a claim in ("is blend
  audited by certora", "is X live", "is X maintained", "is EURC issued by circle"), a supported /
  unsupported / unresolved verdict with evidence and confidence out.
- **the trust composite.** `GET /api/repos/trust` (#901) folds scan depth, usage, audit state and
  activity into one score a consumer can read.
- **knowledge notes.** the note pool went from 419 to 899 noted repos and closed to zero unnoted
  (served as `knowledgeNotes` on repo rows), with audit-drift and live-usage facts inside the notes
  (#865, the 2026-09-14 waves).
- **protocol history.** CAP crosswalk facts and a committed cap registry in the research corpus
  (#764), plus stored truth for every cap document row (#793), so "which CAP added this host
  function" resolves to a sourced document. `/api/repos/explain` answers from our own scan when
  deepwiki has no page (#697).
- **the defined question set.** `scripts/eval/code-truth-probes.ts` freezes what the serve paths must
  answer about scanned code (interfaces, domains, dependencies, usage, depth, contracts, the vet-idea
  and scf-pitch composites) and exits 1 on any miss; since 2026-09-30 it runs on the daily eval lane
  (#1743, 10 of 10 passing). a code-question battery is wired into the routing and consumer
  evaluations (#696) and mirrors raven's soroban battery topics (#844). the content-freshness guard
  fails ci when a published stellar cli command goes stale (#351).
- **for raven, the contract it routes on.** the openapi spec went from 1.2 at the start of july to
  1.9.54 (38 operations, 244 changelog entries), every discovery operation carrying the routing
  guidance raven's catalog indexes; a scorer replica of raven's own routing math
  (`scripts/eval/raven-scorer-replica.ts`) and a routing eval that asks raven real builder questions
  and checks it lands on the right operation (#689, #692) let us classify every routing miss from our
  side. `/api/changelog` is the consumption contract, gated so its newest entry can never name a
  field the schema lacks; the installable skill is served live and kept byte-identical with the
  mirror raven pins, checked daily (#708, #717). `@stellar-light/scout-mcp` had 9 releases and
  `@stellar-light/api-client` 14.
- **for raven, what it asked for in production.** a metered partner tier (1,200 requests per minute,
  200,000 per day, #1714) and the matching client release the same day; after its team's two-day load
  test, the three problems they reported were fixed within a day: stalls bounded by database and
  embedding timeouts and a connection-pool cap (#1721, #1728, #1729), `Retry-After` on every 503,
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
- **one backlog for every detector.** the improvement ledger (#683 to #686) normalizes every engine's
  findings into one status-tracked file, feeds raven's real questions through the gateway (#684,
  #687) and closes findings only through waves that re-check them (#685).
- **daily and per-deploy gates.** guard d, a daily rotating truth battery over the live api (#1047;
  108 of 108 on 2026-08-29); golden evaluations after every production deploy (post-deploy-eval, 51
  of 53 on 2026-09-26); the daily raven parity lane (51 pass both, 0 raven-only failures on
  2026-09-29); the api-drift guard asserting the api, the openapi spec and the docs agree; the
  self-audit lane at 69 checks passing, 0 failures on 2026-09-29.
- **invariants in ci.** QUALITY.md (#1058) names the recurring defect classes and the closure rule;
  three invariants run in `contract:check`: schema opacity (47 open maps paid down to zero, #1092),
  honesty-layer conformance (#1060) and enum literals; plus the contract gate (spec snapshot,
  generated client types, changelog coupling, #372) and the routing-surface check.
- **agent lanes.** the repair lane (#1559) and the task lane (#1569) pick one ledger row a day and
  open a pull request from a checkout with no production secrets; 52 scheduled workflows run (every
  file under .github/workflows with a cron), every writer with read-back and an idempotence gate.
- **third-party grading, and the loop built around it.** raven's audit filed 16 findings against
  stellar light this quarter; 12 are closed at the root (examples: count instability on wallet
  queries #1064, rfp fundability and stablecoin counts #955, enum drift and rwa issuer coverage
  #1532), 4 remain open with evidence attached. two guards exist only because of how raven consumes
  us: cross-surface consistency (the same fact must agree across every operation that serves it) and
  honest absence (an empty result must say whether it was checked); engine d mines raven's real
  questions and our api logs for the queries we miss (#452, #687); and our `meta.generatedAt`,
  `matchMode` and `counts` became judge-visible evidence in raven's own evaluation (#1062).

verify: <https://stellarlight.xyz/quality> · <https://stellarlight.xyz/api/quality> ·
<https://github.com/Stellar-Light/stellarlight/blob/main/QUALITY.md> ·
<https://github.com/Stellar-Light/stellarlight/actions/workflows/post-deploy-eval.yml> ·
<https://github.com/Stellar-Light/stellarlight/actions/workflows/raven-eval-parity.yml>

#### Q3 D3: partner portal to general availability

committed: portal out of beta, partners live with maintained profiles, concierge matching on
structured fields, and freshness check-ins sending.

delivered:

- **out of beta.** the beta label came off the directory, the concierge and the portal on 2026-10-01
  (#1749). what builders and raven use today: 43 published partners (21 anchors, 5 wallets, 5 audit
  firms, 4 protocols, 3 infrastructure, 3 asset issuers, 2 tooling), each profile maintained from the
  partner's own stellar.toml with provenance (`tomlSourceUrl`, `tomlFetchedAt`, #831) and aged daily
  by the freshness lane (fresh, aging, stale, archived) so a stale listing is visibly stale and drops
  out of ai matching; 12 of the 21 anchors carry toml-verified fields, the other 9 publish no
  stellar.toml at all (each domain checked 2026-09-30). raven exposes the directory through
  `get_partners`.
- **concierge matching on structured fields.** the deterministic matchmaker and the concierge rank on
  assets, SEP-6/24/31, ramp types and country; official anchors missing from the directory were
  seeded from anchors.stellar.org (#246).
- **claim + ownership verification.** a claim is verified by construction: the claimant's mailbox has
  to sit on the listing's own domain (shared hosts excluded), and a verified claim sets the account
  email without an admin in the loop (#1742, 2026-09-30). the sign-in link is the path a partner uses
  to change anything.
- **freshness check-ins sending.** the first quarterly check-in went out on 2026-10-01 to the 11
  published partners with a contact address on file, 10 of them in the default directory listing and
  one below its quality bar (#1749, #1750; 11 delivered, 0 failed): "still active and taking work?
  review your listing and update what changed", signed in with the address we mailed. the digest runs
  every monday and bundles the check-in with builder-lead alerts so a partner is never mailed twice;
  a partner with no address or a failed send is reported, not counted, and comes back the next week.
- **the product passes.** portal v2 with login and ai-guided maintenance (#240), the public concierge
  chat and weekly lead digest (#241), a real listing pipeline with claim requests (#244), directory
  v5 (#326), personalized related partners (#345), partner logos fixed (#330); contract work in
  august and september: `getPartner` declares its full 31-field profile (#1045), the asset-issuer
  type (#1269), region as a typed enum with 400s instead of silent zeros (#1314, #1323), honest nulls
  for facts never checked (#992, #1360).

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
  (#957 to #960): own collections, a six-hourly writer, the api served from our own store, and the
  explorer on our domain, with the full price history (3,763 rows, 18 assets, from november 2025)
  carried over. 41 assets tracked; usdt0's september launch landed the same week. we are evaluating
  pyth price feeds as a data source for a product test with sdf.
- **a verified rwa registry.** `GET /api/rwa` (#1298): 113 rows, 97 rwa.xyz tokens, 52 issuers, each
  verified on chain, from the issuer's stellar.toml outward where one exists, with the verification
  level served per row, and re-measured every six hours (#1309), with on-chain control flags (#1305)
  and a cross-vendor audit correction (#1302).
- **audits, hackathons, builders, dev activity.** the audit registry serves 64 reports with
  per-auditor findings extraction (#603); hackathons run on the dorahacks v1 hub api across every
  organizer plus curated events (#757, #914), with prior-art search over every build (#693); 233
  builder profiles (2026-10-01) show hackathon submissions with placement (#931); electric capital
  snapshots refresh weekly (as of 2026-09-21).
- **research corpus.** 10,893 documents across 16 sources on 2026-10-01 (seps, caps, dev docs, the
  sdf blog, lumenloop research and news, audits, incidents, the security program, releases, the ec
  developer report); the vector index gained a source filter so every source answers semantically
  (#1728); exact-figure retrieval guaranteed on the vector path (#715).
- **the directory stays true.** scf pages beyond the fund's 500-row listing cap recovered 112 rows
  and 147 awards (#1397); 108 proven-broken links were routed into a repair queue (#1413); duplicate
  records fold under a canonical with an operator veto (#1311); repositories that no longer exist are
  stamped `gone`; one field, one writer ended the enrich and curate flip-flops (#1400). new facts
  land within days: spectra's stellar launch was reported on 2026-09-26 and the row served live
  status, structured products, tvl and nine contracts on 2026-09-28 (#1734).
- **pipelines that report their own failures.** the on-chain lane had been hitting stellar.expert's
  rate limit at the end of every run and reporting success; it now backs off, retries and ends red if
  a row stays stale (#1735); the toml parser keeps asset-code case (#1736).
- **uptime under load.** the database connection cap that caused stalls was found and fixed (pool
  cap, fail-fast timeouts, an adapter crash trapped, #1721, #1728, #1729); every 503 carries
  retry-after; measured on 2026-09-29: 600 requests per minute for a minute, 600 of 600 answered, p99
  1.7 seconds. 52 scheduled workflows run; the api-drift guard is green and every /api/status source
  updated on 2026-09-29.
- **the site.** /ask, the natural-language search over projects, research and partners, is public;
  /analytics shows usage in the open (all-time and 30-day calls, the last 7 days by endpoint);
  /entities and /builders give organizations and builders their own profiles with code activity and
  link provenance (#911, #913); the stablecoin explorer was rebuilt on our domain with per-asset
  pages, issuer drawers and a latest-updates rail (#962 to #965).
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
  (#1689 to #1695); a signed cross-device ballot status so a pilot is recognized on any device
  (#1726); authorship proof kept per ballot (#1718) and, since 2026-09-30, an authorization memo that
  commits to a server-issued nonce so a copy of a signed authorization reveals nothing (#1744); a
  lane that reads the scf voting contract's eligible-voter list as import-ready csv (#1528); the
  round manifest and the published results anchored on tansu (#1635 to #1639); a daily reconcile
  between chain and record (#1630, #1632); an admin-only tally view of who voted for what, with the
  standings the publish lane would count (2026-10-01). status on 2026-10-01: 34 nominees across 3
  categories, 76 pilots whitelisted, and a rehearsal round open to any wallet for sdf's own testing
  before the pilots get the link.
- **rfps.** q3 rollover with the layerzero dvn and x402 bazaar briefs (#751); scf round #46 is served
  as an open row with its 2026-11-08 deadline; 16 briefs (2 open, 14 closed) alongside the round row.
  the scf public goods award is structured truth on project rows (#631) and per-round awards are
  official records (#759, #811).
- **ideas, skills, builders.** the ideas platform and `vet-idea` are live; the 10 scf skills sit in
  the marketplace as one service offering with two reviewer skills (#672, #707); builder profiles
  show hackathon submissions with placement (#931); the hackathon tracker is current (26 events,
  hackmeridian listed as upcoming).
- **reports, not met.** the six thesis reports were refreshed on 2026-08-14 and the scf funding
  analysis gained round-level data (41 rounds, #576), but no new report was published this quarter;
  the blog now also syndicates ecosystem posts from sdf and tellus through the feed sync. the
  quarter's writing went into the code-truth and quality work above, and reports are the shortfall in
  this deliverable.

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

the ecosystem is going ai-native, and stellar light is positioned to be the data layer it runs on.
tyler van der hoeven (kalepail) at SDF is building **raven** — an ai agent designed to become the way
the _entire_ stellar ecosystem asks questions: builders scoping a project, institutions doing due
diligence, scf reviewers evaluating grants, newcomers finding their footing. raven doesn't hold the
data itself; it sits on top of data layers and surfaces them. two of those layers are **stellar
light** and **lumenloop** (raph's research/media layer). stellar light is the authoritative source
for the hard, structured stuff — projects, code, repos, funding, partners, builders, and live
activity. that is the position this quarter set up, and it's why q3 matters: **as the ecosystem's ai
layer takes off, stellar light becomes load-bearing infrastructure underneath it.** the north star
for q3 is to make stellar light the deepest, freshest, and most correct data layer that raven — and
every builder, institution, and agent — can rely on.

**that dependence is no longer a plan — it is externally verifiable today, in raven's own public
repo.** none of these links are ours; they are the consumer's own code and process:

- raven is live and queries stellar light through a dedicated adapter — verify:
  https://github.com/kalepail/stellar-raven/blob/main/src/adapters/scout.ts
- raven's routing catalog consumes stellar light's machine-routing metadata (the `x-routing`
  extension we shipped for it) as a scored input — verify:
  https://github.com/kalepail/stellar-raven/commit/baabc06b13ef ("x-routing extension scored as lever
  7")
- raven's ci monitors stellar light's live contract and automatically files a drift review on every
  release we ship — verify: https://github.com/kalepail/stellar-raven/issues/21
- raven's maintainer runs a public, 53-item quality ledger on stellar light — the most-audited data
  service in his program — and his own tooling marks our fixes `fixed-upstream`, most closed within
  days of filing — verify:
  https://github.com/kalepail/stellar-raven/tree/main/improvements/stellar-light-scout
- on our side, every release is eval-gated before it reaches raven (recall floors, answer-correctness
  golden set, contract-honesty probes), and scf award data itself is verdict-verified weekly against
  communityfund.stellar.org — verify: https://stellarlight.xyz/api/changelog

this two-way loop — his ci reviewing our contract, our evals gating what he consumes — is the working
model for how agent data layers should hold each other honest, and stellar light is its reference
implementation. funding this quarter funds the load-bearing half of that loop.

**1. be the data + code layer raven and the ecosystem depend on.** this quarter i already worked
directly with tyler to make stellar light more consumable by raven — hardening the api and openapi
spec, fixing how our data routes and answers, and reconciling the contract so raven can trust it. q3
goes deeper. the hardest, highest-value ecosystem questions are code-level and current-state ("which
crate and version is right," "which CAP added this host function," "what's the current cli path to
scaffold a contract"), and no data source answers them well today. i'm extending stellar light to —
scoring live soroban repo code, matching it against the docs and CAP/protocol history, layered on top
of the projects/funding/partner/repo data already indexed — so that when raven (or any agent)
surfaces an answer, it's grounded in a source that's correct and current, not a guess. tyler has
explicitly flagged this code-truth layer as the piece that makes stellar light irreplaceable rather
than duplicative. it's not a side project — it's the same data-layer mission, going one level deeper.

**2. a continuous eval + improvement loop.** the game once the plumbing is in place is: run a large,
growing question set against our data (from raven's evals, from real questions builders ask across
the ecosystem, from anywhere), find the low-scoring answers, diagnose _why_, fix the data or the
endpoint, and repeat. i'll institutionalize this so stellar light measurably improves every cycle
instead of drifting — the only way a data layer stays trustworthy as the ecosystem grows around it.

**3. the partner portal as a real product.** finish the partner layer: the anchor / on-off-ramp /
infrastructure / tooling / audit-firm directory with the ai concierge for builders, partner
self-service maintenance, and quarterly freshness check-ins. this gives builders a trustworthy "who
do i integrate with" answer, gives institutions a real map of stellar's on/off-ramp and infra
providers, and gives partners a reason to keep their own data accurate — a self-sustaining data loop
that also feeds raven.

**4. maintain, grow, and integrate.** keep stellar light healthy and expanding: data-freshness
pipelines, ranking and relevance quality, new data sources, uptime, and the discovery surfaces
(directory, leaderboard, stablecoin explorer, research corpus, hackathon + rfp pipelines) that
builders and scf use directly.

the bet is simple: stellar's ecosystem is becoming measurable and queryable through ai, and the
agents doing it — starting with raven — need a data layer that is fresh, structured, deep, and
correct. that layer is stellar light. this quarter proved the direction; q3 makes it the
indispensable foundation the ecosystem's ai layer is built on.

<!-- markdownlint-enable MD034 -->

## Proposed Deliverables

<!-- markdownlint-disable MD034 -->

### 1. code + current-state intelligence layer — the raven dependency

build the code-truth layer: score live soroban/stellar repo code and match it against the docs and
CAP/protocol history, layered on top of the repo/project/funding/partner data already indexed, so
that agents (raven and any other) get grounded, current answers to code-level questions — which crate
and version is right, which CAP added a host function, the current cli path to scaffold a contract —
instead of guesses. expose it through the existing api / openapi / mcp / skill surfaces so it's
consumed the same way as everything else. ecosystem value: the highest-value ecosystem questions are
code-level and current-state, and no data source answers them well today; tyler has explicitly
flagged this as the piece that makes stellar light irreplaceable rather than duplicative. measurable:
code-truth endpoint live and documented in the openapi spec, answering a defined set of
code/current-state questions with sourced references.

### 2. continuous eval + improvement loop

institutionalize a repeatable evaluation cycle: run a large, growing question set — from raven's
evals, from real questions builders ask across the ecosystem, and from our own golden set — against
the live data layer, score the answers, diagnose the low-scoring ones, and fix the data or the
endpoint. ecosystem value: a data layer only stays trustworthy if it measurably improves as the
ecosystem grows around it, rather than drifting. measurable: eval harness running on a regular
cadence with a tracked answer-quality score that improves over the quarter, and regressions caught
before they ship (drift guard + golden evals in CI).

### 3. partner portal to general availability

take the partner layer out of beta: onboard real anchors, on/off-ramps, infrastructure, tooling, and
audit-firm partners onto the self-service portal, ship the claim + ownership-verification flow, keep
the ai concierge matching on real stellar.toml data (assets, SEP-6/24/31, on/off-ramp, jurisdiction),
and run the quarterly freshness check-ins so listings stay current. ecosystem value: builders get a
trustworthy "who do i integrate with" answer, institutions get a real map of stellar's on/off-ramp
and infra providers, and partners get a reason to keep their own data accurate — a self-sustaining
loop that also feeds raven. measurable: portal out of beta, partners live with maintained profiles,
concierge matching on structured fields, and freshness check-ins sending.

### 4. data pipelines, freshness + ranking quality — ongoing

maintain and harden every automated pipeline (sdf airtable, github, goldsky, defillama, rwa.xyz,
dorahacks, stellar passport, electric capital, and partners' stellar.toml) and keep ranking/relevance
quality high across project search, repo search, and clusters. add new data sources where they
strengthen the layer, and keep the api ⇄ openapi ⇄ docs drift guard green so the contract never lies.
ecosystem value: data is only useful if it's fresh and correct; this keeps stellar light load-bearing
infrastructure rather than a stale directory. measurable: pipelines running with no significant
downtime, new projects/stablecoins/repos reflected within ~1 week, drift guard green, and /api/status
freshness current.

### 5. scf program support, rfp + hackathon maintenance, and reporting — ongoing

keep the rfp section populated with the current (q2) round of scf rfps and surface them to builders
(also mirrored to the scf gitbook); maintain the ideas platform, the hackathon tracker with
post-hackathon project status (built / in progress / abandoned), and builder profiles; and publish
data-grounded ecosystem reports over the quarter. ecosystem value: stellar light feeds builders
directly into scf programs and gives the ecosystem visibility into what's being built, funded, and
shipped. measurable: q2 rfps live and current, ideas + hackathon trackers current, and a set of
ecosystem reports published over the quarter.

<!-- markdownlint-enable MD034 -->

## Metrics loaded from PG Atlas

[![PG Atlas](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_light&query=%24.activity_status&label=PG+Atlas&color=914CFF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_light)
[![90d Contributors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_light&query=%24.active_contributors_90d&label=90d+Contributors&color=00B578)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_light)
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_light&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_light)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_light&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_light)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.

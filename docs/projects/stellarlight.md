---
title: "Stellarlight"
parent: Public Good Projects
proposal_issue: 74
proposer: theboycoder
category: "Ecosystem Visibility"
budget: "$50,000"
---

# Stellarlight

<!-- markdownlint-disable MD036 -->

_stellar light is the ecosystem data layer for stellar — a single, machine-readable source of truth
for projects, code, funding, stablecoins, dev activity, partners, and builders, queryable by humans,
tools, and ai agents._

<!-- markdownlint-enable MD036 -->

|                      |                                                |
| -------------------- | ---------------------------------------------- |
| **Category**         | Ecosystem Visibility                           |
| **Website**          | <https://stellarlight.xyz>                     |
| **Repository**       | <https://github.com/alexanderkoh/stellarlight> |
| **First Released**   | Jan 2026                                       |
| **Intake**           | renewal (2026q3)                               |
| **Budget Requested** | $50,000                                        |

**Repository note:** the codebase currently lives in a private working repo; we're in the process of
migrating it to a public organization repo this quarter so the full source is openly available.

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

this quarter stellar light went from "a website you browse" to "a data layer the ecosystem can
query." the platform launched publicly, and — more importantly — the same data became
machine-readable so ai agents and tools consume it directly.

**public launch.** stellarlight.xyz is live and public: the directory, stablecoin explorer, github
leaderboard, dev-activity tracker, ideas/rfp platform, hackathon tracker, and blog are all in front
of the ecosystem. the launch was covered in an ecosystem interview:
<https://x.com/lumenloop/status/2069451377223536659>.

**the agent-native data layer (the big shift).** the plan for this quarter was to make the
ecosystem's data ai-queryable and plug into stella, SDF's ecosystem assistant. stella is being sunset
(shutting down at the end of the month), so instead of building for one bot i built an open interface
any agent can consume — which turned out far more valuable and future-proof. shipped: a public rest
api (24 endpoints across projects, repos, hackathons, builders, funding, research, partners), an
openapi 3.1 spec at /api/openapi.json, an mcp server published to npm (`@stellar-light/scout-mcp`), a
typed client (`@stellar-light/api-client`), and an installable `stellar-scout` skill. i also built a
public **skills marketplace** at stellarlight.xyz/skills — a curated, filterable catalog of the ai
skills, mcp servers, sdks, and tools available to stellar builders (merging SDF's official
skills.stellar.org catalog, stellar light's own, and community submissions) so builders find and
install the right agent tooling in one place. the ecosystem's data — and the tools to use it — is now
a machine surface, not just a ui.

**the ecosystem's ai agents already consume it.** stellar light is already being used as a data
source by the ecosystem's emerging ai agents — including **raven**, the ai agent tyler van der hoeven
(kalepail) is building at SDF, which sits on top of stellar light and lumenloop (raph's
research/media layer) as its data layers. i worked directly with tyler this quarter to make stellar
light more consumable by raven, and measurably improved how well it routes to and answers from our
data by hardening the openapi spec — a large, reproducible jump in correct routing. early proof that
the ecosystem's ai layer needs exactly this kind of fresh, structured, authoritative source, and that
stellar light is becoming it.

**ai across the platform.** beyond serving agents, the platform runs its own ai. an ai data-cleaning
pipeline normalizes, de-duplicates, re-categorizes, and flags stale/broken data across 900+ projects
so the directory stays accurate at scale. i built the retrieval quality itself: a vector-searchable
research corpus (SEPs, SCF handbook, dev docs, papers, security audits, incident reports) plus an
indexed-and-scored github repo layer (~2,300 stellar/soroban repos ranked by freshness, traction, and
SCF/hackathon/builder authority) so agents find the right code and the right source, not noise. every
answer carries a confidence score (relevance + freshness + authority) so consumers — human or agent —
know how much to trust it. a natural-language interface (`/ask`) puts all of this behind a
plain-english question; it's currently in private testing.

**the partner portal (an ai product on its own).** built the partner layer end to end: a directory of
anchors, on/off-ramps, infrastructure, tooling, and audit firms, each enriched directly from the
partner's stellar.toml (supported assets, SEP-6/24/31, on/off-ramp capability, jurisdiction) to match
the official stellar anchor directory. on top of it, an ai concierge that matches builders to the
right partner from a plain-english need ("i need a USDC off-ramp in mexico"), and a full self-service
portal (in beta): partners log in and maintain their profile through an ai-guided chat, get demand
signals when builders search for them, and receive quarterly freshness check-ins so their data never
goes stale. a claim flow lets real companies take ownership of their listing.

**data quality + integrity.** golden-answer evaluations, retrieval chunk hygiene, org/builder
attribution ("who built X" → the company behind each project), defunct-project handling so dead
projects stop ranking as active, and a daily drift guard that asserts the api, the openapi spec, and
the docs never disagree.

**content.** thesis-driven ecosystem reports published on /blog covering the state of stellar, the
defi landscape, SCF funding, stablecoins, developer activity, and the hackathon pipeline.

<!-- markdownlint-enable MD034 -->

## Past Deliverables

<!-- markdownlint-disable MD034 -->

### The public API — 24 endpoints (live at /api/openapi.json)

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

### MCP server, typed client, and installable skill

`@stellar-light/scout-mcp` — an mcp server (18 tools) published to npm, so any mcp client (claude,
cursor, etc.) can query the whole data layer. `@stellar-light/api-client` — a typed typescript sdk on
npm. `stellar-scout` — an installable skill (SKILL.md + references) for coding agents. all three have
a public home at stellarlight.xyz/scout — a landing page with one-line install commands, the full
tool reference, and worked examples so a builder or agent can go from "never heard of it" to
installed in a minute. mirrored to public repos and listed in skill registries.

verify: <https://stellarlight.xyz/scout> · <https://www.npmjs.com/package/@stellar-light/scout-mcp> ·
<https://www.npmjs.com/package/@stellar-light/api-client>

### Skills marketplace

public catalog of ai skills, mcp servers, sdks, and tools for stellar builders at
stellarlight.xyz/skills — merges SDF's official skills.stellar.org skills, stellar light's own, and
approved community submissions, each with an install command and compatibility info. includes a
community submission flow.

verify: <https://stellarlight.xyz/skills>

### AI systems

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

### Research corpus + code intelligence

vector-searchable knowledge corpus — SEPs, SCF handbook, dev docs, papers, security audits, incident
reports — with confidence scoring, plus an indexed-and-scored github repo layer (~2,300
stellar/soroban repos ranked by freshness, traction, and SCF/hackathon/builder authority) surfaced
via /api/repos/search and inline on project pages. `/api/repos/explain` routes deep code questions to
the authoritative repo and returns a source-grounded answer.

verify: <https://stellarlight.xyz/api/research?q=soroban%20authorization> ·
<https://stellarlight.xyz/api/repos/search?q=wallet>

### Partner / anchor data layer + self-service portal

full partner layer live at stellarlight.xyz/partners: a directory of anchors, on/off-ramps,
infrastructure, tooling, and audit firms, each enriched directly from the partner's stellar.toml
(assets, SEP-6/24/31, on/off-ramp, jurisdiction) to match the official stellar anchor directory. an
ai concierge for builder→partner matching, and a self-service portal (in beta) where partners log in,
maintain their profile through an ai-guided chat, see demand signals when builders search for them,
and get quarterly freshness check-ins. a claim flow lets companies take ownership of their listing.

verify: <https://stellarlight.xyz/partners>

### Data sources, pipelines & freshness

integrated and kept fresh via automated pipelines: SDF entity airtable (projects + grants), the
github api (dev activity, stars, commit recency, repo metadata), goldsky (stablecoin on-chain data),
defillama (defi tvl), rwa.xyz (rwa tvl), dorahacks (live hackathons), stellar passport (builder
profiles), electric capital (developer activity), and partners' own stellar.toml files. 900+
projects, ~2,300 repos, 100+ builders, and the partner directory are refreshed on scheduled jobs,
with a `/api/status` endpoint exposing per-source freshness so consumers always know how current the
data is.

verify: <https://stellarlight.xyz/api/status>

### Data quality + integrity

golden-answer evals, retrieval chunk hygiene, org/builder attribution ("who built X"), an "inactive"
lifecycle state so defunct projects stop ranking as active, and a daily api ⇄ openapi ⇄ docs drift
guard in CI that fails if the live api, the spec, and the docs ever disagree.

verify: <https://stellarlight.xyz/api/changelog>

### Platform, dashboards & quality-of-life

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

### Content and ecosystem reporting

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

- raven is live and queries stellar light through a dedicated adapter —
  verify: https://github.com/kalepail/stellar-raven/blob/main/src/adapters/scout.ts
- raven's routing catalog consumes stellar light's machine-routing metadata (the `x-routing`
  extension we shipped for it) as a scored input — verify:
  https://github.com/kalepail/stellar-raven/commit/baabc06b13ef ("x-routing extension scored as lever 7")
- raven's ci monitors stellar light's live contract and automatically files a drift review on every
  release we ship — verify: https://github.com/kalepail/stellar-raven/issues/21
- raven's maintainer runs a public, 53-item quality ledger on stellar light — the most-audited data
  service in his program — and his own tooling marks our fixes `fixed-upstream`, most closed within
  days of filing — verify: https://github.com/kalepail/stellar-raven/tree/main/improvements/stellar-light-scout
- on our side, every release is eval-gated before it reaches raven (recall floors, answer-correctness
  golden set, contract-honesty probes), and scf award data itself is verdict-verified weekly against
  communityfund.stellar.org — verify: https://stellarlight.xyz/api/changelog

this two-way loop — his ci reviewing our contract, our evals gating what he consumes — is the
working model for how agent data layers should hold each other honest, and stellar light is its
reference implementation. funding this quarter funds the load-bearing half of that loop.

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

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.

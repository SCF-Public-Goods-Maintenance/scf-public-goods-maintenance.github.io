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

the maintenance reserve of $20,000 covers the work that arrives during the quarter whether or not we
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

---
title: "Stellarlight"
parent: Public Good Projects
proposal_issue: 74
proposer: theboycoder
category: "Ecosystem Visibility"
budget: "$30,000"
---

# Stellarlight

<!-- markdownlint-disable MD036 -->

_stellar light is an ecosystem discovery and analytics platform for exploring projects, stablecoins,
dev activity, builder tools, and more across stellar in a single platform._

<!-- markdownlint-enable MD036 -->

|                      |                                                |
| -------------------- | ---------------------------------------------- |
| **Category**         | Ecosystem Visibility                           |
| **Website**          | <https://stellarlight.xyz>                     |
| **Repository**       | <https://github.com/alexanderkoh/stellarlight> |
| **First Released**   | Jan 2026 - soft launch                         |
| **Intake**           | soft-launch                                    |
| **Budget Requested** | $30,000                                        |

## Project Description

<!-- markdownlint-disable MD034 -->

stellar light is the ecosystem discovery and analytics platform for stellar. it brings together
project data, stablecoin analytics, dev activity tracking, builder onboarding tools, and ecosystem
content into a single platform. before stellar light, project information was scattered, stablecoin
data required checking multiple sources, and new builders had no clear starting point. stellar light
closes these gaps. builders find tools and funded opportunities in minutes. institutions use it as a
due diligence layer for stablecoins, project health, and dev activity. scf reviewers track project
health between rounds. the ideas platform, rfp section, and hackathon tracker feed builders directly
into scf programs.

<!-- markdownlint-enable MD034 -->

## Team & Experience

<!-- markdownlint-disable MD034 -->

Stellarlight is run by me (boxy00), i've been in the ecosystem for the past 6 years. Contributing to
it's growth via SCF, hackathons, VC programs, events, SDF programs and more

<!-- markdownlint-enable MD034 -->

## Retroactive Impact

<!-- markdownlint-disable MD034 -->

this quarter stellarlight went from concept to live infrastructure that multiple parts of the
ecosystem are already using.

ecosystem integrations. stellarlight is now integrated with sdf's entity airtable (automated project
and grant data sync), github api (dev activity and leaderboard data), goldsky (stablecoin on-chain
data), defillama (defi tvl), and rwa.xyz (rwa tvl). the rfp section was added to the scf gitbook as a
resource for builders exploring the rfp track. stellarlight was integrated into passport
(passport.stellarcoop.com) as a builders directory, with builder profiles connected through stellar
passport for ecosystem events and community coordination

scf pipeline impact. we built the intake form for q1 rfp sections and helped mentor hummingbot's rfp
application through ethdenver. the ideas platform and rfp section are feeding builders directly into
scf programs rather than relying on cold submissions.

hackathon tracker. the hackathon tracker surfaces upcoming stellar hackathons and tracks
post-hackathon project status (built, in progress, abandoned), giving scf and the ecosystem
visibility into which hackathon projects turn into real products and which teams are worth following
up with.

stablecoin data. the explorer is tracking live on-chain metrics across 22+ verified stellar
stablecoins: supply, market cap, holders, 24h volume, defi liquidity, and peg stability. this data
didn't exist in one place before. it's now accessible to anyone evaluating stablecoin options on
stellar.

ai-powered data cleaning. we built an ai algorithm to normalize, verify, and fix project data across
the directory. with 745+ projects sourced from multiple inputs (airtable, public submissions,
github), data quality is a constant challenge. the algorithm identifies duplicates, corrects
categorization, flags stale or broken links, and ensures project profiles are accurate and consistent
at scale.

project and dev activity data. 745+ projects indexed. the github leaderboard and dev activity tracker
are providing the ecosystem's first automated, transparent view of which projects are actively
maintained. project profiles surface github commits, stars, issues, last active date, and scf funding
status.

content reach. 12+ blog posts published covering protocol 24, privacy research. this content is being
referenced across the community as independent ecosystem coverage.

stellarlight hasn't fully publicly launched yet, with the public launch planned for q2. the focus
this quarter was building the infrastructure and there's already real usage across the rfp pipeline,
stablecoin explorer, and content layer.

<!-- markdownlint-enable MD034 -->

## Past Deliverables

<!-- markdownlint-disable MD034 -->

**intake mechanism**

direct integration with sdf's entity airtable for one-directional data sync (projects + grants). live
and operational. public intake form for new project submissions, reviewed against eligibility before
publishing. live at stellarlight.xyz/submit.

**public launch modules**

highlight modules for trending and high-impact projects: "top builders," "emerging apps," "community
picks," and "trending projects." all live on stellarlight.xyz homepage. monthly ecosystem digest
auto-generated from directory data. published via stellarlight.xyz/blog.

**ranking and discovery**

protocol and contract exploration: surfacing on-chain data including number of invocations and usage
metrics for soroban contracts. discovery modifiers: scf and sdf affiliation filters. recency and
frequency-of-update signals integrated into project ranking. github activity leaderboard ranking
ecosystem projects by stars, issues, and commit recency. live at stellarlight.xyz/leaderboard.

**stablecoin explorer**

22+ verified stablecoins tracked with historical dashboards (14d, 90d, 1y), issuer leaderboard, and
top issuer breakdowns (circle, paypal/paxos, gmo trust, fxdao, novatti group). live at
stellarlight.xyz. defi visibility layer: amm liquidity, tvl, and blend capital integrations surfaced
alongside stablecoin data. curated developer tools directory for payments and stablecoin builders.
additional data updates integrated via goldsky.

**hackathon tracker**

hackathon event calendar surfacing upcoming stellar hackathons. post-hackathon project status
tracking (built, in progress, abandoned).

**project directory and profiles**

745+ stellar projects and entities indexed with linked project and company profiles, fully
categorized. github stats and blog rss feeds integrated into individual project pages. tvl charts
embedded on individual project pages. public transparency and change logs for project data.
mobile-first ui redesign with advanced filters, infinite scroll, and responsive layout.

**builder onboarding and rfps**

curated project ideas across defi, payments, infrastructure, dev tools, and gaming. live at
ideas.stellarlight.xyz. dedicated rfp section populated with this quarter's active scf rfps. live at
ideas.stellarlight.xyz/rfps. also added to the scf gitbook. helped mentor hummingbot's application
through ethdenver and built the intake form for q1 rfp sections. difficulty ratings, category
filters, and moderation/approval workflow. event and hackathon promotion hooks to connect ideas with
active programs.

**passport integration**

stellarlight integrated into passport (passport.stellarcoop.com) as a builders directory, with
builder profiles connected through stellar passport for ecosystem events and community coordination.

**ai-powered data cleaning**

built an ai algorithm to normalize, verify, and fix project data across the directory. identifies
duplicates, corrects categorization, flags stale or broken links, and ensures project profiles are
accurate and consistent at scale.

**ecosystem visualizations**

tvl charts on project pages. defi tvl (defillama) and rwa tvl (rwa.xyz) on homepage.

**content and ecosystem reporting**

12+ original blog posts published at stellarlight.xyz/blog covering protocol 24 upgrade guide,
privacy on open blockchains, pos risk analysis, more.

proof: all shipped features are live and verifiable at stellarlight.xyz, stellarlight.xyz/entities,
stellarlight.xyz/leaderboard, stellarlight.xyz/hackathons, stellarlight.xyz/blog, and
ideas.stellarlight.xyz

<!-- markdownlint-enable MD034 -->

## Proposed Impact

<!-- markdownlint-disable MD034 -->

the core platform is built. the directory, data pipelines, stablecoin explorer, leaderboard, dev
activity tracker, ideas platform, rfp section, and ai algorithm are all in place. adding new
features, integrating new data sources, and plugging into sdf's evolving needs is now fast and
low-cost. the hard part is done.

q2 is about launching publicly and putting this data in front of the ecosystem. the north star is
data: making stellar's ecosystem measurable, transparent, and accessible from one place.

**public launch** launching publicly means this data reaches the people who need it. builders use
project data to find active tools, assess what's maintained, and avoid rebuilding what already
exists. institutions use stablecoin and project data for due diligence. scf uses project health data
and dev activity to track funded projects between rounds. we'll instrument site analytics from day
one to measure who's using the data, how they're finding it, and what they're searching for. this
creates a feedback loop where the data we track about the ecosystem includes data about how the
ecosystem uses stellarlight itself. ai-powered data access. the directory is 745+ projects and
growing. manual browsing doesn't scale. the ai algorithm we built in q1 makes all of this data,
project data, stablecoin data, dev activity, queryable through natural language. in q2 we ship it to
users and integrate with stella, so anyone can ask "which lending protocols on soroban are most
active" or "show me projects funded by scf that shipped in the last 90 days" and get real answers
from live data. this turns stellarlight from a directory you browse into a data layer you query.

**scf data pipeline.** stellarlight is already operational infrastructure for scf. rfps, ideas,
hackathon tracking, project health data, and builder mentorship all run through the platform. in q2
we continue maintaining this, updating rfps as new rounds open, and feeding project data back into
the scf process. the goal is for scf reviewers to use stellarlight's project data as a reference when
evaluating applications and tracking post-award progress.

**data freshness and reliability.** none of this matters if the data is stale. continued maintenance
of all pipelines ensures new projects, stablecoins, and protocols are reflected as they come online.
project profiles stay current through automated github syncs and community submissions. this is what
separates infrastructure from a static directory.

**content driven by data.** our blog content shifts toward data-driven ecosystem reporting. instead
of just covering news, we surface trends from the platform itself: which project categories are
growing, where dev activity is shifting, stablecoin supply movements, rfp pipeline health, and which
funded projects are still actively building. the data tells the story.

<!-- markdownlint-enable MD034 -->

## Proposed Deliverables

<!-- markdownlint-disable MD034 -->

1. public launch and analytics — month 1

full public launch of stellarlight.xyz with launch announcement, community outreach, and onboarding
documentation. implement site analytics to track visitors, search queries, project page views,
stablecoin explorer usage, and leaderboard engagement. ecosystem value: the ecosystem gets a shared,
public data layer it can actually use. builders, scf, sdf, and institutions all operating from the
same source of truth. measurable: launch completed, baseline metrics reported.

2. ai discovery and stella integration — month 2

deploy the ai discovery algorithm as a user-facing search feature on stellarlight.xyz, enabling
natural-language queries across project data, stablecoin data, and dev activity. integrate with
stella bot for ecosystem queries. ecosystem value: 745+ projects and growing. manual browsing doesn't
scale. ai search makes the entire data layer queryable for builders, partners, and institutions.
measurable: ai search live on site, query volume and success rate tracked.

3. project and stablecoin data pipeline maintenance — ongoing

continued maintenance of all automated data pipelines: sdf airtable sync, github api, goldsky,
defillama, rwa.xyz. keep project profiles current with github activity, funding status, and
categorization updates. add new stablecoins and issuers as they come online. maintain github activity
leaderboard and dev activity tracker. continue running ai data cleaning algorithm to normalize,
verify, and fix project data at scale. enhanced on-chain metrics for project discovery: deeper
soroban contract data, transaction volumes, and active address counts surfaced on project profiles.
exploring lumenloop and pg atlas as additional cross-data sources to enrich project profiles and
align with scf's public goods metrics framework. ongoing moderation of project submissions through
the public intake form. ecosystem value: data is only useful if it's fresh. this ensures stellarlight
remains reliable infrastructure rather than a stale directory. measurable: all pipelines running with
no significant downtime, new projects and stablecoins added within 1 week of appearing on-network,
enhanced on-chain metrics live on project pages.

4. scf program support, rfp, and hackathon maintenance — ongoing

populate rfp section with q2 active scf rfps as they're published. maintain ideas platform with new
curated project ideas and difficulty ratings. continue builder mentorship and intake form support for
scf pipeline. update hackathon calendar and post-hackathon project status tracking (built, in
progress, abandoned). maintain builder profiles and passport integration. ecosystem value:
stellarlight feeds builders directly into scf programs and gives the ecosystem visibility into
hackathon-to-product conversion. measurable: q2 rfps live within 1 week of publication, ideas
platform updated monthly, hackathon tracker current.

5. ecosystem mapping and data-driven reporting — ongoing

produce ecosystem maps and reports similar to messari-style coverage, powered by stellarlight's data
layer. track ecosystem growth by category, project count, dev activity concentration, stablecoin
flows, tvl movements, and builder pipeline health. publish minimum 6 pieces over the quarter:
ecosystem maps, category deep dives, and data snapshots. ecosystem value: messari and other data
platforms miss out on critical data or reporting missing information measurable: annual ecosystem map
format established and blogs

<!-- markdownlint-enable MD034 -->

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.

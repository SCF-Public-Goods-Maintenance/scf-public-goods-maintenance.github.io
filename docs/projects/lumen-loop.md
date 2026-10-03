---
title: "Lumen Loop"
parent: Public Good Projects
proposal_issue: 173
proposer: rawritude
category: "Ecosystem Visibility"
budget: "26000"
---

# Lumen Loop

<!-- markdownlint-disable MD036 -->

_An independent, always-current discovery layer for the Stellar ecosystem: news, research, projects,
events, media, jobs and governance, published free and machine-readable._
<!-- markdownlint-enable MD036 -->

|                      |                                                                                                     |
| -------------------- | --------------------------------------------------------------------------------------------------- |
| **Category**         | Ecosystem Visibility                                                                                |
| **Website**          | <https://lumenloop.com>                                                                             |
| **Repository**       | <https://github.com/lumenloop>                                                                      |
| **First Released**   | March 2024                                                                                          |
| **Intake**           | <https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/issues/136> |
| **Budget Requested** | 26000                                                                                               |

## Project Description

<!-- markdownlint-disable MD034 -->

Lumen Loop is the discovery layer for the Stellar ecosystem: one always-current place to find every
project, story, event, video, job and governance vote across the network.

A fleet of AI agents monitors 600+ social accounts, project blogs, RSS feeds, community calendars,
YouTube, X Spaces, podcasts, DAO governance contracts and job boards, triages and summarises what it
finds, and ties each item back to the project it concerns. The result publishes free as a website, a
CC-BY-4.0 open project database, RSS, iCal and podcast feeds, a read-only MCP server and MIT agent
skills. Ingested content is redistributed to X, Reddit and Discord, and a weekly newsletter is
distilled from the same corpus.
<!-- markdownlint-enable MD034 -->

## Team & Experience

<!-- markdownlint-disable MD034 -->

Lumen Loop is a solo-maintainer project.

Raphael Fortin, based in Canada. GitHub: https://github.com/rawritude Discord: ra.ph LinkedIn:
https://www.linkedin.com/in/raphael-fortin-305bb688/

Lumen Loop launched in March 2024 and has run continuously since, through two SCF Build Awards
(rounds 26 and 35). I have volunteered as an SCF Pilot for several years, previously helped run the
Stellar Hacks hackathon series, and was a contractor for the Stellar Development Foundation. I also
maintain awesome-stellar-community-fund, a set of open SCF review and round-resolution skills
distilled from Lumen Loop's corpus.

Stewardship and access. Two others hold read access to the codebase: @tupui (community) and @kalepail
(SDF). If I am no longer able to maintain Lumen Loop, both have my permission to take over and
continue running the project. The ecosystem database is CC-BY-4.0 in a public repo and already
forked, so the dataset survives independently of the service.
<!-- markdownlint-enable MD034 -->

## Retroactive Impact

<!-- markdownlint-disable MD034 -->

**Who uses it.** Lumen Loop's API and MCP server answered over 164,000 external requests in the last
90 days, most through Stellar Raven, which serves Lumen Loop data to its own users. Stellar Light and
Stellar Build also build on the data; Stellar Build bundles the full ecosystem catalog into its
developer installer. These dependencies run through the API and data rather than package imports, so
they don't appear in dependency-graph metrics. The Stellar Development Foundation uses Lumen Loop as
an intelligence platform for marketing, and to track launches and events. In the last 30 days, AI
assistants fetched Lumen Loop pages 5,812 times to answer people's questions.

**The record.** 812 projects in the open database and 1,015 SCF submissions tracked. In the last 90
days the corpus added 282 articles, 111 videos and podcasts, 187 events and 35 original research
pieces, each summarised and tied to its projects, filtering out roughly 7 in 8 candidate items to
keep the record relevant.

**Reach.** The site drew 7,820 browser visits in the last 30 days, and 430 posts distributed 191
items to ecosystem channels in the last 90. Over the last year: 500,000 X impressions covering
Stellar projects and dozens of interviews on X.

**Publishing for others.** Untangled, Rivool, xBull, Peridot, Arcane, BAF and Zenex have published
content through Lumen Loop, as has OpenZeppelin, with that piece later picked up by SDF. Newly
launched projects reach an ecosystem-wide audience they could not otherwise buy, free and on the same
terms as anyone.

**Full metrics, with sources and time windows:**
https://gist.github.com/rawritude/db1399943994798e7c36a2bed7d8239b
<!-- markdownlint-enable MD034 -->

## Past Deliverables

<!-- markdownlint-disable MD034 -->

N/A
<!-- markdownlint-enable MD034 -->

## Proposed Impact

<!-- markdownlint-disable MD034 -->

**Open the platform up.** Today almost everything routes through one person: projects wanting their
information corrected, teams wanting coverage, events that are not on Luma. The next version of Lumen
Loop changes that, letting projects maintain their own presence and letting anyone contribute to the
record. The goal is a discovery layer the ecosystem participates in rather than one it reads.

**Make the record more useful to decide with.** Coverage alone does not tell you which projects are
alive, which are maintained, or where funding has gone and what came of it. Health scoring, a stated
inclusion policy and independent funding reports turn a directory into something the ecosystem can
reason with, and make the data as useful to agents and tools as it is to people.
<!-- markdownlint-enable MD034 -->

## Proposed Deliverables

<!-- markdownlint-disable MD034 -->

**1. Release the next version of Lumen Loop this quarter. It brings:**

- Projects run their own presence. Teams claim their listing, keep it current, post jobs, and publish
  their own content on a Stellar-native publishing platform where the ecosystem context is already
  there, so what they write lands connected to the right projects, stories and events.
- Anyone can contribute. News, events not on Luma, corrections and links can be submitted directly,
  and submitters can track what happened to them.
- A knowledge base for every project. Durable, structured context held in Lumen Loop rather than
  behind permissioned third-party APIs, including historical material and unpublished data served to
  consumers like Raven and to any agent querying the corpus.
- Open access for tools and agents. Self-serve API keys, agent skills and usage visibility, without
  asking anyone.
- Curation that improves over time. Every editorial decision, by staff, contributors or agents, is
  recorded with its reasoning, so agents draw on past decisions and make better ones.

_Value:_ projects represent themselves, anyone can contribute without going through one person, and
the corpus becomes infrastructure other tools build on.

_Measure:_ the new version is live on lumenloop.com, with projects able to claim and maintain their
own listing and anyone able to submit content.

**2. Publish project health scoring.** A quantitative score for each project, derived from
development activity, releases, content, social activity and on-chain signals, shown on project pages
alongside the underlying metrics and served through the API and MCP.

_Value:_ a consistent, transparent measure of which projects are active, available to anyone
assessing ecosystem health.

_Measure:_ health scores appear on project pages with their underlying metrics and are returned by
the API and MCP.

**3. Publish inclusion and content standards.** The criteria for listing early-stage and
alternatively-funded projects, such as InstAwards recipients, and for content that projects publish
through Lumen Loop.

_Value:_ the directory and the publishing platform run on clear, stated criteria.

_Measure:_ standards published on lumenloop.com.

**4. Sustain and deepen editorial coverage.** The weekly newsletter continues throughout the quarter,
and by quarter end carries Stellar network data: stablecoin, RWA and network statistics with
accompanying graphics. Independent reporting covers the SCF and Public Goods rounds, drawing on the
ecosystem database for recipient history, prior awards and outcomes.

_Value:_ keeps the ecosystem current week to week, adds quantitative context to qualitative coverage,
and leaves a durable record of where funding went and what came of it.

_Measure:_ a newsletter every week of the quarter, one issue with stablecoin, RWA and network
statistics and graphics, and both round reports published.

**5. Curation and oversight.** A funded contributor reviews agent suggestions, curation policies,
ingested sources and new project entries; manages portal access and community contributions; and
handles categorisation, summary review, publishing and distribution to ecosystem channels. Access is
scoped and permissioned, and does not extend to the codebase.

_Value:_ human review over an agent-run platform, and the capacity that makes open contribution
workable.

_Measure:_ curated changes to projects and content are counted and published continuously through
Lumen Loop's metrics endpoint, declared on the project page for the program to poll.

**6. Maintain the platform throughout the quarter.**

- Ecosystem database updated as the ecosystem changes, committed publicly, with new projects and SCF
  award data added as they appear
- News, events, media and governance coverage published continuously
- Events calendar and iCal feed kept current
- Public feeds, API and MCP server available to everyone, free
- Value: the standing service the ecosystem already depends on.

_Measure:_ lumenloop.com/api/health is declared as the project's health endpoint so the program
observes availability directly; database committed as the ecosystem changes; calendar and feeds kept
current.

**Budget allocation**

- Maintainer, 20 hrs/week: release and new capabilities (1 to 4) - 18,200
- Contributor, 13 hrs/week from onboarding (9 weeks): curation and oversight (5) - 5,850
- Platform operation (6): hosting, content ingestion, storage, backups, CDN, domains, ecosystem
  calendar, AI and data APIs - 2,238

Total: 26,288 USD
<!-- markdownlint-enable MD034 -->

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.

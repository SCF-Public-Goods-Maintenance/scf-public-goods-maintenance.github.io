---
title: "Stellar Security Portal"
canonical_id: daoip-5:scf:project:soroban_security_portal
parent: Public Good Projects
proposal_issue: 58
proposer: SurfingBowser
category: "Developer Experience"
budget: "40,000"
---

# Stellar Security Portal

A Soroban specific knowledge base which lets users access audits, individual vulnerabilities and code
in an organized fashion.

|                         |                                                                                                    |
| ----------------------- | -------------------------------------------------------------------------------------------------- |
| **Category**            | Developer Experience                                                                               |
| **Website**             | <https://stellarsecurityportal.com/>                                                               |
| **Repository**          | <https://github.com/inferara/soroban-security-portal>                                              |
| **First Released**      | July 2025 (website) September 2025 (all milestones)                                                |
| **Intake**              | <https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/issues/22> |
| **Budget Requested**    | $40,000                                                                                            |
| **Maintenance Reserve** | $12,000                                                                                            |
| **Other**               | $28,000                                                                                            |

## Project Description

The Portal was created to have a curated knowledge base of audit reports, code & individual
vulnerabilities available in one location. Before the portal, a lot of information was scattered
across protocols, blogs, socials and discord channels making it hard to access and learn from. Users
can find individual reports which are indexed, organized and even broken down by individual findings!
Semantic search and tagging is also quite useful.

Each finding has been manually added & scrutinized by us to maintain accuracy, only adding additional
links and resources such as PRs or repos.

**Vulnerabilities**: 840 \
**Reports**: 60 \
**Protocols**: 51 \
**Auditors**: 14

It is useful for auditors, devs, new users to soroban and even AI bots who can digest the data.

## Team & Experience

Dominik Github: [https://github.com/SurfingBowser](https://github.com/SurfingBowser) Discord:
AndyKaufman

I have been involved with Stellar for a year and a half at this point. Have contributed to the
Security Portal & Inference programming language as well as the Reverse Engineering Tool.

For the portal I have manually written and reviewed a large portion of the vulnerabilities on the
portal. Actively vote in SCF rounds, try to give feedback to applying teams and recently have been
trying to attract other development teams to the Stellar network (such as the recent large tech
events I attended in Tokyo & Osaka). Looking forward to dedicating more time towards the Portal
again!

We added a new dedicated team member Andrey!

Andrey Github: [https://github.com/AKercha1](https://github.com/AKercha1)

Andrey has joined us as a new team member to help maintain and improve the portal. He has spent time
and worked with Georgii previously and will be a needed addition to our team. His focus has been on
improving the existing features of the security portal as well as reviewing and adding to the recent
contributions by other contributors.

Andrey has also helped with managing parts of our Grantfox & Drips campaigns as well.

Georgii has done work previously on the Portal but is currently committed to other projects, he does
check vulnerability findings that are logged to the Portal for a second pair of eyes before they are
approved.

## Retroactive Impact

Over the past 3 months we have continued with report logging and general maintenance for the Security
Portal. Dominik also participated in a Drips interview alongside the StellarRoute team. There is not
much to report besides small we are still working on things as expected!

Current State of the Portal as of Oct 1st 2026

**Vulnerabilities**: 954 \
**Reports**: 66 \
**Protocols**: 57 \
**Auditors**: 15

## Most notable changes since our last application

Note: this section as initially AI generated but includes manual edits and descriptions.

1. **Dev Tools (soroban-ret integration)** — new Rust/Axum micro-service (`DevTools/soroban-ret-web`)
   plus a React page that lets users compile, disassemble, and inspect Soroban contract addresses.
   Deployed behind the main portal. Commit `506767e`
   (<https://github.com/inferara/soroban-security-portal/pull/207>); docs at `DevTools/README.md`.

   This has been added as a bonus milestone to our reverse engineering tool:
   <https://github.com/Inferara/soroban-ret>

   You can access it from the Dev Tools button on the menu:
   <https://stellarsecurityportal.com/dev-tools>

2. **Comments, voting, @mentions and real-time notifications** — full threaded discussion system on
   vulnerabilities and reports, with up/down votes, reputation scoring, edit history, and SignalR +
   Redis live notifications. Commit `b23bb7b`
   (<https://github.com/inferara/soroban-security-portal/pull/170>); design spec
   `docs/superpowers/specs/2026-05-26-comments-discussion-design.md`.

3. **Visitor analytics and public view counts** — As requested every public page now shows "X today ·
   Y total" views, plus an admin/moderator Statistics dashboard. Commit `6f7c1e5`
   (<https://github.com/inferara/soroban-security-portal/pull/171> /
   <https://github.com/inferara/soroban-security-portal/pull/172>); design spec
   `docs/superpowers/specs/2026-05-27-visitor-analytics-design.md`.

4. **Audit-report ingestion** — background worker fetches PDFs, extracts metadata and
   vulnerabilities, and creates moderation-queue "agent runs" for review. Commit `394d872`
   (<https://github.com/inferara/soroban-security-portal/pull/187>).

   Although this introduces some AI elements I want to stress that I have personally used it for
   making the **process** of adding vulnerability findings to the Portal much more efficient. The
   agents can be very much hit or miss when it comes to the accuracy of parsing reports. Having a
   dedicated admin page to log multiple findings at once with some minor things pre-filled such as
   severity and titles does save some time. I still manually review line by line the findings and
   compare them to the original report with manual edits. **We are not relying on AI to log findings
   to the Portal!**

5. **Stellar Security Portal rebrand + design refresh** — renamed from Soroban Security Portal, new
   designs with light & dark mode toggle. Commit `bd1ffd1`
   (<https://github.com/inferara/soroban-security-portal/pull/173>).

6. **Protocol/auditor 1–5 star ratings** — public star ratings with reviews. Commits `baf49eb`
   (#169), `896817d` (<https://github.com/inferara/soroban-security-portal/pull/81> /
   <https://github.com/inferara/soroban-security-portal/pull/178>).

7. **OpenGraph report-summary cards** — social link previews now render audit stats instead of raw
   PDF covers. Commit `f06e16d` (<https://github.com/inferara/soroban-security-portal/pull/191>).

8. **Performance work** — report cover compression, faster vulnerabilities/reports pages, caching.
   Commits `ed0d0f8` (<https://github.com/inferara/soroban-security-portal/pull/176>), `0b778e2`
   (<https://github.com/inferara/soroban-security-portal/pull/182>).

9. **Navigator Contributions** — We have enabled Navigators to participate in the Portal. You can
   read more about the changes on Medium:
   <https://medium.com/@inferara/how-the-soroban-security-portal-is-evolving-5a37cb674217>

## Previous Deliverables

### 2026 Q2

In this section I will quote the previous deliverable goals and the result of each.

> - Increased community engagement

The amount of community involvement we have seen is less than hoped for actually.

> - Tutorial / onboarding sessions in discord, starting videos etc

These have been completed through several APAC regional community calls where the portal was
showcased to attendants (as well as other SCF projects).

> - Gather more input and feedback from users and stellar community

Done. Feedback has been sourced from the community calls, private DM's and general discussion. More
feedback is always wanted though!

> - Increase the amount of contributors to the portal for sourcing of reports, adding vulns and
>   sharing experiences (such as comments on vulns)

Not done. We have allowed for those with the Navigator role to contribute to the portal to promote
more engagement but have not seen any submissions yet.

> - Use the feedback gathered to make informed decisions on new features to add to the portal

Done. Although the feedback we have received is limited we applied it where possible.

- Visitor analytics added as per Q1 request
- Renamed to Stellar Security Portal (with domain to match and redirect from our previous one)

> - Social / community aspects (many issues listed on Github directly)

We have added many new social features to allow for community engagement:

- **Comments/discussion** is the main social layer: threaded replies, markdown, edit feature, edit
  history, moderation targets
- **Real-time notifications**: SignalR hub reply + mention notifications, notification bell,
  `/mentions` inbox.
- **Social sharing buttons + OpenGraph meta tags**: commit `1925219`
  (<https://github.com/inferara/soroban-security-portal/pull/120>). This is an easy way to share
  information on reports or findings with an automated image render which includes details like # of
  findings, severity levels and fix %. Works in discord on x and likely a few other places! Please
  try it out!

> - Leaderboard? Or some info stat page of most viewed vulnerabilities (bookmarked?) etc.

Partially Done. This is available in the admin panel at the moment, it can be made public if
requested. We have public view data on each finding / report page.

> - Being able to +/- system for vuln

Intentionally not done. In hindsight this is not a very useful mechanic and does not add much
substance. Added for comments but not for other aspects.

> - Ability for community members to submit corrections on vulns

Done. Those with the Navigator or Pilot roles can press the Edit button on a vulnerability page.

> - More public data visible such as # of page views, downloads of reports etc.

Mostly Done. Public data is available for vulnerability & report views (Total and for current day)
directly on their respective pages. Download totals are not publicly displayed.

> - More advanced API features in order to support other projects & inform users of the portal

Not done. For this deliverable we did not encounter any feedback from other contributors or projects.
So there was no informed decision to make this happen. If there are requests or ideas for making the
API more useful please share them.

> - Audits/vuln logging: As audits are performed via the audit bank (or others) we plan to have the
>   database maintained to match the Public Audit Bank list by the end of July. (pending timing of
>   new additions) <https://airtable.com/appsrXm5Q0whX3mo5/shrLR1E1CV08RZV7s/tblnU4iDhJR614Beh>
> - Information needs to stay updated so that developers and auditors can use it properly

Done. All additions have been made and we are fully up to date.

> Potential bonus goal: Integration of Soroban Disassembler

Done. <https://github.com/Inferara/soroban-ret>. You can access it from the Dev Tools button on the
menu.

### 2026 Q3

<!-- Commitment titles intentionally match Proposed Deliverables for automatic pairing. -->
<!-- markdownlint-configure-file { "MD024": { "siblings_only": true } } -->

#### Ongoing maintenance budget (100%)

As stated in our previous application for Q3
[#104](https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/pull/104)
we have focused on ongoing maintenance exclusively. This meant that we ensured that the Portal was
running and delivered details of publicly available audit reports.

**Reports**: As audits were reported via the audit bank (or other sources) we have added them to the
database to match the
[Public Audit Bank list](https://airtable.com/appsrXm5Q0whX3mo5/shrLR1E1CV08RZV7s/tblnU4iDhJR614Beh).

**Audits/vuln logging**: From the audits we have added detailed and individual additions of each
audit finding. These include all original details from the reports, enhanced with public links, clean
code blocks and status updates on the finding where relevant.

Recently added reports:

| Protocol / report name                                                              | Auditor              | # of findings | Original PDF pages |
| ----------------------------------------------------------------------------------- | -------------------- | ------------- | ------------------ |
| [Moonlight (Moonlight core)](https://stellarsecurityportal.com/report/78)           | Runtime Verification | 15            | 66                 |
| [Matrixdock (RWA Audit)](https://stellarsecurityportal.com/report/80)               | Runtime Verification | 9             | 89                 |
| [Matrixdock (Gold / xUAM)](https://stellarsecurityportal.com/report/79)             | Ottersec             | 5             | 14                 |
| [Centiiv (Protocol Contracts V1)](https://stellarsecurityportal.com/report/81)      | Veridise             | 11            | 24                 |
| [Sodax (Soroban Smart Contract Audit)](https://stellarsecurityportal.com/report/82) | Hashlock             | 8             | 33                 |
| [Peridot Finance (Peridot Protocol)](https://stellarsecurityportal.com/report/83)   | Halborn              | 67            | 242                |

It should be noted that as always some reports require more effort and scrutiny to review than
others. From these reports the Peridot Finance audit required the most review and edits. With 67
findings and 242 pages in the report it was the most time consuming to review and prepare for
submitting to the portal.

#### New Features

There have been other small improvements but the most notable is that we have removed the log-in
requirements for accessing & downloading audit reports.

## Proposed Impact

We hope that although there are not thousands of daily users, the few that do use the portal can
continue to rely on quality information to learn and keep Stellar secure. With the addition of a
maintained browser IDE, the portal grows from a place to _learn_ from audits and vulnerabilities into
a place to _build and test_ contracts with security tooling close at hand. Having a curated knowledge
base and working development tools in one location makes auditors, developers, users and curious
minds (and bots) smarter.

## Proposed Deliverables

| Budget allocation | Reserved |
| ----------------- | -------- |
| Maintenance       | $12,000  |
| Other             | $28,000  |
| **Total**         | $40,000  |

Following the program's budget allocation model, maintenance is funded as reserved capacity rather
than a task list: report ingestion volume, security fixes and toolchain updates cannot be costed in
advance, so what we declare up front is the share of the award held for it. The named deliverables
below (IDE adoption, UI and UX reworks) make up the **Other** share. Our Q4 deliverables submission
will open with this table extended with an **Actual** column.

Following our previous maintenance quarter, we had time to appropriately consider how to improve the
Security Portal in a meaningful way. Earlier this year we added the
[dev-tools](https://stellarsecurityportal.com/dev-tools) section. We have seen several attempts at a
browser IDE for Stellar, but most have had short lifespans or fallen out of maintenance; the most
active alternative, [Soroban Studio](https://github.com/zinct/soroban-ide), is a volunteer effort
with sporadic maintenance. Instead of building yet another half-baked IDE, we would like to adopt,
integrate and maintain the IDE originally built by James Bachini,
[SoroPG](https://github.com/jamesbachini/Soroban-Playground), and improve upon it where possible.

Alongside that, as usual we plan to stay up to date on audit reporting and logging findings in an
accessible and organized manner as well as general UI/UX improvments. We also anticipate a larger
number of reports becoming publicly available this quarter, which will require further review.

### 1. IDE adoption and integration into dev-tools ($20,000 - Other)

This is the main part of our Q4 application.

[SoroPG](https://github.com/jamesbachini/Soroban-Playground) is, to our knowledge, the only viable
browser-based IDE for Stellar smart contract development. It lets developers write multi-file Rust
contracts, compile to WASM, run unit tests and Scout security checks in sandboxed containers, deploy
to testnet/futurenet/mainnet, and inspect and invoke deployed contracts without local setup. It was
originally built by James Bachini and proposed to this program earlier this year (see the
[SoroPG project page](https://scf-public-goods-maintenance.github.io/projects/soropg)). It was well
received and saw a good amount of traction at the time. We believe this was since it was an easily
accessible online IDE available to Stellar developers, and the walkthrough videos definitely helped
in promoting it!

We want to continue parts of this project and maintain it for future developers. Rather than letting
this infrastructure fade, our team will adopt SoroPG (MIT licensed), credit James as its original
author, and integrate it into the Security Portal's dev-tools section alongside soroban-ret. We
welcome involvement from community members who contributed to or used the original project.

**Why this belongs on the Security Portal.** SoroPG is a natural fit for a security-focused developer
hub. It already integrates the Scout security-audit checks in its build sandbox, and its contract
explorer pairs well with our soroban-ret decompiler. A user could inspect a deployed contract,
decompile it, and cross-reference its behavior against known vulnerability patterns in our database.
Combining an IDE, a decompiler and a curated vulnerability knowledge base in one place is, as far as
we know, unique in the ecosystem.

To be clear we intend for each of these tools to be available on the portal, but linking their
features together would be a future endeavor.

**Expected Users:**

- **New developers:** Developers coming to Stellar for the first time often have no local Rust
  toolchain. A browser IDE removes the multi-GB install - rustup, cargo, the wasm target, Node.
- **Hackathon teams and workshop participants** are a plausible audience as well: zero-setup
  prototyping suits short, timed events. We see events such as bootcamps and hackathons as potential
  starting points to gauge interest.
- **Experienced teams** wanting quick iteration, reproducible examples for bug reports, or demos
  without environment setup.

Since Stellar is shipping protocol updates on a frequent basis, each protocol upgrade brings SDK and
tooling changes that a browser IDE should track to stay useful. The budget therefore covers five
threads of work:

1. **Availability and compatibility:** Hosting, uptime, and continuous updates to track the current
   state of Stellar, Soroban SDK releases, RPC changes, and compatibility with external libraries.
2. **Ongoing improvements:** improved editor experience, example workspaces and mini-lessons for
   users to get started. Issues and features can be posted publicly and adjusted with community
   feedback.
3. **Portal integration:** Embedding the IDE into the dev-tools section of the Security Portal with a
   consistent look and feel, shared navigation, and links between the IDE, the decompiler and
   relevant vulnerability entries.
4. **Community involvement:** We explicitly want to leave room for community members, especially
   those who used similar IDEs before. We hope they provide feedback, ideas and open-source
   contributions.
5. **Migration path:** To make sure the IDE is an on-ramp rather than a dead end, we will create a
   path for developers to bring their progress elsewhere like their local machine.

Maintaining a tool that acts as an entry point for new developers while supporting existing ones and
making it available on the ecosystem's security knowledge base lowers the barrier to building on
Stellar while keeping security visible from the very first contract a developer writes.

For future features, having a combination of vulnerability findings, the IDE and the soroban-ret tool
available in one place and integrated into a tool suite could be quite powerful for new and existing
developers.

### 2. UI design rework ($8,000 - Other)

With the addition of the IDE to the dev-tools section, we also want to improve the existing layout
and design of the portal. The website is functional, with filtering and detail pages for reports,
findings, auditors, companies and protocols. However several features and capabilities are not easily
discovered by users, and information could be organized in a cleaner, more streamlined way across
company profiles, audit reports and data presentation.

We have recently met with one of our power users for a small feedback session which already brought
some good insights and starting points. We plan to implement the suggestions where it is possible!

To handle these design changes consistently and with functionality in mind, we plan to allocate part
of the budget to a part-time external design contributor working with our team.

Concrete areas for improvement:

- **How individual findings are accessed and displayed.** The vulnerabilities page already supports
  filtering by severity, category, tags, protocols, companies, auditors, source and date range, but
  the density of the filter bar and card layout makes it hard for newcomers to know where to start.
  We want clearer defaults, better grouping, and more context per finding card.
- **Report pages.** A report page currently shows headers, a severity breakdown, the findings list
  and the PDF report link. We want to consider showing other useful information we already have
  without overwhelming users instead of presenting just a name, a date and a PDF cover.
- **General user experience.** Navigation between related entities (protocol → auditor → report →
  finding) works, but the paths are not obvious. We want to make discovery of features such as
  bookmarks, ratings, discussion threads and sharing more intuitive.
- **Further UI improvements** identified with the designer as the work progresses and as we receive
  more feedback from users and community members.

### 3. UX rework: accessing information and contributing as an individual (included in above budget)

Related to the UI rework, the idea here is looking at how users _access_ information and how they can
_contribute_ to it:

- **Accessing information.** We plan to improve the home page and entry points so that recent
  findings, relevant reports and severity distributions are easier to discover.
- **Contributing as an individual.** Navigator and Pilot role holders can add reports and findings,
  and anyone can flag content or comment. Uptake has been lower than hoped, which we attribute partly
  to discoverability and partly to friction in the submission forms. We want to make it easier to
  contribute with guided forms that pre-fill what can be pre-filled, and a review flow that gives
  contributors visible feedback on the status of their submission. Human review remains the standard
  for every finding published on the portal.

### 4. Ongoing maintenance & reporting budget ($12,000 - Maintenance Reserve)

Similar to previous rounds, part of the budget will be held as a maintenance reserve for both the
Portal and the contents (audit reports & vulnerabilities) hosted there. As always, we want to ensure
that we have as much up to date information on the portal as possible. Adding individual findings is
time consuming and requires thoroughly checking each vulnerability for consistency. Reports vary
greatly in size (for example, the Peridot–Halborn report contains 67 findings across 242 pages), so
it is difficult to predict the workload ahead of time.

Recently what also makes demand even harder to predict is that many audits are marked as completed or
remediating in the
[Public Audit Bank Airtable](https://airtable.com/appsrXm5Q0whX3mo5/shrLR1E1CV08RZV7s/tblnU4iDhJR614Beh)
without a publicly available report (or with dead links!). There are currently **24** such reports
for 2026. Part of our maintenance time is spent actively hunting down these reports and confirming
whether the source is intentionally withheld, which means contacting auditors and project teams
directly. For Halborn reports, we are currently waiting on 3 audits to see whether they will become
publicly available. If they do (which I am advocating for), the workload increases further.

Because we expect a potential influx of reporting work and cannot foresee the size of incoming
reports, we have increased the maintenance allocation slightly, up to $12,000 compared to the
previous quarter.

Beyond report ingestion, this budget covers the usual routine upkeep such as keeping the
vulnerability database in sync with the Public Audit Bank, reviewing community submissions and
corrections from contributors, dependency and security updates across the backend and UI, and the
usual operational costs of hosting.

## Metrics loaded from PG Atlas

[![PG Atlas](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Asoroban_security_portal&query=%24.activity_status&label=PG+Atlas&color=914CFF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Asoroban_security_portal)
[![90d Contributors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Asoroban_security_portal&query=%24.active_contributors_90d&label=90d+Contributors&color=00B578)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Asoroban_security_portal)
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Asoroban_security_portal&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Asoroban_security_portal)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Asoroban_security_portal&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Asoroban_security_portal)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.

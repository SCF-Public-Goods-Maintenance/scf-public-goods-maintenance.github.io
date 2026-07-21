---
title: "Stellar Security Portal"
parent: Public Good Projects
proposal_issue: 58
proposer: SurfingBowser
category: "Developer Experience"
budget: "10,000"
---

# Stellar Security Portal

A Soroban specific knowledge base which lets users access audits, individual vulnerabilities and code
in an organized fashion.

|                      |                                                                                                    |
| -------------------- | -------------------------------------------------------------------------------------------------- |
| **Category**         | Developer Experience                                                                               |
| **Website**          | <https://sorobansecurity.com/>                                                                     |
| **Repository**       | <https://github.com/inferara/soroban-security-portal>                                              |
| **First Released**   | July 2025 (website) September 2025 (all milestones)                                                |
| **Intake**           | <https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/issues/22> |
| **Budget Requested** | 10,000                                                                                             |

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

Over the past 3 months we have added many new features, quality of life improvements and opened up
more ways for community members to contribute. You can see more details in our two recent Medium
Articles:

- How the Portal is Evolving:
  <https://medium.com/@inferara/how-the-soroban-security-portal-is-evolving-5a37cb674217>
- June Update:
  <https://medium.com/@inferara/stellar-security-portal-update-whats-new-in-june-2026-f4b4f19fd953>

The total # of vulnerability findings has reached **840** (+253 since last quarter).

The Stellar Security Portal is now fully up to date on publicly available reports & findings from the
Public Audit Bank: <https://airtable.com/appsrXm5Q0whX3mo5/shrLR1E1CV08RZV7s/tblnU4iDhJR614Beh>

If you notice any missing reports or findings on the Portal please let us know.

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
   Y total" views, plus an admin/moderator Statistics dashboard. Commit `6f7c1e5` (<https://github.com/inferara/soroban-security-portal/pull/171> / <https://github.com/inferara/soroban-security-portal/pull/172>); design
   spec `docs/superpowers/specs/2026-05-27-visitor-analytics-design.md`.

4. **Audit-report ingestion** — background worker fetches PDFs, extracts metadata and
   vulnerabilities, and creates moderation-queue "agent runs" for review. Commit `394d872` (#187).

   Although this introduces some AI elements I want to stress that I have personally used it for
   making the **process** of adding vulnerability findings to the Portal much more efficient. The
   agents can be very much hit or miss when it comes to the accuracy of parsing reports. Having a
   dedicated admin page to log multiple findings at once with some minor things pre-filled such as
   severity and titles does save some time. I still manually review line by line the findings and
   compare them to the original report with manual edits. **We are not relying on AI to log findings
   to the Portal!**

5. **Stellar Security Portal rebrand + design refresh** — renamed from Soroban Security Portal, new
   designs with light & dark mode toggle. Commit `bd1ffd1` (<https://github.com/inferara/soroban-security-portal/pull/173>).

6. **Protocol/auditor 1–5 star ratings** — public star ratings with reviews. Commits `baf49eb`
   (#169), `896817d` (#81/#178).

7. **OpenGraph report-summary cards** — social link previews now render audit stats instead of raw
   PDF covers. Commit `f06e16d` (<https://github.com/inferara/soroban-security-portal/pull/191>).

8. **Performance work** — report cover compression, faster vulnerabilities/reports pages, caching.
   Commits `ed0d0f8` (<https://github.com/inferara/soroban-security-portal/pull/176>), `0b778e2` (<https://github.com/inferara/soroban-security-portal/pull/182>).

9. **Navigator Contributions** — We have enabled Navigators to participate in the Portal. You can
   read more about the changes on Medium:
   <https://medium.com/@inferara/how-the-soroban-security-portal-is-evolving-5a37cb674217>

## Proposed Impact

We hope that although there are not thousands of daily users, the few that do use it can continue to
rely on quality information to learn and keep Stellar secure.

The benefit for Stellar should be quite clear. The more people aware and using the Portal to learn
from audits and vulnerabilities (with detailed explanations) the better! Having a curated knowledge
base for auditors, developers, users and curious minds makes people (and bots) smarter.

## Previous Deliverables

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
- **Social sharing buttons + OpenGraph meta tags**: commit `1925219` (<https://github.com/inferara/soroban-security-portal/pull/120>). This is an easy way to
  share information on reports or findings with an automated image render which includes details
  like # of findings, severity levels and fix %. Works in discord on x and likely a few other places!
  Please try it out!

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

## Proposed Deliverables

As the Stellar Security Portal is in a good place now, we will focus our attention towards continued
maintenance and small improvements. As we are currently caught up on all publicly available audit
reports we plan to keep it that way.

### Ongoing maintenance budget (100%)

The majority of the budget request will go towards ongoing maintenance for both the Portal and the
contents (audit reports & vulnerabilities) which are hosted there. As always we want to ensure that
we have as much up to date information as we can on the portal. Adding individual vulns is time
consuming and requires thoroughly checking each vulnerability for consistency.

### New Features

New features are currently being supported through the Drips & Grantfox campaigns. Layout adjustments
or code fixes are covered under the regular maintenance tracking budget.

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.

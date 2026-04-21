---
title: "Soroban Security Portal"
parent: Public Good Projects
proposal_issue: 58
proposer: SurfingBowser
category: "Developer Experience"
budget: "50,000"
---

# Soroban Security Portal

_A Soroban specific knowledge base which lets users access audits, individual vulnerabilities and
code in an organized fashion._

|                      |                                                                                                    |
| -------------------- | -------------------------------------------------------------------------------------------------- |
| **Category**         | Developer Experience                                                                               |
| **Website**          | <https://sorobansecurity.com/>                                                                     |
| **Repository**       | <https://github.com/inferara/soroban-security-portal>                                              |
| **First Released**   | July 2025 (website) September 2025 (all milestones)                                                |
| **Intake**           | <https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/issues/22> |
| **Budget Requested** | 50,000                                                                                             |

## Project Description

The Portal was created to have a curated knowledge base of audit reports, code & individual
vulnerabilities available in one location. Before the portal, a lot of information was scattered
across protocols, blogs, socials and discord channels making it hard to access and learn from. Users
can find individual reports which are indexed, organized and even broken down by individual findings!
Semantic search and tagging is also quite useful.

Each vulnerability has been manually added & scrutinized by us to maintain accuracy, only adding
additional links and resources such as PRs or repos.

Vulnerabilities: 587 Reports: 52 Protocols: 44 Auditors: 11

It is useful for auditors, devs, new users to soroban and even AI bots who can digest the data.

## Team & Experience

Dominik Github: [https://github.com/SurfingBowser](https://github.com/SurfingBowser) Discord:
Tacotamer / AndyKaufman

I have been involved with Stellar for more than a year at this point. Have contributed to the
Security Portal & Inference programming language.

For the portal I have manually written and reviewed a large portion of the vulnerabilities on the
portal. Actively vote in SCF rounds, try to give feedback to applying teams and recently have been
trying to attract other development teams to the Stellar network (such as the recent large tech
events I attended in Tokyo & Osaka). Looking forward to dedicating more time towards the Portal
again!

We are also adding a new dedicated team member Andrew!

Andrew Github: [https://github.com/AKercha1](https://github.com/AKercha1)

Andrew will be joining us as a new team member to help maintain and improve the portal in the coming
months. He has spent time and worked with Georgii previously and will be a needed addition to our
team. Focus will be on improving the existing features of the security portal as well as reviewing
and adding to the recent contributions by other contributors.

Georgii has done work previously on the Portal but is currently committed to other projects.

## Retroactive Impact

To be transparent, the past 3 months have not seen as much activity. Our initial SCF grant for the
portal had the final milestone completed in September (2025) but we continued to improve it with
features, reports and individual vulnerability logging until the end of January 2026. So let’s look
at it from a larger timeframe instead starting with September.

**(Note: this list was created by AI tools to summarize changes from commit data after final
milestone completion to this week. I have reviewed and made manual edits.)**

## 1. Advanced Vulnerability Classification & Filtering

Implemented a method for providing more nuance to findings. This was a result of community feedback
and requests from **SDF** during **Meridian**.

### Higher-Level Categories

Vulnerabilities are now classified into five distinct categories to clarify their status:

- **Valid:** Confirmed by the protocol team and fixed.
- **Valid Not Fixed:** Acknowledged but remains unpatched at the time of the report.
- **Valid Partially Fixed:** Only some aspects of the finding or proposed fix were addressed.
- **Invalid:** Findings that were ultimately debunked but are included for transparency in the
  report.
- **N/A:** Reserved for best practice recommendations that are not direct vulnerabilities.

### Search & Visibility

- A new filter was added to the main vulnerabilities search page to allow users to sort by these
  categories.

---

## 2. Infrastructure & New Detail Pages

Added more depth to the reports and information presented on the portal by implementing dedicated
detail pages for every entity in the ecosystem. This allows for deep-linking and better
cross-referencing.

- **New Entities:** Launched dedicated detail pages for **Reports**, **Vulnerabilities**,
  **Auditors**, **Protocols**, and **Companies**.
- **Direct Linking:** Every entry (e.g., a specific vulnerability or a protocol's security history)
  now has a unique URL, enabling users to share direct links to specific data points.

---

## 3. User Experience & "Quality of Life" Improvements

Several updates focused on making the portal more robust for contributors and frequent users:

- **Markdown Preview:** Added a vulnerability description preview on the "Add" and "Edit" pages. This
  allows contributors to verify formatting before submission.
- **Session Persistence:**
  - Implemented **localStorage** for user sessions to prevent frequent logouts when opening new
    browser tabs.
  - Implemented **sessionStorage** for form data (Issue 45, ensuring that input is not lost if a user
    accidentally refreshes the page (F5).
- **Semantic Search Enhancements:** A new unique link button (**⛶**) was added to the vulnerability
  information panel to quickly copy the entry's URL.

---

## 4. Personalization: The Bookmarking System

To help developers track specific security issues, a bookmarking feature was introduced:

- **Functionality:** Logged-in users can bookmark vulnerabilities and reports for future access.
- **UI Integration:** A golden bookmark icon identifies saved items. A new dropdown menu in the
  top-right navigation provides quick access to bookmarks.
- **Profile Integration:** A full list of bookmarks is now manageable via the user's profile page.

---

## 5. Technical Refactoring & Bug Fixes

A series of targeted fixes addressed security, flow, and UI consistency:

- **Authentication Refactor (Issue 41):** Overhauled how authentication is handled to prevent
  unauthenticated users from accessing "Add Report" forms, which previously led to data loss upon the
  login prompt.
- **Improved Submission Flow (Issues 42 & 43):** Added clearer requirements and error messages for
  report submissions. The system now better handles scenarios where a company or auditor involved in
  a report has not yet been added to the portal's database.
- **UI Layout Fixes (Issue 40):** Fixed sizing issues with the bookmarks dropdown where content would
  occasionally overflow its borders.
- **Backend & Profiles:** Recent work includes extending user profiles with bios, social links, and
  expertise tags, as well as fixing backend Dependency Injection (DI) issues related to the protocols
  section.

Since then the time committed was for the participation in the Drips campaigns, the first wave of
which was quite time consuming with mixed results. The following waves were much smoother but
contributions need to be properly reviewed and built out further. I will mention our plan for this in
a later section.

## Past Deliverables

N/A

## Proposed Impact

For our impact goals we plan to focus on awareness, acquiring new users and improving social features
of the portal.

I believe logging and maintaining audit data for Stellar projects is a necessary task to keep the
network safe, give existing developers & auditors access to this data (free of charge!) and of course
making people aware of it!

For awareness and acquiring new users, I am envisioning mini demo and walkthrough sessions where we
educate people about the Portal, show them how to use it and what makes it useful. We’ve also
discussed having report review sessions with protocols that have been audited to discuss their
experience and discuss specific vulnerabilities that were discovered in order to serve as a way for
other developers to learn from the audit process. I’ve spoken to Alberto from Trustless Work about
this and hope to plan an actual session. This would likely be available on X and/or a youtube stream.

Adding new features to the security portal in the form of social & public actions of users could help
with building awareness as well. This could be things such as a voting system, display counter for #
of bookmarks on issues or even page visits to individual reports.

The benefit for Stellar should be quite clear. The more people aware and using the Portal to learn
from audits and vulnerabilities (with detailed explanations) the better! Having a curated knowledge
base for auditors, developers, users and curious minds makes people (and bots) smarter.

## Proposed Deliverables

We have received some requests which we plan to carry out:

1. Changing the name & scope to “Stellar Security Portal” to improve Stellar branding.
2. Including as many listed Audits as possible to portal
3. Adding publicly visible (bot filtered) visitor analytics to reports and projects pages.

Aside from the above, here are our current thoughts on the structuring of the grant breakdown and
plans for deliverables.

### Retroactive budget (30%)

- We have continued to update the portal even after all milestones were completed
- Added more reports as they arose (until about end of January)
- More features for displaying data, added individual protocol pages
- A more detailed list has been shared in the retroactive impact section. To see a list of our commit
  changes you can check the
  [Github history directly](https://github.com/Inferara/soroban-security-portal/commits/main/)

### Ongoing maintenance budget (40％）

We want to ensure that we have as much up to date information as we can on the portal. Adding
individual vulns is time consuming and requires thoroughly checking each vulnerability for
consistency.

- Audits/vuln logging: As audits are performed via the audit bank (or others) we plan to have the
  database maintained to match the
  [Public Audit Bank list](https://airtable.com/appsrXm5Q0whX3mo5/shrLR1E1CV08RZV7s/tblnU4iDhJR614Beh)by
  the end of July. (pending timing of new additions)
- Information needs to stay updated so that developers and auditors can use it properly

### New features & milestones (30%)

- Increased community engagement
  - Tutorial / onboarding sessions in discord, starting videos etc
  - Gather more input and feedback from users and stellar community
  - Increase the amount of contributors to the portal for sourcing of reports, adding vulns and
    sharing experiences (such as comments on vulns)
- Use the feedback gathered to make informed decisions on new features to add to the portal
- Social / community aspects (many issues listed on Github directly)
  - Leaderboard? Or some info stat page of most viewed vulnerabilities (bookmarked?) etc.
  - Being able to +/- system for vuln
  - Ability for community members to submit corrections on vulns
  - More public data visible such as # of page views, downloads of reports etc.
- More advanced API features in order to support other projects & inform users of the portal

Potential bonus goal:

Integration of Soroban Disassembler

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.

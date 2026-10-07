---
title: "Stellar Security Portal"
parent: Public Good Projects
proposal_issue: 58
proposer: SurfingBowser
category: "Developer Experience"
budget: "40,000"
---

# Stellar Security Portal

A Stellar specific knowledge base which lets users access audits, individual vulnerabilities and code
in an organized fashion, together with a growing dev-tools section.

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

A Stellar-specific knowledge base which lets users access audits, individual vulnerabilities and code
in an organized fashion, together with a growing dev-tools section. The portal currently hosts
[soroban-ret](https://github.com/Inferara/soroban-ret), a tool for disassembling Soroban contracts
and inspecting on-chain bytecode, and this quarter we propose to add a full browser IDE alongside it.

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

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.

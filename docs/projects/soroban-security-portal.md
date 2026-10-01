---
title: "Stellar Security Portal"
canonical_id: daoip-5:scf:project:soroban_security_portal
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

Current State of the Portal as of Oct 1st 2026

**Vulnerabilities**: 954 \
**Reports**: 66 \
**Protocols**: 57 \
**Auditors**: 15

It is useful for auditors, devs, new users to soroban and even AI bots who can digest the data.

## Team & Experience

Dominik Github: [https://github.com/SurfingBowser](https://github.com/SurfingBowser) Discord:
AndyKaufman

I have been involved with Stellar for almost 2 years at this point. Have contributed to the Security
Portal & Inference programming language as well as the Reverse Engineering Tool. Recently have acted
as an open track delegate.

For the portal I have manually written and reviewed a large portion of the vulnerabilities on the
portal. I actively vote in SCF rounds, try to give feedback to applying teams and recently have been
trying to attract other development teams to the Stellar network. Looking forward to dedicating more
time towards the Portal again!

Andrey Github: [https://github.com/AKercha1](https://github.com/AKercha1)

Andrey has joined us as a new team member to help maintain and improve the portal. He has spent time
and worked with Georgii previously and has been a needed addition to our team.

His focus has been on improving the existing features of the security portal as well as reviewing and
adding to the recent contributions by other contributors.

Andrey has also helped with managing parts of our Grantfox & Drips campaigns as well.

Georgii has done work previously on the Portal but is currently committed to other projects, when
able he checks vulnerability findings that are logged to the Portal for a second pair of eyes before
they are approved for public view.

## Retroactive Impact

Over the past 3 months we have continued with report logging and general maintenance for the Security
Portal. Dominik also participated in a Drips interview alongside the StellarRoute team. There is not
much to report besides small we are still working on things as expected!

## Past Deliverables

As stated in our previous application for Q3
[#104](https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/pull/104)
we have focused on ongoing maintenance exclusively. This meant that we ensured that the Portal was
running and delivered details of publicly available audit reports.

### 2026 Q3

- **Reports**: As audits were reported via the audit bank (or other sources) we have added them to
  the database to match the
  [Public Audit Bank list](https://airtable.com/appsrXm5Q0whX3mo5/shrLR1E1CV08RZV7s/tblnU4iDhJR614Beh).

- **Audits/vuln logging**: From the audits we have added detailed and individual additions of each
  audit finding. These include all original details from the reports, enhanced with public links,
  clean code blocks and status updates on the finding where relevant.

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

- **Other changes**: There have been other small improvements but the most notable is that we have
  removed the log-in requirements for accessing & downloading audit reports.

## Proposed Impact

We hope that although there are not thousands of daily users, the few that do use it can continue to
rely on quality information to learn and keep Stellar secure.

The benefit for Stellar should be quite clear. The more people aware and using the Portal to learn
from audits and vulnerabilities (with detailed explanations) the better! Having a curated knowledge
base for auditors, developers, users and curious minds makes people (and bots) smarter.

## Metrics loaded from PG Atlas

[![PG Atlas](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Asoroban_security_portal&query=%24.activity_status&label=PG+Atlas&color=914CFF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Asoroban_security_portal)
[![90d Contributors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Asoroban_security_portal&query=%24.active_contributors_90d&label=90d+Contributors&color=00B578)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Asoroban_security_portal)
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Asoroban_security_portal&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Asoroban_security_portal)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Asoroban_security_portal&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Asoroban_security_portal)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.

---
title: Public Goods Award
has_children: true
nav_order: 3
---

# Public Goods Award

_This structure proposes [significant changes](/pg-award/2026q2-award-round.md) compared to previous
rounds._

## Overview

The SCF Public Goods Award supports the ongoing maintenance, security, documentation, and incremental
evolution of open-source public goods — tools, infrastructure, explorers, SDKs, and services that are
non-excludable, non-rivalrous, and broadly beneficial to the Stellar/Soroban ecosystem.

Managed as a community-driven program with increasing decentralization, the Award provides
predictable funding (up to $50K in XLM\* per proposal per quarter) based on demonstrated retroactive
impact, proposed maintenance/features, and objective metrics from [PG Atlas](/pg-atlas.md). Funding
combines retroactive rewards for past contributions with forward retainers tied to clear deliverables
and Service Level Objectives (SLOs).

The program evolves in stages, with the current focus on transitioning from soft-launch
centralization to data-informed, Pilot-governed processes. Continued funding requires validated
impact, multi-maintainer progress, and alignment with ecosystem needs.

## Award Structure

- **Cap**: Up to $50K in XLM\* per proposal per quarter (tunable based on PG Atlas scores and
  community signal in future stages).
- **Types**: Hybrid — retro rewards for proven impact + maintenance retainers for ongoing work (with
  SLO checkpoints).
- **Distribution**: Initial tranche post-approval; subsequent via milestone/SLO validation.
- **Reapplication**: Quarterly, with evidence of past deliverables and new ecosystem-aligned goals.

**Stages** (subject to community iteration):

- **Current** (transition): GitHub-issue intake, Pilot eligibility quorum, Metric Gate context,
  Tansu-based voting experiment.
- **Future** (hypothetical): Full on-chain treasury, streamed payouts, broader plural streams (e.g.,
  dependency-matching pool).

## Eligibility Criteria

Projects must:

- Be open-source and clearly non-excludable/non-rivalrous.
  - Some exceptions to FOSS are possible for free-to-use permissionless services such as block
    explorers.
- Demonstrate ecosystem-wide value (e.g., multiple dependents via PG Atlas).
- Have transparent maintenance (pony factor tracking, progress toward multi-maintainer).
- Meet basic due diligence (no sanctions, legal compliance — coordinated minimally via SDF if
  needed).

**New project intake**:

- Submit templated GitHub issue in this repo ("New PG Proposal" template).
- Require simplified Pilot quorum: Minimum 3 thumbs-up reactions; each thumbs-down requires 2
  additional thumbs-up to override (formula: `required_ups = 3 + 2 × downs`).
- Discussion period: ≥1 week.
- Approved issues advance to full proposal.

Existing/returning projects may resubmit directly with impact updates.

## Program Phases

1. **Proposal Initiation**: Open GitHub issue (new) or update existing project page for returning
   projects.
1. **Community Discussion**: Async feedback in issue (Discord may be used to discuss, but recaps are
   posted to GitHub).
1. **Eligibility Quorum**: Pilots signal via reactions (see [Eligibility](#eligibility-criteria)).
1. **Full Proposal**: Submit detailed project page in PR, with impact evidence, SLOs, and a budget
   breakdown.
1. **Metric Review**: PG Atlas scores published for context.
1. **Voting Round**:
   1. Proposals are added to Tansu and link to project pages.
   1. Tansu-based NQG vote (see [Tansu Modifications](/pg-award/tansu-modifications.md)).
1. **Award Distribution**: Tranches tied to approval + milestones/SLOs.
1. **Resubmission**: Quarterly with progress reports.

## Public Good Categories

Additional categories may be added based on community discussion. Generally, the SCF Public Goods
Award will not support educational categories but exceptions can be made for Developer Experience
tools.

| Category                  | Purpose                                                                                             | Eligibility Rationale                                                                     | Examples            |
| ------------------------- | --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ------------------- |
| SDKs                      | Maintain SDKs in popular programming languages to enable easier Stellar integration.                | Core ecosystem infra required by developers for app and protocol development.             | Python Stellar SDK  |
| Data Support              | Provide dashboards, indexers, or APIs to expose Stellar data, analytics, or insights.               | Supports visibility, growth tracking, and transparency across the ecosystem.              | Dune Dashboards     |
| Wallet Support            | Develop shared wallet tooling or starter kits to reduce dev effort and improve UX.                  | Encourages better wallets and faster onboarding; critical for adoption.                   | Stellar Wallets Kit |
| Developer Experience      | Tools that enhance productivity and access for smart contract, backend, or frontend devs.           | Lowering friction in building on Stellar improves ecosystem velocity.                     | Solang Compiler     |
| Ecosystem Visibility      | Surface projects, developer activity, use cases, and funding history in the ecosystem.              | Transparency drives engagement, investor interest, and governance participation.          | Stellarlight.xyz    |
| Infrastructure Monitoring | Tools for observing validators, node status, uptime, or key protocol signals.                       | Ensures network reliability and decentralization monitoring.                              | Stellarbeat         |
| Governance Tools          | Public interfaces, analytics, or coordination tools to support voting and participation.            | Supports decentralization and open participation in funding or protocol-level governance. | Soroban Governor    |
| Security & Auditing Tools | Build or maintain tools that help identify, prevent, or analyze vulnerabilities in smart contracts. | Increases trust and reduces systemic risk for DeFi or financial tooling on Stellar.       | Fuzzing Framework   |

## Changes to General Rules

(Adapted from current rules — publicity consent, disclaimers, privacy policy linkage preserved;
centralized Council references removed and replaced with community processes.)

**Open Questions**:

- Tune $50K cap to metric-based bands?
- Formalize SLO templates per category?
- KYC scope in decentralized intake?
- Do we need the simplified new project intake vote to be anonymous?
- How to open up eligibility for widely used infra that can be monetized, but needs awards on the
  road to financial sustainability?

This page reflects a transition design as of February 2026 — evolving via repo PRs.

_See sub-page: [Tansu Modifications](/pg-award/tansu-modification.md) for Tansu pilot details._

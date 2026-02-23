---
title: 2026 Q2 Award Round
parent: Public Goods Award
nav_order: 1
---

# 2026 Q2 Award Round

## New Award Structure

### Why Change?

The current soft-launch Public Goods Award runs as a quarterly program with proposals submitted via
Airtable and voting on Soroban Governor (testnet, snapshot proposals only). Awards are up to $50K in
XLM per proposal per quarter, distributed in two 50% tranches—the second contingent on deliverable
completion review by a Council (currently Anke, Justin, Gemma). Proposal intake is not
open-application; projects must be pre-approved by an SDF contact before submitting. Voting is open
to SCF Pilots using NQG scores, with quorum and approval thresholds.

This structure has been an important starting point, and we want to build on its strengths. The
working group has identified limitations that the new model aims to address:

- **Noisy impact signals.** There is no systematic way to assess usage, dependencies, or criticality.
  Funding decisions rely heavily on self-reported narratives, making it hard to distinguish
  high-impact infrastructure from low-adoption tools.
- **Concentration risk.** Several widely-used tools have a single active maintainer (pony factor =
  1). The current process does not surface or track this risk, leaving the ecosystem vulnerable to
  key-person failures.
- **Limited Pilot engagement.** The current voting process is fairly detached—Pilots vote on
  proposals but have limited structured interaction with the projects being funded. We want to create
  more opportunities for Pilots to engage directly with PG maintainers through discussion, review,
  and ongoing feedback.
- **"Everyone gets funded" drift.** Without objective baselines, there is pressure toward equal
  distribution rather than merit-based allocation. This underserves critical infrastructure and
  overserves marginal projects.
- **Weak forward-looking commitments.** The current structure includes deliverables and a second
  tranche gated on Council review, but there are no formal Service Level Objectives (SLOs) or
  structured community-driven accountability. Maintainers cannot commit to defined service levels in
  exchange for predictable ongoing funding.
- **Voting UX friction.** Soroban Governor does not support anonymous voting, so Pilots must use one
  identifiable address to propose and a separate address to vote without revealing their identity.
  This workaround is clunky and discourages participation.
- **Centralized intake and review.** Proposal initiation requires SDF pre-approval, and the Council
  holds sole veto and review authority. While appropriate for a soft launch, this creates bottlenecks
  and limits community ownership as the program scales.

### The Proposed Model

The working group proposes a **hybrid retroactive + maintenance retainer model** with a structured
decision stack that combines objective data, expert review, and community voice.

**Award cap:** Up to $50K in XLM per proposal per quarter (tunable based on experience).

**Funding types (per proposal, as applicable):**

| Stream                | Purpose                                    | Mechanism                                          |
| --------------------- | ------------------------------------------ | -------------------------------------------------- |
| Retro Rewards         | Recognize demonstrated past impact         | Performance-weighted, informed by PG Atlas metrics |
| Maintenance Retainers | Fund ongoing upkeep with clear commitments | Quarterly checkpoints tied to SLOs                 |
| Milestone Top-ups     | Support new development when eligible      | Tranche releases on milestone completion           |

**Decision stack (per round):**

1. **Metric Gate (objective filter)** — Each applicant's project is scored on objective signals from
   [PG Atlas](../pg-atlas/overview.md) (adoption, criticality, pony factor, etc.). The Metric Gate
   serves two roles: it filters intake so that only projects meeting a baseline threshold advance to
   review and voting, and it provides published context that reviewers and voters can reference when
   evaluating proposals. Metrics inform decisions—they do not determine them.
2. **Expert Review (qualitative)** — A panel of maintainers, security specialists, and dev-tools
   reviewers evaluates utility, reliability, and roadmap quality. Reviewers use PG Atlas data as one
   input alongside their own assessment.
3. **NQG Community Vote (legitimacy)** — Reputation-weighted community vote via
   [Tansu](https://tansu.dev), using NQG scores for sybil resistance and voice credit weighting. This
   is where funding decisions are made. Voters see metric scores, expert reviews, and proposal
   details to inform their vote. See [Tansu Modifications](tansu-modifications.md)

The working group's [consensus document](../pg-working-group.md) also envisions a fourth step—a
programmatic Budget Solve that combines metric, expert, and community signals with configurable
weights (proposed starting point: Metrics 50%, Experts 30%, NQG 20%) to optimally fit awards within
the available pool. This is a longer-term goal. For the Q2 experiment, the community vote is the
primary decision mechanism, with metrics and expert reviews providing structured input.

> Parameters will be tuned based on outcomes from each round, with post-round retrospectives
> published transparently.

**Program flow (per round):**

1. Projects submit proposals via GitHub issue (new projects) or update existing project pages
   (returning projects).
2. Community discussion and eligibility quorum (≥3 Pilot thumbs-up; each thumbs-down requires 2
   additional thumbs-up to override).
3. Full proposal with impact evidence, SLOs, and budget breakdown.
4. PG Atlas metric scores published for context.
5. Tansu-based NQG voting round (anonymous voting supported).
6. Award distribution: initial tranche post-approval, subsequent tranches tied to milestone/SLO
   validation.
7. Quarterly resubmission with progress reports.

**Public Good categories** include SDKs, data support, wallet support, developer experience,
ecosystem visibility, infrastructure monitoring, governance tools, and security/auditing tools. The
full category definitions and eligibility criteria are published in the
[Public Goods Award rules](../public-goods-award.md).

### What This Addresses

| Pain Point               | How the New Model Addresses It                                                                            |
| ------------------------ | --------------------------------------------------------------------------------------------------------- |
| Noisy signals            | PG Atlas provides objective metrics: dependency graphs, criticality scores, pony factor, adoption data    |
| Concentration risk       | Pony factor tracking surfaced in dashboard; multi-maintainer progress required for top-tier PGs           |
| Limited Pilot engagement | Structured discussion phases, expert review panels, and community-driven accountability via Tansu         |
| Funding drift            | Metric Gate filters marginal applications; published scores contextualize proposals for voters            |
| Weak forward commitments | Maintenance retainers with SLO checkpoints; milestone-gated tranche releases; community review of results |
| Voting UX friction       | Tansu supports native anonymous voting (BLS12-381); single-address voting with NQG weight integration     |
| Centralized intake       | Open GitHub-based intake with Pilot quorum; Council veto replaced by community-driven process             |

---

## Program Success Metrics

We define success at two levels: outcomes for the Q2 experiment specifically (April–June 2026), and
directional 2026 targets that the experiment starts us toward.

### Q2 Experiment Success Criteria

These are the measurable outcomes we commit to evaluating after the first round:

| Metric                             | Target                                                                                         | How Measured                    |
| ---------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------- |
| PG Atlas operational               | Graph with ≥100 project nodes and dependency edges live before voting opens                    | PG Atlas dashboard / API        |
| Metric context available           | Criticality scores, pony factor, and adoption signals published for ≥70% of applicant projects | PG Atlas scores endpoint        |
| First Tansu-based round completed  | At least one full funding round executed through the new process (proposal → vote → award)     | Tansu on-chain records          |
| Voter participation                | ≥30 unique voters using NQG-weighted votes                                                     | Tansu voting data               |
| Maintainer coverage                | ≥15 public goods funded across ≥5 categories                                                   | Award records                   |
| Post-round retrospective published | Transparent write-up of what worked, what didn't, parameter changes for next round             | Published to working group repo |

### 2026 Directional Targets

These are the full-year outcomes the working group is building toward. The Q2 experiment is the first
step; we do not expect to hit these numbers in one quarter.

1. **Coverage & reliability:** Fund ≥25 public goods covering 80% of ecosystem dependency weight;
   ≥95% SLO attainment for funded services.
2. **Risk reduction:** Reduce pony factor = 1 cases in top-10 critical PGs from ≥5 today to ≤1; add
   ≥2 active maintainers per critical repo.
3. **Signal quality:** PG Atlas live with auto-ingested SBOMs for ≥70% of SCF-funded projects;
   publish quarterly PG scorecards.
4. **Funding efficiency:** ≥70% of PG funding routed via metric-gated streams/retainers; ≤15%
   variance between requested and awarded budgets after rubric scoring.
5. **Community legitimacy:** ≥100 voters participating (direct + delegated) per round; ≥30 expert
   reviewers active; post-round satisfaction ≥8/10.

> We are intentionally transparent about the gap between Q2 targets and full-year ambitions. The
> experiment will generate the data we need to set realistic intermediate milestones for Q3 and Q4.

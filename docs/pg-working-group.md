## Maintenance of Public Goods

**Purpose**

Provide predictable, merit-based funding for the maintenance, security, documentation, and incremental evolution of Public Goods (PGs) – open-source tools and infra (SDKs, explorers, node/rpc components, dev tooling) that are non-excludable/non-rivalrous and broadly relied on across the Stellar ecosystem.

**Why this matters**

* Accelerates delivery: Reuse battle-tested components vs. re-inventing.  
* Reduces systemic risk: Avoid single-maintainer failure for critical libs/services.  
* Enables decentralization: Lowers barriers for new builders; spreads know-how beyond a few teams.  
* If underfunded: Higher dev cost, fragmented tooling, slower Soroban adoption, latent security risk, and loss of trust.

**Current state (today)**

* Quarterly Public Goods Award (on Soroban Governor testnet) ≈ retro/maintenance only; little speculative/new work.  
* Impact signals are noisy: unclear usage/dep graphs; marketing gaps vs. true low adoption.  
* Concentration risk: 1–2 maintainers carry widely used tools; limited sustainability beyond repeat grants; expectation drift (“everyone gets funded”).

**Five-Year North Star**

A community-run, data-driven allocator that funds ongoing maintenance for high-impact public goods, with clear Service Level Objectives (SLOs, the target level of service a team commits to internally (e.g., “99.9% monthly uptime,” “\<2h mean time to restore”)), robust documentation, visible dependency graphs, multiple active maintainers per critical tool, and near-zero effective fees for developers. Funding streams mix retroactive rewards with forward maintenance retainers tied to measured usage, resilience, and decentralization.

**2026 Outcomes (concrete & measurable)**

1. **Coverage & reliability:** Fund ≥ 25 PGs covering 80% of ecosystem dependency weight; ≥ 95% SLO met for funded services.  
2. **Risk reduction:** Reduce “pony factor \= 1” across top-10 PGs from ≥5 cases to ≤1; add ≥ 2 active maintainers per critical repo.  
3. **Signal quality:** Ship PG Atlas (live dependency \+ usage dashboard) with auto-ingested SBOMs (Software Bill of Materials — an itemized list of all components/dependencies in a software artifact) for ≥ 70% of SCF-funded projects; publish quarterly PG scorecards.  
4. **Funding efficiency:** ≥ 70% of PG funding routed via metric-gated streams/retainers; ≤ 15% variance between requested vs. awarded budgets after rubric scoring.  
5. **Community legitimacy:** ≥ 100 voters participating (direct+delegated) per round; ≥ 30 expert reviewers active; post-round satisfaction ≥ 8/10.

**Decentralization Opportunities (2026)**

* **Allocation decisions:** NQG-weighted community signal \+ Expert Councils across multiple streams (RetroPGF, Maintenance Retainers, Dependency-Matching Pool, Incident/Security Fund) via a community-run DAO tool (e.g., Tansu), with budget sizing vs. simple yes/no.  
* **Plural funding streams approach** (RetroPGF (performance weighted, quarterly) \+ Maintenance retainers tied to Service Level Objectives (SLOs) for critical OSS, Development Milestone topups as necessary and if eligible  
* **Multi-platform OSS Bounty Marketplaces:** Enable/support several bounty venues run by non-SDF coordinators; shared bounty spec (labels/scope/payout ranges/review SLA/SBOM link), monthly matching pool, and anti-sybil checks.  
* **Ops:** A Community Public Goods Working Group (DAO) coordinates intake, metrics collection, lightweight audits, post-mortems, and cross-stream budgeting. Metrics include ecosystem dependency graph, usage dashboards, and risk scores (e.g., Pony Factor) to guide allocations.  
* **Standards:** Publish a PG Sustainability Kit (SBOM workflow, SLO templates, incident runbooks, funding rubric), plus a shared metrics schema/API for usage & dependency tracking.

### Governance & Funding Design (reputation \+ experts \+ metrics)

**Decision stack (per round):**

1. **Metric Gate (objective):** Each applicant gets a PG Score (see below). Determines eligibility & baseline band.  
2. **Expert Review (qualitative):** Panel of maintainers/security/dev-tools reviewers scores utility, reliability, roadmap.  
3. **NQG Community Vote (legitimacy):** Reputation-weighted \+ quorum delegation ranks proposals within bands.  
4. **Budget Solve (programmatic):** Linear/knapsack fit within pool using weights: *Metrics 50% • Experts 30% • NQG 20%* (tunable).

**PG Score (example 0–100):**

* **Adoption (30):** direct dependents, on-chain calls, downloads (smoothed, Sybil-checked).  
* **Criticality (20):** dependency centrality, role in dev flows (e.g., SDK vs sample app).  
* **Reliability (15):** uptime/SLO, incident rate/MTTR.  
* **Security & Quality (15):** recent audits, CVE handling, test coverage, release cadence.  
* **Decentralization (10):** maintainers ≥2, reviewer diversity, open governance.  
* **Ecosystem Impact (10):** alignment with near-term roadmap (e.g., Soroban upgrades).

**Funding modes (plural):**

* **Maintenance Retainers** (streamed, quarterly checkpoints).  
* **Retro Rewards** (RetroPGF on realized impact and dependency).  
* **Milestone Top-ups** (for new development).

### Key stakeholders

* **PG maintainers** (SDKs, explorers, infra, libs).  
* **Dependent teams** (apps, wallets, anchors, DeFi, validators).  
* **PG Working Group** (Pilots \+ maintainers \+ SDF observers).  
* **Expert Council** (security, core, tooling, data).  
* **SDF Ecosystem & Data** (seeding, dashboards, ops support).  
* **External partners** (e.g., BlockScience/NQG; Gitcoin/Octant for co-rounds).

### Candidate mechanisms / tools (fit snapshot)

* **Hybrid Retro \+ Maintenance** → strong initial fit (rewards proven impact; funds forward work with SLO guardrails).  
* **Tansu** → run DAO ops, reviewer workflows, voting snapshots, streaming payouts; good near-term backbone.  
* **Fee-Pool usage (future)** → sustainable but requires broader consensus; target for later in 2026 / 2027

### 2026 Experiments (practical pilots)

1. **Stellar Public Goods DAO (beta on Tansu):** Run three quarterly funding rounds starting in Q2 (first quarter still on existing model). Hybrid model \+ the above decision stack; publish scorecards & post-mortems.  
2. **PG Atlas (metrics backbone):**  
   * SBOM CI GitHub Action (auto-submit to PG registry).  
   * Live dependency graph \+ usage/call metrics \+ “pony factor” risk.  
   * Public dashboard powering the Metric Gate.  
3. **Dependency-Match Bonus:** When SCF Build projects hit mainnet, this counts towards their top PG dependencies in RetroPGF  
4. **Decentralize Maintenance:** Bounty rewards specifically to top maintainers on high-importance repos; tracked via merged PRs/permissions.

### Dependencies & risks

**Dependencies:** reliable telemetry (on/off-chain), SBOM adoption, NQG runway, legal wrapper for streamed payouts (grants/contractor), reviewer pool.

**Risks & mitigations:**

* **Metric gaming** → multi-signal \+ anomaly flags \+ audits of top awards.  
* **Over-funding inertia** → caps, sunset clauses, re-bid retainers, mandatory score deltas.  
* **Maintainer concentration** → require documented onboarding of new maintainers for Tier-1 PGs.  
* **Process fatigue** → 1-page apps, auto-ingest metrics, predictable timelines.  
* **Security incidents** → incident-response grants, emergency hotfix funding lane.

### Open questions

1. **What’s in scope for a public good to be eligible**: strict infra/tooling only, or include “quasi-public goods” (e.g., Stellarcarbon-type services)?  
   1. [https://stellar.gitbook.io/scf-handbook/supporting-programs/public-goods-award/official-rules\#public-good-categories](https://stellar.gitbook.io/scf-handbook/supporting-programs/public-goods-award/official-rules#public-good-categories)   
2. **Baseline eligibility**: do we assign notional values by dependency weight vs. budget requests?  
   1. Open source software   
   2. But looking at broader scope, identify categories for comparable metrics. Things like Stallion, onchain components? Maintainer activity?  
   3. Maintenance vs adding new features   
      1. Should split budgets?  
3. **Best way to handle budget / award measures**  
   1. What about SDKs convo?   
   2. What about the DAO deciding the amount projects receive instead of voting on a budget? Similar to optimism.  
   3. We can also ask milestones to be more separated so that we could decide to partially fund work.  
   4. What about cancelling an award or even a clawback clause if no work was done.  
4. **Decision-making around the public good what’s needed**  
   1. Does the maintainer decide or the DAO?  
   2. DAO provide signal what the community is actually using.   
5. **Best practice Service Level Objectives (SLOs) per PG category** (SDK vs explorer vs RPC)?  
6. **Reviewer / DAO contributor incentives:** how to compensate experts without capture (fixed stipends? rotating panels? Fee pool supporting Governance operations? How to verify deliverables? What are the consequences of a partially delivered milestone? What accountability is there for PG delivery? Having users of the projects have their say and gather input would be good.  
7. **DAO setup**: What / How / Who are the different decisions to be made?  
   1. Signal capturing, feature requests (is improvement desired?), usage / traffic,   
   2. Decision making on helping the project and figure out what’s needed  
      1. Open source bounties /   
   3. Budget allocation  
   4. Maybe incentivise engagement with the project: if you make a valid issue/request, you get some good points \-\> NQG score impact. Users vote on features and that ties into the NQG. RFP system.  
8. **Long-term funding**: what blend of retro, retainers, and (future) protocol flows is optimal?  
9. **Tooling readiness**: What needs to happen in order to support this setup?  
10. **Needs vs maintainer friction**: What if ecosystem needs don’t align with what the maintainer proposes / wants to move forward with? How do we do this that doesn't make open-source more politically complex / difficult.   
11. **Sybil resistance**: linked to the previous point with a focus on attack vectors vs shift in governance.

### Notes & to-dos

* Publish PG definition & eligibility (with flexible edge-case path).  
* Stand up PG Atlas early; make metrics the default, not an afterthought.  
* Start small, iterate parameters each round; document changes transparently.  
* Use SCF comms to market PGs (discovery matters as much as code).

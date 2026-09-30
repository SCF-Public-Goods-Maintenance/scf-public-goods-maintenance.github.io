---
title: "Scout"
canonical_id: daoip-5:scf:project:scout
parent: Public Good Projects
proposal_issue: 66
proposer: XianPaz
category: "Security & Auditing Tools"
budget: "33000"
---

# Scout

<!-- markdownlint-disable MD036 -->

_Scout is an extensible open source vulnerability analyzer built for Soroban._

<!-- markdownlint-enable MD036 -->

|                      |                                                        |
| -------------------- | ------------------------------------------------------ |
| **Category**         | Security & Auditing Tools                              |
| **Website**          | <https://www.coinfabrik.com/products/scout/>           |
| **Repository**       | <https://github.com/CoinFabrik/scout-audit>            |
| **Repository**       | <https://github.com/CoinFabrik/soroban-audit-harness>  |
| **Repository**       | <https://github.com/CoinFabrik/scout-agent>            |
| **First Released**   | 30 June 2023                                           |
| **Intake**           | soft-launch                                            |
| **Budget Requested** | 33000                                                  |

## Project Description

<!-- markdownlint-disable MD034 -->

Scout is an extensible open-source static analyzer. It allows developers and auditors detect common
security issues and deviations from best practices with the main objective of helping them write
secure and more robust smart contracts.

Scout has several detectors built for Rust and specific for Soroban, Ink! and Substrate. See
[Scout Documentation Site](https://coinfabrik.github.io/scout-audit/docs/intro/) for detailed
information.

During 2025 and 2026, we started experimenting with AI for vulnerability detection through Proof of
Concepts (see <https://github.com/CoinFabrik/scout-audit-ai> and
https://github.com/CoinFabrik/scout-agent).

Our current work with AI is focused on creating an open-source AI product for vulnerability
detection, which will strengthen the offering to the Soroban community with complementary open-source
vulnerability detection tools.

<!-- markdownlint-enable MD034 -->

## Team & Experience

<!-- markdownlint-disable MD034 -->

Victor González - Tech Lead Jose García Crosta - Sr Developer Franco Bragante - Sr Auditor Cristián
Paz Mezzano - Project Manager

<!-- markdownlint-enable MD034 -->

## Retroactive Impact

<!-- markdownlint-disable MD034 -->

We completed the 2026 Q2 scope. The three new Soroban detectors were merged in April 2026; Scout
0.3.17, which includes them along with Soroban SDK 28 support, was released on September 25th, 2026.
We also built and evaluated a new AI-based security analysis proof of concept, the
[Soroban Audit Harness](https://github.com/CoinFabrik/soroban-audit-harness).

Below is a list of updated Scout metrics:

- User Metrics
  - Unique Users: 3779
  - Soroban Crates: 42759
- Operating Systems
  - Linux: 30747
  - MacOS: 22820
  - Windows: 2283
- Client Types
  - ci/cd: 2258
  - Cli: 33633
  - Vscode: 19959
- Installed Versions
  - Prior (0.3.16 deployed Feb 13th, 2026): 21572
  - Last (0.3.17 deployed Sep 25th, 2026): 776
- Usage Over Time
  - Crate Types
    - May: Soroban 369
    - Jun: Soroban 670
    - Jul: Soroban 2007
  - Client Types
    - May: VsCode 0, ci/cd 74, cli 1097
    - Jun: VsCode 2, ci/cd 135, cli 696
    - Jul: VsCode 5, ci/cd 176, cli 2468
- Top 3 Geographic Runs
  - US: 36275 (65.0% of runs, 3194 unique users)
  - AR: 9501 (17.0% of runs, 148 unique users)
  - PT: 1965 (3.5% of runs, 3 unique users)
- crates.io downloads of `cargo-scout-audit`: 36,232 in total, 1,054 in the last 90 days

These figures should be read with care: AI coding agents increasingly run Scout in short-lived
environments, where each session is counted as a new user, so run and user counts can be inflated
by automated use.

The proof of concept was evaluated against 31 audited revisions from 28 Soroban repositories,
covering 243 vulnerabilities confirmed by professional auditors and hidden from the models during
analysis. On a common 12-project subset, weighted recall reached 65.70% with Claude Fable 5.1 High,
and at least one of the three models matched 104 of 121 known vulnerabilities. See the full report in
[Scout AI 2026-Q2 Report](https://github.com/CoinFabrik/soroban-audit-harness/blob/main/docs/Scout%20AI%202026-Q2.md).

<!-- markdownlint-enable MD034 -->

## Past Deliverables

<!-- markdownlint-disable MD034 -->

### 2026 Q2

Q2 results were submitted in Q3, as agreed in advance with SDF. All merged Scout pull requests from
April to September 2026:
https://github.com/CoinFabrik/scout-audit/pulls?q=is%3Apr+is%3Amerged+merged%3A2026-04-01..2026-09-30

#### Q2 D1. Add new detectors (chunk 3 of 3)

Description from last quarter:

> - 3 new Soroban detectors implemented and integrated into Scout.
> - Updated documentation for each detector, including detection logic and remediation advice.
> - GitHub release with new version of Scout including detectors and new test-cases.

Proof of completion:

- New Soroban detectors:
  - [delegated-spending-from-auth](https://github.com/CoinFabrik/scout-audit/pull/339)
  - [init-instead-of-constructor](https://github.com/CoinFabrik/scout-audit/pull/340)
  - [infinite-recursion-over-storage](https://github.com/CoinFabrik/scout-audit/pull/342)
- Documentation:
  - [delegated-spending-from-auth](https://coinfabrik.github.io/scout-audit/docs/detectors/soroban/delegated-spending-from-auth)
  - [init-instead-of-constructor](https://coinfabrik.github.io/scout-audit/docs/detectors/soroban/init-instead-of-constructor)
  - [infinite-recursion-over-storage](https://coinfabrik.github.io/scout-audit/docs/detectors/soroban/infinite-recursion-over-storage)
- Release: [Scout 0.3.17](https://crates.io/crates/cargo-scout-audit/0.3.17)

The detectors were merged in April 2026. The release was published on September 25th, 2026, together
with Soroban SDK 28 support (see Q2 D4), so that the new detectors could analyze current Soroban
projects.

#### Q2 D2. AI Agent POC Iteration 1

Description from last quarter:

> - Updated POC code.
> - Updated POC design document with new refinements, optimizations and new features.
> - Set of contracts chosen for initial testing.

Proof of completion:

- [POC code](https://github.com/CoinFabrik/soroban-audit-harness)
- [POC design](https://github.com/CoinFabrik/soroban-audit-harness/blob/main/docs/Scout%20AI%202026-Q2.md#ai-based-security-analysis-proof-of-concept-first-iteration)
- Initial test set: Allbridge, Blend Capital and Reflector (see the same section).

Instead of refining the Q1 scout-agent prototype, we built a new, more general proof of concept. The
Q1 prototype covered four vulnerability types and relied on simplified code summaries because of the
model limitations at the time. The new harness analyzes whole Soroban repositories for a much wider
range of security issues, supports several model providers, and can be benchmarked repeatably
against professionally audited projects.

#### Q2 D3. AI Agent POC Iteration 2

Description from last quarter:

> - Updated codebase.
> - Updated POC design document with new refinements, optimizations and new features.
> - Expanded set of contracts for testing.
> - Results and findings document.
> - Roadmap from AI POC to a beta-ready product.

Proof of completion:

- [Codebase](https://github.com/CoinFabrik/soroban-audit-harness)
- [POC design](https://github.com/CoinFabrik/soroban-audit-harness/blob/main/docs/Scout%20AI%202026-Q2.md#ai-based-security-analysis-proof-of-concept-second-iteration)
- Expanded test set: 31 audited revisions from 28 repositories, listed in the
  [supporting dataset](https://docs.google.com/spreadsheets/d/1ayqInce49fbBtW-j2eGWaYWLY6E5WeBW/edit?gid=158949213#gid=158949213)
- [Results and findings document](https://github.com/CoinFabrik/soroban-audit-harness/blob/main/docs/Scout%20AI%202026-Q2.md)
- [Roadmap from AI POC to a beta-ready product](https://github.com/CoinFabrik/soroban-audit-harness/blob/main/docs/Scout%20AI%202026-Q2.md#conclusions-and-roadmap)

#### Q2 D4. Soroban SDK 28 support and detector fixes

Description from last quarter:

> This work was not explicitly planned but was completed as additional contribution during the
> quarter.

Proof of completion:

- [Soroban SDK 28 support](https://github.com/CoinFabrik/scout-audit/pull/346)
- [Cycle-safe event traversal in two existing detectors](https://github.com/CoinFabrik/scout-audit/pull/348)

Scout now analyzes Soroban SDK 28 contracts with the normal `cargo scout-audit` command. Release
validation uncovered and fixed a pre-existing cycle-handling problem in two event detectors.

#### Q2 D5. Audit dataset, benchmark and model costs

Description from last quarter:

> This work was not explicitly planned but was completed as additional contribution during the
> quarter.

Proof of completion:

- 58 professional audit reports, 797 normalized findings, and the corresponding pre-fix code
  revisions, used as a hidden answer key
  ([report, First Iteration](https://github.com/CoinFabrik/soroban-audit-harness/blob/main/docs/Scout%20AI%202026-Q2.md#ai-based-security-analysis-proof-of-concept-first-iteration))
- [Evaluation costs](https://github.com/CoinFabrik/soroban-audit-harness/blob/main/docs/Scout%20AI%202026-Q2.md#costs)
- [Exploit-validation experiment with IronCurtain](https://github.com/CoinFabrik/soroban-audit-harness/blob/main/docs/Scout%20AI%202026-Q2.md#out-of-scope-experiment)

Running the benchmark required more than $2,000 in model API charges (about $274 for GLM-5.3 High
and $1,759 to $1,938 for Claude Fable 5.1 High), plus GPT-5.6 Sol High runs under an existing
subscription (about $229 at API rates). We also tested an exploit-oriented workflow based on
IronCurtain; it showed that turning candidate findings into reproducible exploits is a separate and
far more open-ended stage.

As suggested in the Q2 review:

- @AshFrancis (MCP server exposing Scout to users' own agents): planned. We plan to expose both Scout
  and the Soroban Audit Harness through MCP: Scout's static detectors as tools an agent can call, and
  the harness's H1/H2 workflow and knowledge packets as prompts and resources, so developers can run
  them with their own agents and subscriptions, without configuring separate API keys.
- @AshFrancis (feedback loop between tooling and audit findings): addressed in the new harness. H2 is
  guided by knowledge packets distilled from 797 findings in 58 professional audit reports, and the
  harness accepts additional packets through `--knowledge-dir`, so findings from new audits can be
  distilled into packets and fed back into the analysis without publishing the underlying reports.
  The benchmark measures how many audited vulnerabilities the tool rediscovers.
- @oceans404 (Scout as a Scaffold Stellar extension): not yet; to be discussed with the Aha team.

### 2026 Q1

Follows a list of deliverables made during 2026-Q1

Month 1 – Add new detectors - Chunk 2 of 3

- 3 new Soroban detectors implemented and integrated into Scout.
  - [Missing new admin signature detector](https://github.com/CoinFabrik/scout-audit/pull/328)
  - [Extend dos-unexpected-revert-with-vector to detect unbounded growth of Map instances](https://github.com/CoinFabrik/scout-audit/pull/329)
  - [Add uncached-storage-modification detector](https://github.com/CoinFabrik/scout-audit/pull/330)
- Updated documentation for each detector, including detection logic and remediation advice.
  - [Missing new admin signature detector](https://coinfabrik.github.io/scout-audit/docs/detectors/soroban/missing-new-admin-auth)
  - [Extend dos-unexpected-revert-with-vector to detect unbounded growth of Map instances](https://coinfabrik.github.io/scout-audit/docs/detectors/soroban/dos-unexpected-revert-with-storage)
  - [Add uncached-storage-modification detector](https://coinfabrik.github.io/scout-audit/docs/detectors/soroban/uncached-storage-modification)
- GitHub release with new version of Scout including detectors and new test-cases.
  - [Scout version 0.3.16](https://crates.io/crates/cargo-scout-audit/0.3.16)

Month 2 - AI Agents Research and Planning

- [AI agents survey document](https://github.com/CoinFabrik/scout-agent/blob/main/docs/AI%20Agents%20Survey.md)
- [Specification of the selected POC approach](https://github.com/CoinFabrik/scout-agent/blob/main/docs/specification_v2.md)
- Set of contracts chosen for initial testing.Included in the POC Specification document (see Initial
  Contract Set for Testing section).

Month 3 – AI POC Design and Construction

- [Working POC code](https://github.com/CoinFabrik/scout-agent)
- [Detailed POC design document](https://github.com/CoinFabrik/scout-agent/blob/main/docs/specification_v2.md)
- [Results and findings document](https://github.com/CoinFabrik/scout-agent/blob/main/docs/Scout%20AI%202026-Q1.md)
- [Expanded set of contracts for testing](https://github.com/CoinFabrik/scout-agent/blob/main/docs/extended_contract_set.md)

As suggested in the SDF review:

- During Month 1, we engaged with the SDF Security/Audit Bank, presenting detector proposals.
- We delivered new POC metrics.
- We ran the POC using an expanded set of contracts.

<!-- markdownlint-enable MD034 -->

## Proposed Impact

<!-- markdownlint-disable MD034 -->

Our plan for 2026 Q2 was developed with two main objectives:

- Continue adding vulnerability detectors to Scout
- Enhance AI agents POC for vulnerability detection through refinements, optimizations and new
  features

Adding more Soroban-specific detectors will improve Scout and continue to broaden the scope of its
checks.

The Q1 AI POC successfully demonstrated that pivoting to a multi-agent architecture can intelligently
narrow the scope of analysis and overcomes the context dilution observed in single prompt approaches.

The upcoming work on AI POC, will focus on refinements, optimizations and adding more features (i.e.,
expanding the expertise of the agent to broader vulnerability categories, explore the viability of
implementing iterative QA passes as a post-processing layer in the audit pipeline, etc.). A detailed
backlog is included in the
[Results and findings document](https://github.com/CoinFabrik/scout-agent/blob/main/docs/Scout%20AI%202026-Q1.md)
(see the “Conclusion and Next Steps” section).

We will also develop a roadmap to evolve our AI POC into a beta-ready product.

<!-- markdownlint-enable MD034 -->

## Proposed Deliverables

<!-- markdownlint-disable MD034 -->

Month 1 – Add new detectors - Chunk 3 of 3

- 3 new Soroban detectors implemented and integrated into Scout.
- Updated documentation for each detector, including detection logic and remediation advice.
- GitHub release with new version of Scout including detectors and new test-cases.

Month 2 – AI Agent POC Iteration 1

- Updated POC code.
- Updated POC design document with new refinements, optimizations and new features.
- Set of contracts chosen for initial testing.

Month 3 – AI Agent POC Iteration 2

- Updated codebase.
- Updated POC design document with new refinements, optimizations and new features.
- Expanded set of contracts for testing.
- Results and findings document.
- Roadmap from AI POC to a beta-ready product.

<!-- markdownlint-enable MD034 -->

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.

## Reviewers comments

```text
@AshFrancis says:

~31 detectors (with 3 more in this proposal) is pretty good coverage for generic issues.
[CF] Agree. Thanks.

I like the AI work, personally I would also like to see an MCP server that exposes primitives to the users own agents (so they dont have to configure API keys and can use their existing claude/codex/etc. licenses. Though perhaps you've explored this and decided against it for good reasons.
[CF] Thanks a lot for the suggestion. It’s a great feature for driving adoption. Right now, our priority is to iterate on the core first: improving precision, adding more vulnerability categories, and reducing latency and token consumption. We’ll keep the MCP server idea in mind to be considered later as the product matures.

Honestly with recent news on AI based attacks, tooling like this is pretty essential and the bare minimum a project should be doing (combined with audits!)
[CF] Agree. We believe that providing a bundle of Scout and Scout-Agent tools to the community is a good way to respond to these AI-based attacks.

I ran scout on one of my earlier soroban side projects and it did find a mild bug (pagination overflow) alongside some false positives, so that was good to see.
[CF] Glad to hear that.

It would be good to see some kind of positive feedback loop with projects utilizing tools like this, then being audited, with additional audit findings being plugged back into this.
[CF] We are working with SCF to raise awareness around security and provide hands-on support to projects.
```

```text
@oceans404 says:
I like the direction. One distribution thought: Scaffold Stellar has already shipped both their extension system and a reporter extension — framed by Aha as "a distribution surface for other public goods and ecosystem tooling." Scout feels like a natural fit there: a detector extension running during stellar scaffold build, with findings surfaced through the reporter.

This could be a cool default pipeline for Soroban builders using Scaffold. Could you have a chat with the Aha team about this?

[CF] Hi @oceans404, for sure !!
```

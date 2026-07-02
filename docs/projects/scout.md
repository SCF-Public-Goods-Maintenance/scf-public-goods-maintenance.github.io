---
title: "Scout"
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

|                      |                                              |
| -------------------- | -------------------------------------------- |
| **Category**         | Security & Auditing Tools                    |
| **Website**          | <https://www.coinfabrik.com/products/scout/> |
| **Repository**       | <https://github.com/CoinFabrik/scout-audit>  |
| **First Released**   | 30 June 2023                                 |
| **Intake**           | soft-launch                                  |
| **Budget Requested** | 33000                                        |

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

We successfully completed all the main activities and deliverables within the 2026 Q1 scope. As a
result, we deployed a new version of Scout with additional Soroban detectors and developed a new
iteration of our AI-based POC for vulnerability detection using AI agents. This POC successfully
identified issues previously detected in audits and resolved the context dilution problem observed in
earlier versions.

We deployed the new version of Scout in February. Below is a list of updated Scout metrics:

- User Metrics
  - Unique Users: 322
  - Soroban Crates 23060
- Operating Systems
  - Linux: 7445
  - MacOS: 19664
  - Windows: 2236
- Client Types
  - ci/cd: 426
  - Cli: 9019
  - Vscode: 19900
- Installed Versions
  - Prior (0.3.11 deployed Nov 8th, 2025): 1320
  - Last (0.3.16 deployed Feb 13th, 2026): 835
- Usage Over Time
  - Crate Types
    - Feb: Soroban 2194
    - Mar: Soroban 290
    - Apr: Soroban 192
  - Client Types
    - Feb: VsCode 1797, ci/cd 120, cli 713
    - Mar: VsCode 32, ci/cd 45, cli 368
    - Apr: VsCode 0, ci/cd 9, cli 192
- Top 3 Geographic Runs
  - US: 17712 (60.4% of runs, 532 unique users)
  - AR: 5615 (19.1% of runs, 144 unique users)
  - PT: 1965 (6.7% of runs, 3 unique users)

We evaluated precision and recall metrics for the 2025 Q4 POC (single prompt) against the 2026 Q1 POC
(AI agents) using several LLMs. The new POC improved both precision and recall across two evaluation
runs: one using the initial set of contracts and another using the expanded set. See the full report
in
[Scout AI 2026-Q1 Report](https://github.com/CoinFabrik/scout-agent/blob/add_2026q1_report/docs/Scout%20AI%202026-Q1.md).

<!-- markdownlint-enable MD034 -->

## Past Deliverables

<!-- markdownlint-disable MD034 -->

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

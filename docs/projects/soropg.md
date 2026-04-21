---
title: "soropg"
parent: Public Good Projects
proposal_issue: 32
proposer: jamesbachini
category: "Developer Experience"
budget: "$35,000"
---

# soropg

_SoroPG is an open-source, browser-based Soroban IDE that lets developers write, test, run security
checks, deploy, and interact with Stellar smart contracts with zero local setup._

|                      |                                                                                                    |
| -------------------- | -------------------------------------------------------------------------------------------------- |
| **Category**         | Developer Experience                                                                               |
| **Website**          | <https://soropg.com>                                                                               |
| **Repository**       | <https://github.com/jamesbachini/Soroban-Playground>                                               |
| **First Released**   | May 2025                                                                                           |
| **Intake**           | <https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/issues/19> |
| **Budget Requested** | $35,000                                                                                            |

## Project Description

SoroPG is a beautiful open-source web IDE for Soroban development that removes local setup barriers
for Stellar builders.

It provides the only zero-setup Stellar workflow where developers can create, test, security-check,
deploy, and explore contracts entirely in-browser, which makes it valuable for onboarding,
prototyping, debugging, demos, and rapid iteration.

In a browser, developers can create Rust contracts, compile to WASM, run unit tests and Scout
security checks in sandboxed containers, deploy to local, testnet, futurenet, or mainnet, and inspect
or invoke contract functions through integrated Stellar SDK tooling. By combining coding, testing,
deployment, and exploration in one maintained public interface, SoroPG shortens
time-to-first-contract for new developers and speeds up iteration for experienced teams. It is
neutral shared infrastructure for prototyping, debugging, reproducible examples, and future
AI-assisted contract workflows.

## Team & Experience

Just me, James Bachini, sole lonely maintainer of SoroPG. Although it's open-source and contributors
are welcome!

I'm a contract dev and content creator based in the UK. I've been building and experimenting with
Stellar since around summer of 2024 just before the London Meridian. I have been contracted to create
developer tutorials and video content for SDF since around that time. I built SoroPG originally just
for myself as a pet project because I wanted something to demo contract code for the Stellar
ecosystem. Over time it's become slightly more refined and suitable for public consumption.

Profiles:

- GitHub: https://github.com/jamesbachini
- Discord: jamesbachini
- LinkedIn: https://www.linkedin.com/in/james-bachini/

Additional Links:

- Website: https://jamesbachini.com/
- YouTube: https://www.youtube.com/c/JamesBachini

## Retroactive Impact

1940 unique visitors in the last 30 days

Reference cloudflare stats (screenshot attached)
https://jamesbachini.com/misc/soropg-stats-2026-03.png

This is with no advertising or promotion, it's picked up organic traction due to it being the only
online IDE available for Stellar devs

## Past Deliverables

N/A - haven't received a public goods/infra grant before

It's been a self-funded passion project for the last year. There have been updates such as the recent
one this week: https://x.com/james_bachini/status/2041531946116034786

Best proof of _"deliverables"_ or consistent ongoing work would probably be this:
https://github.com/jamesbachini/Soroban-Playground/graphs/commit-activity

## Proposed Impact

### Availability

Maintain and scale SoroPG to support the growing demand.

### Academy

Build a learning platform with lessons for developers new to Stellar. I've started working towards
this by implementing workspaces in the repo. This allows you to pull in complete code bases such as
from [Stellar's Soroban Examples](https://github.com/stellar/soroban-examples/) repo.

### Documentation

Neglected to date but important for technical reference. I know how it works but it might be useful
for others to know as well or at least have a place to find out and dig into the nuts and bolts.

### General

For the best part of the last year it's been, to my knowledge, the only viable option for an online
IDE in the Stellar ecosystem. AI has and will continue to disrupt how we build software which has
brought a lot of the development work to terminal UI's like Claude Code and Codex. I think web IDE's
and even the humble text editor still have value in an AI assisted development world and SoroPG can
become a Swiss Army knife tool for Stellar developers to experiment with Stellar smart contracts. It
can also become a great onboarding and learning resource for new developers. Where as Remix
introduced a generation of Solidity contract developers to Ethereum I want to do the same for
Stellar.

## Proposed Deliverables

### Availability

- Maintain SoroPG with ≥99% uptime

- Ensure full compatibility with the latest Soroban SDK and external crates such as OpenZeppelin
  libraries

Ecosystem value: Deliver a competitive online IDE for smart contract developers.

Budget allocation: $25k

### Academy

- Launch an Academy MVP integrated into SoroPG

- Publish 3-5 beginner lessons with live, executable Stellar contract examples. Concept idea: User
  opens up Academy from the left menu, selects from a series of tutorial style lessons. Each lesson
  opens up the required code in SoroPG, there's a video walkthrough and written explanation of how
  the code works and what new developers need to know about building on Stellar.

Ecosystem value: Accelerates developer onboarding and education pipeline.

Budget allocation: $10k

### Documentation

- Publish core technical documentation

Budget allocation: $0k - I can probably get AI to do this, there's very little cost involved.

Ecosystem value: Improves maintainability, transparency, and long-term reliability of shared
developer infrastructure.

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.

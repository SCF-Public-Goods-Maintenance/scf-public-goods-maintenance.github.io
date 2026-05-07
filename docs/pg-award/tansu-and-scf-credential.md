---
title: Tansu Integration & SCF Credentials
parent: Public Goods Award
nav_order: 2
---

# Tansu Integration & SCF Credentials

## Overview

The SCF Public Goods Award uses [Tansu](https://tansu.dev) as the on-chain voting platform for
proposal evaluation and funding decisions. Tansu integration enables anonymous NQG-weighted voting,
transparent on-chain governance records, and composable SCF Pilot credentials.

**Current status**: Operational for 2026 Q2 award round with NQG-weighted anonymous voting, SCF
Governance space on Tansu, and soulbound credential framework.

## Tansu Voting Integration

### Governance Structure

The SCF operates as a dedicated organization on Tansu:

- **SCF Governance Space** — A non-code project space on Tansu dedicated to Public Goods Award rounds
- **Proposal Submissions** — Each PG Award round creates proposals within the SCF Governance space
- **Anonymous Voting** — BLS12-381 cryptographic scheme (Pedersen commitments) enables Pilots to vote
  without revealing identity using a single address
- **Transparent Results** — All votes recorded on-chain with verifiable tallying

### NQG-Weighted Voting

SCF Pilots vote using their reputation scores for sybil resistance and proportional voice:

**Voting mechanism**:

1. Neural Quorum Governance (NQG) scores calculated and stored in
   [stellar-community-fund-contracts](https://github.com/stellar/stellar-community-fund-contracts)
2. Each Pilot's can cast a vote on Tansu. They can adjust their voting power which is capped based on
   their individual NQG scores
3. Votes are recorded on-chain as Pedersen commitments
4. Votes execute on-chain without ever revealing individual votes

**Vote privacy**:

- Traditional Pedersen commitment scheme preserves vote content privacy
- Space owners can inspect votes (consistent with current SCF governance)
- Pilots use single addresses (no multi-address workarounds for anonymity)

### Voting Workflow

The 2026 Q2 award round follows this on-chain voting pattern:

1. **Proposal Creation** — Council creates proposals on Tansu at close of Discussion & Revision
   window
2. **Voting Period** — ~3 days for Pilots to cast NQG-weighted votes
3. **On-Chain Execution** — Results tallied and recorded on Stellar
4. **Award Distribution** — Approved proposals receive initial funding tranche

See [Proposer Instructions](proposer-instructions.md) for full timeline details.

## SCF Pilot Credentials

### Soulbound Credential Design

The SCF Pilot credential system builds on NQG scores with dynamic NFT representation:

**Credential properties**:

- **Soulbound** — Non-transferable tokens bound to Pilot identities
- **Dynamic** — NFT metadata updates automatically when SCF role and NQG score change
- **SEP-50 Compatible** — Follows Stellar ecosystem standards for wallet integration (Freighter,
  etc.)
- **Composable** — Other projects can leverage trust signals (e.g., Stellar Security Portal)

**Use cases**:

- **Voting** — Badge-based vote weighting on Tansu
- **Access Control** — Pilot-only features in ecosystem tools
- **Reputation Display** — Public profiles showing SCF contribution status
- **Third-Party Integration** — External projects can query Pilot status and reputation

### Credential Lifecycle

1. **Initial Issuance** — New Pilots receive soulbound credential at onboarding
2. **NQG Updates** — Credential metadata refreshes when NQG score changes (monthly recalculation)
3. **Status Evolution** — Visual representation updates to reflect reputation tier
4. **Role-Based Access** — Credential includes role metadata (Pilot, Council, etc.)

The credential contract architecture enables future expansions:

- **Composable metadata** — Game-card style profiles, custom avatars, achievement badges
- **Cross-Platform Recognition** — Pilots carry reputation across SCF tools and partner platforms
- **Governance Participation** — Transparent on-chain record of voting activity

## Integration Benefits

The Tansu + credential architecture addresses key governance challenges:

| Pain Point                  | How Addressed                                                            |
| --------------------------- | ------------------------------------------------------------------------ |
| Voting UX friction          | Single-address anonymous voting (no multi-wallet workarounds)            |
| Identity verification       | Soulbound credentials provide on-chain Pilot verification                |
| Reputation opacity          | Dynamic NFTs surface NQG scores transparently                            |
| Cross-tool friction         | SEP-50 compatibility enables wallet integration and ecosystem-wide trust |
| Limited programmatic access | On-chain credentials replace Discord API dependencies                    |
| Vote manipulation risk      | NQG weighting + soulbound identity prevents sybil attacks                |

## Future Enhancements

Near-term improvements under consideration:

### Automated Execution

Currently, Tansu votes trigger manual award distribution. Future automation possibilities:

- **Smart Contract Execution** — Vote results trigger on-chain payment contracts
- **NQG Updates** — Voting participation automatically updates reputation scores
- **Tranche Automation** — Milestone completion triggers subsequent funding releases

### Enhanced Credentials

- **Visual Evolution** — Dynamic artwork reflecting status tiers and achievements
- **Multi-Signature Support** — Team credentials e.g. for working groups of SCF verified members

### Governance Extensions

- **Delegation** — SCF members delegate voting power while retaining credential
- **Custom NQG** — Specific NQG score tailored to this grant program
- **Conflict of interest** — Integrate the conflict of interest feature from Tansu into the workflow
- **Historical Dashboards** — Transparent analytics of voting patterns and participation rates

The Tansu integration and credential framework provide the foundational infrastructure for
decentralized SCF governance while maintaining backward compatibility with existing processes.

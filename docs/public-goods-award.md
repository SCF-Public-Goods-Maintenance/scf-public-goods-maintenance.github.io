---
title: Public Goods Award Experiment
nav_order: 3
---

# Public Goods Award

## Voting

We would like to propose to use Tansu as a decentralized voting platform to manage the proposals.

There are a few ways we could make this work, projects themselves won’t necessarily have to be registered on Tansu. Instead, we are going to create a specific organization for SCF in Tansu. For visibility, we can attach projects to a given space, but again we don’t need to require this from projects.

At a higher level:

1. Create a SCF Governance space (non-code project on Tansu),  
2. Maintainers to make a proposal by themselves in SCF Governance space. The key here is that the proposals should be made anonymous. Tansu uses a traditional Pedersen commitment scheme meaning that the owner of the SCF space would be able to inspect votes (as it is the case now.) The main difference being that people don’t have to use multiple addresses.  
3. Get all pilots to vote on proposals using their NQG.

Tansu is getting some new options when creating a proposal. We will soon be able to either use a token based vote (locking a collateral based on the selected weight) or a badge based vote. At the moment, said badges are hardcoded. Depending on how we would like to move, we could plug the NQG scores either on the token side, or the badge side without much work.

Votes on Tansu can execute arbitrary smart contracts. We could use this mechanism in multiple ways such as updating the voting history for NQG scoring or even triggering a payment. The last point would require more extensive discussions and we might want to leave that conversation for a phase 2\.

## NQG

At the moment, the everyone’s NQG score is calculated and stored in this contract:

[https://github.com/stellar/stellar-community-fund-contracts](https://github.com/stellar/stellar-community-fund-contracts)

We would like to propose to build a small abstraction on top as a soulbound and dynamic NFT (following SEP-50 as to be compatible with Freighter at least.) This would allow each participant to have a clear view on their score and a nice way to represent and share their accomplishments. Pilots should be proud of their status.

When the NQG score of participants changes, the NFT would be updated to reflect that change.

A second objective could be to move the role based system here as well.

Having all that information readily available on-chain would not only help us with voting on proposals. It would allow other projects to leverage this trust system. E.g. Soroban Security is using the Discord API to allow Pilots to add audit reports onto their platform. Pilots can do more for the community if we have the tools. And this would be an easy lift.

Of course, we would have some accompanying art to show the status evolution. We can even have something composable if we want. E.g. make a game-card like version and as an image the profile picture someone would select.

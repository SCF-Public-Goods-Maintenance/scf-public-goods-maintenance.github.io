---
title: "RefractorSpace"
parent: Public Good Projects
proposal_issue: 38
proposer: orbitlens
category: "Governance Tools"
budget: "20,000"
---

# RefractorSpace

_Pending transactions storage and multisig aggregator for Stellar Network._

|                      |                                                                                                    |
| -------------------- | -------------------------------------------------------------------------------------------------- |
| **Category**         | Governance Tools                                                                                   |
| **Website**          | <https://refractor.space>                                                                          |
| **Repository**       | <https://github.com/stellar-expert/refractor>                                                      |
| **First Released**   | March 2021                                                                                         |
| **Intake**           | <https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/issues/26> |
| **Budget Requested** | 20,000                                                                                             |

## Project Description

Refractor is a pending transactions storage and multisig aggregator for Stellar Network.

It's a developer-focused service in the first place, but anyone can use it to store transactions and
gather signatures required to match the signing threshold. Users can explicitly set expiration date
and custom callback URL. Refractor automatically discovers potential signers and computes the
thresholds, ensuring that signatures are valid and consistent.

Other services and wallets can access and sign a transaction using a standard URL where its hash
serves as a unique identifier. The website displays current signing status, suitable signers, and
thresholds. Any eligible signer can sign the transaction. As soon as it reaches the required
threshold (calculated automatically), the service either submits the transaction to Stellar network
or executes a callback.

## Team & Experience

Refractor is maintained by the [StellarExpert team](https://stellar.expert/). We build infrastructure
tools on Stellar since 2016. Our notable projects: [StellarExpert](https://stellar.expert/),
[Reflector](https://reflector.network/), [StellarBroker](https://stellar.broker/),
[Albedo](https://albedo.link/), [LedgersTax](https://ledgers.tax/).

Active developers of the Refractor service:

- OrbitLens (GitHub profile: [orbitlens](https://github.com/orbitlens), Discord `@orbitlens`)
- HawthorneAbendsen (GitHub profile: [hawthorne-abendsen](https://github.com/hawthorne-abendsen),
  Discord `@hawthorne7187`)
- Yazadzhy (GitHub profile: [yazadzhy](https://github.com/yazadzhy))

## Retroactive Impact

Over the last 3 months our service processed more than 100 multisig transactions. It is actively used
by Aquarius DAO, Reflector DAO, YieldBlox DAO, Stratum, and other services.

Here is, for example, a pending Aquarius DAO distribution
[tx](https://refractor.space/tx/643a50a64293a5d6a54c0b539a226cf7fdaf58ef32d68e0e9b7c3908a62926a5).

## Past Deliverables

N/A

## Proposed Impact

We aim to improve the website, documentation, provide relevant usage examples, and perform some
direct outreach to Stellar developers community to showcase how they can streamline their complex
multisig workflows using our service. This may significantly simplify life for any developers that
have to deal with multi-party controlled wallets, preauthorized transactions, or escrow services
backed by by Stellar.

## Proposed Deliverables

- Update documentation and highlight various usage scenarios to simplify on-boarding for new projects
  (2000$)
- Revamp the website home page, include recently added functionality, emphasize key product features
  (2500$)
- Move infrastructure to a new server (500$)
- Add additional wallets supports on signing interface, improve signing flow on mobile devices
  (7000$)
- Update aggregator, website, dependency libs to support the upcoming Stellar protocol upgrade
  (8000$)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.

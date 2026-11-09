---
title: "The Bridge Reopens Halfway, and Zcash Wants to Run Again"
date: 2026-11-09
draft: false
categories: ["Blockchain", "Crypto"]
tags: ["tBTC", "Threshold", "Zcash", "Aave", "bridge"]
summary: "tBTC restarts after nine days down for a Linux kernel flaw, while the 120 million dollar Aave reserve stays frozen."
url: "/en/2026/11/tbtc-bridge-reopens-halfway-zcash-block-time/"
---

Two pieces of infrastructure news on the same day, and they are about the same thing: what trust costs when it runs through software you do not control. A Bitcoin bridge that reopens halfway after nine days offline for a Linux kernel flaw; a blockchain that, as soon as one upgrade lands, proposes another to gain five seconds.

## The bridge that reopens without reopening

Threshold halted the tBTC bridge on October 30 over a critical Linux kernel vulnerability capable of executing code on unpatched servers. On Sunday it announced the restart: patched nodes are rejoining and requests submitted before the halt are being processed, but the app accepts no new deposits, minting or redemption until enough active nodes are online. No date for a full restoration has been given.

The number that matters is not the bridge, it is what sits around it. On October 31 Aave froze the tBTC reserve on Ethereum Core: roughly 120 million dollars stalled, no new deposits, no new borrowing power, though withdrawals and repayments remain possible. Threshold reports 4,320 BTC in the bridge wallets against 4,185 tBTC in circulation, with no unauthorised transfers. LlamaRisk, Aave's risk provider, will propose unfreezing the reserve once operations return to normal.

The flaw was in Linux, not in tBTC. A bridge that holds for years can stop over an operating-system patch, and a multi-billion protocol discovers it depends on a redemption it does not control. The attack surface of an infrastructure does not coincide with its code.

## Five seconds as a strategy

On Friday 6 November the NU7 upgrade hit mainnet and moved Zcash's block target from 75 to 25 seconds. Two days later, on Sunday 8, ValarDragon and Evan Forbes filed a draft on the community forum to go down to 20 seconds in NU7.1.

The proposal is conservative: it changes only latency, not the daily capacity for private transactions. Blocks stay at 2 MB, shielded action budgets drop from 330 to 264, the per-block subsidy is scaled by 4/5 with the halving interval lengthened, so that issuance does not change. The real risk is orphans: 1.9% on a Zakura-only network, 3.3% on a mixed one, against the 4.68% measured when 25 seconds was judged acceptable.

Zcash is playing its story on the word "cash", and five seconds less to first confirmation is an argument for point-of-sale payments, exchange deposits and cross-chain swaps.

## The same curve

The two facts are not opposites: they are the same curve. The more a system becomes someone else's infrastructure, the more every detail becomes systemic risk. Zcash's twenty seconds will be as safe as the node running on the least-updated operating system in the network.

---
*Verified sources: Cointelegraph, "tBTC bridge partially resumes as $120M Aave reserve remains frozen" (9 November 2026) and the Aave governance thread on the mint/redeem pause; Bloomingbit and Coinfi as same-day cross-checks; Zcash Community forum, "Proposal: Lower Zcash block target spacing from 25s to 20s" by ValarDragon (8 November 2026); Cointelegraph, "Zcash devs propose another block time cut days after NU7 upgrade" (9 November 2026); Grafa, technical summary of the ZIP proposal (9 November 2026).*

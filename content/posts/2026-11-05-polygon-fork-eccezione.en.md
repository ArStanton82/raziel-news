---
title: "Polygon Rewrites a Balance: the $6.8 Million Fork and the Constitution of Exceptions"
date: 2026-11-05
draft: false
categories: ["Crypto", "Blockchain"]
tags: ["Polygon", "POL", "hard fork", "Binance", "Polymarket", "governance"]
summary: "A PIP proposes zeroing five addresses at a fixed block and crediting the stolen funds to their owners, with six conditions written down in advance."
url: "/en/2026/11/polygon-rewrites-a-balance-6-8-million-fork/"
---

Today at 14:30 UTC Polygon's governance debates a proposal that, if approved, will change the network's software in order to do something blockchains declare impossible: rewrite a balance. At a predetermined block, five addresses controlled by an attacker would be zeroed out and the same amount of POL credited to recovery wallets verified by Polymarket and Binance. Total supply does not change: who owns it does.

## What is inside the fork

The arithmetic is precise: 70.49 million POL, of which 23.86 million across four addresses tied to the Polymarket incident of 29 October and 46.63 million on a single address tied to Binance. The PIP reconstructs the movement: overnight between 29 and 30 October a Binance hot wallet had sent that address 46,626,589.6 POL and 6,185,900.1 USDT, and Tether then froze the USDT, leaving the native POL as the only part still at risk. The valuation swings with the price used: about 6.5 million at the 0.0924 dollars of 29 October cited in the proposal, 6.8 million at current prices.

## A blacklist is not enough, and it is already a power

Block producers added the addresses to the transaction exclusion list at the request of the affected parties, and no way around it has been found. But the proposal is honest about the limits: each producer reads the list only at startup, so every change requires a release and a restart; entries never expire; the filter covers only external senders and EIP-7702 authorisations, so it is not a complete freeze. The attacker kept trying, with a transaction offering roughly 219,450 POL in fees, and contacted validators offering money to unblock a transfer. Polymarket opened an on-chain recovery channel through the SEAL Safe Harbor safe, with no answer.

It is worth pausing here: the blacklist was already an act of central control, merely a silent one. The fork makes that power visible.

## Six conditions written down in advance

The most interesting part of the document is not the mechanism, it is the table that precedes it. The proposers list six verifiable conditions: incidents publicly acknowledged by the victims, block applied by every producer, a meaningful sum, clear on-chain tracing to respectable parties, an explicit request from the victims, no competing claims after disclosure. And they add that this is an extreme action, not to be repeated as a matter of course, not a general-purpose tool for freezing and recovery. The text also makes clear that it is not legal advice and that nobody is promising the outcome of the vote.

It is the right way to frame the question, and the underlying problem remains: immutability is not a physical property, it is a governance threshold. Written this way, the threshold is high and expensive. But the sum at stake is small, and a small sum is exactly what makes a precedent cheap.

---
*Verified sources: Polygon Community Forum, full text of the PIP "Recovery of Funds Held in Blocked Addresses following the Polymarket and Binance Incidents", author Parvez03 of the Polygon Labs Validator Support Team, published 2026-11-04 (read on 2026-11-05); PPGC-47 agenda of 5 November 2026; Cointelegraph, article of 2026-11-05 on amounts, split and timing; crypto.news and Cryptopolitan, articles of 2026-11-05 with the same split and the 29 October reference price; FXStreet, 2026-11-05, for the conditions and implementation timing. Bitcoin price used only as context: 80,445 dollars per the CoinGecko API and 80,533 dollars per the Cointelegraph ticker, taken on 2026-11-05.*

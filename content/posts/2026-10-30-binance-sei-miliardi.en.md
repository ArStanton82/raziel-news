---
title: "Six Billion in Twenty Minutes: the Night Binance Lost Its Signatures"
date: 2026-10-30
draft: false
categories: ["Crypto", "Blockchain"]
tags: ["Binance", "hack", "North Korea", "stablecoin", "Bitcoin"]
summary: "The $6.3 billion theft did not break the cryptography: it convinced the system that signs transactions to sign them."
url: "/en/2026/10/six-billion-in-twenty-minutes-the-night-binance-lost-its-signatures/"
---

On the night between 29 and 30 October the largest exchange in the world lost about $6.3 billion, by its own estimates: the biggest crypto theft ever recorded, four times Bybit 2025. But the part worth understanding is not the figure. No private key was breached, no algorithm was broken. Someone got Binance's systems to sign transactions chosen by him.

## Ten blockchains, twenty minutes

According to TRM Labs the attack began at 20:05 UTC on the XRP Ledger: five Binance wallets sent 233.46 million XRP to a single address. Then Solana, Optimism, Tron, Arbitrum, Avalanche, Polygon, Base. At 20:20 a Bitcoin hot wallet sent 18,270 BTC, about $1.4 billion, split within minutes into 19 wallets — seventeen with exactly 1,000 BTC each. By 04:23 on Friday none of the 19 had moved a single coin.

The technical core is on Ethereum: with an EIP-7702 delegation, the tool introduced with Pectra, the attacker turned a hot wallet into a "sweeper" under his own control, presenting fifty pre-signed authorizations in a single transaction. The wallet processes continuous withdrawals and its counter advances: fifty consecutive signatures guaranteed that one of them was still valid. One was enough: 167,464 ETH left in a single transaction.

## Whose fault it is

TRM attributes the operation to TraderTraitor, the North Korean hacking unit, "with high confidence"; Chainalysis speaks of $6.4 billion; ZachXBT has shown that the Binance funds and those of the earlier Bitget exploit came back together on the same address after THORChain. Binance points to a more prosaic trail: a compromised DevOps engineer's laptop, which would have opened a container and allowed unauthorised withdrawals, with no leak of private keys.

## What stops, and what doesn't

Stablecoin issuers moved within hours: Tether, Circle, Ripple and World Liberty Financial froze about $2.7 billion across USDT, USDC and RLUSD, and Arbitrum's Security Council moved 8,426 ETH by authority. Binance speaks of $3 billion frozen. The rest did not: 420,000 ETH and 18,270 BTC are beyond anyone's reach, because bitcoin has no issuer that can put up a blacklist.

The exchange will cover all losses with the SAFU fund and with its own money. But the proof-of-reserves data show a friction: the drained wallets appeared on the balance sheet as backing for client balances, and the 204,500 ETH taken leave ether coverage at 94 percent. The SAFU, according to CoinDesk, is worth about a billion in bitcoin: less than a sixth of the hole.

Meanwhile the market reacted without panic — bitcoin around $78,500, BNB at 716 — but institutional investors are moving assets off exchanges. The lesson is not that bitcoin is unsafe: it is that a platform's security is decided where one machine asks another to sign, and there a laptop, a container, one authorization too many weigh more than any elliptic curve.

---
*Verified sources: TRM Labs, "North Korea Steals USD 6.36 Billion From Binance in the Largest Hack in History" (29 October 2026); Binance Support, "Security Incident Update" (30 October 2026, 02:23); Cointelegraph, "North Korea's TraderTraitor linked to $6.3B Binance hack" (30 October 2026); CoinDesk, "Binance hacker splits $1.4 billion of bitcoin into 19 wallets that no one can freeze" and "Binance says customer money is safe after huge hack drains key reserve wallets" (30 October 2026); Bloomberg (29-30 October 2026); BBC (30 October 2026); CNBC (30 October 2026); TechCrunch (29 October 2026); The Block (29 October 2026).*

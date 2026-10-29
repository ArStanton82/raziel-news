---
title: "The Signature, Not the Loot: How Billions Left Binance in Four Minutes"
date: 2026-10-29
draft: false
url: "/en/2026/10/the-signature-not-the-loot-how-billions-left-binance-in-four-minutes/"
categories: ["Crypto", "Blockchain"]
tags: ["Binance", "EIP-7702", "hack", "Tether", "Circle"]
summary: "A hot wallet emptied in one transaction, for 93 cents in fees. The billions are the headline; the real question is who signed."
---

Underneath the surface, every exchange is a signing problem. On Thursday 29 October at 20:24 UTC a Binance hot wallet — the address Etherscan labels «Binance 14» — sent 167,464 ETH and 63 different tokens, including 1.615 billion USDT, to an address created hours earlier. The fee for moving that much was **93 cents**.

This was not a smart-contract exploit. There is no broken code to fix, no function to pause. There is a signature that someone produced and should not have been able to produce. Everything else — the billions, the freezes, the statements — follows from that.

## Four minutes, line by line

The reconstruction comes from the chain, and it is the part sources agree on even where the totals diverge.

- **28 and 29 October.** A wallet receives three deposits of about 0.1 ETH each, routed through Tornado Cash, a mixer. First warning sign: an exchange does not pay its transaction fees that way.
- **15:59 UTC.** The same wallet deploys a delegate contract, prepared that morning.
- **20:20:59 UTC.** It submits an **EIP-7702** authorization on the Binance 14 wallet, handing control of that wallet to its own contract.
- **20:24 UTC.** It calls the contract. The wallet empties in a single transaction — 167,464 ETH plus the tokens — into `0x5227…2f8c`, which Etherscan now labels «Binance Hot Wallet Exploiter 2».
- **Seconds later.** The Binance 16 wallet sends another 28,005.6 ETH to the same destination.
- **20:41 UTC.** The same delegate pulls 780 million USDC from another Binance wallet, then 43 million more.
- **21:01 UTC.** Tether blacklists the receiving address: 975.1 million USDT stop moving.
- **21:04 UTC.** Circle freezes 823 million USDC. Allaire cites «more than 800M», in coordination with law enforcement.
- **21:15 UTC.** CZ writes that it «does look like a hack» and thanks both issuers. At 22:23 he adds that the loss «might be a bit higher» than circulating estimates, but will be covered.
- **21:29 UTC.** Binance updates its statement: «user funds are completely safe». It has never used the word hack.

## Why EIP-7702 moves the question

EIP-7702 has been live on Ethereum since the Pectra upgrade of 7 May 2025. It lets an ordinary wallet delegate its control to a contract, which is useful: it bundles many transfers into one transaction, and that is why exchanges use it to distribute funds efficiently.

The property that matters is a different one, as Odysseas Lamtzidi of Phylax Systems put it: the delegation **persists**. The installed code can authorise later transfers without another signature from the wallet. This is not a stolen password you can change. It is a track left open until somebody revokes it.

And a delegation requires a signature made with the wallet's private key. The attacker had one. That is the fact, and the only one that really counts: the perimeter of this incident is not the wallet, it is whoever signs for the wallet. A key in the clear on a connected machine, a compromised signing service, an insider — none of these has been confirmed, and until Binance publishes the custody chain of its own keys, the gap between them is the gap between a misconfiguration and a personnel problem.

## The accounting that still does not add up

Published totals diverge, and not through sloppy reporting: they measure different things.

| Measure | Value | What it means |
|---|---|---|
| Ethereum, three wallets | ~$3.5bn | Unchained's own count of outgoing transfers |
| Three chains | ~$5.57bn | aggregate estimate: $3.51bn Ethereum, 18,270 BTC, $0.63bn on Tron |
| Frozen | $1.8-2.4bn | $975.1m USDT in one wallet, $823m USDC; Tether claims more than $1.567bn overall |
| Outside the freezes | ~$3.8bn | Bitcoin and ETH cannot be frozen by any issuer |

That is where the number circulating since last night comes from. DefiLlama's founder, 0xngmi, wrote that with USDT and USDC frozen the loss now sits around one billion dollars — 0.69% of Binance's 144 billion in assets under custody — and that the exchange will cover it from its balance sheet easily. CZ quoted him: «Loss might be a bit higher than that, but will cover.»

The solvency argument is sound. The figure, however, describes a **net loss**, not the theft: if the three-chain tally holds, the uncovered hole is in the 3-4 billion range, not one. Conflating the two is the expensive mistake in cases like this, because the first number says whether the exchange stands, the second says how much was lost.

There is also an accounting detail nobody has settled: a frozen token is not a recovered token. It stays where it is, unusable by the attacker, until Tether or Circle decide — normally with a court order — whether to burn it and reissue it to the victim. Until then a freeze protects the market from the funds moving; it does not rebuild reserves.

## The market did not wait for the accounting

Within the hour Bitcoin slid from $80,327 to $78,763, below 79 thousand, with roughly 628 million dollars of leveraged positions force-closed. BNB lost between 6 and 7 per cent, falling to about 699 dollars. Neither move describes a default. Both describe a market pricing the possibility that the problem is larger than what it can see.

## What still needs verifying

Five questions remain open, and should be kept apart from the on-chain facts.

1. **How the signature was obtained.** This one determines all the others: a key, a signer, or a process.
2. **Whether the Bitcoin and Tron outflows belong to the same attacker.** The $5.57bn tally rests on wallet labelling Binance has not confirmed.
3. **Whether Binance will publish a proof of reserves** or a technical post-mortem. So far it has issued two statements, no detail, and no word «hack».
4. **What happens to the frozen funds**, and on what timetable.
5. **Which other exchanges run the same signing architecture.** EIP-7702 is not a Binance defect, it is a standard: anyone who delegates a hot wallet to a contract has the same attack surface, and nobody has published their controls yet.

An exchange is not a vault. It is a signing machine, exposed to the internet, and its risk is not measured by how much it holds but by how many people and how many machines can produce a valid signature on its behalf. The 93-cent fee for moving two and a half billion dollars is the list price of that architecture: near zero — and that is exactly the part of the problem no freeze can fix.

---
*Verified sources: CryptoTicker, «Binance Hack: $2.8B Drained From Hot Wallet via EIP-7702», 29 October 2026; Unchained, «Binance Says User Funds Are 'Completely Safe' After $3.5 Billion Drains From Its Hot Wallets», 29 October 2026; Decrypt, «Binance Drained of $5.5 Billion in Suspected Hack, Tether and Circle Freeze $1.8 Billion», 29 October 2026; posts by @binance (21:29 UTC), @cz_binance (21:15 and 22:23 UTC), @0xngmi, @paoloardoino, @jerallaire, @spreekaway, @odysseas_eth and @WazzCrypto of 29 October 2026, read via API; EIP-7702, specification at eips.ethereum.org. All sources consulted on 29 October 2026.*

---
title: "Nobody Breached Trezor or the BBC: Their Suppliers Got Breached"
date: 2026-11-17
draft: false
categories: ["Crypto", "Blockchain"]
tags: ["security", "supply chain", "Ledger", "Trezor", "Optimizely", "malware"]
summary: "Two attacks in 24 hours that came through third parties: infected scripts on 178 sites and 27,000 Trezor orders exposed. The perimeter is the supply chain"
url: "/en/2026/11/nobody-breached-trezor-or-the-bbc-their-suppliers-got-breached/"
---

Two security stories in twenty-four hours that look separate and tell the same thing: a compromised script carried malware that steals cryptocurrency and credit cards across 178 organisations, including Ledger, BBC, CNN and Salesforce; Trezor disclosed that a courier lost the data of roughly 27,000 orders. In neither case did the attack start with the company named in the headline.

## One hundred and eighty-eight files, one single vector

The Report URI analysis is detailed: on 16 November, through the Optimizely Web testing platform, malicious JavaScript was served to visitors of 178 organisations. Each customer loads from `cdn.optimizely.com` a snippet carrying its own experiment code and a custom JavaScript field; the attacker wrote his code inside that field, leaving the rest of the file intact, so it kept arriving from the trusted domain. Of the 1,611 snippets checked, 188 are infected, and the payload was rebuilt twenty-six times in a single day.

The malware swapped wallet addresses — Bitcoin, Ethereum, Tron, Solana, Ton, Litecoin, Bitcoin Cash, Dogecoin — validating checksums, including at the moment of copying to the clipboard; it intercepted card data entered into the site's forms, not the data inside payment providers' iframes; it stole cookies and screenshots. On iPhone and iPad it loaded a second stage tied to the Coruna and DarkSword exploit kits.

Optimizely confirmed the exploitation of a vulnerability in the account sign-up procedure for Experimentation accounts and said it had blocked the path, revoked tokens and sessions and stopped delivery through Cloudflare. How the attacker obtained that access remains unexplained.

## How much was stolen, cautiously

Here the numbers diverge. Report URI counted 7,040 dollars reaching the wallets as of 19:25 UTC; StepSecurity estimates 6,600 dollars; Alex Thorn of Galaxy Digital calculates that victims sent 2,300 dollars, because a good part of the incoming bitcoin was the attacker's own funds. The order of magnitude stays in the low thousands of dollars: the real damage, if any, is made of cards and cookies that leave no trace on-chain.

## The third time for Trezor

The second case is slower and more insidious. Skladon, the courier that ships for Trezor, suffered a breach on 7 November and informed the company on the 15th: about 27,000 orders involved, between 9 August and 7 November, with names, phone numbers, addresses, emails, products and prices. No wallet backups, no PINs. Trezor has enabled anonymous pickup in 18 European countries and is cutting order-data retention from 90 to 45 days. It is the third supplier breach in a year, after ShipMonk in August and Brevo in September.

## The perimeter is the supply chain

The lesson is uncomfortable: no perimeter defence covers a third-party tag or a courier. For anyone holding crypto, a leaked shipping record does more damage than it seems, because it links a person, an address and the fact that they hold crypto. Security has moved from protecting your own servers to verifying every link in the chain, including the ones you do not control.

---
*Verified sources: blog.report-uri.com, "World's Largest Brands Infected With Malware Via Optimizely" (16/11/2026, timeline and counts); stepsecurity.io, "OPTIMJACK" (17/11/2026, independent analysis and fund estimate); Cointelegraph, "Hackers inject credit card, crypto-stealing malware into 178 major websites" (17/11/2026, with Optimizely's statement and Alex Thorn's estimate); trezor.io/blog, "Data breach at Trezor shipping partner, Skladon" (15/11/2026, primary source with the exposed data); Cointelegraph, "Trezor customer data exposed in 3rd partner breach this year" (17/11/2026). The estimates of the amount taken are reported separately because they do not match. Not published: the CFTC/Backpack-tZERO item from the report, which rests on a single source with no corresponding statement on the agency's site.*

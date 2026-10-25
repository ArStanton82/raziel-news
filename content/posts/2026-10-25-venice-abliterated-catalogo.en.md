---
title: "A Model Without Refusals Does Not Make the Token More Valuable"
date: 2026-10-25
draft: false
categories: ["Venice.ai", "AI"]
tags: ["venice-ai", "abliterated", "uncensored", "vvv", "defillama"]
summary: "Abliterated Large Flash joins the Venice catalogue at $1.25 and $2.50 per million tokens. VVV sits at $24.6 and TVL is zero."
url: "/en/2026/10/a-model-without-refusals-does-not-make-the-token-more-valuable/"
---

On 22 October Venice added Abliterated Large Flash to its catalogue, an Abliteration model built on a DeepSeek V4.1-Flash-1017 base, in the same round that brought DeepSeek V4.1 Flash Uncensored. The sequence says something the individual announcements hide: the absence of refusals is no longer an experiment at the edge of the catalogue, it is a product line.

## What's inside, and what it doesn't promise

Abliterated Large Flash costs $1.25 per million input tokens and $2.50 output, with cached input at $0.13. It holds a one-million-token context and 128K of output, takes text and images, does tool calling, structured JSON and web search. Venice serves it quantised in FP8 and files it under the "anonymised" tier: prompts are handled transiently, not stored, not profiled, not used for training.

Abliteration strips from the internal representations the directions that produce refusal, so the model answers without the user having to build a jailbreak. The manufacturer's documentation, reproduced on the model's Venice page, nevertheless admits that some requests still get a refusal and that behaviour varies with the prompt. That is the difference between "reduces refusals" and "never refuses".

## Four hundred models, but the market is looking elsewhere

Venice's documentation lists 401 models, 140 of them text-only. The catalogue grows by accumulation, and the question is not which model is better but who pays the bill for this abundance.

VVV is worth $24.64, with a market cap around $1.2 billion and 24-hour volume near $21 million. $855.81 million in tokens is staked, 71.45% of the market cap: nearly three quarters of the project's value is locked in a contract. Protocol TVL as measured by DefiLlama remains zero — not through a measurement error, but because the methodology keeps staking as a separate series. The figure in today's report, $1.71 billion of TVL, does not exist on DefiLlama and should not be repeated.

On the revenue side, the last thirty days produced roughly a million dollars of on-chain fees, $4.37 million annualised and $3.86 million cumulative since December 2025: buybacks and burns of VVV only. Subscriptions, API and credits settle off-chain and do not appear in that figure. The price-to-revenue ratio is around 98 times, according to DefiLlama.

## The part nobody puts in the press release

The token is $34.53 below its all-time high of 21 September, so roughly 29% down: it recovered 9.6% in a week and lost 18.9% in a month, while the catalogue was expanding.

A model that never asks permission is a clear proposition, and Venice is one of the few platforms selling it without beating around the bush. But the proposition is about the product, not the token: whoever buys VVV is not buying access to those 401 models, they are buying a share of the buybacks. As long as on-chain revenue stays at a million a month, the catalogue can grow without the price noticing.

---
*Verified sources: docs.venice.ai/models/overview and docs.venice.ai/overview/pricing, consulted on 25/10/2026 (401 models in the catalogue, 140 text-only; Abliterated Large Flash, id `abliteration-abliterated-model-large-flash`, $1.25/$2.50 per million, cache $0.125, 1,000K context, anonymised tier, Uncensored capability); venice.ai/models/abliteration-abliterated-model-large-flash, consulted on 25/10/2026 (DeepSeek V4.1-Flash-1017 base, 128K maximum output, FP8, transient handling of prompts, manufacturer's note that some requests still receive a refusal); DefiLlama, defillama.com/protocol/venice, reading of 25/10/2026 (TVL $0, staking $855.81 million, 71.45% of mcap, 30d fees $1 million, annualised $4.37 million, cumulative $3.86 million, price $24.64, mcap $1.198 billion, volume $21.18 million, all-time high $34.53 on 21/09/2026, +9.6% over 7 days, −18.9% over 30 days, price-to-fee ratio 98.4x); sovyron.com/providers/venice, updated to 24/10/2026 (listing date of Abliterated Large Flash and DeepSeek V4.1 Flash Uncensored). Discrepancies noted: Echo's report indicated a Venice TVL of $1,711,627,447 and VVV at $24.49 with −0.5% over 24 hours; DefiLlama reports TVL of $0 by methodology — staking is a separate series — and a price of $24.64, so the draft describes the price level rather than the percentage change. The report's scan placed Abliterated Large Flash on 23/10, Venice's documentation on 22/10: the draft uses the documentation date. The Kimi K3.1 Pro story was not picked up because it was already the subject of the 24/10 draft.*

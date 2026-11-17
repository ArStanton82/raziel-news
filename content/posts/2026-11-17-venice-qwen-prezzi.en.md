---
title: "Venice Cuts the Price a Day After Launch: The Downward Race of Intelligence"
date: 2026-11-17
draft: false
categories: ["Venice.ai", "AI"]
tags: ["Venice", "VVV", "Qwen", "GLM", "inference pricing", "staking"]
summary: "Qwen 4 Max arrives with a 1M context and gets discounted 24 hours later. Meanwhile Venice's on-chain revenue stays in the millions"
url: "/en/2026/11/venice-cuts-the-price-a-day-after-launch-the-downward-race-of-intelligence/"
---

Venice added two model families to its catalogue in forty-eight hours and, for one of the two, has already corrected the price list. It is the kind of detail that disappears from press releases and that instead says a lot about where the private inference market is moving: price pressure no longer comes from competitors, it comes from the pace at which models ship.

## Two additions and one markdown

On 16 November the technical changelog records two arrivals. The first is GLM 5.3 Flash Uncensored: a 1,048,576-token context, FP8 weights published on Hugging Face, execution classified as private, at 0.165 dollars per million input tokens and 0.55 output — cache reads cost 0.033. The second is Qwen 4 Max, a one-million-token context, text, image and video input, up to 393,216 output tokens, privacy stated as anonymised.

The next day, 17 November, the changelog carries a single entry: Qwen 4 Max prices fall. Input from 1.875 to 1.50 dollars per million, output from 5.625 to 4.50, cache reads at 0.075. A twenty per cent cut twenty-four hours after the debut. On the comparison price list in the documentation the model's blended price sits at 2.25 dollars per million, just above GPT-6.1 Terra's 2.00 and below Muse Spark Open's 2.50.

## The comparison Venice makes with itself

In the announcement post the company argues that Qwen 4 Max built the same 3D scene "in less than half the time and cost" compared with Qwen 3.8 Max. It is an internal measurement, not an independent test, and should be read as such. It does have one virtue: it moves attention from benchmark scores to cost per finished piece of work.

## The token, which lives on something else

On the market VVV is worth a little over 21 dollars (21.22 on CoinGecko, 21.20 on DefiLlama in the morning readings), with a market cap around 1.04 billion and volume at 51.8 million in 24 hours; 49 million tokens circulate out of 81.26 million issued. But the structural figure is another one: DefiLlama records 729.23 million dollars in staking, 70.21 per cent of the market cap. The protocol's TVL, by the aggregator's declared methodology, stays at zero: staking is a separate series and must not be added.

On the other side of the ledger, cumulative fees are 4.83 million dollars, of which 855,584 in November (the month includes the buyback of about 458,000 dollars on 9 November) and 1.06 million in October. Those are VVV bought back and burned: the on-chain shadow of revenue, not revenue. Subscriptions, API and DIEM credits settle off-chain and DefiLlama excludes them by choice.

The point, then, is this: Venice's valuation does not rest on visible revenue, it rests on almost three quarters of the supply locked in staking. It is a bet on perpetual access to compute, not on billing. As long as per-token prices fall, that bet becomes cheaper to make and harder to measure.

---
*Verified sources: docs.venice.ai/changelog (entries of 16 and 17 November 2026, with prices before and after the cut); docs.venice.ai/models/qwen-4-max and docs.venice.ai/models/glm-5-3-flash-uncensored (technical sheets, consulted on 17/11/2026); defillama.com/protocol/venice (TVL $0, staking $729.23m = 70.21% of market cap, cumulative fees $4.83m, monthly series); coingecko.com/en/coins/venice-token (price, market cap, volume, circulating supply). Discarded: the "Venice TVL" of $1.409bn reported by the radar, since the DefiLlama page shows $0 and keeps staking as a separate series. The 24-hour percentages were not published because the sources gave non-matching values.*

---
title: "DeepSeek 1017 on Venice: the same model, a different bill"
date: 2026-10-19
draft: false
categories: ["Venice.ai", "AI"]
tags: ["deepseek", "privacy", "vvv", "models"]
summary: "DeepSeek V4.1 Flash build 1017 lands on Venice at 0.30 dollars per million tokens, while VVV slides and subscriptions climb."
url: "/en/2026/10/deepseek-1017-on-venice-the-same-model-a-different-bill/"
---

On 17 October DeepSeek published build 1017 of V4.1 Flash. On the 18th Venice made it available in the app and through the API under the identifier `deepseek-v4-1-flash-1017`. The interesting part is what changes for the people using it, and at what price.

## What is inside build 1017

Venice's technical sheet describes a 552-billion-parameter Mixture-of-Experts with a Causal Encoder-Decoder architecture, 8 billion active in prefill and 16 in decode, a one-million-token context, native vision and open weights on Hugging Face. The original version shipped on 10 September: 1017 is an update, not a new model. The number that matters to anyone paying is the price list: 0.30 dollars per million input tokens and 1.20 for output, with cached input at 0.01, against 3.75 and 18.75 for Kimi K3 on the same platform. Venice itself concedes the limit: on long, autonomous terminal work the model still trails the best closed ones.

## Privacy has tiers, and they are worth reading

The delicate point is the word "private". Venice places the model in the zero-retention tier: prompts, images and outputs are not stored, profiled or used for training. But the FAQ on the same page is explicit: the model does not run inside a TEE and traffic is not end-to-end encrypted; the guarantee is a no-logging policy, not hardware isolation. It is a technical distinction that becomes a political one the moment you choose where to send sensitive data. "We don't keep it" and "we can't read it" are two different promises, even when marketing stacks them on the same row of badges.

## The price falls, usage rises

Meanwhile the protocol's token tells the opposite story. VeniceStats' weekly W42 report, published today, puts VVV at 22.77 dollars, down 8.0% over seven days, with Pro sign-ups up 18.4% to 21,935 — an eighth consecutive week of growth, 3,406 new subscribers — and credit purchases at a new daily high of roughly 276,814 dollars. The same report flags the Pro+ share down to a low of eight weeks, at 6.0%. Over the last 24 hours the price has bounced: about 24.1 dollars, up 7.8%, a market capitalisation of 1.17 billion, 842 million VVV in staking, 71.8% of the market cap.

## The metric that isn't there

DefiLlama shows Venice with a TVL of zero dollars: staking is tracked as a separate series, outside TVL. The figure of 1.68 billion circulating in the first drafts of this story finds no support in the cited source. In a sector where metrics are also sales arguments, the difference between "locked" and "TVL" is the difference between a thesis and a number.

What remains is the picture: a cheaper and more capable model, a token losing price while usage grows, and a platform that states its own limits honestly. It is a market starting to tell apart those who own the model from those who own the relationship with the people using it.

---
*Verified sources: model page venice.ai/models/deepseek-v4-1-flash-1017 and FAQ (19/10/2026); pricing table docs.venice.ai/overview/pricing (19/10/2026); VeniceStats weekly report W42 of 19/10/2026 (venicestats.com/insights and @venicestats post); CoinGecko, Venice Token page (19/10/2026); DefiLlama, Venice protocol page (19/10/2026). Discrepancy found: the 1.68bn dollar TVL given in Echo's report does not match DefiLlama, which reports 0 dollar TVL and treats staking as a separate series; the text uses the verified figure.*

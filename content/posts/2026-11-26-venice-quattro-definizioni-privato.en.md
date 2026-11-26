---
title: "Four ways of saying «private»: the week Venice AI had"
date: 2026-11-26
draft: false
categories: ["Venice.ai", "AI"]
tags: ["Venice", "VVV", "privacy", "artificial intelligence"]
summary: "Accusations of routing to third parties and of substituted models put the word Venice built its product and its token on to the test."
url: "/en/2026/11/venice-four-ways-of-saying-private/"
---

Venice built everything — product, customers, token — on a single word. The week closing today shows how elastic that word is: not because of an outside attack, but because the company's own pages define it in ways that don't add up.

## The allegations, and how much they weigh
A researcher writing as "ada cyborg" argued on 26 November that Venice forwards many requests — image generation above all — to third-party providers (DeepInfra, Fireworks, Baseten, Parasail, fal.ai), transmits public keys unencrypted, keeps seven database tables out of twenty-one unencrypted and, on 25 November, returned output from models other than the ones selected. Add KTibow's probe of 21 November: for 14 of the 18 image models Venice lists on OpenRouter, the partners would have been the ones downloading the test images. KTibow declared conflicts of interest (a competing marketplace, OpenRouter credits, possible VVV trading). No independent check, no audit: these are allegations, and that is how they should be read. Venice has not answered publicly.

## What its own pages say
The strong point isn't a researcher's post, it's the comparison between official documents, read today. The `llms.txt` file says Venice "does not store prompts or outputs on its private models". The privacy page lists four tiers and, for the one called "Private", writes: inference runs "on GPUs controlled by Venice or on zero-retention partner infrastructure", with an explicit note — "trust-based: it relies on Venice and its partners honouring their contracts". The same page puts GPT, Claude and Gemini in the "Anonymous" tier, where the user is told to "assume the provider is logging". The difference between "self-hosted" and "partner" is not a semantic detail: it is the difference between an enclave and a contractual clause. The parts that can be verified technically are TEE and E2EE, reserved for Pro subscribers.

An independent check, a small one, is possible: the public list of zero-retention endpoints on OpenRouter today held 32 Venice endpoints out of roughly 950. It is a self-certification by the provider, not proof.

## The price of the word
On the market VVV was worth around $27.6 today, according to DefiLlama, with a market cap just above $1.36 billion and some $905 million staked (two thirds of the market cap); TVL stays at zero by the aggregator's methodology. Outlets report a fall of more than 15% after the allegations, yet CoinGecko's 6 a.m. snapshot had it up 10.5% at $27.66: when two readings 24 hours apart contradict each other, the percentage doesn't get published. The level stands, about 20% below the all-time high of $34.53.

The on-chain buyback tells the solid part of the story: $1.08 million in fees in November, $5.05 million cumulative. Against a $1.36 billion market cap, that is 0.4%: the promise of privacy, today, is worth more than the flow behind it. Which is why the vocabulary matters. Anyone using Venice should read the privacy tier, not the adjective.

---
*Verified sources: venice.ai/privacy and venice.ai/llms.txt (read on 26 November 2026); Crypto Briefing, "Venice AI faces privacy allegations as VVV drops over 15%", 26 November 2026; Sulat AI & Tech News, "Venice AI 'private' claims vs its docs and KTibow's probe", 26 November 2026; direct count of the OpenRouter API `/api/v1/endpoints/zdr` (26 November 2026); DefiLlama, Venice protocol page (26 November 2026).*

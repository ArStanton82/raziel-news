---
title: "From Credit to Clock: Hermes Agent Rewrites Its Subscriptions"
date: 2026-10-28
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes-agent", "nous-research", "subscriptions", "cloud-agent", "plugin"]
summary: "Nous Research replaces the monthly block of credits with daily and weekly limits and puts a cloud agent in every plan."
url: "/en/2026/10/from-credit-to-clock-hermes-agent-rewrites-its-subscriptions/"
---

On 27 October Nous Research announced a revision of Hermes Agent's subscriptions with a phrase that sounds like a commercial detail and instead shifts the product's centre of gravity: every new plan includes a cloud agent, and usage is governed by daily and weekly limits in place of a single monthly block of credits.

## What actually changes

The difference is not in the figures but in the shape of time. On Nous Research's official page you read that daily usage resets after 24 hours and weekly usage after seven days, counted from the first use of each window, while the monthly allowance and the cap reserved for the most expensive models renew with the billing cycle. The three tiers are not alternatives: they add up. A daily reset does not restore capacity if the weekly or monthly limit is already spent.

What is included changes too: hosting for one cloud agent, use of the hosted models and tools move into the allowance; requests made with your own API keys and additional cloud agents stay pay-as-you-go, on credits. Once the quota is gone there are three ways out: a free model, waiting for the reset, or buying credit.

## Why it is an architectural choice

An agent that lives in the cloud is not a chatbot: it runs at night, watches feeds, executes scheduled jobs. The old monthly-credit model treated that time as a tank to be emptied, and whoever emptied it in the first two weeks sat still. Short windows spread capacity across the period, but they take away a freedom: unspent capacity does not accumulate for a later peak. You gain predictability and you lose accumulation.

The move is consistent with the rest of the week. In the same days came the official plugin for ElevenLabs sound effects, with a dedicated tool, the sound library on desktop and the generation of variants. The official catalogue grows while the runtime becomes a subscription service: two faces of the same design, that of an always-on agent that no longer asks the user to manage machines.

## What stays the same

What stays is the point that makes the discussion bearable: Hermes Agent remains open source and MIT, and the Portal is the optional hosted layer. Whoever installs locally pays nobody for the agent's time, except the model provider they choose.

The editorial question, then, is not whether the caps are fair. It is whether the agent's time is becoming the natural metric of software that reasons: no longer how many tokens you burn, but how long you can leave it switched on.

---
*Verified sources: @NousResearch post of 27 October 2026; official nousresearch.com page with the FAQ on plans, resets and usage (consulted 28 October 2026); AlphaSignal, "Nous Research Rebuilds Hermes Agent Pricing Around Always-On Cloud Hosting" (27 October 2026); AICrier, "Hermes Agent Adds Cloud To Plans" (27 October 2026); official documentation of the elevenlabs-sound-effects plugin on hermes-agent.nousresearch.com (28 October 2026). Note: at the time of checking, the Portal price list still showed the old monthly-credit wording; that is why the article gives no figures by tier. Echo's report indicated 2,482 likes and 279,884 views for the post: the X page consulted reports 1.1K likes and 121K views, so the social metrics were left out.*

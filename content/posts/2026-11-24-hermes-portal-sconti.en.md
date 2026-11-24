---
title: "Eighty per cent on one side, twenty on the other: the geography of discounts in the Nous Portal"
date: 2026-11-24
draft: false
categories: ["Hermes", "AI"]
tags: ["Nous Portal", "pricing", "DeepSeek", "Claude", "Arachne Flow"]
summary: "Nous Portal takes 80% off DeepSeek V4.1 Flash 1017 and 20% off the frontier models: the gap between the two discounts shows where the margin is."
url: "/en/2026/11/eighty-per-cent-on-one-side-twenty-on-the-other-the-geography-of-discounts-in-the-nous-portal/"
---

In the night of 24 November Nous Research announced that DeepSeek V4.1 Flash 1017 costs 80% less for ten days, «thanks to DigitalOcean». The evening before it was promising the latest Anthropic and OpenAI models at 20% off for a week. Two different orders of discount: it is not a commercial detail, it is a map of margins.

## The spread, in dollars

The Portal's models page makes the numbers verifiable and they are sharper than the posts. DeepSeek V4.1 Flash 1017 sits at 0.03 dollars per million input tokens and 0.12 for output, against a list price of 0.15 and 0.60: 20% of full price. Claude Opus 5.5 sits at 3.20 and 16.00 against 4.00 and 20.00; GPT-6.2 Sol at 1.60 and 8.00 against 2.00 and 10.00. Between the model discounted by 80% and the one discounted by 20% runs a factor of 107 on input and 133 on output: a million output tokens costs twelve cents on one side and sixteen dollars on the other. In the same table 50% discounts coexist with another 80%: the scale is not binary.

## Who pays for the discount

The post attributes the DeepSeek promotion to a contribution from DigitalOcean, without explaining the mechanism: donated compute, credit, or simply covering the difference. It is the detail that separates a structural cut from a campaign. That it is a campaign is said by the windows — ten days, one week — and by the Portal's history: an independent price tracker (tokenplans.dev) documents on Nous Portal a 20% promotion on all models running since July and a -90% on DeepSeek V4 Flash since August. The promotional price, in short, is the stable exception of this catalogue, not its list price. For anyone choosing a model it is worth looking at the column that is not struck through: that is the one you pay when the campaign ends.

## The catalogue as a moat

The plugin catalogue has meanwhile absorbed Arachne Flow, a node canvas for Hermes Desktop: the pull request (#153240) was merged on 12 November, the author is a third party (EmotionalThrifty) and the official card describes an editor with triggers (schedule, RSS, webhook), LLM nodes, Hermes tools and MCP servers. Teknium, in a reply, added that «a bot market» is coming to Hermes Market: a statement, not an announcement with a date. The point, though, stands: if your work lives in a graph of nodes saved in a catalogue, changing supplier costs more than the discount saves.

The discounts say that inference on commodity models is becoming an almost irrelevant line of cost, and that on frontier models prices are still rigid. The catalogue says that competition has moved elsewhere: from how much a token costs to where the work that consumes that token lives. Read together, the two pieces of news tell the same strategy — enter through the price, stay through the ecosystem — and it is worth remembering that the first of the two numbers has an expiry date.

---
*Verified sources: portal.nousresearch.com/models (consulted on 24/11/2026: point-by-point prices and discounts, including struck-through list prices); @NousResearch posts of 23/11/2026 (19:19) and 24/11/2026 (00:28), reprinted by nousresearch.com; tokenplans.dev/changelog (consulted on 24/11/2026: history of the Portal's promotions); hermes-agent.nousresearch.com/marketplace/arachne-flow (consulted on 24/11/2026); PR NousResearch/hermes-agent #153240, merged on 12/11/2026 (verified via the GitHub API); @Teknium post of 23/11/2026 on the bot market (from Echo's report, not verified independently).*

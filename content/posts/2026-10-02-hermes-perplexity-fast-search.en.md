---
title: "Web search goes free: Hermes hands its answers to Perplexity"
date: 2026-10-02
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes", "perplexity", "agents", "web-search", "nous-research"]
summary: "Perplexity Fast Search becomes the default web search for Hermes Agent, free on every Nous Portal tier: it changes the cost of autonomy."
url: "/en/2026/10/web-search-goes-free-hermes-hands-its-answers-to-perplexity/"
---

There is a cost that never shows up on the model's invoice, and yet decides how autonomous an agent can afford to be: the price of looking outside. A single web search looks like a detail, but multiplied by hundreds of runs a day it stops being a detail and becomes the real ceiling on autonomy. That is the point the news from Nous Research lands on.

## A search built for agents

Hermes Agent can now use Perplexity as the backend for its `web_search` and `web_extract` tools, and Perplexity's official documentation lists Fast Search as the default search, free for Hermes users. No API key is needed: those who want more can configure the paid standard search with their own key. Fast Search is built on Photon, the engine designed specifically for agents, and aims at low latency — around 160 ms at p50 and 230 ms at p95 per call. These numbers matter more than they seem: an agent verifying ten facts in a loop cannot afford to wait ten times for a slow answer.

## The marginal cost of knowledge

The move is interesting because it does not add capability, it changes the price. A more powerful model is paid for by the token; a free search costs, in practice, zero. When the marginal cost of consulting the world collapses, an agent's rational behaviour changes: it becomes worth verifying rather than assuming, searching rather than remembering. That is the difference between an assistant answering from memory and one checking. For anyone building automated pipelines like this one, it is the kind of detail that moves a project more than a model update.

## An ecosystem in motion

The context helps to read the announcement. Nous Research has confirmed NousCon 2026 for 30 October in New York, the community's first public gathering after a year of growth for the open-source agent. The `hermes-agent` repository meanwhile continues its daily development. There is one discrepancy worth flagging: the reference report dates the announcement to 1-2 October, while some outlets place it on 24 September. The substance — Fast Search as default and free — is confirmed by the official documentation; the exact date of the announcement remains uncertain and we do not use it as a fact.

Free search is not a promotion, it is infrastructure. If the cost of knowing tends towards zero, the interesting question stops being "what does the agent know" and becomes "what does it choose to verify". And that is where the quality of automated work will be decided in the coming months.

---
*Verified sources: Perplexity official documentation (docs.perplexity.ai, consulted on 2026-10-02); Nous Research, official site and X account @NousResearch (2026-10-02); Runtimewire, analysis of the announcement (2026-10-02); GitHub NousResearch/hermes-agent (2026-10-02). Note: the date of the Fast Search announcement differs between sources (24 September vs 1-2 October).*

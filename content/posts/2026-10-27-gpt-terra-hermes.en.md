---
title: "GPT-6.1 Terra Lands in Hermes Agent: the Model Becomes a Line Item"
date: 2026-10-27
draft: false
categories: ["Hermes", "AI"]
tags: ["Hermes Agent", "GPT-6.1 Terra", "Nous Portal", "OpenRouter", "models"]
summary: "GPT-6.1 Terra is in Hermes Agent from release day: $1/$5 per million and a 1.05M context. What changes for people building agents."
url: "/en/2026/10/gpt-6-1-terra-lands-in-hermes-agent-the-model-becomes-a-line-item/"
---

On 26 October OpenAI presented GPT-6.1 Terra, the efficient model in the family: visual reasoning, computer use and writing, with a 1.05 million token window. For anyone working with Hermes Agent the news is not the model itself but the speed at which it entered the catalogue: the same day Teknium announced availability through Nous Portal and OpenRouter, and a commit in the main repository ("feat(models): list gpt-6.1-terra on OpenRouter and Nous Portal") made the addition real, with the context fallback at 1,050,000 tokens and the catalogue manifest regenerated.

## One dollar in, five out

On Nous Portal Terra costs 1 dollar per million input tokens and 5 for output; in batch, 0.50 and 2.50. These are the same prices as the OpenAI API. The comparison that matters is not with the model it replaces but with the frontier ones: on Venice Astra costs 12.50 and 62.50, an order of magnitude more. OpenAI claims that on computer use tests Terra "nearly matches" Astra. It is a press-release formula, but it moves the point.

## Why it matters for an agent

An agent does not consume tokens once: it consumes them in a loop. The difference between 62 and 5 dollars per million output tokens is not a marginal saving, it is the difference between a loop you can leave running and one you have to watch by hand. Anyone designing pipelines — like this one, which every morning reads feeds, checks sources and writes — knows that the bottleneck shifts from the cost of a single pass to the number of passes worth attempting.

## The catalogue's two speeds

One substantive detail remains: the model is also reachable from the development build, by switching the release channel from "stable" to "main". Which means whoever tries it today accepts living a little ahead of the official release. The main repository is meanwhile at 257,538 stars and has received pushes in the last hours; hermes-labs-plugins, the experimental plugin repo, is at 131. Numbers that say one simple thing: the ecosystem moves at the speed of the catalogue, not of the individual model.

The useful question, then, is not how good Terra is, but how many times we can afford to let it be wrong. On that, price is a function of the product at least as much as the benchmark is: a model that costs a tenth can be put through ten trials, and the quality of an agent is mostly made of attempts.

---
*Verified sources: OpenAI, "Introducing GPT-6.1 Terra" (26 October 2026); commit a382af2 on NousResearch/hermes-agent, "feat(models): list gpt-6.1-terra on OpenRouter and Nous Portal" (26 October 2026); Nous Portal, model price list (read on 27 October 2026); OpenAI API, gpt-6.1-terra page (27 October 2026); GitHub API for the stars on hermes-agent (257,538) and hermes-labs-plugins (131), read on 27 October 2026. Note: the reference to the "main" channel comes from Teknium's post and has no second independent source.*

---
title: "Hermes Index: measuring agents on real cost, not just on score"
date: 2026-10-07
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes-agent", "benchmark", "nous-research", "cost-per-task", "agents"]
summary: "Nous Research publishes Hermes Index: four benchmarks inside Hermes Agent, with the average cost per task next to the score."
url: "/en/2026/10/hermes-index-cost-per-task/"
---

When you choose a model for an agent, the score on its own says little. What matters is what that score costs, task after task. That is the premise of Hermes Index, the index published on 6 October by Nous Research: four evaluation suites run inside the same Hermes Agent harness, with the average cost per task next to the average result.

## Four tests, one workbench

Hermes Index averages four suites: Hermes Bench, a new benchmark from the same team, TerminalBench 4, TerminalBench Science and SkillsBench. Every model runs under the same rules — pass@1, a single attempt per task — and with reasoning set to "high" where available. The result is not a ranking of abstract intelligence but a measure of how well a model behaves when real work is entrusted to it inside an agent. At the top is Claude Opus 5.5, with 63.31 points at 4.99 dollars per task; GPT 6 Astra follows (56.25 points, but 11.61 dollars per task) and then Claude Sonnet 5.5 (53.14 at 2.82 dollars).

## The interesting part is the tail of the ranking

The most useful figure sits lower down. DeepSeek V4.1 Flash scores 36.91 at 0.259 dollars per task; Ling 3.0 Flash reaches 21.56 at roughly 5 cents. Nous lists six models on the Pareto frontier — those that, at equal cost, nobody else beats — and the list tells a simple story: for many agent tasks a cheap, fast model is the rational choice, while the "best" model stays for the hard jobs. That is exactly why Hermes distinguishes a main model from auxiliary models, used for side tasks such as vision, session titles or context compression.

## Skills and plugins from the chat, memory out of the core

Two more changes arrive in the same window. Hermes Desktop can now search for and install plugins and skills straight from the conversation, without going through the terminal: the search across the Plugin Catalog and the Skills Hub happens in chat, with a confirmation card before installation. And memory providers keep leaving the core: holographic and byterover now have standalone repositories marked "unmaintained", with the exit set for 15 October 2026, when anyone using them will have to move to the corresponding plugins.

## One index, one question

Hermes Index does not say which model is best in absolute terms. It says something more uncomfortable and more useful: that in agentic work cost is part of the result. The question is no longer "how good is it", but "how good is it for what it costs".

---
*Verified sources: portal.nousresearch.com/bench (accessed 7 October 2026); nousresearch.com (7 October 2026); alphasignal.ai/news/nous-research-s-hermes-index-ranks-ai-agents-by-score-and-real-cost (7 October 2026); Hermes Agent documentation — Plugin Catalog, Skills, Memory Providers, Configuration (7 October 2026); github.com/NousResearch/hermes-plugin-holographic and hermes-plugin-byterover (7 October 2026).*

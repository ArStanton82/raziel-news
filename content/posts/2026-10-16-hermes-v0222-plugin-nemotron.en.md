---
title: "Hermes Agent v0.22.2: the patch that reopens the front door"
date: 2026-10-16
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes-agent", "nous-research", "release", "plugin", "nemotron", "open-source"]
summary: "Nous ships patch v0.22.2, opens an official plugin catalogue and measures Nemotron 3.5 Super VL on Hermes Bench: 63.44."
url: "/en/2026/10/hermes-v0222-plugin-nemotron/"
---

On 15 October Nous Research published Hermes Agent v0.22.2. On paper it is a patch, but the changelog is explicit: v0.22.1 had been built from the wrong commit, shipping unreleased work on the gateway, and today's version is what 0.22.1 should have been. It is the kind of transparency an open source project can afford, and worth recording.

## A patch that admits the mistake

The main defect concerned the front door: after a restart, Linux can assign an early PID to an unrelated process, and the supervised gateway — systemd, launchd, Docker — could mistake it for a gateway already running and refuse to start. Hermes now records the boot it was born in and, when it cannot be certain, queries the host lock, which only a live gateway holds. The second fix concerns long turns with local models: streaming requests show prompt-reading progress, stall timers ignore time when the machine was suspended, and a recovered local server gets a second attempt instead of a circuit breaker that failed every subsequent message. One known issue remains and is declared: sessions started under gateway 0.22.1 cannot be deleted in 0.22.2.

## Plugins become an official catalogue

On the ecosystem side, the NousResearch organisation has consolidated its first-party plugins into a single repository, `hermes-official-plugins`, where each plugin lives in its own directory and installs in one line from the catalogue. The repo has absorbed the history of earlier projects, such as the plugin for the Claude subscription, now archived in favour of the new common home. This is maintenance, not expansion: the same direction as the shrunken codebase, but applied to the plugin surface.

## Hermes Bench as scoreboard

The most cited figure of the week comes from NVIDIA: Nemotron 3.5 Super VL, an open model with 120 billion parameters and 12 billion active, scored 63.44 on Hermes Bench — above Nemotron 3 Ultra's 56.33 — with throughput up to five times higher than comparable local models. That an in-project benchmark has become the yardstick a chipmaker uses to measure its own models says something about the weight Hermes is gaining as a reference platform.

In the background remains the Series B of 90 million at a 1.5 billion valuation, led by Robot Ventures, with the capital earmarked for «Hermes for Businesses». The project keeps growing on two opposite fronts: repairing the details that stop the agent from starting, and building the context in which companies adopt it.

---
*Verified sources: github.com/NousResearch/hermes-agent/releases (release v0.22.2, 15 ottobre 2026); releases.sh/nousresearch/hermes-agent e hermes-agent.ai/changelog (consultati il 2026-10-16); github.com/NousResearch/hermes-official-plugins e github.com/orgs/NousResearch/repositories (catalogo plugin, aggiornato il 15 ottobre 2026); developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning (Hermes Bench 63,44); nousresearch.com (annuncio Nemotron 3.5 Super VL); sidley.com, techcrunch.com, startupfortune.com e techfundingnews.com (Series B 90 M$ a 1,5 mld $, 7 ottobre 2026).*

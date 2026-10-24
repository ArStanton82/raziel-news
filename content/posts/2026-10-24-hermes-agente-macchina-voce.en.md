---
title: "The Agent Takes a Machine and a Voice"
date: 2026-10-24
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes", "plugin", "cua", "voice", "agents"]
summary: "Hermes leaves the desktop: an isolated Space anyone can watch live, plus a voice, move the place where the agent lives."
url: "/en/2026/10/the-agent-takes-a-machine-and-a-voice/"
---

For two days the Hermes community has been arguing about two plugins, not about a model. That detail says a lot: the bottleneck for an autonomous agent is no longer how well it reasons, but where it runs and who can interrupt it.

## A machine that isn't yours

The cua-spaces plugin, from the trycua team, has been in the official catalogue since version 0.4.0, verified tier, and it is the most interesting thing this week. It moves terminal, files and code inside a Space: an isolated Linux, macOS or Windows machine, on hardware you already own or in your cloud account. It is enabled with one command, `hermes config set terminal.backend cua`, and from that moment every command lands there instead of on your laptop.

Two consequences matter more than the rest. The first is oversight: the Space has a live view, so anyone on the team can watch, step in, hand control back and let the agent carry on. The second is security: because the Space is already the sandbox, Hermes stops asking for confirmation on risky commands executed inside it. It is an explicit bargain — less friction in exchange for a perimeter — and it is worth reading as exactly that.

## Voice as an orchestration surface

The second plugin is hermes-talk, from the community, not from Nous. It adds real-time two-way voice: you speak, the agent answers aloud and meanwhile uses its real tools, delegates work in the background and reports results as they arrive. It works in the terminal with `hermes talk`, in a Discord voice channel and in the Talk tab of the dashboard. The practical trick is authentication: it can lean on a ChatGPT subscription via Codex login or on an X Premium account, with no API key. The catch is in the catalogue details: live mode runs through an undocumented endpoint, outside the vendor's published terms, and can stop working without notice.

## The release that clears the ground

In the background, the v0.22.5 patch of 22 October: 81 pull requests, 231 non-merge commits across 804 files. The curated notes will arrive with 0.23.0, but the list already signals the direction — swappable delegation backends, subagents routed by model map or profile and changeable per session, `hermes mcp serve` and the Singularity backend moved from the core to plugins.

## The question that remains

An agent with a machine of its own, a voice that can interrupt it and backends that swap on the fly is an agent that looks less and less like a chatbot and more and more like a colleague with network access. The hard part will not be installing the plugin: it will be deciding who answers for what that machine does at three in the morning.

---
*Verified sources: Hermes plugin catalogue, cua-spaces page (v0.4.0, verified tier, `terminal.backend cua` backend, requirements Hermes ≥0.21.6), consulted on 24/10/2026; Nous Research announcement of 22/10/2026 on X and on nousresearch.com; GitHub repository TheSmokeDev/hermes-talk and its README, consulted on 24/10/2026, plus the TheSmokeDev catalogue entry; GitHub, Hermes Agent v0.22.5 release (released 23/10/2026 05:28 UTC, release date 22/10/2026), consulted on 24/10/2026. Note: Echo's report attributed an MIT licence to hermes-talk; this could not be confirmed on the repository page, so the draft does not report it. The Meshy plugin and the availability of Kimi K3.1 Pro on Nous Portal, both present in the report, were not used as the main news: the first is promotional, the second is reported only by community accounts.*

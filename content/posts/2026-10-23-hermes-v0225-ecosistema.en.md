---
title: "Hermes 0.22.5: the computer you share"
date: 2026-10-23
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes-agent", "nous-research", "plugin", "agentic-ai"]
summary: "Patch 0.22.5 with 81 PRs and release notes deferred to v0.23.0; meanwhile Trycua's Spaces plugin widens the Hermes ecosystem."
url: "/en/2026/10/hermes-0-22-5-the-computer-you-share/"
---

On 23 October at 05:28 UTC teknium1 tagged v0.22.5 of Hermes Agent. The date declared in the release body is 22 October, the commit is bf0203a: the gap between the two dates tells you what kind of release this is, a technical roll-up rather than a launch. The curated notes will arrive with v0.23.0, which will cover the whole period from v0.22.0 onwards. That is a stated choice, not an oversight.

## What's inside the window

The numbers are the ones a maintainer checks before signing off: 231 non-merge commits across 804 files, +35,212 and −17,885 lines, 81 pull requests and 30 closed issues. Inside are changes that touch the way the agent installs itself and is governed: Nous sign-in becomes a single device login and free-tier users move from guest to their own account; usage-window plans arrive; delegation backends become replaceable, so subagents get routed by model map or by profile. Then the details that show how far the product is separating itself from the core: `hermes mcp serve` and the Singularity backend leave the core and become plugins, while Electron 44 closes the dependency account.

## The computer you share

The most interesting piece of the week is not in the release. It is Trycua's Spaces plugin, announced on 22 October: it gives Hermes a Linux, macOS or Windows environment on hardware the team already owns. Anyone can open it, watch in real time, step in and then hand control back while the agent keeps working. One clarification is worth making, and it is not in the official post — Teknium added it in the comments: the plugin is maintained by Trycua, not by Nous. It is the same logic as the release: the core gets lighter, the ecosystem takes on the weight.

## A plugin, commercial ones too

On the other side there is Meshy, which in its announcement offers a month of the Pro plan for one dollar: API access and a thousand credits, against the twenty dollars listed as list price. Installation goes through `hermes plugins install meshy` and a key pasted into settings. It is not a technical story, but it says where the project is heading: plugins are also a distribution channel, and the agent becomes the point of access to third-party services.

## Sovereignty, said out loud

The picture closes with the conversation between Dillon Rolnick and Matthew Prince, hosted by USV: agents, the future of the internet, digital sovereignty. No transcripts or summaries appear to have been published by either company, so the content remains the video attached to the post. It is, however, the thread that holds the rest together — a computer shared with the team, a plugin that brings commercial services inside, a core that empties itself out. The question is no longer what Hermes can do, but where its jurisdiction ends.

v0.22.5 is a minor release that says something large: the project is moving complexity out of the core and responsibility into the ecosystem. The v0.23.0 notes will be the first reckoning, and they will be worth reading while looking at what went out, not only at what came in.

---
*Verified sources: GitHub, NousResearch/hermes-agent release v0.22.5 (23 October 2026); @NousResearch post on X of 22 October 2026 (Spaces plugin, Meshy offer, Rolnick-Prince conversation); @Teknium post on X of 22 October 2026 (plugin maintenance handed to Trycua). Note: the "official plugin" label for the X Chat plugin, reported by @HermesWatcher, found no confirmation on the Announcements page of nousresearch.com and has not been included; @adolandev's OSINT project is excluded as amateur.*

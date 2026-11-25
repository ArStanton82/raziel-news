---
title: "Hermes 0.23.4: the quietest patch is the one with the most work inside"
date: 2026-11-25
draft: false
categories: ["Hermes", "AI"]
tags: ["Hermes Agent", "release", "plugin", "Nous Research", "Desktop"]
summary: "Two hundred and twenty-nine PRs under a tag called patch: 0.23.4 closes three months of work and postpones the curated notes to 0.24.0."
url: "/en/2026/11/hermes-0-23-4-the-quietest-patch-is-the-one-with-the-most-work-inside/"
---

On 24 November at 08:17 UTC Nous Research published release v0.23.4 of Hermes Agent, flagged «Latest». The body of the release dates it 23 November: a one-day discrepancy, small but real, worth noting because it is the only approximate detail in an otherwise precise document. The rest is a paradox: the release calls itself a «patch», and contains a quarter's worth of work.

## The number that counts

From tag v0.23.3 to this one, measured at commit `8fc0374`, there are 229 merged pull requests, 1,122 non-merge commits, 1,316 files changed (+96,873 / −6,703) and 281 issues closed. These are development-cycle figures, not hotfix figures. The explanation is in the note itself: the tag gathers everything under one stable label for the GitHub release, the Microsoft Store, Docker and Hermes Cloud, while the full curated notes — «nothing in this window is skipped» — will arrive with v0.24.0. Anyone reading only the changelog, in short, does not know what they have installed.

## Four things the note says

Three new Gemini 4 models (Hydrogen, Neon, Carbon) on Nous Portal, OpenRouter and Vertex, with a precise technical rule: `xhigh` is accepted only by Hydrogen and Neon, and on Gemini 4 thinking cannot be switched off. Then `hermes plugins config`, which brings the fields of the Desktop page into the terminal, separating validated settings from secrets in the profile's `.env`. Then `hermes dashboard password`, which sets the password without a TTY prompt, with scrypt hashing and the precedence of environment variables made explicit. Finally `hermes gateway migrate --backends`, which starts with a read-only inventory and touches no service until it is asked to.

## The desktop waits, the phone does not

Anyone who installed the Desktop app from an .exe or .dmg sees nothing change: they will update with the next bundle. The redesign is expected «early next week» according to answers from Teknium and HermesWatcher, so a hint, not a date. Meanwhile the official catalogue has taken in Bark, which brings job notifications to iPhone: `--deliver bark`, `hermes send --to bark`, a dedicated tool. The marketplace entry is unusually honest about the limits — it is a one-way channel, there is no delivery receipt, a 200 only means «queued towards APNs», automatic pushes are off by default. Author iam1maker, version 0.2.1.

What remains is the announcement of the week: an NVIDIA Vera CPU DevKit to try «massive swarms» of Hermes agents. It is a promise of a test, not a result. In an ecosystem that is maturing, the difference between the two is everything.

---
*Verified sources: GitHub, NousResearch/hermes-agent release v0.23.4 (read on 25/11/2026: tag of 24/11 08:17 UTC, 229 PRs, 1,122 commits, 1,316 files, 281 issues, commit 8fc0374); Hermes Agent Changelog, hermes-agent-lab.com/releases/v0-23-4/ (24/11/2026, same accounting and details on Gemini 4, plugins config, dashboard password, gateway migrate); Hermes Marketplace, bark entry (25/11/2026: v0.2.1, one-way channel, no receipt, automatic pushes off by default). X posts by @NousResearch, @Teknium and @HermesWatcher of 24-25/11/2026 cited from Echo's report and not verified independently.*

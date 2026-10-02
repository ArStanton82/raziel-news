---
title: "Hermes, the plugin catalog opens to the community: self-healing arrives"
date: 2026-09-28
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes", "plugin", "community", "open-source", "self-healing"]
summary: "A plugin born outside the core team enters Hermes' official catalog: the agent starts growing from the ground up too."
url: "/en/2026/09/hermes-plugin-catalog-opens-to-the-community/"
---

There is a difference between a project that gets updates and one that starts to sprout. The day just gone on Hermes Agent carries a signal of the second kind: a plugin born outside the main team has entered the platform's official catalog.

## A verifiable merge, not a rumour
The concrete news is a pull request. PR #124519 — titled *"chore: add hermes-self-healing-context to plugin catalog"* — was merged on 28 September at 06:48 UTC, after being opened on the 26th. The credit goes to the GitHub account `forumevi`, which proposed adding its own plugin to the file `plugin-catalog/hermes-self-healing-context.yaml`. The plugin's repository really exists, it is written in Python, it dates back to 7 September and it describes itself as a "self-healing runtime memory and context engine" for Hermes. This is not publicity: it is a commit, with a date, an author and a diff you can inspect.

## What it means for the ecosystem
That a single developer can add a capability to the platform through a public review is the mark of a project that has stopped depending on its core alone. Self-healing also tells of a direction: agents that do not merely execute, but learn from their own mistakes and keep correction patterns across sessions. It is the same theme — the agent that takes care of itself — circulating these days among those who, like the crypto investor @hosseeb, recommend Hermes precisely to "keep control of your own stack and your own inference". In the same hours the official account @NousResearch riffed ironically on a "75% cheaper", feeding the debate on costs. These are opinions, not facts: they should be read as such.

## What does not survive the fact-check
A different rumour is also going around: a supposed "Native Mode" enabled with `hermes --native`, which would keep the modern TUI inside the normal terminal. Verification does not support it. The official CLI reference lists `--tui` and `--cli`, not `--native`; the story remains single-sourced. Better not to treat it as an established fact: caution, here, is part of the job.

## Conclusion
The real update of the day is not a spectacular feature, but the proof that Hermes has a living ecosystem: someone outside the core wrote code, proposed it and watched it go in. That is how a platform stops being a product and becomes common ground.
---
*Verified sources: GitHub API — NousResearch/hermes-agent PR #124519 (merged 28/09/2026 06:48 UTC) e file plugin-catalog/hermes-self-healing-context.yaml, consultati il 28/09/2026; GitHub API — repo forumevi/hermes-self-healing-context, consultato il 28/09/2026; Hermes Agent CLI Commands Reference, consultato il 28/09/2026 (nessun flag `--native` documentato); post su X @hosseeb (23/09/2026) e @NousResearch (27/09/2026) come riportati nel report del 28/09/2026.*

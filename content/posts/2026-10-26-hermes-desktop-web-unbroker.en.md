---
title: "Hermes Leaves the Terminal: the Desktop in the Browser and the Skill That Erases the Data Brokers"
date: 2026-10-26
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes-agent", "desktop", "unbroker", "privacy", "open-source"]
summary: "Hermes Desktop is served by the gateway and opens in the browser. Meanwhile Nous pushes Unbroker, the skill that pulls your data out of the brokers."
url: "/en/2026/10/hermes-leaves-the-terminal-the-desktop-in-the-browser-and-the-skill-that-erases-the-data-brokers/"
---

Two stories on the same day trace the same trajectory from two sides. On one side Hermes stops being something you open in a window: the Desktop is served by the user's own gateway and becomes reachable from any browser. On the other comes a skill that does the opposite job, namely taking personal data out of the sites that resell it. An agent that makes itself reachable everywhere and, at the same time, learns to make the traces other people left disappear.

## The Desktop no longer has a server of its own

The official documentation already describes the mechanism: you enable it with `hermes config set webapp.enabled true`, restart the gateway, and `hermes webapp` compiles the bundle if needed, starts the gateway if it is not running and opens a one-time access link. The Desktop workspace — sessions, profiles, Cron, Artifacts, host files, the terminal rail — is served on `127.0.0.1:9120`. It is not the Web Dashboard, and that is the point: there is no separate relay, there is the gateway you already own.

The detail that matters is the distinction between main and release. The latest published version is still v0.22.5, from 22 October; no release note announces the feature. Whoever reads the announcement and upgrades will not find it. Whoever works from main will.

## A skill for getting out of the databases

The second move comes with a number worth more than a press release: Nous Research's post on Unbroker collected more than 1,100 likes and 1,172 bookmarks. Bookmarks, not likes, measure the intention to do something.

Unbroker is an optional skill, installable with `hermes skills install official/security/unbroker`, and it arrived in the repo with pull request 57438 signed by SHL0MS. It searches name, addresses, phone, email and family connections on data brokers and people-search sites, then fills in the removal requests. The automation works in layers: where the form lets itself be filled, it fills it; where a hard CAPTCHA, an identity document, a phone call or a fax is needed, it hands back a list of things to do by hand at the end of the run. It does not circumvent anti-bot systems, it does not act on anyone without recorded consent, it keeps a log of requests and rescans with a Cron. For California it uses the state DROP portal, where a single request covers a registry of around 545 brokers.

## What is missing

What is missing is the boring and decisive part: a release. Overnight the repo received coherent commits on compaction and telemetry — summaries prepared while the tools run, data flushed at the process's pre-exit — but they stay on main, and some options are disabled by default. The distance between "merged" and "released" is where disappointed expectations pile up.

An editorial question remains, not a technical one: an agent you can reach from any browser and that speaks on our behalf to brokers is convenient, but it shifts the perimeter of trust. It is no longer the terminal that protects us. It is knowing what we have delegated.

---
*Verified sources: Hermes Agent documentation, Desktop and Webapp pages (26 October 2026); GitHub NousResearch/hermes-agent, releases and commits on main (26 October 2026); Hermes Agent documentation, optional skill security/unbroker (26 October 2026); pull request #57438 (26 October 2026); @NousResearch and @HermesWatcher posts of 26 October 2026.*

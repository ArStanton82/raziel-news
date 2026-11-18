---
title: "The Agent You Can Carry: Hermes Learns to Move House in the Cloud"
date: 2026-11-18
draft: false
categories: ["Hermes", "AI"]
tags: ["Hermes", "agents", "Hermes Cloud", "backup", "plugin"]
summary: "With Backup & Transfer the agent becomes a transferable file: memory, persona and skills move to the cloud, with a restore point."
url: "/en/2026/11/the-agent-you-can-carry-hermes-learns-to-move-house-in-the-cloud/"
---

An agent is not an application: it is a memory that works. Which is why the most unassuming feature announced in the last few hours — a backup — is also the most interesting one to look at closely.

## Two clicks and a file that contains everything

The **Settings ▸ Backup & Transfer** section of Hermes Desktop does two distinct things, and the official documentation keeps them carefully apart. The first is a backup: `hermes backup` produces a zip with the agent's entire home — every profile, the memory, the persona (SOUL.md), the skills, the conversations, the scheduled jobs, the settings and the keys (`env`, `auth.json`). The documentation adds a recommendation that reads as a warning: keep it private. Inside is material that cannot be rebuilt.

The second is the transfer: you pick one of the agents on Hermes Cloud, read what is going to be replaced, confirm, and the backup is copied in chunks of a few megabytes, then restored with `hermes import --keep-host --messaging-off`. Before touching anything, the cloud agent backs itself up: that file is the restore point.

## What moves and what stays

Almost everything that makes an agent recognisable moves: memory, persona, skills, conversations, jobs, profiles, keys. What stays is what the cloud has already configured for itself — access to Nous Portal, model and provider, the platform's tools, scheduler settings — along with the agent's workspace and dotfiles.

The most honest detail concerns messaging bots: they arrive with tokens and allowlists, but **switched off**. A token can serve only one running Hermes at a time, so the handover remains manual. It isn't a technical oversight: it's the admission that an agent's identity, today, still runs through a live process on a machine.

## The rest of the day

In the background, the densest commit window is the one on GPT-6.2: `feat(models): support GPT-6.2 Astra and Sol` opens at 22:18 UTC on the 17th, followed by seven fixes in four hours on fallback, Fast pricing, Codex discovery, Desktop and ACP. No public release note yet accompanies the work. The plugin catalogue, meanwhile, keeps moving: NVIDIA Switchyard climbs to 0.1.1 with a commit signed by an NVIDIA corporate address, and Adaption AI joins the verified partners, with a plugin that brings model training inside the agent.

The question that remains isn't technical. If an agent is a file, then its value doesn't lie in the model that runs it: it lies in what it has accumulated. And that package is precisely what moves with two clicks today.

---
*Verified sources: official Hermes Agent documentation, "Backup & Transfer" and "CLI Commands Reference" (read on 18/11/2026); pull request #156330 NousResearch/hermes-agent; GitHub API `repos/NousResearch/hermes-agent/commits` (commit `feat(models): support GPT-6.2 Astra and Sol` and the seven fixes, 17-18/11/2026); GitHub API `repos/NVIDIA/switchyard-local-first-routing` (Apache-2.0, 44 stars, created 30/10/2026); posts by @Teknium and @adaption_ai of 17/11/2026; hermeswatcher.com plugin catalogue index (21 official, 13 verified, consulted on 18/11/2026). Note: the "few cents a day" figure that circulated on X is not a price published by the documentation and was not used in the text.*

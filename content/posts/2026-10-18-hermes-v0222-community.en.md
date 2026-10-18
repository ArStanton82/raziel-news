---
title: "Hermes 0.22.2: the release that fixes the release"
date: 2026-10-18
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes-agent", "release", "gateway", "local-models", "plugin"]
summary: "Nous Research ships Hermes Agent 0.22.2, built to fix 0.22.1: the gateway, local models and a community building at the edges."
url: "/en/2026/10/hermes-0222-the-release-that-fixes-the-release/"
---

On 15 October Nous Research published Hermes Agent v0.22.2. The most interesting thing is not the list of features, but the reason stated in the release note: v0.22.1 had been built from the wrong commit. It had shipped gateway work that was not yet meant for the public, and the Microsoft Store app could hang on "Connecting". Version 0.22.2 is, in the authors' own words, "the release that 0.22.1 should have been".

## What it actually fixes

The first fix matters to anyone running Hermes on an always-on machine: the supervised gateway (systemd, launchd, Docker) starts again after a reboot. After a restart, Linux can hand an early PID to an unrelated process, and the gateway mistook it for an instance already running, refusing to start. Hermes now records the boot epoch it started in and, when it cannot compare it, queries the host lock — which only a live gateway holds.

The second concerns long turns on local models: local requests always stream with a progress indicator, stall timers skip the time the machine was suspended, and a recovered local server gets another attempt instead of landing in a switch that made every following message fail. One known and honest problem remains: sessions created under gateway 0.22.1 cannot be deleted in 0.22.2.

## The day after, the work doesn't stop

On 18 October the repository had already taken new commits on TLS and the gateway, among them a fix that refuses a deletion racing with a queued steer instead of reporting a false success. It is the mark of a development line that uses a release as a fixed point, not as a finish line.

## The community builds at the edges

Outside the official repository, the ecosystem keeps moving. One user wired an ESP32 desktop robot to Hermes, using Parakeet for speech recognition and Kokoro for replies: you talk to the agent, you hear it while it works, and you delegate long jobs to background helpers. Another flagged a practical detail: `auto_prune: true` and `retention_days: 90` written in an old `config.yaml` stay active even after pruning became disabled by default — anyone who doesn't clean up the file keeps deleting chats. And a simple, sensible workflow is making the rounds: when a local model gets stuck on an automation, pay a few cents to a cloud model to understand the block, then teach it to the local model with an explicit skill file.

A project's maturity is measured less by its features and more by how it handles its own mistakes. A release born to fix another one, documented without beating around the bush, says more than any triumphant changelog.

---
*Verified sources: GitHub NousResearch/hermes-agent, v0.22.2 release (15/10/2026); releases.sh/nousresearch, changelog (16/10/2026); community posts and threads on X (@Alacritic_Super, @GodsBoy7777, @joe_ptrkv_ch, 18/10/2026) — consulted on 18/10/2026.*

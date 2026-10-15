---
title: "The Hermes threshold: the agent that configures itself by talking"
date: 2026-10-15
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes-agent", "nous-research", "release", "plugin", "agents"]
summary: "Hermes Agent v0.22 «The Threshold Release» introduces itself in chat and cuts a third of the codebase; the patch v0.22.1 lands the next day."
url: "/en/2026/10/hermes-v022-threshold/"
---

On 13 October Nous Research published Hermes Agent v0.22.0, «The Threshold Release», rolled out the following day. The name is a statement of intent: after assembling the pantheon with v0.21, v0.22 wants to bring the user through the door. The official changelog describes the largest cycle the project has ever shipped: roughly 24,200 commits and 6,080 pull requests merged since v0.21.0, 15,600 files changed, 7,180 issues closed and around 2,520 contributors.

## The first conversation is not with the model

The most significant change is not technical, it is about experience. A fresh desktop installation opens on a guided setup chat running on a free trial model: newcomers do not have to get hold of an API key before they can talk to the agent. Connectors point the same way, bringing Hermes inside hosted applications such as Linear and Notion without requiring a Nous account to get started, as do local models with a one-click llama.cpp runtime. Onboarding stops being a procedure and becomes a conversation.

## A third less code

The striking figure points in the opposite direction to growth: the codebase is about a third smaller. Shrinking the surface while adding features is a sign of maintenance, not expansion. Around that backbone the release adds signed desktop packages, including on the Microsoft Store, a single package manager underneath everything and a catalogue of 600 plugins. The next day comes patch v0.22.1: fixes for Windows Store and plugin updates, default parameters for Nemotron Super 3.5 and the Korean language pack for the desktop.

## What is left out

Some things remain statements rather than announcements. Co-founder Teknium has said the mobile app is «not far off» and that access to some models still awaits legal work with Google and Microsoft. The third-party accounts describing Hermes — the onboarding, the login that does not expose passwords to the model — describe features confirmed by the official changelog, but should be read as reporting, not as the project's own voice.

The point is that Hermes is no longer asking the user to be an installer. If the threshold works, the project will no longer measure itself in commits but in how many people manage to cross it.

---
*Verified sources: GitHub NousResearch/hermes-agent, release v0.22.0 «The Threshold Release» (13 October 2026) and v0.22.1 (14 October 2026); nousresearch.com, announcement of 14 October 2026; releasebot.io/updates/nousresearch/hermes-agent and releases.sh/nousresearch/hermes-agent (consulted on 2026-10-15); X posts @NousResearch and @Teknium (14-15 October 2026).*

---
title: "Hermes Stops Being a Program and Becomes a Catalog"
date: 2026-11-14
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes agent", "plugin", "marketplace", "home assistant", "modal"]
summary: "Two thousand three hundred plugins in the catalog, Home Assistant moves among the official ones and Modal joins as a provider: Hermes is growing as an ecosystem."
url: "/en/2026/11/hermes-stops-being-a-program-and-becomes-a-catalog/"
---

The number that tells the story of Hermes's week best is not a release but a counter: at the time of writing the official marketplace declares 2,309 plugins, updated a few hours earlier. Three facts from the last few days revolve around that number: a long-standing plugin that changes address, an inference provider that walks in through the front door, and a hackathon that closes with nearly a thousand entries.

## The old code changes address

Home Assistant is nothing new for Hermes: it was part of the core. The official catalog card, at version 2.0.1, says it plainly — "formerly built into Hermes core; existing users are migrated automatically". Platform name, toolset, tool names, environment variables and configuration keys all stay identical; what changes is that it now installs with `hermes plugins install homeassistant` and requires Hermes 0.21.5 or higher. Anyone already using it has nothing to do: the first launch after the update installs it and enables it.

The post that in recent days announced that "Hermes now runs the whole house" was therefore describing a use case, not a debut. The distinction matters, because it points at the direction: what was a monolith becomes a module, and the module can be updated, replaced or uninstalled without touching the rest.

## A provider signed by the people who run it

On November 13 Teknium announced that Modal is available as an inference provider through its "verified" plugin. The card confirms the substance: `modal`, published by modal-labs, version 1.0.0, updated the day before. The plugin exposes Modal's OpenAI-compatible endpoints, is configured with a `MODAL_PROXY_TOKEN` token and is selected from `hermes model`. It is not a third-party wrapper pretending to be official: the author is the company that provides the service.

## A thousand entries and a canary that passes its tests

While the ecosystem was widening, the contest caught it on camera. Entries for the Hermes Agent Plugin Hackathon closed at 17:00 EST on November 12 with "nearly 1,000 entries"; the judges are selecting the top ten, and winners will be notified by email and announced "in about a week". The prize pool was 20,000 dollars.

On the build side, the release notes for November 13 and 14 show a canary v0.23.1 with the native install and chat tests passing on macOS (DMG arm64) and on Windows (MSIX arm64 and x64), with the Linux bundles disabled. A routine — but it is the routine that holds up a catalog updating every single day.

## The problem that arrives with success

Two thousand three hundred plugins are a platform, and a platform has the problems of a platform: attack surface, uneven quality, maintenance expectations. The Home Assistant case shows the most solid solution — code that lived in the core, republished with the same contracts and automatic migration — but it is not one that can be applied to everything. The question of the coming months will not be how many plugins exist, but how many survive their first version bump.

---
*Verified sources: Hermes Marketplace, plugins page and counter at 2,309 (11/14/2026); official homeassistant plugin card v2.0.1 (11/14/2026); modal plugin card by modal-labs v1.0.0 (11/14/2026); NousResearch/hermes-agent GitHub release notes, canary v0.23.1+canary.20261113T064447Z and .20261114T064334Z, read via API (11/13-14/2026); hackathon announcement on nousresearch.com and x.com/NousResearch/status/2120715518243987685 (11/12/2026); @Teknium post on the Modal provider (11/13/2026).*

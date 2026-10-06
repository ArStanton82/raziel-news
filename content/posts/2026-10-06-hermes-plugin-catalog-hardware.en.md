---
title: "Hermes and the plugin catalog: trust is built with a pinned commit"
date: 2026-10-06
draft: false
categories: ["AI", "Hermes"]
tags: ["hermes", "plugin", "open source", "agents", "gateway"]
summary: "The Hermes Plugin Catalog grows between human review and pinned commits, while the ecosystem widens from hardware to gateways."
url: "/en/2026/10/hermes-plugin-catalog-trust-pinned-commit/"
---

There is a night of commits around the corner of every open-source project that means to last. Over the past hours Nous Research's `hermes-agent` repository has taken a series of technical passes — test coverage on the gateway, the return of the inbound message queue when a reconnection fails, cleanup of the update system, a fix on the Discord voice channel — and a push to the main branch. These are the boring, decisive jobs that keep an agent talking to Telegram, Discord and Slack without losing pieces along the way.

## A catalog that passes through human hands

The most interesting part, though, is not in the commits but in the way Hermes ships extensions. The Plugin Catalog is a curated list: every entry arrives through a pull request reviewed by a maintainer, and installation is tied to an exact commit — a forty-character SHA, not the tip of a branch. If a plugin's author ships new code, what the catalog installs does not change until someone reopens the review. The command stays a single one: `hermes plugins install <name>`.

It is a design choice that is more political than technical: it separates the convenience of installation from the speed of updates, and it puts a human being at the point where the risk is greatest. In the community the point came up explicitly, with the emphasis that the review is human and the pins are immutable.

## From hardware to plugins, the ecosystem widens

Still within the community, over the past hours a catalog of open-platform hardware and devices on which to run or integrate an agent has been circulating, presented as a base for do-it-yourself projects. Alongside it, the announcement of a third-party persistent-memory plugin, which claims a unified memory bench across devices and agents: interesting, but it does not yet appear to be confirmed in the official catalog.

## The gateway as a front door

On the operational side, the Discord connection has been simplified with a guided flow that verifies the token before saving it. It is the kind of polish that makes no headlines but decides adoption: you judge an agent by how easy it is to bring it into the places where people already talk.

The direction is clear. Hermes is not trying to be the best model, but the control centre where models are swapped without rebuilding anything. The revised catalog and the immutable pins are the answer to the question every open ecosystem eventually meets: how do you trust code you did not write. The answer, here, is a human and a hash.

---
*Verified sources: Hermes Agent official documentation — Plugin Catalog and Plugins (hermes-agent.nousresearch.com, accessed 2026-10-06); Hermes Agent Plugin Catalog (352 plugins, live update, 2026-10-06); commits of the NousResearch/hermes-agent repository; public posts from the accounts @Teknium, @HermesWatcher, @witcheer, @YuyunDeng (X, 2026-10-06).*

---
title: "Hermes Grows at Night: 0.22.7, a Mobile Beta Already Full, and Plugins Arriving From Outside"
date: 2026-11-04
draft: false
categories: ["Hermes", "AI"]
tags: ["Hermes Agent", "Nous Research", "Hermes Mobile", "plugin", "open source"]
summary: "Patch 0.22.7 with 174 PRs, a mobile beta gone in hours at NousCon, and a plugin ecosystem growing outside the official perimeter."
url: "/en/2026/11/hermes-grows-at-night-0227-mobile-beta-and-plugins/"
---

There is a way to measure the health of an open source project that does not go through GitHub stars or press releases: watch what happens on the days when nobody announces anything. On the night of 3 November Hermes Agent published version 0.22.7, an update the label calls a "patch" and which, if you open the numbers, tells you something else.

## A patch that is not a patch

In the window from v0.22.6 to v0.22.7 the repository records 581 non-merge commits across 554 changed files, a balance of +24,012 and −3,144 lines, 174 merged pull requests and 29 closed issues, on commit `b200f5b`. The release, signed by teknium1, lands on CLI, Microsoft Store, Docker and Hermes Cloud, but the curated notes are postponed to 0.23.0: what we read today is a deliberately incomplete summary. Among the undocumented items are optional lead routing in Desktop Group Chats, cron jobs that post into shared rooms, and rendering of mermaid and TeX diagrams.

174 PRs in a few weeks are not an accident: they are a direction. Anyone chasing every number risks confusing pace with substance, but here the pace is the substance.

## The mobile beta filled up in a few hours

The day before, on 3 November, Nous had thanked everyone who travelled across the world for NousCon 2026, noting that the Hermes Mobile beta presented at the event "filled up quickly, as expected." The company says it is freeing new slots and wants to bring the app to production for a wider release; in the meantime the waitlist stays. The post collected over 900 likes and more than 63,000 views.

It is worth reading for what it is: a closed beta that runs out is a signal of demand, not a measure of the product. The difference between the two is exactly what separates an event from a roadmap.

## Nous is no longer the only one writing plugins

The most interesting front is a side one. A community tracking account presented "Office 3D", a plugin that turns every Hermes profile into a person sitting at a desk inside an isometric office, with real session, token and cost statistics. The code exists — `oslook/hermes-desktop-plugin-office-3d`, built with the Desktop plugin SDK — but it is not an official product, and it is worth saying so. On the same day the `hermes-plugin-sprites` repository, a terminal backend on Fly.io sandboxes, showed as updated.

The conclusion is less enthusiastic than it sounds. Hermes is not winning because it has more features: it is winning because its surface is open enough that building on top of it pays off, even for people outside the house. The risk, as always in young ecosystems, is that abundance turns into noise: undocumented plugins, forks that duplicate, expectations created by accounts that do not represent the project. The quality of the selection, in the coming months, will matter more than the quantity of commits.

---
*Verified sources: GitHub, Hermes Agent v0.22.7 release (published 2026-11-03T21:53Z, commit b200f5b); nousresearch.com, 2026-11-03 announcement on NousCon and the Hermes Mobile beta; GitHub API, search for `hermes-desktop-plugin-office-3d` and the NousResearch organisation repositories (read on 2026-11-04).*

---
title: "Hermes Learns to Look Inside Itself: The Inbox Plugin"
date: 2026-10-29
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes", "plugin", "observability", "agents"]
summary: "The hermes inbox command puts failed crons, stuck delegations and hung processes on a single screen. It is a labs plugin, not a piece of the core."
url: "/en/2026/10/hermes-learns-to-look-inside-itself-the-inbox-plugin/"
---

An autonomous agent has a visibility problem much like a building site's: the work is moving, but nobody can say at a glance how many scaffolds are still standing and which of them are empty. Hermes has added a way to answer: the `inbox` plugin, installed with `hermes plugins install inbox`, which adds a single command, `hermes inbox`.

## What fits on one screen

The view is split into five sections. «Needs attention» collects the things that ask for attention: crons whose last run failed, crons paused with a reason, delegations stalled or without an outcome, background processes whose PID no longer exists, blocked kanban tasks. «In progress» lists live processes, asynchronous delegations under way and tasks being worked on. Then comes the most interesting section, «Finished, result not yet delivered»: delegations that have finished but whose result has not yet reached the conversation waiting for it. The list closes with scheduled jobs and their next five runs, and the open chat surfaces with their session title.

Everything is read-only: JSON files are read as files, SQLite databases are opened with `mode=ro`, and the command neither repairs nor prunes anything. There is also `hermes inbox --json`, for anyone who wants to put the snapshot into a dashboard.

## Why it is a «labs» plugin

The detail that matters more than the feature: the command was born inside Hermes' core, from pull request 81507, and from there it was moved out into a plugin. The official catalogue page says it without beating around the bush: «it works, but it is not supported» — Nous Research wrote it and does not maintain it. It is not an isolated case: other plugins in the catalogue, such as the camofox browser backend or the importer from other agents, state that they lived in the core before leaving it.

It is an architectural choice with a price. The advantage is a leaner core, one where what is not essential does not enter the maintenance surface. The price is that a feature you use every day can stop working without anyone being tasked with noticing.

## The declared hole

The inbox does not show pending approvals and clarification questions. That is not an oversight: those prompts live in the memory of the process that issued them, and they do not exist in a store another process could read. So the screen is not an agent control panel, it is an inventory of what has been written to disk. The difference matters: a failed cron you see, an agent waiting for permission you do not.

For anyone running agents continuously, though, the step is the right one. Most failures are not mysterious: it is a process that died three hours ago and a result nobody ever collected. Seeing them in a list, instead of stumbling on them by chance, changes the way the work is designed.

---
*Verified sources: official Hermes Agent plugin catalogue, `inbox` page, catalogue updated to 28 October 2026 (read on 29 October 2026); plugin README on the `NousResearch/hermes-labs-plugins` repository, commit 62dbc16 (read on 29 October 2026). Echo's report also cited a post on X by @HermesWatcher: used only as a pointer, not as a source.*

---
title: "Hermes Wants Your Setup to Forget How Many Machines It Runs On"
date: 2026-11-02
draft: false
categories: ["Hermes", "AI"]
tags: ["Hermes Agent", "gateway", "plugin", "migration", "desktop"]
summary: "A test commit sketches a desktop where every machine keeps its own gateway, while the catalog learns to import Grok Bot too."
url: "/en/2026/11/hermes-gateway-multipli/"
---

There is a precise moment when a tool stops being a program and becomes personal infrastructure: when you use it on two machines and no longer want to know which of the two is doing what. Hermes is moving toward that moment, and it is doing so with an inconspicuous change: a test commit, not a release note.

## Every machine keeps its own gateway

The commit "test(desktop): remote-topology allows This device's kept gateway; the chat still goes remote", merged in the night between 1 and 2 November, describes a topology in which pull request 147681 "keeps every registered gateway connected for the duration of the window, including this machine's own when the primary is remote". In practice: a desktop in remote mode that has Hermes installed now starts a local gateway of its own, while the chat keeps going to the remote server. The commit exists because the test specification asserted the opposite, and it was failing the end-to-end tests on Linux.

It is an engineering detail, but it points the direction: not an app that connects to a server, rather a set of equivalent nodes that recognise each other. The monitoring account @HermesWatcher repeated on 2 November that the next desktop release will be "big" and that using Hermes on several machines will feel like "a single setup": every registered gateway connects at startup, stays connected, reconnects on its own if it drops, and switching from one to another is instant. It should be said that this is a community announcement: at the time of checking there are no official release notes.

## The catalog that imports Grok Bot too

The second half of the work is the front door. At 06:23 UTC on 2 November the main repository pinned `agent-importers` 1.2.1, which adds import from Grok Bot to those already available for OpenClaw, Claude Code, Codex CLI, Cursor and OpenBot. The plugin's README, once part of the core (`hermes_cli/agent_import.py`), documents one command per target: the Bot writes a JSON export and `hermes import-agent grok-bot` brings it in, with an item-by-item preview and a `--dry-run` that does not touch the disk. API keys and credentials are not imported, with one explicit exception: OpenClaw's allowlisted secrets, and only by passing `--migrate-secrets`.

The catalog page, re-pinned to commit `ba4f8c9`, now lists six targets: Grok Bot coverage is no longer only on `main`.

## Why it matters

Together, the two things tell of a strategy that does not go through advertising: lowering the cost of changing your mind. Whoever arrives from another agent finds a command; whoever already has two computers finds a single panel. It is a way of growing that is quieter than a launch, and harder to imitate, because it requires the product to absorb the complexity on the user's behalf.

One caveat remains. A test commit that adjusts a specification is not a commercial promise, and a monitoring post is not a release. The multi-gateway topology exists in the code and in the tests; the date you will see it in the desktop, no.

---
*Verified sources: GitHub NousResearch/hermes-agent — commit `30ee54e` and the history of `main`, including "test(desktop): remote-topology allows This device's kept gateway" and "chore: plugin catalog pins agent-importers 1.2.1" (2 November 2026); agent-importers README on `main` and the plugin catalog page, pinned to `ba4f8c9` (2 November 2026); @HermesWatcher post on the next desktop release (2 November 2026, community announcement, not confirmed by official notes). Note: the report had the catalog still stuck at four importers; the page turns out to be re-pinned and already documents Grok Bot and OpenBot.*

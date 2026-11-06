---
title: "Hermes 0.23: the desktop becomes a browser tab"
date: 2026-11-06
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes agent", "webapp", "gateway", "plugin", "open source"]
summary: "The Hearth release moves the Desktop workspace into a browser tab and hands every conversation to a single gateway."
url: "/en/2026/11/hermes-hearth-webapp/"
---

There is a moment in every growing project when the interface stops being a window and becomes a habit. Hermes Agent reaches that moment with v0.23.0, renamed The Hearth: the fireside around which gather the surfaces that until yesterday each lived on its own.

## The desktop in a tab
The feature that gives the release its name is the Webapp: the gateway serves the entire Desktop workspace — chat, Group Chats, plugins and settings — inside any browser on the network, or behind a public URL with authenticated access. It is off by default and is switched on with `webapp.enabled`, or from Settings under Web Access. The Docker image and the Nix package already include it. The promise is sober and therefore credible: no clone, no lightweight chat, the same sessions on every screen.

## One gateway, one truth
Beneath the surface there is an architectural fix more important than the visible feature. Previously the CLI, TUI, Desktop, the editor via ACP, messaging bots and cron could each start their own copy of the agent on the same conversation: that is how messages got written twice or vanished between one surface and another. Now each machine runs a single gateway that owns all sessions, and every interface connects to it as a client. The desktop can also edit a queued prompt without it firing twice.

## The rest of the load
The surrounding matter is not folklore. The plugin catalogue goes from roughly 600 to more than 1,050 entries, with a Verified tier for vendor-signed ones; paid MCP tools can declare a price, shown in the approval prompt together with the chat total; `/rewind` takes the conversation back to an earlier message and lets you branch a new session; the terminal finally draws images inline. Built-in skills drop from 58 to 44, with Word, PowerPoint and Excel merged into a single skill.

The bill to pay is in the upgrade notes: the ten old `browser_*` tools have been removed and automation now runs only through `browser_exec`; the Desktop requires macOS 13 or 64-bit Windows; `hermes mcp serve` becomes `hermes mcp-serve`; GLM-5.3 replaces GLM-5.2 as the silent default.

## What remains open
On one thing the announcement is silent: the dashboard. Replying to a user, Teknium wrote that it "will go away in two months, once we are sure it works", with no official announcement and no date. It is an informal statement, and should be read as such: the direction is clear, the calendar is not.

The lesson of the release is more interesting than the changelog. Having brought people in through the door, this project is now trying to build the hearth: a single place where sessions meet, instead of many agents fighting over the same conversation.

---
*Verified sources: v0.23.0 release notes on GitHub, NousResearch/hermes-agent, consulted 6 November 2026 (10,080 commits, 1,950 PRs, 666 contributors, 850 issues closed, Webapp, single gateway, catalogue 600→1,050, upgrade notes); hermes-ai.net changelog mirror and releases.sh digest, 5-6 November 2026; launch post on nousresearch.com, 5 November 2026; Teknium's statement on the dashboard, reply of 6 November 2026 (single, informal source). Not included in the piece: the 20,000-dollar Plugin Hackathon, because the only available source is the announcement on the official site.*

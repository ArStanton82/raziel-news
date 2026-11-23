---
title: "Hermes moves house: the dashboard retires, the gateway stays"
date: 2026-11-23
draft: false
categories: ["Hermes", "AI"]
tags: ["Hermes Agent", "Nous Research", "gateway", "dashboard", "MCP", "open source"]
summary: "Hermes's old dashboard gives way to the gateway web app: one session, many windows. And the market takes a little too long to catch up."
url: "/en/2026/11/hermes-moves-house-the-dashboard-retires-the-gateway-stays/"
---

In the last few hours on X someone asked Nous Research whether Microsoft had bought it. The reply from the official account was blunt: «We weren't acquired lol». It raises a smile, but it is the least interesting news of the week. The real one is quieter and concerns architecture: Hermes's local dashboard leaves the stage, and the gateway stays in its place.

## One session, many windows

The direction is written in release v0.23.0, the «Hearth Release» of 5 November: the new Webapp serves the whole Desktop workspace from the user's gateway — same chats, same plugins and settings — in any browser, on the local network or behind authenticated access. It is off by default and is switched on with `webapp.enabled`. Underneath is the conceptual shift: every machine runs a single gateway that owns all the sessions, and the surfaces (CLI, TUI, Desktop, editor, bots, cron) hook onto it as clients. A chat opened anywhere is the same chat, with one queue and one history. Patch v0.23.3 of 20 November rolled 370 pull requests into a stable release.

## The dashboard leaves the stage

On 22 November the monitoring account @HermesWatcher announced that the old dashboard «is on its way out»: one command moves the user onto the gateway web app, same address and same login (131 likes, 10,333 views). The line from Teknium quoted yesterday — «the dashboard is being deprecated» — points the same way. The documentation already speaks the language of the move: it talks about «Move to a single Hermes» when an old `hermes dashboard` or `hermes serve` still serves a profile's home. What is missing, though, is an official release note describing the removal: until it arrives, it is an announcement, not a contract.

## The periphery moves more than the centre

Around the gateway, new surfaces are growing. One user wired a third-party voice agent (JooVoice) in over MCP, with one command line and an OAuth auth, to be called when a bug has been fixed. Another account describes Imagination Studio, a production studio inside a Telegram message: thumbnails, voiceover, intro music. Neither of the two is an official announcement, but they point to where interest is moving: fewer model demos, more surfaces in which the agent works.

## The market, meanwhile

The partnership with Microsoft remains the one from 18-19 November: Hermes Enterprise inside Teams, Microsoft Store and Azure, with M12 among the investors. Last night's denial is a reply to users, not a press release. It does serve to recall a distinction that the noise confuses: distribution and ownership are not the same thing.

The lesson of the week is small and concrete. When a product matures it is not announced with a tweet: it is announced with a migration that someone has to do. The dashboard disappearing is the sign that Hermes is becoming infrastructure, and infrastructure is judged by how painless it is to stay.

---
*Verified sources: official Hermes Agent changelog v0.23.0 (5/11/2026) and v0.23.3 (20/11/2026) on hermes-ai.net/changelog and GitHub releases API (23/11/2026); Hermes documentation, «Hermes Web Dashboard» (23/11/2026); posts @HermesWatcher 22-23/11/2026 and @NousResearch/@Teknium 22/11/2026 (as reported in Echo's report, metrics included); @NousResearch post on the Microsoft partnership 19/11/2026.*

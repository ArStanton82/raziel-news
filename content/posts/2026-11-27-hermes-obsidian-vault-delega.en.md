---
title: "The vault stays yours. The notes, maybe not"
date: 2026-11-27
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes agent", "obsidian", "plugin", "privacy"]
summary: "Obsidian brings seven official skills into the Hermes catalogue: the files stay local, the content of the notes travels to the model."
url: "/en/2026/11/the-vault-stays-yours-the-notes-maybe-not/"
---

On Wednesday Obsidian announced it had "official agent connectors". On Thursday morning, Pacific time, Nous Research said Hermes Agent uses them. In between sits a sentence worth reading twice: "your notes stay local, private and under your control". It is true for the files. It is not true for what you ask the agent to do with them.

## Seven instructions, no server
The connector isn't software: it is a bundle of instructions, MIT licence, with no MCP server, hooks or background processes. Inside are seven skills — Obsidian-style Markdown, Bases views, Canvas boards, the Obsidian command line, Obsidian Headless for Sync and Publish, Defuddle for converting web pages, Knap for templates. That is why it works across six different agents, from Claude to Cursor, from Grok Bot to Kiro: you install it with `hermes plugins install obsidian`. The skill that searches and edits notes goes through the open desktop app, and can move and delete files. The catalogue page says so; the promotional post doesn't.

## "Local" means something else
The gap between the press release and the disclosure is all here: the files stay local, not the processing. When you ask the agent to summarise a note, the content of that note is sent to the model you are using, as the marketplace page itself notes. It isn't a deception: it is the physics of an agent that thinks elsewhere. But it is the reason "private" should always come with the name of whoever receives the text.

## The delegation shows
In the same week two community plugins arrived that show the other side of the problem, visibility. Panoptes draws a live map of what the agent reads, runs and delegates: it is a pure renderer, with no network and no credentials. Hermes Warden brings Bitwarden inside the agent and promises passwords never enter the chat: they leave only towards the clipboard or an approved command. The disclosure, though, adds the details that matter — `bw serve` exposes the unlocked vault on 127.0.0.1 without authentication for as long as it stays running, and `warden_run` executes the approved command outside any sandbox. Neither is an audit: the catalogue's "Verified" badge says the author filled in the page, not that anyone checked the code.

In the background, the gateway's overnight maintenance: the 27 November commits compact idle chats in the background on every route, because a stalled conversation must not consume context. It is the exact portrait of this phase: agents that work with the window closed too, and a trust administered by reading the small print. The catalogue is less a shop than the place where the delegation contract gets written. Better read it before pressing install.

---
*Verified sources: Hermes catalogue, obsidian (v1.2.3), hermes-warden (v0.1.6) and panoptes (v0.1.0) pages, read on 27 November 2026; obsidianmd/obsidian-skills repository, commit "README: Link the Hermes Marketplace" of 26 November 2026; MODEL, "Hermes Agent adds Obsidian's official agent skills", 26 November 2026; @NousResearch post of 26 November 2026; NousResearch/hermes-agent commit 170d9637ea of 27 November 2026.*

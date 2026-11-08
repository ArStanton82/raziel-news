---
title: "One Database, One Queue, One UNVERIFIED Line: Hermes Gives Agents a State"
date: 2026-11-08
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes agent", "kanban", "compaction", "plugin", "open source"]
summary: "The least spectacular of Hermes's new features are the most important: every task becomes a row, every doubt a label."
url: "/en/2026/11/one-database-one-queue-one-unverified-line/"
---

The feature people talk about most these days makes images with one Google model and video with another. But the change that alters the way an agent works does not show up in a post: it is a table. Hermes Kanban, Hermes Agent's project-board system, treats every task as a row in a SQLite database, every handover as a row anyone can read and write, every worker as an operating-system process.

## The end of the swarm in memory

Until yesterday, collaboration between agents was done with subagents: creatures born inside the parent's process, which vanished with it. The official documentation describes the board as the alternative to "fragile in-process subagent swarms". The shift is not cosmetic. An assignment that lives in a database survives a restart, can be inspected from outside, can be unblocked by hand. Workers launched by the dispatcher do not even see the other boards: the environment variable that starts them is pinned to their own, and the documentation says they "physically cannot see" the others.

There is also a concession to realism: whoever works receives a warning at around 90% of their iteration budget, and the documentation specifies that this is "an occasion to report back", not a guarantee that the model will listen.

## Uncertainty gets a line of its own

The second change is subtler and, for anyone who uses these tools every day, more important. Since version 0.23 "The Hearth", released on 5 November, compaction summaries list uncertain claims on `UNVERIFIED:` lines, each with the basis on which it is made. The pull request that introduces it explains the problem better than a press release: when a long conversation is compressed, words like "I suspect" or "probably" are the first to disappear, and a conjecture comes back after compaction in the form of established fact.

That is the point where an agent fools itself, and it is not a detail for engineers. An assistant that loses track of what it does not know is no more reliable than one that gets things wrong: it is only harder to correct. Alongside it comes a "prepared" compaction that writes the summary in advance, and which is off by default.

## The periphery grows

Around the core, the catalogue moves. The `gemini-media` plugin, from a community maintainer, connects the agent's image and video tools to Google models: Nano Banana with up to 14 reference images and 4K output, Gemini Omni for videos of 3 to 10 seconds with native audio. Then there is `serpapi`, which brings in web search, maps and news. Neither of the two is signed by Nous.

The editorial question, then, is not how many agents can be run at the same time. It is where their state lives and who can read it. A persistent queue and a label for doubts are worth more than one more model on the list, because they are the two things that make an automated system correctable by a person.

---
*Verified sources: official Hermes Agent documentation, Kanban page and CLI reference, consulted on 8 November 2026 (per-project board, separate SQLite database per board, dispatcher, `kanban_*` toolset, checkpoint at 90% of the budget, worker isolation); Hermes Agent v0.23.0 release notes on GitHub, 5 November 2026 (`UNVERIFIED:` lines, prepared compaction off by default); pull request NousResearch/hermes-agent #86019, read on 8 November 2026; gemini-media plugin entry in the official catalogue and repository bytecakelake/hermes-gemini-media-generation, 8 November 2026 (Nano Banana up to 14 references, 1K-4K; Gemini Omni 3-10 s, native audio, community tier); serpapi plugin entry in the catalogue, 8 November 2026. Left out of the piece: the Signal Dog plugin for accessibility — a single post by its author on X, 18 views, no second source.*

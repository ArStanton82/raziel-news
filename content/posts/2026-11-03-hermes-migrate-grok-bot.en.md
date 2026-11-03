---
title: "Hermes 0.22.6 and the Move From Other Agents: Migration as a Feature"
date: 2026-11-03
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes", "migration", "grok-bot", "openbot", "cli"]
summary: "With 0.22.6 Hermes imports routines, skills and memories from Grok Bot and OpenBot: a move, not a cloning."
url: "/en/2026/11/hermes-0226-migration-as-a-feature/"
---

For months, for anyone leaving a conversational agent, the question was a single one: what survives of my automations? The answer Hermes gives as of yesterday is a command. With version 0.22.6, published on 2 November, `hermes migrate` and the first-run procedure can import a Grok Bot or OpenBot account: routines become cron jobs, skills stay skills, memories become profile memory, and the bot's role comes along with them.

## A move with the labels on

The pull request that introduced the feature captures the gap it fills well: until that moment only the agent-importers plugin knew about other agents, and nobody knew about Grok Bot. Now the initial setup offers Grok Bot and OpenBot alongside OpenClaw, Claude Code, Codex and Cursor, while `hermes migrate <agent>` installs the importer when it is missing and then runs it.

The detail worth attention is another one: imported routines arrive paused. No job starts twice while the original is still running. It is the difference between an import and an incident, and it says a lot about how the project understands the word "migration": not a silent fork, but a handover with the engine off.

## 776 PRs in one patch

The number that comes with the release is bigger than the news. The release is avowedly a patch, yet the window since v0.22.5 holds 3,448 non-merge commits across 4,316 files, 776 pull requests and 385 closed issues. The curated notes will come with 0.23.0: here the project chose to list everything, one line per item, giving up hierarchy rather than losing pieces.

It is worth reading as a signal of method. An agent growing at this rate has a problem of storytelling, not of code: whoever uses it needs to know what changed without having to read a six-thousand-line changelog. The decision to postpone the curation is honest, but it moves the synthesis work onto whoever adopts it.

## What does not come across

The mapping is explicit and worth repeating: routines, skills, memories, role. It is not a cloning, it is a reconstruction of operating identity. Anyone expecting to find the conversation history will be disappointed, and perhaps rightly so: an agent is not its transcript.

There is also a practical limit the announcement does not hide. The desktop app installed from a package does not change with this release and will update with the next bundle; CLI users update with `hermes update`. The migration, in short, reaches those who work in a terminal first.

That a young project invests in importing from others is, in the end, an act of trust: it presupposes that an agent's value lies in the procedures it has accumulated, not in the platform that hosts them. If the move works, loyalty becomes a choice renewable every day. And it is a more sober, and a harder, way to compete.

---
*Verified sources: GitHub release v0.22.6, NousResearch/hermes-agent, published on 2 November 2026 at 17:18 UTC (read on 3 November 2026); pull request #147724 "Grok Bot and OpenBot users can move to Hermes from setup and hermes migrate" (read on 3 November 2026); CLI and import-from-other-agents documentation cited in the PR. Not verified and therefore excluded: the changelog counts for the mobile beta and the iOS/Android build numbers, absent from official sources; the Olares use case, promotional in nature.*

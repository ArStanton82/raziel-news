---
title: "Hermes speeds up, but its memory plugins are looking for an owner"
date: 2026-10-03
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes", "nous-research", "plugin", "memory", "open-source", "mcp"]
summary: "Nous Research marks three memory plugins as 'unmaintained' while the Hermes core keeps running. Maintenance is the least visible part of the ecosystem."
url: "/en/2026/10/hermes-plugin-memoria-unmaintained/"
---

On 2 October, the NousResearch organisation on GitHub updated three memory plugin repositories for Hermes Agent — hermes-plugin-holographic, hermes-plugin-byterover and hermes-plugin-retaindb — adding the same description to each: "Unmaintained — looking for an owner. Not maintained by Nous Research." The last commit, signed by teknium1, is explicit: "Nous Research does not maintain memory providers". Three small repos, a short note, and a question that concerns the whole ecosystem: who keeps the lights on when the core runs fast?

## The core doesn't stop

That same night, the main hermes-agent repository received a series of maintenance commits: a fix for the child processes of a dead MCP server, a cap on the wait for the browser resolver lock, and several polish items to the bot roster on Desktop, with traces of identity attribution for multiple connections. The last tagged stable release remains v0.21.5 (v2026.9.24), which had already bundled around 460 pull requests. The pace is that of a project in full flight: the plugin catalogue went from 292 entries at the time of that release to 349 on 2 October, and installing MCPs from the catalogue approved by Nous is now a matter of a few clicks.

## An ecosystem at two speeds

There is a structural tension in every project that grows quickly. The core evolves every night, while the peripheral components — the memory providers, in this case — need an owner to follow them over time. Holographic is a local SQLite store of facts with HRR retrieval; ByteRover builds a knowledge tree through the brv CLI; RetainDB is a cloud API with hybrid search. Three different approaches to the same problem: giving the agent a memory that survives sessions. The fact that Nous has "released" them does not make them useless — it makes them orphaned. The official documentation still lists them among the available providers, but maintenance is now someone else's responsibility.

## The boring part that decides everything

There is a recurring lesson in open-source software: the difference between a demo and an infrastructure is not the idea, it is who answers the issues six months later. An agent that remembers is more useful than one that forgets, but only if that memory keeps working after the core is updated. Nous Research has chosen to focus on what it considers its own core and to hand the rest to whoever wants to maintain it: a legitimate decision, and even honest in the way it is communicated.

The open question is for users. Anyone relying today on one of these providers is building on a piece that no one promises to update. It is the silent trade-off of the Hermes ecosystem: great speed at the centre, and at the periphery the need — an entirely human one — to find someone who will take care of it.

---
*Verified sources: GitHub, org NousResearch (descriptions and commits of the repos hermes-plugin-holographic, hermes-plugin-byterover, hermes-plugin-retaindb, 2026-10-02); GitHub, commits and releases of NousResearch/hermes-agent (v0.21.5, v2026.9.24; commits of 2026-10-03); official Hermes Agent documentation, Plugin Catalog and Memory Providers sections; hermesagents.net, state of the plugin catalogue (349 entries as of 2026-10-02). All consulted on 3 October 2026.*

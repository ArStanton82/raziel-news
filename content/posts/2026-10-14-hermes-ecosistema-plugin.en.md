---
title: "The plugin as interface: the Hermes ecosystem grows at the edges of the core"
date: 2026-10-14
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes-agent", "plugin", "nous-research", "sprites", "release"]
summary: "Hermes Agent v0.21.7 consolidates the core, while the official catalog and community plugins become the real ground for growth."
url: "/en/2026/10/hermes-ecosistema-plugin/"
---

While the Hermes Agent core enters a consolidation phase, the most interesting part of the project is shifting to the edges: to plugins. That is where you can see where an agent goes when it wants to be a platform and not just a program.

## A core that stops to polish

The stable tag v0.21.7, published on 11 October and rolled out on the 12th, is a maintenance release: it gathers around 204 pull requests accumulated since v0.21.6 and introduces no significant features. The changes are operational, and they are worth noting because they tell of a product that is starting to think about the people who install it: source updates now follow tagged releases instead of every commit on main, the desktop app gains a toggle for choosing the update channel, signed reasoning survives a session resumption, and updates no longer fail behind certain regional firewalls. They are details. They are also a sign that the project no longer has to prove it exists.

## Official plugins and remote sandboxes

The real movement is in the catalog. The hermes-official-plugins repository gathers the first-party plugins — Home Assistant, Spotify, Claude Subscription DirectSDK, blender, langfuse, snyk and others — installable in one line from the plugin catalog, and it has passed 270 stars. Alongside it comes hermes-plugin-sprites, which registers a terminal backend based on stateful cloud sandboxes from Fly.io, with checkpoint and restore, built on the terminal backend extension without touching the core. The main repository, meanwhile, is updated to 14 October with roughly 254,000 stars and 55,000 forks: numbers that say more about the project's visibility than about its maturity.

## The community's long tail

Under the official plugins grows a long tail of community tools. Among them Hermes Activity, a read-only usage dashboard with a GitHub-style contribution grid, token breakdown by model and a summary of tools and skills. It is a third-party plugin, not a Nous Research product, and should be read as such: it points to a real need — understanding how much and how an agent consumes — that the core does not yet cover.

The rumours circulating on X in recent hours, however, remain unverified, such as an alleged Hermes Agent hosted by Tencent for Telegram, WhatsApp and Discord, or a plugin capable of driving phone apps. No official Nous Research source confirms them, and they should be treated as background noise.

The question left open is whether this extension-based architecture will hold at scale. A stable core and lively edges is a good model; a stable core and fragmented edges is a governance problem. For now Hermes is taking the first road.

---
*Verified sources: GitHub NousResearch/hermes-agent releases and org repositories (consulted on 2026-10-14); GitHub NousResearch/hermes-official-plugins (272 stars, consulted on 2026-10-14); GitHub NousResearch/hermes-plugin-sprites (consulted on 2026-10-14); releasebot.io/updates/nousresearch/hermes-agent and releases.sh/nousresearch/hermes-agent (v0.21.7, consulted on 2026-10-14); GitHub topics token-usage, repo hassan-kamel/hermes-activity (community plugin, consulted on 2026-10-14).*

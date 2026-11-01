---
title: "The Browser Left the Core and Came Back Through a Side Door"
date: 2026-11-01
draft: false
categories: ["Hermes", "AI"]
tags: ["Hermes Agent", "browser", "plugin", "Camofox", "extension"]
summary: "Hermes pulled browser control out of the core on 23 October. Eight days later a community plugin puts it back inside, with 27 tools."
url: "/en/2026/11/hermes-browser-fuori-core/"
---

On 23 October, at 09:13 UTC, the Hermes Agent repository closed pull request 143146 with a title that reads like a surrender: "browser automation runs only on `browser_exec`; agent-browser and the built-in browser tools are gone (Camofox moves to a plugin)". From that day the agent no longer has a browser of its own. Eight days later, on the evening of 31 October at 21:53 UTC, the community browser extension shipped version 0.4.0 with a plugin that puts those capabilities back inside.

## What left the core

The practical consequence is all in the extension's release notes: canary builds from 24 October and every version after 0.22.5 no longer offer tab control inside Hermes. Whoever updates loses a feature they did not know they had on loan. Whoever stays behind keeps it, and stays behind.

It is a reasonable maintenance call — a browser driven by the core is a surface that ages fast — but it moves the boundary: the edge of the system is no longer where the main code lives.

## Who wrote what

The extension is not Nous Research's. It belongs to Jon Komet, MIT licence, 1,738 stars, and presents itself as a community project for Hermes. The plugin installs from a git address with the `#companion-plugin` subfolder and requires a gateway restart, because the official plugin catalogue, as of today, has no entry for it. The post announcing the release calls it "Hermes's browser extension" without qualification; the qualification is in the README.

## Twenty-seven tools and a naming problem

The count checks out: twenty tab-control tools — `tab_click`, `tab_snapshot`, `tab_create` and company — plus seven read-only context tools, the twenty-seven of the announcement post.

The interesting part is why the new names. They used to be `browser_*`. But the Camofox plugin already registers `browser_navigate`, `browser_click`, `browser_type` and four others, and Hermes keeps the first plugin that registers a name: seven control tools were landing in the wrong browser, and nobody noticed. The tool namespace is territory, and you defend it by renaming.

## The limits, as told by the author

Tab control works only on Chromium; Firefox gets chat and page context, not the debugger. With multiple profiles you need the plugin active for each one and a Hermes that routes calls per profile. When a feature is missing, the panel writes why instead of pretending it is there.

One question remains, and it is not about this release. If the agent's browser lives outside the core, who answers when it breaks? The convenient answer is "whoever wrote the plugin". The honest one is that the user has just discovered they have one more supplier.

---

*Verified sources: NousResearch/hermes-agent repository, pull request 143146, title and merge date 23 October 2026 (GitHub API); abundantbeing/hermes-browser-extension repository, release v0.4.0 published 31 October 2026 at 21:53 UTC, CHANGELOG and README of `companion-plugin`, consulted on 1 November 2026; NousResearch/hermes-official-plugins catalogue, index as of 1 November 2026 (no entry for the extension's plugin).*

---
title: "Hermes' Plugin Catalog Has 644 Entries, Not 700: the Difference Matters"
date: 2026-10-21
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes-agent", "plugin", "game-dev", "nvidia", "asus"]
summary: "Hermes' plugin catalog passes 640 reviewed entries. Around it, a game studio and the RTX Spark laptops are taking shape."
url: "/en/2026/10/hermes-plugin-catalog-644-entries-not-700/"
---

On the same day the Nous Research co-founder was announcing video-game-studio powers for Hermes Agent, the most interesting figure was another one, and it sat at the bottom of a documentation page: the catalog counter.

## The number social media inflates

«Over 700 plugins» was making the rounds on social media. The official catalog page, queried on 21 October, declares 644, split into nine categories: 13 official and 631 from the community. The v0.22.0 release notes, dated 13 October, spoke of 600 entries. Forty-four additions in eight days is a credible pace for a living catalog; a jump to 700 is not. This is not editorial pedantry: in an extension ecosystem the number is also a measure of the exposed surface, and inflating it helps no one.

## A catalog, not an app store

The remarkable thing is not the quantity but the mechanism. Every entry is pinned to a reviewed commit: what you install is exactly what was examined, and an update only arrives when a new pin passes review. The catalog rules forbid plugins from modifying Hermes' internals or shipping binaries that cannot be scanned.

It is a governance choice dressed up as a feature. An ecosystem growing by more than seven percent in a week needs a bottleneck, not an open gate. The catalog is that bottleneck, and its declared slowness is the product.

## The game studio is still a plan

Ryan Teknium listed the missing capabilities needed to turn the agent into a small studio: 3D model generation, animation, sound effects, connectors to Unity and Godot. All through plugins, without touching the core. The specialist press was explicit: the tools have not been added yet, and the proposal is a roadmap. A community plugin for game dev exists as a pull request in the catalog, not as an installable entry.

It is worth recalling the direction: the agent framework is not trying to become a graphics engine. It is trying to orchestrate the ones that already exist.

## The laptop as a distribution channel

The third move is quieter and perhaps more decisive. On 16 October Nous Research confirmed it is a launch partner for RTX Spark, NVIDIA's platform for PCs running local agents. ASUS is bringing it to the ProArt P16 and P14 and to the GR1X mini PC, with pre-orders from 7 October and availability from 16 October. Hermes ships alongside ComfyUI, and security runs through NVIDIA's OpenShell runtime.

«We built Hermes to give you intelligence you can actually own, rather than rent», said CEO Dillon Rolnick. It is a marketing line, but it describes a coherent strategy: first the catalog makes the agent extensible by others, then the hardware puts it on the desk.

Three moves converging. The number to follow is not the one shouted on social media, but the one reviewed on the catalog page.

---

*Verified sources: Hermes Agent plugin catalog, hermes-agent.nousresearch.com/docs/plugins (read on 21/10/2026); v0.22.0 release notes of 13/10/2026 (GitHub NousResearch/hermes-agent); TokenPost, «Nous Research Co-Founder Plans Game Studio Tools for Hermes Agent», 20-21/10/2026; Nous Research, RTX Spark announcement, 16/10/2026; NVIDIA, RTX Spark press release, 01/06/2026; ASUS, press release on ProArt P16/P14 and GR1X, 08/10/2026. Discrepancy noted: the «over 700 plugins» circulating on social media does not match the official count of 644.*

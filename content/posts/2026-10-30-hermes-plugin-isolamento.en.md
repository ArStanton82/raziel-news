---
title: "Hermes Grows by Plugins, and Learns to Fence Them In"
date: 2026-10-30
draft: false
categories: ["AI", "Hermes"]
tags: ["Hermes", "plugin", "sandbox", "security", "Gemini"]
summary: "Three new plugins in the Nous repository, and two fixes that tighten the boundary between a plugin and the installation."
url: "/en/2026/10/hermes-grows-by-plugins-and-learns-to-fence-them-in/"
---

In the last forty-eight hours the Hermes ecosystem has moved in a direction worth watching: not the direction of new features, but that of boundaries. Three plugins have appeared in the repository of the NousResearch organisation, and on the same day two fixes in the core concerned precisely what happens when a plugin is installed. Read together, the two pieces of news tell the same thing from opposite sides: the surface grows, and someone is drawing the fence.

## Three new doors

`hermes-plugin-sprites` brings a terminal backend on a Fly.io sandbox with checkpoint and restore: the machine the agent runs on stops being a disposable environment and becomes a state that can be saved and resumed. `hermes-plugin-solstice` does something subtler and more political: it brings Gemini inside Hermes using the user's own quota via OAuth, "including Gemini 4 Argon", instead of a key shared by the centre. It is the per-user model applied to a closed provider, and it moves the cost — and the responsibility — from whoever runs the instance to the account of whoever uses it.

The third, `hermes-collective-wisdom`, is the most opaque: the description says only "plugin that enables collective wisdom features", zero stars, one push at 04:37 UTC. A plugin without documentation is a hypothesis, not a product: we do not know what it collects, from whom, or where it ends up. Worth remembering every time a suggestive name arrives before the code does.

## The boundary tightens

The more interesting fix adds nothing. Commit `903230b` changes `plugins doctor` so that it stages only the plugin it is validating. Before, a folder holding a plugin alongside other files was copied in full — the commit message cites the example of a Downloads folder with disk images inside — and the doctor answered OK all the same. Or it copied a category with several plugins and failed only after finishing the copy. Now it refuses before touching anything.

That is hygiene, but it is also an uncomfortable lesson: the tool that certifies the health of an installation was the least supervised part of the installation. Whoever validates something should have a smaller reach than the thing it validates, not a larger one.

## Error as interface

The second commit, `ef35e8b`, rewrites the error card of the desktop client: it separates blocking errors from degraded ones, exposes a single primary action at a time, offers the raw details in a copyable block and translates the text into all eight languages of the app. No release note accompanies the work: the latest public release remains v0.22.5 of 23 October. The repository's history and the product people download run at two different speeds.

A plugin is, by definition, an act of trust delegated to someone else. The useful question is not how many plugins exist, but how narrow the passage is through which they enter. Today that passage narrowed a little, and it is not the loudest story of the day: it is only the one that matters most.

---
*Verified sources: GitHub API `NousResearch/hermes-agent`, commits `ef35e8b` (30 October 2026, 06:07 UTC) and `903230b` (30 October 2026, 04:35 UTC); GitHub API NousResearch organisation, descriptions and push dates of the repositories hermes-plugin-sprites, hermes-plugin-solstice, hermes-collective-wisdom (30 October 2026); GitHub API release hermes-agent v0.22.5 (23 October 2026).*

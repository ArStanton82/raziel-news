---
title: "Hermes 0.23.3: the patch that refuses to explain itself"
date: 2026-11-20
draft: false
categories: ["AI", "Hermes"]
tags: ["Hermes", "release", "plugin", "maintenance"]
summary: "Three hundred and seventy pull requests in a patch tag, and release notes that stay silent on purpose: maintenance has become the product."
url: "/en/2026/11/hermes-0-23-3-the-patch-that-refuses-to-explain-itself/"
---

At 00:34 UTC today Nous Research published Hermes Agent 0.23.3. The release notes are explicit with their numbers: 1,657 non-merge commits across 3,948 changed files, +222,379 lines added and 96,154 removed, 370 pull requests merged and 60 issues closed since 0.23.2 existed. Then comes the sentence worth more than all the others: the interesting things inside that window are excluded «undocumented here on purpose», and will arrive with the curated notes for 0.24.0.

## A patch that refuses to explain itself

Anyone reading the notes finds a list of what is not being told: a lifecycle controller for the prompt cache, compaction that archives tool results instead of discarding them, proactive pruning of results enabled by default, a CLI first-run setup cut down to a single question, the GPT-6.2 Astra and Sol models on OpenRouter and Nous Portal, a separate persistence layer behind an interface with a SQLite backend, some dependency security updates.

This is serious material, and all of it is deferred. For an agent that presents itself as «the one that grows with you», growth is now almost entirely plumbing: caching, pruning, persistence. The visible part of the product has settled; the work has moved underneath.

## The bottleneck is installation

The proof arrives a few hours after the tag. Between 05:17 and 08:14 UTC today Teknium merged three commits that do not touch the model, but the way you hand it the keys: plugin configuration now masks platform tokens and rejects list inputs that YAML misreads; terminal installation lists the new plugin's settings and offers to change them right away; an empty variable no longer counts as «set».

These are boring and extremely important fixes. The limit of an agent is no longer convincing the model: it is handing over credentials without printing them on screen, and installing it without a manual. Anyone who has put an assistant into production knows: that is where you lose the user.

## The catalogue moves more than the code

At 03:49 UTC the same day another commit re-pinned five catalogue entries — memory-wiki, bubblewrap, homeassistant, spotify, camofox — to revision `269ddcbc85` of `hermes-official-plugins`. The evening before, seventeen official and labs plugins had been re-pinned. The catalogue, in short, changes more often than the engine.

The same day also brought Livetalk, a community plugin on GitHub (MIT, full-duplex voice chat on Gemini Live, key kept in the local backend): not an official product, but proof that the extension layer is mature enough to produce things nobody planned.

The conclusion is less banal than it looks: a release that refuses to recount itself is discipline, not laziness, but it also means that, for now, version numbers measure housekeeping. The real verdict shifts to 0.24.0: whether the notes will arrive, and whether installation will become a strength instead of a footnote.

---
*Verified sources: GitHub, Hermes Agent v0.23.3 release (20/11/2026, 00:34 UTC); whatsnew.fyi, mirror of the release notes (20/11/2026); GitHub API, commits 65c9b93, 595accf, b1ef9be (20/11/2026); GitHub API, commit 6f533d4 «plugin-catalog: re-pin» (20/11/2026 03:49 UTC) and 6edac63 (19/11/2026); GitHub, repository cruzlxyz/livetalk (README and v2.0.0 release, consulted 20/11/2026).*

---
title: "The Plugin Became the Product: Hermes' Hackathon Closes Tonight"
date: 2026-11-11
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes-agent", "plugin", "hackathon", "nous-research", "ecosystem"]
summary: "Hermes' plugin hackathon closes today: 20,000 dollars in prizes, hundreds of projects. And a 14 MiB bug explains why the plumbing matters."
url: "/en/2026/11/the-plugin-became-the-product-hermes-hackathon-closes-tonight/"
---

At 5 p.m. in New York, 11 p.m. in Italy, submissions for the Hermes Agent Plugin Hackathon close. Nous Research opened it on November 4 with one week on the clock, 20,000 dollars in prizes and a promise: accepted plugins would go into the new Hermes Marketplace, where anyone running the agent can install them. Last night the official account wrote that entries already number "hundreds" and that the jury is about to get to work. This is not a financial story. It is, though, a sign that for Hermes the edge of the product has moved: it is no longer the model that answers, it is what gets attached around it.

## A catalogue, not a shop window

The hackathon rules say a lot about how Nous imagines the ecosystem. A video is not enough to enter: you have to open a pull request that adds the plugin to the official catalogue, publish a demo under 90 seconds and submit both links. Judges weigh usefulness, reliability, polish and creativity, and — in the call's own words — "favour plugins that do more than a prompt or a skill could". The real prize is not the money: it is a place in an index users can consult.

## The bug that explains why the pipes matter

While the demos piled up, Tuesday brought patch v0.23.1: some 618 pull requests rolled into a stability release, but with one fix worth reading. Since November 9 the published `plugin-catalog.json` had gone past the 2 MiB ceiling that clients accept; the result was that every install silently fell back on the catalogue bundled in the release. Plugins added after the last update vanished, old pins were installed, the "removed" entries never arrived. The fix raises the limit to 16 MiB, so the live catalogue becomes usable again.

That is the detail that decides whether an ecosystem exists or merely appears to. A hackathon produces ideas; a catalogue that keeps updating makes them installable. Anyone still on v0.23.0 or earlier keeps seeing the old copy until they update — and that is, in miniature, the story of every software distribution.

## The queue you can't see

Meanwhile the other half of the story is moving. The beta waitlist is open on Nous' official site. The figures going around are the community's, not the company's: the HermesWatcher account speaks of roughly 100,000 people waiting and a full release between Thanksgiving and Christmas, with the beta capped by the tester limits Apple and Google impose. The same account puts the arrival of the Desktop and web app redesign one or two weeks out, with no intermediate beta. They are plausible and unconfirmed: read them that way.

The certain thing is that the ecosystem is organising on three levels — plugins, catalogue, client — and that the bottleneck is no longer the imagination of developers. Hundreds of projects in seven days prove it. The problem, as always, is maintenance: who reviews, who breaks, who bumps the pin. Tuesday's v0.23.1 is there to remind us.

---
*Verified sources: official @NousResearch thread on the hackathon (November 4 and 10, 2026); Hermes Agent v0.23.1 release notes on GitHub (published November 10, 2026, release date November 9); Hermes Agent mobile beta sign-up page, hermes-agent.nousresearch.com/mobile (consulted November 11, 2026); @HermesWatcher post on the waitlist and the Desktop redesign (November 11, 2026, community source, not confirmed by Nous Research).*

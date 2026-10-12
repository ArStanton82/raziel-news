---
title: "Hermes Agent v0.21.7 and the switch to tagged releases: the project grows up"
date: 2026-10-12
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes-agent", "nous-research", "open-source", "release", "plugin", "missingno"]
summary: "Hermes Agent ships v0.21.7 and moves to tagged releases: the open source project from Nous Research chooses stability."
url: "/en/2026/10/hermes-agent-v0217-tagged-releases-the-project-grows-up/"
---

On 12 October, at 05:53 UTC, Nous Research published Hermes Agent v0.21.7. Read on its own, it is an ordinary patch release, the second cut by the new distribution pipeline. But the most interesting detail is not in the version number: it is in the rule it introduces. From today, a source installation of the official repository updates to the latest tagged release `vX.Y.Z`, no longer to every commit on `main`. Anyone who wants to keep following daily development has to ask for it explicitly.

## From the rhythm of commits to the rhythm of releases

For a project born as a tool for developers, it is a change of posture. Updating on every commit means living on the razor's edge: you get the new features immediately, but also the defects that have not been filtered out yet. Moving to tagged releases introduces a slower, more predictable rhythm, the same one adopted by software that people use to work, not just to experiment. v0.21.7 brings no major features — the roll-up of roughly 204 pull requests will serve v0.22.0 — but it consolidates this distribution infrastructure: a switch in Settings ▸ About ▸ Updates, a dialog that tells you which channel you are on, and updates that no longer fail behind certain firewalls. The signed "reasoning" now also survives `hermes chat --resume`.

## Open source and business are not opposites

The context in which this release arrives is significant. On 7 October Nous confirmed a 90 million dollar Series B at a 1.5 billion valuation, led by Robot Ventures with Nvidia, Microsoft M12, Samsung, Union Square Ventures, Y Combinator and Menlo Ventures among the participants. Total funding rises to 158 million and the capital finances the enterprise push with "Hermes for Businesses". The message going around is clear: giving the software away can be how the business starts, not its opposite. The WSJ reports a run-rate of roughly 36 million dollars in mid-September, with the goal of passing 100 million by the end of the year.

## Official plugins only, and a free model

On the operational side, co-founder Teknium has made clear that only the official plugins maintained by Nous will end up in the `hermes-official-plugins` repository, not the community ones: "We are only putting official, nous maintained plugins in that repo". Meanwhile MISSINGNO is still available for a limited time: a model for coding and agentic reasoning that Nous describes as very token-efficient and offers free on Nous Portal. A market announcement, but also an adoption test.

## Conclusion

Hermes is becoming a product with a disciplined release cycle, an enterprise offering and a plugin ecosystem with clear rules. It is the passage from enthusiasm to maintenance: less spectacular, but it is the phase in which an open source project proves it can last beyond the initial curiosity.

---
*Verified sources: github.com/NousResearch/hermes-agent (release v0.21.7, published 12 October 2026, 05:53 UTC) and releasebot.io (12 October 2026); techcrunch.com, startupfortune.com, techfundingnews.com, digg.com and zetik.com on the 90 million Series B and "Hermes for Businesses" (7 October 2026); nousresearch.com and portal.nousresearch.com on MISSINGNO (10 October 2026); github.com/NousResearch/hermes-official-plugins (push 11 October 2026); x.com/Teknium on the official plugins and the Ultrafast tier (12 October 2026). Note: TechCrunch cites "more than 24 million clones", the WSJ "more than 22 million downloads"; the difference depends on the metric used.*

---
title: "Hermes: the plugins that win are the ones that slow the agent down"
date: 2026-11-21
draft: false
categories: ["AI", "Hermes"]
tags: ["hermes", "plugin", "hackathon", "agents", "security"]
summary: "The top places at the Hermes hackathon are not new capabilities but gates: the agent that wins is the one that knows how to stop."
url: "/en/2026/11/hermes-the-plugins-that-win-are-the-ones-that-slow-the-agent/"
---

Seven days, nearly a thousand submissions through the official form, 1,508 pull requests counted by an independent tracker and 743 plugins already merged into the catalogue at closing. Those are the numbers of the Hermes Agent Plugin Hackathon, which closed on 11 November and handed out its awards on Friday 20 November with a 20,000-dollar prize pool. But the interesting figure is not the volume: it is the ranking.

First place went to Foreman, by Pedro Valencia: a gate that reads the real diff before every commit and blocks the agent that skips or deletes tests, changes the test command or slips in a secret. A second model reviews what the rules cannot see, and a human approves the merge from Telegram. The agent cannot run `gh pr merge` on its own. In third place Plan Mode blocks the tools that can change the project until you give the go-ahead; fourth Seedguard keeps seed phrases, keys and 2FA codes out of the model's context; fifth Ariadne replays past sessions to work out whether an update will break something; sixth Mandate, with least-privilege mandates for cron jobs; seventh safe-swap, which rewrites destructive commands into harmless variants; eighth Promise Keeper, which turns your rules into explicit constraints.

## A brake, not a muscle

Seven of the top eight add no capability: they remove it. The only exception is Housemate, runner-up, which turns old phones and laptops into voice-controlled home speakers. It is a likeable product, but it is not what the judges rewarded en masse.

The most honest explanation is that the bottleneck has moved. Once an agent can already write code, search the web and talk on Telegram, the problem is no longer what it can do: it is whether you can trust what it has done. A green test that the agent patched itself is not proof, it is a promise. The winners are all ways of making that promise verifiable by someone else.

## Where developers spend their energy

The hook most used by the competing plugins is `pre_tool_call`, declared by 388 projects, followed by `pre_llm_call` with 341. Developers concentrate where a decision is about to turn into an action. That is where you can still say no.

There is also a lesson in the numbers: the «nearly a thousand» submissions claimed by Nous and the 1,508 pull requests in the independent catalogue say how much work stays outside the official forms. Of 1,508 openings, 743 had already been accepted: just under half. The Marketplace is not a shop window, it is a filter.

## Trust as a feature

For years the story of agents ran incrementally: more tools, more integrations, more autonomy. This hackathon suggests the next phase will be subtractive. The plugin that wins is not the one that does more, it is the one that stops the agent from doing the wrong thing while nobody is watching.

One uncomfortable question remains, and it concerns the people writing this too: how many of these gates survive a hurry? A Telegram approval is only useful if someone actually reads it.

---
*Verified sources: Nous Research, announcement and 1st-10th place ranking, nousresearch.com and x.com/NousResearch (20 November 2026); hackathon rules and prizes, @NousResearch post of 5 November 2026; Foreman plugin README, github.com/PedValme/foreman (21 November 2026); independent census of submissions, aaddrick.com/hermespluginhackathon (snapshot 11 November 2026); catalogue entries for Promise Keeper, Housemate, safe-swap and Mandate (21 November 2026).*

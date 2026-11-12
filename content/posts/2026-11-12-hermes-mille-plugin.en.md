---
title: "A Thousand Plugins in Seven Days: Hermes' Hackathon Closes and Moves the Bottleneck"
date: 2026-11-12
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes agent", "plugin", "hackathon", "nous research", "catalogue"]
summary: "Nearly a thousand plugins in a week for 20,000 dollars in prizes: the problem is no longer inventing them, it is reviewing them."
url: "/en/2026/11/a-thousand-plugins-in-seven-days-hermes-hackathon-closes-and-moves-the-bottleneck/"
---

Submissions closed at 5pm New York time, 23:00 in Italy, and the count arrived a few hours later: «nearly 1,000 entries». Twenty-four hours earlier Nous Research was still saying «hundreds». The jury is now selecting the ten finalists and the winners will arrive by email «in about a week».

That number should be read for what it is: not a thousand products, but a thousand applications for admission to an index.

## A twenty-thousand-dollar prize and a single rule

The brief was linear: 20,000 dollars in total, split across five places (10,000, 5,000, 2,500, 1,500 and 1,000 dollars) plus five honourable mentions. A video was not enough to enter: you had to open a pull request adding the plugin to the official catalogue, publish a demo under 90 seconds and submit both links.

Two details say more than the prizes. There are ten prize places, exactly as many as the entries the jury is selecting. And the application coincides with publication in the catalogue: you do not win a contest and then enter the marketplace, you enter the marketplace and the jury decides what it is worth.

## The bottleneck has moved

A thousand projects in seven days do not measure developers' imagination. They measure the review capacity of whoever has to take them in. With a ratio of one to a hundred between finalists and applications, selection is the real product of the hackathon.

The catalogue, meanwhile, has already shown signs of strain. The community plugin Hermes Multiplayer was added on November 11 and re-pinned four times over a single day: first for a rename of its tools, then for two outdated tests, and finally for the removal of the built-in relay — a piece of infrastructure that was no longer its own. Release v0.23.1 (618 pull requests squashed into one patch) instead raised the catalogue ceiling from 2 to 16 MiB: the published file had outgrown it, and every installation was silently falling back to the copy bundled with the client.

These are maintenance details, and they are the part no hackathon rewards.

## Who pays the plugin's bills

Then there is the question the thousand projects leave open: who carries the running cost. The new community plugin X Bookmarks — which turns X bookmarks into a weekly digest on Hermes — requires its own X developer app on pay-as-you-go terms, plus Hermes v0.23.0 or higher. It works, but it pushes a key and a bill onto the user.

It is the same pattern as the relay removed from Multiplayer: as a plugin grows, the parts that cost money or responsibility tend to leave the code and return to the user. An ecosystem that went from hundreds to a thousand entries in seven days has not solved that point. It has multiplied it.

The right question, in the end, is not how many plugins were written. It is how many will still be installable in six months, with an updated pin and someone answering the issues. The answer arrives in a week, when the jury publishes ten names out of a thousand.

---
*Verified sources: @NousResearch announcement on the close of submissions and the «nearly 1,000» entries (November 12, 2026), picked up from the Announcements section of nousresearch.com; Hermes Agent Plugin Hackathon brief with prizes and entry requirements (November 4, 2026); GitHub API NousResearch/hermes-agent, commits `feat(catalog): add the hermes-multiplayer plugin entry`, `bump … pin to a60c87a`, `bump … to a744368`, `Re-pin … to 8dee088 (built-in relay removed)` (November 11, 2026); Hermes Agent v0.23.1 release, published November 10, 2026, 618 PRs and catalogue ceiling raised from 2 to 16 MiB (#151860, fixes #151856); @HermesWatcher post on the X Bookmarks plugin and its access requirements (November 12, 2026, community source).*

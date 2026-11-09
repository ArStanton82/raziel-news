---
title: "Hermes Learns to Audit Itself, and to Check Who Signs Off"
date: 2026-11-09
draft: false
categories: ["AI", "Hermes"]
tags: ["hermes agent", "security", "plugin", "approvals", "subagent"]
summary: "Nous Research ships the Security plugin for Hermes and tightens the approval chain: trust is not a click."
url: "/en/2026/11/hermes-audits-itself-and-checks-who-approves/"
---

In a little over twenty-four hours Nous Research did two things that, at first glance, have nothing to do with each other: it published a plugin that reads a repository the way an attacker would, and it rewrote the way the agent asks permission to run a command. Two separate moves, telling the same story. An agent that writes code, runs it and ships it needs two guarantees that cannot be delegated to the user's enthusiasm: someone to check the code, and someone to check who gives the green light.

## A reviewer that starts from the right question

The plugin is called `hermes-security` and it has entered the official plugin repository, so it is not a community project dressed up as a product. The approach is more interesting than the average scanner: before looking for bugs, the agent builds a map of what an attacker can reach and which inputs the code trusts. Then it splits the code into chunks, hands them to parallel subagents, and every candidate finding is re-checked against the code to establish whether an attacker can actually get there.

The step that changes the craft is empirical confirmation: the agent writes a small reproduction for each finding and runs it against a temporary copy of the repository. The reports hold evidence, tests and discarded candidates together with the reason for exclusion, because a documented false positive tells you which areas have already been looked at. Patches stay read-only; Hermes 0.21.5 or later with Python 3.11 is required.

## Permission is no longer just any click

The second move is quieter and, in some ways, more important. A series of commits on 9 November closes a race window in the publishing of approval requests: a card that does not carry the request id no longer resolves any request, and every request is born in a "deny only" state until the card, or the full submission of the command, shows the complete command. In plain terms: you no longer approve something you have not seen.

The densest commit introduces `approvals.approvers`, an optional list that in shared chats restricts who can answer — the requester, the listed approvers, or a platform administrator — on Discord, Matrix, Telegram and QQ. The default stays permissive (any admitted member can answer), but the direction is clear: approval stops being an anonymous gesture.

## Why it matters more than an announcement

In the same hours Nous Research wrote that an agent able to change models or code without saying so is "like building on shifting sand". That is a positioning statement, not an announcement: a heading. The point holds, though. An agent's security is not measured by how good it is at not making mistakes, but by how reconstructable its actions are when it does.

An audit that keeps false positives and an approval tied to an identity are parts of the same accountability infrastructure. Installing the plugin is easy; reading the report and signing your own approvals rather less so.

---
*Verified sources: official repository NousResearch/hermes-official-plugins and the hermes-security README (read 9 November 2026); Hermes Marketplace catalog page for hermes-security (9 November 2026); commits 466591fe65d0257c96083df16fcd39636032304c and 085d8b5d987699e95c410186fb65052c8ef5657c on NousResearch/hermes-agent, verified through the GitHub API with date 9 November 2026; @NousResearch post of 8 November 2026 on positioning (a quote, not an announcement).*

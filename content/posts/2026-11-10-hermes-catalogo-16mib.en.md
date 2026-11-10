---
title: "The Plugin That Wasn't There: Hermes 0.23.1 and the Two-Megabyte Ceiling"
date: 2026-11-10
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes-agent", "plugin", "release", "nous-research"]
summary: "The Hermes plugin catalogue crossed the 2 MiB limit and installs silently fell back to the local copy: the patch raises the ceiling to 16."
url: "/en/2026/11/the-plugin-that-wasnt-there-hermes-0-23-1-and-the-two-megabyte-ceiling/"
---

For a little more than a day, anyone who tried to install a freshly published plugin in Hermes Agent saw the same scene: the command runs, returns an outcome, and the plugin is not there. No error, no warning. Just the old catalogue, the one bundled with the release.

## Two megabytes of silence

The cause is small and instructive. The plugin catalogue published on the site on November 9 crossed the 2 MiB ceiling the clients accept: beyond that threshold the response is treated as corrupt, the client writes one line to the debug log and falls back to the local copy. Three consequences, the last of which is the most irritating: the new plugins do not exist on that machine, those repinned to more recent commits install at the old version, and the newest removal entries become invisible, so a formally retired plugin still looks installable. Patch v0.23.1, tagged at 01:42 UTC on November 10, raises the ceiling to 16 MiB, roughly nine thousand entries according to the changelog. Anyone staying on v0.23.0 or earlier keeps using the local catalogue until they update.

## A patch release as a census

The version is declaredly about stability, not features, and it also serves to photograph the window: about 618 merged PRs, 2,578 non-merge commits, 2,781 files changed, 409 issues closed. The curated notes will come with v0.24.0, and the choice not to duplicate them here says something about the project's pace. In between, almost in passing, a few changes that alter daily use: backtracking with Esc in the TUI, group chats running on a gateway without Desktop, the built-in browser signing with the real browser's profile and filling in saved logins from the address bar, the new plugin API hooks.

## The cloud and the models

In the background, two pieces of the same design. On November 9 Nous Research announced that Hermes Cloud agents open in a browser tab with the same interface as Desktop: you pick a name and a model on Nous Portal and the agent runs in a container, reachable from your phone even with the computer off; the Plus, Super and Ultra plans include one. The same day Claude Fable 5.2 arrived in Hermes via Nous Portal, OpenRouter and the Claude subscriptions, and on Venice at 8 and 40 dollars per million tokens, that is at Anthropic's list price for the model, with a million tokens of context.

The lesson of v0.23.1 is not technical, it is about perception: a system that degrades in silence looks like it works. The fallback is the right choice, the silence is not. One update and one test install are enough to tell the two apart.

---
*Verified sources: GitHub release NousResearch/hermes-agent v0.23.1 (November 10, 2026); Hermes Agent Changelog, hermes-agent-lab.com/releases/v0-23-1 (November 10, 2026); nousresearch.com Announcements on Hermes Cloud (November 9, 2026); Anthropic release notes for Claude Fable 5.2 (November 9, 2026); CNBC on the launch of Fable 5.2 and Mythos 5.2 (November 9, 2026).*

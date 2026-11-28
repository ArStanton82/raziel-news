---
title: "Three hundred and thirty-eight PRs, no notes: the patch that postpones the story"
date: 2026-11-28
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes agent", "release", "agents", "open source"]
summary: "Hermes v0.23.5 aligns CLI, Store, Docker and Cloud on 338 merged PRs, while the curated notes slip to v0.24.0: the changelog is written by others."
url: "/en/2026/11/three-hundred-and-thirty-eight-prs-no-notes/"
---
At 03:20 UTC today Hermes Agent v0.23.5 was released. The release body dates it 27 November, the tag arrives on the 28th: it is the first detail of a version that seems to want to pass unnoticed. Inside the window from v0.23.4 there are 338 merged pull requests, 1,262 non-merge commits, 1,146 files changed (+57,989 / −5,346) and 92 issues closed, measured at commit `a428f5344f77`. The curated notes, however, will arrive with v0.24.0. Translated: you update now, you understand later.

## The terminal remembers
The most interesting item is not in the notes, and is declared "undocumented here on purpose": the CLI and the TUI support the OSC 7577 resume protocol. Hermes now tells the terminal the command to reopen the session — `hermes -p PROFILE --cli --resume SESSION_ID` — authenticated with a token from the pane, and clears it only on `/quit` or Ctrl+D. The record survives crashes, loss of the terminal and restarts from `/update`: precisely the cases in which a session ought to be offered back. Persistence stops being an application feature and becomes a terminal convention.

## The agent works with the window closed
The second change is silent: the gateway compacts idle chats in the background. Before, it noticed only at the next message, which then waited for the summarisation; now the maintenance tick that already runs every five minutes takes on the expired conversation. The threshold is `compression.idle_compact_after_seconds`, default `0`, therefore off, and it can be set per single channel. In the author's test on a custom endpoint: from 16 to 8 messages, from roughly 8,611 to 3,665 tokens, and the following prompt down from 28,310 to 5,865.

## The profile is the boundary
Then there is the item that matters to anyone installing plugins: a set of fixes ties the work of the plugins to the name of the profile it was opened with (`owner_home`), not to the resolved directory. When `profiles/<name>` is a symlink outside the root, it was previously possible to launch the launcher named in that profile's `config.yaml` and have a `PYTHONPATH` from its `.env` reach the child process of the plugin host. Now, if no name leads to that directory anymore, the work is refused with a moved-home error. It is a security fix told as maintenance.

## The price and the desktop
On the commercial backdrop, Nous's Black Friday: 50% off the first month of a new or upgraded Portal plan with the code FIFTYFIFTY, for 24 hours from the 27 November post, with a promotional page behind a login. On the desktop, merge `d71a657` at 04:35 UTC brings in-app updates for Linux AppImages, with two fixes in the update lookup.

The editorial point is versioning as an act of communication. A patch that aligns CLI, Microsoft Store, Docker and Hermes Cloud on the same code is a matter of hygiene, but postponing the notes means asking for trust: update without knowing what changes, we will tell you at the next minor. In the meantime the changelog is written by others, and for once the most useful documentation is outside the repository.

---
*Verified sources: GitHub release v0.23.5 and GitHub API on 28/11/2026 (publication 03:20 UTC, commit `a428f5344f77`, window counts); independent changelog hermes-agent-lab.com/releases/v0-23-5 (28/11/2026, details on OSC 7577, compaction and owner_home); @NousResearch post of 27/11/2026 and promotional page portal.nousresearch.com/promos/fiftyfifty; GitHub API for commit `d71a657` (merge 28/11/2026, 04:35 UTC).*

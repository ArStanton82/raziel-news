---
title: "Eight Messages and Then a File: the Night Hermes Stopped Cutting Replies Short"
date: 2026-11-13
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes agent", "gateway", "telegram", "discord", "bug fix"]
summary: "A runaway 402-message reply led to a new rule: past the cap the text is no longer truncated, it is delivered as a file."
url: "/en/2026/11/eight-messages-and-then-a-file-the-night-hermes-stopped-cutting-replies-short/"
---

Four hundred and two messages in a single private Telegram chat. That is not a productivity record, it is a bug: a reply so long it never ended, sent out in pieces until the adapter stopped counting. From that edge case, tracked as issue #152012, came a chain of fixes that in the night between November 12 and 13 changed a product rule, not just a function.

## First the cap, then the rethink

The first remedy was the most banal: a limit of eight messages per reply (`MAX_SPLIT_MESSAGES`), borrowed from Discord. Past the eighth piece the text was cut and replaced by a truncation notice localised across seventeen translation catalogues. It worked, in the sense that it kept the bot out of a flood ban. It failed in the sense that it lost the reply.

The review turned the setting upside down: a file is better than a mutilated answer. In pull request #153476, merged at 06:36 UTC on November 13, a reply that exceeds the cap is uploaded as a single Markdown document, with a translated caption, and the messages already posted are deleted only once the upload is confirmed. The measurements in the commit are explicit: a 415,000-character reply opened 18 messages on the branch and 133 on main; on Discord, 60,000 characters made 33 messages.

## The case that decides everything: when the upload fails

The interesting part is the error branch. If Telegram rejects the document, or Discord cannot upload it, the fallback is not truncation again: it carries on with ordinary messages from the point where the chat had stopped, at the pace the adapters impose. On Telegram files above 45 MB are split, on Discord the limit is 7 MB. An end-to-end test with a rejected upload and a 429 halfway through the fallback shows it plainly: before, 8 messages, 13,843 characters and a notice; after, 31 messages and the whole reply, with no notice.

## The detail nobody would have noticed

Then there is the bug inside the bug. When the agent, after a round of tools, streams the same reply again, the second segment again exceeded the cap and its handoff uploaded a second file: 60,002 bytes against the first one's 60,000, because the ledger prepended a double newline. The final comparison matched the first file and nobody noticed. Now the gateway compares the displayed form against the files already delivered and, if it is a repeat, deletes the previews and closes the turn without uploading anything.

It is the kind of fix nobody sees: no user will ever write "thanks for not sending me the same document twice". But an agent that loses text in silence is an agent you don't trust, and the difference between cutting and delivering a file is the difference between a hidden error and a handled one.

None of this is in a release yet: the last tagged one is still v0.23.1 from November 10. Anyone on the stable version, today, still has the old compromise.

---
*Verified sources: NousResearch/hermes-agent repository on GitHub — commit `fix(telegram): cap split delivery on send and edit-overflow paths` (issue #152012), commit `fix(gateway): a reply past the 8-message cap arrives as one file, nothing cut off`, `fix(discord): a long reply whose file upload fails is sent whole, never cut at 8`, `fix(gateway): a reply past the 8-message cap is one file on every path the review found` (November 13, 2026, 05:18–06:36 UTC), `fix(gateway): a reply repeated after a tool round is not uploaded as a second file`; pull request #153476 "Telegram and Discord replies past 8 messages arrive as one file, nothing cut off (#152012, salvage #152071)", merged_at 2026-11-13T06:36:29Z; GitHub releases API, latest release v0.23.1 published November 10, 2026 (all consulted November 13, 2026).*

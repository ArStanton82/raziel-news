---
title: "A Hundred Fixes in One Weekend: Hermes Makes Security a Maintenance Job"
date: 2026-11-16
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes agent", "security", "release", "plugin"]
summary: "More than a hundred fixes in one weekend, 0.23.2 still stuck in release candidate and a switch for the automatic review."
url: "/en/2026/11/a-hundred-fixes-in-one-weekend-hermes-makes-security-a-maintenance-job/"
---

While the rest of the industry measures its news in announced models, Hermes spent the weekend doing the one thing you cannot put in a launch post: fixing. A batch of more than a hundred fixes, according to the channel that follows the project, touched the way secrets are handled inside the agent — in error messages, in tool output and in logs.

This is not a product note, it is the kind of work you only notice when it is missing.

## What actually changed

The public description talks about new keys being recognised and masked: recent formats from Gemini, Tavily, SendGrid, Slack, Discord, Teams. The evidence in the repository is consistent: between November 13 and 16 there are 178 commits citing secret redaction and 21 merged pull requests carrying the work prefix `sec3/`, including one on redacting credential files and one on lines that contain secrets. In parallel a burst of `fix(approval)` commits closed holes in the command scanner: heredocs, scripts written and then executed, sinks into interpreters with redirects.

It is an unglamorous and very concrete detail: most credential leaks do not come through an exotic attack, they come through a log line nobody had anticipated.

## The release does not chase the commits

The 0.23.2 line stays parked on release candidates: rc.8 was tagged on November 14 at 18:53 UTC with an automation-generated body, no product notes, and it was not promoted. The last stable version remains v0.23.1 from November 9, which had a single declared job — raising the ceiling of the plugin catalogue from 2 to 16 MiB, because the published file had grown past the limit clients accept and every install was silently falling back to the catalogue bundled in the release.

Meanwhile the canaries keep coming out every morning: today's was published at 07:59 UTC. The curated notes for the whole window, the release says, will arrive with v0.24.0.

## The switch that stays in the operator's hand

One detail more useful to people who use the agent than to those who develop it: the automatic background review — the one that revisits the conversation to suggest memories and skills — is switched off with a single configuration line, `auxiliary.background_review.enabled: false`, without touching memory and without resetting the reminder intervals. The documentation confirms the key has to be read under the `auxiliary:` block; a top-level `background_review:` block is not taken into account.

The lesson of the weekend is sober. Security is not announced, it accumulates: a hundred invisible fixes are worth more than a feature in the shop window, and the fact that the stable line was not forced forward to chase them is, in this case, a sign of discipline rather than delay.

---
*Verified sources: GitHub API NousResearch/hermes-agent, releases (11/16/2026, latest canary v0.23.1+canary.20261116T070005Z at 07:59 UTC); release notes v0.23.1 (11/09/2026); release page rc.8-v0.23.2 (11/14/2026, 18:53 UTC); commit and pull request search on the repository (11/13-11/16/2026); Hermes documentation, /docs/user-guide/features/memory (11/16/2026); posts by @HermesWatcher and @Teknium on X (11/16/2026) as interested-party statements. A report of a fake "Hermes Agent - AI" app on the Play Store was excluded: single source, no official confirmation.*

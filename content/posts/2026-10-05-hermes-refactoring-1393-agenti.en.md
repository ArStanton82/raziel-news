---
title: "A million lines, 1,393 agents: Hermes rewrites itself"
date: 2026-10-05
draft: false
categories: ["AI", "Hermes"]
tags: ["Hermes", "Nous Research", "autonomous agents", "refactoring", "plugin"]
summary: "Hermes cleaned up a million lines of code in 19 hours with 1,393 subagents: 19,300 dollars for an estimated value of 1.8 million."
url: "/en/2026/10/million-lines-1393-agents-hermes-rewrites-itself/"
---

There is a way of telling the story of automation that insists on speed. There is another, more interesting one, that insists on what is left afterwards. Nous Research has just published the account of an experiment worth reading for both reasons.

## Nineteen hours, 1,393 agents

On 2 September Teknium asked his Hermes agent to clean up the agent's own repository. The main run lasted about nineteen active hours, deployed 1,393 subagents and peaked at 218 simultaneous agents. The orchestrator split the code into 36 non-overlapping groups, assigning each worker a separate git worktree, with briefs stating what to simplify and which interfaces to preserve. The PR was merged on 4 September.

The final numbers: non-test Python lines went from 1,063,826 to 698,363, down 34.4 per cent. The largest file, gateway/run.py, fell from 34,847 to 5,512 lines; functions longer than 300 lines from 192 to 2; the longest if/elif chain from 92 branches to 9. The estimated model cost is about 19,300 dollars, roughly 25,000 with the follow-up sessions. The estimate for doing it by hand was between 150,000 and 1.8 million dollars.

## The lesson that remains

The point is not the saving, but the mechanism. The agent had accumulated a skill — hermes-agent-dev — built by correcting real mistakes: that is where the instructions on how to prepare a PR and how to verify a change come from. The post does not hide the costs: about 65 exception-handling points were rewritten incorrectly and fixed only thanks to community review; the number of modules and import dependencies grew; six files still exceed 5,000 lines. At about fifty minutes in, an authentication token expiring killed the run, which was picked up by a separate session.

## An ecosystem in motion

Around this core the community grows. Teknium confirmed on X that the team is expanding by two or three people, with three dedicated to the mobile app; the plugin catalogue lists eight official "tested" entries, but the review is not a security certification: it protects against malicious agents, it does not guarantee that a plugin is robust. Then there are the community reports: the Oh My Hermes 3.0 plugin is said to have been added to the catalogue, and someone managed to run the Hermes runtime directly on an Android phone via Termux.

## Conclusion

The useful question is not whether an agent can do a team's work. It is what happens when it gets it wrong: whether there is a net — human review, written skills, verifiable commits — capable of noticing and repairing. The Hermes refactor is convincing precisely because it also tells you about its stumbles.

---
*Verified sources: Nous Research, "Refactoring Hermes with 1,393 agents" (nousresearch.com, September 2026, consulted on 5 October 2026); technical analysis of the refactor on hermes-agent-lab.com; official documentation of the Hermes Agent Plugin Catalog; posts on X by @Teknium and @HermesWatcher from 4-5 October 2026. Note: the addition of Oh My Hermes 3.0 to the catalogue and the Android runtime are reported by community sources and not officially confirmed; the count of eight official plugins is stated by Teknium on X.*

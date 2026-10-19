---
title: "Hermes SEO: forty-five skills in search of a catalogue"
date: 2026-10-19
draft: false
categories: ["Hermes", "AI"]
tags: ["plugin", "seo", "community", "mcp"]
summary: "A community plugin brings 45 SEO skills and 19 specialist roles into Hermes: powerful, but the pull request for the catalogue is still open."
url: "/en/2026/10/hermes-seo-forty-five-skills-in-search-of-a-catalogue/"
---

There is a way of reading the agent ecosystem that does not go through benchmarks, but through how the work gets divided. Last night's news is small and significant at once: "Hermes SEO", a native port of the Claude SEO toolkit, has arrived as a community plugin with 45 skills and 19 specialist roles. It is not a longer prompt. It is a division of labour imported into the agent.

## A department, not a command

The repository is blunt about it: 25 workflow skills, a `seo` router, 19 role skills, 56 utility scripts and the Schema.org templates. The port is declared against version 2.4.2 of Claude SEO, Daniel Agrici's project, and requires Hermes Agent 0.22.2 or higher. Release v0.1.0 dates from 16 October. What sets it apart from a single skill is the chain: site audit, technical, page, brief, structured data, visibility in generative engines, local, strategy. Anyone who has tried to get a serious audit out of an agent knows the bottleneck is not the writing, it is the sequence.

## "In the catalogue" is something else

The announcement circulating on X spoke of the plugin being "in the Hermes catalogue". The project's README, updated on 17 October, says something more sober: it is an independent project, separate from the official Nous Research plugins, and the pull request for the community catalogue (#139998) is still open. The repository has 48 stars; the 15,000 belong to the upstream project, not to the port. This is not a complaint, it is a distinction that matters to anyone installing: for now installation runs from GitHub with a pinned reference to the release commit, not with a command taken from the catalogue. There is also a limit the authors themselves declare: Google OAuth flows are disabled because Hermes does not yet offer an authorisation path tied to the profile.

## Meanwhile the core patches MCP

On the same day, two commits in the main repository show where the real work is happening: MCP configuration. The first, `5fc490e`, stops an unset `${VAR}` from falling back to the value inherited from the parent process. The second, `43c9e0a`, strips entries left as literal placeholders out of a stdio MCP server's environment. It looks like internal hygiene, and it is exactly the kind of detail that decides whether a plugin with optional credentials starts up or stays dark. The latest release remains v0.22.2 of 15 October: these are maintenance commits, not an announcement.

The lesson cuts two ways. On one side, an agent's value is starting to be measured in packaged skills, roles and responsibilities: the SEO plugin is interesting because it tries to teach a trade, not to answer a question. On the other, an ecosystem growing this fast needs boring foundations — environment variables, permissions, catalogues — that nobody tweets about and everybody notices when they are missing.

---
*Verified sources: GitHub repository yuzushi-dev/hermes-seo, README and release v0.1.0 (consulted on 19/10/2026); NousResearch/hermes-agent commits 5fc490e and 43c9e0a (19/10/2026); NousResearch/hermes-agent releases page, v0.22.2 of 15/10/2026; @HermesWatcher post of 19/10/2026. Discrepancy found: the post announces the plugin "in the catalogue", while the README says pull request #139998 is still open — the text reports the repository's version.*

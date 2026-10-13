---
title: "Hermes: the ecosystem grows at the edges — connectors, skills and community projects"
date: 2026-10-13
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes-agent", "nous-research", "connettori", "skill", "community", "open-source"]
summary: "While v0.21.7 consolidates the stable releases, the Hermes ecosystem grows from the ground up: multi-account connectors, the Anatomy skill and projects such as Herald OS."
url: "/en/2026/10/hermes-ecosistema-community/"
---

In recent weeks attention on Hermes Agent has gone to the release cycle and Nous Research's 90-million-dollar round. But the most interesting part, for anyone following the project closely, sits at the edges: the small features, the community contributions, the third-party projects that use the agent as infrastructure. That is where you can tell whether an ecosystem is really taking hold.

## Connectors with multiple accounts, now with names

On 12 October the project changelog recorded 42 pull requests merged on 11 October. The most useful one concerns connectors: they now support multiple accounts of the same application, each with a short alias such as "work" or "personal". Hermes can finally tell two different Gmail inboxes apart and say under which identity it made each call; repairing one account happens without touching the others. It is a detail that looks minor, but it is the difference between a tool you use in a demo and one you use at work. In the same cycle the "guest" identity also arrived: those without a Nous account can use connectors, with a token scoped only to `connectors:invoke`.

## An official skill that came from the community

On the skills front, "Anatomy" has entered Hermes' official catalogue of optional skills. Born as a tool for Claude Code, it describes a machine or a technical concept starting from a single line of text and builds an interactive isometric model of it, with moving parts and live readouts. It installs with `hermes skills install official/creative/anatomy`. Co-founder Teknium presented it as an official integration: an outside contribution becoming part of the product is the clearest sign of an active community.

## Herald OS and the 3D office: building on top of Hermes

Independent projects are also growing around the agent. Herald OS, by Luke The Dev, is an "agent-native" operating system that uses Hermes as its interface: it has passed 400 stars on GitHub and adds a photo editor (Herald Canvas) and a document suite (Herald Docs, Sheets and Slides) that Hermes can be asked to work on directly. It is a project not affiliated with Nous Research — the author says so plainly — but it is also proof of how the agent gets used as a base layer. Along the same lines, one user built a "3D office" for their agents, with separate departments and a real-time view of who is working and who is idle.

## Conclusion

Hermes now has a disciplined release cycle — v0.21.7 in early October moved source updates onto tagged releases — and an enterprise offering on the way. But its durability over time is measured elsewhere: in the ability to absorb outside contributions and to become a platform for others. This week's signals point in that direction.

---
*Verified sources: github.com/NousResearch/hermes-agent (v0.21.7 release, 11-12 October 2026); hermes-agent-lab.com/blog ("Two Gmails, One Hermes: Connector Accounts Finally Get Names", 12 October 2026) and hermesbible.com/changelog (12 October 2026) on multi-account connectors and the guest identity; x.com/HermesWatcher on the roll-up of 42 PRs (12 October 2026); hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog and aihub.com/briefing on the Anatomy skill (12-13 October 2026); github.com/iamlukethedev/Herald-OS and trendshift.io (6-13 October 2026) on Herald OS; x.com/HermesWatcher on the "3D office" project (13 October 2026). Note: the report flagged no confirmation from official channels for the Anatomy skill; the official optional-skills catalogue and Teknium's announcement confirm the integration instead.*

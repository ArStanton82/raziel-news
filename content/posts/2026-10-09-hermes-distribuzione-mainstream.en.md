---
title: "Hermes leaves the terminal: Microsoft Store, catalog plugins and a release that cuts itself"
date: 2026-10-09
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes-agent", "microsoft-store", "plugin-catalog", "release", "nous-research"]
summary: "Hermes arrives on the Microsoft Store, Spotify leaves the core as a catalog plugin, and the stable v0.21.6 release pipeline debuts."
url: "/en/2026/10/hermes-leaves-the-terminal-microsoft-store/"
---

For a year Hermes Agent was an object for initiates: you installed it with a command line, configured it in a YAML file and explained it to friends with a certain air of complicity. This week the project took the step that changes the audience: it leaves the terminals and goes where everyone can find it.

## A one-click install

On 8 October Nous Research announced that Hermes Agent is now available — and prominently featured — on the Microsoft Store, with one-click installation. It is not a cosmetic detail. Distributing an agent on a store means signing the package, handling updates and accepting the rules of a closed platform, exactly the opposite of the repository culture that made the project popular. The company promises more updates for the Windows ecosystem in the coming weeks: the move suggests that the desktop, no longer the CLI, becomes the front door.

## The core gets lighter: Spotify becomes a plugin

On the repository, the commits of 9 October confirm an architectural choice: the Spotify integration leaves the core and becomes an official catalog plugin, maintained in a separate repository. Existing users are migrated automatically, login and data included. It is the logic Nous has already applied elsewhere: the core stays lean, features live in modules you install when you need them. A smaller core is a core that is easier to update and to keep secure.

## v0.21.6 and the release pipeline

On 8 October came release v0.21.6, a patch that gathers about 2,100 pull requests accumulated since v0.21.5. The interesting figure is not the number but the how: it is the first release cut by the new stable pipeline, with a single build reference, a tested Docker image and a receipt tag at publication. Docker and Hermes Cloud follow the stable channel; the desktop app, Termux packages and Microsoft Store stay on the current build until the next grouped release. Among the security fixes, the hardening of dashboard authentication against forged headers.

## The community and its excesses

The community sends the most ambivalent signals. One user reports finding himself with more than 200 skills accumulated in two weeks and asks for tools to govern them; another celebrates the use case of an agent that, given the requirements, builds for itself a team of specialised bots, each with its own model. It is the self-evolution Nous sells as its banner — and which, without brakes, risks becoming noise.

## Conclusion

The open question is no longer whether Hermes is powerful, but whether the power can hold up under the popularity. A store simplifies entry; a lean core keeps it in order. What remains to be seen is whether the ecosystem will stay readable as it grows.

---
*Verified sources: nousresearch.com e X @NousResearch (8 ottobre 2026); hermesbible.com/changelog e commit GitHub NousResearch/hermes-agent (9 ottobre 2026); api.github.com/repos/NousResearch/hermes-agent/releases/latest e github.com/NousResearch/hermes-agent/releases (8 ottobre 2026); hermes-agent.nousresearch.com/docs — installation, plugin-catalog (9 ottobre 2026); X @HermesWatcher e @junthekey (9 ottobre 2026).*

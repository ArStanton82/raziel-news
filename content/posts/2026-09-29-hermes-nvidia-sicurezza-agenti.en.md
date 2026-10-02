---
title: "Hermes and the agent perimeter: NVIDIA sets the rules, the models get there first"
date: 2026-09-29
draft: false
categories: ["Hermes", "AI"]
tags: ["Hermes Agent", "Nous Research", "NVIDIA", "OpenShell", "Claude Sonnet 5.5"]
summary: "NVIDIA launches its open platform for agent security and names Hermes among the supported runtimes: what actually changes."
url: "/en/2026/09/hermes-and-the-agent-perimeter-nvidia-sets-the-rules-the-models-get-there-first/"
---

In the last days of September the conversation about autonomous agents stopped being a question of capability and became one of containment. It is not a change of topic: it is a change of phase.

## A perimeter, not a promise

NVIDIA has presented the Open Agent Safety Platform, with more than a hundred declared partners. The architecture rests on two pieces: OpenShell, a kernel-level isolated runtime distributed under the Apache 2.0 licence, and Sentry, an out-of-band watchdog running on BlueField-4 that can quarantine an agent that steps outside its own boundaries in milliseconds. Hermes is not a passing guest: the NemoClaw page speaks explicitly of "run self-improving Hermes agents", combining Nous Research's skill-and-memory loop with OpenShell's runtime controls. The point is subtler than it looks: the mechanism that makes Hermes useful — learning and retaining — is treated as a load to be confined, not a virtue to be applauded.

## New models, old rules

On 24 September release v0.21.5 (v2026.9.24) brought Claude Opus 5.5 and GPT-6 into the catalogues. On 28 September Anthropic launched Claude Sonnet 5.5 and the Hermes community announced its availability in the runtime: the parent company has not yet published a dedicated note, so the datum should be taken for what it is, a community announcement consistent with the timing. The substance does not change: models reach clients before anyone has decided how to limit them.

## The desktop as identity

Hermes Desktop is customised profile by profile: chat and terminal fonts, themes importable from the VS Code Marketplace, window layout, all saved in the individual profile's config. The "Applies to" selector lets you change another profile's settings without switching applications. A research agent and a production agent can have two faces, two palettes and two different densities. It is aesthetics, but it is also the first time the boundary between agents becomes visible at a glance.

## Conclusion

The week says one simple thing: security is no longer an accessory to the product, it is the ground on which trust is played out. NVIDIA understood this and bought the attention of a hundred partners. Nous, for its part, made sure Hermes was inside the fence — not outside asking for permission. For anyone building agents, the question is no longer "what can it do", but "where is it allowed to go".

---
*Verified sources: NVIDIA Newsroom e GlobeNewswire, lancio Open Agent Safety Platform (28/09/2026); MarkTechPost (28/09/2026); pagina NVIDIA NemoClaw e docs.nvidia.com/nemoclaw (consultate 29/09/2026); GitHub NousResearch/hermes-agent, release v0.21.5 (24/09/2026); docs Hermes Agent "Hermes Desktop" (consultate 29/09/2026); Anthropic release notes e anthropic.com/claude/sonnet (28/09/2026).*
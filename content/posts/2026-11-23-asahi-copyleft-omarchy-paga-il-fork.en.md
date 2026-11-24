---
title: "Asahi goes copyleft, Omarchy pays for the fork: who controls the layer under the Mac"
date: 2026-11-23
draft: false
categories: ["Omarchy"]
tags: ["Asahi Linux", "Aurora Silicon", "Omacom Foundation", "copyleft", "GPLv2", "Apple Silicon", "drivers"]
summary: "Omarchy's foundation pays two maintainers of the Aurora fork while Asahi moves to copyleft: the fight for the layer under the Mac."
url: "/en/2026/11/asahi-goes-copyleft-omarchy-pays-for-the-fork/"
---

On 20 November the Omacom Foundation announced it is funding Aurora Silicon: hardware and tokens for those who work on it, and three months full-time for two maintainers, Dj and Ryan Murray, starting with the M3 and M4 series. Aurora is the project that keeps Linux alive on Apple-chip Macs at the level you do not see: kernel, graphics drivers, boot chain. Thirteen days earlier, on 7 November, Asahi Linux had announced that all its repositories move to GPLv2 or later. Read together, the two pieces of news are a snapshot of who is taking control of a layer that two years ago did not exist.

## The facts, with the dates

Asahi's progress report for Linux 7.3, signed on 7 November, is explicit: «our permissive licensing is no longer sustainable». Asahi was MIT by choice, so that the drivers could also be adopted by the BSDs; now it moves to strong copyleft. The m1n1 bootloader has already migrated, copyleft since 2.0.0, with earlier versions staying MIT. The kernel drivers were already GPL, because the kernel is GPL: the squeeze concerns the rest.

On 20 November the foundation answered with money: hardware for those doing reverse engineering, tokens for the models they use, three months of salary for two people. The post thanks Asahi explicitly and acknowledges that the Aurora tree — bootloader, kernel, installer — was born as a fork of Asahi's work. The same day also brought Beelink as a corporate patron with a hundred thousand dollars a year for three years, and a mini PC with Omarchy preinstalled: the total support declared by the foundation comes to about 24 million dollars, largely in tokens from AI labs rather than in cash.

## The licence is there for the give-back, not for the code

Asahi names no names, but the clues are all there: «several attempts to exploit our permissive licensing to hijack our work, with the stated goal of replacing the project and aggressively monetising Linux on Apple Silicon». In some cases, Calligeros writes, code for features still in development was taken straight from the developers' personal forks and published without attribution, or «lazily rewritten with the help of an LLM to hide its origin». The cited precedent is Wine, which moved from MIT to LGPL in 2002 for the same reasons.

And it should be said what a licence does not do: copyright protects the form, not the idea, whether a paraphrase by a model is a derivative work is an open question, and the GPL is only enforced with a lawsuit. Asahi's copyleft is more a statement of expectations than a remedy. Nobody has yet proved that it was precisely Omarchy or Aurora that took code without attributing it.

David Heinemeier Hansson's answer was short: GPLv2 changes nothing, the kernel was already GPL, the drivers are already available; «Asahi rejects upstreaming», he added, and Omarchy is MIT. The whole point is in that sentence.

## The fork that no longer talks upstream

Aurora Silicon's rulebook says it: «do not contact upstream projects», ever, for any reason — no bugs, no pull requests, no reports. The stated reason is that Aurora's approach to language models and decompilation differs from Asahi's, and that therefore anything born in Aurora must be considered «unusable» from the upstream point of view. It is not secrecy: it is contamination. Aurora only asks that the use of a model be declared in every pull request with an `Assisted-by:` line.

The paradox: two projects on the same hardware, with the same starting code, that have stopped exchanging bugs.

## What changes for those who use the machine

For anyone who wants Linux on a Mac the good news is concrete: the installation route without a USB stick and without a terminal has existed since early November, and now there is a foundation paying the people who make it possible.

The bad news is that knowledge about Apple hardware is splitting into two branches that have decided not to talk to each other, precisely while code can be rewritten with a model and its provenance hidden. Anyone who buys a Mac to put Linux on it is choosing a branch without knowing it, and neither one is safe: upstream there are years of volunteer reverse engineering, downstream a funded structure that depends on patronage and token allocations.

## The point

There is no villain in this story: there is a new model. Foundation plus agents plus paid fork buys speed, and puts it on a tree that has given up going back upstream. Who controls the layer under the Mac, from here on, is decided by whoever pays two salaries and whoever picks a licence — not by whoever writes the driver.

---
*Verified sources: omarchy.org/news/2026/11/omacom-foundation-to-sponsor-aurora-silicon/ (consulted on 23/11/2026: Aurora sponsorship, hardware, tokens, three months full-time for Dj and Ryan Murray, thanks to Asahi); omarchy.org/news/2026/11/beelink-joins-as-a-distinguished-corporate-patron/ (23/11/2026: 100,000 dollars a year for three years, Omarchy Edition mini PC, total support around 24 million); asahilinux.org/2026/11/progress-report-7-3/ (23/11/2026, signed by James Calligeros on 7/11/2026: move of all repositories to GPLv2+, quotes on the hijack attempts and the LLM rewrite, Wine precedent, m1n1 copyleft since 2.0.0); aurorasilicon.org/docs/policies/ (23/11/2026: ban on contacting upstream projects, Assisted-by line in pull requests); heise.de/en/news/Asahi-Linux-changes-license-to-stop-forks-from-taking-its-code-11519257.html (23/11/2026, 10/11/2026: legal picture of MIT versus GPLv2, open question of a derivative work produced by a model, DHH statement on X of 8/11/2026 «Asahi changing to GPLv2 changes nothing» and «thanks to agent acceleration, Asahi rejects upstreaming», no public proof against Omarchy or Aurora); omarchycentral.com (21 and 23/11/2026: reconstruction of the sponsorship and reference to Asahi's licence change); X, search «Omarchy» (23/11/2026: @tylenolburrito on 22/11 «20+ million dollars is actually absurd», @techmore_edu on 23/11 on the appeal to support the Aurora maintainers). Not verified: Asahi does not name Omarchy or Aurora in the report, so the attribution remains circumstantial.*

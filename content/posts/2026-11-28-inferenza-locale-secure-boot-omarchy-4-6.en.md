---
title: "Local inference and Secure Boot: Omarchy 4.6 redraws who controls the machine"
date: 2026-11-28
draft: false
categories: ["Omarchy", "AI"]
tags: ["Omarchy 4.6", "local models", "systemd-boot", "Secure Boot", "polkit", "Tailscale", "DGX Spark", "Chrome"]
url: "/en/2026/11/local-inference-and-secure-boot-omarchy-4-6/"
summary: "Release candidate 4.6 brings local models into the system and moves the boot: the machine changes hands, and says so."
---

On 27 November the 4.6 release candidate of Omarchy came out. The notes warn that it is not a final release and recommend a test machine or a snapshot to roll back to; then they state the thesis plainly: "Omarchy 4.6 brings open models home". It is the first round in which the system reorganises itself around the assumption that agents run on the machine, and in the same release it hands three pieces of the stack to somebody else: the model catalogue to the project, the boot signature to Microsoft, the browser to Google.

## Three changes, three dates

They were merged between 21 and 25 November, all already inside the RC. The first is a bar for local models, separate from the agents panel, which appears only on a machine able to run a model and splits RAM proportionally between system, model and free space, with labels such as "32 GB short". The second is the root password prompt: it shows the icon of the agent that asked, or the line "Authorize Claude to run …". Among the recognised agents are Claude, Codex, Copilot, Hermes. The third moves new UEFI installs from Limine to systemd-boot.

## The bar shows the price

`omarchy models use best` installs a catalogue model that fits the machine's measurements, inside a closed container with no network. The "no network" is in the notes and is stricter than usual: models can be shared over the tailnet, so the isolation applies to the process doing inference, not to the agent's reach. Two DGX Sparks connected by a cable can hold a model together; a `qwen3.8-27b-gufo` wants about 40 GiB on a 128 machine, a Flash Next about 100 with the full 256K window.

The bar makes visible that "which model" is decided by the hardware: inference leaves the provider's hands, but the catalogue is curated by others and the model that fits is a physical constraint.

## The padlock now has a name

The change to the polkit prompt is worth more than the others. The merge request says it with the sentence that is also its limit: "It's a hint, not proof: anything can call itself claude". If two requests contradict each other it shows no agent, if the lookup stalls the plain padlock comes back after a second. The PR was written with Claude Opus 5.5, DHH added two commits of his own before merging, and the day before the same shell had closed a hole in plugin manifests impersonating first-party ones.

An agent asking for root is the first thing that turns the machine into a machine administered by an agent, and the system starts admitting it instead of hiding it behind an anonymous padlock.

## The boot goes through Microsoft

Systemd-boot arrives for a declared reason: "Secure Boot on stock consumer hardware requires a Microsoft-signed shim", and shim review accepts GRUB and systemd-boot as second stage, not Limine. Secure Boot, though, is not switched on by this change: Omarchy's own shim, kernel lockdown and module signing are missing. Whoever has already installed gets no invitation, only `omarchy-boot-switch`, in reversible stages. Snapshots taken before the switch no longer boot. And speed is lost: 9.6 seconds against 4.6 on the installation, a measurement from the same PR, with the promise of dropping below 5 from RC2.

In the same release: Chrome instead of Chromium on new installs, Folio and Omaview instead of Nautilus and mpv, and some of these pieces written by `@omarchybot`, an agent writing the system on which agents will run.

## What changes for whoever uses the machine

The cut of zram to 8 GiB and of swappiness to 1, with the worst stalls down from 162 to 17 milliseconds, confirm that the desktop is already tuned to the model. DHH tells of having optimised Omarchy for a 4 GB RAM ceiling and of using Neon as the default driver "for everything to do with system work"; on X there are already those reporting twenty agent statistics collectors occupying ten threads out of twelve every quarter of an hour.

For whoever installs it: in this form it is not work-machine stuff. The RC is declaredly unstable and anyone with important snapshots should wait for the final, because the new boot makes them unbootable. Whoever instead wants to know whether their laptop can hold a local model now has the cheapest way to find out.

## The point

4.6 moves the inference chain home and at the same time shows the new handles: the project chooses the catalogue, Microsoft signs the boot, whoever asks permission draws the padlock icon. Who controls the machine is no longer an abstract question: since yesterday it is written in three points of the interface, and one of the three is a hint, not proof.

---
*Verified sources: github.com/omacom/omarchy/releases/tag/v4.6.0-rc1 (28/11/2026, published 27/11: local models, no-network containers, catalogue, DGX Spark, Chrome, zram, @omarchybot as PR author); github.com/omacom/omarchy/pull/20103 (28/11/2026: polkit prompt, agent list, "it's a hint, not proof: anything can call itself claude", PR written with Claude Opus 5.5); github.com/omacom/omarchy/pull/19667 (28/11/2026: Microsoft-signed shim, systemd-boot, Secure Boot not active, earlier snapshots unbootable, 9.6 s against 4.6 s); omarchycentral.com/news/omarchy-gives-local-ai-models-their-own-panel-with-a-memory-bar/ (28/11/2026: memory bar, "32 GB short", model measurements, "Omarchy runs every model with no network access"); omarchycentral.com/news/omarchy-4-6-rc1-is-out-with-local-models-for-your-agents-chrome-by-default-and-a-live-try-mode/ (27/11/2026: picture of the RC, Chrome instead of Chromium, no date for the final); aicrier.com/post/x4b590djl4k08s3gpgk4 (27/11/2026: isolation read as a defence against prompt injection, interpretation); X, @dhh timeline (28/11/2026: 4 GB ceiling, Neon as default driver for system work) and "Omarchy" search (28/11/2026: the twenty collectors saturating ten threads out of twelve).*

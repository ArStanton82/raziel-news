---
title: "Hermes Closes Out Nvidia's Keynote, and the Catalog Becomes the Product"
date: 2026-10-22
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes-agent", "nous-research", "nvidia", "gtc-berlin", "plugin", "meshy"]
summary: "Jensen Huang closes GTC Berlin with a Hermes Agent demo, while Nous ships v0.22.4 and the Meshy 3D plugin."
url: "/en/2026/10/hermes-closes-nvidias-keynote-and-the-catalog-becomes-the-product/"
---
There is a moment, in every technology, when it stops being something you show and becomes something you build on. For Hermes Agent that moment may have been the closing scene of Jensen Huang's keynote at GTC Berlin on October 21: not a product announcement, but a demonstration used as the finale, with Nvidia's chief explaining to the audience that the right way to build an agent is to ask an agent to build it.

## What happened on stage

Huang installed and configured a customized version of Hermes with a single prompt. Then the agent, running on RTX Spark, built a simulated training environment for Microduck, the $399 bipedal robot from Pollen Robotics, a Hugging Face subsidiary. Hermes designed an obstacle course with Nemotron, had the environment built by GPT-6 Astra using FreeCAD, the Omniverse libraries, Blender, Newton and Isaac Lab, trained thousands of simulated ducks in the cloud, and brought the validated policy back to RTX Spark for evaluation, before transferring it to the physical robot. At the end, four Microducks walked on stage and ran the commands.

The technical account is consistent across Nvidia's blog, Nous Research's retelling and live reports. It is worth noting the least spectacular part: the real work was not generating a video, but chaining different models, CAD tools, simulators and heterogeneous hardware. That is exactly what a harness is supposed to do.

## The plugin that matters more than the demo

The next day, Nous Research added the official Meshy plugin to the catalog: it installs by name, `hermes plugins install meshy`, requires the MESHY_API_KEY variable and Hermes >= 0.22.3. In pull request #142619, merged on October 21, the plugin sits in the official tier, tools category, with an MCP server, eighteen tools with declared cost and a spend limit of 200 credits. In Hermes Desktop, models appear in the chat, rigged characters animate live, and a gallery keeps the model and the prompt.

A 3D model generated inside a conversation is a small use case. But it is proof that the mechanism works: an external MCP server enters the catalog with disclosure, costs and limits, without the user writing a single line of configuration.

## Maintenance as a signal

Also on October 21 came v0.22.4, a patch with six fixes: the suggestion pills above the composer disappear, plugins without dependencies skip the empty consent step, WhatsApp re-pairs after logout, the approval-mode chip follows the active profile. Joining the catalog: bubblewrap, Singularity/Apptainer, mcp-serve, agent-importers with Cursor, inbox and workflow-record. Fourteen non-merge commits, 82 files, 13 PRs.

None of these lines will end up in a keynote. And that is the point: the difference between a demo and infrastructure is the tedium of maintenance, repeated every week. The open question is no longer what Hermes can do, but how many of the plugins entering the catalog will survive their second month.

---
*Verified sources: Nvidia blog, «GTC Berlin 2026: Live Updates», 21/10/2026; @NousResearch post about the demo (x.com/NousResearch/status/2113010017645244623), 21/10/2026; RuntimeWire, «Nous Research's Hermes agent orchestrates robot training in Jensen Huang's GTC demo», 21/10/2026; Classmethod, report on the GTC Berlin keynote, 21/10/2026; NousResearch/hermes-agent GitHub release v0.22.4, 21/10/2026; pull request #142619 «Meshy joins the plugin catalog as an official plugin», merged 21/10/2026. Annotated discrepancies: the report gave the plugin's minimum requirement as «>= 0.22.3» and it is confirmed by the PR; the pipeline description in the report was rewritten following Nvidia's blog, which distinguishes simulation in Isaac Sim, cloud training and evaluation on RTX Spark.*

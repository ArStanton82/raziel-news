---
title: "Hermes 0.22.2: the release that admits it is a corrected mistake"
date: 2026-10-17
draft: false
categories: ["Hermes", "AI"]
tags: ["Hermes Agent", "Nous Research", "open hardware", "MCP", "security"]
summary: "Nous ships 0.22.2 to repair 0.22.1, opens a page of hardware ideas and makes clear that Hermes does not buy placements."
url: "/en/2026/10/hermes-0-22-2-the-release-that-admits-it-is-a-corrected-mistake/"
---

There are weeks when a project is judged by the features it adds, and weeks when it is judged by how it talks about its own mistakes. In the Hermes ecosystem, the week just gone belongs to the second category.

## The patch that admits the error
On 15 October Nous Research published Hermes Agent v0.22.2, and the release notes are unusually blunt: "v0.22.1 was built from the wrong commit". The previous version had shipped unreleased gateway work, and the Microsoft Store app could get stuck on "Connecting". The 0.22.2, it reads, is the release that 0.22.1 should have been. The two declared fixes are concrete: the supervised gateway restarts after a reboot — Linux can hand an early PID to an unrelated process, mistaken for a live gateway, and Hermes now records the boot it started from — and long turns with local models survive on laptops, with stall timers ignoring the time the machine spent suspended. One known issue is declared rather than hidden: sessions started under gateway 0.22.1 cannot be deleted in 0.22.2. Those updating via CLI or installer use `hermes update`.

## Placements are not for sale
On 16 October Nous Research's official account published an editorial note: a post from an internal social account was satire, Hermes had not been selected for a list because "we don't do paid PR". The text also appears in the Announcements section of nousresearch.com. It is a small detail, but it says how a company chooses to build its reputation: with the product, not with placements.

## Hardware as a proving ground
Co-founder Teknium flagged a new IoT device based on Hermes and published a page with hundreds of project ideas for the meeting of agent and open hardware: battery-powered sensor nodes, Zigbee bridges, test benches, even an FPGA core. It is not a product catalogue but a catalogue of hypotheses: the agent as a layer that writes firmware, reads logs and orchestrates devices that never had a conversational interface.

## The risk that comes from the protocol
On 15 October the advisory for CVE-2026-59951 was made public, concerning the MCP Python SDK: Streamable HTTP servers in stateful mode — the default — were not reclaiming sessions. They never expired, a DELETE left the entry registered and the session count had no ceiling, so a client able to reach the endpoint could grow memory without limit until a restart. Affected versions run from 1.8.0 to 1.29.1 and from 2.0.0 to 2.1.1; the fix lands in 1.30.0 and 2.2.0, with `session_idle_timeout` and `max_sessions`. For anyone exposing tools over MCP, it is a note to read before opening the port.

Three different stories, the same lesson: maintenance is a form of credibility, and the ecosystem around an agent is worth as much as the care taken over its points of contact.

---
*Verified sources: GitHub NousResearch/hermes-agent, release v0.22.2 (15 October 2026); nousresearch.com, Announcements section (16 October 2026); teknium.io/hermes-devices (17 October 2026); Red Hat Customer Portal and Kodem Security, CVE-2026-59951 (15 October 2026).*

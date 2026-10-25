---
title: "Hermes Learns Not to Look Like a Bot, and Leaves the Password in the Snapshot"
date: 2026-10-25
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes-agent", "camofox", "browser", "security", "plugin"]
summary: "The camofox plugin gives Hermes a local, cloud-free Firefox with a faked fingerprint. The bill is paid in transparency."
url: "/en/2026/10/hermes-learns-not-to-look-like-a-bot-and-leaves-the-password-in-the-snapshot/"
---

Camofox is not Nous Research's browser: it is an official plugin from the Hermes catalogue that wraps Camoufox, a Firefox fork with fingerprint spoofing written in C++, behind a Node server running on the user's own machine. The distinction matters, because the post that spread the news spoke of a browser "of its own": the fork is not Nous's. What's actually there is more interesting. Hermes, which until now introduced itself to websites as an automated client, can now present itself as just another Firefox — and the way it does so says where the line between browsing and pretending to be someone else is moving.

## A Firefox that doesn't declare it is an agent

The architecture is deliberately modest. The plugin downloads and starts nothing: the server has to be launched by hand on `localhost:9377`, with Node or with the Docker image, and Hermes drives it over REST. No cloud dependency: traffic stays on the machine of whoever uses it. The plugin registers eleven tools and adds cookie import from a `cookies.txt` file, available only with an API key, capped at five megabytes and five hundred cookies.

By default every session gets a random identity, so logins and cookies do not survive a restart; whoever wants persistence turns it on, and then Camofox writes the profile to disk only at an explicit checkpoint or on a clean shutdown. Killing Node by force throws away any logins never saved.

## The bill is paid in transparency

A browser that hides its own identity, by definition, also hides it from the person who owns it. The plugin's documentation is unusually honest: Hermes's credential vault does not reach the Camofox tab, so credentials have to be typed into the browser. And Camoufox prints the value of every filled field, passwords included, without marking in the snapshot which field is a password field. The password thus ends up in the snapshot text and in the result of the browsing step, which is to say in the conversation history. The rest of the perimeter is sturdier: URLs containing secrets, cloud metadata endpoints and blocklisted domains are refused.

## Why it's needed, and who benefits

Anti-bot walls have turned automated browsing into a technical and political problem at once: an agent that reads a commercial site is treated as an intruder, and the simplest answer is to look like a user. It is an arms race in which neither side has an interest in declaring how far ahead the other is.

The context is release v0.22.5 of 23 October: about 81 pull requests merged since the previous tag, 231 non-merge commits across 804 files, thirty issues closed, with the curated notes postponed to 0.23.0.

The question is not whether an agent should look human. It is who pays the bill when it succeeds: the site receiving traffic indistinguishable from a person's, or the user who believed they had put their password in a vault and found it in a snapshot.

---
*Verified sources: camofox plugin page in the official Hermes Agent catalogue, hermes-agent.nousresearch.com/docs/plugins/camofox, consulted on 25/10/2026 (self-hosted Node server, Camoufox as a Firefox fork with C++ spoofing, eleven tools, CAMOFOX_URL on port 9377, cookie import with 5 MB and 500 cookie limits, no vault coverage on Camofox tabs, values of filled fields — passwords included — printed in snapshots, blocking of URLs with secrets and cloud metadata); code `tools/browser_camofox.py` in the NousResearch/hermes-agent repository, commit eb75627f (REST backend, default URL localhost:9377); GitHub, release v0.22.5, github.com/NousResearch/hermes-agent/releases, published on 23/10/2026 (81 PRs merged, 231 non-merge commits, 804 files, +35,212/−17,885, 30 issues closed, curated notes with v0.23.0). Discrepancies noted: Echo's report describes Camofox as "a browser of its own" released by Hermes and cites an "official Nous Research plugin"; the primary sources indicate an official plugin wrapping the camofox-browser server by jo-inc and the Camoufox fork, not a browser developed by Nous, and note that the code previously lived in the core. The technical description in @HermesWatcher's X post was not used as a source: the t.co link cannot be resolved from the raw data. @NousResearch's 25/10 notice about third-party projects using the Hermes name was excluded for lack of a second source.*

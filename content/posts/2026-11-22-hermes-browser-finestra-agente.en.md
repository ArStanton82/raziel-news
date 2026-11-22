---
title: "Hermes steps out of the chat: the browser becomes a window on the agent"
date: 2026-11-22
draft: false
categories: ["AI", "Hermes"]
tags: ["hermes", "browser extension", "plugin", "proactivity", "dashboard"]
summary: "A community plugin brings Hermes into the browser sidebar; meanwhile Teknium talks about proactivity with approval and a dashboard being retired."
url: "/en/2026/11/hermes-steps-out-of-the-chat-the-browser-becomes-a-window-on-the-agent/"
---

The way an agent enters our day matters as much as what it can do. For months Hermes lived in a terminal window or in a chat. This weekend's three pieces of news describe the same shift, from the inside towards the outside.

## The page as context

The most concrete piece is a browser extension signed by Jon Komet, a community plugin and not an official one from Nous Research: MIT licence, a side panel on Chromium and a sidebar on Firefox, public code on GitHub. The agent no longer receives a page pasted in by hand: it reads the one you are looking at, with headings, links, forms and selected text.

The limits are declared by the author. On Firefox control is reduced: the extension reads pages, opens addresses and manages tabs, but it cannot click or type. On Chromium browsers control is complete. The complementary plugin is also required on Hermes builds later than 24 October 2026, plus a gateway restart. It is not a chatbot inside the browser: it is a door onto the runtime you have already configured, with your models, tools and memory.

## Proactivity with the handbrake on

The second clue comes from replies by Teknium, co-founder of Nous Research, in a thread on 21 November: «there was no proactivity in Hermes, that would be the next step» and, shortly after, the hope that «asking for approval on some of these proactive attempts allows the user to curb the absurdities». These are conversational remarks, not an announcement, and the public changelog still shows no trace of such a feature.

The editorial point, however, stands: an agent that acts without asking is more useful and more dangerous in the same gesture. Moving consent into the flow, instead of entrusting it to an initial configuration, is the mature choice. Anyone who has used autonomous agents knows the problem is not refusal: it is misplaced initiative.

## The dashboard moves into the gateway

The third signal is technical and for now informal. Also on 22 November Teknium wrote, replying to two users, that «the dashboard is being retired». The changelog of 21 November shows the consistent direction: pull requests moving the old dashboard backend inside the gateway, with a dedicated system sheet for the migration. It is not a removal announced with a press release, but it is the end of a piece of architecture.

The implicit message: the interface is no longer a separate application to administer, but a surface of the gateway. Fewer components, fewer credentials to keep in sync, fewer ways to get it wrong.

## The boundary, not the feature

The temptation is to read it all as a list of features. It is more interesting to notice that browser, proactivity and dashboard converge on the same problem: where the agent ends and the user begins. An extension that reads the page, a permission requested before acting, a dashboard that stops being a world apart. None of the three is spectacular. Together they describe a product learning to sit at the edge of attention instead of at its centre.

---

*Verified sources: github.com/abundantbeing/hermes-browser-extension repository and the addons.mozilla.org listing (consulted on 22/11/2026, MIT licence, author Jon Komet, limits of Hermes Control on Firefox); hermesatlas.com/projects/abundantbeing/hermes-browser-extension (22/11/2026); @Teknium posts of 21-22/11/2026 on proactivity and the dashboard (informal statements, no entry in the changelog); hermesbible.com changelog of 21/11/2026 and gradually.ai/changelogs/hermes-agent (v0.23.3 of 20/11/2026). Annotated discrepancy: the report states that the official plugin catalogue could not be read in this run (`plugin-catalog.json` empty), so the plugin's «official» status is neither confirmed nor excluded; the @HermesWatcher post presents it as installable with `hermes plugins install`, while the README calls it a community plugin.*

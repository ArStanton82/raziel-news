---
title: "ChatGPT walks into Hermes's porch: identity becomes the interface"
date: 2026-09-29
draft: false
categories: ["Hermes", "AI"]
tags: ["Hermes Agent", "Nous Research", "OpenAI", "GPT-6.1 Sol", "plugins"]
summary: "OpenAI opens Sign in with ChatGPT to third-party apps and Hermes Agent is on the list: the user's plan becomes the agent's key."
url: "/en/2026/09/chatgpt-walks-into-hermes-porch-identity-becomes-the-interface/"
---

For years the yardstick of an autonomous agent's adoption was the model it managed to use. From 29 September the question that matters is a different one: with which identity it walks into the tools the user already pays for. OpenAI has extended "Sign in with ChatGPT" to a list of third-party applications, and Hermes Agent by Nous Research is on that list. Nous announced it as a partnership: sign in to Nous Portal with ChatGPT and use your plan inside Hermes, with visibility and controls in ChatGPT's settings.

## A plan instead of a key

The novelty is not the login itself — the beta has been live since 2 August, with Airtable, GitLab, HubSpot, Notion, Supabase and Vercel as the first partners — but what travels through it. A Plus or Pro user can authorise AI requests inside an external app without generating an API key, and those requests draw on their own plan, with a weekly cap per app. Access and consumption remain two distinct acts: logging in does not grant the plan, and granting the plan does not open conversations or memories. It is a technical detail that is also an architectural choice: identity becomes the point where permission is negotiated.

## The model arrives before the market

The same day OpenAI presented GPT-6.1 Sol: an update that approaches the capabilities of GPT-6 Astra on agentic coding and computer use, at a fifth of Astra's input and output price. Cache entry costs $0.10 per million tokens, $2 for standard input and $10 for output. In the following days an Ultrafast variant will also arrive, up to eight times faster in Codex. For anyone building agents, though, the number that weighs is not the price per token but the work carried through per dollar: a cheap model that stops halfway costs more than an expensive one that closes the file.

## The catalogue as a product

While the models update, what distinguishes a runtime is how easy it is to change your mind. AIHubMix has entered Hermes Agent's official plugin catalogue: a single key for a catalogue of OpenAI-compatible models, with the selector filtered down to those that genuinely know how to use tools. In the same hours, two minor but consistent signals come from the community: the first reconnaissance of memory plugins and the count of 200 pull requests merged in a single day. The real indicator, at this stage, is not a model's power but the speed with which the ecosystem around it absorbs the new arrivals.

The open question remains the hardest one: if the front door is an OpenAI account, how much sovereignty does the person building on top of that identity keep? The answer will come from the first case in which an app wants to leave the enclosure.

---
*Verified sources: OpenAI Help Center, «Sign in with ChatGPT» (aggiornato 29/09/2026); OpenAI, «Introducing GPT-6.1 Sol» (29/09/2026); Runtimewire, «OpenAI launches Login with ChatGPT and routes plan usage into third-party AI apps» (29/09/2026, elenco commerciale con Hermes Agent di Nous Research); Hermes Agent — Plugin Catalog, voce `aihubmix` (in catalogo dal 17/09/2026); X @NousResearch e @browser_use (post del 29/09/2026, citati come annunci di parte).*
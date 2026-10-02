---
title: "Game over: Hermes Agent and MiMo build a 3D videogame with no human input"
date: 2026-09-26
draft: false
categories: ["AI", "Hermes"]
tags: ["Hermes Agent", "MiMo", "autonomy", "AI agents", "videogames", "Nous Research"]
summary: "An AI agent built, tested, debugged and deployed a complete 3D videogame in full autonomy. Not a line of code written by a human. The record: 18 seconds, 10/10 coins, zero falls. Welcome to the era of autonomous agents."
url: "/en/2026/09/hermes-agent-and-mimo-build-a-3d-game-with-no-human-input/"
---

There is a video going around on X right now. It shows a 3D videogame — bright colours, platform mechanics, coins to collect, a timer running down. It looks like the classic project work of a game design student. Instead it is something very different: it was built entirely by an autonomous AI agent. No human being wrote a line of code. Nobody fixed a bug. Nobody pressed "deploy".

The author of the post, Luigi Marcon, threw a challenge at Hermes Agent paired with Xiaomi's MiMo-V2.5-Pro: "Build a complete 3D game autonomously." The agent accepted, and the result is a playable game with a documented record of 18 seconds, 10 coins out of 10, and zero falls. It is not a pre-recorded demo: you can play it now.

This is not a laboratory curiosity. It is a precise signal of where we are heading.

## What actually happened

Let us start with the concrete facts. Hermes Agent is an open-source AI agent developed by Nous Research, launched on 25 February 2026. In seven months it has passed 249,000 stars on GitHub and 52,000 forks, becoming one of the most followed repositories in the platform's history. It is not a chatbot, not a copilot: it is a persistent daemon living on a server, accumulating knowledge across sessions, writing its own reusable skills, and able to reach the user on more than 20 messaging platforms.

MiMo-V2.5-Pro is the model Xiaomi released in April 2026 under the MIT licence: 1.02 trillion total parameters (42 billion active), Mixture-of-Experts architecture, a context window of 1 million tokens. It was designed specifically for prolonged agentic workloads — exactly what is needed when an agent has to hold coherence across hundreds or thousands of tool calls.

The combination has already produced impressive results in the past: in a documented test, Hermes on MiMo-V2.5-Pro generated 301 Git commits, built complete APIs, integrated Stripe payments and produced more than 60 pages of production code — all for 70.12 dollars of inference cost, helped by a cache hit rate of 96%.

The 3D game is the latest example, but it is the most visually immediate. And, probably, the most disruptive in its implications.

## Beyond "vibe coding"

2026 has been described as the year software engineering moved from "vibe coding" — describing what you want in natural language and watching AI generate code — to something structurally different. According to Anthropic's "Agentic Coding Trends 2026" report, agents are evolving from experimental tools into production systems that ship real features to real customers. The key figure: 46% of all the code written by active developers in 2026 comes from AI, and the 50% threshold is expected by the end of the year.

But there is a fundamental difference between generating code on request and building something in complete autonomy. In the first case, the human is still at the centre: they set the specifications, assess the results, correct the course. In the second, the agent acts as a genuine autonomous professional: it plans, executes, verifies, corrects, deploys.

Marcon's game is a perfect example of that second category. The agent did not just write code: it tested the game, identified bugs, fixed them, and in the end put it online so others could play it. It acted as a small development team inside a single entity.

## The economics of agents: when autonomy becomes affordable

One of the most discussed aspects of MiMo-V2.5-Pro is its economics. With an input cost of 0.435 dollars per million tokens (and just 0.0036 on cache hits) and output at 0.87 dollars per million tokens, the model makes round-the-clock autonomous operation financially sustainable. Agentic workloads are structurally cache-friendly: the system prompt, the memory files and the skill documents are reused continuously, producing cache hit rates of 80-96% in real sessions.

This changes everything. It is not only a question of capability — it is a question of access. When an agent can work for days producing hundreds of commits at the cost of a dinner, the barrier to entry for complex automation collapses. You no longer need a team of ten people to build an MVP: you need an agent, a powerful model, and a clear description of what you want to achieve.

## What it means for the future

The question that naturally arises is: if an AI agent can build a 3D videogame on its own, what can it not do?

The answer, for now, is that autonomous agents excel at well-defined tasks with clear objectives and measurable success criteria. Building a platform game with coins, a timer and falling mechanics fits perfectly into that category. Designing the emotional experience of a game, balancing difficulty for a specific audience, or innovating at the level of game design — these are spheres where human intuition remains irreplaceable.

But the trajectory is clear. As Deloitte writes in its report on the future of software engineering, we are moving from a model in which engineers write code to one in which they orchestrate agents that write code. The human being defines the intent, the constraints and the strategic decisions; the agent executes, verifies and iterates. Engineering becomes "unbound": compositional, creative, autonomous.

Marcon's 3D game is a perfect demonstration of this principle. And the most interesting thing is that in a year, probably, we will not be surprised any more. It will be the norm.

## The game has only just begun

As we write, hundreds of autonomous agents are working on servers around the world: some writing code, some analysing data, some managing infrastructure. Many of them use Hermes Agent, many others use competing frameworks. Almost all share one characteristic: they are doing things that, until yesterday, required specialised human teams.

The 3D game built by Hermes Agent and MiMo is a playful reminder of a serious truth: the autonomy of AI agents is no longer a future promise. It is already here. It works. And it is accessible to anyone with a clear idea and the desire to explore what happens when you let the agent get on with it.

The record is 18 seconds, 10/10 coins, zero falls. Think you can do better? The challenge is open. But the real challenge — the one that concerns all of us — is understanding what we will build, together with our agents, when there is no longer a limit to what they can do on their own.

---

*Verified sources: X post by @LuigiMarcon28 (26 September 2026), official Hermes Agent documentation (Nous Research), MiMo-V2.5-Pro technical sheet (Xiaomi), "Agentic Coding Trends 2026" report (Anthropic), "The Future of Software Engineering" whitepaper (Deloitte), SaaSCity analysis on MiMo-V2.5-Pro.*

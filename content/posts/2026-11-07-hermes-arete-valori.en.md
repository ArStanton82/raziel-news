---
title: "A Model's Values Are One Fine-Tune Away"
date: 2026-11-07
draft: false
categories: ["AI", "Hermes"]
tags: ["Nous Research", "Arete-27B", "open weights", "alignment"]
summary: "Nous redesigns the values of Qwen3.8-27B: state-line answers fall from 22% to 0.9%. But who writes the rubric that measures the result?"
url: "/en/2026/11/hermes-arete-valori/"
---

Nous Research has published Arete-27B, a Qwen3.8-27B retrained to reduce the answers that adopt Beijing's official line on sensitive topics. It is not a new model: it is a demonstration. If the result holds, it says something uncomfortable about Chinese models as much as about ours: the layer of values in an open model is thin, and it can be redone in a few hours of compute.

## Fifty million tokens, no shortcuts

The method is deliberately modest: supervised fine-tuning, about 52.8 million tokens, 50,000 samples at 64,000 context, two epochs, 1,202 steps. No reinforcement learning, no preference optimization, no architectural change. The teacher is Inkling, an open model, chosen also to avoid the contractual constraints on "illicit distillation". Weights, evaluation prompts and training data are public.

## The number, and what it measures

The internal evaluation uses 803 prompts across seven categories: freedom of expression, state ideology, state versus market, education, privacy and surveillance, democracy, environment. The average fact score rises from 2.32 to 2.98 out of 5; the share of answers that adopt the official line falls from 22% to 0.9% with thinking off (0.6% with thinking on; the post's text rounds it to 1%). Zero-score answers drop from 359 to 216 out of 803. The sharpest jump is on freedom of expression: from 0.89 to 2.44, with propaganda from 60% to 1%. On capabilities it claims no gains: Hermes Bench scores 65.60% against 65.77% for the base model, a difference the lab dismisses as noise.

## Who judges, and with what yardstick

The reservation lies in the perimeter. The rubric is Nous's, the prompts are Nous's, the judge is a model (Grok 4.7) instructed by Nous, and no independent replication appears to exist. The metric measures conformity to a declared values policy, not the absence of a point of view: the lab itself writes as much. If the stratification is that shallow, the conclusion is symmetrical: no model is neutral, and an open model is one option among many, not an oracle. The possibility of realigning it makes it impossible to trust blindly whoever did.

## The power and the price of access

On the same day Nous is also working on the agent. Cofounder Teknium wrote on X that the in-app browser will be able to inherit cookies and passwords, with the user's consent, "in the next patch": a promise without a date, not an available feature. It means the assistant will browse with the sessions of whoever uses it. The two pieces sit well together: the more a model is aligned to the values of whoever trains it, the more capable it is of acting on their behalf. The question is not whether values can be changed, but who holds the key, and with what rubric.

Arete-27B is a good experiment and a bad talisman: it says that alignment is not a stable property of models, but a repeatable editorial choice. Whoever makes it should publish the yardstick, as Nous did; whoever reads it should remember that the yardstick is part of the work.

---
*Verified sources: Nous Research, "Introducing Arete-27B", 6 November 2026 (nousresearch.com/arete); NousResearch/Arete-27B model card on Hugging Face; AlphaSignal, 6 November 2026; @NousResearch post of 6 November 2026; @Teknium post of 7 November 2026 (picked up by Digg AI on 7 November 2026). Verification note: the report gives 0.9% and 1% as the same value; they are the figure with thinking off and the rounding used in the post's text.*

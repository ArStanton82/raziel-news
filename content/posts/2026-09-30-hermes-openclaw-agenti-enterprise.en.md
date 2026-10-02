---
title: "OpenClaw Enterprise and the trust agents still have to earn"
date: 2026-09-30
draft: false
categories: ["Hermes", "AI"]
tags: ["Hermes Agent", "OpenClaw", "autonomous agents", "OpenAI Dots", "security"]
summary: "OpenClaw Enterprise brings persistent agents into the enterprise, while Hermes and Dots reopen the question of trust."
url: "/en/2026/09/openclaw-enterprise-and-the-trust-agents-still-have-to-earn/"
---

On 29 September the OpenClaw Foundation presented OpenClaw Enterprise, an open-source control plane for persistent agents, developed with Red Hat and NVIDIA after OpenAI donated the project to the foundation. The announcement matters little to end users and a great deal to how organisations are preparing to govern software that acts on its own, for days, inside real infrastructure.

## A Kubernetes for agents

OpenClaw Enterprise is neither a model nor an assistant: it is the layer that sits above agents. Multi-tenancy, rigid security boundaries between trusted and untrusted workloads, granular permissions, sandboxes and tamper-proof auditing. The licence is MIT, the code is public, and it installs on your own infrastructure with Docker Compose for local development or Kubernetes for production. The repository itself describes it as "Kubernetes for agents". It stays free for organisations, and the documentation says so honestly: the real cost remains compute, models and operational management. It is a political move as much as a technical one, because it puts an open standard where proprietary platforms used to be.

## Hermes: trust is earned with evidence

On the Hermes side the scanning window picked up signals of a different nature. On one hand, harmless tips, such as the Settings - Advanced - Keep computer awake entry in Hermes Desktop, which the official documentation confirms and which keeps overnight jobs from being interrupted. On the other, a public call for a feature freeze, accusing the project of hundreds of bugs and more than twenty security issues, RCE included. The count, as it stands, is not verifiable. The substance, however, should not be dismissed: in 2026 real CVEs were published on Hermes Agent, from code execution via a malicious .git/config to a supply-chain flaw in the MCP catalogue, and an independent audit listed four critical and nine high-severity findings in the default configuration. This is not a collapse: it is the bill that every open-source agent with shell access eventually presents.

## Dots: permissions are not handed out for a demo

While OpenClaw was selling governance, OpenAI launched Dots, always-on agents based on GPT-6 Astra, each with its own computer in the cloud and more than four thousand connected apps. Reuters reports that the live demos stalled several times. One Hermes user put the crux well: an always-on agent does not get full permissions because it is convincing on stage; trust arrives when scope grows on evidence, not on enthusiasm.

## Conclusion

OpenClaw Enterprise, the Hermes case and the Dots launch say the same thing from three different angles: agents have become infrastructure, and infrastructure is judged on permissions, audits and CVEs, not on demos. The hard part is not making an agent act. It is deciding what it may do when nobody is watching.

---

*Verified sources: VentureBeat, "OpenClaw launches free enterprise control plane for persistent AI agents, backed by OpenAI, Red Hat and Nvidia" (consulted 30/09/2026); Forkast News, "OpenAI, Red Hat, and NVIDIA Back an Open-Source Agent Control Plane" (30/09/2026); OpenClaw Enterprise documentation, docs-enterprise.openclaw.org (30/09/2026); Hermes Agent documentation, "Hermes Desktop" (30/09/2026); GitHub NousResearch/hermes-agent, issue #7826 "Security Audit: 4 Critical, 9 High severity findings in default configuration" (30/09/2026); NVD, CVE-2026-71963 and cve.org, CVE-2026-82021 (30/09/2026); Reuters, "OpenAI takes on Meta with dots agent in autonomous AI push" (29/09/2026); OpenAI, "Introducing dots" (29/09/2026).*

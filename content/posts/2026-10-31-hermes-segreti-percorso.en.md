---
title: "The Secret Was in the Wrong Folder"
date: 2026-10-31
draft: false
categories: ["Hermes", "AI"]
tags: ["Hermes Agent", "security", "sandbox", "approvals", "cron"]
summary: "Four files moved up one level: the sandbox defends paths, not intentions, and a renamed folder is enough to read a secret."
url: "/en/2026/10/the-secret-was-in-the-wrong-folder/"
---

On 31 October, at 03:49 UTC, the Hermes Agent repository recorded the merge of pull request 146715. The title is about housekeeping: "move secret caches and Photon token to profile home root." Moving four files up one level does not look like news. The reasoning behind it, though, is the lesson.

## The defect was geometric

The sandbox does not hide secrets: it hides paths. On Windows the MXC mechanism, used by the OpenShell plugin, exposes a `deniedPaths` list that can protect only a file sitting directly in the home directory granted to the agent. If the file lives one level down — in `cache/` or in `runtime/` — the agent can rename the folder it writes to and read the hidden file at its new address. It was measured on MXC 1.0.0 and 1.0.1: this is not a theory.

Hence the fix, which is both simple and embarrassing: the plaintext Bitwarden cache (`bws_cache.json`), the encrypted one, the 1Password cache (`op_cache.json`) and the Photon sidecar record, which holds port and token, now live in the home root. The old copies are deleted without being read. The PR text adds a detail worth more than the rest: the 1Password cache was the only one no guard covered.

## Move a file, update five lists

A secret is protected only if every check knows its name. The same change touches the profile's credential path lists, the agent's read and write bans, the gateway's media filter, the dashboard Files API's hidden names and the `.gitignore` of the flat installation. Four files moved, five registers rewritten. The real cost of a security measure is not the measure: it is keeping the list of everyone who has to know about it in sync.

## Who decides when nobody is there

The same documentation surfaces the other half of the problem. Approvals for dangerous commands have three modes — `smart` by default, `manual`, `off` — and three keys governing contexts without a human: `cron_mode`, `single_query_mode`, `unattended_mode`. All three default to `deny`: if a scheduled job hits a destructive command, the command is blocked and the agent has to find another way.

It is the most interesting default in the system, because it does not protect the person at the keyboard. It protects the case where there is no keyboard.

One uncomfortable thought remains. The safety of an autonomous agent is not measured by how clever its risk assessment is, but by how short the list of paths it forgot to update happens to be. The day a cache ends up one level too low, the sandbox keeps working perfectly and protects nothing.

---
*Verified sources: NousResearch/hermes-agent pull request #146715, text and merge date 31 October 2026 (GitHub API); official Hermes Agent documentation, Security page (`approvals.mode`, `cron_mode` modes) and X Search, consulted on 31 October 2026.*

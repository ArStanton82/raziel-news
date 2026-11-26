---
title: "The cookie that shouldn't have existed: Hermes closes the 127.0.0.1 door"
date: 2026-11-26
draft: false
categories: ["Hermes", "AI"]
tags: ["Hermes", "security", "webapp", "loopback", "cookie"]
summary: "An overnight fix in the Hermes repository: on the loopback webapp, cookie logins are refused, because 127.0.0.1 doesn't isolate ports."
url: "/en/2026/11/the-cookie-that-shouldnt-have-existed/"
---

There is an idea almost all of us take for granted: if a service runs on 127.0.0.1, it is safe because it is "local only". The commit Nous Research published overnight on the Hermes Agent repository (3e33ec2a, 05:29 UTC) shows that idea has a precise hole in it, and that the hole wasn't in the agent's code but in a browser specification.

## What actually happens on localhost
RFC 6265, section 8.5, establishes that cookies are not isolated by port on 127.0.0.1. In practice: a cookie issued by a service listening on port 9119 is also sent by the browser to any other local service visited on a different port — a dev server, a test page, some other application's umpteenth panel. Had the Hermes webapp accepted a cookie login on loopback, whoever controlled one of those pages could have captured the cookie and replayed it against the REST APIs and against the host terminal ticket (`/api/webapp/socket-ticket?socket=host-terminal`), getting around the mechanism that keeps the session token out of the HTML.

## The choice: launch links only
The fix (PR #160226, which closes report #159500) takes the sharper road: on loopback the webapp stays "launch-link-only", meaning it is opened with `hermes webapp`. The `/login` page now explains this instead of showing a form; `/auth/password-login`, `/auth/login` and `/auth/callback` answer 403 without setting any cookie; `/api/auth/providers` returns an empty list. The pull request claims thirteen new regression tests and 319 passing tests across eighteen files.

## Why it is a lesson, not an incident
The dashboard documentation already says that no login is needed on loopback and that a non-loopback bind switches the auth gate on, failing closed when a provider is missing. The flaw didn't break that model: it created a credential that no middleware accepted but that the browser could have replayed elsewhere. The security of the local space isn't a permission granted once, it is an assumption to check every time a secret is issued.

Two practical details. The fix is on main but not in a tagged release: the latest stable is still v0.23.4 from 24 November, the most recent canary is from the 25th. And meanwhile the official plugin catalogue has promoted Mission Control, a read-only dashboard with token and cost metres, as a Desktop plugin: version 1.0.0, requires Hermes 0.21.6, updated fourteen days ago. It isn't a product novelty, it is a shop window: watching what an agent costs while it works remains, though, the most honest way to use it.

---
*Verified sources: commit 3e33ec2a and PR #160226 (NousResearch/hermes-agent, 25-26 November 2026); issue #159500; Hermes Web Dashboard documentation, authentication section and notes on `--insecure` and loopback bind (read on 26 November 2026); GitHub releases API, latest stable v0.23.4 of 24 November 2026; mission-control entry in the plugin catalogue on hermes-agent.nousresearch.com (26 November 2026).*

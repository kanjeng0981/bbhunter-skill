---
name: hunt-http-smuggling
description: Hunt HTTP request smuggling (CL.TE, TE.CL, H2.CL, H2.TE). Cause: front-end proxy and back-end server disagree on where one request ends and the next begins (Content-Length vs Transfer-Encoding header parsing inconsistency). CL.TE: front-end uses CL, back uses TE → smuggle by sending TE: chunked but with body that fits CL count. TE.CL: opposite. H2.CL: HTTP/2 downgrade, smuggle CL into HTTP/1.1 back-end. Detectiontools: Burp HTTP Request Smuggler extension, smuggler.py, h2csmuggler. Confirm: time-delay technique (smuggled GET with 30s timeout) — if front-end returns slow on next victim request, smuggling works. Validate: cache poisoning chain (smuggle request that gets cached for victim), credential theft (smuggle X-Forwarded-For override that captures next user's cookies), bypass auth (smuggled internal-path request). Real paid examples from major CDN deployments. Use when hunting H1 paid programs running CDN+origin stacks, when targeting load balancer / WAF bypass.
scope: web2
---
Hunt HTTP request smuggling (CL.TE, TE.CL, H2.CL, H2.TE). Cause: front-end proxy and back-end server disagree on where one request ends and the next begins (Content-Length vs Transfer-Encoding header parsing inconsistency). CL.TE: front-end uses CL, back uses TE → smuggle by sending TE: chunked but with body that fits CL count. TE.CL: opposite. H2.CL: HTTP/2 downgrade, smuggle CL into HTTP/1.1 back-end. Detectiontools: Burp HTTP Request Smuggler extension, smuggler.py, h2csmuggler. Confirm: time-delay technique (smuggled GET with 30s timeout) — if front-end returns slow on next victim request, smuggling works. Validate: cache poisoning chain (smuggle request that gets cached for victim), credential theft (smuggle X-Forwarded-For override that captures next user's cookies), bypass auth (smuggled internal-path request). Real paid examples from major CDN deployments. Use when hunting H1 paid programs running CDN+origin stacks, when targeting load balancer / WAF bypass.

- **HTTP smuggling without two-tier architecture** — smuggling requires a front-end proxy and back-end server that disagree on request boundaries. Single-tier apps are immune.
- **TE.CL vs CL.TE confusion** — these are opposite attacks. Fingerprint the specific disagreement before attempting.
- **Smuggling probe without confirmable side effect** — a 200 or 400 on a probe request doesn't confirm smuggling. Need a visible side effect (cache poison, request queue poisoning, response queue).
- **HTTP/2 downgrade smug
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-http-smuggling/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

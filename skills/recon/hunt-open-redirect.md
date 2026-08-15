---
name: hunt-open-redirect
description: Hunt Open Redirect — all types including low-impact, chained to OAuth token theft → ATO, phishing chains. URL parameter manipulation, JavaScript redirect, meta refresh, header injection. Use when hunting redirect bugs or building ATO chains.
scope: web2
---
Hunt Open Redirect — all types including low-impact, chained to OAuth token theft → ATO, phishing chains. URL parameter manipulation, JavaScript redirect, meta refresh, header injection. Use when hunting redirect bugs or building ATO chains.

Use when the target has any redirect parameter — ?url=, ?next=, ?redirect=, ?return=, ?redirect_uri=, or similar — on login/logout flows, OAuth authorization endpoints, language switchers, payment redirects, or any parameter that controls where the user is sent after an action. Open redirect alone is Low on most programs, but becomes Critical when chained to OAuth token theft (redirect_uri bypass) or SSRF escalation. Every OAuth authorization endpoint with a configurable redirect_uri is the highest-value target.

1. **Parameter whitelist without validation** — Developers maintain a list of redirect parameters (url, next, return) but only validate that the parameter *exists*, not its value.
2. **User-friendly redirect features** — Post-login redirect, logout redirect, and language-switching features all need to redirect to user-controlled destinations.
3. **Third-party OAuth/SAML libraries** — Many auth libraries allow configuring redirect_uri validation loosely (prefix match, suffix match, wildcard) that match attacker-controlled subdomains.
4. **SSO implementation shortcuts** — Developers configure redirect_uri to accept the current request Host header, enabling Host-header-based open redirects.
5. **Assume-JSON-bodies-are-safe** — POST
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-open-redirect/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

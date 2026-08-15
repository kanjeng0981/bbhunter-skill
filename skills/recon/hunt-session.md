---
name: hunt-session
description: Hunt Session Management vulnerabilities — session fixation (no regeneration on login), insufficient invalidation on logout / password-change / email-change, predictable or low-entropy session IDs, JWT-as-session with no exp/revocation, refresh-token rotation/reuse-detection gaps, OAuth/SSO session linkage, device-bound-session (DBSC) downgrade, and cookie attribute issues (Secure/HttpOnly/SameSite/__Host-). Validate with TWO real sessions (attacker A + victim B), body-diff every 200, and OOB confirmation for theft chains. Medium to Critical (fixation→admin hijack, no-invalidation→persistent ATO).
scope: web2
---
Hunt Session Management vulnerabilities — session fixation (no regeneration on login), insufficient invalidation on logout / password-change / email-change, predictable or low-entropy session IDs, JWT-as-session with no exp/revocation, refresh-token rotation/reuse-detection gaps, OAuth/SSO session linkage, device-bound-session (DBSC) downgrade, and cookie attribute issues (Secure/HttpOnly/SameSite/__Host-). Validate with TWO real sessions (attacker A + victim B), body-diff every 200, and OOB confirmation for theft chains. Medium to Critical (fixation→admin hijack, no-invalidation→persistent ATO).

- **Session fixation without pre-login session** — if the app issues a new session ID after login, fixation is not possible. Test pre/post-login session ID behavior.
- **Session ID in URL** — ?sessionid=xxx leaks via Referer header. Demonstrate Referer leakage to a third-party domain.
- **Missing HttpOnly without XSS** — HttpOnly missing is a defense-in-depth issue, not a vulnerability without demonstrated XSS.
- **Session timeout too long** — long session timeout is a policy issue, not a bug (unless combined with physical access or shared device scenario).

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-session/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

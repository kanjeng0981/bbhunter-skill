---
name: hunt-ato
description: Hunt account takeover taxonomy — 9 distinct paths to ATO, plus chains. Paths: (1) password reset flaws (host-header injection redirects token, predictable/numeric token, Referer leak, no-expiry/reuse), (2) email change without re-auth, (3) OAuth account-link CSRF, (4) MFA bypass (per hunt-mfa-bypass), (5) session fixation, (6) JWT manipulation (alg:none, RS256→HS256 key confusion, weak HMAC secret, kid injection), (7) password change without step-up (chain with login timing/length oracle), (8) social-recovery / security-question brute-force, (9) SSO subdomain takeover at OAuth redirect_uri. Chains: cookie theft + password oracle + no step-up = persistent ATO; lax redirect_uri = auth-code theft; dangling-CNAME takeover at redirect_uri = ATO. Validate: demonstrate real takeover of test account B from attacker A's session; OOB/Collaborator confirm blind token-leak steps. Use when hunting ATO chains, testing password reset / email change / MFA / OAuth / session / JWT, or chaining primitives toward Critical.
scope: web2
---
Hunt account takeover taxonomy — 9 distinct paths to ATO, plus chains. Paths: (1) password reset flaws (host-header injection redirects token, predictable/numeric token, Referer leak, no-expiry/reuse), (2) email change without re-auth, (3) OAuth account-link CSRF, (4) MFA bypass (per hunt-mfa-bypass), (5) session fixation, (6) JWT manipulation (alg:none, RS256→HS256 key confusion, weak HMAC secret, kid injection), (7) password change without step-up (chain with login timing/length oracle), (8) social-recovery / security-question brute-force, (9) SSO subdomain takeover at OAuth redirect_uri. Chains: cookie theft + password oracle + no step-up = persistent ATO; lax redirect_uri = auth-code theft; dangling-CNAME takeover at redirect_uri = ATO. Validate: demonstrate real takeover of test account B from attacker A's session; OOB/Collaborator confirm blind token-leak steps. Use when hunting ATO chains, testing password reset / email change / MFA / OAuth / session / JWT, or chaining primitives toward Critical.

- **Self-ATO is not ATO** — changing your own password, resetting your own account, or locking yourself out proves nothing. You MUST demonstrate takeover of a SECOND test account (victim B) from attacker A's session/IP.
- **Host-header injection without email confirmation** — the reflected header value appearing in a test response doesn't prove the reset link was poisoned. Read the actual email (use a Collaborator domain and a controlled victim B inbox).
- **Predictable token
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-ato/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

---
name: hunt-mfa-bypass
description: Hunt MFA / 2FA bypass — 7 distinct patterns. (1) MFA not enforced on sensitive endpoints (password change, email change accept without MFA challenge), (2) MFA-step skip via direct navigation to post-login URL, (3) MFA-token replay (same code accepted twice), (4) brute-force the 6-digit OTP without rate limit (10^6 attempts at server speed), (5) race condition on OTP validation, (6) recovery-code dump via /api/me, (7) backup factor downgrade (SMS factor with no rate limit). Plus the chain: cookie theft + password oracle + no step-up = ATO without MFA challenge. Detection: trace auth flow in Burp, find every state transition, check if MFA is middleware-gated vs per-endpoint, check OTP entropy and rate limit on OTP-validate. Validate: attacker session reaching post-MFA state. Use when hunting auth bypass, MFA flows, chaining primitives toward ATO.
scope: web2
---
Hunt MFA / 2FA bypass — 7 distinct patterns. (1) MFA not enforced on sensitive endpoints (password change, email change accept without MFA challenge), (2) MFA-step skip via direct navigation to post-login URL, (3) MFA-token replay (same code accepted twice), (4) brute-force the 6-digit OTP without rate limit (10^6 attempts at server speed), (5) race condition on OTP validation, (6) recovery-code dump via /api/me, (7) backup factor downgrade (SMS factor with no rate limit). Plus the chain: cookie theft + password oracle + no step-up = ATO without MFA challenge. Detection: trace auth flow in Burp, find every state transition, check if MFA is middleware-gated vs per-endpoint, check OTP entropy and rate limit on OTP-validate. Validate: attacker session reaching post-MFA state. Use when hunting auth bypass, MFA flows, chaining primitives toward ATO.

- **MFA bypass via direct URL access** — navigating to /dashboard after initial login (but before MFA) is the most common bypass. Test all post-login paths.
- **Response manipulation** — changing {"mfa_required":true} to false in the response is a bypass only if the server trusts client-side state.
- **MFA code reuse** — if the code can be reused within its validity window, document the window length and number of possible reuses.
- **Backup code brute-force** — backup codes are typically 8+ characters. Feasibility depends on rate limiting. Test rate limits before claiming exploitability.
- **MFA enrollment without re-authentication**
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-mfa-bypass/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

---
name: hunt-brute-force
description: Hunt Missing/Weak Rate Limiting — login brute force, OTP/2FA brute force (10^6 keyspace), password-reset-token brute, credential stuffing, username/email enumeration via error-string / status-code / timing differences, weak password policy, missing CAPTCHA, IP-based rate-limit bypass via X-Forwarded-For and friends, ReDoS. Distinguishes hard lockout vs soft IP-throttle vs CAPTCHA-injection vs silent shadow-throttling (avoids false-negative 'no rate limit' conclusions). Medium to Critical depending on what the brute reaches (OTP→ATO = Critical).
scope: web2
---
Hunt Missing/Weak Rate Limiting — login brute force, OTP/2FA brute force (10^6 keyspace), password-reset-token brute, credential stuffing, username/email enumeration via error-string / status-code / timing differences, weak password policy, missing CAPTCHA, IP-based rate-limit bypass via X-Forwarded-For and friends, ReDoS. Distinguishes hard lockout vs soft IP-throttle vs CAPTCHA-injection vs silent shadow-throttling (avoids false-negative 'no rate limit' conclusions). Medium to Critical depending on what the brute reaches (OTP→ATO = Critical).

- **Testing without rate-limit awareness** — brute-forcing without -rate and -t flags triggers account lockouts and IP bans. Always test with conservative settings first.
- **Single-account testing** — brute-forcing your own test account proves nothing. Need two accounts to demonstrate the attack works against a victim.
- **HTTP status code alone as oracle** — 200 vs 403 differential can be misleading. Always diff response bodies; some apps return 200 with different content for valid vs invalid credentials.
- **Response timing as sole evidence** — single-sample timing differentials are jitter. Need n>=10 interleaved trials per group with 2-sigma threshold.
- **Lockout policy not documented** — if the target has account lockout after N attempts, document it. Brute-force with lockout is high-risk and low-reward.
- **Token entropy claims without measurement** — claiming a token is predictable requires actual measurement (Burp Sequencer e
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-brute-force/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

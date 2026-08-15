---
name: hunt-oauth
description: Hunting skill for oauth vulnerabilities. Built from 19 public bug bounty reports. Use when hunting oauth on any target.
scope: web2
---
Hunting skill for oauth vulnerabilities. Built from 19 public bug bounty reports. Use when hunting oauth on any target.

1. **Weak redirect_uri validation** — developers whitelist by prefix (startsWith) rather than exact match, or whitelist an entire domain instead of specific paths. A sub-path open redirect on the same domain then becomes a full token theft primitive.

2. **Missing or unvalidated state parameter** — developers implement OAuth by following basic tutorials that omit CSRF protection, or validate state client-side only in JavaScript (easily bypassed).

3. **Nonce not validated post-exchange** — nonce is generated and sent in the request but never verified against the ID token after the code exchange, making replay attacks possible.

4. **Authentication step ordering not enforced server-side** — teams implement multi-step auth (signup → email verify → OAuth grant) but don't enforce the sequence server-side. The token endpoint doesn't check completion of prerequisite steps.

5. **Token/code in URL with outbound requests on callback page** — developers land users on a callback page with tokens in the query string, then that page fires analytics, social share, or CDN requests that leak the full URL via Referer header.

6. **Mobile deep link handlers trust all input URLs** — Android/iOS developers build webview wrappers for push notification flows without validating that the loaded URL belongs to their own domain.

7. **Misconfigured OAuth application registration**
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-oauth/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

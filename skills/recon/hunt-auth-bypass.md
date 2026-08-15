---
name: hunt-auth-bypass
description: Hunting skill for auth bypass vulnerabilities. Built from 12 public bug bounty reports across SAML XSW / parser-differential (GitHub Enterprise CVE-2025-25291/25292), SAML signature stripping (Uber, Rocket.Chat, samlify CVE-2025-47949), SAML domain enforcement bypass via control characters (HackerOne 2024), partner-portal cross-IdP assertion reuse (Slack), WordPress XMLRPC bypassing SSO (Uber), JWT alg-confusion HS256/RS256 (Jitsi), JWT signature-validation skip (Linktree, Newspack), and token-audience confusion (Argo CD CVE-2023-22482). Use when hunting auth bypass — see the Legacy-Protocol Matrix for branded-UI vs legacy-endpoint patterns.
scope: web2
---
Hunting skill for auth bypass vulnerabilities. Built from 12 public bug bounty reports across SAML XSW / parser-differential (GitHub Enterprise CVE-2025-25291/25292), SAML signature stripping (Uber, Rocket.Chat, samlify CVE-2025-47949), SAML domain enforcement bypass via control characters (HackerOne 2024), partner-portal cross-IdP assertion reuse (Slack), WordPress XMLRPC bypassing SSO (Uber), JWT alg-confusion HS256/RS256 (Jitsi), JWT signature-validation skip (Linktree, Newspack), and token-audience confusion (Argo CD CVE-2023-22482). Use when hunting auth bypass — see the Legacy-Protocol Matrix for branded-UI vs legacy-endpoint patterns.

1. **SSO bypasses local auth entirely at the UI layer, but not at the API layer** — developers disable the login form but forget that API endpoints (/xmlrpc.php, REST API, mobile API) have their own auth handlers that still accept native credentials.

2. **SAML signature validation is skipped or optional** — library defaults often don't enforce signature checking; developers use wantAssertionsSigned: false or fail to configure the IdP certificate correctly.

3. **Shared session infrastructure across different trust levels** — partner portals and admin portals reuse the same session cookie or JWT secret because they're built on the same internal framework, assuming access control at the application layer is sufficient.

4. **Trust inheritance in multi-tenant architectures** — a token issued in a lower-privilege context (partner, reseller)
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-auth-bypass/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

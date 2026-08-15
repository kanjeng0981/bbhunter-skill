---
name: hunt-misc
description: Hunting skill for misc vulnerabilities. Built from 225 public bug bounty reports. Use when hunting misc on any target.
scope: web2
---
Hunting skill for misc vulnerabilities. Built from 225 public bug bounty reports. Use when hunting misc on any target.

1. **Soft deletes without permission invalidation** — removing a user from an org marks them as removed but doesn't revoke active sessions or cached permission checks; subsequent API calls still pass old auth context

2. **Invitation acceptance without verification gate** — developers implement invitation flow optimistically (assume user who received email is legitimate) and skip re-verification when token is consumed by a different session

3. **Token scope checked at issuance, not at use** — PAT/OAuth scopes validated when token is created but individual API endpoint handlers don't re-check scope, trusting middleware that may have a gap

4. **Role-based access control checked at UI layer only** — frontend hides buttons for restricted roles but backend API endpoints don't enforce the same restriction; direct API calls bypass UI gating

5. **SAML XML parsing quirks** — signature covers only part of the document; XML canonicalization differences allow unsigned content to pass verification; namespace prefix attacks

6. **Config/URL fields trusted as internal** — integration URL fields (Sentry, webhooks) assumed to be set only by trusted admins; maintainer-level roles can modify them to exfiltrate tokens

7. **Ruby header injection via string interpolation** — developer builds HTTP response headers by string concatenation without sanitizing newlines; Rack 3 beh
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-misc/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

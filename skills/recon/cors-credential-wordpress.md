---
name: cors-credential-wordpress
description: Exploit WP CORS credential reflection for data theft.
scope: web2
---
Exploit WP CORS credential reflection for data theft.

- After wp-mass-recon flags a target with Access-Control-Allow-Credentials: true.
- Testing any WordPress site's REST API for cross-origin data access.
- Building attack chains: CORS → user enumeration → spear-phishing → ATO.
- Validating whether a CORS finding is exploitable (not just present).

- **Preflight blocking:** Some servers require OPTIONS preflight for CORS requests with custom headers. Test with both simple GET (no preflight) and credentialed fetch (triggers preflight).
- **SameSite cookies:** SameSite=Lax or SameSite=Strict cookies won't send cross-origin even with CORS. Check cookie attributes in browser.
- **WAF interference:** Cloudflare may strip Origin header or block cross-origin requests. Test from non-Cloudflare IP.
- **False positive: Access-Control-Allow-Origin: * without credentials** — this is public data, not a vulnerability. The key is Access-Control-Allow-Credentials: true.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/cors-credential-wordpress/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

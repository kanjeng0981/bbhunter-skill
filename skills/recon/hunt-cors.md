---
name: hunt-cors
description: Hunt CORS Misconfiguration — origin-reflection with credentials, null-origin trust, subdomain-regex bypass (unanchored vs unescaped-dot vs prefix-only), pre-flight (OPTIONS) gating bypass, postMessage origin checks. High only when an attacker-controlled origin can perform a CREDENTIALED cross-origin read of sensitive data and you have proven it in a browser. Use when testing API endpoints, SPAs, or any app emitting Access-Control-* headers.
scope: web2
---
Hunt CORS Misconfiguration — origin-reflection with credentials, null-origin trust, subdomain-regex bypass (unanchored vs unescaped-dot vs prefix-only), pre-flight (OPTIONS) gating bypass, postMessage origin checks. High only when an attacker-controlled origin can perform a CREDENTIALED cross-origin read of sensitive data and you have proven it in a browser. Use when testing API endpoints, SPAs, or any app emitting Access-Control-* headers.

- **ACAO:* without ACAC is safe** — Access-Control-Allow-Origin: * without Access-Control-Allow-Credentials: true is NOT exploitable. Stop here.
- **Testing only GET** — some endpoints only emit CORS on OPTIONS preflight. Always test both methods.
- **Single-origin probe** — testing only Origin: https://evil.com misses null-origin trust and subdomain-regex bypass patterns.
- **Auth-required endpoint false negatives** — 401/403 responses may still emit CORS headers. Test with and without auth cookies.
- **Subdomain regex: missing end-anchor** — ^https://.*\.target\.com without $ matches https://x.target.com.evil.com. Always test end-anchor bypass.
- **Preflight-only CORS** — some servers only validate Origin on OPTIONS. If GET bypasses, the preflight is the real gate.


---

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-cors/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

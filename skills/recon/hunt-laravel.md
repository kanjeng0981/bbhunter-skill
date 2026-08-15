---
name: hunt-laravel
description: Hunt Laravel specific vulnerabilities — Debug mode leakage (APP_DEBUG=true exposes full stack trace + env vars), Laravel Telescope/Horizon dashboard unauthorized access, Ignition RCE (CVE-2021-3129), Signed URL manipulation, Queue Worker abuse, mass assignment via Eloquent, deserialization via cookies, .env file exposure. Use when target runs Laravel (PHP) — detected via X-Powered-By, Laravel session cookies, or /storage/ paths.
scope: web2
---
Hunt Laravel specific vulnerabilities — Debug mode leakage (APP_DEBUG=true exposes full stack trace + env vars), Laravel Telescope/Horizon dashboard unauthorized access, Ignition RCE (CVE-2021-3129), Signed URL manipulation, Queue Worker abuse, mass assignment via Eloquent, deserialization via cookies, .env file exposure. Use when target runs Laravel (PHP) — detected via X-Powered-By, Laravel session cookies, or /storage/ paths.

- **APP_KEY exposure without exploit** — knowing the APP_KEY enables cookie decryption and signing. Demonstrate forged session cookie or decrypted data.
- **Debug mode without sensitive output** — APP_DEBUG=true showing stack traces is Low. Need credentials or secrets in the debug output.
- **.env exposure without database credentials** — exposed .env with only APP_NAME=... is informational. Need DB creds, API keys, or secrets.
- **Telescope/Horizon without auth** — these tools expose queue/cache/request data. Demonstrate access to sensitive data through them.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-laravel/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

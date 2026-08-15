---
name: visual-recon
description: Screenshot all live hosts for rapid visual triage and technology fingerprinting.
scope: web2
---
Screenshot all live hosts for rapid visual triage and technology fingerprinting.

- You have 100+ live subdomains and need to prioritize targets quickly.
- Manual browsing is too slow for bulk reconnaissance.
- Need to identify default install pages (WordPress setup, phpMyAdmin login, Jenkins dashboard).
- Want to compare visual fingerprints across subdomains (shared infrastructure).
- Target serves different content based on User-Agent or geolocation.

- **Large screenshot batches can overwhelm disk.** 500 screenshots at 1440x900 ≈ 300MB.
- **JS-heavy SPAs may render as blank.** Use headless mode with longer timeout.
- **Redirect chains produce screenshots of the redirect target.** This is correct — you want the final destination.
- **CAPTCHA pages waste screenshots.** Filter CAPTCHA hosts before screenshotting.
- **Timeout on slow servers.** --timeout 15 is usually sufficient; increase for slow connections.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/visual-recon/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

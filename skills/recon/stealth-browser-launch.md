---
name: stealth-browser-launch
description: Launch stealth Chromium with C++ fingerprint patches for anti-bot bypass.
scope: web2
---
Launch stealth Chromium with C++ fingerprint patches for anti-bot bypass.

- Target blocks curl/httpx/nuclei with Cloudflare, Akamai, DataDome, or Kasada.
- Need full browser JavaScript execution for form submission, login, or XSS testing.
- Target returns 403 on all unauthenticated requests even with proper headers.
- Need to access reCAPTCHA-protected endpoints without solving CAPTCHAs.
- Running automated recon behind residential proxies — stealth browser prevents IP+UA correlation.

- **Datacenter IPs get blocked regardless of browser fingerprint.** Always use residential proxies.
- **page.wait_for_timeout() leaks CDP traffic that reCAPTCHA detects.** Use time.sleep() instead.
- **Puppeteer sends more CDP traffic than Playwright.** Use Playwright for reCAPTCHA-heavy targets.
- **Missing fonts cause canvas hash mismatches on Kasada/Akamai.** Install the font packages listed in Phase 7.
- **--fingerprint-noise=false can cause ML-based detection on FingerprintJS.** Only disable noise when specifically blocked by it.
- **Headless mode can be detected even with C++ patches.** Use headed mode (headless=False) for maximum stealth on aggressive sites.
- **Binary auto-updates are cached ~24h.** Pin with browser_version= if you need reproducibility.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/stealth-browser-launch/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

---
name: wp-mass-recon
description: Batch WP recon: users, CORS, XMLRPC, leaks across domains.
scope: web2
---
Batch WP recon: users, CORS, XMLRPC, leaks across domains.

- You have an authorized target list from a bug bounty program, pentest engagement, or red team with signed RoE.
- Sector-wide recon within authorized scope.
- After subfinder/crt.sh produces a target list and you need to triage.
- You want maximum findings per minute with a parallelizable pipeline.

- **SPA catch-all false positives:** Single-page apps return 200 for every path. Always verify .env has DB_/APP_/_KEY/_SECRET patterns; .git/config has [core]; SQL files have CREATE TABLE/INSERT INTO. Skip bodies with <html or <script in first 100 chars.
- **Cloudflare/WAF blocking:** httpx may show tech as "Cloudflare" but WP is behind it. Try HTTP/1.0 for WP Engine-hosted sites: curl --max-time 30 --connect-timeout 10 -sk --http1.0 "https://TARGET/wp-json/..."
- **Rate limiting:** WP Engine and Hostinger throttle after ~50 requests. Use 2-4s jitter between requests. Chrome/125 UA has 0% block rate; curl/8.4 UA has 5% block rate; Python urllib has 15%.
- **WordPress on subpaths:** Check justified candidates such as /blog/ and
  /wp/ in addition to the root; secondary installations can have different
  versions and controls.
- **Non-standard XMLRPC paths:** Some hosts rename xmlrpc.php. Verify with system.listMethods (not just HTTP 200) — look for <string> tags in response XML.
- **Registration form false positives:** Many sites show login form on ?action=register without actually allowing registration. The v2 check requ
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/wp-mass-recon/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

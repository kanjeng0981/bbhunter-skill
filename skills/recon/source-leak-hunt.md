---
name: source-leak-hunt
description: Mass scan for exposed env files, backups, and git configs.
scope: web2
---
Mass scan for exposed env files, backups, and git configs.

- After skill_view(name='wp-mass-recon') confirms a target is alive.
- Broad scanning across a batch of domains.
- When probing for credential exposure that enables deeper access.
- Complementing skill_view(name='js-secrets-extraction') for client-side secrets.

- **SPA catch-all false positives over 70% of results without filtering.** Single-page apps return HTTP 200 with index.html for any path. Content verification is mandatory.
- **CloudFront/S3 error pages.** Some CDNs return 200 with an XML error body for missing files. Check content type and body.
- **Truncated content on large files.** error_log files can be 1.7MB+. Fetch in chunks or use curl -r 0-5000 for sampling.
- **git/HEAD false positive.** Some themes/setups have .git/HEAD returning 200 with a legitimate git hash. Verify .git/config first.
- **Parked/for-sale domains return HTTP 200 for every path.** Generic parking pages serve content for /.env, /.git/config, /info.php, etc. with no error handling — every path returns 200 with the same landing page. Detect these by checking if multiple unrelated paths return identical content (same body hash, same <title>, or same keyword like "for sale" or "parked"). Add early-exit: if /robots.txt and /.env both return 200 with near-identical HTML, mark domain as parked and skip further source-leak checks.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/source-leak-hunt/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

---
name: cms-detection
description: Identify CMS, frameworks, and server technology stacks on live hosts.
scope: web2
---
Identify CMS, frameworks, and server technology stacks on live hosts.

- You have a list of alive hosts and need to categorize them by technology.
- WordPress-specific tests produced false positives (the site uses Drupal).
- Need to identify which CMS version is running to match against known CVEs.
- A host returns generic 200 on all paths — technology detection tells you what it actually runs.
- Want to find sites running outdated versions of popular CMS platforms.

- **Generator meta tags can be spoofed.** A site claiming "WordPress 7.0" may be running 6.5. Cross-check with readme.html or RSS feed.
- **Technology detection is signature-based.** Custom themes may strip or modify signatures.
- **CDN caching may serve stale version info.** Force cache bypass with random query parameters.
- **whatweb can trigger WAF blocks on aggressive scans.** Use -a 2 (less aggressive) on protected targets.
- **Headless CMS (Strapi, Contentful) has no version file.** Look for API endpoints instead.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/cms-detection/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

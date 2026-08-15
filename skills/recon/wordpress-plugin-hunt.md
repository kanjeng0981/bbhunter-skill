---
name: wordpress-plugin-hunt
description: Hunt WP plugins via REST, exploit CVEs when version known.
scope: web2
---
Hunt WP plugins via REST, exploit CVEs when version known.

- WordPress confirmed on target (via wp-mass-recon).
- Running deep-invade Phase 3.
- You need an exploitation vector beyond CORS/XMLRPC.
- Target has a plugin-heavy WordPress site (e-commerce, page builder, forms).

- **REST namespace 200 ≠ plugin present.** Some themes and security plugins return 200 for all /wp-json/ paths. Verify response content has actual plugin data (JSON with id, name, or slug fields).
- **readme.txt blocked on many hosts.** WP Engine, Hostinger, and Cloudflare often block readme.txt at the CDN level. Fall back to REST namespaces or HTML source grep.
- **Custom plugin slugs.** Premium plugins may have custom directory names. gravityforms may be gravityforms-clientsite. Check HTML source for actual slugs via wp-content/plugins/ paths.
- **SliderRev v1 endpoints may return 404 on 6.x.** Slider Revolution renamed
  REST endpoints while the plugin remained active. Probe current non-v1 paths,
  including /wp-json/sliderrevolution/sliders/.
- **Plugin version comparison needs semantic versioning.** Bash string comparison (<) fails on 10.x vs 2.x. Use sort -V or python for complex comparisons.
- **Elementor 500 is only a lead.**
  /wp-json/elementor/v1/favorites is an information disclosure only when the
  response contains a stack trace, server paths, or other non-public details.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/wordpress-plugin-hunt/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

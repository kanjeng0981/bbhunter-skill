---
name: hunt-xss
description: Hunting skill for xss vulnerabilities. Built from 174 public bug bounty reports. Use when hunting xss on any target.
scope: web2
---
Hunting skill for xss vulnerabilities. Built from 174 public bug bounty reports. Use when hunting xss on any target.

Use when the target has any endpoint where user input is reflected in HTML output, processed by a JavaScript framework, or stored for later display. XSS is the foundational client-side vulnerability class — it enables session hijacking, data theft, phishing, and account takeover. Every form, search field, URL parameter, file upload, and user-controlled field is a candidate. Highest-value targets: admin panels, OAuth sign-in pages, markdown/wiki renderers, email templates, file upload endpoints (SVG/HTML), and help/documentation sites with looser security posture.

1. **Trusting html_safe in Rails** — Developers mark strings as safe after partial sanitization, or chain .html_safe on user-supplied data without full sanitization.

2. **Allowlist sanitizers with dangerous tag combinations** — Allowing style alongside math or svg creates mXSS (mutation XSS) opportunities even when individual tags seem harmless.

3. **Third-party rendering pipelines** — Markdown-to-HTML pipelines (Banzai, Kramdown, Kroki) introduce XSS when diagram/rendering engines aren't sandboxed and output isn't re-sanitized.

4. **Reflecting URL parameters without encoding** — UTM params, redirect URLs, and search terms are reflected in page HTML or JS without proper HTML-encoding, especially on marketing/help pages that are treated as lower-security.

5. **SVG treated as non-script content** —
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-xss/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

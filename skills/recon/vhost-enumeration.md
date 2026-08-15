---
name: vhost-enumeration
description: Discover hidden virtual hosts via Host header fuzzing and SSL certificate parsing.
scope: web2
---
Discover hidden virtual hosts via Host header fuzzing and SSL certificate parsing.

- You have a list of target IPs from skill_view(name='origin-ip-discovery') or skill_view(name='port-service-discovery').
- A server returns default/blank pages for unknown Host headers.
- Subdomain enumeration may have missed internal-only hostnames.
- SSL certificates on an IP list multiple domain names in the SAN field.
- You need to map internal services behind a reverse proxy.

- **Wildcard DNS returns valid HTTP for any Host header.** Use auto-calibration (-ac) and verify manually.
- **The default virtual host may return a generic page for unknown names.** Calibrate -fs with a known-nonexistent hostname.
- **SSL/TLS prevents content comparison without SNI.** Use openssl s_client -servername for each hostname.
- **Some servers accept any Host header.** This produces false positives — verify each finding with manual curl.
- **Internal-only services may not be accessible from your IP.** They may require internal network access.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/vhost-enumeration/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

---
name: origin-ip-discovery
description: Discover origin IPs behind CDN/WAF via favicon hash, DNS history, and SSL certs.
scope: web2
---
Discover origin IPs behind CDN/WAF via favicon hash, DNS history, and SSL certs.

- Target is behind Cloudflare/Akamai and returns 403 or CAPTCHA challenges on all requests.
- You need direct access to the origin to bypass WAF rules.
- Subdomain enumeration reveals internal/staging hosts on non-CDN IPs.
- The target uses a single favicon across all infrastructure.
- SSL certificates share the same organization name across IPs.

- **Cloudflare may block your IP on repeated scans.** Rotate user-agents and proxies.
- **Shodan queries require an API key.** Free tier is rate-limited.
- **The origin may also be behind firewall rules.** Even if you find the IP, it may only accept traffic from Cloudflare's IP ranges.
- **Google Analytics IDs are shared across unrelated sites.** Verify by favicon or content match before claiming a finding.
- **Non-CDN IPs from subdomains may be load balancers,** not the actual web server origin. Probe with Host header to confirm.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/origin-ip-discovery/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

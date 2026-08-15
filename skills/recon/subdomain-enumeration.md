---
name: subdomain-enumeration
description: Map subdomains via crt.sh and subfinder at recon kickoff.
scope: web2
---
Map subdomains via crt.sh and subfinder at recon kickoff.

- Starting recon on any target domain.
- Production site is well-secured — find softer entry points.
- After skill_view(name='wp-mass-recon') — enumerate subdomains for each WordPress target.
- Building a complete asset inventory for a target organization.

- **crt.sh rate limiting.** crt.sh may return empty JSON if rate-limited. Use delays or query the PostgreSQL dump directly.
- **subfinder requires API keys.** Some sources (VirusTotal, Shodan) require API keys in ~/.config/subfinder/provider-config.yaml. Without them, results are limited.
- **Wildcard DNS.** If *.example.com resolves to the same IP, all subdomains will appear "live" in httpx. Check for wildcard by resolving a random string: dig RANDOMSTRING.example.com.
- **Cloudflare proxying.** Subdomains behind Cloudflare will show Cloudflare IPs, not origin IPs. Use SecurityTrails or DNSDumpster for historical DNS records.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/subdomain-enumeration/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

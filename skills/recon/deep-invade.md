---
name: deep-invade
description: Deep pentest WP: SSRF, plugin CVE, JS mine, port scan chain.
scope: web2
---
Deep pentest WP: SSRF, plugin CVE, JS mine, port scan chain.

- wp-mass-recon scored a target >= 6 (CORS confirmed, XMLRPC open, source leaks found).
- You are assigned a single high-value target for deep assessment.
- After surface recon, you need to find the chain that leads to RCE or data breach.
- Multiple independent signals justify a deeper, target-specific follow-up.

- **SSRF faultCode 0 is NOT proof of reachability.** Some servers return 0 for unreachable hosts. Always confirm with your own collaborator callback first.
- **Error logs can be multi-GB.** Use curl -r 0-100000 to fetch only the first 100KB for sampling.
- **Plugin namespace HTTP 200 doesn't mean the plugin is present.** Some themes/setups return 200 for all /wp-json/ paths. Check response body for actual plugin data.
- **nmap requires root for SYN scan.** Use -sT (TCP connect) if running as non-root inside the container.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/deep-invade/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

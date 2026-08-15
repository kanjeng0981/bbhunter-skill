---
name: asn-infrastructure-mapping
description: Map organization IP infrastructure via ASN, CIDR, TLD expansion, and reverse DNS.
scope: web2
---
Map organization IP infrastructure via ASN, CIDR, TLD expansion, and reverse DNS.

- You have a target domain and want to discover EVERY IP owned by the organization.
- Passive subdomain enumeration found only a few hosts — the rest may be on sibling TLDs or different IP ranges.
- The target has a known ASN that can be expanded to full CIDR blocks.
- Services on non-standard ports are invisible to web-only recon.
- Acquired subsidiaries or international domains may sit on different ASNs with weaker security.

- **CIDR ranges can be massive (e.g., AWS).** Only scan IP ranges confirmed to belong to the target, not the entire hosting provider.
- **RADB whois data may be stale.** Cross-reference with multiple sources (bgp.he.net, Censys, Shodan).
- **TLD expansion is noisy.** Only .com/.org/.net/.io/.dev usually produce useful results.
- **Reverse DNS may reveal internal hostnames.** Handle with care in external recon — these leaks are findings themselves.
- **Sub-organization discovery can lead to out-of-scope targets.** Always verify the relationship before scanning.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/asn-infrastructure-mapping/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

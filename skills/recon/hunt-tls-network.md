---
name: hunt-tls-network
description: Hunt TLS/SSL and DNS misconfigurations — missing HSTS (downgrade attack), weak cipher suites, expired/invalid certificates, mTLS bypass, missing SPF/DKIM/DMARC (email spoofing), DNS Zone Transfer (AXFR), dangling CNAME subdomain takeover, CAA records. Most of these are Info/Low on their own — this skill is opinionated about which findings actually pay (spoofable DMARC with delivered-to-inbox proof, AXFR returning internal hosts, dangling-CNAME takeover) versus which get rejected as best-practice noise (missing CAA, missing HSTS with no MitM position). Use during recon to find infrastructure weaknesses, and to TRIAGE them honestly before reporting.
scope: web2
---
Hunt TLS/SSL and DNS misconfigurations — missing HSTS (downgrade attack), weak cipher suites, expired/invalid certificates, mTLS bypass, missing SPF/DKIM/DMARC (email spoofing), DNS Zone Transfer (AXFR), dangling CNAME subdomain takeover, CAA records. Most of these are Info/Low on their own — this skill is opinionated about which findings actually pay (spoofable DMARC with delivered-to-inbox proof, AXFR returning internal hosts, dangling-CNAME takeover) versus which get rejected as best-practice noise (missing CAA, missing HSTS with no MitM position). Use during recon to find infrastructure weaknesses, and to TRIAGE them honestly before reporting.

- **TLS version without exploit** — TLS 1.0/1.1 support is a configuration finding, not a vulnerability (unless paired with a specific downgrade attack).
- **Weak cipher without exploit** — RC4, 3DES, etc. are weak but exploitation requires active MITM. Document the attack scenario.
- **Self-signed certificate** — self-signed certs are common on internal services. On public services, this is a phishing risk (Low-Medium).
- **Certificate transparency log monitoring** — finding subdomains via CT logs is recon, not a vulnerability. The finding is what those subdomains expose.
- **Heartbleed/POODLE test** — these legacy TLS vulnerabilities are extremely rare in 2024+. Test but don't spend excessive time.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-tls-network/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

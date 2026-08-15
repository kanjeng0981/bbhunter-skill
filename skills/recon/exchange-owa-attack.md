---
name: exchange-owa-attack
description: Exchange/OWA NTLM AD leak, spray attack when mail subdomain.
scope: web2
---
Exchange/OWA NTLM AD leak, spray attack when mail subdomain.

- Target has owa., mail., webmail., exchange., or autodiscover. subdomains.
- crt.sh reveals Exchange-related SAN names (mail.domain.com, autodiscover.domain.com).
- Port 443 returns NTLM WWW-Authenticate: Negotiate or WWW-Authenticate: NTLM.
- After subdomain-enumeration discovers mail-related hosts.
- After port-service-discovery finds HTTPS on port 443 with Exchange fingerprints.

- **NTLM relay requires specific network position.** Unless you control a machine the Exchange server can reach, NTLM relay is not exploitable remotely.
- **Modern Exchange (Exchange Online, 2019+) blocks Basic Auth by default.** Test with Modern Auth (OAuth2) if Basic is blocked.
- **Account lockout policies vary.** Test with a single known-bad password before spraying.
- **ADFS is NOT Exchange.** ADFS is a separate service with its own attack surface (SAML, WS-Trust).

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/exchange-owa-attack/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

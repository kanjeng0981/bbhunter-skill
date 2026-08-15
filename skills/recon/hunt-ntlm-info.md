---
name: hunt-ntlm-info
description: Hunt NTLM/Negotiate information disclosure on internet-reachable IIS/SharePoint/Exchange. Anonymous NTLM Type-2 challenge capture leaks NetBIOS domain, internal DNS forest, computer name, AD timestamp via AV_PAIRS structure. Default Windows-installer hostnames (WIN-XXXXXXXXXXX pattern) signal lazy provisioning. Use when target advertises `WWW-Authenticate: NTLM` or `Negotiate` headers anonymously.
scope: web2
---
Hunt NTLM/Negotiate information disclosure on internet-reachable IIS/SharePoint/Exchange. Anonymous NTLM Type-2 challenge capture leaks NetBIOS domain, internal DNS forest, computer name, AD timestamp via AV_PAIRS structure. Default Windows-installer hostnames (WIN-XXXXXXXXXXX pattern) signal lazy provisioning. Use when target advertises `WWW-Authenticate: NTLM` or `Negotiate` headers anonymously.

1. **Dual-auth IIS bindings on the public zone.** Administrators leave NTLM enabled on the public-facing IIS site even when Forms auth is the intended entry point. Internal users get SSO; external attackers get the AD topology leak.

2. **Default IIS Application Pool identity left as ApplicationPoolIdentity.** Combined with default hostname, signals provisioning never went past first-boot.

3. **Server never renamed from Windows-installer-generated hostname.** Microsoft's default WIN-XXXXXXXXXXX 11-character pattern is the immediate tell. Sometimes also WORKGROUP\WIN-... in older boxes.

4. **Sub-domain joined to corporate forest without zone-isolation.** European-integrator case: a a European importer's SharePoint test environment is a child domain inside a corporate global AD, disclosed via NTLM DNS Tree Name. The customer probably intends customer.parent-corp.example to be operationally separate but the NTLM Type-2 reveals the forest membership to anyone who probes.

5. **IIS Extended Protection NOT enabled.** When <system.webServer><security><authentication><windowsAuthenticati
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-ntlm-info/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

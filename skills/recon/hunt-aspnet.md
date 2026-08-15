---
name: hunt-aspnet
description: Hunt ASP.NET-specific surface — ViewState deserialization (signed-only vs encrypted), machineKey recovery, dual-parser MAC-bypass anti-pattern, request-validator bypass, trace.axd/elmah.axd disclosure, load-balanced ViewState cross-node failures, SafeControl enumeration via reflection, customErrors mode=Off stack-trace leaks, classic Webforms .aspx/.asmx/.svc surface. Built for ASP.NET Webforms + WCF + SharePoint farms.
scope: web2
---
Hunt ASP.NET-specific surface — ViewState deserialization (signed-only vs encrypted), machineKey recovery, dual-parser MAC-bypass anti-pattern, request-validator bypass, trace.axd/elmah.axd disclosure, load-balanced ViewState cross-node failures, SafeControl enumeration via reflection, customErrors mode=Off stack-trace leaks, classic Webforms .aspx/.asmx/.svc surface. Built for ASP.NET Webforms + WCF + SharePoint farms.

1. **viewStateEncryption="Auto" defaults to signed-only on pages without sensitive ViewState data.** Many SharePoint pages are configured this way. When __VIEWSTATEENCRYPTED is empty, ViewState is signed-only — recovery of validationKey alone enables forgery.

2. **<machineKey> AutoGenerate in a Web Farm.** Each WFE generates a different key on first boot; ViewState issued by one WFE fails MAC validation on another. Operationally produces 500s; security-wise broadcasts the topology (the error message names the cluster).

3. **<customErrors mode="Off"> left from development.** Stack traces with full method names, file paths, version banners exposed to anonymous internet users.

4. **trace.axd / elmah.axd left enabled in production.** Often forgotten in <system.web><trace enabled="true"> blocks.

5. **Forgotten WCF .svc admin endpoints.** Built for internal admin tooling, never disabled when the main app went to internet exposure.

6. **Dual-parser anti-pattern: ObjectStateFormatter (legacy) vs LosFormatter (modern) deserialize in different orders relative to M
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-aspnet/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

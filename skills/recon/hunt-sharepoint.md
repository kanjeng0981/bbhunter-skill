---
name: hunt-sharepoint
description: Hunt Microsoft SharePoint Server (2013/2016/2019/Subscription Edition) on-prem farms — anonymous endpoint enumeration, version disclosure, legacy SOAP login bypass (Authentication.asmx), ToolShell precondition chain (CVE-2025-53770), SafeControl reflection enumeration via Picker.aspx, NTLM Type-2 AD topology disclosure, custom-branding module discovery, EoL farm permanent-CVE-window exploitation, FormDigest anonymous issuance, file-extension blocklist NOT-an-oracle pattern, custom-zone Forms auth bridging on-prem AD. Use when target has SharePoint headers (SPRequestGuid, X-MS-InvokeApp, X-SharePointHealthScore, MicrosoftSharePointTeamServices) or paths (/_layouts/15/, /_vti_bin/, /_api/, /_catalogs/).
scope: web2
---
Hunt Microsoft SharePoint Server (2013/2016/2019/Subscription Edition) on-prem farms — anonymous endpoint enumeration, version disclosure, legacy SOAP login bypass (Authentication.asmx), ToolShell precondition chain (CVE-2025-53770), SafeControl reflection enumeration via Picker.aspx, NTLM Type-2 AD topology disclosure, custom-branding module discovery, EoL farm permanent-CVE-window exploitation, FormDigest anonymous issuance, file-extension blocklist NOT-an-oracle pattern, custom-zone Forms auth bridging on-prem AD. Use when target has SharePoint headers (SPRequestGuid, X-MS-InvokeApp, X-SharePointHealthScore, MicrosoftSharePointTeamServices) or paths (/_layouts/15/, /_vti_bin/, /_api/, /_catalogs/).

1. **/_vti_bin/Authentication.asmx left enabled on the public-zone IIS binding.** SharePoint admins enable Forms auth on a custom login UI and don't realise the legacy SOAP Login endpoint is independently reachable.

2. **viewStateEncryption="Auto" on layouts pages.** SharePoint's default ViewState mode signs-only for pages without sensitive form fields. Pages like ToolPane.aspx have __VIEWSTATEENCRYPTED="" — exploitable if machineKey leaks.

3. **/_api/contextinfo POST accessible anonymously.** SharePoint Online and SPE 2024-07+ require auth on contextinfo. Earlier versions and most SP2013 farms allow anonymous POST → FormDigest token returned with 1800s validity. This is the second ToolShell precondition.

4. **NTLM enabled on public-zone IIS binding.** Default dual-auth (For
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-sharepoint/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

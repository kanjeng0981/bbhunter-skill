---
name: zimbra-attack
description: Zimbra SOAP user enum, CVE-2022-37042, SSRF when webmail.
scope: web2
---
Zimbra SOAP user enum, CVE-2022-37042, SSRF when webmail.

- Target has webmail., mail., or zimbra. subdomains.
- Redirect to /zimbra/ path on mail server.
- Server header or page title contains "Zimbra".
- After subdomain-enumeration discovers webmail hosts.
- Government, university, or enterprise targets (Zimbra is common in these sectors).

- **SOAP user enumeration is noisy.** Each request generates a login failure in Zimbra audit logs.
- **UploadServlet may be blocked at nginx.** If Zimbra is behind a reverse proxy, path traversal may be blocked even if the servlet is active.
- **Proxy SSRF requires authentication in newer versions.** Pre-8.8.15 it was accessible without auth.
- **Zimbra Admin on 7071 is internal by default.** Only exposed if misconfigured or port-forwarded.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/zimbra-attack/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

---
name: hunt-ldap
description: Hunt LDAP Injection and XPath Injection — authentication bypass, blind char-by-char attribute exfiltration, AD user/group enumeration, XML-store XPath bypass. Covers the LDAP special-character set (* ( ) \\ NUL /), search-filter-context vs DN-injection, parenthesis-balancing, AND/OR filter logic, and {SSHA}/{CRYPT} userPassword exfil on non-AD directories. Use when target uses LDAP/AD authentication, corporate SSO with a directory backend, an address-book/people-search API, or XML-based data stores queried with XPath.
scope: web2
---
Hunt LDAP Injection and XPath Injection — authentication bypass, blind char-by-char attribute exfiltration, AD user/group enumeration, XML-store XPath bypass. Covers the LDAP special-character set (* ( ) \\ NUL /), search-filter-context vs DN-injection, parenthesis-balancing, AND/OR filter logic, and {SSHA}/{CRYPT} userPassword exfil on non-AD directories. Use when target uses LDAP/AD authentication, corporate SSO with a directory backend, an address-book/people-search API, or XML-based data stores queried with XPath.

- **Anonymous LDAP bind without sensitive attributes** — anonymous bind returning public directory info is normal. Need PII, credentials, or membership data.
- **LDAP injection without authentication bypass** — blind LDAP injection that only returns true/false is harder to exploit. Need data exfiltration or auth bypass.
- **LDAPS not enforced but on internal network** — plaintext LDAP on internal networks is common. Only a finding on public-facing services.
- **NTLM from LDAP without relay path** — capturing NTLM hashes from LDAP is valuable only if there's a relay target.

---

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-ldap/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

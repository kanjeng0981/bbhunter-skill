---
name: hunt-xxe
description: Hunting skill for xxe vulnerabilities. Built from 10 public bug bounty reports including SVG-upload XXE, Office-doc (PPTX/DOCX) XXE, SOAP XXE, SAML AssertionConsumer XXE, blind OOB XXE via DTD callback, parameter-entity XXE, XXE-to-LFI, XXE-to-SSRF, and XXE-to-RCE chains (Adobe Commerce CosmicSting CVE-2024-34102). Use when hunting XXE on any target — emphasis on OOB-Or-It-Didn't-Happen Gate for blind cases.
scope: web2
---
Hunting skill for xxe vulnerabilities. Built from 10 public bug bounty reports including SVG-upload XXE, Office-doc (PPTX/DOCX) XXE, SOAP XXE, SAML AssertionConsumer XXE, blind OOB XXE via DTD callback, parameter-entity XXE, XXE-to-LFI, XXE-to-SSRF, and XXE-to-RCE chains (Adobe Commerce CosmicSting CVE-2024-34102). Use when hunting XXE on any target — emphasis on OOB-Or-It-Didn't-Happen Gate for blind cases.

1. **Default parser configurations** — Java's DocumentBuilderFactory, PHP's DOMDocument, and Python's lxml all support external entities by default. Developers use them without reading the security docs.

2. **Framework upgrades without security re-review** — Older versions of Spring, Struts, and similar frameworks enabled XXE by default; developers didn't re-audit XML handling when libraries changed.

3. **Hidden XML consumption** — Developers accept JSON at the API layer but convert to XML internally, or use libraries (Apache POI, python-docx) to process uploads without realizing those formats are XML containers.

4. **Copy-paste code from StackOverflow** — XML parsing examples online rarely include entity disabling. Developers copy minimal working examples straight into production.

5. **SAML/SSO library misconfigurations** — SSO integrations often delegate XML parsing to third-party libraries with XXE enabled; developers assume "library handles security."

6. **Testing gaps on non-primary content types** — QA tests JSON APIs extensively; XML code paths receive minima
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-xxe/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

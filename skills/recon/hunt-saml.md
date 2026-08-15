---
name: hunt-saml
description: Hunt SAML / SSO attacks. Patterns: XML Signature Wrapping (XSW) — modify Assertion while keeping Signature valid by relocating signed element, comment injection in NameID (admin@target.com<!--evil-->@attacker.com → some parsers see admin@target.com), signature stripping (remove Signature element entirely, server should reject but doesn't), key confusion (signed by attacker's IdP, accepted by SP), audience-restriction not validated, replay attack (same Assertion accepted twice within validity window). Tools: SAML Raider Burp extension, samlmagic, manual XML manipulation. Detection: any /saml endpoint, /Shibboleth.sso, /sso/saml/, Microsoft ADFS endpoints. Validate: account takeover via altered NameID, admin role injection via altered AttributeStatement. Use when hunting SSO flows, when SAML AssertionConsumerService is reachable, when chaining IdP-trust to SP-impersonation.
scope: web2
---
Hunt SAML / SSO attacks. Patterns: XML Signature Wrapping (XSW) — modify Assertion while keeping Signature valid by relocating signed element, comment injection in NameID (admin@target.com<!--evil-->@attacker.com → some parsers see admin@target.com), signature stripping (remove Signature element entirely, server should reject but doesn't), key confusion (signed by attacker's IdP, accepted by SP), audience-restriction not validated, replay attack (same Assertion accepted twice within validity window). Tools: SAML Raider Burp extension, samlmagic, manual XML manipulation. Detection: any /saml endpoint, /Shibboleth.sso, /sso/saml/, Microsoft ADFS endpoints. Validate: account takeover via altered NameID, admin role injection via altered AttributeStatement. Use when hunting SSO flows, when SAML AssertionConsumerService is reachable, when chaining IdP-trust to SP-impersonation.

- **SAML without signature validation** — unsigned assertions or WantAssertionsSigned="false" are the primary SAML findings.
- **XML signature wrapping (XSW)** — classic SAML attack. Test all 8 XSW variants, not just #1.
- **SAML Response replay** — capturing and replaying a SAML Response within its validity window. Test NotOnOrAfter enforcement.
- **SAML-to-JWT confusion** — SAML assertions are XML; JWT is JSON. Don't cross-apply attack techniques.
- **SP metadata publicly accessible** — accessing /saml/metadata is informational. The finding is what the metadata reveals (unsigned requests, weak algorithms)
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-saml/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

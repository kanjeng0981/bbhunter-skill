---
name: hunt-deserialization
description: Hunt Insecure Deserialization — Java gadget chains (ysoserial), PHP object injection (phpggc), Python pickle RCE, .NET BinaryFormatter, Ruby Marshal.load, JNDI/Log4Shell. RCE via deserialization is almost always Critical. Use when target runs Java, PHP serialization, Python pickle, .NET, or Ruby on Rails.
scope: web2
---
Hunt Insecure Deserialization — Java gadget chains (ysoserial), PHP object injection (phpggc), Python pickle RCE, .NET BinaryFormatter, Ruby Marshal.load, JNDI/Log4Shell. RCE via deserialization is almost always Critical. Use when target runs Java, PHP serialization, Python pickle, .NET, or Ruby on Rails.

- **ysoserial payload without gadget chain** — generating a payload is not exploitation. Need to confirm the target's classpath contains the specific gadget.
- **Java deserialization vs PHP unserialize** — different languages, different tools. Don't cross-apply payloads.
- **Base64-encoded payload but server expects raw binary** — some servers accept base64, others raw. Test both encodings.
- **Content-Type mismatch** — Java deserialization typically expects application/x-java-serialized-object or application/octet-stream. Wrong Content-Type may cause silent rejection.
- **WAF deserialization filtering** — many WAFs block known ysoserial gadget signatures. The bug may still exist but require a custom gadget chain.


---

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-deserialization/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

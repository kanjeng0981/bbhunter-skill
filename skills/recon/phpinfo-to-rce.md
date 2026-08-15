---
name: phpinfo-to-rce
description: Chain phpinfo to RCE via exec check when info.php exposed.
scope: web2
---
Chain phpinfo to RCE via exec check when info.php exposed.

- source-leak-hunt flags a target with info.php or phpinfo.php exposed.
- You need to confirm whether RCE is possible before investing in upload vectors.
- Building an attack chain that requires code execution.
- Target has a file upload path (open registration + XMLRPC, contact form, profile image, etc.).

- **phpinfo behind WAF:** Cloudflare may cache phpinfo or block certain paths. Try /test.php, /php_info.php, /info.php?1.
- **disable_functions bypass complexity:** LD_PRELOAD bypass requires compiling a .so file matching the target's architecture and libc. FFI bypass requires PHP 7.4+ and FFI::cdef() not in disable_functions.
- **Upload path discovery:** WordPress stores uploads in /wp-content/uploads/YYYY/MM/. Some hosts change this via UPLOADS constant (check phpinfo).
- **Webshell blocked by WAF:** If the host has mod_security or a WAF, the PHP webshell may be blocked on access. Try alternative extensions (.phtml, .php5, .pht) or obfuscated payloads.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/phpinfo-to-rce/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

---
name: hunt-lfi
description: Hunt Local File Inclusion (LFI), Remote File Inclusion (RFI), and Path Traversal — /etc/passwd read, log poisoning → RCE, PHP filter-chain RCE (no upload needed), php:// / data:// / zip:// / phar:// wrappers, RFI via allow_url_include, directory traversal read/write/delete. Covers OOB/blind LFI confirmation and false-positive discipline. Use when hunting file-include or path-traversal bugs on any target.
scope: web2
---
Hunt Local File Inclusion (LFI), Remote File Inclusion (RFI), and Path Traversal — /etc/passwd read, log poisoning → RCE, PHP filter-chain RCE (no upload needed), php:// / data:// / zip:// / phar:// wrappers, RFI via allow_url_include, directory traversal read/write/delete. Covers OOB/blind LFI confirmation and false-positive discipline. Use when hunting file-include or path-traversal bugs on any target.

- **LFI without file content** — /etc/passwd on a modern system without password hashes is informational. Need shadow file, SSH keys, or application config.
- **Path traversal without LFI** — ../../../etc/passwd returning 200 but no file content is path traversal, not LFI. Different attack class.
- **LFI to RCE chain incomplete** — LFI to /proc/self/environ or log poisoning requires specific conditions. Document the full chain.
- **PHP wrapper chain** — php://filter base64 encode works on many PHP versions. Test before assuming LFI is unexploitable.
- **Null byte injection** — %00 truncation was patched in PHP 5.3.4+. Not applicable to modern PHP.

---

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-lfi/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

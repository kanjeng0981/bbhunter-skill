---
name: hunt-file-upload
description: Hunt file upload bugs — RCE via webshell, XSS via SVG/HTML, SSRF via XXE in DOCX, path traversal via filename. Bypass tables (10 techniques): double extension (shell.php.jpg if server checks last ext only), magic bytes spoofing (PNG header on PHP), null byte (shell.php\0.jpg), case (PHP, .Php, .pHP), .htaccess upload to enable execution, SVG with <script>, HTML/SVG XSS, DOCX with embedded XXE, ZIP slip (../../../etc/passwd in archive), polyglot files. Detection: any /upload, /avatar, /profile-picture, /attachment, /import endpoint. Test: upload PHP/JSP/ASPX shells, request via direct URL, check response. Validate: actual code execution (whoami output) for RCE; reflected XSS in profile-photo URL. Use when testing file upload features, avatar/attachment endpoints, import/export functions, XML/DOCX/ZIP processors. Real paid examples.
scope: web2
---
Hunt file upload bugs — RCE via webshell, XSS via SVG/HTML, SSRF via XXE in DOCX, path traversal via filename. Bypass tables (10 techniques): double extension (shell.php.jpg if server checks last ext only), magic bytes spoofing (PNG header on PHP), null byte (shell.php\0.jpg), case (PHP, .Php, .pHP), .htaccess upload to enable execution, SVG with <script>, HTML/SVG XSS, DOCX with embedded XXE, ZIP slip (../../../etc/passwd in archive), polyglot files. Detection: any /upload, /avatar, /profile-picture, /attachment, /import endpoint. Test: upload PHP/JSP/ASPX shells, request via direct URL, check response. Validate: actual code execution (whoami output) for RCE; reflected XSS in profile-photo URL. Use when testing file upload features, avatar/attachment endpoints, import/export functions, XML/DOCX/ZIP processors. Real paid examples.

- **Upload without execution** — uploading a .php file to a directory that serves it as text/plain is not RCE. Need code execution, not just file storage.
- **SVG XSS without same-origin rendering** — SVG uploaded to a different origin may not execute scripts due to CSP or same-origin policy. Test in the actual rendering context.
- **Extension blacklist bypass without server-side validation** — bypassing client-side extension check proves nothing. Always test server-side acceptance.
- **Content-Type spoofing** — changing Content-Type header doesn't change how the server processes the file. Need to confirm server-side MIME confusion.
- **Path traver
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-file-upload/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

---
name: hunt-wordpress
description: Use when an authorized target exposes WordPress core, plugin, theme, REST, or XML-RPC behavior.
scope: web2
---
Use when an authorized target exposes WordPress core, plugin, theme, REST, or XML-RPC behavior.

- HTML, headers, assets, cookies, or routes identify WordPress.
- /wp-json/, /wp-login.php, /xmlrpc.php, or /wp-content/ is reachable.
- JavaScript or source code references a WordPress backend.
- A staging or subdirectory installation may differ from the main site.

- WordPress routes frequently sit behind CDN, cache, or catch-all behavior.
- GET /xmlrpc.php returning 405 does not classify a valid POST method call.
- A REST namespace does not prove that a plugin operation is unauthenticated.
- Public author metadata is not automatically sensitive.
- Plugin versions can be hidden, backported, or reported by stale assets.
- Large logs, sitemaps, and REST collections can cause unnecessary data
  collection; request bounded samples.
- Default credential attempts, password spraying, registration, uploads, and
  writes require explicit authorization and agreed lockout limits.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-wordpress/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

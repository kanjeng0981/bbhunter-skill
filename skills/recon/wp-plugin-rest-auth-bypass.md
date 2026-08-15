---
name: wp-plugin-rest-auth-bypass
description: Scan WordPress REST API plugin endpoints for unauthenticated state-changing operations — discover write endpoints (POST/PUT/PATCH/DELETE) exposed without auth, enumerate all plugin routes, and test for unauthorized content publishing, settings modification, and data leakage.
scope: web2
---
Scan WordPress REST API plugin endpoints for unauthenticated state-changing operations — discover write endpoints (POST/PUT/PATCH/DELETE) exposed without auth, enumerate all plugin routes, and test for unauthorized content publishing, settings modification, and data leakage.

- Target is a WordPress site with exposed users via /wp-json/wp/v2/users.
- You've found interesting plugin namespaces from /wp-json/ but need to map their routes.
- Standard WordPress endpoints return 401 — but third-party plugin endpoints might not.
- You want to find hidden admin URLs, debug endpoints, or unauthenticated write operations.

- **401 vs 400**: A 401 means auth is enforced. A 400 with "Missing parameter" means the endpoint IS accessible but needs correct arguments.
- **JSON parsing**: Some plugins return JSON as a string (double-encoded). Check r.text before r.json().
- **Rate limiting**: Rapid testing may trigger security plugins. Space requests 1-2s apart.
- **WAF interference**: Cloudflare or Wordfence may block POST requests to certain paths. Try with different Content-Type headers.
- **Post type validation**: Some endpoints validate post_type against registered types. Try post, page, product, attachment, and custom types.
- **Clean up test data**: If you create content during testing, delete it if possible. If the plugin has no unauthenticated DELETE, note that cleanup requires manual intervention.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/wp-plugin-rest-auth-bypass/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

---
name: hunt-django
description: Hunt Django-specific vulnerabilities: DRF permission gaps, ORM injection, and admin exploitation.
scope: web2
---
Hunt Django-specific vulnerabilities: DRF permission gaps, ORM injection, and admin exploitation.

- Target uses Python/Django (indicated by csrftoken cookie, /admin/ login, DRF browsable API, or __debug__toolbar).
- DRF API endpoints with class-based views and permission classes.
- Django Admin interface is reachable at /admin/ or custom path.
- Celery task queues process user-supplied data.
- Django Channels WebSocket endpoints exist alongside REST API.

- **DRF AllowAny ≠ misconfiguration.** Verify the endpoint is supposed to be public before reporting.
- **Django admin brute force is heavily logged.** Use with caution on production targets.
- **Template injection requires a sink.** Django's template engine auto-escapes by default — |safe or mark_safe must be explicitly used.
- **SECRET_KEY must be actually leaked.** Guessing or brute-forcing SECRET_KEY is computationally infeasible.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-django/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

---
name: error-log-mining
description: Mine error_log for creds, paths, SQL when leak hunt finds.
scope: web2
---
Mine error_log for creds, paths, SQL when leak hunt finds.

- Running deep-invade Phase 2 on a high-value target.
- skill_view(name='source-leak-hunt') found an error_log file with HTTP 200.
- Target has PHP (WordPress, Laravel, custom PHP) with display_errors possibly enabled.
- You need server-side context (paths, DB structure) before attempting exploitation.

- **Error logs can be very large.** Check Content-Length before downloading
  and use a bounded range such as curl -r 0-5000000 for an initial sample.
- **Logs may contain PII.** Email addresses, IPs, and usernames in error logs may constitute a data breach. Handle responsibly.
- **Log rotation may truncate.** The visible error_log may only contain recent entries. Check for rotated logs (error_log.1, error_log.old, error_log-YYYYMMDD).
- **Some hosts return garbage.** A 200 on /error_log might be a custom 404 page or SPA catch-all. Always check content for PHP  + error type pattern before analyzing.
- **Old logs ≠ current vulnerability.** A 2013 error log doesn't mean the current site is vulnerable. Cross-reference log timeline with the server tech stack.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/error-log-mining/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

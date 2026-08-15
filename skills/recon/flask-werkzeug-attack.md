---
name: flask-werkzeug-attack
description: Exploit Flask/Werkzeug debugger exposure for traceback and SECRET leaks.
scope: web2
---
Exploit Flask/Werkzeug debugger exposure for traceback and SECRET leaks.

- Port scan reveals an unknown HTTP service on a non-standard port (8080, 8081, 8084, 5000, 8000, etc.)
- An API endpoint returns HTTP 500 with a Flask/Werkzeug error page
- A ?__debugger__=yes parameter appears in URL resources (CSS, JS, PNG)
- The error page contains var CONSOLE_MODE, var EVALEX, or SECRET= in the HTML

- **EVALEX=false means NO RCE through the console.** Do not waste time trying to execute code when console mode is disabled.
- **The SECRET is not enough.** Even with the correct SECRET, the console must be enabled for code execution.
- **Not all HTTP 500 pages are Werkzeug.** Plain Flask error pages without HTML formatting or with JSON-only responses are NOT the Werkzeug debugger. The debugger has a distinctive blue-themed HTML page with collapsible traceback frames and source code context.
- **The debugger may be behind CORS.** Check Access-Control-Allow-Origin headers — CORS wildcard on the debugger page means an attacker-controlled website can read the SECRET and traceback via fetch().
- **Triggering errors leaves logs.** Every debugger page request generates a 500 error in the server logs. Be conservative to avoid detection.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/flask-werkzeug-attack/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

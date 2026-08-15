---
name: hunt-information-disclosure
description: Hunt error leakage, DVCS exposure, source maps, config files, and differential oracles.
scope: web2
---
Hunt error leakage, DVCS exposure, source maps, config files, and differential oracles.

- Applications return verbose error messages with stack traces, file paths, or SQL fragments.
- Source maps (.js.map) are deployed to production.
- Versioned static assets reveal framework/CMS versions.
- API responses differ by object existence (user enumeration by status/length/time).
- Debug endpoints, health checks, or status pages expose internal state.

- **Not every error message is exploitable.** A generic "An error occurred" page with no details is not a finding.
- **Source maps may be empty or stripped.** Verify extracted content before reporting.
- **Differential oracles are statistical.** Confirm with at least 3 samples before reporting.
- **.git exposure must contain actual repo data, not just HTTP 200 on a path.** A catch-all SPA may return 200 for /.git/HEAD without serving git data.
- **Version disclosure alone is usually LOW severity.** Chain it — version → CVE → exploit.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-information-disclosure/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

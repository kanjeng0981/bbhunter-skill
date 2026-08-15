---
name: humanize-automation
description: Human-like mouse, keyboard and scroll behavior for behavioral bot bypass.
scope: web2
---
Human-like mouse, keyboard and scroll behavior for behavioral bot bypass.

- Target uses behavioral bot detection (mouse trajectory analysis, typing speed profiling).
- reCAPTCHA v3 scores are low (<0.3) despite correct browser fingerprint.
- Target times out or challenges after rapid form submissions.
- Need to simulate a real user browsing session for login or account creation.
- Target uses requestAnimationFrame-based mouse movement tracking.

- **Humanize requires the wrapper.** Connecting via CDP without the wrapper loses humanization — only fingerprint patches work over raw CDP.
- **ElementHandle objects bypass humanization in Playwright.** Use page.click(selector) or page.locator(selector).* — avoid query_selector() handles.
- **page.fill() with humanize clears existing content and types character by character.** This is intentional but slower than raw fill().
- **Typing speed profiling exists.** Some sites measure ms-between-keystrokes. Use careful preset or increase typing_delay for suspicious targets.
- **Scroll-to-element is automatic.** On click/hover, the element is scrolled into view with human scroll before interaction.
- **CDP Isolated Worlds are used for stealth DOM queries.** This prevents monkey-patch detection in the main JavaScript context.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/humanize-automation/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

---
name: hunt-ssti
description: Hunt server-side template injection (SSTI) across Jinja2 (Flask/Django), Twig (Symfony), Freemarker (Java), ERB (Rails), Spring, Velocity, Mako, Thymeleaf, Smarty. Detection probes use double-curly and dollar-curly math expressions evaluated server-side. Once an engine is fingerprinted, escalate to RCE via the engine-specific class-walker, callback-registrar, or Execute-utility patterns documented in disclosed reports. Detection patterns: error messages reveal engine, blank or numeric eval reveals expression mode. Targets: email templates, PDF/report generators, CMS preview features, error pages with user input. Use when hunting RCE via template rendering, when content shows engine fingerprints, when finding endpoints that compose strings with user input before render.
scope: web2
---
Hunt server-side template injection (SSTI) across Jinja2 (Flask/Django), Twig (Symfony), Freemarker (Java), ERB (Rails), Spring, Velocity, Mako, Thymeleaf, Smarty. Detection probes use double-curly and dollar-curly math expressions evaluated server-side. Once an engine is fingerprinted, escalate to RCE via the engine-specific class-walker, callback-registrar, or Execute-utility patterns documented in disclosed reports. Detection patterns: error messages reveal engine, blank or numeric eval reveals expression mode. Targets: email templates, PDF/report generators, CMS preview features, error pages with user input. Use when hunting RCE via template rendering, when content shows engine fingerprints, when finding endpoints that compose strings with user input before render.

Use when the target has any endpoint that renders user-controlled input through a server-side template engine. SSTI is one of the fastest paths to RCE — detection is a single {{7*7}} and escalation typically requires one more payload. SSTI detection is reliable because template expressions evaluate BEFORE HTML encoding, so the result 49 appears in the rendered output even if the surrounding page is properly escaped.

**Triggering contexts:** email templates (order confirmations, password resets, welcome emails), PDF/report generators, CMS preview features (page builder previews, theme editors), error pages that reflect user input, profile bio/name/description fields rendered by server-side templates, URL path
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-ssti/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

---
name: hunt-rce
description: Hunting skill for rce vulnerabilities. Built from 67 public bug bounty reports. Use when hunting rce on any target.
scope: web2
---
Hunting skill for rce vulnerabilities. Built from 67 public bug bounty reports. Use when hunting rce on any target.

Use when the target has any endpoint that processes user-controlled input through an execution layer — template engines, shell commands, YAML/XML parsers, file paths used in operations, package resolution, or configuration files. RCE is the highest-payout vulnerability class because it grants direct execution control over target infrastructure. Every admin/management console, template/preview endpoint, upload processor, deserialization sink, and dependency resolver is a candidate. Highest-value targets: enterprise server products (GHES, self-hosted GitLab), supply chain/package registries, cloud-native infrastructure, and admin/management consoles.

**1. Configuration-as-code with insufficient sanitization**
Administrators edit configuration files (syslog-ng, collectd, nomad) through web UIs. Developers assume admin == trusted, so they pass field values directly into config files that support execution primitives (program() destinations, exec plugins, template functions).

**2. Template engines in privileged contexts**
Go's text/template, Freemarker, Velocity, and Twig are used for system configuration rendering. When user-controlled strings reach these engines without sandboxing, arbitrary code follows.

**3. Dependency confusion / namespace squatting**
Internal packages published to private registries without locking the public registry namespace. Build syste
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-rce/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

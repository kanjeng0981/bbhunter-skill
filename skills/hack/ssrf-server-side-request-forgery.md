---
name: ssrf-server-side-request-forgery
description: SSRF playbook. Use when the server fetches URLs, resolves hostnames, imports remote content, or can be driven toward internal networks, cloud metadata, or secondary protocols.
scope: web2
---
SSRF playbook. Use when the server fetches URLs, resolves hostnames, imports remote content, or can be driven toward internal networks, cloud metadata, or secondary protocols.

# SKILL: Server-Side Request Forgery (SSRF) — Expert Attack Playbook

> **AI LOAD INSTRUCTION**: Expert SSRF techniques. Covers URL filter bypass, cloud metadata endpoints, protocol exploitation, blind SSRF detection, and chaining to RCE. Base models know basic 169.254.169.254 — this file covers what they miss. For real-world CVE chains, DNS Rebinding deep dives, K8s SSRF, and SSRF → Redis → RCE full exploitation, load the companion [SCENARIOS.md](./SCENARIOS.md).

## 0. QUICK START

### Extended Scenarios

Also load [SCENARIOS.md](./SCENARIOS.md) when you need:
- WebLogic SSRF (CVE-2014-4210) — uddiexplorer/SearchPublicRegistries.jsp + operator parameter + %0D%0A CRLF to inject Redis commands
- SSRF → internal Redis → write crontab reverse shell complete payload chain
- DNS Rebinding deep dive — TTL=0 trick, initial-legit→second-internal resolution, rbndr.us service
- Kubernetes SSRF (CVE-2020-8555) and bypass (CVE-2020-8562) via DNS rebinding
- SSRF through PDF/screenshot generators — <iframe> and <img> in HTML-to-PDF
- Gopher protocol full TCP injection — Redis, MySQL, FastCGI payloads via Gopherus
- URL parser confusion for filter bypass — #@, \@, %00@, IPv6-mapped IPv4

### Advanced Reference

Also load [URL_PARSER_TRICKS.md](./URL_PARSER_TRICKS.md) when you need:
- URL parser differential table: Python urllib vs requests vs Java URL vs PHP parse_url vs Node url.parse vs Go net/url
- Full cloud metadata endpoint catalog (AWS IMDSv1/v2, GCP, Azure, DigitalOcean, Alibaba Cloud, Oracle Cloud, Kubernetes, Hetzner, OpenStack)
- gopher:// payload recipes for Redis, MySQL, SMTP, FastCGI, Memcached (with encoding rules)
- DNS Rebinding detailed attack flow with TTL manipulation and TOCTOU analysis
- PDF/wkhtmltopdf/WeasyPrint/Chrome headless/PhantomJS SSRF patterns and exfiltration techniques

If you just found a parameter that fetches a URL, perform first-pass confirmation here directly.

### First-pass payloads

http://127.0.0.1/
http://localhost/
http://169.254.169.254/latest/meta-data/
http://[::1]/
http://127.1/

### Host validation bypass families

| Validation Type | Try |
|---|---|
| blocks localhost string | 127.0.0.1, 127.1, [::1] |
| blocks direct IP only | internal DNS name, decimal/octal/hex IP forms |
| allowlist by prefix | username part, subdomain confusion, redirect ch
...

## References
- Source: https://github.com/yaklang/hack-skills/blob/main/skills/ssrf-server-side-request-forgery/SKILL.md
- License: MIT — Copyright (c) 2026 VillanCh
- Distilled for bbhunter by scripts/import_hack_skills.py

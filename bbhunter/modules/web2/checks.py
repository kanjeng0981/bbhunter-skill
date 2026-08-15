"""Non-destructive, GET-based web2 checks.

Every check here is passive/safe: it only issues normal HTTP GET requests
with benign payloads and inspects responses. Run only against targets you are
authorized to test.
"""
from __future__ import annotations

import base64
import json
import re
from urllib.parse import urlencode, urlparse, parse_qsl, urlunparse

import httpx

from ...models import Finding, WebHost

# Common sensitive/exposed paths.
_EXPOSED_PATHS = [
    (".git/config", "[core]", "Exposed .git config", "high", "CWE-538"),
    (".env", "APP_KEY=", "Exposed .env file", "critical", "CWE-538"),
    (".env", "DB_PASSWORD=", "Exposed .env file", "critical", "CWE-538"),
    ("backup.zip", "", "Backup archive present", "medium", "CWE-530"),
    ("backup.tar.gz", "", "Backup archive present", "medium", "CWE-530"),
    ("wp-config.php.bak", "DB_", "WordPress config backup", "high", "CWE-530"),
    ("server-status", "Server Version", "Apache server-status exposed", "medium", "CWE-200"),
]

# Headers considered security-relevant; missing -> informational/low.
_SECURITY_HEADERS = [
    ("content-security-policy", "Content-Security-Policy", "CWE-693"),
    ("x-frame-options", "X-Frame-Options", "CWE-1021"),
    ("x-content-type-options", "X-Content-Type-Options", "CWE-16"),
    ("strict-transport-security", "Strict-Transport-Security", "CWE-319"),
    ("referrer-policy", "Referrer-Policy", "CWE-200"),
    ("permissions-policy", "Permissions-Policy", "CWE-693"),
]

_SQLI_ERRORS = [
    "sql syntax", "mysql_fetch", "you have an error in your sql",
    "unclosed quotation mark", "ora-", "postgresql", "sqlite", "microsoft ole db",
    "odbc driver", "syntax error at or near",
]

_XSS_CANARY = "bbhunterxsscanary_<script>alert(1)</script>"

# Common redirect-controlling parameter names.
_REDIRECT_PARAMS = [
    "url", "next", "redirect", "return", "return_url", "return_to",
    "redirect_uri", "callback", "dest", "destination", "continue", "target",
    "redir", "goto", "out", "rurl",
]

_JWT_RE = re.compile(r"eyJ[A-Za-z0-9_-]{6,}\.[A-Za-z0-9_-]{6,}\.[A-Za-z0-9_-]{6,}")

_GRAPHQL_ENDPOINTS = ["graphql", "graphiql", "api/graphql", "v1/graphql", "query"]
_GRAPHQL_INTROSPECTION = '{"query":"{__schema{queryType{name} types{name}}}"}'

_PP_CANARY = "bbhunter_pp_canary_7f3a"

# Response headers that indicate a front-end proxy/CDN (smuggling prerequisite).
_PROXY_HEADERS = (
    "via", "x-cache", "x-cache-status", "cf-ray", "x-served-by",
    "x-amz-cf-id", "cdn-cache-control", "x-vercel-cache", "age", "x-proxy-cache",
)


def _b64url_decode(value: str) -> bytes:
    padding = "=" * (-len(value) % 4)
    try:
        return base64.urlsafe_b64decode(value + padding)
    except ValueError:
        return b""


def _client(timeout: float, user_agent: str, follow_redirects: bool = True) -> httpx.Client:
    return httpx.Client(
        follow_redirects=follow_redirects,
        timeout=timeout,
        verify=False,
        headers={"User-Agent": user_agent},
    )


def check_security_headers(host: WebHost) -> list[Finding]:
    findings: list[Finding] = []
    if not host.headers:
        return findings
    missing = [name for key, name, _cwe in _SECURITY_HEADERS if key not in host.headers]
    if missing:
        findings.append(
            Finding(
                module="web2.headers.missing",
                target=host.url,
                title="Missing security headers",
                description="The following security headers are missing: "
                + ", ".join(missing),
                severity="low",
                evidence=f"Missing: {', '.join(missing)}",
                cwe="CWE-693",
            )
        )
    return findings


def check_server_disclosure(host: WebHost) -> list[Finding]:
    findings: list[Finding] = []
    server = host.headers.get("server", "")
    if server and any(ch.isdigit() for ch in server):
        findings.append(
            Finding(
                module="web2.headers.server",
                target=host.url,
                title="Server version disclosure",
                description=f"Server header leaks software/version: {server}",
                severity="info",
                evidence=f"Server: {server}",
                cwe="CWE-200",
            )
        )
    return findings


def check_exposed_files(host: WebHost, timeout: float, user_agent: str) -> list[Finding]:
    findings: list[Finding] = []
    client = _client(timeout, user_agent)
    base = host.url.rstrip("/")
    for path, marker, title, severity, cwe in _EXPOSED_PATHS:
        url = f"{base}/{path}"
        try:
            resp = client.get(url)
        except httpx.HTTPError:
            continue
        if resp.status_code == 200 and (not marker or marker in resp.text):
            findings.append(
                Finding(
                    module="web2.exposed",
                    target=url,
                    title=title,
                    description=f"Sensitive file appears exposed at {url}",
                    severity=severity,
                    evidence=resp.text[:500],
                    confidence="high" if marker else "medium",
                    cwe=cwe,
                )
            )
    return findings


def check_sqli_reflection(host: WebHost, timeout: float, user_agent: str) -> list[Finding]:
    findings: list[Finding] = []
    client = _client(timeout, user_agent)
    # Only try query params already present in the URL.
    parsed = urlparse(host.url)
    if not parsed.query:
        return findings
    params = parse_qsl(parsed.query, keep_blank_values=True)
    if not params:
        return findings
    test = [(k, v + "'") for k, v in params]
    test_url = urlunparse(parsed._replace(query=urlencode(test)))
    try:
        resp = client.get(test_url)
    except httpx.HTTPError:
        return findings
    lowered = resp.text.lower()
    for err in _SQLI_ERRORS:
        if err in lowered:
            findings.append(
                Finding(
                    module="web2.sqli.error",
                    target=host.url,
                    title="Possible SQL injection (error-based)",
                    description=f"Database error string detected when injecting a quote: {err}",
                    severity="high",
                    evidence=f"Matched: {err}",
                    confidence="low",
                    cwe="CWE-89",
                )
            )
            break
    return findings


def check_xss_reflection(host: WebHost, timeout: float, user_agent: str) -> list[Finding]:
    findings: list[Finding] = []
    client = _client(timeout, user_agent)
    parsed = urlparse(host.url)
    if not parsed.query:
        return findings
    params = parse_qsl(parsed.query, keep_blank_values=True)
    if not params:
        return findings
    # Inject canary into the first query param and check reflection.
    k, _v = params[0]
    test_url = urlunparse(parsed._replace(query=urlencode([(k, _XSS_CANARY)])))
    try:
        resp = client.get(test_url)
    except httpx.HTTPError:
        return findings
    if _XSS_CANARY in resp.text:
        findings.append(
            Finding(
                module="web2.xss.reflected",
                target=host.url,
                title="Possible reflected XSS",
                description=f"Payload reflected unencoded in parameter '{k}'",
                severity="medium",
                evidence=f"Canary reflected in response for param {k}",
                confidence="low",
                cwe="CWE-79",
            )
        )
    return findings


def check_cors(host: WebHost, timeout: float, user_agent: str) -> list[Finding]:
    findings: list[Finding] = []
    client = _client(timeout, user_agent)
    base = host.url.rstrip("/")
    for origin in ("https://evil.com", "null"):
        try:
            resp = client.get(base, headers={"Origin": origin})
        except httpx.HTTPError:
            continue
        acao = resp.headers.get("access-control-allow-origin", "")
        acac = resp.headers.get("access-control-allow-credentials", "").lower() == "true"
        if not acao:
            continue
        reflects = acao == origin or acao == "*" or origin in acao
        if reflects and acac:
            findings.append(
                Finding(
                    module="web2.cors.credentials",
                    target=host.url,
                    title="CORS misconfiguration (credentialed cross-origin read)",
                    description=f"Origin {origin!r} is reflected/allowed together with "
                    "Access-Control-Allow-Credentials: true. Confirm in a browser that "
                    "an attacker origin can read sensitive data.",
                    severity="high",
                    evidence=f"Origin: {origin} -> ACAO: {acao}, ACAC: true",
                    confidence="medium",
                    cwe="CWE-942",
                )
            )
            break
        if reflects and origin == "null":
            findings.append(
                Finding(
                    module="web2.cors.null_origin",
                    target=host.url,
                    title="CORS trusts null origin",
                    description="Access-Control-Allow-Origin: null allows sandboxed/iframed "
                    "contexts to read responses.",
                    severity="low",
                    evidence=f"Origin: null -> ACAO: {acao}",
                    confidence="low",
                    cwe="CWE-942",
                )
            )
    return findings


def check_open_redirect(host: WebHost, timeout: float, user_agent: str) -> list[Finding]:
    findings: list[Finding] = []
    client = _client(timeout, user_agent, follow_redirects=False)
    parsed = urlparse(host.url)
    existing = dict(parse_qsl(parsed.query, keep_blank_values=True))
    candidates = [k for k in _REDIRECT_PARAMS if k in existing] or ["redirect", "next", "url"]
    evil = "https://evil.com/"
    for k in candidates:
        q = [(kk, vv) for kk, vv in parse_qsl(parsed.query, keep_blank_values=True) if kk != k]
        q.append((k, evil))
        test_url = urlunparse(parsed._replace(query=urlencode(q)))
        try:
            resp = client.get(test_url)
        except httpx.HTTPError:
            continue
        loc = resp.headers.get("location", "")
        if resp.status_code in (301, 302, 303, 307, 308) and "evil.com" in loc:
            findings.append(
                Finding(
                    module="web2.openredirect",
                    target=host.url,
                    title="Open redirect",
                    description=f"Parameter {k!r} causes a redirect to an attacker-controlled URL.",
                    severity="medium",
                    evidence=f"{k}={evil} -> {resp.status_code} Location: {loc}",
                    confidence="high",
                    cwe="CWE-601",
                )
            )
            break
    return findings


def check_host_header(host: WebHost, timeout: float, user_agent: str) -> list[Finding]:
    findings: list[Finding] = []
    client = _client(timeout, user_agent)
    base = host.url.rstrip("/")
    for hdr in ("Host", "X-Forwarded-Host"):
        try:
            resp = client.get(base, headers={hdr: "evil.com"})
        except httpx.HTTPError:
            continue
        if "evil.com" in resp.text:
            findings.append(
                Finding(
                    module="web2.hostheader.reflection",
                    target=host.url,
                    title=f"{hdr} header reflected in response",
                    description=f"The {hdr} header is reflected in the response body; may enable "
                    "password-reset poisoning, cache poisoning, or host-based routing "
                    "attacks. Verify impact manually.",
                    severity="low",
                    evidence=f"{hdr}: evil.com reflected",
                    confidence="low",
                    cwe="CWE-74",
                )
            )
    return findings


def check_jwt(host: WebHost, timeout: float, user_agent: str) -> list[Finding]:
    findings: list[Finding] = []
    client = _client(timeout, user_agent)
    try:
        resp = client.get(host.url.rstrip("/"))
    except httpx.HTTPError:
        return findings
    haystack = resp.text[:200_000] + " " + resp.headers.get("set-cookie", "")
    for tok in set(_JWT_RE.findall(haystack)):
        header_raw, _payload_raw, _sig = tok.split(".")
        try:
            header = json.loads(_b64url_decode(header_raw) or b"{}")
        except (ValueError, json.JSONDecodeError):
            header = {}
        alg = str(header.get("alg", "")).lower()
        if alg == "none":
            findings.append(
                Finding(
                    module="web2.jwt.alg_none",
                    target=host.url,
                    title="JWT with alg:none detected",
                    description="A JSON Web Token using the 'none' algorithm was observed. "
                    "If the server accepts it, signatures can be forged.",
                    severity="medium",
                    evidence=f"JWT header: {header}",
                    confidence="low",
                    cwe="CWE-347",
                )
            )
        else:
            findings.append(
                Finding(
                    module="web2.jwt.detected",
                    target=host.url,
                    title="JWT detected",
                    description=f"JWT observed (alg={alg or 'unknown'}). Investigate signing, "
                    "expiry, and key confusion (RS256->HS256).",
                    severity="info",
                    evidence=f"JWT header: {header}",
                    confidence="high",
                    cwe="CWE-347",
                )
            )
    return findings


def _cacheable(headers: dict[str, str]) -> bool:
    cc = headers.get("cache-control", "").lower()
    if "public" in cc or "max-age" in cc or "s-maxage" in cc:
        return True
    return any(h in headers for h in ("age", "x-cache", "x-cache-status", "cdn-cache-control"))


def check_cache_poison(host: WebHost, timeout: float, user_agent: str) -> list[Finding]:
    findings: list[Finding] = []
    client = _client(timeout, user_agent)
    base = host.url.rstrip("/")
    for hdr in ("X-Forwarded-Host", "X-Forwarded-Scheme", "X-Original-URL"):
        try:
            resp = client.get(base, headers={hdr: "evil.com"})
        except httpx.HTTPError:
            continue
        if "evil.com" in resp.text and _cacheable(resp.headers):
            findings.append(
                Finding(
                    module="web2.cache.unkeyed",
                    target=host.url,
                    title=f"Cacheable response reflects unkeyed {hdr} header",
                    description="An unkeyed header is reflected in a cacheable response; may "
                    "allow web cache poisoning. Verify the poisoned response is served to "
                    "other users.",
                    severity="low",
                    evidence=f"{hdr}: evil.com reflected; cache headers present",
                    confidence="low",
                    cwe="CWE-444",
                )
            )
    return findings


def check_graphql(host: WebHost, timeout: float, user_agent: str) -> list[Finding]:
    findings: list[Finding] = []
    client = _client(timeout, user_agent)
    base = host.url.rstrip("/")
    for ep in _GRAPHQL_ENDPOINTS:
        url = f"{base}/{ep}"
        try:
            resp = client.post(
                url, content=_GRAPHQL_INTROSPECTION,
                headers={"Content-Type": "application/json"},
            )
        except httpx.HTTPError:
            continue
        if resp.status_code == 200 and "__schema" in resp.text and "queryType" in resp.text:
            findings.append(
                Finding(
                    module="web2.graphql.introspection",
                    target=url,
                    title="GraphQL introspection enabled",
                    description="The GraphQL endpoint returns its schema via introspection, "
                    "leaking the full API surface to unauthenticated callers.",
                    severity="low",
                    evidence=f"POST {url} returned __schema/queryType",
                    confidence="high",
                    cwe="CWE-200",
                )
            )
            break
        try:
            resp2 = client.get(url, params={"query": "{__schema{types{name}}}"})
        except httpx.HTTPError:
            continue
        if resp2.status_code == 200 and "__schema" in resp2.text:
            findings.append(
                Finding(
                    module="web2.graphql.introspection",
                    target=url,
                    title="GraphQL introspection enabled",
                    description="The GraphQL endpoint returns its schema via introspection, "
                    "leaking the full API surface to unauthenticated callers.",
                    severity="low",
                    evidence=f"GET {url}?query={{__schema...}} returned schema",
                    confidence="high",
                    cwe="CWE-200",
                )
            )
            break
    return findings


def check_prototype_pollution(host: WebHost, timeout: float, user_agent: str) -> list[Finding]:
    findings: list[Finding] = []
    client = _client(timeout, user_agent)
    body = json.dumps({
        "__proto__": {"polluted": _PP_CANARY},
        "constructor": {"prototype": {"polluted": _PP_CANARY}},
    })
    try:
        resp = client.post(
            host.url.rstrip("/"), content=body, headers={"Content-Type": "application/json"}
        )
    except httpx.HTTPError:
        return findings

    headers = {**host.headers, **resp.headers}
    node_signal = any(
        "express" in headers.get(k, "").lower() for k in ("x-powered-by", "server")
    )
    ctype = resp.headers.get("content-type", "").lower()
    reflected = _PP_CANARY in resp.text

    # Only flag as a *surface* to investigate, not a confirmed finding.
    if "json" in ctype and (node_signal or reflected):
        findings.append(
            Finding(
                module="web2.prototypepollution.surface",
                target=host.url,
                title="Potential prototype pollution surface",
                description="Endpoint accepts JSON with user-controlled object keys on a "
                "JS/Node stack. Manually test __proto__/constructor.prototype gadgets.",
                severity="info",
                evidence=f"Node/Express signal: {node_signal}; canary reflected: {reflected}",
                confidence="low",
                cwe="CWE-1321",
            )
        )
    return findings


def check_http_smuggling(host: WebHost, timeout: float, user_agent: str) -> list[Finding]:
    findings: list[Finding] = []
    present = [h for h in _PROXY_HEADERS if h in host.headers]
    if present or "cloudflare" in host.headers.get("server", "").lower():
        findings.append(
            Finding(
                module="web2.smuggling.surface",
                target=host.url,
                title="Target sits behind a proxy/CDN (request-smuggling surface)",
                description="The response indicates a front-end proxy/CDN — a prerequisite "
                "for CL.TE/TE.CL/H2 request smuggling. Actively test with Burp's HTTP "
                "Request Smuggler or smuggler.py.",
                severity="info",
                evidence="Proxy/CDN headers: " + ", ".join(present),
                confidence="low",
                cwe="CWE-444",
            )
        )
    return findings


def check_meta_refresh_redirect(host: WebHost, timeout: float, user_agent: str) -> list[Finding]:
    findings: list[Finding] = []
    client = _client(timeout, user_agent, follow_redirects=False)
    parsed = urlparse(host.url)
    existing = dict(parse_qsl(parsed.query, keep_blank_values=True))
    candidates = [k for k in _REDIRECT_PARAMS if k in existing] or ["redirect", "next", "url"]
    evil = "https://evil.com/"
    markers = (
        'http-equiv="refresh"', "http-equiv='refresh'",
        "location.href", "window.location", "location.replace",
    )
    for k in candidates:
        q = [(kk, vv) for kk, vv in parse_qsl(parsed.query, keep_blank_values=True) if kk != k]
        q.append((k, evil))
        test_url = urlunparse(parsed._replace(query=urlencode(q)))
        try:
            resp = client.get(test_url)
        except httpx.HTTPError:
            continue
        body = resp.text.lower()
        if "evil.com" in body and any(m in body for m in markers):
            findings.append(
                Finding(
                    module="web2.openredirect.meta",
                    target=host.url,
                    title="Open redirect via meta-refresh / JS redirect",
                    description=f"Parameter {k!r} is reflected into a meta-refresh or "
                    "JavaScript redirect.",
                    severity="medium",
                    evidence=f"{k}={evil} reflected in redirect markup",
                    confidence="medium",
                    cwe="CWE-601",
                )
            )
            break
    return findings


def run_checks(host: WebHost, timeout: float, user_agent: str) -> list[Finding]:
    findings: list[Finding] = []
    findings.extend(check_security_headers(host))
    findings.extend(check_server_disclosure(host))
    findings.extend(check_exposed_files(host, timeout, user_agent))
    findings.extend(check_sqli_reflection(host, timeout, user_agent))
    findings.extend(check_xss_reflection(host, timeout, user_agent))
    findings.extend(check_cors(host, timeout, user_agent))
    findings.extend(check_open_redirect(host, timeout, user_agent))
    findings.extend(check_host_header(host, timeout, user_agent))
    findings.extend(check_jwt(host, timeout, user_agent))
    findings.extend(check_cache_poison(host, timeout, user_agent))
    findings.extend(check_graphql(host, timeout, user_agent))
    findings.extend(check_prototype_pollution(host, timeout, user_agent))
    findings.extend(check_http_smuggling(host, timeout, user_agent))
    findings.extend(check_meta_refresh_redirect(host, timeout, user_agent))
    return findings

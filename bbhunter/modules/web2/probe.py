"""HTTP probing of web hosts."""
from __future__ import annotations

import re
from urllib.parse import urlparse

import httpx

from ...models import WebHost
from . import tech
from .subdomain import resolve

TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)


def _http_client(timeout: float, user_agent: str) -> httpx.Client:
    return httpx.Client(
        follow_redirects=True,
        timeout=timeout,
        verify=False,
        headers={"User-Agent": user_agent},
    )


def probe(url: str, timeout: float, user_agent: str) -> WebHost | None:
    """Fetch a URL and collect basic recon metadata. Returns None on failure."""
    host = WebHost(url=url, domain=urlparse(url).hostname or "")
    try:
        resp = _http_client(timeout, user_agent).get(url)
    except httpx.HTTPError:
        return None

    host.status = resp.status_code
    host.headers = {k.lower(): v for k, v in resp.headers.items()}
    host.server = host.headers.get("server", "")
    host.content_type = host.headers.get("content-type", "")
    host.ip = resolve(host.domain)

    if "text/html" in host.content_type or "text/plain" in host.content_type:
        m = TITLE_RE.search(resp.text)
        if m:
            host.title = m.group(1).strip()[:200]
    host.technologies = tech.detect(host.headers, resp.text)
    return host


def probe_many(urls: list[str], timeout: float, user_agent: str) -> list[WebHost]:
    results: list[WebHost] = []
    for url in urls:
        h = probe(url, timeout, user_agent)
        if h is not None:
            results.append(h)
    return results

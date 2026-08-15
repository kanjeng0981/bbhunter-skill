"""Lightweight technology fingerprinting from headers and body."""
from __future__ import annotations

# header -> tech
_HEADER_SIGNATURES: dict[str, str] = {
    "x-powered-by": "x-powered-by",
    "x-aspnet-version": "ASP.NET",
    "x-aspnetmvc-version": "ASP.NET MVC",
    "x-generator": "generator",
    "x-drupal-cache": "Drupal",
    "x-varnish": "Varnish",
}

# (header, substring) -> tech
_HEADER_SUBSTRINGS: list[tuple[str, str, str]] = [
    ("server", "nginx", "Nginx"),
    ("server", "apache", "Apache"),
    ("server", "cloudflare", "Cloudflare"),
    ("server", "gws", "Google Web Server"),
    ("server", "microsoft-iis", "IIS"),
    ("set-cookie", "phpsessid", "PHP"),
    ("set-cookie", "jsessionid", "Java"),
    ("set-cookie", "asp.net_sessionid", "ASP.NET"),
]

_BODY_SIGNATURES: list[tuple[str, str]] = [
    ("wp-content/", "WordPress"),
    ("wp-includes/", "WordPress"),
    ("/x.js?v=", "Next.js"),
    ("__NEXT_DATA__", "Next.js"),
    ("_nuxt/", "Nuxt.js"),
    ("data-reactroot", "React"),
    ("ng-version=", "Angular"),
    ("vue.js", "Vue.js"),
    ("jquery", "jQuery"),
    ("laravel", "Laravel"),
    ("django", "Django"),
    ("csrfmiddlewaretoken", "Django"),
    ("shopify", "Shopify"),
]


def detect(headers: dict[str, str], body: str) -> list[str]:
    found: list[str] = []

    for hdr, tech_name in _HEADER_SIGNATURES.items():
        if hdr in headers:
            found.append(tech_name)

    for hdr, sub, tech_name in _HEADER_SUBSTRINGS:
        value = headers.get(hdr, "")
        if sub in value.lower():
            found.append(tech_name)

    lowered = body[:200_000].lower()
    for sig, tech_name in _BODY_SIGNATURES:
        if sig in lowered:
            found.append(tech_name)

    # dedupe preserving order
    return list(dict.fromkeys(found))

---
name: xssi
description: Cross-site script inclusion and JSON hijacking
scope: web2
---
XSSI / JSON hijacking testing checklist:

1. Find endpoints returning sensitive JSON/JSONP or JS with user data.
2. Check if responses are served with `text/html`, `text/javascript`, or
   missing `X-Content-Type-Options`.
3. Test JSONP callbacks: can you supply a callback name to exfiltrate data?
4. Test cross-origin inclusion: `<script src>` to the endpoint and override
   `Array.prototype`/`Object.prototype` setters to steal data.
5. Look for identifiers (Japan-style) leaking through scripts.
6. Check CORS misconfig that allows reading the response directly.

## References

- Plain text considered harmful (XSSI) — http://balpha.de/2013/02/plain-text-considered-harmful-a-cross-domain-exploit/
- JSON hijacking for the modern web — http://blog.portswigger.net/2016/11/json-hijacking-for-modern-web.html
- OWASP XSSI — https://www.owasp.org/images/f/f3/Your_Script_in_My_Page_What_Could_Possibly_Go_Wrong_-_Sebastian_Lekies%2BBen_Stock.pdf
- Japan identifier-based XSSI attacks — http://www.mbsd.jp/Whitepaper/xssi.pdf

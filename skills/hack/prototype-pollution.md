---
name: prototype-pollution
description: Prototype pollution testing for JavaScript stacks. Use when user input is merged into objects (query parsers, JSON bodies, deep assign), when configuring libraries via untrusted keys, or when hunting RCE gadgets via polluted Object.prototype in Node or the browser.
scope: web2
---
Prototype pollution testing for JavaScript stacks. Use when user input is merged into objects (query parsers, JSON bodies, deep assign), when configuring libraries via untrusted keys, or when hunting RCE gadgets via polluted Object.prototype in Node or the browser.

# SKILL: Prototype Pollution — Expert Attack Playbook

> **AI LOAD INSTRUCTION**: Expert prototype pollution for client and server JS. Covers __proto__ vs constructor.prototype, merge-sink detection, Express/qs-style black-box probes, and gadget chains (EJS, Timelion-class patterns, child_process/NODE_OPTIONS). Assumes you know object spread and prototype inheritance — focus is on **parser behavior** and **post-pollution sinks**.

Routing note: prioritize PP when you see deep merges, recursive assign, JSON.parse followed by Object.assign, or URL queries converted to nested objects.

## 0. QUICK START

### Client-side first probes

#__proto__[polluted]=1
#__proto__[polluted]=polluted
#constructor[prototype][polluted]=1

When input can reflect into DOM or framework routing, pair with alert(1) / console checks to observe whether global object properties were polluted.

#__proto__[xxx]=alert(1)

### Server-side first probes（JSON / form）

{"__proto__":{"polluted":true}}

{"constructor":{"prototype":{"polluted":true}}}

After sending, check whether unrelated follow-up responses show abnormal headers/status/JSON spacing, or whether app logic reads Object.prototype.polluted (see §3 detection table).

### Quick boolean

If target code uses lodash.merge, deep-extend, hoek.applyToDefaults, or some qs/query-string configurations, **raise priority**.

---

## 1. MECHANISM

**Prototype chain**: when accessing obj.key, if obj lacks own property key, lookup walks up [[Prototype]] until Object.prototype.

**__proto__**: many parsers treat literal key __proto__ as a magic path that attaches child properties to the prototype. Merging { "__proto__": { "x": 1 } } can be equivalent to Object.prototype.x = 1 depending on implementation and patch level.

**constructor.prototype**: constructor typically points to the object's constructor function; constructor.prototype is that constructor's prototype object. For plain objects this usually links to Object.prototype. Example path:

{"constructor":{"prototype":{"polluted":1}}}

This is not always equivalent to __proto__ (filtering, JSON parsing, Bun/Node differences), so **test both paths**.

**Core issue**: this is not just "one extra parameter"; in non-isolated merge lo
...

## References
- Source: https://github.com/yaklang/hack-skills/blob/main/skills/prototype-pollution/SKILL.md
- License: MIT — Copyright (c) 2026 VillanCh
- Distilled for bbhunter by scripts/import_hack_skills.py

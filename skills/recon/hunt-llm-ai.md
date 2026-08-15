---
name: hunt-llm-ai
description: Hunt LLM/AI feature bugs — prompt injection, indirect injection, exfiltration viatool-use/markdown, ASCII smuggling, agentic AI security (OWASP Agentic Apps 2026, ASI01-ASI10). Patterns: direct injection ('ignore previous instructions'), indirect injection via documents/web pages/email the model reads, ASCII smuggling (Unicode Tags block U+E0000-U+E007F, invisible to humans, decoded by the model),tool-use exfiltration (model has fetch/browse tool, attacker injects OOB URL, model exfils chat history/secrets), markdown-image zero-click exfil, system-prompt extraction, IDOR-via-AI (cross-tenant data). Targets: chatbots, RAG, summarizers, agentic copilots, MCPtools. Detection: any LLM-backed endpoint, doc upload triggering AI processing, autonomous agent withtools. Validate: OOB/Collaborator callback for exfil, verbatim-reproducible system-prompt leak (run twice), verifiable cross-tenant leak or RCE. Confabulation is NOT a finding. Use when hunting AI features, chatbots, RAG, agentic systems, MCP.
scope: web2
---
Hunt LLM/AI feature bugs — prompt injection, indirect injection, exfiltration viatool-use/markdown, ASCII smuggling, agentic AI security (OWASP Agentic Apps 2026, ASI01-ASI10). Patterns: direct injection ('ignore previous instructions'), indirect injection via documents/web pages/email the model reads, ASCII smuggling (Unicode Tags block U+E0000-U+E007F, invisible to humans, decoded by the model),tool-use exfiltration (model has fetch/browse tool, attacker injects OOB URL, model exfils chat history/secrets), markdown-image zero-click exfil, system-prompt extraction, IDOR-via-AI (cross-tenant data). Targets: chatbots, RAG, summarizers, agentic copilots, MCPtools. Detection: any LLM-backed endpoint, doc upload triggering AI processing, autonomous agent withtools. Validate: OOB/Collaborator callback for exfil, verbatim-reproducible system-prompt leak (run twice), verifiable cross-tenant leak or RCE. Confabulation is NOT a finding. Use when hunting AI features, chatbots, RAG, agentic systems, MCP.

- **Prompt injection without data exfiltration** — making the LLM say "hacked" is not a vulnerability. Need data exfiltration, tool misuse, or downstream impact.
- **Indirect prompt injection vs direct** — indirect (via ingested documents) is harder to demonstrate. Need the document to be processed and the response to reach the victim.
- **Hallucination as "information disclosure"** — LLMs hallucinate. Fabricated data is not a real information disclosure.
- **Tool calling without sensi
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-llm-ai/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

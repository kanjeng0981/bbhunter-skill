---
name: hunt-mcp-security
description: Hunt Model Context Protocol (MCP) vulnerabilities in AI-tool integration systems.
scope: web2
---
Hunt Model Context Protocol (MCP) vulnerabilities in AI-tool integration systems.

- Target deploys AI agents with MCP tool access (Claude Desktop MCP, Cursor AI tools, custom agent frameworks).
- AI agent can invoke tools (database queries, file operations, API calls, web searches).
- Tool registration, schema validation, or access control logic is present.
- Need to test whether tool outputs can inject prompts back into the agent.
- Target uses RAG (Retrieval Augmented Generation) with external data sources.

- **MCP is a protocol standard, not an implementation.** Each MCP server may have different tool schemas and access patterns. Map the tool catalog first.
- **Tool output poisoning requires the agent to process the output.** If the agent just displays tool results to the user, the impact is lower than if it acts on them.
- **Not every unauthenticated tool is a finding.** Sometools are intentionally public (weather, news, public APIs). Focus ontools that access internal data or perform state-changing operations.
- **MCP tool schemas are self-documenting.** The /tools endpoint often reveals all available functions. Use this to map the attack surface before testing.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-mcp-security/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py

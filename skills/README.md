# Skills

Drop Markdown files here to teach the agent domain-specific playbooks.
Every skill is injected into the LLM prompts during contract analysis and
finding triage.

Format (frontmatter is optional):

```markdown
---
name: web3-reentrancy
description: Deep-dive checklist for reentrancy in Solidity
---
1. Check all external calls for CEI (checks-effects-interactions) violations.
2. Look for missing `nonReentrant` modifiers on state-changing functions.
...
```

Use `bbhunter skills` to list loaded skills.

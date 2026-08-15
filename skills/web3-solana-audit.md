---
name: web3-solana-audit
description: Solana/Anchor program audit — 6 critical vulnerability patterns (Trail of Bits)
scope: web3
---
Solana / Anchor program audit — check these 6 critical patterns:

1. **Arbitrary CPI (critical)**: user-controlled program IDs in
   `invoke`/`invoke_signed` without validating the target program. Anchor:
   use `Program<'info, T>` to auto-validate the program ID.
2. **Improper PDA validation (critical)**: using `create_program_address`
   without the canonical bump, or accepting a user-provided bump. Use
   `find_program_address()` or Anchor `seeds` constraints and store/reuse the
   bump.
3. **Missing ownership check (high)**: deserializing an account
   (`try_from_slice`/`try_deserialize`) without validating
   `account.owner == expected_program_id`. Anchor: `Account<'info, T>`.
4. **Missing signer check (critical)**: authority operations without
   `account.is_signer` validation. Anchor: `Signer<'info>`.
5. **Sysvar account spoofing (high)**: trusting sysvar accounts that were not
   validated (pre-Solana 1.8.1); use checked sysvar access.
6. **Improper instruction introspection (medium)**: absolute instruction
   indexes that allow reuse; use `load_instruction_at_checked` and relative
   indexing.

Report each finding with file/line, vulnerable code, attack scenario, and a
concrete fix.

## References

- Source: https://github.com/trailofbits/skills/blob/main/plugins/building-secure-contracts/skills/solana-vulnerability-scanner/SKILL.md
- License: CC-BY-SA-4.0 (Trail of Bits). This file is a condensed summary of
  the upstream skill for use in bbhunter. See the upstream SKILL.md for the
  full vulnerability-pattern documentation and code examples.

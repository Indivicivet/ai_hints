---
name: avoid-those-mistakes
description: Analyze user corrections, mistaken agent actions, or flawed prompt/skill instructions, identify the failure mode, and update governing skills or AGENTS.md.
---

# Avoid those mistakes

Diagnose why the agent went astray—whether due to ambiguous prompting, bad skill guidance, or model overreach—and refine the governing rules or skills to prevent recurrence.

## Core mindset

1. Treat user pushback as a failure of prompt constraints, skill design, or agent judgment, not just a rejected edit.
2. Distinguish between syntax/layout formatting and structural code changes. Do not rewrite control flow when asked to adjust formatting layout.
3. Update the permanent instructions (`skills/<skill>/SKILL.md` or `rules/AGENTS.md`) so the mistake cannot repeat.

## Diagnosis steps

When the user points out agent mistakes or poor interventions:

1. **Classify the failure source**:
   - **Instruction overreach / ambiguity**: Did the prompt or skill encourage aggressive intervention without boundary guards? (e.g., Telling an agent to "fix awkward layout" without forbidding semantic rewrites like turning expressions into `if`/`elif`/`else` blocks).
   - **Agent over-eagerness**: Did the agent invent problems to solve, alter readable code unnecessarily, or break locality of inline comments?
   - **Prompt gap**: Did the user's prompt assume domain taste that was never articulated?
2. **Review the specific counter-examples**:
   - Compare what was asked versus what the agent actually overreached on or touched.
3. **Formulate the remediation**:
   - If an existing skill gave bad incentives, edit that skill's rules and anti-patterns immediately.
   - If repo-level guidance was violated or lacking, propose targeted additions to `AGENTS.md`.
   - If the user's prompting style has an avoidable pitfall, explain the failure mechanism directly and suggest prompt phrasing or triggers.

## Refining rules and skills

- **Negative constraints over vague goals**: State strictly what the agent is forbidden from doing.
- **Good examples and tricks**: Anchor on exact snippets or techniques that worked, rather than vague praise that can trigger unsolicited rewrites elsewhere.

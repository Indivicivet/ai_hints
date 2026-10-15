---
name: avoid-those-mistakes
description: Analyze user corrections, mistaken agent actions, or flawed prompt/skill instructions, identify the failure mode, and update governing skills or AGENTS.md. Use only when explicitly invoked via /avoid-those-mistakes or instructed to update skills based on an agent mistake.
---

# Avoid those mistakes

Diagnose why the agent went astray—whether due to ambiguous prompting, bad skill guidance, or model overreach—and refine the governing rules or skills to prevent recurrence.

## Core mindset

1. Treat user pushback as a failure of prompt constraints, skill design, or agent judgment, not just a rejected edit.
2. Update the permanent instructions (`skills/<skill>/SKILL.md` or `rules/AGENTS.md`) with explicit negative constraints so the mistake cannot repeat.

## Diagnosis steps

When investigating an agent mistake or poor intervention:

1. **Classify the failure source**:
   - **Instruction overreach / ambiguity**: Did the prompt or skill encourage aggressive intervention without boundary guards? (e.g. telling an agent to "fix awkward layout" without forbidding semantic rewrites like converting expressions to `if`/`elif`/`else` blocks).
   - **Agent over-eagerness**: Did the agent invent problems to solve, alter readable code unnecessarily, or break locality of inline comments?
   - **Prompt gap**: Did the user's prompt assume domain taste that was never articulated?
2. **Review the specific counter-examples**:
   - Compare what was asked versus what the agent actually overreached on or touched.
3. **Formulate the remediation**:
   - If an existing skill gave bad incentives, edit that skill's rules and anti-patterns directly.
   - If repo-level guidance was violated or lacking, edit `rules/AGENTS.md`.
   - If the user's prompting style has an avoidable pitfall, explain the failure mechanism directly and suggest prompt phrasing or triggers.
   - Explicitly report the exact rule additions or modifications made to the user.

## Refining rules and skills

- **Negative constraints over vague goals**: State strictly what the agent is forbidden from doing.
- **Good examples and tricks**: Anchor on exact snippets or techniques that worked, rather than vague praise that can trigger unsolicited rewrites elsewhere.

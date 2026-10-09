---
name: refine-from-feedback
description: Analyze user corrections, mistaken agent actions, or flawed prompt/skill instructions, identify the failure mode, and update governing skills or AGENTS.md.
---

# Refine from feedback

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
   - Note what Black / the tool did versus what the agent did.
   - Respect developer ergonomics: inline commented-out code (like `# * 4`), single-expression evaluations that avoid mutable variables, and localized comments must not be destroyed in pursuit of "flat" lines.
3. **Formulate the remediation**:
   - If an existing skill gave bad incentives, edit that skill's rules and anti-patterns immediately.
   - If repo-level guidance was violated or lacking, propose targeted additions to `AGENTS.md`.
   - If the user's prompting style has an avoidable pitfall, explain the failure mechanism directly and suggest prompt phrasing or triggers.

## Refining rules and skills

- **Negative constraints over positive goals**: Tell the agent what it is strictly forbidden from doing (e.g., "Do not convert expressions to if/else blocks or introduce new temporary variables").
- **Preserve comment locality**: Comments describing a specific clause or containing toggleable code (e.g. `foo  # * 2`) must stay inline with that clause, not be hoisted above the entire statement.
- **Run Black**: Run `python -m black .` after editing any Python rules or examples.

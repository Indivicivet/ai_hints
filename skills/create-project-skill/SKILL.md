---
name: create-project-skill
description: Draft a project-specific skill inside the current workspace repository. Use when teaching the agent local build or testing commands, and repository conventions.
---

# Create project skill

Add a project-scoped skill to the active repository.

## Location

Write the file to `<project-root>/.agents/skills/<skill-name>/SKILL.md`. If the repository already keeps skills in `<project-root>/skills/` and has them configured, follow that existing pattern instead.

## Instructions

1. Read `skill-writing`: You MUST read the `skill-writing` skill before drafting. Apply its core test: only write opinions and constraints that counteract default model habits.
2. Ground in the codebase: Inspect existing build configs, test scripts, or task runners first. Hardcode exact paths, flags, commands, and expected outputs.
3. Separate rules from procedures: If the instruction is a passive constraint or coding standard, put it in `.agents/rules/` or `AGENTS.md` instead of a skill. Use skills for executable workflows and runbooks.

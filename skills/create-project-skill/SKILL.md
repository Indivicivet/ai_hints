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
2. Consider what context you have about the project that a fresh agent wouldn't, e.g. what you've been working on.
3. Ground in the codebase: Inspect existing build configs, test scripts first. Hardcode exact paths, flags, commands, and expected outputs.
4. Scope appropriately: Put broad-scope project invariants in `AGENTS.md`. Use skills for specific aspects of the project, or multi-step procedures that only need to load when relevant to the task.

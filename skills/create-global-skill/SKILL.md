---
name: create-global-skill
description: Draft a global skill in the ai_hints repository, regardless of active workspace. Use when creating a reusable rule or habit that applies everywhere.
---

# Create global skill

Add a cross-project skill to the ai_hints repository.

## Location

Locate this skill file's path (provided in the system prompt under available skills for `create-global-skill`). Walk up two directories from `create-global-skill/SKILL.md` to find the root of `ai_hints`. Write the new skill to `<ai_hints_root>/skills/<skill-name>/SKILL.md`.

Do not write to the current workspace root unless it happens to be `ai_hints`. Even when invoked inside another project, target `<ai_hints_root>` directly.

## Instructions

1. Read `skill-writing`: You MUST read `<ai_hints_root>/skills/skill-writing/SKILL.md` before drafting. Apply its core test: only write opinions and constraints that counteract default model habits.
2. Keep it universal: Do not mention paths, database schemas, or build tools specific to your active project. If a rule relies on local context outside `ai_hints`, it belongs in `create-project-skill`.
3. Register the skill: After creating the file, add an entry to `<ai_hints_root>/README.md` under the Custom Skills list.

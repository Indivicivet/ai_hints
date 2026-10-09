---
name: create-global-skill
description: Draft a cross-cutting, personal skill in the ai_hints repository, regardless of active workspace. Use when creating a reusable rule or habit that applies everywhere.
---

# Create global skill

Add a cross-project skill to the personal plugin repository.

## Location

Locate this skill file's path (provided in the system prompt under available skills for `create-global-skill`). Walk up two directories from `create-global-skill/SKILL.md` to find the root of `ai_hints`. Write the new skill to `<ai_hints_root>/skills/<skill-name>/SKILL.md`.

Do not write to the current workspace root unless it happens to be `ai_hints`. Even when invoked inside another project, target `<ai_hints_root>` directly.

## Rules

Follow general `skill-writing` guidelines.

Keep it universal. Omit project-specific paths, or repository tooling outside of `ai_hints`.

After creating the file, register it in `<ai_hints_root>/README.md` under the custom skills section.

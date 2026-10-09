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

1. Keep it universal. Omit project-specific paths, or repository tooling outside of `ai_hints`.
2. Override default model behavior. If an unprompted model already does it, do not write the skill. Target a specific bad habit or patterns the user doesn't approve of. If your first idea of what the skill looks like is your natural output, ask the user what you want to differ, and only include the difference in the skill.
3. Keep descriptions under three lines. State the exact trigger cues so the runtime loads it when needed and ignores it otherwise.
4. Keep instructions short and imperative. Do not write tutorials or language syntax overviews. Do not write full descriptions of entire systems that should be in a human-targeted README file instead.
5. After creating the file, register it in `<ai_hints_root>/README.md` under the custom skills section.

---
name: skill-writing
description: Draft, review, or refine an agent skill. Use when turning guidelines or habits into a skill, or improving existing skills.
---

# Skill writing

Skills inject opinions, counteract model blind spots, and enforce non-obvious taste. A skill is not a manual for things the model already knows. If an unprompted model does it anyway, cut it.

## The core test

Before writing, identify what an unprompted model does wrong here, and what opinion or constraint overrides that. If your first idea looks like default model output, ask the user what should differ, and only put that difference in the skill.

If the skill lacks an opinion that contradicts default LLM habits, it does not need to exist.

## Rules for drafting

1. Keep it short. Instructions load into context on every use. Write direct imperatives.
2. Target specific model habits: Name the exact anti-pattern to stop and forbid it directly.
3. Write sharp trigger descriptions: The description dictates when the skill loads. Name the exact cues, impulses, commands, or file patterns.
4. Do not write tutorials. Do not explain entire systems that belong in a project README. If tempted, suggest writing a README instead.
5. Apply the `unslop` skill.

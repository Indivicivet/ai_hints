---
name: skill-writing
description: Draft, review, or refine an agent skill. Use when turning guidelines or habits into a skill, or improving existing skills.
---

# Skill writing

Skills inject opinions, counteract model blind spots, and enforce non-obvious taste. A skill is not a manual for things the model already knows. If a base model does it anyway, cut it.

## The core test

Before writing, figure out: what does an unprompted model do wrong here, and what opinion, guideline or piece of information overrides that? Has the user made it clear, or is it clear from the current model context that a fresh agent won't see?

If the skill lacks an opinion that contradicts default LLM habits, it does not need to exist.

## Rules for drafting

Keep it short, because instructions load into context on every use. Write direct imperatives.

Target specific model habits: Name the exact anti-pattern to stop and forbid it directly.

Write sharp trigger descriptions: The description dictates when the skill loads. Name the exact cues, impulses, commands, or file patterns. Think about whether this works as a model invocable skill or whether the user only wants this specific behaviour when requested; if so, use `disable-model-invocation: true`.
   
Do not write tutorials. Do not write full descriptions of entire systems that should be in a human-targeted README file instead. If you are tempted to do so, you can consider suggesting to the user that we write a README instead.
   
Use the `unslop` skill.

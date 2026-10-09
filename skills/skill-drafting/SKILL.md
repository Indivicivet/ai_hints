---
name: skill-drafting
description: Draft, review, or refine an agent skill. Use when creating a new skill, turning guidelines or habits into a skill, or stripping slop and bloat from existing skills.
---

# Skill drafting

Skills inject opinions, counteract model blind spots, and enforce non-obvious taste. A skill is not a manual for things the model already knows. If a base model does it anyway, cut it.

## The core test

Before writing, answer: what does an unprompted model do wrong here, and what hard opinion overrides that?

- "Explain how to write Python." Worthless.
- "Assume everything is installed; never run pre-flight imports." High leverage.
- "Pair every slider with a spinbox and kill the mouse wheel." High leverage.
- "Don't paper over crashes with nil checks." High leverage.

If the skill lacks an opinion that contradicts default LLM habits, it does not need to exist.

## Rules for drafting

1. Strip generic documentation: Omit basic syntax, standard library overviews, and file layouts. The model already knows them. Give it the decisions, not the manual.
2. Target specific model habits: Name the exact anti-pattern to stop (such as pre-flight checks, speculative layers, defensive nil-checks, or hedging) and forbid it directly.
3. Keep it terse: Instructions load into context on every use. Write direct imperatives. Cut introductory throat-clearing and disclaimers.
4. Write sharp trigger descriptions: The frontmatter description dictates when the skill loads. Name the exact cues, impulses, commands, or file patterns. Vague triggers either never fire or pollute every turn.
5. Separate principles from procedures:
   - Invariant guidelines (such as laziness or root-cause discipline) set `disable-model-invocation: true`.
   - Procedures (such as grilling or transcribe) outline strict steps and exit.
6. Cut AI tells: Follow the rules in `unslop`. No filler words, no decorative markup, and no sycophantic framing.

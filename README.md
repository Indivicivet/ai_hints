# AI Hints

Developer rules, formatting standards, and pair-programming skills.

## Gemini Setup

~/.gemini/config/plugins.json:
{
  "entries": [
    {
      "path": "... repo folder ..."
    }
  ]
}

and add "... repo folder .../" to Antigravity settings -> General -> File Access Rules

## User-invoked

- **[grill-me](./skills/grill-me/SKILL.md)**: Relentless interview to resolve every branch of a design tree.
- **[wait-what](./skills/wait-what/SKILL.md)**: Re-pitch the last message in plain English with missing context.
- **[principle-fix-root-causes](./skills/principle-fix-root-causes/SKILL.md)**: Trace bugs to root cause; no symptom-guard band-aids.
- **[principle-laziness-protocol](./skills/principle-laziness-protocol/SKILL.md)**: Minimal diffs, flat call chains, and deletion over addition.
- **[principle-minimize-reader-load](./skills/principle-minimize-reader-load/SKILL.md)**: Fewer layers of indirection and reduced mutable state.

## Model-invoked

- **[assume-installed](./skills/assume-installed/SKILL.md)**: Assume packages are installed without pre-flight checks.
- **[bro](./skills/bro/SKILL.md)**: Restate the last message in plain language with no jargon.
- **[grilling](./skills/grilling/SKILL.md)**: Stress-test plans and assumptions through structured questions.
- **[research](./skills/research/SKILL.md)**: Investigate questions against primary sources with direct citations.
- **[unslop](./skills/unslop/SKILL.md)**: Cut AI tells, fluff, and puffery from writing.

## Sources

Many skills are sourced, and sometimes adapted, from [pstack](https://github.com/poteto/pstack) and [mattpocock/skills](https://github.com/mattpocock/skills).

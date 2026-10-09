# AI Hints

Developer rules, formatting standards, and pair-programming skills.

## Gemini Setup

~/.gemini/config/plugins.json:
```
{
  "entries": [
    {
      "path": "... repo folder ..."
    }
  ]
}
```

and add "... repo folder .../" to Antigravity settings -> General -> File Access Rules

## pstack Skills

Engineering principles and discipline adapted from [pstack](https://github.com/cursor/plugins/tree/main/pstack) (Lauren Tan / `@poteto`):

- **[bro](./skills/bro/SKILL.md)**: Restate the last message in plain language with no jargon. *(Identical to upstream)*
- **[principle-fix-root-causes](./skills/principle-fix-root-causes/SKILL.md)**: Trace bugs to root cause; no symptom-guard band-aids. *(Identical text; unslopt header bolding)*
- **[principle-guard-the-context-window](./skills/principle-guard-the-context-window/SKILL.md)**: Route bulk payloads to subagents; keep context window clean. *(Identical to upstream)*
- **[principle-laziness-protocol](./skills/principle-laziness-protocol/SKILL.md)**: Minimal diffs, flat call chains, and deletion over addition. *(Identical text; unslopt header bolding)*
- **[principle-minimize-reader-load](./skills/principle-minimize-reader-load/SKILL.md)**: Fewer layers of indirection and reduced mutable state. *(Identical text; unslopt header bolding)*
- **[unslop](./skills/unslop/SKILL.md)**: Cut AI tells, fluff, and puffery from writing. *(Diverged: adapted rules around bolding, colons, em dashes, shorthand like e.g./i.e., and streamlined guidelines)*

## Matt Pocock Skills

Workflows and feedback loops adapted from [mattpocock/skills](https://github.com/mattpocock/skills):

- **[grilling](./skills/grilling/SKILL.md)**: Stress-test plans and assumptions through structured design-tree interview rounds. *(Diverged: cleaned formatting/unicode artefacts, consolidated standalone prompt)*
- **[research](./skills/research/SKILL.md)**: Investigate questions against primary sources with direct citations. *(Identical to upstream)*
- **[wait-what](./skills/wait-what/SKILL.md)**: Re-pitch the last message in plain English with missing context. *(Identical to upstream)*

## Custom & Project-Specific Skills

Skills developed specifically for this environment and workflow:

- **[assume-installed](./skills/assume-installed/SKILL.md)**: Assume packages and libraries are installed without pre-flight check commands.
- **[clang-format-black](./skills/clang-format-black/SKILL.md)**: Format C/C++ (and supported languages) using clang-format with a black-esque style configuration.
- **[desktop-gui](./skills/desktop-gui/SKILL.md)**: Guidelines for building desktop GUIs (PySide6 default, slider-spinbox sync, theme safety).
- **[direct-web-cite](./skills/direct-web-cite/SKILL.md)**: Verify and extract verbatim quotes from live web pages as unmanipulated HTML citations.
- **[mathematical-audience](./skills/mathematical-audience/SKILL.md)**: Frame technical concepts for a mathematically experienced reader without assuming niche domain vocabulary.
- **[pitch-higher](./skills/pitch-higher/SKILL.md)**: Nudge the last explanation a step higher in assumed competence and density.
- **[pitch-lower](./skills/pitch-lower/SKILL.md)**: Nudge the last explanation a step lower in assumed background, unpacking jargon and steps.
- **[sort-out-imports](./skills/sort-out-imports/SKILL.md)**: Tidy Python imports via isort and enforce explicit namespace imports.
- **[transcribe](./skills/transcribe/SKILL.md)**: Extract image text with optional kana reading/pronunciation (`ro`), translation (`tl`), and nuance explanation (`explain`).

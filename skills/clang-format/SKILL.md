---
name: clang-format-black
description: Format C, C++, C#, Java, JavaScript, JSON, or Proto files using clang-format with black-esque style.
---

# Clang Format

Format code files matching clang-format supported languages (C/C++, Java, JavaScript, C#, Proto, JSON) across any project using this skill's bundled [.clang-format](./.clang-format).

## Usage

When asked to run or apply `clang-format` on target files:

1. Resolve the path to this skill's [.clang-format](./.clang-format) file (located in the same directory as this `SKILL.md`).
2. Run `clang-format` in-place (`-i`), passing the resolved configuration path via `--style=file:<path-to-skill-dir>/.clang-format>`:

```powershell
clang-format -i --style=file:"<path-to-this-skill-dir>/.clang-format" <path-to-file>
```

## Options

- In-place modification: `-i`
- Verification / dry-run only: `--dry-run --Werror`

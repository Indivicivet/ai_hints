"""Register skills and instructions for Claude Code."""

import argparse
from pathlib import Path
import sys

root = Path(__file__).resolve().parent
claude_dir = Path.home() / ".claude"
skills_src = root / "skills"
skills_dest = claude_dir / "skills"

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument(
    "--individual",
    action="store_true",
    help="Symlink each skill individually into ~/.claude/skills/<skill-name>",
)
args = parser.parse_args()


def link(src: Path, dest: Path) -> None:
    if dest.is_symlink() or dest.is_junction():
        dest.unlink()
    elif dest.is_dir():
        if any(dest.iterdir()):
            if not args.individual:
                sys.exit(
                    f"\nError: {dest} already exists and is not empty.\n"
                    "Run with --individual to link alongside existing skills."
                )
            print(f"Skipping {dest.name}: directory already exists.")
            return
        dest.rmdir()
    elif dest.exists():
        dest.unlink()

    dest.symlink_to(src, target_is_directory=True)
    print(f"Linked {src.name} -> {dest}")


claude_dir.mkdir(parents=True, exist_ok=True)

if args.individual:
    skills_dest.mkdir(parents=True, exist_ok=True)
    for skill in sorted(skills_src.iterdir()):
        if skill.is_dir():
            link(skill, skills_dest / skill.name)
else:
    link(skills_src, skills_dest)

claude_md = claude_dir / "CLAUDE.md"
reference = f"@{(root / 'rules' / 'AGENTS.md').as_posix()}"
content = claude_md.read_text(encoding="utf-8") if claude_md.exists() else ""

if reference not in content:
    separator = "\n" if content and not content.endswith("\n") else ""
    claude_md.write_text(f"{content}{separator}{reference}\n", encoding="utf-8")
    print(f"Added reference to {claude_md}")
else:
    print(f"Reference already present in {claude_md}")

"""Register skills and instructions for Claude Code."""

import argparse
from pathlib import Path

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


def link_dir(src_dir: Path, target_dir: Path) -> None:
    if target_dir.is_symlink() or target_dir.is_junction():
        target_dir.unlink()
    elif target_dir.is_dir():
        print(f"Skipping {target_dir.name}: directory already exists.")
        return
    elif target_dir.exists():
        target_dir.unlink()
    target_dir.symlink_to(src_dir, target_is_directory=True)
    print(f"Linked {src_dir.name} -> {target_dir}")


claude_dir.mkdir(parents=True, exist_ok=True)

if args.individual:
    skills_dest.mkdir(parents=True, exist_ok=True)
    for skill in sorted(skills_src.iterdir()):
        if skill.is_dir():
            link_dir(skill, skills_dest / skill.name)
else:
    link_dir(skills_src, skills_dest)

claude_md = claude_dir / "CLAUDE.md"
reference_line = f"@{(root / 'rules' / 'AGENTS.md').as_posix()}"
content = claude_md.read_text(encoding="utf-8") if claude_md.exists() else ""

if reference_line not in content:
    with claude_md.open("a", encoding="utf-8") as f:
        if content and not content.endswith("\n"):
            f.write("\n")
        f.write(reference_line + "\n")
    print(f"Added reference to {claude_md}")
else:
    print(f"Reference already present in {claude_md}")

"""Register skills and instructions for Claude Code."""

from pathlib import Path

root = Path(__file__).resolve().parent
home = Path.home()
claude_dir = home / ".claude"
skills_src = root / "skills"
skills_dest = claude_dir / "skills"
claude_md = claude_dir / "CLAUDE.md"
agents_md = root / "rules" / "AGENTS.md"

claude_dir.mkdir(parents=True, exist_ok=True)
skills_dest.mkdir(parents=True, exist_ok=True)


def link_skill(src_dir: Path, target_dir: Path) -> None:
    if target_dir.is_symlink() or target_dir.is_junction():
        target_dir.unlink()
    elif target_dir.is_dir():
        # If target exists as normal directory, don't silently overwrite
        print(f"Skipping {target_dir.name}: directory already exists.")
        return
    elif target_dir.exists():
        target_dir.unlink()
    target_dir.symlink_to(src_dir, target_is_directory=True)
    print(f"Symlinked {src_dir.name} -> {target_dir}")


for skill in sorted(skills_src.iterdir()):
    if skill.is_dir():
        link_skill(skill, skills_dest / skill.name)

agents_path_str = agents_md.as_posix()  # forward slashes
reference_line = f"@{agents_path_str}"

if not claude_md.exists() or not claude_md.read_text(encoding="utf-8").strip():
    claude_md.write_text(reference_line + "\n", encoding="utf-8")
    print(f"Created {claude_md} with reference to {agents_path_str}")
else:
    content = claude_md.read_text(encoding="utf-8")
    if reference_line not in content:
        separator = "" if content.endswith("\n") else "\n"
        claude_md.write_text(
            content + separator + reference_line + "\n", encoding="utf-8"
        )
        print(f"Appended reference to {claude_md}")
    else:
        print(f"Reference already present in {claude_md}")

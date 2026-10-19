"""Link this repository's AGENTS.md into Codex's global instructions."""

from pathlib import Path


root = Path(__file__).parent
agents_path = Path.home() / ".codex" / "AGENTS.md"

if agents_path.exists() and agents_path.read_text().strip():
    raise RuntimeError(
        f"Existing Codex instructions:\n{agents_path}\n\n"
        f"{agents_path.read_text()}\n"
        "Delete or merge this file yourself, then run this script again."
    )

agents_path.unlink(missing_ok=True)
agents_path.parent.mkdir(parents=True, exist_ok=True)
agents_path.hardlink_to(root / "rules" / "AGENTS.md")

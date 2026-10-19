"""Register this plugin in Codex's personal marketplace."""

from pathlib import Path
from subprocess import run


root = Path(__file__).parent
agents_path = Path.home() / ".codex" / "AGENTS.md"
run(["codex", "plugin", "marketplace", "add", str(root)], check=True)
print(f"Registered ai-hints marketplace at {root}")

if agents_path.exists() and agents_path.read_text().strip():
    raise RuntimeError(
        f"Existing Codex instructions:\n{agents_path}\n\n"
        f"{agents_path.read_text()}\n"
        "Delete or merge this file yourself, then run this script again."
    )

agents_path.unlink(missing_ok=True)
agents_path.parent.mkdir(parents=True, exist_ok=True)
agents_path.hardlink_to(root / "rules" / "AGENTS.md")

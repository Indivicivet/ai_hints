"""Register this plugin in Codex's personal marketplace."""

import json
from pathlib import Path
from shutil import copytree, ignore_patterns


root = Path(__file__).parent
home = Path.home()
marketplace_path = home / ".agents" / "plugins" / "marketplace.json"
agents_path = home / ".codex" / "AGENTS.md"
plugin_path = home / ".codex" / "plugins" / "ai-hints"

marketplace_path.parent.mkdir(parents=True, exist_ok=True)
copytree(root, plugin_path, dirs_exist_ok=True, ignore=ignore_patterns(".git"))
marketplace = {"name": "personal-local", "plugins": []}
if marketplace_path.exists():
    marketplace = json.loads(marketplace_path.read_text())

marketplace["plugins"] = [
    plugin for plugin in marketplace["plugins"] if plugin["name"] != "ai-hints"
]
marketplace["plugins"].append(
    {
        "name": "ai-hints",
        "source": {"source": "local", "path": "./.codex/plugins/ai-hints"},
        "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
        "category": "Productivity",
    }
)
marketplace_path.write_text(json.dumps(marketplace, indent=2) + "\n")
print(f"Registered ai-hints in {marketplace_path}")

if agents_path.exists() and agents_path.read_text().strip():
    raise RuntimeError(
        f"Existing Codex instructions:\n{agents_path}\n\n"
        f"{agents_path.read_text()}\n"
        "Delete or merge this file yourself, then run this script again."
    )

agents_path.unlink(missing_ok=True)
agents_path.parent.mkdir(parents=True, exist_ok=True)
agents_path.hardlink_to(root / "rules" / "AGENTS.md")

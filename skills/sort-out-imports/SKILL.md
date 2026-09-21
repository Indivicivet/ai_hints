---
name: sort-out-imports
description: Tidy up imports in current Python work and make them explicit.
---

Firstly call isort; if working in a directory, just directly call `python -m isort --profile black .`. If working only on specific files, then you can call with `python -m isort --profile black <file path>`. This will order imports into stdlib, thirdparty, firstparty, localfolder.

Next, address any `from` imports in firstparty, and replace these with explicit imports; for example `from core_engine import Engine` should be replaced by `import core_engine`, and references to `Engine` should become `core_engine.Engine`, and so forth.

Exception: things like `from tqdm import tqdm` is fine, since the resulting `tqdm` local clearly indicates which package it's from. e.g. `from pathlib import Path` is completely fine. To clarify, it is acceptable to do a `from` import if things stay in a representative namespace rather than polluting locals, e.g. `from PIL import Image` is completely fine, since this is called as `Image.open`.

The key idea is to keep things in a sensible namespace. You may also address firstparty and stdlib if it's not obvious to an experienced user where the imported locals come from.

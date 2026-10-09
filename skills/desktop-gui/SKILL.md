---
name: desktop-gui
description: Guidelines for building desktop GUIs. Default to PySide6 (or Qt if C++ required). Use when creating or editing desktop user interfaces.
---

# Desktop GUI

## Frameworks
- Default to Python with PySide6. Assume PySide6 is already installed.
- For C++, use Qt. Assume it is at `C:/Qt/` by default. If not found there, check most common locations, and otherwise ask the user for their install path.

## Controls
- Pair every slider with a synced numeric spin box (`QSpinBox` or `QDoubleSpinBox`). Make sure the spinbox is big enough to fit enough digits.
- Disable the mouse wheel on sliders so scrolling past them never alters their values (install an event filter or ignore `wheelEvent`).
- Avoid dropdowns for cases where you only have a few, known options. It's quicker to interact with radio buttons if there are just a few categorical options. If the value is numerical, consider a slider. If the value represents something physical, such as position, consider a visual control. Only use dropdowns when there's a dynamic lits of options (e.g. files automatically detected in a folder), or a long non-numerical list that won't fit in the GUI.
- Give sliders generous ranges and sizes. Consider whether the slider's numerical values should be linear as a function of position, or not (e.g. geometric, for things like scale factors, where 0.1x and 10x are equally important).

## Colors and theming
- Avoid hardcoded background or text colors that break across light and dark modes. Rely on default system palette roles so the UI tracks the OS theme cleanly.
- If a specific fixed theme (always dark or always light) makes sense for the use case, raise it with the user first before forcing it.
- Explicit colors are allowed when the content itself demands it, such as image viewers, data visualizations, or status badges.

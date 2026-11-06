---
name: desktop-gui
description: Guidelines for building desktop GUIs. Default to PySide6 (or Qt if C++ required). Use when creating or editing desktop user interfaces.
---

# Desktop GUI

## Frameworks
- Default to Python with PySide6. Assume PySide6 is already installed.
- For C++, use Qt. Assume it is at `C:/Qt/` by default. If not found there, check most common locations, and otherwise ask the user for their install path.

## Colors and theming
- Avoid hardcoded background or text colors that break across light and dark modes. Rely on default system palette roles so the UI tracks the OS theme cleanly.
- If a specific fixed theme (always dark or always light) makes sense for the use case, raise it with the user first before forcing it.
- Explicit colors are allowed when the content itself demands it, such as image viewers, data visualizations, or status badges.

## General notes
- Use the `interaction` skill when designing controls (`QSpinBox`/`QDoubleSpinBox` synced with sliders, ignoring `wheelEvent` on sliders, and avoiding unnecessary dropdowns).
- If presenting visual information, use the `make-key-information-dominant` skill.

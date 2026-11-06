---
name: interaction
description: Choose fast, direct UI controls for user input. Use when building or editing interactive controls in GUIs, web apps, dashboards, or interactive widgets.
---

# Interaction

Pick controls that minimize clicks and give both quick adjustment and exact entry:

- Avoid dropdowns when options are few and fixed. Use radio buttons or segmented buttons for small categorical sets so options are visible and selectable in one click. Reserve dropdowns for dynamic lists (e.g. detected files) or long non-numerical lists that cannot fit inline.
- For numerical values, pair a slider with a synced numeric input box (`QSpinBox`/`QDoubleSpinBox` or number input) sized to fit all digits.
- Give sliders generous ranges and physical width. Choose scaling that matches the quantity: linear for additive values, geometric/logarithmic for ratios or scale factors (where 0.1x and 10x need equal travel).
- Disable scroll-wheel changes on sliders so scrolling a page or panel never accidentally alters a parameter.
- For spatial or physical parameters (such as 2D position, crop bounds, or regions), prefer direct manipulation on the canvas over separate abstract inputs.

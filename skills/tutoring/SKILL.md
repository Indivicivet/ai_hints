---
name: tutoring
description: Run an interactive study session alongside a textbook, course, or reading material using `course_summary.md`, `user_progress.md`, and `agent_details.md`. Use when teaching, tutoring, reviewing sections, or working through practice problems with the user.
---

# Tutoring

Act as a live study companion alongside the user's own reading of the source material. If the study folder does not yet have `course_summary.md`, `user_progress.md`, and `agent_details.md`, run `tutoring-setup` first.

## Maintaining the working files

Keep the working files in sync whenever there is a new development (finishing or starting a section, solving a problem, spotting a misconception, learning something new about the user's background, or pulling in outside material):

1. `user_progress.md`:
   - Update `## User background and preferences` on the fly as you learn what fields, notation, or prerequisites the user already knows or lacks.
   - Update `## Progress checklist` items (`- <section> | started: [ ] | understood: [ ] | reviewed: [ ] — <1-sentence note with date>`):
     - Check `started: [x]` when pre-briefing or discussing a section.
     - Check `understood: [x]` when the user is happy to move on or cleanly answers a problem on it. Use the 1-sentence note to record the actual depth (e.g., `(2026-10-26) Followed proof and solved Ex 2.4` vs `(2026-10-26) Read only, skipped exercises; shaky on boundary case`).
     - Check `reviewed: [x]` only when returning to the section in a later session, review pass, or later chapter recap.
2. `agent_details.md` (or `agent_details/chXX.md`): Treat this as a live notebook. Add new insights, record where the user got stuck, refine exercises, and append digested notes for newly reached chapters or external materials.
3. `course_summary.md`: Consult the dependency graph to see what earlier sections a new topic relies on, and update it if the scope expands.

## Teaching loop

1. Pre-brief by default: When starting a new section (unless the user says they already read it), give a short pre-briefing before they read. Supply the missing motivation and concrete examples up front, link the ideas to `## User background and preferences`, and warn about unstated assumptions or tricky notation in the text.
2. Proactive recaps: Before starting a section, check its prerequisites in `course_summary.md` against `user_progress.md`. If a required earlier concept was skipped, left un-understood, or has not been touched in a while, weave a tailored recap into the pre-briefing.
3. Enrich and connect after reading: Fill in intuition, concrete examples, and cross-disciplinary links that the author omitted. Do not merely repeat the text.
4. Socratic problem guidance by default: When talking through practice questions, proofs, or exam problems, default to Socratic guidance. If the user's idea is incomplete or slightly off, probe them to be more specific, test an edge case, or check an assumption rather than handing over the fix. Do not keep probing if the user gives a sound proof or complete answer; confirm it works and move on. Switch to direct whiteboard-colleague mode when requested or when Socratic nudges are not appropriate.
5. Assimilate extra material: If the primary text explains a topic poorly or assumes missing background, pull in outside sources or explanations and record them in `agent_details.md`.
6. High bar for interactive apps and plots: Only build an interactive widget (`generative_ui`) or plot script when geometry, dynamics, or parameter-tweaking genuinely beat equations and prose, or when the user asks for one.

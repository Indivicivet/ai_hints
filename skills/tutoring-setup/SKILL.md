---
name: tutoring-setup
description: Ingest and digest a textbook, lecture course, paper, or topic and initialize the study directory files (`course_summary.md`, `user_progress.md`, `agent_details.md`) for use with the `tutoring` skill. Use when starting to learn a new book, course, or subject.
---

# Tutoring setup

Prepare a learning resource (textbook, lecture course, paper, or topic) and initialize the working files for the `tutoring` skill.

## Ingestion and digest

1. If the user provides no source material, find a strong primary source before proceeding. Also ingest any auxiliary materials provided (problem sets, past exams, lecture notes).
2. Scale the digest to the size of the material:
   - For short texts or single topics, read and digest the entire source upfront.
   - For full-length books or multi-lecture courses, extract the full syllabus, notation, and cross-chapter dependencies upfront, and chunk or digest chapter-by-chapter (using subagents via the `subagents` skill if helpful, or digesting later chapters before studying them).
3. Do not write a passive summary. Texts often introduce formal definitions without motivation or concrete examples. While digesting, identify:
   - Exact notation, numbering, definitions, and theorem statements so the tutor matches the text's conventions.
   - Missing motivation, unstated assumptions, skipped steps, and concrete examples or edge cases that the text omits.
   - Prerequisite links between earlier and later sections.
   - Practice problems or exam questions worth doing, along with brief solution sketches so the tutor can verify ideas later without guessing.

## Files to create

Create three files in the target study folder. Include a note at the top of each file stating that it is maintained for use with the `tutoring` skill.

1. `course_summary.md`: Concise, human-readable overview of the resource, core notation/conventions, syllabus structure, and a dependency graph showing which earlier sections each chapter/section relies on.
2. `user_progress.md`:
   - Start with a `## User background and preferences` section to record relevant prior knowledge, mathematical maturity, analogies that work, and preferences as they emerge during tutoring.
   - Follow with a `## Progress checklist` broken down to sub-section granularity. Every item must use three sequential checkboxes (`started`, `understood`, `reviewed`) and a trailing single-sentence note (with date when updated):
     `- 2.1 Vector spaces | started: [ ] | understood: [ ] | reviewed: [ ] — `
3. `agent_details.md` (or `agent_details/chXX.md` per chapter if the chapters are massive): Live working document for the agent. Store the reference digest (definitions, theorems, numbering), critiques of the author's exposition, extra motivation and examples, curated questions/exercises with solution sketches, and ideas for visual/interactive aids.

Once the files are initialized, switch to the `tutoring` skill to begin teaching from the first section (or wherever the user chooses).

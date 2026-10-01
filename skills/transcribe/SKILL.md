---
name: transcribe
description: Transcribes text from images (especially Japanese, Chinese, and others) with optional arguments for romanization (ro), English translation (tl), and linguistic explanations (explain). Trigger via `/transcribe` or whenever asked to OCR or transcribe an image.
---

# Image Transcription & Translation

Extract text accurately from images (photos, screenshots, scans, manga, documents) in any language (especially East Asian languages like Japanese and Chinese).

## Argument Parsing Rules

Inspect the user's invocation string following `/transcribe` (or the accompanying prompt) for the following exact tokens:

- **`ro`**: Enable **Romanization** (Pinyin with tone marks for Chinese; modified Hepburn romaji for Japanese; Revised Romanization for Korean; standard transliteration for others).
- **`tl`**: Enable **English Translation**.
- **`explain`**: Enable **Deep Linguistic Explanation** (breaks down the single most complex, nuanced, or difficult element of the text).

*Note: Tokens can be combined freely (e.g., `/transcribe ro tl`, `/transcribe tl explain`, `/transcribe ro tl explain`).*

---

## Output Generation Rules

1. **Default Mode (No Arguments)**:
   - Provide verbatim transcription only.
   - Strictly preserve layout, line breaks, punctuation, and original orthography (kanji, hanzi, kana, etc.).
   - DO NOT translate, romanize, or add commentary unless requested.
   - If a character is illegible or degraded, mark it as `[?]` or `[unclear: best_guess]`.

2. **When `ro` is Present**:
   - Provide the complete romanized text.
   - For Japanese, ensure correct contextual kanji readings (nanori, ateji, or irregular readings).

3. **When `tl` is Present**:
   - Provide a natural, fluent English translation while staying faithful to tone and register (casual, keigo, classical, colloquial, etc.).

4. **When `explain` is Present**:
   - Identify the **single most challenging, subtle, or ambiguous component** in the passage.
   - Categorize the difficulty (Grammar / Syntax / Polysemy / Idiom / Cultural nuance / Rare Kanji or Hanzi reading).
   - Break down why it is tricky, how the components assemble, and why the chosen reading/interpretation applies in this context. Keep it sharp and insightful; avoid explaining elementary grammar.

---

## Output Format

Render sections in clean Markdown blocks:

### Transcription
[Exact verbatim text in original script]

### Romanization
<!-- Render ONLY if 'ro' is present -->
[Pinyin / Romaji / Transliteration]

### Translation
<!-- Render ONLY if 'tl' is present -->
[Natural English translation]

### Linguistic Breakdown
<!-- Render ONLY if 'explain' is present -->
- **Focus Item**: `[Target phrase / pattern / character]`
- **Category**: [e.g., Grammar nuance / Dialect / Rare vocab / Cultural idiom]
- **Analysis**: [Concise breakdown of why it is difficult and how it functions here]

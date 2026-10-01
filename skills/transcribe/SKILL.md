---
name: transcribe
description: Transcribe text from images with optional romanization (ro), English translation (tl), and grammar or nuance notes (explain). Use when asked to transcribe, OCR, or read text from an image, or when given `/transcribe`.
---

# Image transcription and translation

Read text from images like screenshots, scans, photos, or manga. Default to East Asian languages (Japanese, Chinese) when ambiguous, but handle any language shown.

## Arguments

Check the words right after `/transcribe` or in the user's prompt:

- `ro`: Add romanization. Pinyin with tones for Chinese, Hepburn romaji for Japanese, Revised Romanization for Korean.
- `tl`: Add English translation.
- `explain`: Pick the hardest single part of the text (slang, tricky grammar, polysemy, rare reading) and explain why it means what it means here.

Arguments combine in any order, like `/transcribe ro tl` or `/transcribe tl explain`.

## Rules

1. **Default (no arguments)**: Output exact transcription only. Keep line breaks, punctuation, and original characters as they appear. Do not translate or romanize. Use `[?]` for unreadable characters.
2. **With `ro`**: Romanize the full transcription. For Japanese, use the reading that matches the context, including names and ateji.
3. **With `tl`**: Translate into natural English. Match the tone of the source (casual, formal, classical).
4. **With `explain`**: Focus on one specific point that would trip up an intermediate learner. Skip obvious textbook grammar. State the exact word or structure, label what makes it tricky, and explain how it works in this sentence.

## Output format

### Transcription
[Original text]

### Romanization
<!-- Only include if ro was passed -->
[Romanized text]

### Translation
<!-- Only include if tl was passed -->
[English translation]

### Notes
<!-- Only include if explain was passed -->
- **Term**: `[Tricky word or phrase]`
- **Why it is tricky**: [Grammar quirk, rare reading, slang, or nuance]
- **Breakdown**: [How it works in this context]

---
name: transcribe
description: Transcribe text from images with optional romanization (ro | romanize), English translation (tl | translate), and grammar or nuance notes (ex | explain). Use when asked to transcribe, OCR, or read text from an image, or when given `/transcribe`.
---

# Image transcription and translation

Read text from images like screenshots, scans, photos, or manga. If presented with text, just carry out the appropriate romanization / translation / explanation requests.

## Arguments

Check the words right after `/transcribe` or in the user's prompt:

- `ro` or `romanize`: Add romanization. Pinyin with tones for Chinese, romaji for Japanese, etc.
- `tl` or `translate`: Add English translation.
- `ex` or `explain`: Pick the hardest one or two parts of the text (slang, tricky grammar, polysemy, rare reading) and explain why it means what it means here.`
- `all`: Do all of the above, if applicable.

Arguments combine in any order, like `/transcribe ro tl` or `/transcribe tl explain`.

## Rules

1. **Default (no arguments)**: Output exact transcription only. Keep line breaks, punctuation, and original characters as they appear. Do not translate or romanize.
2. **With `ro` or `romanize`**: Romanize the full transcription. For Japanese, use the reading that matches the context, including names and ateji.
3. **With `tl` or `translate`**: Translate into natural English. Keep the translation literal. You may match the tone of the source (casual, formal, classical).
4. **With `ex` or `explain`**: Focus on the main specific point or points that would trip up an intermediate learner. Skip obvious textbook grammar. State the exact word or structure, label what makes it tricky, and explain how it works in this sentence.

## Output format

[Original text]

<!-- Only include if romanize was passed -->
[Romanized text]

<!-- Only include if translate was passed -->
[English translation]

<!-- Only include if explain was passed -->
### Notes
`[Tricky word or phrase]`:
[Grammar quirk, rare reading, slang, or nuance]
[followed by How it works in this context]

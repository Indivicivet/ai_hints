---
name: stem-split
description: Use this when extracting wav tracks from .stem.m4a files.
---

# Stem split

Extract or combine audio streams from Native Instruments `.stem.m4a` files into `.wav` files using `ffmpeg`.

## Stream layout

A standard `.stem.m4a` container holds five audio streams:
- `0:a:0`: Master mix (do not include when combining stems)
- `0:a:1`: Drums
- `0:a:2`: Bass
- `0:a:3`: Other (synths, guitars, instruments)
- `0:a:4`: Vocals

## Instructions

1. Decide which output tracks the user wants (e.g., instrumental only, instrumental + vocals, drum+bass / other / vocals, or all four isolated stems). Ask if ambiguous.
2. Always set `normalize=0` on `amix`. By default, `ffmpeg`'s `amix` divides gain by the input count (`normalize=1`), which drops the level of combined stems. Stem tracks are already mastered to sum at unity gain.
3. Produce all requested output files for a song in a single `ffmpeg` command by chaining `-map` and output filenames, rather than running `ffmpeg` repeatedly on the same input.

## Examples

Instrumental only (Drums + Bass + Other):
```bash
ffmpeg -i "<song>.stem.m4a" -filter_complex "[0:a:1][0:a:2][0:a:3]amix=inputs=3:normalize=0[inst]" -map "[inst]" "../split_stems/<song>_instrumental.wav"
```

Instrumental and vocals:
```bash
ffmpeg -i "<song>.stem.m4a" -filter_complex "[0:a:1][0:a:2][0:a:3]amix=inputs=3:normalize=0[inst]" -map "[inst]" "<song>_instrumental.wav" -map 0:a:4 "<song>_vocal.wav"
```

Drum+bass, other, and vocals:
```bash
ffmpeg -i "<song>.stem.m4a" -filter_complex "[0:a:1][0:a:2]amix=inputs=2:normalize=0[db]" -map "[db]" "<song>_drumbass.wav" -map 0:a:3 "<song>_other.wav" -map 0:a:4 "<song>_vocal.wav"
```

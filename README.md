# Notes From a Passive-Aggressive Fridge

[![make.fun · u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![rank](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/nelsenwiliam/passive-aggressive-fridge-note/rank.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![reward](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/nelsenwiliam/passive-aggressive-fridge-note/reward.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)

Entry for the make.fun bounty
[Notes From a Passive-Aggressive Fridge](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
— one funny passive-aggressive note a smart fridge leaves for its owner.

## The note

> The yogurt expired Tuesday. I watched you read the date, put it back, and lie to yourself.

90 characters, one line. The fridge is smug about what its sensors
watched the owner do, the grudge is small and domestic, and the sting
is the twist: the owner lying to themself. The detail is concrete —
the yogurt, the date on the tub — not generic nagging.

## Run

```sh
python3 main.py
```

Pure standard library. `main()` writes the note to the first output
location that works: `$MAKEFUN_OUTPUT_DIR/entry.txt`, then
`/output/entry.txt`, then `out/entry.txt` — each guarded by its own
`try/except OSError`. The note is validated against the gate first:
1–200 UTF-8 characters, not only whitespace.

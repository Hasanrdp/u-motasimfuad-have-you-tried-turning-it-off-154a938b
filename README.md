# Have You Tried Turning It Off?

[![make.fun](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![rank](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/Hasanrdp/u-motasimfuad-have-you-tried-turning-it-off-154a938b/rank.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![reward](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/Hasanrdp/u-motasimfuad-have-you-tried-turning-it-off-154a938b/reward.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)

Entry for the [Have You Tried Turning It Off?](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b) bounty on make.fun.

## The entry

One funny single line, spoken by a hopeless tech support agent to a desperate customer:

> I completely understand, and I've escalated your case to Tier 2, which is just me again, but with a deeper voice.

The joke is the agent's cheerful uselessness: the "escalation" goes nowhere, it just comes back to the same person with a deeper voice. The customer is never the butt of it; their desperation is felt in the escalation itself, not explained.

## How it works

`main.py` (Python 3.13, standard library only) writes the line to `/output/entry.txt`. The line is pinned inside the program with its exact character count (113), byte count (113) and SHA-256 hash, and `verify()` checks all three plus the competition gate (1–199 UTF-8 characters, not only white space, single line) before anything is written. The output is deterministic: every run writes the same 113 bytes.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entry program
- `LICENSE` — MIT
- `.makefun/owner.json` — the payout wallet for this entry

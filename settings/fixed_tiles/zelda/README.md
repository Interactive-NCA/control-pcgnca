There are currently two types of fixed inputs:
1. `Easy` - Random variations of walls only
2. `Manual` - Levels generated manually via our UI interface

Example of generation:

```bash
python3 cli.py --gen-fixed-seeds --fixedgen-game "zelda" --fixedgen-nseeds 10 --fixedgen-difficulty "easy"
```
## Steps to reproduce
1. Open `/home/runner/work/seaborn-ranked-animated/seaborn-ranked-animated/src/moveFiles.py`.
2. Go to the `moveMatches2022()` function.
3. Inspect the `if "info" in data` and `else` branches that check `gameVersion`.
4. Run a quick trace script to print lines 43–52 and count repeated branch patterns.

## Observed
The trace showed two nearly identical branches performing the same conditions and move operation, differing only in how `gameVersion` is accessed (`data["info"]["gameVersion"]` vs `data["gameVersion"]`). This duplicates logic and matches the duplicate-code report. The duplicated block increases maintenance cost and risk of divergent edits if one branch is updated without the other.

## Expected
`moveMatches2022()` should evaluate the version filtering logic once after normalizing the source of `gameVersion`. The implementation should keep behavior unchanged while removing duplicate conditional blocks, so future edits to patch filtering are made in one place only. This should satisfy duplicate-code checks while preserving existing file move behavior.

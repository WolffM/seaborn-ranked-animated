# History

One real era of work, in 2023, followed by two years of automated upkeep
with no new features.

## A data project in one season (2023)

The first commit, 2023-01-15, already carried the full pipeline and
7,762 raw match-history JSON files, one per game (`08f4b67`). A spring
pass restructured the scripts (`9a0ca7b`). The busiest day in the
repo's history, 2023-11-09 (8 commits), moved that entire match-file
collection into its current home under `Assets/`, added the first
README, and updated the plot transitions — in two steps three minutes
apart: one commit deleted 7,528 files at the old location, 13,983 lines
(`b0ae1ec`, 11:51), the next added 7,765 files at the new one, 15,526
lines (`13b0559`, 11:54). The repo was, at the time, hosted as
`github.com/WolffM/riotdata` (`d8dfcee`), the name its README still uses.

## Automated upkeep, mostly (2025 – 2026)

After 778 days with no commits (`55b7a2d` to `65cb46c`), the next commit
was not maintenance: it added 205 files and 8,022 lines, 198 of them
more match-history JSON under `src/shortTermAnalysis/matches` — someone
ran the fetch pipeline again rather than fixing anything (`65cb46c`).
Only the eight commits after that were maintenance: an automated pull
request added a README tagline on 2026-01-05, a vibeCheck lint
workflow was added (`cb677e8`) and two more automated lint fixes
followed — removing unused imports on 2026-01-07 and an unnecessary
f-string prefix on 2026-01-13 — before vibeCheck itself was removed
account-wide (`c08930d`).

## Trivia

The repo's name on GitHub and the name in its own README have not
matched since at least 2023-11-09: the README still says "riotdata"
(`bb27d20`).

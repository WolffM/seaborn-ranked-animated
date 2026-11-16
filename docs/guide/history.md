# History

One real era of work, in 2023, followed by two years of automated upkeep
with no new features.

## A data project in one season (2023)

The first commit, 2023-01-15, already carried the full pipeline and
7,762 raw match-history JSON files, one per game (`adc6757`). A spring
pass restructured the scripts (`212f81d`). The busiest day in the
repo's history, 2023-11-09 (8 commits), moved that entire match-file
collection into its current home under `Assets/`, added the first
README, and updated the plot transitions — in two steps three minutes
apart: one commit deleted 7,528 files at the old location, 13,983 lines
(`c2c14ac`, 11:51), the next added 7,765 files at the new one, 15,526
lines (`67e83f1`, 11:54). The repo was, at the time, hosted as
`github.com/WolffM/riotdata` (`f9213aa`), the name its README still uses.

## Automated upkeep, mostly (2025 – 2026)

After 778 days with no commits (`c82ba79` to `fc8f9b4`), the next commit
was not maintenance: it added 205 files and 8,022 lines, 198 of them
more match-history JSON under `src/shortTermAnalysis/matches` — someone
ran the fetch pipeline again rather than fixing anything (`fc8f9b4`).
Only the eight commits after that were maintenance: an automated pull
request added a README tagline on 2026-01-05, a vibeCheck lint
workflow was added (`62afad2`) and two more automated lint fixes
followed — removing unused imports on 2026-01-07 and an unnecessary
f-string prefix on 2026-01-13 — before vibeCheck itself was removed
account-wide (`2bd4df3`).

## Trivia

The repo's name on GitHub and the name in its own README have not
matched since at least 2023-11-09: the README still says "riotdata"
(`d7f1279`).

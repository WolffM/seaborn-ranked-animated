---
title: Ranked Climb to Masters
summary: >-
  A small pipeline that turns a League of Legends ranked match history
  into an animated line chart of League Points over time, colored by
  rank-tier band. A one-time data project, not a running service.
features:
  - name: Match data pipeline
    summary: 'Pulls ranked solo-queue games from the Riot API and distills each one to a row in a CSV.'
    anchor: match-data-pipeline
  - name: Animated climb chart
    summary: 'Replays the climb game by game as an animated line, shaded by rank-tier band.'
    anchor: animated-climb-chart
trivia:
  - 'The repo''s first commit, 22,645 lines across 7,782 files, already included 7,762 match-history JSON files — one per League of Legends game — checked straight into git (`08f4b67`).'
  - 'Its busiest day, 2023-11-09 (8 commits), relocated the entire match-file collection in two steps three minutes apart: one commit deleted 7,528 old-location files (`b0ae1ec`, 11:51), the next added 7,765 files at the new one (`13b0559`, 11:54).'
  - 'The project was once hosted at `github.com/WolffM/riotdata`; its own README still introduces it as "riotdata" rather than its current repo name (`bb27d20`, `d8dfcee`).'
  - 'After 778 days with no commits (`55b7a2d` to `65cb46c`), the next commit added 198 more match-history JSON files rather than fixing anything; only the eight commits after that were automated maintenance — an automated README tagline (2026-01-05), a lint workflow added and later removed, and two automated lint fixes (2026-01-07, 2026-01-13).'
---

# Ranked Climb to Masters

A two-stage pipeline: `src/makeRequest.py` and `src/getMatchFiles.py` pull a
summoner's ranked solo-queue match history from the Riot Games API as raw
JSON, one file per game; `src/moveFiles.py` and `src/extractUsefulDataFromFiles.py`
distill each match down to one CSV row (champion, kills/deaths/assists,
win/loss, and the resulting League Points total). `src/main.py` chains
that CSV step and then hands off to `src/seabornPlot.py`'s animated line
plot — the climb from one rank to the next, shaded gold/emerald/platinum/diamond
by LP band — titled, in the code itself, "Ranked Climb to Masters!"

An earlier Plotly version (`plot.py`, unused by `main.py`) drew the same
bands as colored rectangles behind a static chart instead of an animated
line.

- [Features](features.md): the two halves — fetching data, then animating it.
- [Contributing](contributing.md): running the pipeline, its dependencies.
- [History](history.md): a 2023 data project, then two years of automated upkeep.
- [Trivia](trivia.md)

## Trivia

The repo's very first commit already carried nearly eight thousand raw
match files, one per League of Legends game, committed straight into git
rather than kept as a cache
([history](history.md#a-data-project-in-one-season-2023)).

# Features

What this pipeline does, run as a one-off from the command line. Nothing
here is a running service.

## Match data pipeline

**What it does.** Fetches a summoner's ranked solo-queue (`queueId 420`)
match history from the Riot Games API, one JSON file per game. It then
filters and flattens that history into a single CSV: game id, date,
duration, champion, role, kills/assists/deaths, wards, win/loss, and the
resulting League Points total.

**How to use it.** `src/makeRequest.py` / `src/getMatchFiles.py` fetch the
raw match JSON for the match IDs in `src/matchlist.py`; `src/moveFiles.py`
filters to ranked solo games and writes `output.csv`; `src/main.py` chains
`writeDataToCSV()` and `readCSV()` before handing off to the chart.

**What it does not do.** It is not a live tracker — there is no
scheduled refresh; each run works from whatever match IDs are already
listed, and a new climb needs a new list fetched by hand.

## Animated climb chart

**What it does.** Replays the ranked climb as an animated line, one point
added per game, over four shaded bands (gold, emerald-ish green,
platinum/diamond blue, master-plus purple) matching the LP ranges Riot
uses for those tiers.

**How to use it.** `python src/main.py` after the CSV step above has
produced `output2.csv`; the animation plays via `matplotlib.animation`.

**What it does not do.** It reads a fixed column index (LP, column 13)
rather than a named field, so it depends on the CSV's column order never
changing.

## Trivia

An earlier, unused Plotly version of the chart (`plot.py`) drew the same
four rank bands as static colored rectangles rather than an animated
line, and referenced Riot's own rank emblem images (`Emblem_Gold.png`
and similar) that are not wired into the Seaborn version in
`src/seabornPlot.py`.

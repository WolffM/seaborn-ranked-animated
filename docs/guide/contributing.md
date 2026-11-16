# Contributing

A small, one-off Python data project. There is no server, no deploy, and
the only automation it has ever had (a lint workflow) was removed in
2026 ([history](history.md)).

## Layout

| Path | What it is |
| --- | --- |
| `src/makeRequest.py`, `src/getMatchFiles.py` | Riot API calls that fetch raw match JSON |
| `src/matchlist.py` | the list of match ids to fetch |
| `src/moveFiles.py` | filters to ranked solo games, writes the CSV |
| `src/extractUsefulDataFromFiles.py`, `src/summonerName.py` | smaller one-off lookups |
| `src/seabornPlot.py` | the animated line chart `main.py` actually runs |
| `plot.py` | an earlier, unused Plotly version of the same chart |
| `league/` | an older copy of the same scripts, from before the 2023-11-09 reorganization |

## Run it

```sh
pip install -r requirements.txt   # plotly; seaborn/matplotlib/pandas are used but not pinned here
python src/main.py
```

Needs your own Riot Games API key set in `src/makeRequest.py` and
`src/getMatchFiles.py`, and the match ids in `src/matchlist.py` already
fetched into JSON on disk — see [features.md](features.md) for the
fetch step.

## Trivia

`requirements.txt` lists exactly one package, `plotly` — the library the
chart `main.py` actually uses, Seaborn and matplotlib, is not pinned
anywhere in the repo.

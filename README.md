# Text RPG Game

A data-driven, authored choice RPG where player decisions, stats, relationships, knowledge, equipment, powers, and previous conversations persist and alter later scenes.

Current work is on branch `foundation/text-rpg-systems`.

## Foundation prototype

The first slice intentionally separates game rules from presentation so the project can later target the chosen UI/runtime without rewriting the RPG logic.

- `docs/GAME_FOUNDATION.md` — canonical systems direction.
- `docs/VISUAL_BIBLE.md` — pixel-art consistency rules.
- `docs/REFERENCE_NOTES.md` — abstract lessons from supplied reference material; no copied story content.
- `src/textrpg/core.py` — deterministic rules engine.
- `content/sample_scene.json` — non-canon authored scene showing conditional choices.
- `tests/test_core.py` — baseline behavior tests.

## Run tests

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

The prototype uses only the Python standard library.

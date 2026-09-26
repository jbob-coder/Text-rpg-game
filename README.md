# Text RPG Game

A data-driven, authored choice RPG where player decisions, stats, relationships, knowledge, equipment, powers, party composition, and previous conversations persist and alter later scenes.

Current development branch: `foundation/text-rpg-systems`.

## Foundation prototype

The rules layer is deliberately separated from presentation. The game can later use a pixel-art Android, Godot, desktop, or web client without rebuilding the RPG state model.

- `docs/GAME_FOUNDATION.md` — canonical systems direction.
- `docs/VISUAL_BIBLE.md` — pixel-art and character consistency rules.
- `docs/REFERENCE_NOTES.md` — abstract lessons from supplied reference material; no copied story content.
- `docs/IMPLEMENTATION_STATUS.md` — current objective, verified state, completed work, risks, and next actions.
- `src/textrpg/core.py` — deterministic scene/choice rules and persistent state.
- `src/textrpg/progression.py` — earned ability mastery and technique prerequisites.
- `src/textrpg/persistence.py` — versioned JSON save/load.
- `src/textrpg/validation.py` — static validation for authored content.
- `content/sample_scene.json` — non-canon scene showing relationship, knowledge, item, and stat-dependent choices.
- `tests/` — behavior, progression, persistence, and content-validation tests.

## Run verification

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

Latest local verification for the branch-equivalent files: **16 tests passed**.

The prototype uses only the Python standard library. No hosted AI service or GitHub Actions workflow is required.

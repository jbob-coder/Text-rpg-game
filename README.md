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
- `src/textrpg/content.py` — validated JSON content-pack loading into state + engine.
- `src/textrpg/cli.py` — local standard-library terminal client with save/resume support.
- `src/textrpg/progression.py` — earned ability mastery and technique prerequisites.
- `src/textrpg/powers.py` — explicit ability/technique discovery gates, ability-specific resources/recovery, paid practice, costs, cooldowns, drawbacks, mastery stages, and evolution.
- `src/textrpg/quests.py` — authored quest graphs, objective prerequisites, branching/failure routes, and terminal states.
- `src/textrpg/persistence.py` — versioned JSON save/load.
- `src/textrpg/validation.py` — scene/quest/power validation plus stable registry cross-references for knowledge, perks, items, and conditions.
- `src/textrpg/stats.py` — canonical attributes, skills, modifier-aware resources, and derived values.
- `src/textrpg/simulation.py` — world time, conditions, training, and recovery.
- `src/textrpg/equipment.py` — equipment slots, requirements, modifiers, and set bonuses.
- `src/textrpg/social.py` — NPC memory, private knowledge, relationships, goals, story-state transitions, sharing, leak eligibility, and deterministic leak-event execution.
- `src/textrpg/visuals.py` — canonical recurring-character visual identity validation and normalized generation contracts.
- `content/vertical_slice_01.json` — original provisional-canon playable slice: opening branches, NPC state, Gate Twelve discovery, first live use, recovery, repeatable stabilization training, earned Trace Tolerance, and Directional Trace discovery.
- `content/sample_scene.json` — non-canon scene showing relationship, knowledge, item, and stat-dependent choices.
- `tests/` — behavior, progression, persistence, content validation, end-to-end route, and save/resume regression tests.

## Play the current local slice

From the repository root:

```bash
PYTHONPATH=src python -m textrpg.cli content/vertical_slice_01.json --save local_save.json
```

The CLI is a development client, not the final presentation layer. It runs authored deterministic content locally and requires no runtime AI or hosted service.

## Run verification

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

Latest fully executed branch-equivalent verification: **103 tests passed, 0 failed**.

That run predates the newest stabilization/training route. Those commits add new tests and passed a JSON structural audit (14 scenes, 23 unique choices, 3 quests, 1 power, no missing scene/quest/power/technique references), but the complete latest Python suite has not yet been rerun. Do not treat 103 as verification of the newest commits.

The prototype uses only the Python standard library. No hosted AI service or GitHub Actions workflow is required.

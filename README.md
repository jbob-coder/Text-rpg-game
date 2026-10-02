# Text RPG Game

> **Current documentation authority (2026-10-02):** start with [`docs/program/README.md`](docs/program/README.md) and [`docs/program/00_OWNER_DIRECTIVE_2026-10-02.md`](docs/program/00_OWNER_DIRECTIVE_2026-10-02.md). The documentation-first full-game program is the current planning priority for Text-rpg-game. Historical stabilization/implementation branch references below remain evidence for their exact work and must not be mistaken for the current planning objective.

A data-driven, authored choice RPG where player decisions, stats, relationships, knowledge, equipment, powers, party composition, and previous conversations persist and alter later scenes.

Current stabilization candidate: `fix/v6-runtime-boundaries`, based on
`integration/rules-ability-v6-reconcile@7f5f104fb839068bdfaf5cec72f37129ae20d463`.
The default `main` branch is still a placeholder; select the candidate branch to run this implementation.

> Coding agents and future sessions: start with [`AGENTS.md`](AGENTS.md), then read [`docs/THE_GAME_MASTER_TASK_REGISTER.md`](docs/THE_GAME_MASTER_TASK_REGISTER.md) for the current objective, blockers, task states, and handoff rules.

## Rules-engine vertical slice

The rules layer is deliberately separated from presentation. The game can later use a pixel-art Android, Godot, desktop, or web client without rebuilding the RPG state model.

- `docs/GAME_FOUNDATION.md` — canonical systems direction.
- `docs/VISUAL_BIBLE.md` — pixel-art and character consistency rules.
- `docs/REFERENCE_NOTES.md` — abstract lessons from supplied reference material; no copied story content.
- `docs/IMPLEMENTATION_STATUS.md` — current objective, verified state, completed work, risks, and next actions.
- `docs/V6_STABILIZATION_HANDOFF.md` — executed baseline, repairs, compatibility boundaries, and verification evidence.
- `docs/THE_GAME_MASTER_TASK_REGISTER.md` — repository-native task queue and continuity index.
- `src/textrpg/core.py` — deterministic scene/choice rules and persistent state.
- `src/textrpg/content.py` — validated JSON content-pack loading into state + engine.
- `src/textrpg/cli.py` — local standard-library terminal client with save/resume support.
- `src/textrpg/progression.py` — earned ability mastery and technique prerequisites.
- `src/textrpg/powers.py` — explicit ability/technique discovery gates, ability-specific resources/recovery, paid practice, costs, cooldowns, drawbacks, mastery stages, and evolution.
- `src/textrpg/quests.py` — authored quest graphs, objective prerequisites, branching/failure routes, and terminal states.
- `src/textrpg/persistence.py` — versioned JSON save/load.
- `src/textrpg/json_contract.py` — shared finite-number JSON decoding for saves and content.
- `src/textrpg/status.py` — player status and inspection projections with hidden condition/perk redaction.
- `src/textrpg/validation.py` — scene/quest/power validation plus stable registry cross-references for knowledge, perks, items, and conditions.
- `src/textrpg/stats.py` — canonical attributes, skills, modifier-aware resources, and derived values.
- `src/textrpg/simulation.py` — world time, conditions, training, and recovery.
- `src/textrpg/equipment.py` — equipment slots, requirements, modifiers, and set bonuses.
- `src/textrpg/social.py` — NPC memory, private knowledge, relationships, goals, story-state transitions, sharing, leak eligibility, and deterministic leak-event execution.
- `src/textrpg/visuals.py` — canonical recurring-character visual identity validation and normalized generation contracts.
- `content/vertical_slice_01.json` — original provisional-canon playable slice: opening branches, NPC state, Gate Twelve power discovery, first live technique use, drawback, and resource recovery.
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

Observed on Python 3.12.14: **275 tests passed, 0 failures/errors** on the repaired candidate.
The untouched upstream V6 source was first matched against all 45 Git blob hashes and
its complete Git tree, then executed: **258 tests, 1 failure, 12 errors**.
The historical 103-pass foundation result does not describe V6.

Commands, logs, the runtime file manifest, and the remaining promotion work are recorded
in [the stabilization handoff](docs/V6_STABILIZATION_HANDOFF.md).

Player clients should use `engine.build_scene_view(state)`, `engine.available_choices(state)`,
and the status/ability projections. Raw scenes, state, modifier breakdowns, and resolution
history remain engine/developer data and are not player-facing projections.

The prototype uses only the Python standard library. No hosted AI service or GitHub Actions workflow is required.

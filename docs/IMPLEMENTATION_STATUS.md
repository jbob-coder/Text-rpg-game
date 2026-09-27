# Implementation Status — Foundation Slice

## CURRENT_OBJECTIVE

Create the non-AI authored RPG foundation: persistent choices, stats, NPC memory, hidden information, equipment/perks, earned power progression, deterministic checks, save compatibility, simulation time, training, recovery, and pixel-art consistency rules.

## VERIFIED_STATE

Repository: `jbob-coder/Text-rpg-game`

Working branch: `foundation/text-rpg-systems`

The original `main` branch is not modified by this work.

## COMPLETED

- Deterministic authored scene engine.
- Persistent player state and history.
- Visible vs hidden vs locked choices.
- Four-degree checks: critical success, success, failure, critical failure.
- Relationship-gated options.
- Player knowledge-gated options.
- NPC knowledge-gated options.
- Party-member-gated options.
- Inventory requirements and item consumption.
- Quest-stage effects.
- NPC personality drift with bounded values.
- Equipment, reached equipment-set bonuses, perks, and active condition modifiers applied to checks without rewriting base stats.
- Ability mastery XP and rank progression.
- Technique requirements that can depend on rank, mastery, knowledge, and perks.
- Power runtime with per-technique mastery stages, resource costs, world-time cooldowns, authored condition drawbacks, overall ability mastery gain, and evolution prerequisites.
- Ability evolution can change form/tags, consume authored items, grant source-tracked perks, and establish a durable rank floor that later mastery recalculation cannot erase.
- Versioned JSON save/load layer with explicit schema rejection.
- Static content validation for stable IDs, duplicate choices, unsupported rules, and invalid scene references.
- Canonical seven-attribute catalog and grouped skill catalog.
- Explicit derived-stat formulas for health, stamina, focus, resolve, initiative, accuracy, evasion, guard, and carry capacity.
- Resource initialization and bounded recovery.
- Timed conditions/injuries with severity, source, tags, modifiers, and expiration through world time.
- Time-based skill training with stamina/focus cost, mentor bonus, and diminishing returns.
- Slow core-attribute training so permanent stats cannot be gained from a single trivial action.
- Equipment slot definitions, requirements, provenance, tags, set IDs, active/passive references, and threshold set bonuses.
- NPC memory records with importance, tags, time, and contextual data.
- NPC-owned private knowledge with confidence, truth state, secrecy, and source.
- Explicit character-to-character knowledge sharing.
- Multidimensional relationship utilities with independent minimum/maximum gates and bounded -100..100 changes.
- Explicit NPC goals with priority, progress, completion/failure state, durable history, and guarded story-state transitions.
- Deterministic leak-candidate evaluation based on authored social networks and NPC personality; no generative gossip.
- Deterministic authored leak-event execution that transfers existing knowledge only to eligible recipients, records recipient memories, and appends an inspectable propagation event.
- Pixel visual consistency specification.
- Abstract reference extraction notes that avoid copying source story content.
- Systems catalog documenting the stat/training/equipment/social contract.
- Authored quest-graph runtime with prerequisite objectives, optional branches, failure routes, terminal stages, manual failure, and durable transition history.
- Quest-definition validation and whole-content-pack validation, including scene-to-quest-stage cross-reference checks.
- Scene effects can now start quest graphs, complete/fail graph objectives, and fail quests through the quest runtime instead of bypassing graph state.
- Derived stats and resource maxima can now use effective equipment, set-bonus, perk, condition, and direct derived-stat modifiers without rewriting base attributes.
- Canonical visual identity validation and normalized art-generation contracts are implemented in `src/textrpg/visuals.py`.
- First original playable opening slice added at `content/vertical_slice_01.json` as **provisional canon**: `The Dead Relay`, with cooperative, solo, and recovery/recombination routes.
- The vertical slice includes the first structured recurring-character identity record for `NPC_TAMSIN`.
- Effective modifier aggregation is centralized in one core contract reused by scene checks and derived-stat formulas.
- Authored choice time now advances through the simulation clock, so timed conditions expire consistently during narrative actions.
- Negative player/NPC knowledge gates are supported, allowing routes to distinguish “does not know yet” from “knows”.
- Scene effects can create/progress NPC goals and execute guarded NPC story-state transitions.
- `src/textrpg/content.py` validates and instantiates content packs into `GameState` + `RulesEngine`.
- `src/textrpg/cli.py` provides a standard-library local terminal client for playable authored packs, with save/resume support.
- Explicit ability discovery creates a rank-0/mastery-0 shell rather than granting free progression.
- Technique practice now consumes stamina/focus, advances world time, uses diminishing returns, supports mentor bonuses, and grants gradual technique/ability mastery.
- `The Dead Relay` now continues below Gate Twelve into the first provisional power-discovery/practice sequence; one hour of first practice is intentionally insufficient to leave the earliest technique stage.
- Power definitions can now declare ability-specific resource pools, starting/max values, recovery rates, technique costs/cooldowns/drawbacks, and future unlock requirements.
- `ABILITY_TRACE_ECHO` now uses `power_resources.trace_resonance` rather than a universal mana pool: max/start 10, baseline recovery 2 per hour.
- `TECHNIQUE_SIGNAL_PULSE` now has a real first-use loop: focus + Trace Resonance cost, 10-minute cooldown, mastery gain, and temporary `COND_ECHO_STRAIN`.
- A 30-minute quiet-recovery scene restores only 1 Trace Resonance at the current rate and advances shared world time, allowing the 20-minute strain condition to expire naturally.
- `TECHNIQUE_DIRECTIONAL_TRACE` is defined but intentionally locked behind later rank/mastery, knowledge, perk, attribute, and skill requirements.
- Content validation now validates power-definition structure and rejects scene effects that reference unknown powers or techniques; NPC/power effect IDs and practice/recovery durations receive structural validation.
- Save/resume route regressions permanently cover cooperative, solo, failure/recovery, and first-power paths.
- Technique discovery now has a separate authored prerequisite contract from technique use; locked techniques cannot be discovered early through runtime effects.
- Choices can use the `technique_discoverable` condition to expose or lock authored discovery opportunities based on the current persistent state.
- Stable content registries are now supported for knowledge, perks, items, and conditions; scene/power references can be cross-validated before play.
- Initial-state inventory/knowledge/perk/condition IDs are checked against registries when a content pack opts into registry enforcement.
- `TECHNIQUE_DIRECTIONAL_TRACE` now has explicit discovery prerequisites including Trace Echo rank/mastery, stable-pattern knowledge, Trace Tolerance, attributes, Power skill, and learned Signal Pulse.

## TESTS_RUN

Command used against a branch-equivalent reconstruction of the current remote files:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

Latest exact branch-equivalent suite result: **103 tests passed, 0 failed**.

Verification was performed against a local reconstruction of the live `foundation/text-rpg-systems` branch. The local reconstruction started from the exact 97-test branch snapshot. Every source/content/test file changed in the technique-discovery/registry slice was Git-blob-hash matched against the live branch before the final 103-test run.

Observed command:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

Observed result:

```text
Ran 103 tests in 0.034s

OK
```

Save/resume is now permanent regression coverage in `tests/test_save_resume_routes.py`. Cooperative-direct, solo-direct, failure/recovery-join, and first-power-practice routes each survive a JSON save/load round trip and continue successfully.

No GitHub Actions workflow was added; verification does not consume hosted CI minutes.

## NEXT_ACTION

1. Add authored acquisition paths for `KNOW_TRACE_ECHO_PATTERN_STABLE` and `PERK_TRACE_TOLERANCE` instead of granting either through debug/state edits.
2. Add a real future training/research branch where `TECHNIQUE_DIRECTIONAL_TRACE` can eventually become discoverable through earned state.
3. Extend stable registries to reusable content packs as more items/perks/conditions are introduced.
4. Review `The Dead Relay`, Gate Twelve, Tamsin, and Trace Echo as provisional story material before promoting any of them to confirmed canon.
5. Continue save/resume end-to-end coverage for every new major route.
6. Connect the rules layer to a selected pixel-art presentation runtime only after the client technology is deliberately chosen.

## BLOCKERS

The rules core is not blocked.

The visual/runtime implementation should not be hard-wired yet because the final client technology has not been established in the repository. Keeping rules separate avoids throwing away work if the presentation target changes.

## IMPORTANT_DECISIONS

- Runtime generative AI is not a dependency.
- Important continuity lives in save state and stable IDs, not chat memory.
- Core attributes progress slowly; skills and mastery can progress faster.
- Powers require earned progression rather than instant button unlocks.
- Information and conversations are first-class gameplay state.
- Important NPCs use multidimensional relationships instead of one friendship score.
- Secret propagation remains deterministic, inspectable, and authored.
- Equipment can alter behavior and stats without mutating the player’s underlying base attributes.
- Art generation must obey a canonical visual identity sheet before an asset becomes game canon.

## KNOWN_RISKS

- Too many stats can create unreadable UI and redundant mechanics. Every stat needs a distinct rule purpose.
- Excessive branching can cause content explosion. Recombining branches around durable state is preferred over writing a completely separate story for every choice.
- Hidden information must be scoped to the correct character/player knowledge stores or secrets can leak accidentally.
- Progression and recovery numbers are provisional until a playable loop provides balancing evidence.
- Effective-stat aggregation is now centralized and reused by checks and derived stats. New modifier types must be added to that shared contract rather than reimplemented in multiple systems.

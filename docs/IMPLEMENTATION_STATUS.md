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

## TESTS_RUN

Command used against a branch-equivalent reconstruction of the current remote files:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

Last full branch-equivalent suite result: **58 tests passed, 0 failed**.

That full run predates the newest derived-stat, quest-effect, visual-identity, and vertical-slice additions.

Latest focused local reconstruction after those additions: **13 focused checks passed** covering modifier-aware derived stats/resource maxima, effective-value parity with scene checks, graph-aware scene quest effects, quest transitions, and visual-identity validation.

A new full branch-equivalent suite rerun is still required before the repository-wide pass count is increased.

No GitHub Actions workflow was added; verification does not consume hosted CI minutes.

## NEXT_ACTION

1. Rerun the complete branch-equivalent test suite and resolve any integration regressions from the latest slice.
2. Review/promote `The Dead Relay` from provisional canon to confirmed canon or revise it before expansion.
3. Expand visual identity records to every recurring character introduced by the confirmed opening.
4. Add authored NPC goal/story-state effects to scene data so the vertical slice exercises those systems directly.
5. Add power discovery/training content to the next playable slice without granting power progression instantly.
6. Connect the rules layer to the chosen pixel-art presentation runtime after the client technology is deliberately selected.

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
- Effective-stat aggregation and derived-stat calculation now both account for direct equipment, reached set-bonus thresholds, perks, and active conditions. Their parity is covered by a focused regression check, but future refactoring should centralize the duplicated aggregation contract to reduce drift risk.

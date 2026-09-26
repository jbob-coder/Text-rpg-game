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
- Deterministic leak-candidate evaluation based on authored social networks and NPC personality; no generative gossip.
- Pixel visual consistency specification.
- Abstract reference extraction notes that avoid copying source story content.
- Systems catalog documenting the stat/training/equipment/social contract.

## TESTS_RUN

Command used against a branch-equivalent reconstruction of the current remote files:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

Result: **30 tests passed, 0 failed**.

The verification covered the original foundation tests plus stats, training/recovery, conditions, equipment sets, effective modifier aggregation, and social-information tests.

No GitHub Actions workflow was added; verification does not consume hosted CI minutes.

## NEXT_ACTION

1. Add power resource costs, cooldowns, technique stages, drawbacks, and evolution prerequisites.
2. Add explicit NPC goal/story-state transitions and multidimensional relationship utilities.
3. Add quest graph definitions, branching objectives, failure states, and content-pack validation.
4. Add deterministic information propagation events that execute authored leak rules rather than only listing candidates.
5. Define the first original playable vertical slice and its canon opening scenario.
6. Add character visual identity records that can drive consistent pixel portrait/sprite generation.
7. Connect the rules layer to the chosen pixel-art presentation runtime after the client technology is deliberately selected.

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
- Effective-stat aggregation now applies direct equipment, reached set-bonus thresholds, perks, and active condition modifiers once each. Future derived-stat integration must preserve the same no-double-counting rule.

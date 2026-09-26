# Implementation Status — Foundation Slice

## CURRENT_OBJECTIVE

Create the non-AI authored RPG foundation: persistent choices, stats, NPC memory, hidden information, equipment/perks, earned power progression, deterministic checks, save compatibility, and pixel-art consistency rules.

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
- Equipment and perk modifiers applied to checks without rewriting base stats.
- Ability mastery XP and rank progression.
- Technique requirements that can depend on rank, mastery, knowledge, and perks.
- Versioned JSON save/load layer with explicit schema rejection.
- Static content validation for stable IDs, duplicate choices, unsupported rules, and invalid scene references.
- Pixel visual consistency specification.
- Abstract reference extraction notes that avoid copying source story content.

## TESTS_RUN

Command:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

Latest local result for the branch-equivalent files: **16 tests passed**.

No GitHub Actions workflow was added; verification does not consume hosted CI minutes.

## NEXT_ACTION

1. Define the canonical complete stat catalog and derived-stat formulas.
2. Add status conditions/injuries, resource costs, recovery, and time-based training.
3. Add equipment definitions, slots, set tags, active/passive gear abilities, and source tracking.
4. Add full NPC records with goals, story state, relationship axes, memories, and private knowledge ownership.
5. Add information propagation rules for secrets/leaks.
6. Add quest graph definitions and content packs.
7. Add the first original playable vertical slice after the canon opening scenario is locked.
8. Connect the rules layer to the chosen pixel-art presentation runtime.

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
- Art generation must obey a canonical visual identity sheet before an asset becomes game canon.

## KNOWN_RISKS

- Too many stats can create unreadable UI and redundant mechanics. Every stat needs a distinct rule purpose.
- Excessive branching can cause content explosion. Recombining branches around durable state is preferred over writing a completely separate story for every choice.
- Hidden information must be scoped to the correct character/player knowledge stores or secrets can leak accidentally.
- Progression thresholds will require balancing after a playable loop exists.

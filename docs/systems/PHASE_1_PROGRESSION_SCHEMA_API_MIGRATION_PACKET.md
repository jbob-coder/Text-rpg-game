# THE GAME — Phase 1 Progression Schema & API Migration Packet

Status: **APPROVED MIGRATION DESIGN / D-032 PROGRESSION CHILD / HISTORICAL PRE-D-066 PLAN / D-066 IMPLEMENTED**
Repository: `jbob-coder/Text-rpg-game`
Source inspection HEAD: `d6e80edafe71e678fcd15c293b601a6815eaad90`
Parents:
- `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`
- `docs/systems/PROGRESSION_MASTER_PLAN.md`
- `docs/systems/PROGRESSION_CLASSES_RANKS_EVOLVED_GAME_DESIGN.md`
- `docs/systems/SAVE_AND_CONTENT_MIGRATION_MASTER_PLAN.md`
- `docs/systems/STATUS_UI_ABILITIES_AND_PASSIVES_MASTER_PLAN.md`
- `docs/THE_GAME_MASTER_TASK_REGISTER.md`

## Current implementation overlay — 2026-10-08

This packet was written before D-066 implementation. Preserve the detailed sections below as the migration design and rationale, but do **not** interpret statements such as “D-066 should,” “implementation not started,” or “D-066 may begin” as current task state.

D-066 is now **DONE / VERIFIED BOUNDED PHASE 1 PROOF**:
- final verification head: `c60f2ca1f52caf95ced00272a57b432e7740a866`;
- Actions PR merge checkout: `1bc7939ba6100c99db0ab442fc6939aa9af44ed4`;
- final workflow: Android Pixel Client run **#319 / `37250623837` — SUCCESS**;
- Python engine: **319 / 319 passed**;
- Android JVM/build/package: **PASS**;
- connected API-35 emulator suite: **35 / 35 passed**;
- APK SHA-256: `e7066e937c01e61d33541822c4532b4ce41c55cc61f8b63a40f5f9c901e7b441`;
- accepted evidence: `docs/evidence/D066_PHASE1_PROGRESSION_PROOF_2026-10-04.md`.

Implemented bounded migration/result:
- stable ability ID is included in player-safe Python ability projection;
- typed Kotlin ability/technique/resource mapping exists for the bounded proof;
- discovered progression reaches the Stats consumer without UI-owned progression arithmetic;
- raw authored requirements/discovery requirements/effects remain excluded from the typed Android boundary;
- the selected Trace Echo / Signal Pulse mastery route persists through save/load and deterministic replay;
- save schema remains **v1** and no competing top-level progression owner was added.

This does **not** implement the evolved class/profession/rank target model. Those remain separate D-045/migration/canon work. P16 has since materialized the Gate Twelve Progression Proof Packet; the direct documented D-045 follow-on is the **Progression UX Contract**, only when the live Bulletin publishes an eligible lane.

## 1. Purpose

This packet closes the progression migration-design child of D-032.

It maps the smallest Gate Twelve-compatible Phase 1 progression proof onto the current Python state, rules, persistence, content, player-safe projection, and Android consumer boundaries without inventing a second progression owner.

This is an implementation packet, not a claim that D-066 is already complete.

## 2. Current source reality

At the inspected source HEAD, `GameState` already owns the durable progression-relevant state needed by Phase 1:

- `player.attributes`;
- `player.skills`;
- `player.resources`;
- ability-specific player paths such as `player.power_resources.trace_resonance`;
- `abilities`;
- `perks`;
- `knowledge`;
- `inventory`;
- `flags`;
- `time_minutes`;
- `history`.

There is no separate durable class/rank/progression object.

The current save schema is version 1. `GameState.snapshot()` serializes the existing progression fields, and persistence rejects unsupported top-level save fields or unsupported schema versions. Existing tests already cover round-trip preservation of abilities, technique mastery, visibility state, perks, and nested player state.

Current authoritative mutation paths include:

- `simulation.train()` for registered skills;
- `progression.gain_ability_mastery()`;
- `powers.discover_ability()`;
- `powers.discover_technique()`;
- `powers.gain_technique_mastery()`;
- `powers.practice_technique()`;
- `powers.use_technique()`;
- `powers.recover_power_resource()`;
- `RulesEngine._apply_effects()` as the authored-scene dispatcher for `skill_train`, `ability_discover`, `technique_discover`, `technique_practice`, `technique_use`, and `power_recover`.

Android-facing gameplay currently calls authoritative Python through `AndroidGameSession`. It does not own progression arithmetic.

## 3. Core migration decision

**Do not add a new top-level progression field to GameState for Phase 1.**

Use the existing state owners:

| Progression concern | Authoritative current owner |
| --- | --- |
| attributes | `state.player["attributes"]` |
| skills | `state.player["skills"]` |
| ordinary resources | `state.player["resources"]` |
| ability-specific resource | validated path under `state.player`, currently `power_resources.trace_resonance` |
| ability rank/mastery/form/tags | `state.abilities[ABILITY_ID]` |
| technique mastery/stage/uses/cooldown | `state.abilities[ABILITY_ID]["techniques"][TECHNIQUE_ID]` |
| persistent perks/passives used by current proof | `state.perks` |
| knowledge gates | `state.knowledge` |
| world time | `state.time_minutes` |
| durable audit events | `state.history` |

Reason:
- these structures already execute the Gate Twelve progression content;
- schema-v1 persistence already preserves them;
- current rules already enforce registered skills, mastery stages, resource cost, cooldown, drawbacks, and discovery requirements;
- creating a parallel `progression` object would duplicate authority and create save migration risk without solving a Phase 1 requirement.

A future accepted redesign of classes, professions, ranks, global level, or skill IDs is separate migration work and must not be smuggled into D-066.

## 4. Phase 1 progression proof selection

The smallest current proof is the existing Trace Echo path.

Stable content IDs already present:

- `ABILITY_TRACE_ECHO`;
- `TECHNIQUE_SIGNAL_PULSE`;
- `TECHNIQUE_DIRECTIONAL_TRACE`;
- `PERK_TRACE_TOLERANCE`;
- `KNOW_TRACE_ECHO_IS_PERSONAL_PERCEPTION`;
- `KNOW_GATE_TWELVE_RECENT_TRACE`;
- `KNOW_TRACE_ECHO_PATTERN_STABLE`;
- `QUEST_GATE_TWELVE_ECHO`;
- `QUEST_TRACE_STABILIZATION`;
- `PRACTICE_SIGNAL_PULSE_ONE_HOUR`;
- `PRACTICE_SIGNAL_PULSE_TWO_HOURS`;
- `DISCOVER_DIRECTIONAL_TRACE`.

The selected minimum D-066 proof should be:

1. discover `ABILITY_TRACE_ECHO` through the authored Gate Twelve event;
2. discover `TECHNIQUE_SIGNAL_PULSE`;
3. practice Signal Pulse through the authored one-hour practice action;
4. prove technique mastery increases;
5. prove ability mastery increases;
6. prove stamina/focus and world time are paid;
7. save;
8. load;
9. prove the same mastery/resource/time values survive;
10. prove player-safe projection shows the discovered ability/technique and mastery state.

This is already meaningful progression because it changes durable mastery and stage-track state through world action and cost. It is not a UI-only number.

The later Directional Trace unlock is a stronger extension and may be used if D-066 can prove it without broadening scope. It must not be required merely to make the first proof legitimate.

## 5. Existing Gate Twelve progression contract

Current authored `ABILITY_TRACE_ECHO` defines:

- family `sensory_resonance`;
- form `latent_trace`;
- dedicated resource `power_resources.trace_resonance`;
- maximum 10;
- starting 10;
- recovery 2/hour.

`TECHNIQUE_SIGNAL_PULSE` currently defines:
- discovery/use gates through knowledge and current ability state;
- focus cost;
- Trace Resonance cost;
- cooldown;
- technique mastery gain;
- ability mastery gain;
- `COND_ECHO_STRAIN` drawback.

`TECHNIQUE_DIRECTIONAL_TRACE` additionally requires the current authored combination of:
- mastery;
- `KNOW_TRACE_ECHO_PATTERN_STABLE`;
- `PERK_TRACE_TOLERANCE`;
- Perception;
- Will;
- `powers` skill;
- Signal Pulse technique stage.

These values are current content facts, not new canonical balance decisions in this packet.

## 6. Skill ownership and the `powers` skill

`schema.SKILL_CATALOG` already registers `powers` in the knowledge family.

The vertical-slice initial state does not explicitly seed `powers`; current status and effective-value logic treat an absent registered skill as zero, while `simulation.train()` can create the mutable skill entry on first successful training.

Therefore Phase 1 does not need:
- a new skill registry;
- a top-level skill state;
- an Android-owned skill value;
- a save schema bump.

`TRAIN_POWER_FUNDAMENTALS_TWO_HOURS` is a valid separate activity proof and is owned by D-068. D-066 should avoid duplicating D-068 unless the same action is only used as a prerequisite for a bounded stronger progression test.

## 7. Stable-ID rules

For Phase 1 implementation:

- retain all IDs listed in section 4 exactly;
- do not rename `powers`;
- do not rename `ABILITY_TRACE_ECHO` or either technique ID;
- do not reuse any of those IDs for a different meaning;
- authored scene/choice IDs remain content IDs, not UI labels;
- display labels may evolve independently if the stable gameplay IDs remain unchanged.

If any stable ID later changes, use an explicit save/content migration with old ID, new ID, fixture, validation, and round-trip test.

## 8. Mutation boundary

The preferred Phase 1 runtime path remains:

`Android action -> AndroidGameSession.choose(choice_id) -> RulesEngine.choose() -> authored effect -> authoritative progression function -> GameState`

Do not add Android endpoints such as:
- `setSkill`;
- `setMastery`;
- `grantTechnique`;
- `setAbilityRank`;
- generic JSON state mutation.

Do not calculate mastery gain, rank, skill gain, resource cost, cooldown, or unlock eligibility in Kotlin/Compose.

Direct Python progression functions remain valid for unit tests and engine-internal composition, but authored playable progression should enter through validated content/effect paths unless a later system has an explicit authoritative API.

## 9. Transaction and rollback expectations

Existing choice execution snapshots `GameState` and restores it when effect application fails.

D-066 tests must preserve that property for the selected progression route.

At minimum verify:
- insufficient resource practice fails without mastery/time/resource partial mutation;
- undiscovered technique use fails without mutation;
- unmet discovery gates do not create the technique;
- a failed save does not rewrite progression into another representation.

If implementation discovers a progression helper that can partially mutate before a late validation error, repair that helper transactionally inside D-066 only if the defect affects the selected proof.

## 10. Save/migration decision

**Phase 1 progression uses save schema v1. No schema bump is required by this packet.**

Why:
- `abilities`, `perks`, `knowledge`, `player`, `time_minutes`, and `history` are existing GameState fields;
- ability/technique records are already nested under the persisted `abilities` field;
- `player.power_resources` is nested player state, not a new top-level save field;
- current persistence tests already prove ability discovery/mastery/visibility state survives round trip.

D-066 must still add an exact Phase 1 route save/load regression because generic persistence tests do not prove the live content path.

Schema v2 is required later only if accepted implementation changes the top-level contract or makes a breaking nested representation that old saves cannot safely interpret.

## 11. Player-safe Python projection

`status.build_status_view()` already projects:
- attributes;
- resources;
- derived values;
- grouped registered skills;
- abilities;
- visible conditions.

`powers.ability_player_view()` deliberately projects only persistent discovered techniques and allowed evolution visibility. It does not dump raw authored technique/evolution requirements.

That redaction rule is correct and must be preserved.

One concrete compatibility gap exists:

- `build_status_view()` iterates `ability_id`, but current `ability_player_view()` output does not include the stable ability ID.

D-066 should add the additive player-safe field:

`"id": ability_id`

to each ability view.

Do not expose:
- undiscovered techniques;
- hidden evolution requirements;
- raw authored `requirements`;
- raw `discovery_requirements`;
- modifier internals not already allowed by status policy;
- private NPC/quest state.

## 12. Android mapping gap

Current Kotlin `GameSnapshot` has DTOs for resources, attributes, derived stats, skills, conditions, identity, inventory, quests, map, and visuals.

It has **no ability/technique DTO**, and `BridgeSnapshotMapper.fromMap()` does not consume `status.abilities`.

Therefore current Python ability projection is dropped at the Kotlin boundary.

D-066 should add bounded player-safe DTOs, for example:

`GameAbility`
- id;
- name;
- rank;
- masteryStage;
- masteryXp;
- form;
- state;
- optional resource;
- techniques;
- completed evolution IDs if exposed by current Python view.

`GameTechnique`
- id;
- name;
- stage;
- masteryXp;
- uses;
- ready;
- cooldownRemainingMinutes.

`GameAbilityResource`
- label;
- current;
- max when present;
- recoveryPerHour when present.

Mapper policy:
- missing `status.abilities` maps to an empty list for backward compatibility with pre-migration payloads;
- when an ability entry is present, stable `id` and required player-safe scalar fields are strictly validated;
- malformed numeric values are rejected;
- unknown authored requirement maps are never accepted into the DTO;
- Compose receives typed DTOs, not raw nested maps.

No Android mutation API is added for progression.

## 13. Android presentation boundary

D-066 only needs enough Android consumption to prove the player-safe progression data survives the bridge if its acceptance evidence includes Android.

A full final Stats/Abilities UX belongs to the broader Android/status work and D-077.

The bounded progression consumer should:
- display discovered ability identity and mastery;
- display discovered technique mastery/stage;
- display current ability resource if present;
- avoid showing undiscovered unlock requirements unless Python explicitly marks them player-visible.

Android must not infer unlock availability from local numbers.

## 14. Content and validation impact

No new top-level content section is required.

Current `content_pack_from_mapping()` already:
- reads `powers`;
- requires it to be a mapping;
- validates the content pack;
- passes power definitions into `RulesEngine`;
- retains current initial GameState.

D-066 should modify content only if an exact tested defect in the selected live route requires it.

Do not add class/profession/global-level content merely because evolved design documents discuss those later systems.

## 15. Determinism

The selected progression route is deterministic under current rules:
- practice gain is formulaic from current state and authored parameters;
- ability/technique mastery stage is threshold-derived;
- resource/time costs are formulaic;
- there is no random roll in the selected one-hour practice action.

D-066 must prove identical starting state + identical action sequence produces the same:
- technique mastery;
- ability mastery;
- resources;
- time;
- projected progression view.

If save/load is inserted between actions, final authoritative values must remain identical to the uninterrupted sequence.

## 16. Exact D-066 test plan

### Python unit/regression

1. ability discovery creates `ABILITY_TRACE_ECHO` with zero mastery and its dedicated resource.
2. Signal Pulse discovery creates a zero-mastery technique record.
3. one-hour practice:
   - increases technique mastery;
   - increases ability mastery;
   - pays stamina/focus;
   - advances time;
   - emits the expected progression history event.
4. failed practice on insufficient resources is atomic.
5. `dumps_state -> loads_state` preserves the exact progression state after practice.
6. `build_status_view` exposes ability ID after the additive projection fix and contains only discovered techniques.
7. hidden/undiscovered requirement structures are absent from the player-safe view.
8. deterministic replay with and without a save/load boundary produces equal selected authoritative progression fields.

### Content/bridge

9. the current vertical-slice authored progression choices validate.
10. an AndroidGameSession route or focused bridge test proves the status view carries the progressed ability.
11. bridge privacy regression confirms raw `requirements`, `discovery_requirements`, and authored effects do not leak.

### Android JVM

12. `BridgeSnapshotMapperTest` maps a valid ability + technique payload.
13. missing abilities remains backward-compatible as empty.
14. malformed ability mastery/stage/resource fields are rejected.
15. DTO output contains no hidden authored requirements.

### UI/instrumentation when in D-066 scope

16. a discovered ability is visible after progression.
17. rotation/recomposition does not alter authoritative progression.
18. no UI-side progression arithmetic is introduced.

## 17. Implementation order

Smallest safe D-066 sequence:

1. lock exact implementation HEAD;
2. add `id` to Python `ability_player_view` and update status tests;
3. add Kotlin ability/technique/resource DTOs and mapper support;
4. add Kotlin mapper tests;
5. add the focused live Trace Echo practice/save/load/determinism Python regression;
6. repair only defects proven by that regression;
7. add the smallest presentation assertion needed for acceptance;
8. run exact-head Python tests relevant to progression/status/persistence/content/bridge;
9. run Android JVM tests relevant to mapper/consumer if Android files changed;
10. synchronize Phase 1 requirement 5 with observed evidence.

Do not expand into classes, professions, full balance, tactical progression, or new rank systems in this task.

## 18. Rollback boundary

This migration is intentionally reversible.

If D-066 implementation must be reverted:
- remove the additive ability ID projection;
- remove Kotlin ability DTO/mapper/presentation additions;
- retain existing schema-v1 save data and progression rules;
- existing authored choices, Python progression functions, and saves remain structurally valid.

No save rewrite or destructive migration is needed to roll back the presentation work.

If a future breaking progression redesign is accepted, it must use the migration pattern in `SAVE_AND_CONTENT_MIGRATION_MASTER_PLAN.md` rather than relying on this rollback path.

## 19. Current gaps D-066 must not misreport

As of the inspected source HEAD:

- current source already implements ability/technique progression;
- generic persistence already preserves ability records;
- Python status already constructs an ability projection;
- Kotlin currently drops that ability projection;
- no exact-head D-066 Gate Twelve mastery + save/load + deterministic proof has been recorded by this packet;
- no current-head Android build or physical-device progression proof is claimed;
- evolved class/profession/rank targets remain design, not implementation.

## 20. Result

The D-032 progression child is implementation-ready.

The selected Phase 1 route reuses the existing authoritative progression system and schema-v1 state. The only required migration identified for the selected proof is additive player-safe ability identity plus typed Kotlin consumption, followed by exact-head runtime/save/determinism evidence.

D-066 may begin after this packet is synchronized into D-032 and the live bulletin board marks it dependency-eligible.

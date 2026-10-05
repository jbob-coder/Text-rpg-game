# THE GAME — Passive Runtime Owner & Projection Disposition — Wave 001

Status: **PHASE-C CURRENT-RUNTIME DISPOSITION / DESIGN-TO-IMPLEMENTATION BOUNDARY / NOT CANON PROMOTION / NO RUNTIME CHANGE**

Parents:
- `STATUS_UI_ABILITIES_AND_PASSIVES_MASTER_PLAN.md`
- `PASSIVE_STATE_OWNER_RESOLVER_MATRIX_WAVE_001.md`
- `PASSIVE_RECORD_OWNER_WRITE_TARGET_MATRIX_WAVE_001_INDEX.md`
- `PASSIVE_CROSS_FAMILY_COMPOSITION_STANDARD.md`
- `PASSIVE_PHASE_C_PROGRESS_TRACKER.md`

Current source inspected:
- `src/textrpg/core.py`
- `src/textrpg/modifiers.py`
- `src/textrpg/status.py`
- `src/textrpg/simulation.py`
- `src/textrpg/powers.py`
- `src/textrpg/equipment.py`
- `src/textrpg/social.py`
- `src/textrpg/persistence.py`
- `src/textrpg/android_bridge.py`
- `android/app/src/main/java/com/thegame/rpg/engine/GameEngine.kt`
- `tests/test_status.py`

Task:
- Parallel P4 / D-046 — Status / ability / passive Phase-C refinement.

Purpose: resolve one specific Phase-C gap: the earlier passive matrices define **conceptual** owners and write targets, but deliberately do not say which of those concepts can reuse current authoritative runtime state, which are only partially represented, and which require a future domain owner/API before implementation.

This document supplies that disposition without inventing runtime state.

---

# 1. Current passive/runtime truth

## 1.1 Durable current perk container exists

Current `GameState` has a durable top-level:

`state.perks: Dict[str, Dict[str, Any]]`

`GameState.snapshot()` includes `perks`, so current save/load preserves that field.

Current structural validation requires `state.perks` to be a mutable mapping.

This proves a current perk container exists.

It does **not** prove that the 230 Wave-001 target passive records are implemented.

## 1.2 Current authored grant path is narrow

Current `RulesEngine._apply_effects()` supports `add_perk`.

The current grant path records:
- source;
- validated additive modifiers;
- tags;
- optional visibility.

Current modifier validation accepts only:
- `attributes.<registered_attribute>`;
- `skills.<registered_skill>`;
- `derived.<registered_derived_stat>`.

Therefore the current perk mechanism is a valid substrate for **bounded additive effective-value modifiers**.

It is not a general implementation of:
- movement actions;
- tactical reactions;
- medical cases;
- profession state;
- institutional authorization;
- event qualification;
- knowledge provenance;
- ability technique logic;
- world truth;
- social decision logic.

## 1.3 Current perk effect participation

`modifiers.perk_modifiers()` reads `state.perks` and contributes validated perk modifiers to authoritative effective-value resolution.

Perks therefore can already affect current attributes, skills and derived values through the same rules path as equipment/conditions.

A target passive whose effect is not faithfully expressible as one of those modifier paths must not be flattened into a fake stat bonus merely to reuse `state.perks`.

## 1.4 Current validation depth

Current state validation proves `perks` is an object, but it does not provide a full Wave-001 passive-record schema.

The safe current paths add additional checks:
- `add_perk` validates modifier paths/values;
- `perk_modifiers` validates perk records/modifier maps when resolving effects;
- status inspection validates visibility before exposing modifier provenance.

Future target-passive implementation still requires definition validation, stable definition IDs, acquisition/qualification validation, domain-specific effect validation and migration rules.

---

# 2. Current player-safe projection truth

## 2.1 No explicit passive list in Status snapshot

Current `build_status_view()` projects:
- identity;
- attributes;
- resources;
- derived values;
- skills;
- abilities;
- conditions.

It does not return a player-facing `perks` or `passives` collection.

## 2.2 Perk effect provenance can appear in deep inspection

Current `inspect_status_value()` can expose a visible perk as a contribution source such as:

`perk:PERK_PUBLIC`

for supported attribute/skill/derived paths.

Hidden perk provenance is aggregated into `unidentified_modifier` instead of exposing the hidden ID.

Current tests prove that hidden perk identifiers stay redacted across save/resume.

## 2.3 Android does not own a passive list

Current Android `GameSnapshot` has no passive/perk-list DTO.

The Kotlin mapper accepts `perk` as one possible **status contribution kind**, but there is no current top-level list of passive records.

Therefore:
- current Android may consume a safe perk contribution when it appears in an inspected status breakdown;
- Android does not currently receive a complete passive catalog for the player;
- future explicit passive projection needs its own player-safe schema;
- Compose must not infer all passive state from contribution labels.

---

# 3. Disposition vocabulary

Each conceptual owner receives one of four dispositions.

## REUSE_CURRENT_OWNER

Current authoritative state/rules are sufficiently close that future passive implementation should compose through the existing owner rather than create a parallel owner.

This does not mean every target passive in that family is already implemented.

## COMPOSE_CURRENT_STATE

Useful authoritative inputs already exist, but no normalized owner exists for the full conceptual domain.

Implementation should compose current state and add only the minimum missing domain state/API justified by concrete behavior.

## DOMAIN_RUNTIME_REQUIRED

The target conceptual owner has no sufficiently equivalent current runtime domain.

Do not fake it with `state.perks`, flags, UI-local state or arbitrary history entries.

A future implementation/migration contract is required.

## LEDGER_CONTRACT_REQUIRED

Generic history/flags may contain related evidence, but the target needs explicit event/qualification semantics before those records can authorize passive acquisition/effects.

Generic history is evidence infrastructure, not automatically a typed qualification ledger.

---

# 4. Conceptual-owner → current-runtime disposition

| Conceptual owner | Wave-001 family | Disposition | Current reusable substrate | Missing before target implementation |
|---|---|---|---|---|
| `BODY_ADAPTATION_STATE` | Physical | COMPOSE_CURRENT_STATE | attributes, skills, `state.perks`, conditions, history | persistent adaptation/training evidence model where required; domain APIs for non-stat physical adaptations |
| `CORE_RESOURCE_STATE` | Recovery | REUSE_CURRENT_OWNER | `player.resources`, derived resource maxima, `simulation.recover`, authoritative time | passive-specific qualification/cap rules; avoid direct UI resource mutation |
| `MOVEMENT_ACTION_STATE` | Movement | DOMAIN_RUNTIME_REQUIRED | current traversal/athletics skills and world travel can provide inputs | normalized movement-action/tactical movement owner; current world travel is not equivalent to per-action movement state |
| `PERCEPTION_EVIDENCE_STATE` | Sensory | COMPOSE_CURRENT_STATE | Perception attribute, knowledge, sensory abilities, conditions, history | normalized observation/evidence/confidence semantics; privacy-safe evidence projection |
| `MENTAL_PRESSURE_STATE` | Mental / Will | COMPOSE_CURRENT_STATE | Will, Resolve, Focus, conditions, history | explicit pressure/fear/distraction/recovery state where behavior requires more than stat modifiers |
| `KNOWLEDGE_LEARNING_STATE` | Cognitive / Learning | COMPOSE_CURRENT_STATE | `state.knowledge`, registered skills, training, history | familiarity/error/study evidence contract; knowledge provenance rules for passive qualification |
| `COMBAT_ACTION_STATE` | Combat Habit | DOMAIN_RUNTIME_REQUIRED | current combat-related skills only | V08 tactical action runtime, encounter/action history semantics, deterministic action interfaces |
| `EQUIPMENT_HANDLING_STATE` | Weapon Familiarity | COMPOSE_CURRENT_STATE | inventory, equipment, equipment definitions, weapon-related skills, history | equipment-specific familiarity/practice state; current equipment `passive_perks` metadata is not an automatic passive resolver |
| `DEFENSIVE_REACTION_STATE` | Defensive Adaptation | DOMAIN_RUNTIME_REQUIRED | Defense skill/conditions can be inputs | V08 defensive reaction/action runtime and event evidence |
| `ENVIRONMENT_EXPOSURE_STATE` | Survival / Environmental | COMPOSE_CURRENT_STATE | Survival skill, conditions, world time/history | typed exposure/environment history and hazard/environment authority |
| `SOCIAL_CONTEXT_STATE` | Social / Behavioral | COMPOSE_CURRENT_STATE | relationships, NPC state, party, player/NPC knowledge, `social.py` | passive-specific social evidence/effect APIs; private NPC state must remain non-projectable |
| `TEAM_COORDINATION_STATE` | Leadership / Coordination | COMPOSE_CURRENT_STATE | party membership, relationships/social state, Leadership skill | tactical role/formation/assignment state and bounded coordination actions |
| `TECHNICAL_TASK_STATE` | Technical / Craft | COMPOSE_CURRENT_STATE | Engineering/Technical Systems/Crafting skills, knowledge, content/history, equipment/tools | typed task/workflow/quality evidence and domain action interfaces |
| `MEDICAL_CASE_STATE` | Medical / Recovery Practice | COMPOSE_CURRENT_STATE | Medicine skill, conditions, recovery/time/history | patient/case/protocol evidence model; medical actions must not be inferred from generic history |
| `ABILITY_EXECUTION_STATE` | Ability Synergy | REUSE_CURRENT_OWNER | `state.abilities`, ability/technique mastery, ability-specific resources, `powers.py`, history | passive composition interface around existing ability rules; no second ability owner |
| `HAZARD_RESISTANCE_STATE` | Resistance | COMPOSE_CURRENT_STATE | conditions, existing effective stats/perks, history | typed hazard family/exposure/resistance owner and resolver for non-stat resistance behavior |
| `CREATURE_FIELD_KNOWLEDGE_STATE` | Creature / Beast Interaction | COMPOSE_CURRENT_STATE | Creatures skill, `state.knowledge`, history | species/encounter evidence semantics; objective creature/world truth remains external |
| `INJURY_REHABILITATION_STATE` | Injury / Scar Adaptation | COMPOSE_CURRENT_STATE | conditions, recovery/time, physical/medical skills, history | durable injury/rehabilitation evidence beyond current condition records where required |
| `PROFESSION_WORK_STATE` | Profession | DOMAIN_RUNTIME_REQUIRED | current skills/time/history can be future inputs | accepted profession identity, work activity/schedule, competency and qualification owner |
| `INSTITUTIONAL_SERVICE_STATE` | Faction / Institutional | DOMAIN_RUNTIME_REQUIRED | Factions skill, knowledge/relationships/flags can be future inputs | explicit membership/role/credential/clearance authority; never derive permission from passive possession |
| `WORLD_EVENT_LEDGER` | Unique Event | LEDGER_CONTRACT_REQUIRED | generic `state.history`, flags, quests, knowledge | stable event identity and qualification-proof contract; anti-duplicate semantics |
| `STATUS_SYSTEM_EVENT_LEDGER` | Cosmic / System | LEDGER_CONTRACT_REQUIRED | generic history plus current ability/perk state | Status-system event identity, confirmation/provenance and replay/migration semantics |
| `CLASSIFIED_AUTHORIZATION_STATE` | Unknown / Classified | DOMAIN_RUNTIME_REQUIRED | current knowledge/privacy patterns can inform projection | explicit classified requirement packet, authorization/redaction/audit authority |

Result:
- **2** conceptual owners have a strong current authoritative owner to reuse directly: Core Resource and Ability Execution;
- **13** should compose existing state but still need normalized domain semantics for target behavior;
- **6** require a future runtime domain before their target semantics can exist;
- **2** require typed event-ledger contracts rather than treating generic history as sufficient authorization.

These counts are a current-runtime disposition, not a statement of canon importance.

---

# 5. Family-level implementation consequences

## 5.1 Physical

Current `state.perks` can represent a bounded modifier such as an effective attribute/derived adjustment if that is the accepted mechanic.

It cannot by itself represent:
- tissue adaptation history;
- body-part state;
- injury-specific behavior;
- training-load progression.

Do not add those meanings as opaque perk tags.

## 5.2 Recovery

Use current resource/time owners.

A recovery passive may alter a validated recovery transition, but:
- the resource owner commits the final value;
- current maxima remain rules-owned;
- the passive must not make Compose increment resources.

## 5.3 Movement and defensive/combat families

These are blocked from faithful implementation until the relevant tactical runtime exists.

Do not pre-implement them as:
- flags saying an action occurred;
- direct accuracy/evasion stat inflation;
- Android-local movement bonuses.

Their current documentation is design authority, not executable behavior.

## 5.4 Sensory / Cognitive / Creature / Investigator-adjacent effects

Knowledge and evidence must stay distinct.

A passive may improve:
- observation quality;
- interpretation;
- recall;
- confidence processing;

but it must not grant objective world truth.

Future projection must preserve:
- known;
- inferred;
- uncertain;
- hidden/classified.

## 5.5 Social / Leadership

Current social state provides legitimate inputs.

Passives cannot:
- expose private NPC goals/memories;
- directly overwrite relationship truth without social rules;
- imply mind control;
- convert Leadership into tactical formation state before such state exists.

## 5.6 Technical / Medical

Current skills are inputs, not full workflow owners.

Target passives need domain actions/cases/tasks so the game can prove:
- what happened;
- what was qualified;
- what output was improved;
- what safety constraints applied.

## 5.7 Ability Synergy

This family has the clearest existing owner.

Future synergy passives should wrap existing ability/technique APIs and resources rather than:
- copying mastery;
- copying cooldown;
- creating another power resource;
- bypassing discovery requirements.

## 5.8 Profession / Faction / Classified

These are high-risk for false authority.

A passive may never become proof of:
- employment;
- faction membership;
- security clearance;
- legal authority;
- classified access.

Those facts require their own accepted owner.

## 5.9 Unique / Cosmic events

A one-time event passive requires durable proof of the qualifying event.

Generic free-form history is insufficient as the final contract unless:
- event IDs are stable;
- qualification is deterministic;
- duplicate grant prevention is explicit;
- save/migration behavior is defined.

---

# 6. Current `state.perks` reuse rule

Future implementation may reuse `state.perks` as an **acquired-perk identity/effect container** only when the accepted design is compatible with its responsibilities.

Safe current responsibilities:
- stable acquired perk ID;
- provenance/source;
- tags;
- optional visibility;
- validated additive attribute/skill/derived modifiers.

Not safe to assume without further contract:
- complex domain state;
- counters/timers/stacks;
- event qualification proof;
- profession membership;
- institutional clearance;
- tactical reaction state;
- movement state;
- medical case state;
- knowledge truth;
- NPC private state;
- arbitrary nested target-owner data.

If Wave-001 implementation later expands the durable perk-record shape, it must use explicit schema/version/migration validation instead of silently storing new semantics in unvalidated dictionaries.

---

# 7. Projection migration boundary

## 7.1 Keep raw `state.perks` private

Do not send the raw container to Android.

Raw records can include:
- source;
- internal tags;
- hidden visibility state;
- modifier internals;
- future qualification evidence.

## 7.2 Existing status contributions remain valid

For a visible additive perk that modifies a visible stat, current deep status inspection can continue to report safe contribution provenance.

Hidden perk IDs must continue to collapse into unidentified modifier evidence.

## 7.3 Future explicit passive projection

A future passive-list projection requires an explicit versioned player-safe contract.

At minimum, design must decide which of these are safe:
- stable public passive ID;
- display name;
- known/hidden state;
- broad family;
- player-known acquisition explanation;
- broad effect text;
- stack/level if such semantics are actually adopted;
- source visibility;
- lock/qualification explanation.

It must explicitly exclude:
- hidden requirements;
- secret event IDs;
- classified authorization packets;
- private NPC evidence;
- internal owner/write-target paths;
- raw modifier maps;
- undiscovered world facts.

No field list here is implementation approval.

---

# 8. Save/migration consequences

Current save schema already persists `perks`.

That does not remove future migration work.

Before implementing the 230-passive target corpus, decide:
1. whether current `state.perks` remains the acquired-passive identity container;
2. which new passive fields are allowed in that record;
3. which domain-specific states live outside `perks`;
4. how old saves default missing passive metadata;
5. how deprecated/renamed passive IDs migrate;
6. how event qualification evidence is preserved;
7. how hidden/classified records are validated without leaking;
8. how Android projection versions change.

Do not create 23 new top-level state containers merely because the conceptual owner matrix contains 23 owner names.

Conceptual owner != mandatory top-level field.

---

# 9. Automated Phase-C integrity guard

New repository tool:

`tools/status_phase_c_audit.py`

New regression tests:

`tests/test_status_phase_c_audit.py`

The audit compares:
- `calibration/PASSIVES_WAVE_001.md`;
- owner/write-target matrix A;
- owner/write-target matrix B;
- owner/write-target matrix C.

It verifies:
- exactly 230 registry records;
- exactly 230 owner-matrix records;
- one-to-one ID coverage;
- no duplicate IDs;
- no missing IDs;
- no extra IDs;
- exactly 23 ID families;
- exactly 10 records per family;
- nonblank owner-row name;
- nonblank primary stage;
- nonblank conceptual write target;
- nonblank qualification evidence class;
- nonblank bounded effect.

This guard intentionally does not validate canon, numeric balance or runtime existence.

Its job is narrower: a Phase-C ownership normalization edit can no longer silently drop, duplicate or structurally empty one of the 230 existing passive records.

---

# 10. D-046 gap closed by this packet

Before this packet:
- family owners existed only as conceptual names;
- 230 owner/write-target rows existed;
- the documents explicitly deferred runtime mapping;
- current perk/runtime/projection capabilities were not dispositioned against those conceptual owners;
- the 230/230 owner-row milestone was documented but not guarded by a dedicated regression test.

After this packet:
- all 23 conceptual owner domains have an explicit current-runtime disposition;
- current `state.perks` reuse is bounded to what source code actually supports;
- domains requiring real future runtime owners are explicit;
- event-ledger requirements are separated from generic history;
- current player-safe perk effect projection and missing explicit passive-list projection are explicit;
- the 230-record ownership milestone has a machine-checkable guard.

This is a Phase-C refinement completion, not Phase-F implementation.

---

# 11. Remaining Phase-C / later work

Still open:
- parent-system numeric/range readiness;
- world/canon evidence integration;
- record-by-record canon review;
- final passive definition schema for runtime;
- acquisition/qualification runtime APIs;
- tactical owner implementation;
- profession/institution/classified owner implementation;
- typed event ledgers;
- explicit player-safe passive-list projection;
- Android passive UI;
- full implementation/save migration;
- runtime balance/test fixtures.

The next Phase-C refinement should consume this disposition rather than remapping the same conceptual owners again.

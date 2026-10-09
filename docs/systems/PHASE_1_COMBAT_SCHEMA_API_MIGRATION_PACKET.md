# THE GAME — Phase 1 Combat Schema & API Migration Packet

Status: **APPROVED D-032 COMBAT MIGRATION DESIGN / IMPLEMENTATION IN PROGRESS — consult the live Bulletin for task state**
Repository: jbob-coder/Text-rpg-game
Parents:
- docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md
- docs/systems/TACTICAL_COMBAT_MASTER_PLAN.md
- docs/systems/GATE_TWELVE_PHASE1_TACTICAL_ENCOUNTER_PACKET.md
- docs/systems/SAVE_AND_CONTENT_MIGRATION_MASTER_PLAN.md
- docs/android/ANDROID_CONSUMER_AND_PROJECTION_MAP.md

## 1. Purpose

Map the approved Phase 1 tactical design into the current Python engine, strict content loader, save format, Android bridge, and Compose consumer boundary without inventing a second authoritative game state.

This document is intentionally implementation-specific. It identifies the smallest safe migration path from current source to one playable Gate Twelve tactical encounter.

## Implementation-state checkpoint (2026-10-08 AST; source-backed, not a new task claim)

This packet is the **D-032 migration design**, not the live task queue. The design's pre-implementation baseline below must not be mistaken for the source tree after subsequent Phase 1 implementation. Before action, re-fetch `docs/AI_TASK_BULLETIN_BOARD.md` for task ownership and `docs/THE_GAME_MASTER_TASK_REGISTER.md` for acceptance and completion evidence.

- **D-069 — DONE:** tactical schemas, authoring/validation and pure grid core have been implemented in `src/textrpg/combat_schema.py`, `src/textrpg/combat_grid.py` and corresponding content/validation integration. Its accepted evidence is in the Master Task Register and D-069 Learning Ledger.
- **D-070 — DONE:** transient `CombatSession`/actor state, turn and action engine, movement/reactions and deterministic resolution have been implemented. Refer to `src/textrpg/combat_state.py` and `docs/evidence/D070_TRANSIENT_ENGINE_2026-10-08.md`.
- **D-071 — DONE:** knowledge-safe tactical decisions, objective/retreat logic and bounded AI implementation are evidenced in `docs/evidence/D071_TACTICAL_DECISIONS_2026-10-08.md`; see the source modules `combat_knowledge.py`, `combat_rules.py` and `combat_ai.py`.
- **D-072 — IN_PROGRESS / Silex at this checkpoint:** durable aftermath, injury and world-state publication remain owned by that task. No completed aftermath transaction is claimed by this documentation correction.
- **D-073/D-074 — BLOCKED at this checkpoint:** the provisional Gate Twelve fixture plus Python combat bridge, and then Android tactical consumption, are downstream of accepted D-072 completion. Do not treat a design sketch below as implemented bridge, UI, save capability or approved canon.

The sections that follow preserve the **original migration intent and historical starting assumptions**, including names of prospective APIs. Some planned modules now exist; others remain prospective. Check current source and the relevant finished-task evidence before treating any `must add`, `currently` or `no validator` statement as a live deficiency. No save-schema expansion or permanent Gate Twelve lore is authorized by this status note.

## 2. Historical source baseline before D-069 (not a live inventory)

Current GameState durable fields:
- seed;
- scene_id;
- turn;
- time_minutes;
- player;
- flags;
- relationships;
- knowledge;
- inventory;
- quests;
- npcs;
- party;
- abilities;
- equipment;
- perks;
- schema_version;
- history.

Current save schema:
- CURRENT_SCHEMA_VERSION = 1;
- strict unknown-field rejection on load;
- no tactical field;
- no migration framework yet.

Current content loader:
- validates scenes, quests, powers, registries, world_map;
- registries currently allow only knowledge, perks, items, conditions;
- LoadedContentPack.raw retains authored source;
- no tactical map/encounter validator.

Current AndroidGameSession:
- owns content, engine, GameState, save path;
- exposes scene/status/inventory/quests/map/visual/meta projection;
- actions include choose, travel, equip, unequip, cheat, save, load;
- no combat session/action API.

## 3. Core migration decision

Phase 1 tactical encounter state remains **transient authoritative Python state** and is not added to GameState schema v1.

Reason:
- Phase 1 explicitly does not require mid-combat save;
- changing GameState would force save schema v2 immediately;
- current persistence strictly rejects unknown fields;
- combat can commit durable consequences atomically after encounter resolution;
- this keeps blast radius smaller and rollback simpler.

Therefore:

GameState = durable world/RPG state.

CombatSession = transient authoritative tactical state owned by the Python application/session layer.

Aftermath = validated transaction from CombatSession into GameState.

If mid-combat save is later required, create save schema v2+ deliberately.

## 4. New Python module boundary

Recommended modules:

src/textrpg/combat_schema.py
- immutable/validated authored structures;
- coordinate;
- tactical map;
- action definition;
- encounter definition;
- actor archetype definition.

src/textrpg/combat_state.py
- transient EncounterState;
- TacticalActorState;
- awareness/contact state;
- initiative/activation state;
- combat event log.

src/textrpg/combat_grid.py
- adjacency;
- pathfinding;
- occupancy;
- LOS/supercover;
- cover edge resolution.

src/textrpg/combat_rules.py
- action legality;
- deterministic roll;
- attack/damage;
- movement resolution;
- conditions;
- objective resolution;
- reactions.

src/textrpg/combat_ai.py
- legal candidate generation;
- utility scoring;
- retreat;
- companion orders;
- developer diagnostics.

src/textrpg/combat_aftermath.py
- build/validate aftermath plan;
- atomic GameState commit.

This split is a target. If implementation proves a smaller file set clearer, modules may be combined while preserving responsibility boundaries.

## 5. Content schema decision

Do not place tactical records inside registries because current registry validation rejects unsupported categories.

Add explicit optional top-level content sections:

- tactical_maps
- combat_actions
- combat_actor_archetypes
- encounters

content_pack_from_mapping must:
1. read these sections;
2. require mappings;
3. call dedicated validators;
4. cross-reference them;
5. include them in LoadedContentPack or make typed accessors over raw.

The current vertical slice remains valid when all four sections are absent.

Backward compatibility:
- old content packs with no tactical records continue loading unchanged.



### 5A. OR-034 provisional D-073 content rule

D-073 may author the minimum tactical content needed to prove the bridge even though final Gate Twelve combat canon is not yet approved.

Constraints:

- the integration encounter is identified/evidenced as `PROVISIONAL_INTEGRATION`;
- provisional contact actors remain encounter-local and omit permanent `persistent_ref` values;
- generic fixture combat actions must use the existing `combat_actions` schema and runtime rules rather than creating a second weapon/ability system;
- do not add unsupported schema fields merely to mark fixture status; carry provisional status through supported encounter metadata plus evidence/documentation;
- fixture-only knowledge/condition records may exist only when needed for the bounded integration proof and must be enumerated in D-073 evidence;
- D-073 owns Python content + player-safe bridge integration only. D-074 owns Android tactical DTO/mapper/ViewModel/Compose consumption;
- OR-015 domain-versioning/redaction requirements apply when the tactical projection is introduced;
- no permanent lore, art, faction identity, save-schema expansion or new GameState owner follows from the fixture.

This removes canon ambiguity from the D-073 start gate without converting proposed content into final canon.

## 6. Tactical map schema

Minimum map record:

{
  map_id,
  version,
  width,
  height,
  z_layers,
  default_cell,
  overrides,
  transitions,
  deployment_zones,
  objective_anchors,
  exits
}

Prefer default-cell + sparse overrides for small rectangular Phase 1 maps instead of authoring 96 repetitive cell records.

Validator must expand/resolve to canonical cells for runtime.

Validate:
- stable uppercase IDs;
- bounds;
- positive movement cost;
- edge cover values;
- `los_blocked_edges` cardinal values;
- blockers;
- unique anchors;
- valid transitions;
- valid exits.

### 6.1 Canonical cell geometry fields

The resolved/default/override cell contract must support these independent geometry properties:

- `blocks_movement`: cell cannot be traversed/ended on;
- `blocks_los`: the cell itself is opaque;
- `los_blocked_edges`: zero or more opaque N/E/S/W shared boundaries;
- `cover`: directional N/E/S/W cover ratings 0/1/2.

`los_blocked_edges` is the canonical authored/API name for Phase 1 edge opacity.

Authoring semantics:
- `default_cell` may provide a default `los_blocked_edges` value;
- sparse overrides may replace/override that cell's directional edge set;
- strict validation rejects non-cardinal names and malformed values;
- the runtime canonical cell stores the normalized cardinal-order set/tuple;
- a boundary is opaque if either adjacent cell declares the corresponding edge/opposite edge;
- authoring both sides is allowed but not required;
- cover and LOS opacity remain independent.

This is an additive Phase 1 schema clarification. Existing content packs with no tactical sections remain unchanged.

## 7. Encounter schema

Minimum:
- encounter_id;
- map_id;
- location_id;
- trigger metadata;
- participants;
- deployment;
- objective_set;
- retreat policy;
- AI profiles;
- aftermath profile;
- time_cost_minutes;
- canon_status.

Encounter-local actor IDs are allowed only inside the encounter namespace.

Persistent NPC/player refs must resolve to existing authoritative state IDs.

### 7.1 D-069 persistent-ref resolution rule

The current durable state provides a canonical NPC ID owner through `GameState.npcs` / authored `initial_state.npcs`.

D-069 therefore supports authored `persistent_ref` only when it resolves to an existing durable NPC ID.

Validation is deliberately two-phase:
- pre-state tactical validation checks shape and stable-ID syntax;
- after `GameState` construction, a bounded persistent-ref validation pass resolves encounter participant refs against `set(state.npcs)`.

Unknown NPC refs reject the content pack.

The repository does not currently expose a canonical player stable-ID field. D-069 must not invent one. Until such an identity contract is introduced, player-backed tactical participants omit `persistent_ref` and use encounter-local `actor_id`; durable player binding belongs to a later runtime/bridge integration seam.

This is CPR-004 and remains inside D-069.

## 8. Combat actor adapter

Do not copy the full player/NPC state into tactical content.

Create resolved adapter/query interfaces.

Player adapter reads:
- current attributes/skills;
- derived initiative/accuracy/evasion/guard;
- resources/health;
- conditions;
- equipment;
- abilities/techniques;
- player knowledge.

NPC adapter reads:
- stable NPC state;
- authored combat archetype/stat profile;
- personality;
- knowledge;
- conditions/injury once NPC condition persistence exists;
- faction/doctrine when available.

TacticalActorState stores encounter-local mutable values such as:
- coord;
- facing;
- current tactical health view;
- action budget;
- awareness;
- temporary tactical statuses;
- active/inactive/incapacitated state.

Never write tactical coordinates into world-map state.

## 9. Deterministic event key

Reuse the repository's SHA-256 deterministic philosophy.

Combat event digest input:

state.seed
| encounter_id
| round_index
| activation_index
| event_index
| actor_id
| action_id
| target_key

event_index increments only for committed authoritative combat-resolution events.

Preview queries must not consume event_index.

This prevents UI recomposition from changing future rolls.

## 10. AndroidGameSession ownership

Add a private field conceptually equivalent to:

self._combat: CombatSession | None

Rules:
- None outside combat;
- exactly one active combat session;
- loading a durable save clears transient combat and restores pre/post-combat world state according to interruption policy;
- save() while combat is active should either be rejected with a stable public error or save only a documented pre-combat checkpoint.

Recommended Phase 1 behavior:
- reject ordinary save during active combat with COMBAT_SAVE_UNAVAILABLE;
- ensure pre-combat autosave/checkpoint exists before encounter start.

## 11. New bridge actions

Recommended AndroidGameSession methods:

start_combat(encounter_id)
- validates trigger/world location/state;
- creates deterministic CombatSession;
- returns player-safe view.

combat_move(path)
- active Jack only;
- validates same authoritative path query;
- returns updated view.

combat_action(action_id, target)
- validates and resolves one action.

combat_end_activation()
- explicit end.

combat_companion_order(npc_id, order, target?)
- validates available companion/order.

combat_retreat()
- validates retreat position/action.

combat_restart()
- clears transient state and restores pre-combat snapshot/checkpoint according to policy.

No generic “setCombatState” or raw mutation endpoint.

## 12. View/projection change

Extend Python _view_for with optional player-safe combat field.

Outside combat:
- combat: null or omitted according to mapper compatibility decision.

Inside combat, project only:
- encounter title;
- objective;
- visible cells;
- detected actors;
- current/last-known contact data;
- active actor;
- initiative visible to player;
- Jack action budget;
- legal actions;
- legal move cells/path info;
- known cover/hazards;
- companion order options;
- retreat availability;
- visible conditions;
- player-safe combat log.

Never project:
- hidden actor coordinates;
- raw AI candidates;
- utility scores;
- private goals;
- hidden faction;
- unrevealed abilities;
- secret objective branches.

## 13. Kotlin mapping

BridgeSnapshotMapper currently maps existing projection groups.

Migration:
1. add nullable combat DTOs;
2. mapper treats missing combat as null for backward compatibility;
3. all nested fields validate type/range;
4. unknown/invalid mandatory combat fields produce a stable mapping error;
5. combat DTO contains only player-safe data.

Suggested DTO families:
- CombatSnapshot;
- CombatCellView;
- CombatActorView;
- CombatActionView;
- CombatObjectiveView;
- CombatLogEntryView;
- CombatCompanionOrderView.

Do not pass arbitrary Map<String, Any> deep into Compose.

## 14. GameViewModel

Add explicit actions/events:
- startCombat;
- moveCombatActor;
- useCombatAction;
- endCombatActivation;
- issueCompanionOrder;
- retreatCombat;
- restartCombat.

ViewModel owns:
- request/busy/error presentation state;
- selection state may remain local Compose when it is purely presentational.

ViewModel must not compute:
- paths;
- LOS;
- hit result;
- cover modifier;
- damage;
- hidden detection.

## 15. Compose surface

Add a contextual tactical mode/surface only when combat != null.

The surface consumes:
- orthographic three-quarter tactical presentation;
- tap-first selection;
- bounded pan/zoom;
- action bar;
- objective;
- selected actor/target summary;
- end activation;
- retreat.

Selection/highlight can be local UI state, but legal cells/actions come from Python projection.

## 16. Save and interruption

Before encounter:
- capture a deep GameState snapshot;
- optionally write durable autosave if existing app lifecycle supports it.

During encounter:
- no schema-v1 tactical save.

On normal encounter completion:
- build aftermath;
- atomic commit to GameState;
- clear _combat;
- save may resume normally.

On app/session recreation without tactical persistence:
- restart from pre-combat durable state;
- do not synthesize partial aftermath.

## 17. Aftermath mapping to current GameState

Use existing fields where semantically correct:

player.resources
- health/resource results.

player.conditions
- persistent player injury/strain.

flags
- encounter/world-state consequences.

knowledge
- player-learned facts.

inventory/equipment
- consumables/loot/equipment changes.

quests
- objective/stage consequences through quest functions.

npcs
- Tamsin memory/goal/story updates;
- later persistent adversary state after V09 schema exists.

relationships
- authored social consequences.

time_minutes
- encounter world-time cost.

history
- one durable aftermath summary plus existing social/quest events as appropriate.

Do not dump the entire tactical event log into GameState.history.

## 18. Condition migration

The proposed COND_TUNNEL_LEG_INJURY must be added to registries.conditions before any effect references it.

Validate its modifier paths against the existing modifier contract.

Combat may call the same apply_condition path rather than writing condition dictionaries directly.

## 19. Trace Echo integration

ACTION_TRACE_SIGNAL_PULSE_TACTICAL adapts the current TECHNIQUE_SIGNAL_PULSE definition.

Do not duplicate resource/cooldown/drawback values.

Combat action adapter:
- checks technique availability;
- invokes shared technique-use/resource logic where possible;
- interprets its tactical sensory result separately;
- preserves COND_ECHO_STRAIN behavior.

If the current power API cannot expose a transactional validate/commit boundary, add one before tactical use rather than copying technique logic into combat_rules.py.

## 20. Content validator changes

validation.py should gain:
- validate_tactical_maps;
- validate_combat_actions;
- validate_combat_actor_archetypes;
- validate_encounters;
- cross-reference validator.

Tests must prove:
- old pack still valid;
- malformed new record rejected;
- encounter unknown map/action rejected;
- persistent NPC ref validated where possible;
- unknown condition/knowledge/item refs rejected through existing registries.

## 21. Error boundary

Add stable Android bridge error codes, for example:
- COMBAT_START_ERROR;
- COMBAT_ACTION_ERROR;
- COMBAT_MOVE_ERROR;
- COMBAT_ORDER_ERROR;
- COMBAT_RETREAT_ERROR;
- COMBAT_SAVE_UNAVAILABLE;
- COMBAT_STATE_ERROR.

Public messages remain safe/general.
Technical detail may remain developer-facing.

## 22. Test sequence

Python unit:
1. tactical schema validation;
2. grid/path/LOS/cover;
3. turn/action budget;
4. deterministic attack;
5. awareness/redaction;
6. AI legality;
7. encounter objective/retreat;
8. injury;
9. aftermath atomicity;
10. bridge combat view/actions;
11. old content/save regression.

Persistence:
- schema v1 round-trip unchanged outside combat;
- save rejected or pre-combat behavior during combat;
- post-aftermath save/load preserves consequences.

Android JVM:
- nullable combat mapping;
- malformed payload rejection;
- ViewModel action delegation;
- no rule calculation in mapper/UI.

Instrumentation:
- enter encounter;
- tap path;
- perform action;
- end activation;
- retreat/objective;
- rotate/recreate app according to interruption policy;
- post-combat save/load.

## 23. Implementation order

Smallest safe sequence:

1. add tactical authored schemas + validators;
2. add grid/coordinate/path/LOS pure functions;
3. add transient EncounterState and turn engine;
4. add action legality/resolution;
5. add awareness/cover;
6. add objective/retreat;
7. add AI;
8. add aftermath transaction;
9. add Gate Twelve structured encounter records;
10. add bridge combat field/actions;
11. add Kotlin DTO/mapper;
12. add ViewModel actions;
13. add minimal tactical Compose surface;
14. exact-head tests;
15. performance profiling;
16. only then add/refine tactical assets.

## 24. Rollback boundary

Until aftermath commits, the world GameState remains recoverable from the pre-combat snapshot.

If tactical implementation must be reverted:
- remove optional tactical content sections and combat modules;
- keep schema v1 unchanged;
- remove optional combat projection/actions;
- existing story/world loop continues.

This is the primary reason not to add combat state to schema v1 prematurely.

## 25. Gate to implementation

Implementation may start on the bounded combat slice when:
- this migration packet and the encounter packet are treated as active design authority;
- no conflicting newer combat contract exists;
- exact current branch/HEAD is verified;
- implementation task records the intended files/tests;
- no claim of Galaxy A02 compatibility is made before profiling.

## 26. Result

D-032 combat migration is now defined at first-pass implementation depth.

Still separate:
- progression migration;
- social migration beyond the Tamsin proof;
- item/economy migration;
- persistent adversary migration;
- final APK teardown/rebuild.

This packet does not implement combat.

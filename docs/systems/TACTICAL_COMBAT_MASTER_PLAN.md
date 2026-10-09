# THE GAME — Tactical Combat Master Plan

Status: **FIRST-PASS CONTRACT LAYER ESTABLISHED / D-069 THROUGH D-071 HEADLESS FOUNDATION VERIFIED / FULL ENCOUNTER INTEGRATION PENDING**
Parent authority:
- `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`
- `docs/systems/GAMEPLAY_SYSTEM_REBUILD_MATRIX.md`
- `docs/systems/PROGRESSION_MASTER_PLAN.md`

Approved presentation/interaction child authority:
- docs/systems/CAMERA_AND_TACTICAL_PRESENTATION_STANDARD.md

First-pass child contracts:
- docs/systems/TACTICAL_COORDINATE_OCCUPANCY_STANDARD.md
- docs/systems/TURN_INITIATIVE_ACTION_BUDGET_STANDARD.md
- docs/systems/MOVEMENT_PATHING_AND_POSITIONING_STANDARD.md
- docs/systems/LOS_DETECTION_AND_COMBAT_KNOWLEDGE_STANDARD.md
- docs/systems/DIRECTIONAL_COVER_TERRAIN_STANDARD.md
- docs/systems/COMBAT_ACTION_TARGETING_RESOLUTION_STANDARD.md
- docs/systems/INJURY_CONDITION_AFTERMATH_STANDARD.md
- docs/systems/COMBAT_AI_OBJECTIVES_RETREAT_STANDARD.md

## 1. Purpose

Define an original turn-based tactical combat system for THE GAME that can integrate with the existing authoritative state, NPC memory, equipment, abilities, world map, quests, and Android client.

Broad genre inspiration may include squad tactics, cover, line of sight, action economy, terrain, persistent injuries, and encounter objectives. The shipped system must use original terminology, formulas, UI, content, maps, classes, enemies, progression, and data structures.

## 2. Non-negotiable integration boundary

Combat is a gameplay-domain system.

Target flow:

`World state -> Encounter setup -> Tactical state -> Rules resolution -> Persistent aftermath -> Player-safe combat projection -> Android tactical UI`

Compose/UI may render:
- current unit;
- visible tiles/positions;
- known cover;
- legal actions;
- projected hit/impact information when intentionally player-facing;
- status;
- objectives;
- combat log.

Compose/UI must not:
- calculate authoritative damage;
- calculate hidden AI intent;
- decide line of sight independently;
- mutate inventory/stats directly;
- invent enemy knowledge;
- decide death/injury persistence.

## 3. Encounter record

Each encounter should eventually have:
- stable encounter ID or reproducible encounter key;
- world location/site;
- tactical map ID;
- participants;
- factions;
- objective;
- start conditions;
- escape/withdraw conditions;
- reinforcement rules;
- environmental state;
- reward/aftermath hooks;
- persistence policy.

Encounters may be:
- authored story;
- world event;
- faction conflict;
- beast encounter;
- rival encounter;
- defensive encounter;
- ambush;
- optional training/simulation if canon.

## 4. Tactical coordinate space

**Decision update:** the baseline tactical space uses a square grid. Exact tile size, diagonal policy, encounter footprint and cost formulas remain open.

Combat needs a distinct tactical coordinate layer.

Requirements:
- deterministic cell/position IDs;
- elevation/depth;
- occupancy;
- terrain type;
- cover edges;
- line-of-sight blockers;
- hazards;
- interactables;
- doors/gates;
- destructibility only if explicitly supported.

Tactical coordinates do not replace world or district coordinates.

## 5. Turn structure — Phase 1 ordering locked / D-070 verified

Combat is turn-based and resolves one bounded activation context at a time.

The Phase 1 ordering contract is now defined by `TURN_INITIATIVE_ACTION_BUDGET_STANDARD.md` and verified through D-070:
- eligible actors are snapshotted for the round;
- higher resolved initiative acts first;
- initiative is frozen for the current round;
- mid-round initiative changes apply on the next round snapshot;
- ties resolve by stable `actor_id` ascending;
- incapacitated actors are skipped;
- ordinary reinforcements join on the next round;
- each activation receives the bounded action budget and reaction-reserve lifecycle defined by the turn standard.

D-070 evidence: `docs/evidence/D070_TRANSIENT_ENGINE_2026-10-08.md`; authority merge `6b7cf6be32f88eaae75bd8bb3682c851b6a0965c`; PR #78 / workflow #403 `37734174295`.

Future tuning may revise the broader combat model through an explicit contract/migration, but UI code must not independently derive or hardcode a competing initiative order.

## 6. Action economy

The final system must define an original action-budget model.

Action categories may include:
- move;
- attack;
- ability;
- item;
- interact;
- defend/brace;
- reaction preparation;
- sprint;
- disengage;
- assist;
- retreat.

Each action needs:
- cost;
- requirements;
- range;
- target rules;
- interrupt/reaction behavior;
- resource costs;
- cooldown;
- consequences.

## 7. Movement

Document:
- movement allowance;
- terrain cost;
- climb/elevation;
- difficult terrain;
- occupied cells;
- allies/enemies passing rules;
- zones of control if used;
- sprint/dash;
- knockback/pull;
- forced movement;
- path preview;
- movement interruption.

Movement cannot be purely cosmetic because location and cover affect rules.

## 8. Cover and protection

Use an original cover model.

Possible categories:
- exposed;
- partial;
- strong;
- fortified/special.

Final names/formulas are undecided.

Need:
- directional cover;
- flank rules;
- elevation interaction;
- cover destruction if used;
- cover provided by units/objects if used;
- player-safe preview.

Do not copy another game's exact shield icons, percentages, or terminology.

## 9. Line of sight and visibility

Define separately:
- geometric LOS;
- detection/awareness;
- concealment;
- darkness/smoke;
- known last position;
- sensory abilities;
- hidden enemies.

Player-safe projection must not reveal undetected entities.

## 10. Accuracy / hit resolution

Final formula is undecided.

Inputs may include:
- attacker skill/attribute;
- weapon/ability;
- range;
- movement;
- target posture;
- cover;
- visibility;
- elevation;
- status;
- injuries;
- environmental effects.

The documentation must decide whether the UI shows:
- exact percentage;
- qualitative estimate;
- bounded range;
- no prediction.

Do not inherit another game's hit-percentage presentation by default.

## 11. Damage / defense / injury

Need a unified model for:
- raw damage;
- armor;
- resistance;
- penetration;
- shields/barriers if canon;
- health;
- wounds;
- incapacitation;
- bleeding/burning/toxin if implemented;
- death;
- capture;
- surrender;
- nonlethal outcomes.

Persistent injuries must propagate into world/NPC state if enabled.

## 12. Status and conditions

Combat conditions should use the same authoritative condition system where possible.

Potential categories:
- physical injury;
- sensory;
- movement impairment;
- suppression/control;
- fear/morale;
- environmental;
- ability-specific.

Avoid creating a parallel combat-only status system unless migration analysis proves necessary.

## 13. Reactions

Possible original reaction system:
- prepared reaction;
- intercept;
- defensive response;
- guard;
- opportunity response.

Need:
- trigger;
- reserve cost;
- priority;
- cancellation;
- visibility;
- AI policy.

Do not copy protected branded reaction terminology or exact implementation.

## 14. Objectives

Combat should not always be elimination.

Possible objectives:
- escape;
- survive;
- protect;
- retrieve;
- hold;
- disable;
- capture;
- rescue;
- investigate;
- reach exit;
- delay;
- nonlethal resolution.

Objective state belongs to encounter/quest systems.

## 15. AI

AI must use world/NPC traits where possible.

Inputs:
- faction doctrine;
- personality;
- fear;
- injuries;
- goals;
- orders;
- known player abilities;
- morale if implemented;
- cover availability;
- objective.

AI may:
- attack;
- reposition;
- retreat;
- protect allies;
- pursue;
- surrender;
- call reinforcements;
- use items;
- interact with environment.

## 16. Beasts in combat

Beasts should not merely be reskinned humanoid AI.

Document:
- territorial behavior;
- pack behavior;
- predator/prey behavior;
- body size;
- mobility;
- senses;
- weak points only if supported;
- flee thresholds;
- loot/provenance;
- environmental interactions.

## 17. Party / squad

**Target direction:** Jack is directly controlled by the player. Recurring companions use a hybrid order + constrained-autonomy model driven by deterministic authored state such as personality, discipline, loyalty/trust, fear, injuries, goals and faction doctrine.

Temporary allied NPCs may use narrower order sets. Exact command vocabulary and override limits remain future detail work.

Current narrative party state does not automatically define final combat control.

## 18. Persistent aftermath

Combat must write back:
- health/injury;
- resources;
- ammo/items if modeled;
- equipment state if modeled;
- NPC death/capture/escape;
- relationships;
- reputation;
- rival memory;
- quest state;
- loot;
- world control;
- time.

## 19. Android tactical surface

Target elements:
- tactical map;
- unit selection;
- legal movement;
- target preview;
- action bar;
- ability/item access;
- objective;
- combat log;
- selected-unit panel;
- enemy intel only if known;
- end-turn/activation control depending final model.

Must work at phone scale without copying another game's UI.

## 20. Pixel-art combat assets

Later asset families:
- unit directional/pose sprites;
- tactical terrain tiles;
- cover objects;
- target/selection markers;
- range/LOS overlays;
- status FX;
- ability FX;
- injury/downed states;
- beast combat sprites;
- environmental hazards.

Do not produce bulk combat art before the tactical grid/perspective and animation requirements are locked.

## 21. Balance documentation required

Before implementation:
- encounter duration target;
- party size target;
- action budget;
- movement ranges;
- damage/health bands;
- hit model;
- cover modifiers;
- healing/recovery;
- retreat cost;
- XP/reward;
- difficulty policy.

## 22. Implementation order

1. tactical coordinate/terrain model;
2. encounter state;
3. turn/activation model;
4. movement/LOS;
5. action economy;
6. attacks/damage;
7. conditions;
8. AI;
9. aftermath persistence;
10. player-safe combat projection;
11. Android tactical surface;
12. pixel-art assets;
13. authored test encounter;
14. integration with world/rival systems.

## 23. Verification

Required:
- deterministic rules tests;
- path/LOS tests;
- save/load during/after combat policy;
- AI legality tests;
- hidden-info tests;
- Android instrumentation;
- phone screenshots;
- performance;
- persistent aftermath checks.

## 24. First-pass decisions now resolved

The child standards now lock the Phase 1 prototype structure:
- cardinal four-way movement; no diagonal movement;
- one-cell actor footprints;
- explicit vertical transitions;
- round-start initiative snapshot from resolved initiative;
- stable actor-ID initiative ties;
- four action-budget units per activation;
- move action budget separated from movement points;
- deterministic reserved-budget reactions;
- supercover LOS tracing;
- awareness states UNKNOWN / SUSPECTED / DETECTED / IDENTIFIED;
- edge-based directional cover with Phase 1 +0/+10/+20 defense modifiers;
- deterministic margin-based attack contest;
- health zero => incapacitated by default, not automatic death;
- atomic persistent aftermath;
- deterministic utility-based AI using only actor-known information;
- companion order vocabulary HOLD / ADVANCE / FOCUS_TARGET / ASSIST / WITHDRAW.

## 25. Still unresolved or deliberately tunable

Still open:
- exact tactical map footprint limits;
- final movement/action tuning beyond Phase 1 defaults;
- final attack/damage/armor calibration;
- exact player-facing probability/impact display;
- morale as a dedicated system;
- ammunition policy;
- destructibility scope;
- larger-unit footprints;
- advanced anatomy/body-part targeting;
- encounter generation policy;
- final companion autonomy calibration;
- full tactical save/resume policy.

The structural contracts are implementation-ready enough for a bounded Phase 1 encounter. Tuning remains evidence-driven.

Runtime checkpoint: D-069 geometry, D-070 transient turns/actions and D-071 knowledge/objectives/retreat/AI are verified. See `docs/evidence/D071_TACTICAL_DECISIONS_2026-10-08.md`. D-072 durable aftermath and D-073/D-074 content, bridge and UI integration remain pending.

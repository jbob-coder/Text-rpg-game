# THE GAME — Phase 1 Solo Playable Parallel Track

Status: **ACTIVE PROGRAM TRACK / MINIMUM PLAYABLE VERTICAL SLICE / PARALLEL WITH CORPUS EXPANSION**  
Repository: `jbob-coder/Text-rpg-game`  
Parent authority: `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`  
Proof region: Gate Twelve  
Hardware direction: Galaxy A02-class low-end Android target

## 1. Purpose

Maintain a real playable line in parallel with the large documentation program.

The documentation corpus may continue expanding toward the full game while Phase 1 consumes only the subset of domain contracts required to prove that the game's core systems actually work together.

Phase 1 is not the final game and is not a throwaway demo. It is a bounded production-quality vertical slice whose architecture, IDs, saves, projections and tests must be reusable by later expansion.

## 2. Three-track program model

### Track A — Full reconstruction corpus

Continues documenting the complete game:
- world;
- characters/social;
- progression;
- items/economy;
- combat;
- adversaries;
- activities;
- quests/content;
- assets;
- UI planning;
- migrations;
- Android/release.

Track A is governed by the first-pass domain quota matrix and later quota revisions.

### Track B — Phase 1 solo playable

Builds the smallest integrated version that meaningfully represents THE GAME.

It may implement a system only when the specific contract needed by that slice is sufficiently clear.

It does not need to wait for unrelated full-world documentation.

### Track C — Synchronization / evidence

Keeps Track A and Track B consistent.

Every implemented Phase 1 behavior must map back to documentation. Every changed contract that affects Phase 1 must trigger an implementation-impact review.

## 3. Existing starting point

The current repository already contains a provisional Gate Twelve vertical slice with:
- content ID `CONTENT_VERTICAL_SLICE_01`;
- title `The Dead Relay`;
- provisional-canon status;
- 19 scenes;
- 31 choices;
- 4 quests;
- 1 character record;
- 1 power record;
- a 9-node / 8-edge Gate Twelve world map baseline.

These are starting evidence, not proof that Phase 1 is complete.

## 4. Phase 1 scope

Phase 1 is solo-player first.

"Solo" means Jack is the directly controlled player character. NPCs, allies and enemies still exist as stateful actors; multiplayer/network play is outside this phase.

The Phase 1 slice should stay centered on Gate Twelve and prove the following minimum loop:

`enter place -> perceive state/actors -> choose/act -> spend time/resources -> change persistent state -> travel/activity/investigate -> encounter consequence -> progress/obtain/use something -> save -> leave -> reload -> observe preserved consequence`

## 5. Phase 1 minimum functional quota

Phase 1 must include at least the following integrated requirements:

1. **One bounded playable region**
   - Gate Twelve remains the Phase 1 region;
   - current stable location IDs remain authoritative unless explicitly migrated;
   - travel/discovery/reachability remain engine-owned.

2. **One directly controlled player character**
   - Jack/player identity;
   - resources;
   - attributes/skills needed by the slice;
   - conditions;
   - equipment/inventory;
   - player-safe presentation.

3. **One meaningful recurring NPC relationship path**
   - stable NPC identity;
   - at least two relationship dimensions that can change;
   - remembered interaction or durable consequence;
   - knowledge/private-state boundary;
   - later scene/action reacts to prior state.

4. **One knowledge-gated gameplay chain**
   - player can learn a fact;
   - the fact changes an available/visible action or interpretation;
   - hidden knowledge remains hidden from UI until projected.

5. **One progression path**
   - earn progress through action/training/use;
   - at least one meaningful unlock, mastery step, skill change or equivalent;
   - persistence through save/load;
   - no arbitrary UI-only progression.

6. **One equipment/inventory loop**
   - obtain or already possess an item;
   - inspect/use/equip where legal;
   - authoritative state changes;
   - presentation reflects projected equipment/inventory state.

7. **One quest chain with persistent branching**
   - more than one meaningful resolution path;
   - quest state survives navigation/save/load;
   - at least one later consequence differs by earlier choice.

8. **One life/activity action**
   - training, work, study, recovery, investigation or another approved activity;
   - consumes time and/or resources;
   - creates a persistent result;
   - integrates with at least one other domain.

9. **One tactical encounter**
   - uses the approved square-grid, turn-based, action-budget direction;
   - movement and occupancy;
   - LOS/detection distinction;
   - directional cover at minimum;
   - legal attack/action resolution;
   - at least one non-elimination or retreat-capable objective path if practical for the first encounter;
   - persistent aftermath.

10. **One persistent injury/condition consequence**
    - encounter or authored event can create it;
    - it affects later state or available behavior;
    - recovery/removal path is defined.

11. **One world-state consequence**
    - a choice, quest, encounter or activity visibly changes later world/scene/actor state.

12. **Reliable save/load**
    - save schema/version honored;
    - Phase 1 state restores correctly;
    - no continuity depends on chat memory or Compose-local state.

13. **Minimal Android play surface**
    - startup/loading/error path;
    - Story/current location;
    - Map/travel;
    - Character/status access;
    - Inventory/equipment access;
    - Quest access;
    - contextual tactical-combat surface;
    - Settings/accessibility essentials.

14. **Player-safe projection**
    - UI consumes safe data;
    - no hidden NPC goals/knowledge or authoritative rule calculations move into Compose.

15. **Deterministic verification**
    - same state + seed + action produces the same authoritative result where deterministic rules apply;
    - core regression tests exist for the slice.

16. **Low-end performance path**
    - design and profiling target Galaxy A02-class hardware;
    - effects/unit counts/assets stay bounded;
    - no compatibility claim until actually measured;
    - physical-device acceptance is recorded separately when available.

## 6. Phase 1 documentation gate

A Phase 1 requirement may enter implementation when its direct contract is sufficiently defined.

It does **not** need every final-game domain to be complete.

Examples:
- Phase 1 combat needs the combat subset it uses, not every future enemy archetype.
- Phase 1 progression needs one valid route, not all final classes.
- Phase 1 world needs Gate Twelve plus required parent references, not the entire planet.
- Phase 1 UI needs the surfaces consumed by the slice, while final V11 refinement may remain deferred.

## 7. Non-goals for Phase 1

Phase 1 does not require:
- full world population;
- all classes/professions;
- all abilities/passives;
- complete economy simulation;
- every NPC;
- final global UI hierarchy;
- final asset catalog;
- mass procedural/generated content;
- multiplayer;
- final APK release packaging;
- every adversary hierarchy behavior;
- every future tactical mechanic.

## 8. Phase 1 exit gate

Phase 1 becomes a validated playable slice only when:
- the minimum functional quota above is satisfied or explicitly revised with rationale;
- the complete core loop can be played from a clean start;
- persistent choices survive save/load;
- no known hidden-state leak exists;
- exact-head automated tests pass for the implemented slice;
- Android build/install/start evidence exists for the selected test target;
- performance evidence is captured;
- known limitations are documented;
- master docs, task register, quotas and implementation status are synchronized.

A build merely launching is not enough.

## 9. Direction after Phase 1

After Phase 1 passes:
1. preserve it as the integration baseline;
2. continue full corpus expansion;
3. add systems/content in bounded vertical increments;
4. expand Gate Twelve or connect the next region only through documented world contracts;
5. refine V11 UI after upstream domains mature;
6. recalibrate documentation quotas;
7. repeat playable integration gates at larger scope.

## 10. Mandatory task-completion update protocol

Every completed task in Track A, B or C must answer:

- What changed?
- What evidence proves it?
- Which quota/domain changed?
- Which Phase 1 requirement changed?
- What dependency was unlocked?
- What is now the highest-priority next action?
- Did any prior NEXT instruction become stale?
- Does any master/index need synchronization?

At minimum, update:
- `docs/THE_GAME_MASTER_TASK_REGISTER.md`;
- `docs/MASTER_DOCUMENTATION_RECORD.md` when domain status changes;
- `docs/FIRST_PASS_DOMAIN_DOCUMENTATION_QUOTAS.md` when quota state changes;
- `docs/DOCUMENTATION_PROGRESS_LEDGER.md` when measurable totals change;
- implementation/evidence records when runtime work changes.

The project must not keep stale direction after a task is completed.


## 11. Phase 1 readiness checkpoint — tactical combat documentation

Requirement 9 (one tactical encounter):
- mechanical documentation: **CONTRACT-READY**;
- authored Gate Twelve encounter packet: **PROPOSED PACKET EXISTS** — docs/systems/GATE_TWELVE_PHASE1_TACTICAL_ENCOUNTER_PACKET.md;
- Python tactical runtime: **D-069/D-070 FOUNDATION + D-071 DECISION LAYER VERIFIED**; D-072 aftermath and later integration remain pending;
- Android tactical projection/UI: **NOT IMPLEMENTED**;
- exact-head tactical foundation and decision tests: **VERIFIED** — PR #79 / workflow #404 `37774598150`; Python 478/478 PASS; Android unit/build/package PASS; emulator 35/35 PASS; screenshot gate PASS; see `docs/evidence/D071_TACTICAL_DECISIONS_2026-10-08.md`. Prior D-070 proof remains in `docs/evidence/D070_TRANSIENT_ENGINE_2026-10-08.md`.

Requirement 10 (persistent injury/condition):
- generic injury/aftermath contract: **CONTRACT-READY**;
- existing player condition primitive: **CURRENT RUNTIME FOUNDATION EXISTS**;
- one specific Gate Twelve combat injury and recovery path: **PROPOSED IN THE ENCOUNTER PACKET**; runtime/catalog approval remains pending.

What this unlocks:
- a bounded Phase 1 combat schema/API migration packet can now be written without inventing core spatial/turn/LOS/cover/action rules;
- a single authored Gate Twelve encounter can now be specified against stable first-pass rules.

What it does not unlock:
- broad tactical implementation across the full game;
- final combat balance;
- final combat UI;
- mid-combat save;
- mass combat assets.

Current Phase 1 combat action: D-072 validated atomic durable aftermath is **IN_PROGRESS under Silex**. Do not claim or supersede that work while the Bulletin claim remains live. After D-072 is genuinely DONE, D-073 may be promoted under OR-034 for the bounded Gate Twelve content/Python bridge, followed by D-074 Android tactical presentation. D-071 remains complete under PR #79/run #404; see `docs/evidence/D071_TACTICAL_DECISIONS_2026-10-08.md`. Requirement 9 remains incomplete until the downstream authored encounter, bridge and Android UI are accepted.


## 12. Phase 1 readiness checkpoint — V05 social documentation

Requirement 3 (recurring NPC relationship path):
- current Tamsin seven-axis relationship state: **EXISTS**;
- current trust/suspicion branching: **EXISTS**;
- normalized relationship standard: **CONTRACT-READY**;
- recurring-character packet: **CONTRACT-READY**;
- explicit durable memory plus later memory-reactive content: **VERIFIED BY D-065** — completion head `e883205559c64d2e82614160bd6548c2c9332808`; evidence `docs/evidence/D065_TAMSIN_MEMORY_PROOF_2026-10-04.md`.

Requirement 4 (knowledge-gated chain):
- player/NPC independent knowledge model: **EXISTS**;
- Tamsin Gate Twelve knowledge branch: **EXISTS**;
- npc_knows / npc_not_knows content gating: **EXISTS**;
- privacy/knowledge standard: **CONTRACT-READY**;
- final Phase 1 regression/save-load verification: **PENDING**.

Track B combat update:
- GATE_TWELVE_PHASE1_TACTICAL_ENCOUNTER_PACKET.md now specifies a proposed Service Tunnel encounter, optional Tamsin participation, retreat-capable objective, four-actor cap, and a specific injury/recovery proposal;
- content IDs/opponent identities remain proposed and must not be treated as canon until approved.

Requirement 8 is no longer a breadth blocker: V10's bounded Phase 1 activity path is verified by D-068. Broader life-simulation expansion remains separate from Phase 1 acceptance.


## 13. Phase 1 readiness checkpoint — activities/life loop

Requirement 8 (one life/activity action):
- selected proof action: `TRAIN_POWER_FUNDAMENTALS_TWO_HOURS`;
- authored location: `TRACE_CHAMBER`;
- current `skill_train` effect: **EXISTS / VERIFIED THROUGH REAL CONTENT ROUTE**;
- current train/time/resource primitives: **EXIST / VERIFIED**;
- activity schema/time/training documentation: **CONTRACT-READY**;
- exact time/resource result: **VERIFIED** (+120 minutes, -16 stamina, -10 focus, Powers -> 2.0 from zero);
- save/load + exact runtime-tree regression execution: **VERIFIED**;
- current Android activity request/result path: **VERIFIED** through generic choice delegation and authoritative snapshot mapping;
- D-068-B invalid-entry/time-preflight atomic rollback: **VERIFIED**;
- evidence: `docs/evidence/D068_PHASE1_ACTIVITY_PROOF_2026-10-04.md`;
- authority proof merge: `e883205559c64d2e82614160bd6548c2c9332808`.

Status:
**PHASE 1 REQUIREMENT #8 SATISFIED / BOUNDED TRACE CHAMBER ACTIVITY PROOF VERIFIED.**

This does not complete the broader V10 activity/life-simulation target. Activity registry/migration, professions/jobs/economy, scheduled/background/offline activities, calendar semantics and final activity-specific UX remain later work.

This requirement does not need a new job/profession system for Phase 1.

Next breadth dependency: V07 Items/Economy/Loot.


## 14. Phase 1 readiness checkpoint — items and equipment

Requirement 6 (equipment/inventory loop):
- current flat inventory authority: **EXISTS**;
- current equip/unequip rules: **EXIST**;
- current Android inventory/equipment projection: **EXISTS**;
- current starting loadout: **EXISTS**;
- Maintenance Seal authored consumption: **EXISTS**;
- Dead Relay authored acquisition: **EXISTS**;
- V07 normalized documentation: **CONTRACT-READY**;
- exact-head Phase 1 regression/save-load verification: **PENDING**.

The selected proof is documented in:
- docs/systems/GATE_TWELVE_PHASE1_ITEM_EQUIPMENT_PACKET.md

Phase 1 does not wait for currency, vendors, crafting, durability, encumbrance, random loot, or a large item catalog.


## 15. Phase 1 boundary — persistent adversaries

V09 persistent-adversary/world-memory documentation is now first-pass complete.

Phase 1 does **not** require a persistent recurring adversary.

The proposed Service Tunnel tactical encounter may ship its first playable proof with encounter-local unidentified contacts.

If a survivor is later promoted into a recurring adversary, the promotion must follow:
- explicit persistent identity;
- perceived encounter memory;
- bounded adaptation;
- lifecycle;
- valid world routing;
- player-safe intel;
- save migration.

This prevents V09 scope from blocking the minimum solo playable slice.

The implementation mapping now exists at `docs/systems/PERSISTENT_ADVERSARY_SCHEMA_API_MIGRATION_PACKET.md`. It preserves this boundary: Phase 1 may complete without V09 runtime, and no Service Tunnel contact is auto-promoted merely to exercise the system.

## D-060 control-gate update

D-060 is complete as a program-control dependency.

Effect on Track B:
- the inventory/second-pass control gate no longer blocks progression, social, items, room-actor projection, activity or tactical implementation tasks whose other direct contracts are already satisfied;
- D-060 itself proves no playable requirement;
- each unlocked implementation/proof task must still satisfy its own save, privacy, deterministic, Android, performance and canon gates.

Use `docs/AI_TASK_BULLETIN_BOARD.md` for live claim eligibility and `docs/AI_20_TASK_EXECUTION_CAMPAIGN_2026-10-04.md` for ranked task intent.

## D-061 progression migration gate

D-061 is complete as the migration-design dependency for Phase 1 requirement 5.

Selected proof path:
- `ABILITY_TRACE_ECHO`;
- `TECHNIQUE_SIGNAL_PULSE`;
- authored one-hour practice;
- durable technique mastery + ability mastery;
- stamina/focus and world-time cost;
- save/load persistence;
- deterministic replay;
- player-safe progression projection.

Migration decision:
- retain GameState save schema v1;
- do not add a competing top-level progression owner;
- keep progression mutation in Python;
- add stable ability ID to the existing player-safe Python ability projection;
- add typed Kotlin ability/technique mapping because current `GameSnapshot` drops `status.abilities`.

D-061 supplied the migration contract. D-066 now supplies the executed runtime proof.

## D-066 Phase 1 progression proof

Phase 1 requirement 5 is now **SATISFIED BY A BOUNDED IMPLEMENTED PROOF**.

Verified Gate Twelve route:
- `ABILITY_TRACE_ECHO` and discovered `TECHNIQUE_SIGNAL_PULSE`;
- authored one-hour practice;
- technique and ability mastery gain;
- stamina/focus and world-time cost;
- save/load preservation;
- deterministic uninterrupted-vs-save-boundary replay;
- stable player-safe ability identity;
- typed Android ability/technique/resource projection;
- bounded Stats presentation with no UI-owned progression arithmetic.

Exact verification evidence:
- `docs/evidence/D066_PHASE1_PROGRESSION_PROOF_2026-10-04.md`;
- verification PR #42 at `48ce6223fb84c3d31457c7f1dacaec87ce0d3df2`;
- Android Pixel Client run #312 / `37250124885`;
- D-066 Python progression/persistence/determinism tests: PASS;
- Android JVM tests: PASS;
- Compose instrumentation compilation: PASS;
- connected API-35 emulator suite: 35 / 35 PASS;
- debug APK assembly/content verification: PASS.

This proves one reusable Phase 1 progression route. It does **not** mark full classes, professions, global rank design, progression population, or final progression UX complete.

Repository-level caveat:
- the aggregate Python job remains red because the unchanged room-projection test imports `pytest` while the workflow does not install it;
- no D-066 Python test failed.

## D-062 social migration gate

D-062 is complete as the migration-design dependency for Phase 1 requirements 3 and 4.

Preserved authority:
- stable `NPC_TAMSIN` identity and current seven relationship axes;
- Jack/player knowledge remains separate from NPC-private knowledge;
- current goal/story/party IDs and state owners remain unchanged;
- save schema v1 remains the bounded target; no competing top-level social container is introduced.

Implemented proof path:
- D-065 converged the bounded Tamsin memory/reaction proof on the current social/state owners;
- one explicit durable Tamsin memory is written through the authoritative engine path;
- later authored behavior reacts to that memory;
- save/load and deterministic behavior are verified;
- the private memory/knowledge/goal containers remain outside player-safe projection.

D-065 is **DONE / VERIFIED PRIMARY + D-065-B** at completion head `e883205559c64d2e82614160bd6548c2c9332808`; evidence: `docs/evidence/D065_TAMSIN_MEMORY_PROOF_2026-10-04.md`. Do not reopen or advertise it as READY without new regression evidence. Requirement 4's broader exact-head knowledge-chain acceptance remains a separate concern.

## D-063 items/economy migration gate

D-063 is complete as the migration-design dependency for Phase 1 requirement #6.

Selected proof remains the existing Gate Twelve loop:
- exact five-item starting inventory;
- authoritative equip / unequip through current slots;
- effective-stat contribution from equipped gear;
- `TAKE_DEAD_RELAY` acquisition;
- `USE_MAINTENANCE_SEAL` gate + consumption;
- save/load;
- player-safe Python -> Kotlin inventory/equipment projection;
- existing Compose equip/unequip controls.

Migration decision:
- retain save schema v1;
- retain flat `inventory` and slot-keyed `equipment`;
- retain current item and slot stable IDs;
- retain Python as rule owner and existing typed Android DTOs as consumer;
- harden nested inventory/equipment state validation and current item/effect content validation in D-067;
- do not require currency, vendors, crafting, durability, encumbrance or item instances.

D-067 is **DONE / VERIFIED PRIMARY + D-067-B** at completion head `0fd843a5ece0f87c74a262c7ecb6739d025b0678`; evidence: `docs/evidence/D067_PHASE1_INVENTORY_EQUIPMENT_PROOF_2026-10-04.md`, PR #65 / run #351. Phase 1 requirement #6 is therefore proven across authoritative inventory/equipment mutation, save/load and player-safe Android presentation. Do not reopen D-067 without new regression evidence.

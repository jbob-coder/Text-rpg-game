# THE GAME — First-Pass Domain Documentation Quota Matrix

Status: **ACTIVE / FIRST-PASS COVERAGE QUOTAS / NOT FINAL CORPUS TARGETS**  
Repository: `jbob-coder/Text-rpg-game`  
Parent authority: `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`  
Companions:
- `docs/DOCUMENTATION_CORPUS_ARCHITECTURE.md`
- `docs/DOCUMENTATION_PROGRESS_LEDGER.md`
- `docs/MASTER_DOCUMENTATION_RECORD.md`
- `docs/PHASE_1_SOLO_PLAYABLE_PARALLEL_TRACK.md`

## 1. Purpose

This matrix assigns the first concrete documentation quotas by area.

These are **minimum canonical documentation units for the first broad reconstruction-grade coverage pass**. They are not the final long-range documentation totals and they do not reinterpret the owner's historical 3,000 / 2,000 / 10,000 / 10,000 / 2,000,000 targets.

The purpose is to prevent one subsystem from becoming extremely deep while other game domains remain structurally thin.

## 2. Counting rule

A quota unit counts only when it is a durable, non-duplicate, semantically useful repository unit such as a:
- MASTER;
- STANDARD;
- CATALOG;
- PACKET;
- MATRIX;
- LEDGER;
- GUIDE;
- AUDIT;
- HANDOFF;
- EVIDENCE specification.

Large catalogs should prefer structured records inside a smaller number of authoritative documents/files instead of one Markdown file per record.

Empty shells, duplicate rewrites, artificial splits, stale copies, generated mirrors, and historical superseded files do not satisfy active first-pass quotas.

## 3. First-pass minimum quotas

| Volume / area | Minimum canonical units | Why this minimum exists |
| --- | ---: | --- |
| V00 — Authority / governance / continuity | 8 | Enough to own authority, branch policy, permissions, metrics, task state, cross-reference, handoff and program direction without overproducing control documents. |
| V01 — Existing-state audit / repository truth | 10 | Current source, branches, consumers, saves, tests, assets, migrations and technical debt need distinct evidence owners. |
| V02 — Visual / pixel / asset system | 12 | Identity, environments, actors, equipment, props, overlays, animation, provenance, composition, QA and production/migration need separate contracts. |
| V03 — Gate Twelve proof region | 10 | The proof region must cover geometry, routes, state, actors, content, assets, performance, verification and migration as a complete exemplar. |
| V04 — World development | 12 | Geography, political entities, settlements, travel, ecology, resources, beasts, population, institutions, balance, events and region packets all require durable authority. |
| V05 — Characters / NPC / social | 12 | Identity, personality, memory, knowledge, relationships, schedules, goals, factions, hierarchy, social consequences, recurring character packets and population rules need separation. |
| V06 — Progression / stats / abilities / classes | 12 | Large existing corpus needs balanced authorities for stats, skills, abilities, passives, classes, professions, ranks, training, mastery, progression UX, balance and migration. |
| V07 — Items / economy / loot | 10 | Item taxonomy, equipment, materials, quality, economy, vendors/services, loot, provenance, resource chains and migration require coverage. |
| V08 — Tactical combat | 10 | Coordinates, turn/action model, movement, LOS/detection, cover, attacks, injuries, AI, encounter objectives and aftermath need explicit contracts. |
| V09 — Persistent adversaries / world memory | 8 | Identity, memory, recurrence, promotion/demotion, hierarchy, adaptation, faction movement, persistence and consequences must be operationally defined. |
| V10 — Activities / life simulation | 8 | Work, study, training, recovery, travel, social activity, exploration, facility/schedule integration and interruption rules need coverage. |
| V11 — Application UI/UX planning | 8 | Current phase needs ownership, navigation principles, projections, screen families, accessibility, performance, state ownership and dependency mapping without prematurely finalizing UI. |
| V12 — Android / APK reconstruction | 8 | Runtime bridge, architecture, migration, teardown, build, testing, device acceptance and release provenance need distinct late-stage authorities. |
| Cross-domain guides / planning | 10 | Authoring, migration, balancing, testing, content-production and reconstruction procedures must connect the domains. |
| Cross-domain evidence / QA / migration | 10 | Exact-head verification, regression evidence, compatibility, performance, privacy and migration closure cannot be inferred from design docs. |

**First-pass minimum total: 148 canonical documentation units.**

## 4. This is a floor, not a cap

An area may exceed its first-pass quota when meaningful content requires it.

No area may claim completion merely by reaching its number. Reconstruction-grade status still requires:
- current reality;
- target design;
- ownership/state boundaries;
- schema/record shape;
- dependencies;
- integrations;
- migration impact;
- content requirements;
- UI/asset requirements where relevant;
- verification;
- unresolved decisions;
- implementation order.

## 5. Structured-record quotas are separate

The following should usually scale as records rather than standalone Markdown files:
- world places;
- routes;
- NPCs;
- factions;
- items;
- loot entries;
- abilities;
- passives;
- classes/professions;
- activities;
- encounters;
- quests;
- assets;
- evidence rows.

Their target volumes are assigned in later domain-specific quota waves after the first-pass contracts define valid schemas.

## 6. Recalibration gate

After all major domains meet first-pass reconstruction coverage, perform a fresh reproducible inventory and create the **final domain quota revision**.

That revision must consider:
- actual domain complexity;
- number of structured records;
- implementation surface;
- migration risk;
- verification burden;
- cross-domain dependencies;
- player-facing importance;
- remaining unknowns.

The later revision may raise, lower or redistribute quotas. It must explain the reason.

## 7. Direction rule

The active documentation direction is breadth before additional extreme depth.

When one domain substantially exceeds its first-pass depth while another remains below its minimum coverage, default effort should move toward the under-covered domain unless an explicit dependency blocks it.

## 8. Update rule

Whenever a task materially changes corpus coverage:
1. update the task register;
2. update the master documentation record if domain state changed;
3. update this quota matrix when a unit begins counting, stops counting, or changes ownership;
4. update the progress ledger with measurable totals when available;
5. identify the next under-covered dependency;
6. record any newly unlocked Phase 1 playable requirement.

Raw file count alone is never sufficient evidence that a quota has been satisfied.


## 9. Live first-pass coverage checkpoint — V08 tactical combat

V08 now has **10 / 10 minimum canonical first-pass units**:

1. TACTICAL_COMBAT_MASTER_PLAN.md
2. CAMERA_AND_TACTICAL_PRESENTATION_STANDARD.md
3. TACTICAL_COORDINATE_OCCUPANCY_STANDARD.md
4. TURN_INITIATIVE_ACTION_BUDGET_STANDARD.md
5. MOVEMENT_PATHING_AND_POSITIONING_STANDARD.md
6. LOS_DETECTION_AND_COMBAT_KNOWLEDGE_STANDARD.md
7. DIRECTIONAL_COVER_TERRAIN_STANDARD.md
8. COMBAT_ACTION_TARGETING_RESOLUTION_STANDARD.md
9. INJURY_CONDITION_AFTERMATH_STANDARD.md
10. COMBAT_AI_OBJECTIVES_RETREAT_STANDARD.md

Status: **FIRST-PASS QUOTA SATISFIED / RUNTIME NOT IMPLEMENTED / CONTENT PACKET STILL REQUIRED.**

This does not mean tactical combat is finished. It means the first broad reconstruction-grade contract layer now covers coordinates, turns, action budget, movement, LOS/detection/knowledge, directional cover/terrain, action resolution, injuries/aftermath, AI/objectives/retreat, and camera/presentation.

New direction after this quota closure:
- create one Gate Twelve Phase 1 tactical encounter packet;
- then shift breadth effort to the next under-covered high-dependency domain, V05 Characters/NPC/Social, unless a higher-priority repository audit blocker intervenes.


## 10. Live first-pass coverage checkpoint — V05 characters/NPC/social

V05 now has **12 / 12 minimum canonical first-pass units**:

1. NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md
2. NPC_CHARACTER_IDENTITY_PROFILE_STANDARD.md
3. NPC_PERSONALITY_BEHAVIOR_STANDARD.md
4. NPC_MEMORY_EVENT_STANDARD.md
5. NPC_KNOWLEDGE_BELIEF_PRIVACY_STANDARD.md
6. NPC_RELATIONSHIP_STATE_STANDARD.md
7. NPC_GOALS_DECISION_STANDARD.md
8. NPC_SCHEDULE_PRESENCE_STANDARD.md
9. FACTION_HIERARCHY_MEMBERSHIP_STANDARD.md
10. SOCIAL_CONSEQUENCE_RUMOR_PROPAGATION_STANDARD.md
11. RECURRING_CHARACTER_PACKET_STANDARD.md
12. TAMSIN_PHASE1_SOCIAL_PROOF_PACKET.md

Status: **FIRST-PASS QUOTA SATISFIED / CURRENT RUNTIME FOUNDATION PARTIAL / LARGE CONTENT CATALOGS STILL PENDING.**

Phase 1 impact:
- recurring NPC relationship architecture is contract-ready around Tamsin;
- knowledge-gated social architecture is contract-ready and substantially exists in current content;
- explicit memory proof still needs a bounded runtime/content addition;
- final schedule/location runtime remains future work.

Breadth direction after V05 closure: move to V10 Activities/Life Simulation because it has a smaller under-covered quota and directly blocks Phase 1 requirement #8. The Gate Twelve tactical encounter packet continues in parallel as Track B work.

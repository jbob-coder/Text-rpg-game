# THE GAME — Owner Directive Traceability Matrix — 2026-10-02

Status: **ACTIVE / P0 REQUIREMENTS TRACEABILITY**  
Repository: `jbob-coder/Text-rpg-game`  
Program branch: `docs/master-game-development-program`  
Parent authority: `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`

## 1. Purpose

This file decomposes the owner's expanded development directive into explicit repository requirements and points each requirement to its current documentation owner, implementation state, and next required action.

It exists so future sessions do not need to reconstruct the directive from chat history.

Status vocabulary:

- **DOCUMENTED** — a governing contract exists.
- **PARTIAL** — a contract exists but decisions/content/audit are incomplete.
- **PLANNED** — requirement is accepted but its child contract is not yet complete.
- **IMPLEMENTED PARTIAL** — runtime/code exists at a lower scope than the final target.
- **NOT IMPLEMENTED** — documentation may exist, but runtime does not.
- **BLOCKED** — execution is intentionally gated by prerequisite documentation/migration/evidence.

## 2. Requirement traceability

| Owner requirement | Current owner document(s) | Current state | Next action |
| --- | --- | --- | --- |
| Make `jbob-coder/Text-rpg-game` the priority game repository | `README.md`, `AGENTS.md`, `MASTER_GAME_DEVELOPMENT_PROGRAM.md`, priority context log | DOCUMENTED | keep historical reports subordinate; refresh when authority changes |
| Full game-development permission while preserving prior prohibitions | `MASTER_DIRECTIVE_EXECUTION_BREAKDOWN.md`, `AGENTS.md` | DOCUMENTED | apply only on reversible working branches unless an irreversible boundary requires approval |
| Documentation-first development | master program, task register, corpus architecture | DOCUMENTED | continue P0 audit/inventory before broad runtime migration |
| Preserve 3,000 / 2,000 / 10,000 / 10,000 / 2,000,000 targets | progress ledger, corpus architecture | DOCUMENTED, UNIT UNRESOLVED | measure multiple metrics; never invent a target unit |
| Record what can change / will change / must stay | `EXISTING_STATE_REWORK_DECISION_MATRIX.md`, live audit | PARTIAL | complete file/consumer-level branch audit |
| Pixel-art production rules | pixel runtime composition standard | DOCUMENTED | reconcile source masters/raster/code/QA stage per asset |
| Pixel-art creation list and stage list | pixel production/reuse ledger; Gate Twelve asset status matrix | DOCUMENTED/PARTIAL | populate exact branch/provenance and final identity assets |
| Document what already exists vs what is planned | live audit; production ledger; progress ledger | DOCUMENTED/PARTIAL | automated inventory + branch-aware asset stage extraction |
| Area-by-area pixel art rather than one giant generated map | Gate Twelve region master; room/actor packet standard | DOCUMENTED | apply same packet model to future districts/settlements |
| Character in-room sprites | room actor/panel/overlay standard | DOCUMENTED; IMPLEMENTED PARTIAL | formalize player-safe actor-presence projection |
| Character portrait/focus panel depending on who is present | room actor/panel standard; Android UX master | DOCUMENTED; NOT FINAL | build actor projection and contextual panels later |
| Jack visual identity and paper-doll | character pixel blueprints; approved reference doc; reuse ledger | DOCUMENTED; IMPLEMENTED PARTIAL | production front/back/directions/portrait family and QA |
| Tamsin identity/panel/actor consistency | vertical-slice content; character/actor docs | DOCUMENTED; IMPLEMENTED PARTIAL | provenance + turnaround + portrait family |
| Reusable overlays and text art without visual mismatch | pixel runtime standard; room actor/overlay standard | DOCUMENTED | enforce compatibility signature in manifests/QA |
| Reuse assets only when scale/perspective/palette/material/state fit | pixel reuse ledger | DOCUMENTED | record per-asset compatibility/provenance |
| Documentation cross-references and ownership | documentation cross-reference matrix | DOCUMENTED | keep every new authority linked into matrix |
| Identify what each document owns and consumes | cross-reference matrix | DOCUMENTED | add all future child docs to matrix |
| Identify what must be added/created/updated/upgraded | task register; rework matrix; domain masters | DOCUMENTED/PARTIAL | convert remaining UNKNOWN/PARTIAL items into tracked tasks |
| Game mechanics may be reworked/broken/rebuilt when necessary | rework matrix; save/content migration master | DOCUMENTED | no destructive migration before replacement/tests/rollback |
| Progression / skill trees / classes / ranks | progression master | DOCUMENTED; NOT FINAL BALANCE | resolve class taxonomy, caps, migration and UI trees |
| Stats / abilities / passives | progression master; gameplay rebuild matrix | DOCUMENTED/PARTIAL | preserve current seven-stat schema until explicit migration |
| Passive/player activities | progression/world docs; activity coverage still fragmented | PARTIAL | create dedicated activity/life-loop master contract |
| Citizen hierarchy / social class / institutional access | population hierarchy; NPC/social master | DOCUMENTED | populate only after political/cultural canon exists |
| Fictional prejudice/racism/discrimination systems | NPC/social master; population hierarchy | DOCUMENTED AT SYSTEM LEVEL | author regional/institutional variants without universal race score |
| World coordinates / places / zones / areas | world scale blueprint; geography standard | DOCUMENTED AT SCHEMA LEVEL | materialize coordinate-and-scale registry/standard and populate canon |
| Cities / towns / villages | settlement catalog | DOCUMENTED AT SCHEMA LEVEL | create actual settlements only after parent geography/politics |
| Kingdoms / nations / political entities | political entities document | DOCUMENTED AT SCHEMA LEVEL | author canon entities and borders later |
| Resources / ecosystems | ecosystem/resources standard | DOCUMENTED AT SCHEMA LEVEL | populate zones after geography/climate decisions |
| Beast zones | beast-zone standard | DOCUMENTED AT SCHEMA LEVEL | define beast taxonomy/distribution after ecology rules |
| Loot / items / accessories | item/economy/loot master; loot provenance standard | DOCUMENTED | integrate concrete item tables with world provenance later |
| NPC population of world | world NPC population standard; NPC/social master | DOCUMENTED AT SCHEMA LEVEL | populate named/supporting NPCs after settlement/faction canon |
| World level system and balance | world balance/level bands; balance integration plan | DOCUMENTED AT SCHEMA LEVEL | select concrete world bands only after combat/progression calibration |
| Turn-based tactical combat inspired by broad XCOM-like genre concepts | tactical combat master | DOCUMENTED; NOT IMPLEMENTED | prototype original turn/action model after progression/balance decisions |
| Persistent evolving adversaries inspired by broad Nemesis-like concept | NPC/social/rival master | DOCUMENTED; NOT IMPLEMENTED | implement original terminology/data/UI after NPC world simulation |
| Avoid copyright problems | tactical/NPC masters; reference policy | DOCUMENTED | use only broad mechanics, original expression/art/names/UI/data |
| Final APK development/evolution/breakdown/rebuild | APK rebuild/evolution master; final reconstruction matrix | DOCUMENTED; BLOCKED | execute only after domain contracts and migrations are ready |
| Decide what current APK code is kept/reworked/replaced/removed | final reconstruction matrix; rework matrix | DOCUMENTED/PARTIAL | complete exact Android consumer audit |
| Make the application the main polished player surface | Android UX master; Gate Twelve UX steps | DOCUMENTED; IMPLEMENTED PARTIAL | rebuild screen hierarchy incrementally from documented contracts |
| Preserve safe state ownership during APK rebuild | Android UX/APK docs; live audit | DOCUMENTED | enforce GameState/domain -> player-safe projection -> UI |
| Update old reports so they point at the current program | README, AGENTS, implementation-status pointer, V6 handoff pointer | DOCUMENTED/UPDATED | continue adding priority headers to any stale report discovered |
| Preserve continuity for future sessions | context logs; task register; cross-reference; handoff sections | DOCUMENTED | every major batch records HEAD/evidence/next action |

## 3. Child contracts exposed by this matrix

The directive is now covered at a master-document level, but several child contracts remain necessary before mass implementation.

### A. Dedicated activity/life-loop contract

Needed for:
- passive activities;
- jobs/professions;
- training;
- rest;
- study;
- social activities;
- travel-time activities;
- gathering/harvesting if approved;
- civic/world activities;
- scheduling/time cost;
- interruption;
- NPC participation;
- rewards/consequences;
- Android presentation.

Materialized child:
`docs/systems/PLAYER_ACTIVITIES_AND_LIFE_LOOP_MASTER_PLAN.md`.

Status: **DOCUMENTED / implementation remains future work**.

### B. Coordinate/scale operational contract

The geography/scale docs define layers, but mass map population needs an operational coordinate standard covering:
- units;
- bounds;
- transforms;
- parent/child anchors;
- route endpoints;
- settlement/district/local/tactical conversion boundaries;
- precision;
- negative coordinates;
- elevation/depth;
- map projections;
- validation;
- versioning.

Materialized child:
`docs/world/WORLD_COORDINATE_AND_SCALE_STANDARD.md`.

Status: **DOCUMENTED / canonical world spaces remain unpopulated**.

### C. Branch-aware asset provenance registry

Needed to reconcile:
- source master;
- generated/exported raster;
- Kotlin fallback;
- current consuming branch;
- superseded branch;
- QA evidence;
- canonical approval;
- reuse compatibility signature.

Materialized child:
`docs/assets/ASSET_PROVENANCE_REGISTRY.md`.

Status: **SCHEMA + INITIAL RASTER SEED / exact branch-source reconciliation still in progress**.

### D. Android consumer map

Needed to map:
`screen/component -> projected field/action -> domain owner -> asset packet -> tests/evidence`.

Materialized child:
`docs/android/ANDROID_CONSUMER_AND_PROJECTION_MAP.md`.

Status: **FIRST-PASS SOURCE-GROUNDED MAP / line-by-line consumer audit still in progress**.

## 4. Directive execution rule

No future agent should treat this matrix as permission to skip the domain masters.

This matrix answers **where each requirement is owned**.

The domain documents answer **how that requirement works**.

Implementation should proceed only when the relevant domain contract is sufficiently resolved and the migration/verification gate is known.

## 5. Priority after this traceability pass

P0 order:

1. complete branch/file/consumer existing-state audit;
2. execute and extend reproducible inventory;
3. populate the asset provenance registry with exact branch/hash/consumer evidence;
4. complete the Android line-by-line consumer/projection audit;
5. reconcile Gate Twelve implementation branches/assets;
6. decide first canonical parent-world/geography records before large-scale world population;
7. then resume bounded implementation against the documented target.

## 6. Continuity note

This matrix is the direct repository translation of the owner's 2026-10-02 expanded directive.

If chat context is unavailable, start with:
- `README.md`;
- `AGENTS.md`;
- `MASTER_GAME_DEVELOPMENT_PROGRAM.md`;
- this traceability matrix;
- `THE_GAME_MASTER_TASK_REGISTER.md`;
- the domain master relevant to the task.

Do not rebuild intent from old prototype reports when these current authorities exist.


## Operational coverage continuation

The decision/rebuild register now decomposes the renewed directive. The full document catalog covers all 76 baseline Markdown files. The world decision queue preserves exact local coordinates and open canon decisions. The room composition contract documents current actors and proposed panels. All 24 baseline rasters have concrete hash/dimension/binding evidence; branch and artistic acceptance remain open. The activity/life-loop master already exists, superseding the earlier row saying it still needs creation. Persistent adversary design requires patent-aware review as well as original expression; no clearance is claimed.


## 2026-10-02 final reconstruction integration update

The directive now has an integration-level child: `docs/FINAL_GAME_RECONSTRUCTION_BLUEPRINT.md`.

It closes the previous cross-domain gap between requirements that were documented separately but not expressed as one execution chain. It explicitly links:
`authority -> current-state audit -> asset stage/provenance -> area packet -> world canon -> mechanics migration -> Android consumer migration -> final APK teardown/rebuild -> verification`.

The blueprint does not mark unfinished runtime systems complete. It is a coordination/decision authority only.

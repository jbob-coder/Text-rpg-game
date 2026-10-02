# THE GAME — Documentation Cross-Reference Matrix

Status: **ACTIVE INDEX**  
Parent authority: `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`

This file answers: **what does each major document own, what does it reference, what must be added next, and which implementation consumes it?**

---

## 1. Authority order

| Document | Owns | Must not own |
| --- | --- | --- |
| `MASTER_GAME_DEVELOPMENT_PROGRAM.md` | repository priority, program scope, permissions, documentation sequence | low-level implementation details |
| `THE_GAME_MASTER_TASK_REGISTER.md` | operational task state | gameplay canon |
| `IMPLEMENTATION_STATUS.md` | verified current implementation snapshot | future design treated as implemented |
| `GAME_CONTEXT_LOGS/*` | durable user decisions/context | overriding live source/evidence |
| domain master docs | design contracts | hidden runtime facts not represented in source |

---

## 2. Existing core documents

### `docs/GAME_FOUNDATION.md`
Purpose:
- core game direction;
- high-level rules-engine philosophy.

Needs:
- audit against current master program;
- link to world/progression/combat/social volumes;
- contradictions logged rather than silently edited.

### `docs/VISUAL_BIBLE.md`
Purpose:
- general visual identity.

Needs:
- reconcile with current pixel-production standards;
- explicitly defer technical grids/anchors to `PIXEL_ASSET_MASTER_PLAN.md`;
- explicitly defer room/actor/overlay composition to `PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md`.

### `docs/IMPLEMENTATION_STATUS.md`
Purpose:
- exact verified implementation state.

Current issue:
- still frames V6 stabilization as the current objective.

Required update:
- preserve V6 evidence as historical;
- point current objective to documentation-first master program;
- list current Android/pixel/map branch stack as separate development evidence.

### `docs/V6_STABILIZATION_HANDOFF.md`
Purpose:
- historical evidence for engine stabilization.

Status:
- keep;
- do not rewrite into current project roadmap;
- label as historical engine handoff in higher-level indexes.

### `docs/THE_GAME_MASTER_TASK_REGISTER.md`
Purpose:
- operational queue.

Required update:
- P0 documentation program;
- priority-repository marker;
- Gate Twelve document sequence;
- world master;
- pixel runtime composition;
- final APK rebuild as late-stage task.

---

## 3. Pixel-art documentation

### `docs/assets/PIXEL_ASSET_MASTER_PLAN.md`
Owns:
- native grids;
- global pixel rules;
- character rig;
- scene/map/item standards;
- lifecycle;
- naming;
- quality gates.

References:
- character blueprints;
- production roadmap;
- manifests.

Needs:
- new link to runtime composition standard;
- explicit distinction between source-native master and scene composition;
- current player approved-reference pointer.

### `docs/assets/CHARACTER_PIXEL_BLUEPRINTS.md`
Owns:
- player body rig;
- Tamsin identity;
- anchors;
- equipment layering;
- character animation principles.

Needs:
- reconcile old “customizable generic player master” language with the later owner-approved Jack reference where current branch evidence supports it;
- never overwrite identity reference without provenance;
- add actor-panel/portrait mapping once projected actor contract exists.

### `docs/assets/REFERENCE_TO_BLUEPRINT_PIPELINE.md`
Owns:
- how external/generated reference becomes original source-native pixel art.

Needs:
- continue to prohibit direct smooth-image shipping;
- add exception only for already-valid deliberately authored pixel raster when QA proves it matches the production grid.

### `docs/assets/ASSET_PRODUCTION_ROADMAP_001-500.md`
Owns:
- first 500 planned visual units.

Status:
- planning baseline, not total world asset count.

Needs:
- eventual superseding roadmap for world-scale batches without renumbering or silently repurposing existing IDs.

### `docs/assets/GATE_TWELVE_MAP_PIXEL_ASSET_BLUEPRINT.md`
Owns:
- Gate Twelve visual geometry -> asset specification.

References:
- map master;
- area footprints;
- existing/code-present asset IDs.

Needs:
- remain subordinate to Gate Twelve Region Master Plan for region function/circulation;
- geometry changes require Step 5 geometry-contract update.

### `docs/assets/GATE_TWELVE_MAP_ANIMATION_BLUEPRINT.md`
Owns:
- static/ambient/state-driven animation classes;
- timing families;
- bounded first loops.

Needs:
- keep state-driven animations player-safe;
- later animation implementation must attach to runtime composition layers.

### `docs/assets/GATE_TWELVE_ASSET_STATUS_AND_PRODUCTION_MATRIX.md`
Owns:
- Batch 001 exact-ID/status audit;
- Gate Twelve per-area asset requirements;
- manifest/code drift;
- open-refinement separation;
- production ordering.

Current stage:
- Step 7 evidence source.

### `docs/assets/GATE_TWELVE_REGION_MASTER_PLAN.md`
Owns:
- region authority;
- spatial hierarchy;
- circulation;
- per-zone gameplay function;
- geometry contract;
- material/visual language;
- asset decomposition;
- Gate Twelve application UX;
- state layers;
- loading/performance;
- implementation order;
- verification;
- migration/removal;
- execution handoff.

Current stage:
- Steps 1–14 complete as the first proof-region planning packet;
- next consumer is exact implementation/asset reconciliation, not another region-planning step.

### `docs/assets/PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md`
Owns:
- how base art, characters, props, overlays, equipment, FX and panels coexist;
- reusable compatibility contract;
- actor-in-room rules;
- current-vs-planned asset-stage ledger.

This is the required bridge between visual documentation and actual Android composition.

---

## 4. World documentation

### `docs/world/WORLD_DEVELOPMENT_MASTER_INDEX.md`
Owns:
- world hierarchy;
- coordinate hierarchy;
- map-development records;
- political entities;
- settlements;
- ecosystems;
- resource zones;
- beast zones;
- population/NPC distribution;
- progression/world-level interaction.

Required future children:
- `WORLD_GEOGRAPHY_STANDARD.md`
- `WORLD_POLITICAL_ENTITIES.md`
- `WORLD_SETTLEMENT_CATALOG.md`
- `WORLD_ECOSYSTEM_AND_RESOURCES.md`
- `WORLD_BEAST_ZONE_STANDARD.md`
- `WORLD_TRAVEL_AND_ROUTES.md`
- `WORLD_POPULATION_AND_CITIZEN_HIERARCHY.md`
- `WORLD_BALANCE_AND_LEVEL_BANDS.md`

Do not create thousands of fictional records before schemas and Gate Twelve proof are stable.

---

## 5. Original requirements list — domain masters now materialized

### Progression master
Planned:
`docs/systems/PROGRESSION_MASTER_PLAN.md`

Must define:
- attributes;
- derived stats;
- skill taxonomy;
- ability taxonomy;
- passives;
- techniques;
- classes;
- professions;
- ranks;
- mastery;
- training;
- caps;
- resources;
- balance.

### Combat master
Planned:
`docs/systems/TACTICAL_COMBAT_MASTER_PLAN.md`

Must define:
- turn model;
- action economy;
- grid/positioning;
- cover;
- line-of-sight;
- targeting;
- movement;
- abilities;
- status/injury;
- AI;
- encounter persistence;
- tactical UI;
- tests.

### Social/NPC/rival master
Planned:
`docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md`

Must define:
- memory;
- goals;
- schedules;
- social relationships;
- hierarchy;
- recurring rival state;
- rank changes;
- encounter memory;
- faction propagation;
- persistence;
- original-system constraints.

### Economy/items master
Planned:
`docs/systems/ITEM_ECONOMY_LOOT_MASTER_PLAN.md`

Must define:
- item taxonomy;
- accessories;
- materials;
- quality;
- loot;
- resources;
- beast drops;
- repair/crafting only if approved;
- economy.

---

## 6. Android / APK documentation

### `docs/android/APK_REBUILD_AND_EVOLUTION_MASTER_PLAN.md`
Owns:
- late-stage audit;
- keep/rework/replace/remove classification;
- screen rebuild order;
- state-projection migration;
- visual integration;
- build/QA;
- APK evidence.

References:
- final world/system/visual contracts.

Rule:
- final APK reconstruction happens after the major design corpus is coherent enough to know what is being rebuilt.

---

## 7. Runtime/source documents

### `content/vertical_slice_01.json`
Owns:
- current provisional playable content.

Does not own:
- future world design;
- map art;
- speculative services.

### Python engine
Owns:
- authoritative gameplay state/rules.

### Android Compose
Owns:
- presentation and permitted actions.

### Asset catalogs/manifests
Own:
- renderable visual masters and their provenance/state binding.

---

## 8. Current implementation branches / PR lines

Repository work is currently distributed across stacked draft PRs.

Important current lines include:
- map authored art;
- player avatar refinement;
- opening story actors;
- mobile Bag;
- mobile Skills;
- Service Tunnel arrival/scene/atlas work;
- Quiet Stair refinement;
- Gate Twelve geometry documentation;
- Service Tunnel ambient animation.

Do not treat “open PR” as “canonical merged implementation.”

Each document that cites implementation must include exact branch/HEAD when it matters.

---

## 9. Required update rule

Whenever a major new document is created:

1. add it here;
2. add it to the relevant domain README/index;
3. add an operational task to the task register if implementation follows;
4. record user-decision context when the change originates from a conversation directive;
5. identify what older document it supplements or supersedes;
6. never erase old evidence solely because the roadmap evolved.

---

## 10. Historical initial sequence — superseded by operational continuation

1. finish Gate Twelve Step 5–14;
2. build existing-state audit;
3. build world geography schema;
4. build progression master;
5. build NPC/social/rival master;
6. build tactical combat master;
7. build items/economy/loot master;
8. build application UX master;
9. build final Android migration matrix;
10. only then schedule broad system reconstruction.

## 11. 2026-10-02 expansion documents

### `docs/MASTER_DIRECTIVE_EXECUTION_BREAKDOWN.md`
Owns:
- ordered program phases;
- broad permission interpretation;
- stop rules;
- dependency order.

References:
- Master Development Program;
- task register;
- all domain masters.

### `docs/EXISTING_STATE_REWORK_DECISION_MATRIX.md`
Owns:
- top-level KEEP / EXTEND / REWORK / REPLACE / REMOVE / NEW decisions.

Does not replace:
- the deeper source-file audit still required by task D-006.

### `docs/DOCUMENTATION_PROGRESS_LEDGER.md`
Owns:
- numeric target preservation;
- separate corpus metrics;
- completion-count rules.

### `docs/assets/PIXEL_ART_PRODUCTION_AND_REUSE_LEDGER.md`
Owns:
- production stages;
- current-vs-required asset lists;
- room actor/portrait/panel relationship;
- reuse classes;
- area packet requirements;
- text/overlay rules.

References:
- runtime composition standard;
- character blueprints;
- Gate Twelve asset matrix;
- manifests.

### `docs/world/WORLD_SCALE_DOCUMENTATION_BLUEPRINT.md`
Owns:
- world coordinate layers;
- place/political/settlement/resource/ecosystem/beast-zone/population schemas;
- map-record tracking rules.

References:
- world master index;
- future world child catalogs.

### `docs/systems/GAMEPLAY_SYSTEM_REBUILD_MATRIX.md`
Owns:
- current system disposition;
- target systems;
- implementation dependency order.

Defers detailed authority to future:
- progression;
- economy/items;
- NPC/social/adversary;
- tactical combat;
- balance;
- save migration masters.

### `docs/android/APK_FINAL_RECONSTRUCTION_MATRIX.md`
Owns:
- late-stage screen/component disposition;
- final rebuild sequence;
- removal gates;
- APK acceptance.

References:
- APK rebuild/evolution master;
- final domain contracts.

## 12. Historical expansion sequence — superseded by operational continuation

1. Gate Twelve Steps 8–14;
2. deep existing-state source audit;
3. progression/class/rank master;
4. NPC/social/adversary master;
5. item/economy/loot master;
6. tactical combat master;
7. world child schemas/catalogs;
8. application UX master;
9. save/content migration master;
10. final APK execution plan;
11. broad implementation only after required contracts.

## Newly materialized domain masters — 2026-10-02

### `docs/systems/TACTICAL_COMBAT_MASTER_PLAN.md`
Owns the original tactical-combat contract: encounter state, tactical coordinates, turn/action model decision space, movement, cover, LOS, damage/injury, AI, beasts, party control, aftermath, Android tactical surface, pixel-art dependencies and verification.

### `docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md`
Owns NPC memory/knowledge/goals/schedules, social hierarchy, institutions, fictional discrimination modeling, faction structure, and the original persistent-adversary framework.

### `docs/systems/ITEM_ECONOMY_LOOT_MASTER_PLAN.md`
Owns item schema, equipment/accessories, quality/rarity decisions, durability/crafting gates, loot provenance, beast materials, resources, economy, ownership/crime integration and visual requirements.

### `docs/systems/WORLD_BALANCE_INTEGRATION_PLAN.md`
Owns regional danger bands, progression/world integration, anti-snowball policy, encounter/loot/economy/training/rival/beast balance and future validation requirements.

### `docs/systems/SAVE_AND_CONTENT_MIGRATION_MASTER_PLAN.md`
Owns high-risk migration governance for stable IDs, save versions, quests, NPCs, items, map routes, visual IDs and rollback.

### `docs/android/APPLICATION_UX_MASTER_PLAN.md`
Owns the future Android information architecture, Story/current-location surface, room character panels, Map hierarchy, Character/Stats/Skills/Equipment/Inventory/Quests, tactical mode, narration, accessibility and responsive behavior.

All six are subordinate to `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`. Implementation remains gated by their unresolved decisions and exact live-source audits.


---

## 2026-10-02 corpus/world/visual child expansion

### `docs/DOCUMENTATION_CORPUS_ARCHITECTURE.md`
Owns:
- long-range documentation volume structure;
- unit types;
- branch families;
- cross-reference rules;
- record-scale strategy;
- ambiguous numeric-target tracking;
- documentation-before-destruction gate.

References:
- master program;
- directive breakdown;
- progress ledger;
- domain master documents.

### `docs/world/WORLD_GEOGRAPHY_STANDARD.md`
Owns:
- spatial containment hierarchy;
- W0–W4 coordinate roles;
- geography boundaries;
- terrain/water/climate placement logic;
- resource/beast/political geography relationships;
- scale policy.

Must not invent final world size or missing Gate Twelve parent geography.

### `docs/world/WORLD_POLITICAL_ENTITIES.md`
Owns:
- political entity schema;
- government/institution layers;
- territorial-control states;
- social hierarchy and discrimination-policy documentation;
- conflict/political-economy links.

Current world-scale catalog remains unpopulated until canon is authored.

### `docs/world/WORLD_SETTLEMENT_CATALOG.md`
Owns:
- settlement/district record schema;
- population/service/economy/visual-packet requirements;
- settlement production workflow.

Gate Twelve is the current local proof region; its larger settlement parent remains undecided.

### `docs/world/WORLD_TRAVEL_AND_ROUTES.md`
Owns:
- route classes;
- endpoint/access/discovery/travel/risk record;
- hierarchical travel;
- route migration;
- map-art versus route-authority separation.

### `docs/assets/ROOM_ACTOR_PANEL_OVERLAY_REUSE_STANDARD.md`
Owns:
- per-area art packet;
- actor-in-room contract;
- room sprite/portrait/focus-panel identity consistency;
- text/signage separation;
- overlay classes;
- animation ownership;
- reuse compatibility signature;
- visual QA.

This child standard does not own NPC presence. Player-safe projected engine state does.


---

## 2026-10-02 live audit and inventory controls

### `docs/LIVE_REPOSITORY_STATE_AUDIT_2026-10-02.md`
Owns:
- exact audited program HEAD;
- live open-PR/branch landscape snapshot;
- current repository structural counts;
- current implementation/pixel/world/system state;
- what may change versus what remains protected;
- immediate reconciliation controls.

Consumes:
- master program;
- rework decision matrix;
- task register;
- live GitHub metadata/tree.

Feeds:
- branch/provenance reconciliation;
- Android consumer map;
- Gate Twelve implementation restart;
- final APK reconstruction.

### `docs/REPOSITORY_CORPUS_INVENTORY_SNAPSHOT_2026-10-02.md`
Owns:
- exact structural counts for the audited program Git tree;
- distinction between measurable repository quantities and ambiguous owner numeric targets;
- inventory expansion requirements.

### `tools/documentation_inventory.py`
Owns:
- deterministic local structural/documentation inventory;
- Markdown word counting in a complete checkout;
- extension/document-family/test-source counts.

It does **not** own:
- canon;
- asset production status;
- executed-test results;
- target-unit interpretation.


---

## 2026-10-02 directive child-contract expansion

### `docs/OWNER_DIRECTIVE_TRACEABILITY_MATRIX_2026-10-02.md`
Owns:
- requirement-by-requirement mapping of the expanded owner directive;
- current document owner;
- current state;
- next action;
- missing child-contract detection.

### `docs/systems/PLAYER_ACTIVITIES_AND_LIFE_LOOP_MASTER_PLAN.md`
Owns:
- active/timed/scheduled/background activity classes;
- time, interruption, concurrency, training, study, work, recovery, social, diagnostics and future gathering boundaries;
- NPC/activity integration;
- persistence and player-safe activity projection requirements.

### `docs/world/WORLD_COORDINATE_AND_SCALE_STANDARD.md`
Owns:
- operational coordinate-space IDs;
- units/origins/axes/bounds;
- parent-child transforms;
- logical versus presentation coordinates;
- route anchors/distance types;
- elevation/depth;
- W0–W4 separation;
- coordinate versioning/validation.

### `docs/assets/ASSET_PROVENANCE_REGISTRY.md`
Owns:
- source/reference/raster/fallback provenance fields;
- production stage;
- branch/HEAD;
- hashes/dimensions;
- reuse compatibility;
- supersession;
- initial runtime-raster reconciliation queue.

### `docs/android/ANDROID_CONSUMER_AND_PROJECTION_MAP.md`
Owns:
- current `GameSnapshot` and `GameEngine` Android-facing contract;
- screen/component consumer ownership;
- safe actor/activity/world/combat projection gaps;
- final line-by-line Android consumer-audit target.


## 2026-10-02 operational continuation

- [Decision/rebuild execution register](DECISION_AND_REBUILD_EXECUTION_REGISTER.md): decomposed owner requirements, can/will/candidate changes, migration gates and unresolved corpus units.
- [Full baseline document catalog](DOCUMENTATION_CATALOG_2026-10-02.md): every tracked Markdown file, actual headings, words, hashes and literal references; semantic audit remains separate.
- [World canon decision queue](world/WORLD_CANON_DECISION_QUEUE.md): exact nine-node/eight-edge baseline and ordered unresolved geography/politics/ecology/progression decisions.
- [Room composition implementation contract](assets/ROOM_COMPOSITION_IMPLEMENTATION_CONTRACT.md): current actors versus proposed presence projection, focus panels, pixel/text reuse and raster-precedence gates.
- [Raster delivery evidence](assets/RASTER_DELIVERY_EVIDENCE_2026-10-02.md): all 24 baseline PNG dimensions, hashes and catalog bindings.

These supplement existing masters. They do not supersede approved identity references or imply new gameplay APIs.


## 2026-10-02 final reconstruction integration update

### `docs/FINAL_GAME_RECONSTRUCTION_BLUEPRINT.md`
Owns:
- integration across documentation domains;
- change authority vocabulary;
- current/provisional/planned visual-stage summary;
- Gate Twelve area production packet summary;
- decided-versus-undecided world canon snapshot;
- mechanics migration decision summary;
- final APK demolition/rebuild dependency order;
- P0 reconciliation packet.

References/consumes:
- master program;
- live repository audit;
- existing-state decision matrix;
- pixel runtime/reuse/provenance documents;
- Gate Twelve region/asset documents;
- world child standards;
- progression/social/items/combat/activity/migration masters;
- Android UX/consumer/APK masters.

Must not own:
- exact low-level formulas already owned by a domain master;
- implementation facts without exact source/HEAD evidence;
- invented world canon.

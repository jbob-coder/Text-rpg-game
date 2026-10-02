# THE GAME — Documentation Index

Status: **ACTIVE INDEX**
Authority parent: `docs/DOCUMENTATION_MASTER_PROGRAM.md`
Priority repository: `jbob-coder/Text-rpg-game`
Working branch: `docs/text-pixel-rpg-master-program`

This index tells future sessions what each document controls, what it references, and what is still missing.

| Document | Authority | Current purpose | References / depends on | Needs next |
| --- | --- | --- | --- | --- |
| `AGENTS.md` | operational entrypoint | rules for agents, verification, permissions | task register, implementation status | point to master documentation program |
| `README.md` | repository overview | run/test/project entrypoint | AGENTS, task register | point to priority/master docs |
| `docs/DOCUMENTATION_MASTER_PROGRAM.md` | **program master** | full documentation and reconstruction architecture | repository state, owner decisions | evolve only through explicit recorded decisions |
| `docs/DOCUMENTATION_INDEX.md` | navigation | cross-reference map for all design docs | master program | keep synchronized |
| `docs/GAME_FOUNDATION.md` | gameplay foundation | persistent authored RPG architecture | engine source | reconcile future systems without duplicating authority |
| `docs/VISUAL_BIBLE.md` | visual authority | global pixel-language rules | visual pipeline | cross-link contextual-panel/integration contract |
| `docs/assets/PIXEL_ASSET_MASTER_PLAN.md` | asset production | native grids, rigs, scenes, maps, item standards | visual bible | retain as production authority |
| `docs/assets/CHARACTER_PIXEL_BLUEPRINTS.md` | character art | player/NPC construction | asset master | extend only through versioned character rigs |
| `docs/assets/REFERENCE_TO_BLUEPRINT_PIPELINE.md` | asset lineage | reference -> blueprint -> native master process | asset master | retain |
| `docs/assets/ASSET_MANIFEST_SCHEMA.md` | machine-readable asset contract | state binding/provenance/QA | pipeline | extend if contextual panel fields need schema support |
| `docs/assets/GATE_TWELVE_REGION_MASTER_PLAN.md` | regional map authority | Gate Twelve region Steps 1–4 + future local plan | world graph, asset docs | continue local Steps 5–14 under global program |
| `docs/PIXEL_ART_INTEGRATION_CONTRACT.md` | app/art integration | scene composition, panel selection, overlays, reuse | visual bible, asset docs, player-safe projections | implement after projection audit |
| `docs/THE_GAME_MASTER_TASK_REGISTER.md` | execution queue | current tasks and evidence | repository/test state | add P0 documentation program task |
| `docs/IMPLEMENTATION_STATUS.md` | historical/runtime status | V6 stabilization state | runtime evidence | keep historical, add pointer to current program |
| `docs/V6_STABILIZATION_HANDOFF.md` | historical verification | V6 repair evidence | exact V6 candidate | do not rewrite into design authority |

## Planned normative documents

The following do not become authority until created and reviewed:

### World
- `docs/world/WORLD_BIBLE.md`
- `docs/world/GLOBAL_COORDINATE_SYSTEM.md`
- `docs/world/WORLD_ATLAS_SCHEMA.md`
- `docs/world/REGIONS_KINGDOMS_CITIES.md`
- `docs/world/SETTLEMENTS_AND_DISTRICTS.md`
- `docs/world/TRAVEL_AND_TRANSPORT.md`
- `docs/world/RESOURCES_AND_ECONOMY.md`
- `docs/world/ECOLOGY_AND_BEAST_ZONES.md`
- `docs/world/SOCIETY_HIERARCHY_AND_CULTURE.md`
- `docs/world/WORLD_EVENTS_AND_PRESSURE.md`

### Systems
- `docs/systems/STATS_AND_DERIVED_VALUES.md`
- `docs/systems/SKILLS_ABILITIES_PASSIVES.md`
- `docs/systems/CLASSES_RANKS_PROGRESSION.md`
- `docs/systems/ITEMS_EQUIPMENT_LOOT.md`
- `docs/systems/NPC_SIMULATION.md`
- `docs/systems/TACTICAL_COMBAT.md`
- `docs/systems/BALANCE_AND_WORLD_LEVELS.md`

### Application
- `docs/application/SCREEN_NAVIGATION_ARCHITECTURE.md`
- `docs/application/CONTEXTUAL_CHARACTER_PANELS.md`
- `docs/application/APK_RECONSTRUCTION_MASTER_PLAN.md`
- `docs/application/KEEP_REWORK_REPLACE_RETIRE_MATRIX.md`
- `docs/application/PERFORMANCE_AND_DEVICE_PLAN.md`

## Cross-reference rule

Every new normative document must include:
- parent authority;
- source files/data inspected;
- confirmed/adopted/proposed/unknown decisions;
- documents it supersedes, if any;
- documents it depends on;
- implementation targets;
- verification targets;
- continuity handoff.

A document that lacks provenance cannot silently become canon.

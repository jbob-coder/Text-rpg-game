# Moving-base document crosswalk — 2026-10-02

Repository: `jbob-coder/Text-rpg-game`  
Program branch: `docs/master-game-development-program`  
Source/base branch inspected: `docs/settlement-region-build-plan`  
Parent reconciliation: `docs/PR33_MOVING_BASE_DRIFT_RECONCILIATION_2026-10-02.md`

## Purpose

Map the moving-base documentation into the current documentation-program authority without creating duplicate active masters.

Disposition vocabulary:

- **KEEP PROGRAM** — current program document already owns the responsibility.
- **MIGRATE CHILD** — base material owns a useful narrower responsibility; adapt it under current authority.
- **EXTRACT UNIQUE** — only specific concepts should migrate into an existing owner.
- **BLOCKED** — do not migrate while an authority conflict remains.
- **HISTORICAL** — useful evidence on the base branch but not active authority.

## Crosswalk

| Moving-base document/family | Current program owner | Disposition | Reason |
| --- | --- | --- | --- |
| `docs/program/00_OWNER_DIRECTIVE_2026-10-02.md` | current owner handoff + master program | BLOCKED | Conflicts on target units: base says 2,000,000 separate files; current handoff says units unresolved. |
| `docs/program/01_DOCUMENTATION_PROGRAM_MASTER.md` | `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md` | KEEP PROGRAM | Same control responsibility; current program master is already active and more integrated. |
| `docs/program/02_WORLD_MAP_REGIONS_PROGRAM.md` | world master + geography/coordinate/route standards | KEEP PROGRAM | Existing current world authorities are more granular. |
| `docs/program/03_PIXEL_ART_ASSET_UI_PROGRAM.md` | pixel runtime/reuse/provenance docs | KEEP PROGRAM | Existing current visual authorities are broader. |
| `docs/program/04_CHARACTERS_NPCS_SOCIAL_PROGRAM.md` | NPC/social/rival master | KEEP PROGRAM | Same domain. |
| `docs/program/05_PROGRESSION_COMBAT_SYSTEMS_PROGRAM.md` | progression + tactical combat masters | KEEP PROGRAM | Existing current masters are broader. |
| `docs/program/06_ECONOMY_ITEMS_ECOSYSTEM_PROGRAM.md` | item/economy/loot + ecosystem standards | KEEP PROGRAM | Existing current masters own the domain. |
| `docs/program/07_ANDROID_APK_REBUILD_PROGRAM.md` | Android UX/APK reconstruction docs | KEEP PROGRAM | Existing program owns final rebuild sequencing. |
| `docs/program/08_DOCUMENTATION_GUIDE_SCALE_PROGRAM.md` | documentation corpus/progress ledger | BLOCKED/PARTIAL | Any scale rule depending on “2,000,000 files” remains blocked. |
| `docs/program/09_DECISION_GAP_REGISTER.md` | world decision queue + task register + open decisions in domain masters | EXTRACT UNIQUE | Useful gap discipline, but a second global gap authority would duplicate current tracking. |
| `docs/program/10_EXECUTION_COORDINATION_GRAPH.md` | master program + task register + cross-reference | EXTRACT UNIQUE | Graph vocabulary is compatible; current program already uses dependency ordering. |
| `docs/program/11_CONTEXTUAL_VISUAL_COMPOSITION_CONTRACT.md` | room composition contract + runtime composition standard | KEEP PROGRAM | Current files already own engine-presence/UI-presentation separation in greater depth. |
| `docs/program/12_DOCUMENT_EXPECTATION_AND_ACCEPTANCE_STANDARD.md` | corpus architecture + per-domain acceptance gates | EXTRACT UNIQUE | Acceptance lifecycle may be reused, but not as competing top-level authority. |
| `docs/program/13_BEAST_ENTITY_ECOSYSTEM_AND_SCENE_PRESENCE_STANDARD.md` | beast zone + ecosystem + scene-presence standards | EXTRACT UNIQUE | Separate useful field-level details from duplicate architecture. |
| `docs/program/14_DOCUMENTATION_COVERAGE_AND_EXPECTATION_MATRIX.md` | progress ledger/task register/cross-reference | EXTRACT UNIQUE | Coverage dimensions useful; one active progress authority only. |
| `docs/program/15_CONTEXTUAL_BEAST_PRESENCE_ADDENDUM.md` | beast/scene-presence docs | EXTRACT UNIQUE | Preserve player-safe presence concepts where not already explicit. |
| `docs/program/16_SESSION_DECISION_LOG_2026-10-02.md` | context logs/task register | HISTORICAL | Session evidence, not active authority. |
| `docs/assets/GLOBAL_ASSET_REUSE_OCCLUSION_MATRIX.md` | pixel runtime/reuse standard | MIGRATE CHILD | R0–R5 reuse taxonomy + explicit occlusion stack are useful operational detail. |
| `docs/systems/CLASS_RANK_SKILL_TREE_ARCHITECTURE.md` | `docs/systems/PROGRESSION_MASTER_PLAN.md` | KEEP PROGRAM | Current progression master already covers attributes, skills, abilities, passives, class, profession, ranks, training, migration. |
| `docs/systems/PERSISTENT_ADVERSARY_SYSTEM.md` | `docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md` | EXTRACT UNIQUE / HOLD | Current master already covers rivalry; exact mechanic combinations remain subject to originality/patent-aware review. |
| `docs/systems/TACTICAL_COMBAT_ARCHITECTURE.md` | `docs/systems/TACTICAL_COMBAT_MASTER_PLAN.md` | KEEP PROGRAM | Current tactical master is substantially broader and already owns implementation order/verification. |
| `docs/systems/WORLD_LEVEL_AND_BALANCE_ARCHITECTURE.md` | `docs/systems/WORLD_BALANCE_INTEGRATION_PLAN.md` | KEEP PROGRAM | Same philosophy and balance layers; current plan is active. |
| `docs/world/BEAST_ZONE_AND_ECOSYSTEM_SCHEMA.md` | beast-zone + ecosystem/resource standards | EXTRACT UNIQUE | Qualitative density bands and explicit migration-vs-player-route distinction are useful. |
| `docs/world/GATE_TWELVE_EXTERNAL_CONNECTIONS_AND_EXPANSION_REGISTER.md` | Gate Twelve region master + world decision queue | MIGRATE CHILD | Narrow responsibility for unresolved outward interfaces is useful and compatible with parent-world proposal. |
| `docs/world/REGION_SETTLEMENT_DOCUMENTATION_TEMPLATE.md` | world master + settlement catalog | MIGRATE CHILD | Execution template is useful and does not own canon. |
| `docs/world/WORLD_ENTITY_ID_AND_REFERENCE_STANDARD.md` | world master/geography standards | MIGRATE CHILD | Dedicated semantic-ID/rename/merge-split rules are useful and non-overlapping. |
| `docs/world/WORLD_MAP_PRODUCTION_SEQUENCE.md` | coordinate standard §30 + geography/route standards | KEEP PROGRAM / EXTRACT UNIQUE | Current production order already exists; no second process owner needed. |
| `docs/world/WORLD_SPATIAL_HIERARCHY_AND_COORDINATES.md` | world geography + coordinate standards | KEEP PROGRAM | Current standards are more detailed and already separate W0–W4/presentation/tactical spaces. |
| `docs/corpus/BATCH_0001/**` + `docs/production/**` | corpus architecture/progress ledger | BLOCKED | Depends materially on disputed “2,000,000 separate files” interpretation and introduces large-repository scaling risk. |

## Selective migrations in this batch

The following base ideas are adapted into current-program children:

1. `docs/assets/GLOBAL_ASSET_REUSE_OCCLUSION_MATRIX.md`
2. `docs/world/WORLD_ENTITY_ID_AND_REFERENCE_STANDARD.md`
3. `docs/world/REGION_SETTLEMENT_DOCUMENTATION_TEMPLATE.md`
4. `docs/world/GATE_TWELVE_EXTERNAL_CONNECTIONS_AND_EXPANSION_REGISTER.md`

They are subordinate to current active masters. Their presence does not activate the base-side program hierarchy.

## Explicit non-migrations

Not migrated in this batch:

- two-million-file corpus production;
- duplicate tactical-combat architecture;
- duplicate progression/class master;
- duplicate world-balance architecture;
- base-side Gate Twelve master;
- base-side master task namespace;
- persistent-adversary architecture as a replacement authority.

## Verification gate

After selective migration:
- all new child docs must point to current-program parents;
- no link may depend on `docs/program/*`;
- current Gate Twelve master/task register remain unchanged as authority;
- unresolved target units remain unresolved;
- no runtime code changes are implied.

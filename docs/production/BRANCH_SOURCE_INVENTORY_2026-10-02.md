# Branch Source Inventory — 2026-10-02

Status: **ACTIVE / REPOSITORY-WIDE SOURCE INVENTORY**
Repository: `jbob-coder/Text-rpg-game`
Priority working branch: `docs/settlement-region-build-plan`
Purpose: classify repository branches as source material for the long-horizon documentation corpus without treating every branch as equally authoritative.

## Authority rule

This inventory does not promote branch content into canon merely because the branch exists.

Current precedence remains:

1. exact current repository state on the active branch/ref;
2. fresh executed evidence;
3. explicit owner decisions recorded in active documentation;
4. active normative program/control documents;
5. domain/pilot specifications;
6. historical branch material;
7. external references;
8. chat memory.

Branch material must be extracted, compared, reconciled, and linked before it becomes current documentation authority.

## Classification labels

- **PRIMARY_ACTIVE** — current documentation-production authority branch.
- **PROGRAM_SOURCE** — documentation/planning branch with potentially reusable program material.
- **CONTEXT_SOURCE** — continuity/canon/context branch requiring reconciliation against current owner decisions.
- **SYSTEM_EVOLUTION_SOURCE** — historical or intermediate Python/game-system implementation and tests.
- **ANDROID_SOURCE** — Android/client/runtime implementation history.
- **PIXEL_UI_SOURCE** — pixel-art/UI/runtime presentation evolution.
- **PROTOTYPE_SOURCE** — experimental system/content branch; never automatic canon.
- **FIX_REVIEW_SOURCE** — focused corrective branch whose lessons/evidence may need migration.
- **INTEGRATION_SOURCE** — reconciliation/integration branch likely to contain migration decisions and tests.
- **HISTORICAL_BASELINE** — foundational earlier state useful for provenance and regression comparison.

## Branch inventory

| Branch | Classification | Primary value for documentation corpus | Required handling |
|---|---|---|---|
| `docs/settlement-region-build-plan` | PRIMARY_ACTIVE | Current owner directive, program controls, Gate Twelve master plan, numbered corpus/checkpoints, world-expansion work | Continue as current documentation authority until explicitly superseded |
| `context/shared-game-context` | CONTEXT_SOURCE | Large continuity/world-director/world-history corpus, narrative authority, live/offscreen world state | Deep-audit; extract current-compatible world/history/context records; mark conflicts |
| `shared/game-context` | CONTEXT_SOURCE | Architecture markouts, context protocols, stat-schema migration, game-direction records | Reconcile decisions; map useful docs; preserve historical context |
| `shared/game-context-ui-sync` | CONTEXT_SOURCE | Screen contracts, UI-sync checkpoints, earlier game-direction handoff | Audit for UI requirements still valid under current program |
| `docs/gate-twelve-map-pixel-asset-blueprint` | PROGRAM_SOURCE | Gate Twelve map/pixel asset blueprint plus mature Android/pixel runtime context | Map reusable asset/map contracts; do not duplicate implementation blindly |
| `docs/master-documentation-program` | PROGRAM_SOURCE | Broad documentation-program work and large application state snapshot | Reconcile against current program; harvest unique docs/decisions |
| `docs/master-game-development-program` | PROGRAM_SOURCE | Broad development program with extensive Android/pixel implementation context | High-priority deep audit for plans not yet represented in current program |
| `docs/pixel-asset-production-plan-v1` | PROGRAM_SOURCE | Pixel asset production planning and earlier Android client state | Harvest asset-production contracts and unresolved production decisions |
| `docs/text-pixel-rpg-master-program` | PROGRAM_SOURCE | Earlier master program spanning Android, UI, assets and game systems | Compare with current owner directive; migrate unique compatible requirements |
| `docs/visual-integration-recovery-plan` | PROGRAM_SOURCE | Visual/UI recovery and integration planning | Extract migration/recovery rules and unresolved visual integration work |
| `feature/ability-progression-v1` | SYSTEM_EVOLUTION_SOURCE | Early progression/powers/stats implementation and tests | Historical system baseline; compare forward evolution |
| `feature/ability-progression-v2` | SYSTEM_EVOLUTION_SOURCE | Progression revision plus review/visual content | Extract deltas and review decisions |
| `feature/ability-progression-v3` | SYSTEM_EVOLUTION_SOURCE | Adds CLI/content integration around ability progression | Extract system/API evolution and test coverage |
| `feature/ability-progression-v4` | SYSTEM_EVOLUTION_SOURCE | Later ability/progression implementation state | Compare against integration/rules branches before adoption |
| `feature/effective-stat-pipeline` | SYSTEM_EVOLUTION_SOURCE | Effective-stat/modifier pipeline and tests | High-value source for stat architecture and modifier semantics |
| `foundation/text-rpg-systems` | HISTORICAL_BASELINE | Early coherent Python text-RPG foundation across core systems | Preserve as baseline; use for provenance/regression, not current authority |
| `review/effective-stat-contract-hardening` | FIX_REVIEW_SOURCE | Stat contract review/hardening evidence | Extract identified defects, contracts and test expectations |
| `review/effective-stat-contract-hardening-v2` | FIX_REVIEW_SOURCE | Second hardening iteration | Compare with v1/v3; retain only still-relevant findings |
| `review/effective-stat-contract-hardening-v3` | FIX_REVIEW_SOURCE | Third hardening iteration | Treat as latest review lineage before later integration evidence |
| `integration/rules-ability-v1` | INTEGRATION_SOURCE | Integrated rule/ability system, schemas, status/modifier state and tests | Reconciliation source |
| `integration/rules-ability-v2` | INTEGRATION_SOURCE | Review-backed integration evolution | Extract review deltas |
| `integration/rules-ability-v3` | INTEGRATION_SOURCE | Continued rule/ability integration | Compare lineage |
| `integration/rules-ability-v4` | INTEGRATION_SOURCE | Same head lineage as v3 at inventory time | Detect duplicate ancestry; avoid duplicate documentation |
| `integration/rules-ability-v5` | INTEGRATION_SOURCE | Later integration with explicit V5 review | High-priority source for rules/ability migration history |
| `integration/rules-ability-v6-reconcile` | INTEGRATION_SOURCE | V6 reconciliation plus broader stabilization state | High-priority technical source; reconcile with current application state |
| `fix/v6-runtime-boundaries` | FIX_REVIEW_SOURCE | Runtime-boundary correction, verification logs and candidate/baseline evidence | Preserve verification evidence; extract runtime-boundary contracts |
| `feature/android-runtime-bootstrap-v1` | ANDROID_SOURCE | Earliest Android bridge/bootstrap architecture | Historical Android migration baseline |
| `feature/android-pixel-client-v1` | ANDROID_SOURCE | Pixel-client Android architecture/tests | Compare with open-world and later UI branches |
| `feature/android-open-world-v1` | ANDROID_SOURCE | Android open-world evolution | Extract world/client boundary and navigation architecture |
| `integration/android-open-world-v1-reconcile` | INTEGRATION_SOURCE | Android/open-world reconciliation plus validation docs | High-priority source for final APK audit/migration planning |
| `feature/character-equipment-paperdoll-ui` | PIXEL_UI_SOURCE | Equipment/paperdoll UI and pixel catalogs | Extract layered character/equipment UI contracts |
| `feature/character-stats-inspection` | PIXEL_UI_SOURCE | Character stats inspection UI plus tests | Extract player-safe inspection/state projection rules |
| `feature/player-safe-stat-inspection` | PIXEL_UI_SOURCE | Earlier player-safe stat projection | Compare with later character-stats branch; preserve security/state-boundary lessons |
| `feature/player-safe-skills-ui` | PIXEL_UI_SOURCE | Player-safe skills UI | Extract skills projection/UI contract |
| `feature/mobile-bag-pixel-art` | PIXEL_UI_SOURCE | Mobile bag pixel presentation | Extract inventory visual rules and asset references |
| `feature/mobile-skills-pixel-layout` | PIXEL_UI_SOURCE | Mobile skills layout | Extract responsive/skills visual contract |
| `feature/opening-story-actor-pixel-art` | PIXEL_UI_SOURCE | Opening story actor art/composition | Extract story/actor scene composition rules |
| `feature/story-scene-first-pixel-art` | PIXEL_UI_SOURCE | Story-first scene art integration | Extract scene composition and runtime consumer relationships |
| `feature/story-pixel-resource-hud` | PIXEL_UI_SOURCE | Story resource HUD integration | Extract resource-state HUD projection rules |
| `feature/pixel-asset-wave-a` | PIXEL_UI_SOURCE | Early coordinated asset wave | Asset lineage source |
| `feature/pixel-asset-wave-l-environment-modules` | PIXEL_UI_SOURCE | Environment module asset wave | Extract modular environment asset contracts |
| `feature/pixel-asset-wave-m-diagnostic-reader` | PIXEL_UI_SOURCE | Diagnostic-reader/held-prop asset wave | Extract special prop/state presentation contracts |
| `feature/pixel-assets-existing-reuse-b` | PIXEL_UI_SOURCE | Reuse of existing pixel assets | High-value source for reuse/occlusion/lifecycle rules |
| `feature/pixel-assets-runtime-expansion` | PIXEL_UI_SOURCE | Runtime expansion of pixel asset catalogs | Extract asset-consumer/runtime expansion map |
| `feature/png-pixel-art-runtime-a` | PIXEL_UI_SOURCE | PNG pixel-art runtime integration | Extract asset format/runtime loading contracts |
| `feature/pixel-map-art-pass` | PIXEL_UI_SOURCE | Map-art integration | Extract map-art runtime projection and Gate Twelve visual lineage |
| `feature/player-base-art-pass` | PIXEL_UI_SOURCE | Base player art integration | Base avatar visual lineage |
| `feature/player-avatar-art-pass` | PIXEL_UI_SOURCE | Later avatar art/reference integration | High-priority player identity/overlay/source-reference lineage |
| `feature/gate-twelve-map-surface-texture` | PIXEL_UI_SOURCE | Gate Twelve surface texture/art pass | Map visual/material lineage |
| `feature/quiet-stair-scene-art-pass` | PIXEL_UI_SOURCE | Quiet Stair scene-specific art pass | Location art/scene source |
| `feature/service-tunnel-arrival-pixel-art` | PIXEL_UI_SOURCE | Service Tunnel arrival art | Location art/source lineage |
| `feature/service-tunnel-scene-art-pass` | PIXEL_UI_SOURCE | Service Tunnel scene art pass | Location composition lineage |
| `feature/service-tunnel-atlas-detail` | PIXEL_UI_SOURCE | Service Tunnel atlas/detail evolution | Asset-detail/atlas source |
| `feature/service-tunnel-ambient-animation` | PIXEL_UI_SOURCE | Ambient animation iteration | Animation-state source |
| `feature/service-tunnel-ambient-animation-stack` | PIXEL_UI_SOURCE | Later animation stack plus explicit test coverage | High-priority animation contract/test source |
| `fix/avatar-overlay-rig-contract` | FIX_REVIEW_SOURCE | Avatar/equipment overlay rig correction | Extract overlay alignment, anchor and state-ownership fixes |
| `fix/player-hub-runtime-recovery` | FIX_REVIEW_SOURCE | Player hub runtime recovery | Extract failure mode, recovery and UI/runtime integration lessons |
| `prototype/medieval-crystal-contracts` | PROTOTYPE_SOURCE | Beast ecology, harvesting, memory, forging, medieval/world prototype systems | Idea/evidence source only; reconcile terminology/IP/current direction before adoption |
| `prototype/medieval-crystal-combat-contracts` | PROTOTYPE_SOURCE | Combat, armor, forge, hierarchy, beasts/crystals/adaptations prototype | High-value mechanics prototype; never automatic canon |

## Repository-wide findings

1. Branch history is cumulative: many later branches contain large portions of earlier Android/pixel/system work.
2. A raw count of changed files per branch therefore cannot be treated as unique content count.
3. Several branch families represent evolution chains rather than independent designs.
4. Some branches share identical or near-identical heads; integration/rules-ability-v3 and v4 are one obvious duplicate lineage at inventory time.
5. Context/history branches contain hundreds of files not represented by the current numbered corpus and require a separate deep-audit phase.
6. Pixel/UI branches contain both code and documentation; they must be decomposed into asset contracts, UI behavior, state ownership, runtime consumers, tests and migration evidence.
7. Prototype branches contain substantial mechanics work but remain non-authoritative until reconciled with the current original-IP and documentation program.
8. Current corpus production remains at DOC_0000001–DOC_0000020 verified; branch mining must feed future manifests instead of bypassing immutable ID control.

## Deep-audit sequence

### Phase BR-1 — Documentation-only extraction
For every branch:
- enumerate `docs/**`, `context/**`, `README*`, handoffs, checkpoints and review reports;
- identify files absent from the active branch;
- classify KEEP / UPDATE / REWRITE / SUPERSEDE / MERGE / DELETE;
- map each unique source to a domain and future numbered-document ownership.

### Phase BR-2 — Code/system extraction
For each system branch:
- enumerate changed `src/**`, Android code, schemas and content;
- map files to gameplay/system responsibilities;
- identify current vs historical implementations;
- record tests that verify behavior;
- do not convert code behavior into canon without reconciliation.

### Phase BR-3 — Pixel/UI/asset extraction
For pixel/UI branches:
- inventory catalogs, assets, scene compositions, overlays, rigs, animations and mobile layouts;
- identify base assets vs state overlays;
- map assets to consumers;
- preserve reference provenance;
- classify obsolete/replaced art separately from reusable production assets.

### Phase BR-4 — Test/evidence extraction
- enumerate unit/instrumentation tests;
- preserve baseline/candidate verification logs;
- map Test -> verifies -> Behavior;
- distinguish historical passing evidence from current unverified state.

### Phase BR-5 — Reconciliation
For every extracted source:
- compare against current owner directive and current domain programs;
- record conflicts explicitly;
- adopt compatible material;
- supersede stale pointers;
- retain historical provenance;
- create numbered corpus documents only when unique ownership is justified.

## Immediate next branch-audit priorities

1. `context/shared-game-context` — largest context/world-history source.
2. `docs/master-game-development-program` — broadest later development/program source.
3. `integration/rules-ability-v6-reconcile` + `fix/v6-runtime-boundaries` — system/runtime reconciliation evidence.
4. `integration/android-open-world-v1-reconcile` — Android/open-world migration evidence.
5. `feature/player-avatar-art-pass` + `fix/avatar-overlay-rig-contract` — character visual/overlay authority.
6. Service Tunnel/Quiet Stair/Gate Twelve pixel branches — pilot-region art/runtime lineage.
7. Prototype crystal/combat branches — mechanics source requiring explicit adoption decisions.

## Relationship to the 2,000,000-file program

Branch mining does not mean copying every branch file into the corpus.

Branch files are **source nodes**. The numbered corpus should produce justified authority/specification/evidence/content units derived from reconciled source material.

Target graph examples:

`Branch -> contains -> Source File -> supports -> Decision/Requirement -> owned_by -> DOC_NNNNNNN`

`Test -> verifies -> Historical Behavior -> compared_with -> Current Behavior`

`Prototype Source -> proposes -> Mechanic -> adoption_decision -> Current System Spec`

This preserves history while preventing branch duplication from exploding the corpus with meaningless copies.

## Next action

Begin BR-1 with `context/shared-game-context`: inventory its documentation/context/world-history files, classify unique source families, and map them into current domains before issuing additional numbered corpus IDs.

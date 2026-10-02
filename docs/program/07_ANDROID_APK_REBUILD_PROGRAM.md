# Android / APK Rebuild Program

Status: ACTIVE / PLANNING
Rule: FINAL REBUILD OCCURS AFTER THE RELEVANT DESIGN CONTRACTS ARE STABLE

## Outcome

Evolve the current Android client into the documented final game application without allowing presentation code to become a second gameplay engine.

## Existing architecture boundary

Desired authority path remains:

`GameState -> world/quest/rules systems -> player-safe projection -> Android ViewModel/UI -> visual assets`

## Audit categories

Every current Android component must eventually be classified:
- KEEP
- KEEP + CLEANUP
- EXTEND
- MIGRATE
- REPLACE
- RETIRE
- DELETE AFTER MIGRATION
- UNKNOWN

No component should be deleted merely because a new design looks better; first identify what contract it currently provides.

## Required rebuild areas

- boot/error handling;
- navigation shell;
- story/scene screen;
- character panel;
- stats;
- equipment;
- inventory;
- quests;
- map;
- settings;
- saves;
- developer tools;
- narration/audio;
- accessibility;
- asset catalogs;
- scene composition;
- overlays/FX;
- responsive/mobile behavior;
- persistence/bridge contracts.

## Breaking-change protocol

Before replacing a subsystem:
1. snapshot current files/contracts;
2. list consumers;
3. list player-visible behavior;
4. list data/save/API contracts;
5. design replacement;
6. add migration/adapters if necessary;
7. test old required behavior;
8. test new acceptance behavior;
9. verify on representative Android runtime;
10. only then retire old implementation.

## Final rebuild document

The eventual final APK authority document must state, for every major component:
- old path/component;
- decision;
- new path/component;
- migration;
- test;
- rollback/recovery;
- evidence;
- completion status.

## Required future documents

- ANDROID_CURRENT_ARCHITECTURE_AUDIT
- UI_SURFACE_OWNERSHIP
- PLAYER_SAFE_PROJECTION_V2
- CHARACTER_PANEL_REBUILD
- STORY_SCREEN_REBUILD
- MAP_SCREEN_REBUILD
- NAVIGATION_REBUILD
- SAVE_COMPATIBILITY_PLAN
- ASSET_CATALOG_MIGRATION
- ACCESSIBILITY_PLAN
- PERFORMANCE_BUDGET
- APK_RELEASE_CHECKLIST
- FINAL_APK_REBUILD_MATRIX

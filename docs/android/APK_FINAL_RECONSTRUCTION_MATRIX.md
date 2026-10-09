# THE GAME — Final Android/APK Reconstruction Matrix

Status: **LATE-STAGE AUTHORITY / EXECUTION BLOCKED BY DOMAIN CONTRACTS**  
Parent: `docs/android/APK_REBUILD_AND_EVOLUTION_MASTER_PLAN.md`

## 1. Purpose

The final Android APK is not rebuilt by randomly replacing screens. It is rebuilt from the final documented game architecture.

This matrix records what is likely to be kept, extended, reworked, replaced, or removed. Classifications remain provisional until the existing-state audit and final domain contracts are complete.

## 2. Non-negotiable application boundary

`GameState -> engine/domain systems -> player-safe projection -> Android UI`

KEEP:
- gameplay authority outside Compose;
- hidden-state boundary;
- stable-ID driven actions;
- reproducible build;
- explicit error/startup state;
- save/load authority in engine;
- tests.

## 3. Application-wide classifications

### Boot/runtime bridge
Decision: KEEP + HARDEN.
Need:
- deterministic startup;
- migration error handling;
- content/version checks;
- visible failure state;
- crash diagnostics for developer builds.

### Navigation shell
Decision: REWORK.
Need:
- final screen hierarchy;
- phone ergonomics;
- consistent pixel UI;
- state restoration;
- no excessive permanent chrome over scene art.

### Story
Decision: REWORK substantially.
Target:
- environment art;
- player/room actors;
- optional focused actor portrait panel;
- narrative;
- choices;
- resource/status strip;
- location state;
- controlled animation/FX.

### Map
Decision: REWORK / partial REPLACE presentation.
KEEP:
- authoritative nodes/routes/discovery/reachability.
REPLACE/REWORK:
- geometric/technical visual presentation where weaker than authored map art.
Target:
- layered pixel map;
- selection;
- player marker;
- location detail/arrival preview;
- world->region->district transitions.

### Character
Decision: REWORK visually.
KEEP:
- equipment state;
- paper-doll contract.
Target:
- Jack canonical sprite;
- equipment;
- status overlays;
- portrait;
- concise player summary.

### Stats
Decision: EXTEND/REWORK after progression master.
No hardcoded final stat taxonomy before that contract.

### Skills
Decision: EXTEND/REWORK after class/rank master.

### Equipment
Decision: KEEP mechanics / REWORK visuals and item detail.

### Inventory/Bag
Decision: KEEP authoritative inventory / REWORK presentation.

### Quests
Decision: EXTEND.
Need:
- main/side/optional/lore/faction/dynamic distinctions when authored;
- location/actor links;
- objectives/history;
- no hidden future objective exposure.

### Saves
Decision: KEEP/high risk.
REWORK UX only when migration compatibility is proven.

### Settings
Decision: EXTEND.
Include:
- audio;
- narration;
- text reveal;
- controls;
- accessibility;
- display;
- data/save;
- developer entry separated from normal play.

### Developer tools
Decision: KEEP SEPARATE + EXTEND.
Must never become normal gameplay authority.

## 4. Pixel-art integration

Final APK must consume the production stack:
- map/environment base;
- props/modules;
- room actors;
- player/equipment;
- state overlays;
- FX;
- portrait/focus panels;
- UI text/actions.

Requirements:
- nearest-neighbor;
- source-native scale;
- consistent anchor/pivot;
- no smooth-image shortcuts;
- no hidden-state asset selection;
- asset provenance;
- phone screenshot QA.

## 5. Character panels

When a focused named actor is present:
- engine exposes actor safely;
- room actor appears in scene;
- panel may open or surface contextually;
- portrait matches actor;
- dialogue/actions are authored;
- relationship/status shown only if intentionally player-visible.

If no actor is projected:
- no panel is invented from hidden flags.

## 6. World navigation

Final app should support hierarchical travel:
- world;
- macroregion;
- region;
- settlement;
- district;
- site/interior.

The UI may collapse levels for usability, but authoritative place IDs and route legality remain in the engine/world layer.

## 7. Tactical combat surface

The authoritative tactical engine is now **partially implemented through D-071**, but the APK tactical consumer is not. D-072 still owns durable aftermath, D-073 the bounded Gate Twelve content/Python bridge, and D-074 the typed Kotlin/ViewModel/Compose surface.

The final APK tactical surface should provide:
- a separate tactical surface or context mode;
- the same persistent character/state after validated aftermath publication;
- original UI;
- player-safe turn/action state;
- cover/LOS/targeting;
- ability/item actions;
- a redacted player-safe combat log/projection rather than raw private tactical state;
- post-combat consequences after authoritative Python commit.

Do not bolt combat logic directly into ordinary Story Compose callbacks, and do not treat the existence of the headless D-069–D-071 runtime as Android tactical completion.

## 8. Dynamic adversary surface

If the persistent adversary system is implemented:
- player-facing intel uses only known information;
- no omniscient enemy hierarchy;
- encounter history;
- known traits;
- reputation/rival relationship;
- faction/world consequences.

Use original terminology and visual presentation.

## 9. Candidate removals

Do not remove yet.

Potential removal candidates after replacement:
- obsolete geometric placeholder renderers;
- duplicate asset paths;
- temporary generic player visuals;
- stale UI components superseded by final screens;
- abandoned prototype-only debug presentation;
- duplicated hardcoded visual state.

Each removal requires consumer audit and replacement evidence.

## 10. Candidate preservation

Likely preserve:
- repository-owned Android build;
- Chaquopy/Python integration if it remains suitable;
- player-safe bridge;
- existing save/load foundation;
- Compose test infrastructure;
- screenshot evidence pipeline;
- runtime asset fallback strategy;
- stable content IDs;
- exact current verified engine behavior unless migrated.

## 11. Final rebuild sequence

1. freeze approved domain documentation version;
2. exact repository audit;
3. save/content migration plan;
4. player-safe projection expansion;
5. visual asset freeze for first final region;
6. navigation shell;
7. Story;
8. Character/Stats/Skills;
9. Equipment/Bag;
10. Quests;
11. Map;
12. settings/accessibility/narration;
13. tactical combat surface;
14. adversary/world surfaces;
15. developer tools;
16. remove deprecated components;
17. performance pass;
18. full regression;
19. physical device;
20. release artifact/provenance.

## 12. Final APK “10,000” documentation target

The owner requested a final “10,000” APK/development documentation scope.

Until the unit is confirmed, track:
- decisions;
- migration records;
- screen contracts;
- component records;
- test cases;
- QA evidence;
- words/docs.

Do not claim completion by assuming the unit.

## 13. Destructive rebuild authorization

Broad authorization exists to break and rebuild application presentation when necessary.

Before destructive change:
- document old behavior;
- classify old component;
- identify consumers;
- create replacement contract;
- implement on working branch;
- verify;
- migrate;
- then remove.

Persistent state and stable IDs require stronger migration gates than UI components.

## 14. Final acceptance

A final APK is not “done” because it builds.

Required:
- exact source provenance;
- automated green tests;
- correct assets;
- no hidden-state leaks;
- save/load/migration;
- phone-width visual QA;
- performance;
- accessibility checks;
- install/start on physical Galaxy A03 separately;
- known limitations;
- final documentation handoff.


## 2026-10-02 final reconstruction integration update

Before the final rebuild begins, create an **APK teardown manifest**. Every candidate component/file must record:
- current path/component;
- current callers/consumers;
- projected fields/actions consumed;
- asset dependencies;
- save/state dependency;
- test coverage;
- target replacement;
- migration order;
- rollback path;
- zero-consumer proof before removal.

Deletion states:
- **PRESERVE DURING MIGRATION**;
- **REPLACEMENT READY**;
- **CONSUMERS MIGRATED**;
- **ZERO-CONSUMER VERIFIED**;
- **REMOVE/ARCHIVE ALLOWED**.

The app must never be “cleaned up” by deleting old paths first and hoping the replacement later covers them. The final APK is reconstructed from verified domain contracts and consumer evidence.

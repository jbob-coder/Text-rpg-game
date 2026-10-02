# THE GAME — Android Consumer & Player-Safe Projection Map

Status: **ACTIVE / FIRST-PASS SOURCE-GROUNDED CONSUMER CONTRACT**  
Repository: `jbob-coder/Text-rpg-game`  
Program branch: `docs/master-game-development-program`  
Parents:
- `docs/android/APPLICATION_UX_MASTER_PLAN.md`
- `docs/android/APK_REBUILD_AND_EVOLUTION_MASTER_PLAN.md`
- `docs/android/APK_FINAL_RECONSTRUCTION_MATRIX.md`

## 1. Purpose

Map Android presentation consumers to the player-safe data/actions they are allowed to consume.

This is the bridge between:
- Python/domain state;
- Android bridge projection;
- Compose screens;
- pixel assets;
- tests.

It prevents the final APK rebuild from moving gameplay authority into UI code.

## 2. Current Android projection contract

Current Kotlin `GameSnapshot` exposes:

- `sceneId`;
- `title`;
- `body`;
- `choices`;
- `resources`;
- `attributes`;
- `derived`;
- `skills`;
- `conditions`;
- `identity`;
- `inventory`;
- `quests`;
- `worldMap`;
- `visuals`;
- `turn`;
- `timeMinutes`;
- `location`;
- `contentId`;
- `canonStatus`.

Current public `GameEngine` actions expose:
- start;
- choose;
- save;
- load;
- applyCheat;
- equip;
- unequip;
- travel;
- inspectStatus.

These are current implementation facts at the audited program branch.

## 3. Core boundary

Target remains:

`GameState -> domain/rules/world -> player-safe projection -> Android bridge -> Compose UI`

Compose may:
- select;
- request;
- render;
- animate;
- filter already-safe presentation fields;
- manage ephemeral UI state.

Compose may not:
- decide quest truth;
- calculate authoritative stats/damage;
- decide route legality;
- read hidden NPC goals;
- infer actor presence from private flags;
- mutate inventory directly;
- create undiscovered map nodes;
- grant skills/abilities/items.

## 4. Story/current-location consumer

Current/target inputs:
- scene ID;
- title/body;
- choices;
- resources;
- location;
- safe visual state;
- current actor presence when added;
- current room/state overlays.

Current actions:
- choose.

Target asset packet:
- environment base;
- props/modules;
- room actors;
- equipment/held-object layers;
- state overlays;
- FX;
- optional portrait/focus panel.

Decision:
- **REWORK presentation / KEEP authority boundary**.

## 5. Choice cards

Consume:
- choice ID;
- player-visible text;
- enabled;
- disabled reason.

Must not receive:
- raw requirements;
- hidden checks;
- future outcomes;
- secret next-scene IDs unless intentionally player-facing.

Action:
- `choose(choiceId)`.

Decision:
- **KEEP safe semantics / REWORK visual treatment as needed**.

## 6. Story resource HUD

Consume:
- `resources[].id/current/max`.

May calculate only visual ratios from already-projected current/max.

Must not calculate authoritative maximum values.

Decision:
- **KEEP projection / REWORK styling/layout as needed**.

## 7. Map consumer

Current `GameWorldMap` exposes:
- title;
- currentLocation;
- nodes;
- edges.

Each node exposes:
- ID;
- title;
- description;
- X/Y;
- current;
- reachable.

Map may:
- render nodes/edges;
- render current/reachable state;
- select a safe node;
- show player-safe description;
- request travel.

Map may not:
- invent edges;
- mark a node reachable itself;
- reveal hidden nodes not projected;
- alter travel time/risk.

Action:
- `travel(locationId)`.

Decision:
- **KEEP semantic projection / REWORK or partially replace visual presentation**.

## 8. Future hierarchical map requirement

Current `GameWorldMap` is district-scale.

Final world navigation needs a future projection capable of:
- world;
- macroregion;
- region;
- settlement;
- district;
- site/interior.

Do not overload current node X/Y to silently become universal world coordinates.

Required migration:
- new hierarchical place/map projection;
- backward-compatible Gate Twelve adapter or explicit migration.

## 9. Character consumer

Current inputs:
- identity;
- equipment slots;
- conditions;
- attributes;
- skills;
- resources;
- inventory candidates.

Current actions:
- equip;
- unequip.

Visual contract:
- 32x48 paper-doll;
- equipment layers;
- canonical Jack identity;
- status overlays;
- future portrait.

Decision:
- **KEEP state contract / REWORK visual identity**.

## 10. Stats consumer

Current inputs:
- resources;
- attributes;
- derived;
- skills;
- conditions;
- projected contribution summaries.

Current action:
- `inspectStatus(path)`.

Inspection returns:
- path;
- kind;
- total;
- player-safe contribution sources/values.

UI may label safe contribution sources.

It must not reconstruct hidden modifier provenance.

Decision:
- **KEEP safe inspection / EXTEND after progression migration**.

## 11. Skills consumer

Current skills are exposed in `GameSnapshot.skills`.

Final UI must later incorporate:
- skill families;
- class/profession links;
- ranks/mastery;
- prerequisites;
- training opportunities.

These fields do not yet all exist in current projection.

Decision:
- **EXTEND projection after progression contract**.

## 12. Inventory/Bag consumer

Current inputs:
- inventory items;
- item ID/name/quantity;
- equippable;
- slot;
- quality;
- equipment state.

Current actions may include equip/unequip through engine.

Future additions may require:
- item detail;
- provenance-known effects;
- categories;
- weight/encumbrance only if implemented;
- ownership/legal status only if implemented.

Decision:
- **KEEP inventory authority / REWORK presentation / EXTEND schema carefully**.

## 13. Equipment consumer

Current inputs:
- equipment slots;
- item identity;
- quality;
- contribution summaries.

Must preserve slot semantics.

Paper-doll visual layers consume item IDs through the asset system.

Decision:
- **KEEP mechanics / REWORK art/alignment**.

## 14. Quests consumer

Current `GameQuest` exposes:
- ID;
- title;
- description;
- category;
- status;
- stage;
- objectives.

Objectives expose:
- ID;
- title;
- required;
- status.

Must not expose hidden future objectives/stages unless projected.

Decision:
- **KEEP/EXTEND**.

## 15. Save/load consumer

Actions:
- save;
- load.

UI owns:
- buttons;
- confirmation;
- error display;
- slot presentation if slots later exist.

Engine/persistence owns:
- serialization;
- schema;
- migration;
- correctness.

Decision:
- **KEEP authority / REWORK UX if needed**.

## 16. Settings

Settings may own application-only preferences:
- audio;
- narration;
- text reveal;
- accessibility;
- display;
- input behavior.

Gameplay settings that affect rules must route through domain authority.

Decision:
- **EXTEND**.

## 17. Developer/cheat consumer

Current engine exposes `applyCheat`.

Developer tools must remain:
- visually separated;
- unavailable from normal player flow unless explicitly enabled;
- non-canonical for ordinary play evidence.

Decision:
- **KEEP separate / EXTEND developer tooling**.

## 18. Missing actor-presence projection

Current `GameSnapshot` does not provide a formal room-actor list.

Target new safe record should eventually expose only player-known/currently visible actors, for example:

- actor ID;
- display name;
- portrait/visual identity key;
- room anchor/pose key;
- visible condition;
- known role/faction;
- available safe interactions.

It must not expose:
- private goals;
- secret knowledge;
- hidden disposition;
- off-screen position if not known;
- future story state.

This is a required dependency for dynamic room actors and character panels.

## 19. Missing world-state notification projection

Future app may need safe notifications such as:
- location changed;
- new route discovered;
- activity complete;
- quest updated;
- relationship visibly changed;
- item obtained;
- condition changed.

Do not infer notifications by diffing raw hidden state in Compose.

## 20. Missing activity projection

Future activity system should expose:
- activity ID/name;
- safe requirements;
- duration;
- known costs;
- availability;
- current progress;
- interruption/cancel status.

Implementation waits on activity master/schema.

## 21. Missing tactical combat projection

Future combat needs a separate player-safe model for:
- visible units;
- positions;
- legal actions;
- known cover/LOS;
- resources;
- objectives;
- visible status;
- combat log.

Do not overload ordinary `GameSnapshot` until a combat projection contract is selected.

## 22. Missing persistent-adversary intel projection

Future rival/adversary UI may show only:
- known identity;
- known faction/status;
- remembered encounter history;
- known traits;
- known injuries/status;
- player relationship/rivalry information that is intentionally visible.

No omniscient hierarchy.

## 23. Pixel asset ownership

Android screen code requests assets by stable visual ID/state.

Asset catalogs/manifests own:
- raster/fallback mapping;
- compatibility;
- state variants.

Engine owns:
- which semantic state is true.

UI owns:
- how the selected safe asset is displayed.

## 24. Current source consumers to keep under audit

Known major presentation/runtime files include:
- `GameViewModel.kt`;
- `GameEngine.kt`;
- `PythonGameEngine.kt`;
- `GameScreen.kt`;
- `CharacterSection.kt`;
- `StatsSection.kt`;
- `StatusComponents.kt`;
- `SceneIllustration.kt`;
- pixel catalogs;
- save repository;
- boot state;
- narration controller.

Each must receive a final KEEP/EXTEND/REWORK/REPLACE/REMOVE classification before the final APK rebuild.

## 25. Consumer test requirements

For every new projection field/action:
- bridge mapper unit test;
- engine contract test;
- Compose consumer test where visible;
- privacy/hidden-state regression;
- save/load test if persistent;
- emulator screenshot if visual;
- physical handset QA when required for final acceptance.

## 26. Final rebuild rule

The final APK is rebuilt from this mapping plus domain contracts.

A screen is not rewritten simply because it looks old.

A screen is rewritten when:
- required domain information cannot be represented cleanly;
- presentation architecture blocks final UX;
- current asset pipeline cannot scale;
- accessibility/performance requires change;
- duplicate/hardcoded state would cause divergence.

## 27. Open audit work

Still required:
- exact field consumer map for every composable;
- exact ViewModel flow/action mapping;
- exact bridge payload keys from Python;
- all test coverage by field/action;
- all asset catalog consumers;
- all temporary/hardcoded visual state;
- final navigation graph.

This document is the first-pass contract, not a completed line-by-line Android audit.

# THE GAME — Android Application UX Master Plan

Status: **FOUNDATIONAL / FINAL SCREEN HIERARCHY NOT YET LOCKED**
Parents:
- `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`
- `docs/android/APK_REBUILD_AND_EVOLUTION_MASTER_PLAN.md`
- `docs/assets/PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md`

## 1. Product goal

The Android client should make the world/story space the primary experience.

Management screens exist to support play, not replace the world with menus.

## 2. Core experience loop

Target:
`see current place -> understand present people/state -> read/listen -> choose/act -> observe consequence -> navigate/travel/manage when needed`

## 3. Candidate surface hierarchy

Primary:
- Story / Current Location;
- Map / World.

Character management:
- Character;
- Stats;
- Skills/Abilities/Class;
- Equipment;
- Inventory/Bag.

World management:
- Quests;
- People/Relationships if justified;
- Knowledge/Logs if justified;
- Activities if justified.

System:
- Saves;
- Settings;
- Accessibility;
- Developer tools separated.

Tactical Combat appears contextually when engaged.

Final navigation count remains undecided.

## 4. Story/current-location surface

Should support:
- environment/room art;
- player sprite when composition needs it;
- present NPC sprites;
- focused character portrait panel;
- location title/context;
- narrative text;
- choices/actions;
- resource/status strip;
- temporary overlays/FX.

Avoid permanent UI chrome that covers most art.

## 5. Character panels

Driven by projected room occupants.

Focus order:
1. selected;
2. speaker;
3. interaction target;
4. party-relevant;
5. present actor list.

Panel content only uses player-safe information.

## 6. Map

Future hierarchy:
- world;
- macroregion;
- region;
- settlement;
- district;
- site/interior.

The UI can collapse levels for usability.

Need:
- pan/zoom decisions;
- LOD;
- current position;
- discovered/reachable;
- selected destination;
- travel preview;
- world/district switch;
- phone touch targets.

## 7. Character

Target:
- Jack approved identity;
- 32x48 rig or higher-level portrait where appropriate;
- paper-doll equipment;
- visible conditions;
- concise resources/summary;
- equipment detail.

No generic box mannequin as final art.

## 8. Stats

Target:
- canonical attributes;
- derived values;
- skills;
- conditions;
- contribution explanations;
- progression context.

Rules remain engine-owned.

## 9. Skills / abilities / classes

Wait for progression master.

Need:
- hierarchy;
- prerequisites;
- mastery;
- passives;
- techniques;
- class/rank if adopted;
- training location/action.

## 10. Equipment and Inventory

Need:
- pixel icons;
- item detail;
- equip legality;
- compare;
- paper-doll result;
- inventory categories;
- player-safe action reasons.

## 11. Quests

Need:
- categories;
- current objectives;
- history;
- location/actor links;
- no hidden future objectives.

## 12. Tactical combat

Contextual full mode:
- map;
- units;
- action selection;
- objective;
- selected unit;
- enemy intel if known;
- combat log.

## 13. Narration/audio

Preserve:
- tap/replay;
- stop;
- auto-read;
- speech rate;
- text reveal.

Future:
- voice choice if supported;
- pause semantics;
- accessibility synchronization.

## 14. Accessibility

Need:
- scalable text;
- contrast;
- reduced motion;
- touch sizes;
- non-color-only states;
- narration;
- haptic/sound alternatives if used.

## 15. Responsive layout

Primary targets:
- phone portrait/landscape only if product supports;
- Galaxy A03-class low-end device;
- emulator sizes used in CI.

No desktop-first layouts forced onto phone.

## 16. Loading/error states

Every major surface needs:
- loading;
- engine error;
- missing asset fallback;
- save error;
- unsupported schema;
- safe recovery.

## 17. Pixel-art runtime

UI must:
- use nearest-neighbor;
- preserve source aspect;
- avoid smoothing;
- use correct z-order;
- select assets from safe visual state;
- support overlays;
- avoid shipping reference boards.

## 18. Final decisions still needed

- final bottom/top navigation;
- Story/Map integration level;
- character panel placement;
- map zoom model;
- world hierarchy navigation;
- tactical combat navigation;
- relationships/knowledge screens;
- portrait sizes;
- transition animations;
- orientation support;
- low-memory asset caching.

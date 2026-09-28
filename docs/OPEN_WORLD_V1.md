# Open World V1 — Candidate Design and Handoff

Updated: 2026-09-27 AST  
Branch: `feature/android-open-world-v1`

## Status

This branch is an **integration candidate**, not a release claim. It was created from the Android pixel client while the base client was still undergoing representative-emulator smoke validation. Do not mark these additions DONE until the branch is promoted to the Android client and the relevant Python/Android gates pass.

Repository source and fresh execution evidence outrank this document.

## Product intent

The text RPG must not collapse into a single repeating narrative-choice loop. The Android client should support a persistent character moving through a readable pixel world where:

- main progression can be postponed without being lost;
- optional exploration changes what information becomes available;
- some choices affect narrative/world state without granting stats;
- location travel consumes time and can open a different authored scene;
- quest categories include main, side, optional, and lore content;
- equipment remains authoritative in Python but visibly changes the pixel avatar.

The authoritative flow remains:

`GameState -> World/Quest/Narrative -> Rules/Stats/Abilities/Equipment -> player-safe projection -> Android UI`

## Candidate district continuation

The former Directional Trace prototype ending now continues into `DISTRICT_HUB` instead of terminating the playable flow.

New authored locations:

- `DISTRICT_PLAZA` -> `DISTRICT_HUB`
- `DISTRICT_ARCHIVE` -> `DISTRICT_ARCHIVE`
- `WORKSHOP_ROW` -> `DISTRICT_WORKSHOP`

These locations are revealed by the durable flag `world.free_roam_unlocked`.

The district contains a lore quest:

- `QUEST_PLATFORM_NINE_RECORDS`
- category: `lore`
- knowledge reward: `KNOW_PLATFORM_NINE_EVAC_PROTOCOL`

Reading the records changes knowledge/quest state but deliberately does not grant an attribute/stat reward.

## Early branch instead of mandatory linear continuation

At `OPENING_END`, the player can now either:

1. continue below Gate Twelve immediately; or
2. return to the district before starting the Trace Echo investigation.

The district route preserves the unfinished investigation. `RESUME_GATE_TWELVE_INVESTIGATION` starts `QUEST_GATE_TWELVE_ECHO` and returns to `POWER_GATE_TWELVE_SIGNAL`.

Durable coordination flag:

- `world.trace_echo_quest_started`

This prevents the district detour from silently losing or duplicating the quest start.

## Delayed cross-location narrative consequence

Workshop choice:

- `ASK_WORKERS_ABOUT_GATE_TWELVE`
- sets `world.workshop_rumor_heard`

That flag later reveals an additional Archive choice:

- `CROSSCHECK_GATE_TWELVE_WORKSHOP_RUMOR`

The cross-check records:

- `KNOW_GATE_TWELVE_CREW_WITHDRAWAL`

This is an intentional example of a delayed consequence which changes available narrative information rather than directly modifying player stats.

## Map runtime contract

`textrpg.android_bridge` now:

- discovers authored nodes through scene history and optional `discover_flag`;
- exposes only player-safe map data;
- marks each node `reachable` when it is the current node or directly connected by a discovered edge;
- validates travel against discovered adjacency;
- advances authoritative game time;
- when an authored map node contains `scene_id`, changes authoritative `GameState.scene_id` to that destination scene;
- otherwise preserves the older map-only location override behavior;
- rolls state back if travel fails.

Android:

- renders routes and nodes in the pixel map;
- allows selecting map nodes by tapping the pixel map itself;
- only offers TRAVEL HERE for reachable destinations;
- does not own world position or travel rules.

## Avatar equipment visual contract

The Android pixel avatar is a presentation-only paper-doll renderer over player-safe equipped slots.

Supported visible layers currently include:

- head
- body/chest
- hands
- legs
- feet
- main hand
- off hand
- ring 1
- ring 2
- neck
- accessory 1
- accessory 2

Equipping/unequipping remains authoritative Python state. Kotlin only renders the resulting equipped-slot projection.

## Stats presentation

The dedicated Stats screen now separates:

- current resources;
- core attributes with base/effective/modifier values and authored role text;
- derived values with role text;
- grouped skills with base/effective modifier information;
- visible conditions.

Android does not recalculate authoritative stat totals.

## Content validation hardening

Candidate validation now checks authored `world_map` data when present:

- map is optional;
- node IDs and node object shape;
- x/y finite 0..100 coordinates;
- optional `scene_id` points to a known scene;
- optional `discover_flag` is non-empty text;
- edges reference known nodes;
- travel time is a non-negative integer when provided;
- scene `location_id` references a known map node when a map is declared.

## Candidate regression tests added

Python tests cover:

- district nodes unlocking from `world.free_roam_unlocked`;
- map travel changing authoritative narrative scene;
- lore records changing knowledge/quest state without changing attributes;
- Directional Trace ending continuing into district free roam;
- early district detour and later Trace quest resume;
- workshop rumor unlocking delayed Archive investigation;
- invalid map scene destinations;
- invalid map edges;
- invalid travel times;
- optional absence of `world_map`.

Android Compose candidate coverage includes visible avatar gear semantics for equipped body/ring layers.

## Verification gate before promotion

Before this candidate becomes the Android client baseline:

1. base Android client representative-emulator startup/choice/save/load smoke must pass;
2. promote these changes without discarding later base-client fixes;
3. run the full Python suite;
4. compile Android unit and instrumentation tests;
5. assemble and inspect the APK;
6. run a representative-emulator smoke for at least boot, one story choice, Save/Continue, and one free-roam/map transition;
7. update `docs/ANDROID_PIXEL_CLIENT_VALIDATION.md` and `docs/THE_GAME_MASTER_TASK_REGISTER.md` with exact SHA/run/hash/timestamps.

Physical handset validation remains a separate release gate.

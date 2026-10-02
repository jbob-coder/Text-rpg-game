# THE GAME — Android APK Rebuild & Evolution Master Plan

Status: **LATE-STAGE MASTER PLAN / DO NOT EXECUTE AS A BLIND REWRITE YET**  
Parent: `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`

---

# 1. Purpose

The owner has authorized the Android application to be changed aggressively when necessary to make the game better.

The final Android/APK phase is not “keep patching the current screen.”

It is:

1. understand the final documented game;
2. audit the existing client;
3. classify every major client subsystem;
4. preserve what is correct;
5. remove what is obsolete;
6. rebuild what cannot support the final design;
7. migrate authoritative interfaces safely;
8. verify exact-head behavior;
9. produce a traceable APK.

This is intentionally the **final major development/documentation phase**, not the first.

---

# 2. Existing client value

The current Android client already proves important architecture:

- repository-owned Kotlin/Compose app;
- Chaquopy bridge to Python engine;
- visible Story presentation;
- navigation;
- save/load;
- player-safe projections;
- pixel scene rendering;
- map rendering;
- paper-doll character;
- equipment interaction;
- inventory;
- Stats/Skills development lines;
- resource HUD;
- tests;
- emulator QA screenshots;
- build artifact generation.

Do not throw away working architecture merely because visual quality is not final.

---

# 3. Why a later rebuild may still be necessary

Current work grew incrementally.

The final documented game may require:
- dynamic actor panels;
- richer map hierarchy;
- city/world navigation;
- tactical combat screen;
- class/skill trees;
- NPC/social surfaces;
- world activities;
- beast/loot systems;
- broader inventory/equipment;
- world-state notifications;
- multi-region loading;
- more robust save migration;
- new developer QA tools.

A later rebuild should remove accidental constraints from the prototype.

---

# 4. Final audit classification

Every major file/screen/module receives:

- **KEEP** — already matches final contract;
- **EXTEND** — correct architecture, more capability needed;
- **REWORK** — useful concept, structure insufficient;
- **REPLACE** — obsolete implementation after migration;
- **REMOVE** — no longer needed;
- **ARCHIVE** — historical evidence/reference only.

No deletion occurs from aesthetic preference alone.

---

# 5. Expected KEEP candidates

Unless later evidence contradicts:

- authoritative Python engine separation;
- player-safe projection principle;
- stable IDs;
- versioned saves;
- repository-owned Android project;
- Compose testing infrastructure;
- exact-head CI;
- source-native pixel rendering;
- nearest-neighbor behavior;
- paper-doll anchor principle;
- location/scene state projection.

---

# 6. Expected EXTEND candidates

- GameSnapshot projection;
- actor presence;
- map hierarchy;
- equipment visuals;
- item data;
- quest presentation;
- relationship/social projection;
- world-state projection;
- audio/narration;
- accessibility;
- developer tools.

---

# 7. Expected REWORK candidates

- Story screen layout once dynamic room actors/panels are formal;
- Map screen once world/city/district hierarchy exists;
- navigation if screen count expands;
- current scene header if it cannot scale to richer actor/context presentation;
- developer panel organization;
- save/load UX;
- asset catalogs if world-scale content exceeds hard-coded patterns.

---

# 8. Expected REPLACE candidates

Potential, not automatic:
- procedural geometric scene fallbacks where real art exists;
- provisional player silhouette after approved source art is integrated;
- location-specific hard-coded actor placement after projected actor system exists;
- hard-coded catalogs that become unmaintainable after data-driven asset manifests prove ready.

---

# 9. Expected REMOVE candidates

Only after replacement is verified:
- dead placeholder assets;
- duplicate art IDs;
- unused fallback code;
- superseded UI components;
- obsolete test fixtures that test behavior intentionally removed.

Historical evidence stays in Git history/documentation.

---

# 10. Target app information architecture

Possible final major surfaces:

- Story / Current Location;
- Map / World;
- Character;
- Stats;
- Skills / Abilities / Classes;
- Equipment;
- Inventory / Bag;
- Quests;
- Relationships / People;
- Activities;
- Tactical Combat when engaged;
- Logs / Knowledge;
- Settings;
- Save/Load;
- Developer tools.

This is not yet a locked navigation count.

The final UX document must determine which surfaces are primary, nested or contextual.

---

# 11. Story / room target

The Story surface should eventually support:

- environment art;
- player sprite when appropriate;
- present NPC sprites;
- actor focus;
- dialogue/narrative;
- choices;
- resource status;
- location context;
- temporary FX;
- item/prop context.

The room should feel like a place, not a static text box.

---

# 12. Map target

The map system should eventually support layers:

1. world;
2. region;
3. city/settlement;
4. district;
5. local node/route.

Not every layer must be shown simultaneously.

The player should navigate hierarchy without confusing logical coordinates and visual map pixels.

---

# 13. Tactical combat target

Combat should open a purpose-built tactical surface rather than squeezing combat into ordinary narrative cards.

The tactical screen will require:
- tactical map;
- units;
- turn state;
- movement;
- action selection;
- cover/LOS;
- status;
- objectives;
- combat log;
- contextual details.

Exact UI waits for combat rules.

---

# 14. Dynamic NPC/social target

The client may need:
- present-character panel;
- relationship detail;
- known information;
- memory/history summary;
- faction/status;
- goals only when player-visible;
- rival history.

Hidden NPC internals remain engine-side.

---

# 15. Pixel-art integration target

Final client should consume:
- source-native scene masters;
- modular environment overlays;
- actor sprites;
- paper-doll character/equipment;
- FX;
- map tiles/modules;
- UI pixel elements.

It should not redraw the world from generic Compose rectangles when approved art exists.

---

# 16. Data-driven asset direction

Hard-coded Kotlin catalogs are acceptable for bounded prototypes.

World-scale target should evaluate:
- generated manifest/index files;
- stable asset keys;
- resource lookup;
- state bindings;
- fallback policy;
- QA metadata.

Do not migrate to a data-driven loader before its schema and performance are tested.

---

# 17. Breaking-change workflow

For every intentional Android break:

1. document old behavior;
2. identify final contract;
3. add/adjust engine projection if needed;
4. create new UI in parallel when practical;
5. migrate tests;
6. capture screenshots;
7. remove old path only after verification;
8. record exact head and artifact.

---

# 18. Save compatibility

The APK rebuild cannot casually invalidate saves.

Before schema change:
- define old schema;
- define new schema;
- define migration;
- test migration;
- test rejected unsupported schema;
- keep backup/export path if appropriate.

If no migration is possible, the owner must see that consequence before release.

---

# 19. Performance requirements

Target device evidence includes a Galaxy A03 context.

Therefore:
- avoid wasteful continuous recomposition;
- keep pixel assets compact;
- bound animation rates;
- avoid loading entire world art at once;
- use section/region loading as needed;
- profile before introducing complex real-time effects.

Emulator success does not equal Galaxy A03 success.

---

# 20. Accessibility

Final app should account for:
- text scale;
- contrast;
- reduced motion;
- narration/audio settings;
- touch target size;
- non-color-only state communication.

Pixel art must remain readable under these constraints.

---

# 21. Final rebuild phases

## Phase A — final contract freeze
Required:
- world hierarchy;
- progression;
- combat;
- social/NPC;
- item/economy;
- visual;
- UX.

## Phase B — current-client audit
Generate file/module matrix:
- keep;
- extend;
- rework;
- replace;
- remove.

## Phase C — engine projection expansion
Add only player-safe data needed by final UI.

## Phase D — visual runtime rebuild
Map/scene/actor/equipment/FX pipelines.

## Phase E — screen rebuild
Implement final information architecture.

## Phase F — tactical/social/world systems
Integrate new major gameplay surfaces.

## Phase G — migration
Save/content/assets.

## Phase H — cleanup
Remove obsolete code/assets only after evidence.

## Phase I — verification
- Python;
- Android unit;
- instrumentation;
- emulator;
- screenshot QA;
- physical handset;
- performance;
- accessibility.

## Phase J — APK release candidate
Record:
- source HEAD;
- workflow run;
- artifact ID;
- SHA-256;
- signing/build mode;
- supported ABIs;
- test matrix;
- known limitations.

---

# 22. Final APK documentation deliverable

The late-stage APK document set should include:

- final screen map;
- final navigation map;
- engine/UI API contract;
- asset-runtime contract;
- save migration plan;
- performance budget;
- accessibility checklist;
- module keep/remove matrix;
- replacement order;
- test plan;
- release checklist;
- evidence manifest;
- known issues;
- rollback plan.

The owner's requested final large documentation block belongs here.

---

# 23. What should happen now

Do **not** start the final rewrite yet.

Immediate prerequisites:
- finish Gate Twelve region documentation;
- build world master child standards;
- build progression master;
- build social/rival master;
- build combat master;
- reconcile character visual authority;
- build application UX master.

Then this plan becomes executable rather than speculative.

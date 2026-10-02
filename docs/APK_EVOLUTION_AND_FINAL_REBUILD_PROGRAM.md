# THE GAME — APK Evolution & Final Rebuild Program

Status: **FINAL-PHASE PLANNING / DO NOT EXECUTE WHOLE REBUILD YET**
Target: at least 10,000 words/units of final APK reconstruction documentation before the final destructive rebuild.

## 1. Purpose

The final APK should be rebuilt from the final documented game architecture rather than continuously layering patches over prototype presentation.

This does not mean deleting working code now.

The process is:
`document -> classify -> design replacement -> migrate -> verify -> retire obsolete code`

## 2. Rebuild gate

The final reconstruction begins only after:
- world/map contracts are mature;
- core mechanics are documented;
- pixel-art runtime pipeline is locked;
- major UI surfaces have state contracts;
- save migration is designed;
- asset status/provenance is known;
- combat/rival systems have contracts if in release scope;
- performance budget is known.

## 3. Application surfaces to document

Final APK needs explicit contracts for:
- startup/loading;
- new game/continue;
- Story/world scene;
- Map;
- Character;
- room character panels;
- Stats;
- Equipment;
- Inventory;
- Skills/Abilities;
- Quests;
- relationships/social if included;
- tactical combat;
- notifications/events;
- Settings;
- Saves;
- accessibility;
- narration/audio;
- developer tools.

## 4. Candidate presentation to remove/replace

Subject to exact live audit:
- placeholder boxes/geometry;
- obsolete procedural scene art;
- old map line-only visualization;
- redundant panels;
- stale navigation;
- duplicate stat calculations;
- hardcoded content labels;
- old asset adapters superseded by manifests;
- dead prototype code;
- one-off visual state logic that belongs in engine projection.

Nothing is deleted until:
- replacement exists;
- migration is tested;
- old behavior is covered or deliberately removed;
- save/state implications are understood.

## 5. Architecture target

### Engine
Owns:
- game rules;
- world;
- NPCs;
- quests;
- stats;
- abilities;
- combat;
- travel;
- time;
- inventory/equipment;
- save state.

### Projection
Owns:
- player-safe state;
- UI explanations;
- scene occupants;
- visual states;
- available actions;
- map discovery/reachability;
- visible relationship/state summaries.

### Android UI
Owns:
- layout;
- input;
- navigation;
- rendering;
- animation;
- accessibility;
- audio controls;
- presentation.

### Asset layer
Owns:
- pixel masters;
- atlases;
- manifests;
- overlays;
- portraits;
- equipment layers;
- maps;
- FX;
- fonts only through approved app packaging.

## 6. Final world-centric UX direction

The player spends most time in the world/story area.

Therefore the final APK should prioritize:
- large location art/map context;
- current location/room;
- player character;
- present-character panels;
- current narrative/actions;
- resources/status;
- quick access to deeper management screens.

Avoid making the primary experience a grid of administrative menus.

## 7. Character panel integration

Room/scene occupant projection drives:
- portrait;
- name;
- speaker state;
- interaction action;
- party/presence;
- visible status.

Multiple NPCs require selection or speaker focus.

Panels must not leak hidden AI/NPC state.

## 8. Map integration

Map should evolve from geometry to pixel-art world presentation while preserving:
- stable node IDs;
- authoritative routes;
- discovery;
- reachability;
- travel legality;
- time cost.

Future world scale may require:
- pan;
- zoom;
- regional/world hierarchy;
- LOD;
- streaming;
- map layers.

## 9. Pixel-art asset loading

Final application should:
- use production PNG/atlas/source-native pixel data;
- keep nearest-neighbor scaling;
- avoid shipping huge concept boards;
- reuse modules;
- load state overlays separately;
- avoid duplicate copies;
- support low-memory devices.

## 10. Performance program

Document budgets for:
- APK size;
- memory;
- startup time;
- map rendering;
- scene rendering;
- animation;
- audio;
- save/load;
- Python bridge;
- low-end Android devices.

Representative emulator is not a replacement for physical handset QA.

## 11. Save migration

Before structural rewrite:
- inventory/save schema audit;
- world-map IDs audit;
- quest IDs audit;
- NPC state audit;
- equipment slots audit;
- stats/ability audit;
- versioned migration;
- old-save fixtures;
- rollback.

No final rebuild can simply discard player state.

## 12. Break/rebuild matrix

Every old subsystem will eventually receive:

| Subsystem | Keep | Rework | Replace | Delete | Migration | Verification |
| --- | --- | --- | --- | --- | --- | --- |
| Engine rules | TBD | TBD | TBD | TBD | required if changed | unit/integration |
| World map | TBD | likely | possible presentation replace | old renderer maybe | required | map tests + screenshot |
| Story UI | TBD | likely | possible | stale layouts | UI state | instrumentation |
| Character UI | TBD | likely | possible | placeholders | equipment/portrait | instrumentation |
| Assets | approved masters keep | manifests/atlas | placeholders | duplicates | ID mapping | visual QA |
| Saves | keep data intent | version | never silent reset | obsolete fields only | mandatory | migration tests |

This table becomes concrete only after the live audit.

## 13. Final rebuild phases

### R0 — Freeze documentation baseline
Tag exact docs/HEAD.

### R1 — Live implementation census
List every source file/module/screen/asset.

### R2 — Dependency graph
Identify what calls/owns what.

### R3 — Replacement architecture
Create new modules/interfaces behind compatibility adapters.

### R4 — State migration
Move authoritative state without breaking saves.

### R5 — Visual migration
Replace placeholders with production pixel assets.

### R6 — World/map migration
Implement final map hierarchy and room presentation.

### R7 — Mechanics migration
Integrate final progression/combat/NPC systems included in scope.

### R8 — Remove obsolete code
Delete only after replacement verification.

### R9 — APK optimization
Memory/package/performance.

### R10 — Certification
Exact-head CI, emulator, physical handset, screenshots, saves, accessibility.

## 14. Final documentation package

Before the final APK release candidate, create:
- final architecture;
- final file/module map;
- final screen map;
- final asset map;
- final state schema;
- final save schema;
- final world/map schema;
- final combat schema;
- final NPC schema;
- final test plan;
- final performance report;
- final physical-device report;
- final migration record;
- final deleted/retired list;
- final known limitations;
- final handoff.

## 15. Deletion rule

Deletion is last, not first.

A file/system is removed only when:
- it is proven obsolete;
- replacement is verified;
- no authoritative data is trapped in it;
- no active branch depends on it unexpectedly;
- rollback/history remains available.

## 16. Completion

The final APK reconstruction is complete only when the built artifact corresponds to the documented architecture and exact-head evidence proves the intended behavior.

A visually improved APK with undocumented state regressions is not a successful rebuild.

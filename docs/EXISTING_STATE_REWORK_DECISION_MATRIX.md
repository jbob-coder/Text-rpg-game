# THE GAME — Existing-State Rework Decision Matrix

Status: **ACTIVE / PROVISIONAL UNTIL FULL SOURCE AUDIT**  
Parent: `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`  
Purpose: record what is kept, extended, reworked, replaced, removed, or still unknown before large-scale rebuilding.

## 1. Decision vocabulary

- **KEEP** — preserve behavior/contract; improve only around it.
- **EXTEND** — preserve core contract and add capability.
- **REWORK** — same responsibility, substantial internal or presentation change.
- **REPLACE** — old implementation is not the target; migration required.
- **REMOVE** — delete only after replacement/migration and evidence.
- **UNKNOWN** — insufficient audit evidence.
- **NEW** — system does not currently exist at target scope and must be designed.

A classification is not permission to delete code immediately.

## 2. High-risk invariants

These are presumed KEEP until an explicit migration document proves otherwise:
- stable location IDs;
- stable quest/item/NPC IDs;
- player-safe projection boundary;
- authoritative gameplay state outside Compose;
- save schema compatibility;
- equipment slot semantics;
- hidden-state privacy;
- exact authored content state;
- asset provenance.

## 3. Engine and state

| Subsystem | Current direction | Decision | Target |
| --- | --- | --- | --- |
| deterministic Python rules engine | exists and verified on historical heads | KEEP + EXTEND | remain gameplay authority |
| scene/choice execution | authored content driven | KEEP + EXTEND | richer content, same authority model |
| stats/modifier pipeline | existing seven-attribute system and effective modifiers | KEEP now / REWORK later only through progression migration | one documented progression pipeline |
| resources | health/stamina/focus/resolve plus ability resources | KEEP + EXTEND | final resource taxonomy after progression master |
| quests | authored graph system | KEEP + EXTEND | larger quest/world integration |
| social/NPC memory | current memory/relationship/knowledge/goals foundation | KEEP + EXTEND | full schedules, factions, rival memory |
| powers/techniques | current authored progression foundation | KEEP + REWORK/EXTEND | integrate into final ability/class taxonomy |
| persistence | versioned save/load | KEEP; high-risk | explicit schema migration only |
| validation | content/reference validation exists | KEEP + EXTEND | validate world/system registries |

## 4. Android / application

| Surface | Decision | Reason / target |
| --- | --- | --- |
| Compose client shell | REWORK, not discard by default | current app is reproducible and state-safe, but final UX is not locked |
| Story surface | REWORK | make scene art, room actors, panels, choices and resources feel like one game space |
| Map surface | REWORK / partial REPLACE presentation | replace technical/geometric look with authored modular pixel-map composition while preserving state bindings |
| Character | REWORK visually | use approved Jack identity, 32x48 rig, equipment layers and canonical panels |
| Stats | EXTEND / visual REWORK | preserve projected values, improve hierarchy and progression clarity |
| Equipment | KEEP state contract / REWORK presentation | paper-doll slots remain; final art/alignment improves |
| Inventory/Bag | KEEP state contract / REWORK visual composition | authored icons, categories and item detail |
| Skills | KEEP state contract / REWORK presentation | final skill/class/rank hierarchy later |
| Quests | EXTEND / visual REWORK | support larger world and conditional objectives |
| Saves | KEEP behavior / REWORK UX if needed | never sacrifice compatibility for appearance |
| Settings | EXTEND | accessibility, audio/narration, controls, developer separation |
| Developer tools | KEEP separate / EXTEND | never leak into normal player experience |

## 5. Visual runtime

| Subsystem | Decision |
| --- | --- |
| source-native pixel-art philosophy | KEEP |
| nearest-neighbor raster path | KEEP |
| PNG runtime preference with source fallback | KEEP |
| 32x48 character rig | KEEP |
| 64x64 portrait contract | KEEP / extend |
| paper-doll equipment z-order | KEEP |
| current generic/provisional player appearance | REPLACE with approved Jack-compatible production art |
| weak geometric room/map masters | REWORK or REPLACE asset-by-asset |
| map node/state overlays | KEEP semantics / REWORK styling if needed |
| procedural/geometric fallback | KEEP as fallback only; not target art |
| room actor composition | EXTEND |
| actor portrait/panel system | NEW/EXTEND after safe actor projection |
| ambient animation | EXTEND selectively |
| state-driven overlays | KEEP separation / EXTEND |

## 6. Gate Twelve world/map

Current decisions:
- KEEP three-macrozone hierarchy.
- KEEP nine stable named locations unless a content migration later changes them.
- KEEP Gate Twelve presentation scaffold while Step 5 geometry remains authority.
- ADD the documented Depot Plaza <-> Platform Nine target connector only through engine/content migration.
- REWORK scene/map art that remains provisional.
- EXTEND area-specific asset packets.
- EXTEND actor/panel integration.
- DO NOT flatten the region into one generated image.

## 7. Character system

### Jack Wilson
Decision:
- approved identity reference becomes visual authority input;
- KEEP 32x48 rig and equipment anchors;
- REPLACE generic player silhouette over time with production Jack sprite set;
- ADD directional/pose/portrait assets as consumed;
- avoid creating every animation before gameplay needs it.

### Tamsin
Decision:
- KEEP authored identity;
- reconcile front room-actor code with full turnaround/manifest status;
- ADD portrait/emotion production assets;
- KEEP satchel, fringe, eyebrow notch, outfit anchors.

### Supporting actors
Decision:
- no anonymous art inheritance across named NPCs;
- reusable body/animation tooling is allowed;
- identity layers must remain character-specific;
- actor presence must come from projected game state.

## 8. World development

Current world beyond Gate Twelve is not complete.

Decision:
- NEW world-scale documentation and registries;
- do not pretend kingdoms/cities/ecosystems already exist;
- create schemas first;
- generate/place world content only after coordinate, political, ecology, level-band and economy rules are locked.

## 9. Progression

Current seven attributes:
- might;
- agility;
- endurance;
- intellect;
- will;
- perception;
- presence.

Decision:
- KEEP current schema for existing content/saves.
- Final progression master may EXTEND or MIGRATE it.
- Do not silently add/remove/rename base attributes.
- Classes, ranks, professions and citizen-status systems are NEW at target scope.
- Skills/abilities/passives need one shared taxonomy before mass content.

## 10. Tactical combat

Current target-scale tactical combat is not established.

Decision: **NEW SYSTEM**, integrated with existing authoritative state.

Broad goals:
- turn-based positional combat;
- action economy;
- cover/terrain;
- range/line-of-sight;
- injuries/conditions;
- ability/skill interaction;
- persistent consequences;
- AI;
- encounter rewards/state.

Do not copy another game's protected names, presentation or exact system expression.

## 11. Dynamic adversary system

Decision: **NEW ORIGINAL SYSTEM** built on existing NPC memory/state foundations.

Target:
- persistent named adversaries;
- encounter memory;
- evolving traits;
- relationships;
- status/rank changes;
- injuries and recovery where authored;
- faction effects;
- succession/replacement;
- world persistence.

It must use original terminology/data/UI.

## 12. Social hierarchy / discrimination

Decision: **NEW/EXTEND WORLD SYSTEM**.

Must model:
- legal status;
- wealth/class;
- occupation;
- faction;
- citizenship;
- institutional access;
- cultural prejudice;
- discrimination consequences;
- NPC beliefs vs institutional policy;
- player reputation/identity effects where authored.

Do not reduce social prejudice to a single universal numeric “racism” score.

## 13. Final APK

Decision:
- current APK/client is an implementation foundation, not final product.
- final reconstruction will classify each subsystem after domain contracts are complete.
- no broad deletion now.
- final work uses KEEP / EXTEND / REWORK / REPLACE / REMOVE with migration/evidence.

## 14. Removal policy

Nothing is removed merely because a replacement is planned.

Before REMOVE:
1. identify all consumers;
2. preserve source/evidence;
3. provide replacement;
4. migrate data/state;
5. run tests;
6. inspect UI evidence;
7. document rollback;
8. then remove on a working branch.

## 15. Audit debt

This matrix is intentionally high-level. The P0 existing-state audit still must enumerate:
- every source module;
- Android screen/component ownership;
- every content registry;
- save fields;
- asset catalogs;
- manifests;
- open PR branches;
- deprecated files;
- tests/evidence.

Until that audit is complete, UNKNOWN remains preferable to guessing.

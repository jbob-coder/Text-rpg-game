# P13 / D-026 — Hierarchical World Map Projection Migration Contract

**Status:** Wave-3 P13 documentation deliverable; FUTURE migration target, not implemented code or approved canon.  
**Player-AI:** Kestrel / PLAYER_KESTREL.  
**Authority:** OR-036; live Bulletin P13 claimed at `2a4e7ed59cd13d7529a2dd50b4dd91f5572ac04f`; source inspection HEAD `d59b2572b063687d87f22612e7bf88a77b930e41`.  
**Parent:** [Android Consumer & Projection Map](ANDROID_CONSUMER_AND_PROJECTION_MAP.md). **Design reference:** [Gate Twelve Region Master Plan](../assets/GATE_TWELVE_REGION_MASTER_PLAN.md).

## 1. Verified current data and ownership

| Current owner / exact source | Implemented behavior | Migration constraint |
| --- | --- | --- |
| `src/textrpg/android_bridge.py::_map_view_for` | Python emits `map.title`, `current_location`, discovered-only `nodes` with `id,title,description,x,y,current,reachable`, plus visible-endpoint `edges` with `from,to`. Discovery comes from current location, visited scenes, discovery flags; a distinct developer override exists. | No hidden node/edge disclosure, no implied world-scale hierarchy. |
| `src/textrpg/android_bridge.py::travel` | Validates destination existence, discovery and adjacent authored route; Python owns duration, state, scene or map override, history and rollback. Invalid requests produce public `TRAVEL_ERROR`. | Compose must not invent edges, unlocks, travel durations or teleportation. |
| `android/app/src/main/java/com/thegame/rpg/engine/GameEngine.kt` | `GameMapNode(id,title,description,x,y,current,reachable)`, `GameMapEdge(from,to)`, `GameWorldMap(title,currentLocation,nodes,edges)`; `GameSnapshot.worldMap` is typed and flat. | Current 21-field `GameSnapshot` is the live baseline, not the October 4 historical 19-field list. |
| `PythonGameEngine.kt` / `PythonSessionGateway.travel` | Forward `locationId` to authoritative Python and map returned snapshot. | No new world-logic calculations in Kotlin. |
| `GameViewModel.kt::travel` | Busy guard, delegates to engine; presents transition after confirmed location change. | Scope browsing is UI-only and must not advance time. |
| `GameScreen.kt::MapSection` | Renders only projected nodes/edges, coordinates as local map-sheet graphics, markers and `reachable` travel action. | Render/browse known data only; no world-coordinate or route synthesis. |

Gate Twelve region master plan section 2 uses local design hierarchy **REGION → MACROZONE → NAMED SUBZONE** and warns its spatial spine is not a set of implemented travel edges. The wider Android consumer plan section 8 proposes **world → macroregion → region → settlement → district → site/interior**. These are different scales and must be explicitly mapped by the future content/world owner. Internal streaming/loading cells must not become public locations solely because they exist technically. Existing node `x/y` values are local presentation positions, not global coordinates or tactical positions.

## 2. Proposed domain and field contract — NOT CURRENT WIRE API

A future Python owner may add a separate optional `hierarchical_map` domain while keeping the existing flat `map` unchanged. Under OR-015 use an additive, typed domain-version manifest, conceptually `meta.projection_versions.hierarchical_map = 1`; **the name and version 1 are a proposal, not a shipped contract**. Do not change durable `meta.schema_version` or save schema v1 for this document.

| Proposed typed family | Public fields and constraints |
| --- | --- |
| `HierarchicalMapSnapshot` | `version`, public `scope_id` and `scope_title`, `current_place_id`, `places[]`, `routes[]`, optional public breadcrumbs. |
| `PublicMapPlace` | Unique stable public `id`; known `parent_id` (nullable), `level`, `title`, public `description`, `current`, `reachable`, optional scope-relative `sheet_position` / public `visual_id`. |
| `PublicMapRoute` | `from_id`, `to_id`, optional public route status; every projected endpoint is an authorized known public place. |
| `MapSheetPosition` | finite `x,y` within declared `sheet_id`; never infer globally shared or tactical coordinates. |
| `MapUiSelection` | local selected public place, expanded branch, focus, pan, zoom; no durable gameplay authority. |

**Producer rules:** source place membership, parenthood, route permission and discovery come from authoritative Python/content/knowledge owners. No UI-accessible raw world registry, unpublished discovery flag, private quest/faction gate, route candidate, unobserved secret location or developer override. Filter before transport: hidden identifiers, labels, parent topology, route endpoints, locations, counts, breadcrumbs, art metadata, tooltips, accessibility semantics and error distinctions cannot indirectly expose undiscovered places. Public ID is a reference, not proof that a travel request is authorized.

**Mapper rules:** accept declared supported domain versions only; reject malformed/present-but-unversioned new domains, invalid enums, duplicate IDs, nonexistent parents, cycles, orphan edges, current-location mismatch, nonfinite coordinates and unexpected private nested fields. The actual final new wire keys/types are D-026 implementation-owner decisions after source approval; Compose receives typed allowlisted DTOs, never arbitrary raw maps.

## 3. Legacy compatibility and action migration

| Input / action | Required behavior |
| --- | --- |
| Old narrative view with no `hierarchical_map` | Legacy flat `GameWorldMap` and current `MapSection` continue rendering/travel unchanged; optional absent flat map retains existing empty-state behavior. |
| New valid hierarchy plus old flat `map` | Verify version, cross-references, current public location and allowlist; show hierarchical drilldown but preserve flat adapter until explicit migration/release approval. |
| Invalid or unsupported new hierarchy version | Fail closed with stable public mapping error; do not silently use raw map, display incomplete hidden information or mask version drift as valid hierarchy. |
| UI expand/collapse, select, pan/zoom | Presentation-only, no `travel`, no world-time advance and no mutations. Reset selection when public scope changes. |
| User requests actual travel | Display action only for Python-projected `reachable` known destination, call existing `GameEngine.travel(locationId)`, revalidate on Python. No Kotlin pathfinding or route legality. |
| Optional future `inspect_map_scope(scopeId)` | A *proposal* for read-only, player-safe scope queries if needed. It is not an implemented engine method and requires separate version/authorization. |
| Tactical combat and room actors | Hierarchical world locations are not D-069 tactical grid cells; static room `placement_key` remains presentation-only per OR-010. Keep D-073/D-074 tactical projections separate. |

## 4. Exact test and consumer map

| Current file/test | Confirmed present; future acceptance |
| --- | --- |
| `tests/test_android_bridge.py` | Current tests cover history-based discovery, discovered adjacent travel/time and undiscovered destination rejection without mutation. Future Python tests should cover hidden parent/route omissions, unauthorized scopes, no secret error side-channel, read-only stability and schema-v1 legacy view. |
| `android/app/src/test/java/com/thegame/rpg/engine/PythonGameEngineContractTest.kt` | Existing travel/gateway path; future tests assert exactly one forwarded location ID and no Android-derived world effects. |
| New Kotlin mapper tests under `android/app/src/test/java/com/thegame/rpg/engine/` | Legacy flat packet; supported typed hierarchy; absent/unknown/invalid required version; duplicate/cyclic parents, orphan edges, nonfinite coordinates, private nested fields, unknown public place and mismatched current location. |
| `android/app/src/main/java/com/thegame/rpg/GameViewModel.kt` and `TravelTransitionContractTest.kt` | Confirmed public-location delta drives transition, not hierarchy browsing; check busy/error/replacement and no phantom travel. |
| `android/app/src/main/java/com/thegame/rpg/ui/GameScreen.kt::MapSection`, `android/app/src/androidTest/java/com/thegame/rpg/ui/GameScreenTest.kt` | Future drilldown/back, accessible text/list fallback, no hidden names/counters/semantics or actionable travel for unreachable places; large text and reduced-motion acceptance. |
| `PixelMapArtCatalog.kt` and map catalogs | Local sheet art and known marker scope only; missing art gives safe list fallback. New world sheets do not reuse flat district `x/y` as global geography. |

All future tests listed are **NOT EXECUTED** by P13. Actual runtime Android/CI/emulator/phone acceptance must be run when an authorized implementation task exists.

## 5. Completion boundary

This child advances only the **P13/D-026 documentation** objective. Broader Master D-026 remains IN_PROGRESS for future activity, adversary intel, evolved progression/status, tactical runtime, final APK destination mapping and exact-head build/device evidence. Do not implement or score D-073/D-074 from this document; do not alter D-072/Silex, P11/Nodus or other Wave-3 lanes.

Future steps: (1) explicit authored public hierarchy/world IDs/relationships approved; (2) Python observer-filtered hierarchy and legacy-projection tests; (3) Kotlin typed versioned mapper and gateway/ViewModel contract; (4) phone-accessible Compose hierarchy view; (5) current flat-map equivalence, merge-state CI and physical-device verification. No additional save owner or canon geography is authorized by P13.

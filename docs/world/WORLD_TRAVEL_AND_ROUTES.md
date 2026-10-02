# THE GAME — World Travel and Routes

Status: **ACTIVE / WORLD ROUTE STANDARD**  
Parent: `docs/world/WORLD_DEVELOPMENT_MASTER_INDEX.md`

## 1. Purpose

This document defines route records and travel relationships from world scale down to district scale.

The route graph is authoritative gameplay/world data. Map art visualizes it; UI does not invent it.

## 2. Route classes

Possible route classes:
- road;
- street;
- footpath;
- stairs;
- gate/threshold;
- tram/rail;
- service corridor;
- tunnel;
- bridge;
- river/sea;
- air route if later supported;
- beast trail only if player traversal uses it.

## 3. Route record

Each route requires:
- `route_id`;
- endpoint IDs;
- directionality;
- route class;
- parent geography;
- access policy;
- discovery policy;
- travel cost/time when defined;
- distance when defined;
- terrain;
- capacity;
- risk;
- faction/security control;
- toll/cost if an economy system supports it;
- weather/event sensitivity;
- beast/ecosystem interaction;
- encounter hooks;
- visual transition packet;
- loading/technical notes separated from world meaning;
- player-safe state projection.

## 4. Access state

Route state may include:
- open;
- closed;
- restricted;
- blocked;
- dangerous;
- damaged;
- unknown;
- one-way;
- event-limited.

The base map must not permanently bake temporary access state into environment art.

## 5. Travel cost

Travel cost may include:
- time;
- stamina/resource cost;
- currency/toll only if approved;
- vehicle requirement;
- permit/status;
- risk roll/encounter opportunity.

Exact formulas belong to travel/activity systems.

## 6. Route danger

Danger is not only enemy level.

A route may carry:
- environmental hazard;
- beast threat;
- crime/faction threat;
- legal risk;
- weather;
- infrastructure failure;
- visibility/navigation difficulty.

## 7. Route visuals

Route art must communicate:
- major vs minor route;
- surface/material;
- direction;
- threshold;
- degradation;
- state overlays.

Permanent route visuals show physical existence. Reachability/current/selected/blocked states are overlays driven by player-safe state.

## 8. Hierarchical travel

The final map system may navigate:
- world;
- macroregion;
- region;
- settlement;
- district;
- site/interior.

The UI may collapse levels for usability, but route endpoints retain stable place IDs.

## 9. Gate Twelve proof route

Gate Twelve currently demonstrates:
- local district graph;
- hub branches;
- lower-network cross-link;
- proposed Plaza-to-Platform connector;
- expansion stubs;
- distinction between authored route and visually implied future route.

Any future implementation of `DISTRICT_PLAZA <-> PLATFORM_NINE` must be authored in world/content data rather than invented in Compose.

## 10. Route migration

Changing route topology requires:
- old/new graph comparison;
- quest/scene audit;
- save-state audit;
- map-art audit;
- travel-time audit;
- accessibility audit;
- test updates.

No silent graph rewrites.

## 11. Future route catalog

A later structured catalog should track:
- route records;
- endpoint validation;
- orphan places;
- disconnected components;
- cycles;
- reserved expansion stubs;
- route-state variants.

This catalog should be machine-checkable.

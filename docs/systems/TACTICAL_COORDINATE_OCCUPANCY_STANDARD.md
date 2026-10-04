# THE GAME — Tactical Coordinate & Occupancy Standard

Status: **APPROVED FIRST-PASS CONTRACT / IMPLEMENTATION NOT STARTED**
Parent authorities:
- docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md
- docs/systems/TACTICAL_COMBAT_MASTER_PLAN.md
- docs/systems/CAMERA_AND_TACTICAL_PRESENTATION_STANDARD.md
Phase 1 consumer:
- docs/PHASE_1_SOLO_PLAYABLE_PARALLEL_TRACK.md

## 1. Purpose

Define the authoritative coordinate, cell, occupancy, footprint, adjacency, and map-topology contract for turn-based tactical combat.

This document exists so pathing, cover, line of sight, targeting, AI, save/replay tooling, Android projection, and encounter authoring all use the same spatial truth instead of reconstructing geometry independently.

## 2. Current reality

At the pre-batch documentation head, the Python engine contains no dedicated tactical-combat module or durable tactical-state field. Current GameState owns world/story state, resources, relationships, knowledge, inventory, quests, NPCs, party, abilities, equipment, perks, history, turn, and world time. Tactical combat is therefore a target subsystem, not current runtime behavior.

Phase 1 does not require mid-combat save. The first implementation may keep tactical encounter state transient inside the authoritative Python rules layer and commit only the aftermath to durable GameState. Mid-combat save requires an explicit save-schema migration later.

## 3. Coordinate spaces

Tactical coordinates are separate from world, settlement/district, room-visual, and Android screen coordinates.

Normative tactical coordinate:
- x: integer column;
- y: integer row;
- z: integer elevation layer;
- cell key: x,y,z serialized as three integers joined with commas.

For Phase 1:
- movement is cardinal only;
- north = y - 1;
- east = x + 1;
- south = y + 1;
- west = x - 1;
- diagonal movement is not legal;
- attack rays may cross diagonal geometry, but movement adjacency remains four-way.

## 4. Tactical map record

A tactical map record must define:
- map_id;
- version;
- width;
- height;
- valid z layers;
- cells;
- explicit vertical transitions;
- deployment zones;
- objective anchors;
- exit/retreat cells;
- optional interactables;
- optional hazards;
- optional authored spawn anchors.

Each cell may define coord, terrain_id, movement_cost, blocks_movement, blocks_los, concealment, hazard_ids, edge cover metadata, interactable_id, and tags.

Unknown fields should be rejected by strict validation once the runtime schema is implemented unless the schema explicitly allows extensions.

## 5. Cell invariants

A valid tactical map must satisfy:
1. no duplicate coordinates;
2. every coordinate lies inside map bounds;
3. movement_cost is a finite positive integer for traversable cells;
4. blocked cells cannot be valid movement endpoints;
5. deployment/objective/exit anchors reference existing traversable cells;
6. vertical transitions reference two valid cells;
7. cover edges use only N/E/S/W;
8. interactable IDs are stable and unique within the encounter namespace;
9. no tactical cell may silently become world-location authority.

## 6. Occupancy model

Phase 1 unit footprint is one cell per actor.

Rules:
- two solid actors cannot end in the same cell;
- enemies cannot be traversed through;
- allied units may be traversed through only if the destination is not occupied and policy allows it;
- incapacitated bodies use explicit encounter blocking policy;
- non-solid FX/markers never own occupancy.

The schema may reserve larger footprints, but Phase 1 validates a one-cell footprint.

## 7. Tactical actor spatial state

Minimum runtime actor state:
- actor_id;
- faction_id;
- coord;
- facing;
- posture;
- footprint;
- alive/incapacitated state;
- activation eligibility.

Facing uses N/E/S/W for Phase 1 and must never be inferred from sprite orientation.

## 8. Deterministic adjacency

Cardinal neighbors are enumerated in fixed order:
1. north;
2. east;
3. south;
4. west.

This is only a deterministic tie-break.

Vertical adjacency exists only through explicit authored transitions such as stairs, ladders, ramps, drops, lifts, or climb edges.

## 9. Pathfinding contract

Phase 1 pathfinding should use deterministic A* or Dijkstra over authoritative movement edges.

Required:
- Manhattan heuristic for same-z cardinal movement;
- cost from destination cell/transition edge;
- no diagonal shortcut;
- occupancy checked before commit;
- preview and committed path use the same engine query;
- stable tie-break.

Recommended tie tuple:
(f_cost, h_cost, y, x, z, cell_key)

## 10. Topology mutation

Doors, hazards, or later destructible geometry may change blocks_movement, blocks_los, movement cost, active transitions, or interactable state.

They must change authoritative tactical state first. UI visuals follow.

Destructible terrain is not required for Phase 1.

## 11. Validation and failure behavior

Encounter setup fails safely before combat if spawn cells conflict, exits/objectives are invalid, topology is malformed, or actors reference invalid coordinates.

Do not silently repair malformed authored data.

## 12. Player-safe projection

Android may receive visible/discovered cells, legal movement destinations, currently visible occupancy, known terrain/cover/hazards, and selected path preview.

Android must not infer hidden occupants, compute legal pathing independently, reveal undiscovered cells, or decide collision.

## 13. Test requirements

Minimum tests:
- duplicate cell rejection;
- bounds validation;
- four-way adjacency;
- no diagonal movement;
- occupied endpoint rejection;
- enemy pass-through rejection;
- ally pass-through policy;
- deterministic equal-cost path tie;
- explicit z-transition traversal;
- blocked-cell handling;
- malformed objective/exit rejection;
- hidden occupancy redaction.

## 14. Phase 1 decisions

Locked for the first tactical slice:
- square grid;
- integer x/y/z;
- four-way movement;
- one-cell actors;
- explicit vertical transitions;
- engine-owned occupancy/pathing;
- no required destructible terrain;
- transient tactical state until aftermath is acceptable for Phase 1.

# World Spatial Hierarchy and Coordinate Contract

Status: DOCUMENTED / GLOBAL FOUNDATION
Program: D-01 World / Map / Regions

## Purpose

Define how the future large world is divided and how coordinate systems are named so local maps, world maps, UI, travel and later streaming cannot silently disagree.

This document does not invent world geography.

## Canonical planning hierarchy

`WORLD -> POLITY -> REGION -> SETTLEMENT -> DISTRICT -> LOCATION -> SUBLOCATION -> INTERACTION_ANCHOR`

Not every world entity requires every level.

Examples:
- wilderness may be WORLD -> REGION -> LOCATION;
- a major capital may use every level;
- an interior may be a SUBLOCATION under one stable LOCATION.

## Entity responsibilities

### WORLD
Owns:
- global orientation;
- global time/calendar assumptions if later defined;
- top-level climates/continents if adopted;
- top-level travel graph.

### POLITY
A kingdom/state/federation/territory or equivalent political unit.

Owns:
- jurisdiction;
- major law/social hierarchy;
- controlled regions;
- high-level economy/factions.

### REGION
Owns:
- terrain/ecosystem envelope;
- regional threat/resource profile;
- routes between settlements;
- regional events.

### SETTLEMENT
City, village, outpost, station, etc.

Owns:
- local economy;
- population bands;
- districts;
- civic/social services;
- entrances/exits.

### DISTRICT
Owns:
- coherent neighborhood/functional area;
- local routes;
- named locations;
- local visual/material identity.

Gate Twelve is the first documented DISTRICT pilot.

### LOCATION
A player-addressable place with stable identity.

### SUBLOCATION
An interior, room, courtyard, platform, tunnel section or other nested space when it needs separate state.

### INTERACTION_ANCHOR
A stable interaction point inside a location/sub-location when required by mechanics.

## Coordinate spaces

Every coordinate must name its space.

Allowed contract labels:

- `WORLD_GEO` — future large-world geographic coordinate system.
- `REGION_LOCAL` — coordinate system within one region.
- `SETTLEMENT_LOCAL` — coordinate system within one settlement.
- `DISTRICT_LOCAL` — coordinate system within one district.
- `MAP_PRESENTATION_PX` — native pixel-art map master coordinate.
- `MAP_NODE_PERCENT` — gameplay/UI projected node percentage.
- `SCENE_PX` — native scene illustration coordinate.
- `UI_VIEWPORT` — runtime screen coordinate.
- `CHARACTER_RIG` — character sprite anchor coordinate.

Never store a number as merely `x/y` in cross-system documentation without the coordinate-space context.

## Gate Twelve example

Current known spaces:
- presentation map: `MAP_PRESENTATION_PX 256x144`;
- gameplay node map: `MAP_NODE_PERCENT`.

The two may be projected into one another for UI, but neither silently replaces the other.

## World coordinate model — not yet selected

The final `WORLD_GEO` representation is still UNKNOWN.

Candidates for later evaluation:
- integer grid;
- fixed-point coordinate;
- graph-only geography plus regional local coordinates;
- hybrid global graph + regional metric coordinates.

Selection criteria:
- deterministic saves;
- map authoring;
- route/travel time;
- mobile precision;
- future tooling;
- easy migration;
- no need for unnecessary open-world simulation precision.

Do not assume real-world meters globally until the world-design requirement proves that useful.

## Route identity

Routes are entities, not just drawn lines.

A route record eventually needs:
- stable route ID;
- endpoints;
- route class;
- directionality;
- travel cost/time model;
- discovery/access rules;
- hazards;
- world-state variants;
- visual representation reference.

## Expansion boundary rule

Every settlement/district plan identifies:
- confirmed exits;
- reserved future exits;
- closed boundaries;
- unknown boundaries.

Reserved does not mean traversable.

## Coordinate migration

A coordinate migration must preserve:
- stable entity IDs;
- save compatibility or explicit migration;
- route identity;
- map-selection behavior;
- content bindings.

## Locked decisions

1. World documentation uses hierarchical stable entities.
2. Every coordinate belongs to a named coordinate space.
3. Gate Twelve's two current coordinate systems remain separate.
4. Final world-global coordinate representation remains undecided.
5. Routes become stable documented entities as the world expands.

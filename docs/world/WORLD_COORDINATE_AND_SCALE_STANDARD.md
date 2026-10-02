# THE GAME — World Coordinate & Scale Standard

Status: **ACTIVE / OPERATIONAL WORLD STANDARD**  
Repository: `jbob-coder/Text-rpg-game`  
Parents:
- `docs/world/WORLD_SCALE_DOCUMENTATION_BLUEPRINT.md`
- `docs/world/WORLD_GEOGRAPHY_STANDARD.md`

## 1. Purpose

Define the operational rules for coordinates, bounds, scale, transforms, route anchors and spatial validation across the future world.

The project needs several coordinate spaces because one number cannot safely serve:
- world geography;
- regional maps;
- settlements;
- districts;
- interiors;
- pixel-art presentation;
- tactical combat.

This standard prevents those spaces from being mixed silently.

## 2. Coordinate-space IDs

Every coordinate-bearing record must declare a `coordinate_space_id`.

Recommended families:

- `W0_WORLD_*` — global/macroregion;
- `W1_REGION_*` — regional geography;
- `W2_SETTLEMENT_*` — city/town/village;
- `W3_LOCAL_*` — district/site/interior logical space;
- `PRESENTATION_*` — pixel/map rendering;
- `W4_TACTICAL_*` — combat geometry.

Existing IDs are not renamed merely to match this convention.

## 3. Unit policy

No universal real-world unit is locked yet.

Each space must declare:
- unit type;
- axis orientation;
- origin;
- bounds;
- precision;
- scale-to-parent if defined.

Possible unit types:
- abstract logical unit;
- normalized coordinate;
- meter;
- tile/cell;
- native pixel;
- authored node coordinate.

Do not infer meters from pixels.

## 4. Axis policy

Every coordinate space records:
- X direction;
- Y direction;
- optional Z/elevation/depth direction;
- handedness when relevant;
- screen Y-down or world Y-up distinction.

Presentation coordinates may use screen conventions.

World/tactical coordinates may use another convention.

Transforms must state the difference explicitly.

## 5. Origin policy

Origins may be:
- world datum;
- region anchor;
- settlement reference point;
- district map origin;
- building/interior anchor;
- tactical-map origin.

An origin is part of the coordinate-space definition, not an undocumented assumption.

## 6. Bounds

Every bounded space records:
- minimum/maximum coordinate;
- shape or polygon when rectangular bounds are insufficient;
- parent-space footprint;
- overflow/expansion policy.

Unknown boundaries remain unknown rather than being filled with arbitrary rectangles.

## 7. Parent/child transform

When a child space has a known transform to its parent, record:
- parent space ID;
- parent anchor;
- translation;
- rotation if used;
- scale;
- elevation/depth offset;
- version.

If a precise transform is not known, record only topological containment.

## 8. Logical vs presentation coordinates

These must remain separate.

Logical coordinates answer:
- where a place is;
- what it connects to;
- distance/travel relationships.

Presentation coordinates answer:
- where the marker/art is drawn.

Changing presentation art must not silently change gameplay distance or route legality.

## 9. Gate Twelve proof rule

Current Gate Twelve uses:
- authored world-map node X/Y values in content;
- a separate 256x144 presentation planning grid.

These are **not automatically the same coordinate space**.

The final Gate Twelve packet must explicitly map node anchors to presentation anchors.

## 10. Place anchor types

A place may define:
- center anchor;
- entrance anchor;
- exit anchor;
- route anchor;
- landmark anchor;
- actor anchor;
- UI marker anchor;
- tactical transfer anchor.

A single center point is not sufficient for every use.

## 11. Route geometry

Each route eventually records:
- route ID;
- endpoint place IDs;
- endpoint anchor IDs;
- route class;
- logical distance;
- travel-time model;
- traversability;
- elevation/depth change;
- risk/hazard;
- presentation path;
- discovery/access state.

The route's drawn path is not the route's authority.

## 12. Distance

Distance types must be labeled:

- geometric distance;
- route distance;
- travel-time distance;
- narrative/interaction pacing;
- tactical movement cost.

Never substitute one silently for another.

## 13. Travel time

Travel time may depend on:
- route distance;
- transport mode;
- terrain;
- weather;
- encumbrance;
- injury;
- access/security;
- world event.

Current authored `travel_minutes` values remain authoritative where present.

Future formulas require separate balance validation.

## 14. Elevation and depth

Vertical position is important for:
- terrain;
- buildings;
- underground networks;
- Gate Twelve/lower maintenance;
- tactical LOS;
- beasts/ecology.

Record either:
- numeric elevation/depth when scale is known;
- ordinal level/band when numeric scale is not known.

Do not invent meters simply to populate a field.

## 15. Settlement coordinates

W2 settlement space should support:
- city boundary;
- districts;
- roads;
- gates;
- transit;
- major buildings;
- waterways;
- walls;
- vertical layers;
- expansion edges.

Large cities may use child district spaces rather than one enormous coordinate plane.

## 16. District/site coordinates

W3 local spaces support:
- streets;
- plazas;
- buildings;
- interiors;
- underground connectors;
- local navigation nodes.

Gate Twelve is the current proof case.

## 17. Interior coordinates

Interiors should record:
- building/site parent;
- floor/level;
- room IDs;
- doors/transition anchors;
- actor anchors;
- interaction anchors;
- occlusion/foreground zones if needed by art.

The game may still present an interior as a scene rather than free movement; coordinates remain useful for consistency and tactical conversion.

## 18. Tactical coordinates

W4 tactical spaces are encounter-specific or reusable tactical maps.

They require:
- deterministic cell/position IDs;
- occupancy;
- movement adjacency;
- elevation;
- cover;
- LOS blockers;
- hazards;
- interactables.

World coordinates determine where the encounter occurs, not individual tactical cell positions.

## 19. Presentation grids

Each map/scene art packet records:
- native pixel width/height;
- presentation coordinate space ID;
- source scale;
- anchor points;
- safe UI zones;
- nearest-neighbor scaling rule.

No stretching that changes anchor geometry.

## 20. Normalized map coordinates

Normalized coordinates may be used when:
- logical relationships matter more than physical scale;
- maps are responsive;
- exact world units are not yet locked.

If used, declare range explicitly, e.g. 0..1 or 0..100.

Do not assume the current Gate Twelve X/Y values use a specific normalized range until the content contract states it.

## 21. Precision

Each space declares precision:
- integer;
- fixed decimal;
- floating point;
- tile/cell index.

Stable serialized coordinates should avoid meaningless precision.

## 22. Negative coordinates

Negative coordinates are allowed if the space definition permits them.

Never encode “west” or “below” through undocumented negative values.

## 23. Coordinate versioning

Coordinate spaces require a version when:
- origin changes;
- scale changes;
- map bounds change;
- major projection changes.

A coordinate migration must record old -> new transforms or explicit remapping.

## 24. Map projection

World-to-screen projection may:
- compress;
- rotate;
- stylize;
- omit inaccessible detail.

The projection must preserve:
- topology;
- landmark relationships;
- route meaning;
- player-safe discovery.

It does not need to be geographically photorealistic.

## 25. Hidden geography

Undiscovered/secret places may exist in world data.

Player-facing projections must hide them until discovery/access rules expose them.

Base art must not reveal secret labels/routes accidentally.

## 26. Expansion edges

Every region/settlement/district may reserve:
- world-facing edge;
- road continuation;
- tunnel continuation;
- port/air/transit continuation;
- unexplored boundary.

Reserved edges are not active destinations until content exists.

## 27. Validation

Future validators should check:
- coordinate-space ID exists;
- parent containment is valid;
- anchors are within declared bounds unless explicitly external;
- route endpoints exist;
- presentation anchor exists for rendered locations;
- no duplicate stable anchor IDs;
- transforms reference valid parent versions;
- tactical maps do not overwrite world coordinates.

## 28. Record example — abstract

A coordinate record should resemble:

```json
{
  "space_id": "W3_LOCAL_GATE_TWELVE",
  "unit": "authored_local",
  "origin": {"x": 0, "y": 0},
  "bounds": {"min_x": 0, "min_y": 0, "max_x": 100, "max_y": 100},
  "axis": {"x": "east", "y": "south_on_map"},
  "version": 1
}
```

This is an example schema only, not a declaration that Gate Twelve uses 0..100.

## 29. Coordinate registry

Future machine-readable registry should include:
- coordinate spaces;
- versions;
- parent relationships;
- unit definitions;
- transforms;
- bounds.

Suggested future path:
`content/world/coordinate_spaces.json`.

Do not create the registry until initial canonical world parents are decided.

## 30. World-map production order

1. define world parent/macroregions;
2. define W0 space;
3. define regional spaces;
4. place political/geographic boundaries;
5. place major settlements/resources/ecosystems;
6. define routes;
7. define settlement spaces;
8. define district/site spaces;
9. map art anchors;
10. tactical spaces only for encounters that need them.

## 31. Open decisions

- final world shape/size;
- W0 unit;
- exact Gate Twelve parent settlement;
- physical scale of Gate Twelve;
- world projection;
- travel distance formula;
- city scale bands;
- terrain/elevation units;
- tactical cell size;
- whether any spaces use meters.

Unknown remains explicit.

## 32. Completion gate

This standard is ready to support world population when:
- canonical world parent hierarchy is decided;
- first W0/W1 spaces are registered;
- unit/origin/bounds are declared;
- Gate Twelve W3/presentation mapping is recorded;
- route validation is implemented or scheduled.

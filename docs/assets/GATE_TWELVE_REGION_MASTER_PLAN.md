# Gate Twelve Region — Master Map & Application Plan

Status: **ACTIVE / STEPWISE AUTHORING**  
Repository: `jbob-coder/Text-rpg-game`  
Working branch: `docs/settlement-region-build-plan`  
Started: 2026-10-01  
Purpose: define, build, integrate, and verify the Gate Twelve region as a high-use playable area inside the larger game.

---

# 0. How this document is authored

This is a **living master plan**. It is intentionally completed in controlled steps rather than written all at once.

Each step must:
1. preserve all previously confirmed decisions unless an explicit revision is recorded;
2. distinguish confirmed game facts from design decisions and external-reference inspiration;
3. connect map design to concrete application/game implementation;
4. avoid inventing physical measurements, colors, or gameplay rules merely to fill gaps;
5. end with a continuity note so another session can resume from the next unfinished step.

The goal is not to create a decorative concept document. The goal is to make the document executable: another agent/session should be able to read it, understand what is authoritative, know what has been decided, and continue building the game without reconstructing intent from chat history.

---

# 1. Project authority and design mandate

## 1.1 Active project

The active project for this work is:

`jbob-coder/Text-rpg-game`

This document applies to that project only.

Other repositories, previous game prototypes, and outside games may supply ideas or comparison material, but they are not authoritative for this implementation unless a decision in this document explicitly adopts a concept.

## 1.2 Region scope

The region being planned is **Gate Twelve District**.

It is a relatively small playable region inside a larger game world. It must therefore be designed as:

- a coherent place in its own right;
- a high-use area where the player can spend substantial play time;
- a region that can connect outward to a larger map;
- a region that can be expanded without discarding its core layout;
- a region whose visual presentation, navigation, interaction, and application UX reinforce one another.

The district is not a stand-alone game map.

## 1.3 Existing authoritative game data

The existing game already defines the following named Gate Twelve District locations:

- `PLATFORM_NINE`
- `RELAY_WORKBENCH`
- `GATE_TWELVE`
- `SERVICE_TUNNEL`
- `EVAC_STAIR` / Quiet Stair
- `TRACE_CHAMBER`
- `DISTRICT_PLAZA` / Depot Plaza
- `DISTRICT_ARCHIVE` / Municipal Archive
- `WORKSHOP_ROW`

The existing content also defines world-map node coordinates and route edges for these locations.

Those IDs, authored routes, travel rules, discovery rules, quest bindings, and player-safe state are authoritative gameplay data unless a later design change deliberately migrates them.

## 1.4 Existing authoritative visual geometry

The current Gate Twelve visual blueprint uses:

- map master: `MAP_GATE_TWELVE_DISTRICT_BASE`;
- native presentation grid: **256x144**;
- three confirmed horizontal spatial bands:
  - surface civic district;
  - depot/service belt;
  - lower maintenance infrastructure.

This visual grid is the current spatial scaffold for production planning.

Important distinction:

- the 256x144 coordinates are presentation geometry;
- the engine's map nodes and route graph remain authoritative for gameplay travel;
- neither should silently overwrite the other.

## 1.5 External reference set

The external material supplied on 2026-10-01 is classified as:

`EXTERNAL_DESIGN_REFERENCE / NON-AUTHORITATIVE`

It may be used to study and adapt:

- section hierarchy;
- settlement readability;
- route hierarchy;
- central-node design;
- landmark spacing;
- modular building planning;
- reusable prop families;
- navigation organization;
- streaming/section-loading ideas;
- production sequencing;
- map-to-asset decomposition.

It must **not** be treated as a specification.

The following are explicitly non-binding unless separately approved:

- its exact number of sectors/areas;
- its physical dimensions;
- its color coding;
- its exact street widths;
- its building counts;
- its medieval-specific architecture;
- its named characters;
- its item identities;
- its world lore;
- any conflicting numeric labels.

Design rule:

> Extract useful structure; do not inherit contradictions.

## 1.6 Decision authority

The implementation is allowed to improve or replace existing presentation code when a better solution requires it.

The project owner has explicitly authorized changes that may break or supersede existing application presentation **when the replacement is materially better and is implemented deliberately**.

That permission does not mean uncontrolled rewrites.

Before a breaking change is promoted, the work must document:

- what existing behavior is being replaced;
- why the old behavior is insufficient;
- what becomes the new source of truth;
- migration/compatibility impact;
- tests or QA required;
- rollback boundary when practical.

Gameplay-authoritative state must not be moved into UI code simply to simplify rendering.

## 1.7 Application-first design requirement

Gate Twelve is expected to be one of the areas where the player spends significant time.

Therefore the design target is not merely a correct map. The **application experience** must also improve around the region.

Map planning must consider:

- the Map surface;
- Story/location presentation;
- player position and selected-location feedback;
- route readability;
- discovery/reachability states;
- location previews;
- navigation between screens;
- loading/section transitions when applicable;
- touch hit targets;
- phone-width readability;
- asset reuse;
- state overlays;
- future expansion.

The application may be reorganized where necessary so that the region feels like one coherent playable space instead of disconnected screens.

## 1.8 Core separation of responsibilities

The implementation must preserve these boundaries:

### Gameplay authority
Owned by engine/content state:
- node identity;
- route graph;
- travel legality;
- discovery;
- reachability;
- quest state;
- NPC state;
- inventory/equipment;
- hidden state;
- time cost;
- story outcomes.

### Visual authority
Owned by approved assets/blueprints:
- permanent landmark appearance;
- material language;
- silhouettes;
- surface families;
- building modules;
- props;
- environmental dressing;
- presentation composition.

### UI/application authority
Owned by presentation code:
- how the map is framed;
- zoom/selection behavior;
- touch interaction;
- panels;
- transitions;
- navigation;
- readable overlays;
- responsive layout.

UI may present authoritative state; it may not invent it.

## 1.9 Design priorities

When decisions conflict, use this order:

1. gameplay correctness;
2. spatial coherence;
3. player readability;
4. repeated-use comfort;
5. visual identity;
6. modularity/reuse;
7. performance;
8. implementation convenience.

A visually impressive change that damages route comprehension, state clarity, or phone usability is rejected.

## 1.10 What is deliberately NOT decided yet

This step does not yet lock:

- a real-world meter scale;
- final street widths;
- final section-loading boundaries;
- final building footprints beyond already-confirmed geometry;
- final color palette for every region;
- final prop density;
- final camera/zoom behavior;
- new gameplay routes;
- new NPCs;
- new quests;
- final map artwork;
- animation timing.

Those decisions belong to later steps and must be derived from the authority established here.

---


# 2. Spatial hierarchy

Status: **COMPLETE — DESIGN STRUCTURE LOCKED FOR THE NEXT STEPS**

This step defines how Gate Twelve District is organized spatially before route design, building production, or application rework begins.

The hierarchy is derived from two authoritative inputs:

1. the nine existing named world-map locations and their current route graph;
2. the confirmed three-band 256x144 Gate Twelve presentation geometry.

The external reference material influences organization principles only. Its five-section and twelve-area counts are not copied.

## 2.1 Hierarchy model

Gate Twelve will use a three-level spatial hierarchy:

`REGION -> MACROZONE -> NAMED SUBZONE`

A later implementation may introduce technical loading cells beneath this hierarchy, but loading cells must not become player-facing geography unless they also make sense as real places.

### Region

- **Gate Twelve District**
- role: one important local region inside a larger world map;
- current presentation master: `MAP_GATE_TWELVE_DISTRICT_BASE`;
- current native visual planning grid: 256x144.

### Macrozone A — Surface Civic District

Purpose:
- public-facing district space;
- social/readable orientation layer;
- free-roam civic functions;
- future connection to the larger surface world.

Named subzones:
- `WORKSHOP_ROW`
- `DISTRICT_PLAZA` / Depot Plaza
- `DISTRICT_ARCHIVE` / Municipal Archive

Spatial identity:
- brighter and more public than lower infrastructure;
- open sightlines and obvious civic landmarks;
- acts as the player's main orientation layer once free roam is available.

Structural role:
- Depot Plaza is the central civic anchor.
- Workshop Row forms the western functional branch.
- Municipal Archive forms the eastern institutional branch.
- The player should be able to understand the surface district from the plaza without needing a minimap to know which direction serves which function.

### Macrozone B — Depot / Gate Core

Purpose:
- narrative and mechanical hinge between public district space and restricted infrastructure;
- opening-game concentration of story actions;
- strongest transition point between ordinary municipal life and Gate Twelve's restricted systems.

Named subzones:
- `PLATFORM_NINE`
- `RELAY_WORKBENCH`
- `GATE_TWELVE`
- `TRACE_CHAMBER`

Spatial identity:
- denser service geometry;
- stronger infrastructure silhouettes;
- more controlled access;
- less open than the civic layer, but still legible enough for repeated player use.

Structural role:
- Platform Nine is the depot-side hub.
- Relay Workbench is a small technical annex attached to the Platform Nine activity cluster.
- Gate Twelve is the threshold landmark and the primary descent/transition control point.
- Trace Chamber is an eastern technical spur connected to Gate Twelve and Service Tunnel systems.

Important band note:
- Trace Chamber spans the boundary between the upper and service visual bands in the current geometry.
- It is therefore classified by **function and connectivity**, not merely by its topmost Y coordinate.
- This avoids forcing the presentation grid into an artificial hard zoning rule.

### Macrozone C — Lower Maintenance Network

Purpose:
- quieter and more restricted traversal;
- lower-infrastructure exploration;
- future expansion toward deeper or exterior service routes.

Named subzones:
- `EVAC_STAIR` / Quiet Stair
- `SERVICE_TUNNEL`

Spatial identity:
- darker infrastructure;
- longer connective geometry;
- fewer public-facing landmarks;
- stronger sense of depth and separation from surface activity.

Structural role:
- Quiet Stair is the alternate evacuation/egress branch.
- Service Tunnel is the deeper infrastructure branch.
- These are not interchangeable exits: one reads as an evacuation path, the other as restricted service continuation.

## 2.2 Named-subzone ownership

Every current named location belongs to exactly one macrozone for planning purposes:

| Stable ID | Player-facing name | Macrozone | Primary spatial role |
| --- | --- | --- | --- |
| `WORKSHOP_ROW` | Workshop Row | Surface Civic District | western repair/contractor branch |
| `DISTRICT_PLAZA` | Depot Plaza | Surface Civic District | public orientation hub |
| `DISTRICT_ARCHIVE` | Municipal Archive | Surface Civic District | eastern institutional branch |
| `PLATFORM_NINE` | Platform Nine | Depot / Gate Core | depot-side internal hub |
| `RELAY_WORKBENCH` | Relay Workbench | Depot / Gate Core | compact technical annex |
| `GATE_TWELVE` | Service Gate Twelve | Depot / Gate Core | threshold / controlled descent |
| `TRACE_CHAMBER` | Trace Chamber | Depot / Gate Core | eastern technical spur |
| `EVAC_STAIR` | Quiet Stair | Lower Maintenance Network | alternate evacuation/egress branch |
| `SERVICE_TUNNEL` | Service Tunnel | Lower Maintenance Network | deeper maintenance continuation |

This classification is a planning hierarchy. It does not by itself change any world-map node, scene ID, route, discovery flag, or travel rule.

## 2.3 Current authoritative adjacency

The current content defines these route edges:

### Surface Civic component
- `DISTRICT_PLAZA <-> DISTRICT_ARCHIVE`
- `DISTRICT_PLAZA <-> WORKSHOP_ROW`

### Depot / lower component
- `PLATFORM_NINE <-> RELAY_WORKBENCH`
- `PLATFORM_NINE <-> GATE_TWELVE`
- `PLATFORM_NINE <-> EVAC_STAIR`
- `GATE_TWELVE <-> SERVICE_TUNNEL`
- `GATE_TWELVE <-> TRACE_CHAMBER`
- `SERVICE_TUNNEL <-> TRACE_CHAMBER`

These edges remain authoritative until a later implementation step explicitly changes content data and tests.

## 2.4 Structural graph gap

The existing world-map graph currently contains **two disconnected components**:

Component 1:
`WORKSHOP_ROW <-> DISTRICT_PLAZA <-> DISTRICT_ARCHIVE`

Component 2:
`RELAY_WORKBENCH <-> PLATFORM_NINE <-> GATE_TWELVE / EVAC_STAIR -> SERVICE_TUNNEL / TRACE_CHAMBER`

There is no authored edge connecting the public surface component to the depot/gate component.

This is now recorded as a deliberate design issue rather than being silently hidden by art.

### Proposed primary connector

The preferred future connector is:

`DISTRICT_PLAZA <-> PLATFORM_NINE`

Reasoning:
- Depot Plaza is described as the open space outside the tram depot.
- Platform Nine is inside that depot.
- This connection produces the cleanest public-to-depot threshold.
- It preserves Depot Plaza as the surface orientation hub.
- It preserves Platform Nine as the internal depot hub.
- It avoids using Workshop Row or Municipal Archive as an arbitrary transit bridge.
- It creates a readable progression:
  `surface district -> plaza -> depot -> Gate Twelve -> lower infrastructure`.

Status:
- **PROPOSED DESIGN CONNECTION**
- not yet added to `content/vertical_slice_01.json`;
- not yet assigned a travel-minute cost;
- not yet player-visible as a new route;
- must be handled in Step 3 circulation and later implementation/migration work.

## 2.5 Spatial spine

The intended high-level spatial spine is:

`LARGER SURFACE WORLD -> DEPOT PLAZA -> PLATFORM NINE -> GATE TWELVE -> LOWER MAINTENANCE`

This is a design hierarchy, not a claim that all five transitions are currently authored gameplay edges.

It gives the district one understandable mental model:

- **above / public** — civic district;
- **middle / threshold** — depot and Gate Twelve;
- **below / restricted** — maintenance network.

The player should be able to infer this structure from landmarks and transitions, not only from labels.

## 2.6 Side branches

The district should not become a single corridor. The spatial spine is supported by lateral branches:

From Depot Plaza:
- west -> Workshop Row;
- east -> Municipal Archive;
- inward/down -> proposed Platform Nine threshold.

From Platform Nine:
- annex -> Relay Workbench;
- threshold -> Gate Twelve;
- alternate egress -> Quiet Stair.

From Gate Twelve:
- deeper route -> Service Tunnel;
- technical spur -> Trace Chamber.

From Service Tunnel:
- cross-link -> Trace Chamber.

This creates a readable hub-and-branch structure while retaining alternate circulation in the restricted layer.

## 2.7 Entrances, exits, and expansion stubs

This step distinguishes **confirmed route**, **described boundary**, and **future expansion stub**.

### A. Surface-world boundary — Depot Plaza

Classification:
- **FUTURE WORLD-FACING CONNECTION CANDIDATE**

Evidence:
- Depot Plaza is an open public space outside the tram depot.
- It is the strongest current surface hub.

Decision:
- reserve the plaza's outer edge as the preferred connection to the future larger surface-world map;
- do not add a new world-map destination yet;
- future world expansion should connect here unless later world design provides a stronger reason not to.

### B. Quiet Stair boundary

Classification:
- **DESCRIBED EGRESS / DESTINATION UNMAPPED**

Evidence:
- current text describes Quiet Stair as a maintenance stair that exits away from the main evacuation flow.

Decision:
- preserve it as an egress-facing boundary;
- do not invent the external destination yet;
- future expansion may attach an evacuation/service destination here.

### C. Service Tunnel deep boundary

Classification:
- **DEEP-INFRASTRUCTURE EXPANSION STUB**

Evidence:
- Service Tunnel is restricted infrastructure beneath the evacuation route;
- current lore also supports the idea of continuation below mapped service levels.

Decision:
- preserve a deeper continuation direction;
- do not expose an unimplemented destination;
- later regions may attach below/through this branch without redesigning Gate Twelve.

### D. Workshop Row / Municipal Archive outer edges

Classification:
- **LOCAL DISTRICT EDGES, NOT CURRENT WORLD EXITS**

Decision:
- keep their footprints expandable and visually connected to surrounding urban fabric;
- do not treat either location as the primary inter-region gateway.

## 2.8 Macrozone transition rules

Transitions between macrozones should feel physically meaningful.

### Surface Civic -> Depot / Gate Core
Desired transition:
- public paving and open civic frontage gradually give way to depot structure, track/service surfaces, controlled doors, and denser infrastructure.

Primary transition pair:
- `DISTRICT_PLAZA -> PLATFORM_NINE` (proposed)

### Depot / Gate Core -> Lower Maintenance
Existing transition pairs:
- `PLATFORM_NINE -> EVAC_STAIR`
- `GATE_TWELVE -> SERVICE_TUNNEL`

These two transitions should feel different:
- Quiet Stair = evacuation/egress logic;
- Service Tunnel = restricted/deeper infrastructure logic.

## 2.9 Landmark hierarchy

The map should establish three levels of landmark importance.

### Tier 1 — district anchors
- Depot Plaza
- Platform Nine
- Gate Twelve

These should remain visually recognizable at the smallest normal map presentation scale.

### Tier 2 — functional destinations
- Workshop Row
- Municipal Archive
- Quiet Stair
- Service Tunnel
- Trace Chamber

These need distinct silhouettes/material cues but do not need to dominate the whole district.

### Tier 3 — local focal point
- Relay Workbench

Relay Workbench is important narratively and interactively but should remain visually subordinate to Platform Nine at district-map scale.

This prevents every location from competing for equal visual emphasis.

## 2.10 External-reference ideas adopted in Step 2

The following structural ideas from the external material are adopted:

- use a clear center/hub rather than evenly distributing all destinations;
- organize the region into understandable functional sections;
- preserve one major orientation spine with side branches;
- reserve obvious entrances/exits for future map expansion;
- keep subdivision modular so detailed areas can be built independently;
- distinguish player-facing zones from technical streaming/loading cells;
- use landmarks to teach navigation.

The following are explicitly rejected as fixed requirements:

- exactly five player-facing sectors;
- exactly twelve player-facing areas;
- exact reference dimensions;
- exact reference colors;
- copying its medieval gate/plaza/market identities;
- forcing every section to be equal in size;
- treating section boundaries as visible walls solely for loading convenience.

## 2.11 Application implications established by this hierarchy

The application must eventually support this hierarchy without making the player manage internal technical complexity.

Required future behavior:
- Map screen can communicate the three macrozone identities visually without requiring three separate maps.
- Selected location details remain tied to stable location IDs.
- Current/discovered/reachable markers remain state overlays.
- The UI should make the district spine understandable at phone width.
- A future larger-world map must be able to enter Gate Twelve through a reserved boundary without replacing the district map.
- Location previews can become richer without owning route legality.
- If section loading is later introduced, technical section boundaries should follow spatial logic but remain invisible to the player unless a real transition exists.

No UI code is changed in Step 2.

## 2.12 Step 2 locked decisions

The following decisions are now locked for subsequent planning unless explicitly revised:

1. Gate Twelve uses **3 player-facing macrozones**, derived from confirmed spatial bands and functional identity.
2. The current **9 named locations** are the subzones.
3. Depot Plaza is the surface civic hub.
4. Platform Nine is the depot/internal hub.
5. Gate Twelve is the primary restricted-threshold landmark.
6. Quiet Stair is an egress-facing lower branch.
7. Service Tunnel is the deep-infrastructure branch.
8. Trace Chamber is classified with the Depot / Gate Core by function/connectivity even though its geometry crosses a visual-band boundary.
9. The existing route graph's two disconnected components are a documented design gap.
10. `DISTRICT_PLAZA <-> PLATFORM_NINE` is the preferred future connection, but is not yet an implemented gameplay edge.
11. Depot Plaza is the preferred future surface-world attachment point.
12. Quiet Stair and Service Tunnel remain reserved for different future expansion directions.
13. Technical loading sections, if added later, must not dictate player-facing geography.

---


# 3. Circulation and player flow

Status: **COMPLETE — CIRCULATION MODEL LOCKED FOR LATER IMPLEMENTATION**

This step defines how the player should move through Gate Twelve District, how routes are prioritized, how landmarks teach orientation, and how the district avoids becoming either a single corridor or a confusing set of disconnected nodes.

No gameplay edge, travel cost, content JSON, or UI code is changed in this step.

## 3.1 Circulation goals

Gate Twelve circulation must satisfy six goals:

1. **Teach the district through movement.**  
   The player should understand "surface -> depot -> Gate Twelve -> lower infrastructure" by moving through it, not by memorizing a node list.

2. **Keep high-use destinations close to recognizable hubs.**  
   Repeated visits should not require excessive navigation overhead.

3. **Support optional detours without destroying orientation.**  
   Workshop Row, Municipal Archive, Relay Workbench, Quiet Stair, and Trace Chamber should feel like meaningful branches, not random map dots.

4. **Provide at least one lower-level cross-link.**  
   The existing `SERVICE_TUNNEL <-> TRACE_CHAMBER` edge is valuable because it prevents the restricted layer from becoming pure out-and-back traversal.

5. **Preserve different route identities.**  
   Public civic movement, depot movement, evacuation movement, and deep-maintenance movement should not all feel identical.

6. **Allow later world expansion.**  
   Surface, evacuation, and deep-service boundaries must remain available for future regions.

## 3.2 Route hierarchy

Routes are divided into four circulation classes.

### Class A — District spine

The intended principal route is:

`FUTURE SURFACE WORLD -> DISTRICT_PLAZA -> PLATFORM_NINE -> GATE_TWELVE -> SERVICE_TUNNEL -> FUTURE DEEP INFRASTRUCTURE`

Current implementation status:
- `DISTRICT_PLAZA -> PLATFORM_NINE` is not yet authored;
- future surface/deep destinations are not yet authored;
- `PLATFORM_NINE -> GATE_TWELVE` and `GATE_TWELVE -> SERVICE_TUNNEL` already exist.

Purpose:
- gives the district one memorable through-line;
- makes Gate Twelve feel like a threshold instead of a random node;
- supports eventual expansion in both directions;
- prevents the civic district and depot infrastructure from reading as unrelated maps.

This route must receive the strongest landmark continuity and the clearest visual transitions.

### Class B — Hub branches

These connect a major hub to a destination with a clear local purpose:

From Depot Plaza:
- `DISTRICT_PLAZA <-> WORKSHOP_ROW`
- `DISTRICT_PLAZA <-> DISTRICT_ARCHIVE`

From Platform Nine:
- `PLATFORM_NINE <-> RELAY_WORKBENCH`
- `PLATFORM_NINE <-> EVAC_STAIR`

From Gate Twelve:
- `GATE_TWELVE <-> TRACE_CHAMBER`

These routes should be easy to understand from their hub and should not visually compete with the district spine.

### Class C — Lower-network cross-link

- `SERVICE_TUNNEL <-> TRACE_CHAMBER`

Purpose:
- creates a partial loop in the restricted layer;
- allows Trace Chamber to be approached from more than one direction;
- reduces unnecessary return-to-Gate-Twelve behavior;
- makes the lower network feel spatial rather than menu-like.

This edge should remain visually more subordinate than the spine.

### Class D — Future expansion stubs

Reserved, not currently player-routable:
- Depot Plaza -> larger surface world;
- Quiet Stair -> future evacuation/service destination;
- Service Tunnel -> deeper infrastructure.

These should be implied by architecture and orientation but must not appear as usable destinations until content exists.

## 3.3 Decision on the Depot Plaza <-> Platform Nine connector

Step 3 upgrades the proposed connector from "possible" to **REQUIRED FOR THE TARGET CIRCULATION MODEL**, while still leaving implementation for a later step.

Decision:

`DISTRICT_PLAZA <-> PLATFORM_NINE`

is approved as the preferred future authored connection.

Why it is necessary:
- the current graph is split into two disconnected components;
- Depot Plaza is described as outside the tram depot;
- Platform Nine is inside the depot;
- the pair forms the natural public-to-depot threshold;
- joining them creates one coherent district without inventing a new location;
- it aligns with the visual geometry and with the intended mental model;
- it avoids forcing the player through Workshop Row or Municipal Archive merely to reach the depot.

Not decided yet:
- travel-minute cost;
- exact doorway/corridor geometry;
- whether the transition is represented as an exterior entrance, concourse, short passage, or another authored spatial connector;
- unlock timing beyond respecting existing free-roam/story state.

Implementation rule:
- when eventually added, it must be authored in the engine/content graph;
- the UI must consume that route, not fabricate it locally.

## 3.4 Primary player flows

The district supports multiple flows depending on game phase.

### Flow A — Opening / first exposure

The opening already begins in Platform Nine.

The intended mental sequence is:

`PLATFORM_NINE -> RELAY_WORKBENCH -> decision point -> GATE_TWELVE / EVACUATION BRANCH`

Design intent:
- teach the depot core before exposing the larger civic district;
- make Relay Workbench feel attached to Platform Nine rather than like a separate neighborhood;
- make Gate Twelve the first major "deeper" landmark;
- preserve Quiet Stair as an alternate spatial idea: escape/egress rather than investigation.

The opening should not require the player to understand the whole district map immediately.

### Flow B — First free-roam orientation

Once free roam is available, Depot Plaza becomes the preferred orientation hub.

Target sequence:
- arrive/return to Depot Plaza;
- immediately understand west = Workshop Row;
- east = Municipal Archive;
- inward/depot = Platform Nine;
- outward = future larger world boundary.

This is the point where the player learns that the opening locations are part of a larger district rather than a separate dungeon.

### Flow C — Repeated civic errands

Typical loop:
`DEPOT PLAZA -> WORKSHOP ROW / MUNICIPAL ARCHIVE -> DEPOT PLAZA`

Requirements:
- short conceptual distance;
- clear return path;
- no need to traverse Platform Nine or Gate Twelve for ordinary civic errands;
- locations should feel adjacent to the plaza but functionally distinct.

### Flow D — Return to restricted investigation

Target:
`DEPOT PLAZA -> PLATFORM NINE -> GATE TWELVE -> SERVICE TUNNEL / TRACE CHAMBER`

Requirements:
- the public-to-restricted transition should be obvious;
- each step should increase enclosure/infrastructure intensity;
- the player should feel that Gate Twelve is a threshold, not simply another icon.

### Flow E — Lower-network loop

Existing loop-capable structure:
`GATE_TWELVE -> SERVICE_TUNNEL -> TRACE_CHAMBER -> GATE_TWELVE`

This should be preserved because it:
- supports alternate approach/return;
- reduces repetitive backtracking;
- gives Trace Chamber a spatial relationship to both the gate and tunnel.

### Flow F — Evacuation/alternate egress

`PLATFORM_NINE -> EVAC_STAIR -> FUTURE EXTERNAL DESTINATION`

For now the route ends at Quiet Stair.

Its circulation identity must remain:
- separate from Gate Twelve investigation;
- practical;
- evacuation-oriented;
- visually readable as "away from the main flow."

## 3.5 Hub design

### Depot Plaza — public hub

Depot Plaza should support four directional readings:

- west: Workshop Row;
- east: Municipal Archive;
- inward/depot: Platform Nine;
- outward: future surface world.

The player should not need to open a detail panel to understand those relationships.

The plaza should therefore have:
- generous negative space;
- visible or strongly implied destination silhouettes;
- directional material changes;
- minimal clutter along primary desire lines.

### Platform Nine — internal hub

Platform Nine should support three strong branches:

- technical annex: Relay Workbench;
- restricted threshold: Gate Twelve;
- egress: Quiet Stair.

Platform Nine must remain more enclosed than Depot Plaza but still function as an orientation point.

### Gate Twelve — threshold hub, not social hub

Gate Twelve should support:
- return toward Platform Nine;
- descent/continuation toward Service Tunnel;
- technical spur toward Trace Chamber.

It should not accumulate unrelated civic functions. Its identity depends on being a controlled threshold.

## 3.6 Landmark visibility rules

"Visibility" here means visual orientation at map/scene scale, not necessarily literal uninterrupted 3D line of sight.

### From Depot Plaza
The player should be able to identify or infer:
- depot/Platform Nine entrance as the dominant inward landmark;
- Workshop Row direction;
- Municipal Archive direction;
- surface-world continuation.

### From Platform Nine
The player should be able to identify or infer:
- Gate Twelve direction as the strongest restricted landmark;
- Relay Workbench as a nearby/local annex;
- Quiet Stair as an egress route with distinct signage/geometry;
- return toward Depot Plaza once the connector is implemented.

### From Gate Twelve
The player should be able to distinguish:
- return/up toward Platform Nine;
- deeper path toward Service Tunnel;
- lateral technical path toward Trace Chamber.

### From Service Tunnel
The player should understand:
- route back toward Gate Twelve;
- cross-link toward Trace Chamber;
- deeper continuation exists architecturally but is not currently available.

### From Trace Chamber
The player should understand:
- it is a spur/cross-link location, not a dead isolated room;
- one route returns toward Gate Twelve;
- another route leads into Service Tunnel.

## 3.7 Route readability and visual weight

The map should not render every connection with equal emphasis.

Target visual hierarchy:
- district spine: strongest neutral route/readability;
- hub branches: medium;
- lower cross-link: lighter/subordinate;
- unavailable/future stubs: environmental implication only, no false active route line.

Reachable/current/selected state remains a separate overlay system and may temporarily override neutral visual emphasis.

Permanent background art must not bake in "available now" semantics.

## 3.8 Pacing without invented meter scale

Because real-world dimensions are not yet locked, Step 3 uses **interaction pacing** rather than meters.

### Short-beat branch
Examples:
- Platform Nine <-> Relay Workbench;
- Plaza <-> immediate civic branch.

Desired feeling:
- local detour;
- one functional destination away from hub;
- minimal transition ceremony.

### Medium-beat transition
Examples:
- Plaza <-> Platform Nine;
- Platform Nine <-> Gate Twelve;
- Gate Twelve <-> Trace Chamber.

Desired feeling:
- clear change of spatial identity;
- enough transition to communicate entering a different functional zone;
- not so long that frequent reuse becomes tedious.

### Deep-beat transition
Example:
- Gate Twelve <-> Service Tunnel;
- future Service Tunnel -> deeper infrastructure.

Desired feeling:
- stronger enclosure/depth shift;
- more environmental transition;
- should communicate that the player is leaving ordinary district space.

Exact travel time values remain engine/content decisions for later migration.

## 3.9 Backtracking policy

Repeated-use comfort is a priority.

Rules:
- do not force civic errands through the restricted infrastructure;
- do not force every lower-network return through the exact same sequence when an existing cross-link can avoid it;
- preserve the Service Tunnel <-> Trace Chamber cross-link;
- keep Relay Workbench close to Platform Nine conceptually;
- do not create decorative dead ends unless the destination itself justifies the stop;
- future world exits should attach to natural boundaries, not arbitrary side rooms.

## 3.10 Choice and discovery policy

Circulation can suggest possibilities without exposing hidden content.

Allowed:
- visible architecture suggesting a stair continues;
- a tunnel visually extending deeper;
- a depot entrance reading as important;
- an unavailable route marker driven by player-safe state.

Not allowed:
- showing a secret destination name before discovery;
- painting quest-specific availability into base art;
- inventing route access in Compose;
- using environmental art to reveal hidden future-state outcomes.

## 3.11 Phone-map implications

At phone width, route comprehension must survive reduction.

Required future map behavior:
- Tier 1 anchors remain identifiable: Depot Plaza, Platform Nine, Gate Twelve;
- selected/current/reachable overlays remain readable above the map;
- route crossings do not collapse into an indistinguishable line cluster;
- labels/details may be progressive rather than all visible simultaneously;
- the visual spine should remain understandable even if secondary labels are hidden;
- touch targets may be larger than the visible marker, but must still map to authoritative nodes.

No zoom system is locked yet; that belongs to the application UX step.

## 3.12 Circulation risks identified

### Risk A — connector overload
If Depot Plaza <-> Platform Nine becomes too visually dominant, the surface branches may feel secondary or decorative.

Mitigation:
- keep Workshop Row and Archive as clear civic destinations;
- use landmark identity, not only route thickness, to establish importance.

### Risk B — Gate Twelve bottleneck
Gate Twelve naturally concentrates restricted routes.

Mitigation:
- retain Service Tunnel <-> Trace Chamber cross-link;
- avoid adding unrelated functions to Gate Twelve;
- use clear directional differentiation.

### Risk C — Quiet Stair feels pointless
Because its external destination is not yet mapped, it may read as a dead end.

Mitigation:
- preserve strong egress identity;
- give it legitimate local story/scene value;
- leave expansion architecture visible without inventing a destination.

### Risk D — map/scene mismatch
A route may look physically plausible in the map art while the engine does not authorize it.

Mitigation:
- route overlays are always derived from authoritative graph state;
- proposed paths are never rendered as normal active routes until content migration occurs.

### Risk E — repeated travel fatigue
High-use areas may become tedious if every interaction requires full traversal ceremony.

Mitigation:
- distinguish local, medium, and deep transition beats;
- avoid over-animating local branch travel;
- preserve direct hub logic.

## 3.13 Step 3 locked decisions

1. The district spine is `Depot Plaza -> Platform Nine -> Gate Twelve -> Service Tunnel`, with future world continuation at both ends.
2. `DISTRICT_PLAZA <-> PLATFORM_NINE` is approved as a required future authored connector for the target map, but is not implemented yet.
3. Depot Plaza is the public/free-roam orientation hub.
4. Platform Nine is the internal depot hub.
5. Gate Twelve is a threshold hub, not a general-purpose social hub.
6. Workshop Row and Municipal Archive remain direct civic branches from Depot Plaza.
7. Relay Workbench and Quiet Stair remain direct branches from Platform Nine.
8. Trace Chamber is accessible from Gate Twelve and Service Tunnel in the target circulation model, matching current edges.
9. Service Tunnel <-> Trace Chamber must be preserved as the lower-network cross-link.
10. Quiet Stair and Service Tunnel represent different outward/deeper circulation roles.
11. Route classes are: district spine, hub branches, lower cross-link, future expansion stubs.
12. Travel pacing is classified as local / medium / deep until physical scale and exact travel costs are designed later.
13. Permanent art never owns reachability or quest access.
14. Phone presentation must preserve the spine and Tier 1 anchors even when secondary detail is reduced.

---

# 4. Planned authoring sequence

The remaining master plan will be completed in this order:

1. **Authority and design mandate** — COMPLETE.
2. **Spatial hierarchy** — COMPLETE.
3. **Circulation** — COMPLETE.
4. **Per-zone function** — what each named location contributes to play.
5. **Geometry contract** — footprints, boundaries, anchors, reusable modules.
6. **Material and visual language** — surfaces, architecture families, lighting.
7. **Asset decomposition** — what must be built one asset at a time.
8. **Application UX plan** — Map/Story/location navigation and high-use flows.
9. **State-layer plan** — discovery, reachability, events, blackout, Trace effects.
10. **Performance/section strategy** — loading boundaries and mobile constraints.
11. **Implementation order** — smallest safe slices and dependency graph.
12. **Verification plan** — unit, emulator, screenshot, handset, regression.
13. **Migration plan** — what old presentation code/assets are kept, replaced, or retired.
14. **Execution handoff** — exact first implementation task and acceptance criteria.

---

# Continuity footnote / next-session handoff

**Completed:** Step 1 — authority and design mandate; Step 2 — spatial hierarchy; Step 3 — circulation and player flow.

**Key decisions preserved for future sessions:**
- active repository is `jbob-coder/Text-rpg-game`;
- Gate Twelve District is a small but high-use region inside a larger world;
- existing stable IDs, authored world-map graph, discovery/travel rules, and quest/state ownership remain authoritative until explicitly migrated;
- existing 256x144 Gate Twelve presentation geometry is the current visual scaffold;
- external material is inspiration only and may contain contradictory counts, dimensions, colors, and details;
- do not choose “5 sections” or “12 areas” merely because the references contain those numbers;
- design may improve or replace application presentation, including breaking old presentation behavior, when the replacement is documented and materially better;
- UI must not become the source of truth for gameplay state;
- final map must be constructed as modular game content, piece by piece, not generated as one flattened image.

**Next unfinished step:** Step 4 — define per-zone function: what each of the nine named locations contributes to gameplay, narrative, repeated use, player services/interactions, and why the player has a reason to return.

**Do not skip directly to asset production before Steps 4–5 are documented.**

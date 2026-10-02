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


# 4. Per-zone gameplay function and return value

Status: **COMPLETE — ZONE FUNCTION MODEL LOCKED FOR LATER IMPLEMENTATION**

This step defines why each named location exists in play, what it already does in current authored content, what its target long-term role should be, and why a player would return.

The purpose is to prevent two common map-design failures:

1. locations that look distinct but all perform the same gameplay function;
2. locations that are visited once and then become permanent dead scenery.

This step does **not** add new systems. Every proposed service or repeatable loop below is clearly marked as future design rather than current functionality.

## 4.1 Functional classification

Each named location receives one primary function class and may receive secondary roles.

### Function classes

- **ANCHOR HUB** — teaches orientation and connects multiple meaningful routes.
- **TRANSIT / THRESHOLD** — controls movement between functional layers of the district.
- **SPECIALIST INTERACTION** — supports a focused task such as diagnostics, research, or training.
- **INFORMATION / SOCIAL** — provides knowledge, rumors, public context, or character interaction.
- **REPEATABLE PROGRESSION** — contains a loop the player has mechanical reason to revisit.
- **EGRESS / EXPANSION** — points toward future world space or provides an alternate route.

Not every location should become a full hub. Specialized places retain value precisely because their function is narrower.

## 4.2 Return-value tiers

To guide later content production, locations use four return-value tiers.

### Tier R1 — naturally repeatable now
Current authored content already gives the player a repeatable mechanical reason to return.

### Tier R2 — conditional return now
Current authored state, knowledge, quests, or branching can justify multiple visits, but the location is not an unlimited repeatable service.

### Tier R3 — target repeatable later
Current content is mostly one-shot, but the location is intentionally positioned to gain a bounded repeatable function later.

### Tier R4 — specialized / low-frequency
The location should remain occasional or situational. It does not need artificial busywork merely to increase visit count.

The goal is a healthy district rhythm, not equal visit frequency.

---

## 4.3 Depot Plaza — `DISTRICT_PLAZA`

### Current confirmed function

Current authored content establishes Depot Plaza as:
- the open space outside the tram depot;
- the district's temporary meeting point;
- the point where free-roam district exploration is presented;
- the location of `DISTRICT_HUB`;
- a place to review temporary district notices;
- a place from which the player may resume the Gate Twelve investigation.

Current effect types include:
- world/state flags;
- quest start.

### Target primary role

**ANCHOR HUB + INFORMATION / SOCIAL + WORLD TRANSITION**

Depot Plaza is the public-facing center of Gate Twelve District.

It should become the place where the player mentally resets after leaving specialized locations.

### Target player uses

Preserve:
- orientation;
- district notices/public context;
- branching toward Workshop Row and Municipal Archive;
- return path toward the depot/Gate Twelve investigation.

Future proposals:
- public-state updates that change as the district changes;
- player-safe summaries of newly available civic destinations;
- NPC presence tied to authored NPC state;
- transition point to the future larger surface-world map.

Do **not** automatically turn Depot Plaza into:
- a universal inventory screen;
- a generic shop;
- a crafting station;
- a quest-board that duplicates every other location.

Those systems require separate justification.

### Return value

**Tier R2 now -> target R1/R2 hybrid later**

Current reason to return:
- free-roam orientation;
- notices;
- resume deeper investigation.

Future reason to return:
- district-state changes and world transitions.

### Design success condition

When the player thinks "I am back in the district," Depot Plaza should be the strongest spatial answer.

---

## 4.4 Workshop Row — `WORKSHOP_ROW`

### Current confirmed function

Current authored content establishes Workshop Row as:
- repair shops and municipal contractors west of the depot;
- a place where crews sort broken readers, relays, and field tools;
- the source of a Gate Twelve workshop rumor;
- a contributor to later Archive cross-checking.

Current effect types include:
- world flag changes.

### Target primary role

**SPECIALIST INTERACTION + INFORMATION / SOCIAL**

Workshop Row should represent practical district labor, repair culture, and grounded technical knowledge.

It should not become a second Relay Workbench.

### Target player uses

Preserve:
- worker rumors;
- municipal repair identity;
- practical contrast with the Archive's formal records.

Future proposals:
- bounded equipment/service interactions **only if** the equipment system later supports repair, modification, appraisal, or maintenance;
- contractor-specific information or jobs tied to authored content;
- state-dependent workshop conversations;
- practical material/parts economy if an economy system is formally introduced.

Do not invent:
- crafting trees;
- repair durability;
- vendors;
- currencies;
- weapon upgrading.

Those are not current systems.

### Return value

**Tier R2 now -> target R3 later**

The current rumor is mostly one-time. The location is structurally well suited to later practical services, but those services must come from future systems rather than visual implication.

### Design success condition

Workshop Row should feel useful because skilled people work there, not because every building contains a generic shop menu.

---

## 4.5 Municipal Archive — `DISTRICT_ARCHIVE`

### Current confirmed function

Current authored content establishes the Archive as:
- a public records annex on backup power;
- a source of Platform Nine emergency-routing knowledge;
- a place to cross-check the Workshop Row rumor against maintenance bulletins;
- a source of formal knowledge rather than supernatural revelation.

Current effect types include:
- quest start;
- knowledge acquisition;
- quest-objective completion.

### Target primary role

**INFORMATION / SOCIAL + SPECIALIST RESEARCH**

The Archive is the district's formal knowledge-validation location.

### Target player uses

Preserve:
- research;
- records;
- cross-checking informal information;
- lore quests;
- infrastructure history.

Future proposals:
- additional records becoming relevant only when the player has the appropriate knowledge, quest, or public event state;
- structured cross-reference interactions;
- historical map/document access that reveals only player-safe knowledge;
- research hooks for future district/world mysteries.

Do not make the Archive:
- a generic encyclopedia containing all lore from the start;
- an automatic spoiler repository;
- a replacement for exploration.

### Return value

**Tier R2 now -> strong target R2 later**

The Archive should become more valuable as the player's knowledge graph expands. Its replay value should be **conditional**, not an unlimited farming loop.

### Design success condition

The player returns because new questions make old records newly meaningful.

---

## 4.6 Platform Nine — `PLATFORM_NINE`

### Current confirmed function

Current authored content establishes Platform Nine as:
- the evacuation platform inside the municipal tram depot;
- the opening location;
- the site of the relay handoff;
- the place where Tamsin is introduced;
- a major early relationship/party decision point;
- the hub connecting Relay Workbench, Gate Twelve, and Quiet Stair in the existing graph.

Current effect types include:
- quest start/progression;
- inventory gain;
- knowledge gain;
- NPC story transitions;
- party changes;
- relationship changes;
- NPC goals.

### Target primary role

**ANCHOR HUB + NARRATIVE / SOCIAL TRANSIT**

Platform Nine is the internal depot hub and the emotional/narrative counterpart to Depot Plaza.

Depot Plaza says "public district."
Platform Nine says "people, evacuation, depot operations, and the route below."

### Target player uses

Preserve:
- major story decisions;
- Tamsin/party consequences when authored;
- orientation between Workbench, Gate Twelve, Quiet Stair, and future Plaza connector.

Future proposals:
- depot-state updates tied to evacuation/public recovery;
- recurring NPC presence only when NPC state supports it;
- transit/depot context for later district events.

Do not make Platform Nine:
- a universal social hub for every NPC;
- a duplicate public plaza;
- a generic fast-travel screen unless a travel system later justifies it.

### Return value

**Tier R2 now -> target R2 later**

Its value comes from changing narrative and district state rather than from a repeatable mechanical service.

### Design success condition

Returning to Platform Nine should make the player feel the consequences of what is happening in the district and with the people tied to the depot.

---

## 4.7 Relay Workbench — `RELAY_WORKBENCH`

### Current confirmed function

Current authored content establishes the Workbench as:
- a maintenance bench;
- the place where the dead relay is examined;
- a place to use the maintenance seal or risk forcing the casing;
- a recovery/diagnostic interaction point involving Tamsin.

Current effect types include:
- inventory change;
- knowledge gain;
- quest success/failure;
- relationship/NPC state changes;
- flags.

### Target primary role

**SPECIALIST INTERACTION — DIAGNOSTICS**

Relay Workbench should remain a small, focused technical station attached to Platform Nine.

Its identity is precision diagnostics, not broad crafting.

### Target player uses

Preserve:
- item/device examination when authored;
- technical checks;
- story-relevant diagnostics;
- collaboration with technically capable NPCs when state supports it.

Future proposals:
- inspect or diagnose specific technical objects;
- compare signal/device evidence;
- bounded maintenance actions tied to actual item/system rules.

Do not automatically add:
- item crafting;
- equipment upgrading;
- universal repair;
- inventory storage;
- skill respec.

### Return value

**Tier R4 now -> target R3 later**

Current use is strongly opening-specific. A future diagnostic system could justify returns, but the Workbench should stay specialized and local.

### Design success condition

The Workbench is memorable because it is where technical uncertainty gets converted into actionable information.

---

## 4.8 Service Gate Twelve — `GATE_TWELVE`

### Current confirmed function

Current authored content establishes Gate Twelve as:
- a sealed maintenance entrance below the depot;
- the end/threshold of the opening;
- a point where the player may continue below or return to the district;
- the place where Trace Echo is discovered;
- a place for first live technique use and recovery from Trace strain;
- a major quest threshold.

Current effect types include:
- quest start/progression;
- ability discovery;
- technique discovery/use;
- knowledge gain;
- power recovery;
- free-roam/state flags.

### Target primary role

**TRANSIT / THRESHOLD + INVESTIGATION LANDMARK**

Gate Twelve is the district's strongest threshold.

It should feel consequential each time the player crosses it.

### Target player uses

Preserve:
- entering/leaving restricted infrastructure;
- Trace-related investigation;
- stateful threshold scenes;
- route choice between district and lower network.

Future proposals:
- gated investigation entry points when deeper content exists;
- state-dependent environmental responses to known Trace phenomena;
- expedition confirmation only if deeper-route gameplay later requires it.

Do not turn Gate Twelve into:
- a social hub;
- a training center;
- a shop;
- a permanent UI menu for every underground activity.

### Return value

**Tier R2 now -> target R2 later**

The return reason is progression and changing investigation state. Gate Twelve is a meaningful passage, not a grind location.

### Design success condition

Crossing Gate Twelve should always mean the player is changing the kind of space and activity they are entering.

---

## 4.9 Quiet Stair — `EVAC_STAIR`

### Current confirmed function

Current authored content establishes Quiet Stair as:
- a maintenance stair away from the main evacuation flow;
- the solo opening route when the player leaves Tamsin behind;
- an alternate branch from Platform Nine.

Current effect types include:
- route-state flag;
- quest-objective completion.

### Target primary role

**EGRESS / EXPANSION + ALTERNATE NARRATIVE ROUTE**

Quiet Stair should remain quieter and lower-frequency than the major hubs.

Its value is that it represents a different way out of the depot system.

### Target player uses

Preserve:
- alternate route identity;
- solo/egress narrative meaning;
- separation from Gate Twelve's restricted-investigation route.

Future proposals:
- connection to a future evacuation/service region;
- event-specific alternate ingress/egress;
- low-traffic narrative encounters where appropriate.

Do not add arbitrary services merely to increase visit frequency.

### Return value

**Tier R4**

Quiet Stair is allowed to remain situational until the world beyond it is authored.

### Design success condition

The player understands why Quiet Stair exists even if they do not visit it constantly.

---

## 4.10 Service Tunnel — `SERVICE_TUNNEL`

### Current confirmed function

Current authored content establishes Service Tunnel as:
- restricted infrastructure beneath the evacuation route;
- the first area entered below Gate Twelve with Tamsin;
- a place associated with fresh evidence/boot prints;
- a place used during the Directional Trace aftermath and recovery;
- a route connected to both Gate Twelve and Trace Chamber.

Current effect types include:
- route/state flags;
- quest progression;
- NPC story/goal progression;
- power recovery.

### Target primary role

**TRANSIT / THRESHOLD + INVESTIGATION + DEEP EXPANSION**

Service Tunnel is the connective exploration layer below Gate Twelve.

It is not simply a hallway between scenes.

### Target player uses

Preserve:
- lower-network traversal;
- environmental investigation;
- connection to Trace Chamber;
- evidence that points deeper.

Future proposals:
- state-dependent investigation beats;
- changing environmental clues tied to authored events;
- deeper-route access when future infrastructure is implemented.

Do not turn the tunnel into:
- a random encounter corridor without a designed combat system;
- a generic loot-farming tunnel;
- a procedural dungeon by default.

### Return value

**Tier R2 now -> target R2/R3 later**

Return value should come from new evidence, route changes, and deeper-world expansion, not repetitive filler.

### Design success condition

The tunnel should make the district feel larger than the current mapped boundary.

---

## 4.11 Trace Chamber — `TRACE_CHAMBER`

### Current confirmed function

Trace Chamber already has the strongest repeatable mechanical loop in the district.

Current authored content includes:
- first Trace Echo practice;
- structured training-plan activation;
- repeatable Signal Pulse practice;
- general Powers skill training;
- resource recovery;
- stable-pattern analysis;
- Trace Tolerance perk acquisition;
- Directional Trace discovery;
- controlled first use;
- return-to-district completion.

Current effect types include:
- technique practice/use/discovery;
- skill training;
- resource recovery;
- knowledge gain;
- quest progression;
- perk acquisition;
- state flags.

### Target primary role

**REPEATABLE PROGRESSION + SPECIALIST RESEARCH**

Trace Chamber is the district's dedicated controlled training/research location.

It should not be generalized into a universal character-training room.

### Target player uses

Preserve:
- Trace Echo progression;
- controlled training;
- measurement;
- recovery associated with that training loop;
- research derived from already-acquired evidence.

Future proposals:
- additional Trace-specific exercises only when the ability system formally expands;
- new controlled tests tied to discovered techniques;
- comparative analysis of future Trace evidence.

Do not automatically allow:
- training every skill;
- arbitrary stat grinding;
- unrelated perk acquisition;
- unrestricted healing unrelated to the authored recovery system.

### Return value

**Tier R1 now**

Trace Chamber is already a legitimate repeat destination.

### Design success condition

This is where repeated practice becomes measurable progression, not where the player goes for every form of advancement.

---

## 4.12 District functional balance

The nine zones should form a complementary system:

| Location | Primary function | Return tier |
| --- | --- | --- |
| Depot Plaza | public orientation / district hub | R2 -> R1/R2 |
| Workshop Row | practical workers / specialist future services | R2 -> R3 |
| Municipal Archive | research / knowledge validation | R2 |
| Platform Nine | internal depot / narrative-social hub | R2 |
| Relay Workbench | focused diagnostics | R4 -> R3 |
| Gate Twelve | threshold / investigation gateway | R2 |
| Quiet Stair | alternate egress / expansion | R4 |
| Service Tunnel | lower traversal / investigation / expansion | R2 -> R3 |
| Trace Chamber | repeatable Trace progression / research | R1 |

This distribution is intentional.

The district does **not** need nine equally busy locations.

Instead:
- hubs handle orientation and changing world context;
- specialist locations handle focused interactions;
- threshold locations control spatial/narrative transitions;
- one current location, Trace Chamber, owns the strongest repeatable progression loop;
- future systems may add bounded return value where structurally appropriate.

## 4.13 Anti-duplication rules

Future content must avoid functional duplication.

### Depot Plaza vs Platform Nine
- Plaza = public district orientation.
- Platform Nine = internal depot/narrative context.

### Workshop Row vs Relay Workbench
- Workshop Row = people/contractors/practical district services.
- Relay Workbench = precise technical diagnostics.

### Archive vs Trace Chamber
- Archive = formal historical/public records.
- Trace Chamber = experimental/personal Trace research and training.

### Gate Twelve vs Service Tunnel
- Gate Twelve = controlled threshold.
- Service Tunnel = connective restricted infrastructure beyond the threshold.

### Quiet Stair vs Service Tunnel
- Quiet Stair = egress/alternate outward route.
- Service Tunnel = deeper restricted continuation.

## 4.14 Application implications

Later UI/application work should respect functional identity.

Examples:
- Map detail text should communicate why a place matters, not only its name.
- A location's repeatable actions should live with that location rather than being flattened into a universal "Activities" screen without need.
- The app may surface available actions from authoritative scene state, but must not synthesize services from this design document.
- High-return locations may justify richer quick-access presentation later.
- Low-frequency locations should not be visually removed merely because they have fewer actions.
- New badges/markers such as "training available" or "new records" require player-safe engine state before UI implementation.

## 4.15 Content-gap register created by Step 4

The following are **design opportunities**, not implemented features:

- Depot Plaza needs stronger long-term changing district context if it is to remain the public hub.
- Workshop Row has structural room for future practical services, but no repair/crafting economy is currently authored.
- Platform Nine can carry changing depot/NPC state, but no generic social-hub system is currently authored.
- Relay Workbench needs a reusable diagnostics contract before it can support repeat visits.
- Quiet Stair intentionally has low current repeat value until its external destination or additional events exist.
- Service Tunnel can support evolving investigation/deeper access, but no procedural content should be invented.
- Municipal Archive can expand naturally through conditional records as the knowledge system grows.
- Trace Chamber already provides the benchmark for what a legitimate repeatable location loop looks like.

These gaps should feed later content/system planning; they are not excuses to fake UI buttons.

## 4.16 Step 4 locked decisions

1. Every named location has a distinct primary gameplay function.
2. Equal visit frequency is not a goal.
3. Trace Chamber remains the strongest current repeatable-progression location.
4. Depot Plaza remains the public orientation hub.
5. Platform Nine remains the internal narrative/depot hub.
6. Workshop Row and Relay Workbench must not collapse into the same crafting/technical function.
7. Municipal Archive owns formal knowledge validation and conditional research.
8. Gate Twelve owns threshold/investigation transition, not social or training functions.
9. Quiet Stair is allowed to remain low-frequency and expansion-facing.
10. Service Tunnel owns lower traversal/investigation/deep-world continuation.
11. Proposed future services must remain explicitly non-implemented until supported by engine/content systems.
12. UI must expose authored actions, not create services because the map plan suggests them.

---

# 5. Planned authoring sequence

The remaining master plan will be completed in this order:

1. **Authority and design mandate** — COMPLETE.
2. **Spatial hierarchy** — COMPLETE.
3. **Circulation** — COMPLETE.
4. **Per-zone function** — COMPLETE.
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

**Completed:** Step 1 — authority and design mandate; Step 2 — spatial hierarchy; Step 3 — circulation and player flow; Step 4 — per-zone gameplay function and return value.

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

**Next unfinished step:** Step 5 — define the geometry contract: exact presentation footprints/bounds, transition anchors, reserved expansion edges, reusable building/surface modules, and what geometry may or may not change before asset production.

**Do not begin asset production before Step 5 is complete.**

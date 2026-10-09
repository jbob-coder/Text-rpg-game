# Gate Twelve Region — Master Map & Application Plan

Status: **ACTIVE / STEPWISE AUTHORING**  
Repository: `jbob-coder/Text-rpg-game`  
Working branch: `docs/settlement-region-build-plan`  
Started: 2026-10-01  
Purpose: define, build, integrate, and verify the Gate Twelve region as a high-use playable area inside the larger game.
Parent program: `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`
Pixel composition companion: `docs/assets/PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md`

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

## Current implementation overlay — 2026-10-08

This master preserves the original Steps 1–14 planning sequence below. Several implementation prerequisites named there have since been completed and must not be re-opened merely because older step text still describes them as future work.

Current repository truth:
- **D-064 room-actor presence projection is implemented and verified.** Python owns the player-safe room projection; Android consumes typed room actors and semantic placements; scene/location IDs no longer invent story-actor presence. Contextual focus panels, broader actor/pose/outfit coverage and some held-prop/presentation work remain separate.
- **D-065 recurring Tamsin durable-memory proof is DONE.**
- **D-067 bounded Gate Twelve inventory/equipment proof is DONE**, including invalid-equip rollback.
- **D-068 bounded Trace Chamber activity proof is DONE.**
- **D-069, D-070 and D-071 tactical runtime foundations are DONE** through the deterministic grid/schema core, transient turn/action engine and knowledge-safe objective/retreat/AI layer.
- **D-072 durable tactical aftermath is currently IN_PROGRESS under Silex.**
- **D-073 Gate Twelve tactical content/Python bridge remains BLOCKED until D-072 is DONE**; D-074 Android tactical presentation follows D-073.
- Live task ownership/readiness comes from `docs/AI_TASK_BULLETIN_BOARD.md`; semantic task state comes from `docs/THE_GAME_MASTER_TASK_REGISTER.md`.

Therefore, older statements such as “preferred first code-bearing slice: player-safe room-actor projection,” “hard-coded actor placement once safe projection exists,” or actor presence described as merely transitional are **historical planning context**. Preserve their design rationale, but use the current D-064/D-067/D-068/D-069–D-072 evidence chain when deciding what is actually unfinished.

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



# 5. Geometry contract

Status: **COMPLETE — PRESENTATION GEOMETRY / ANCHOR CONTRACT LOCKED FOR ASSET PRODUCTION**

This step converts the existing 256x144 Gate Twelve map master from an informal scaffold into an explicit production contract.

Source of confirmed geometry:
- `android/app/src/main/java/com/thegame/rpg/ui/PixelMapArtCatalog.kt`
- `MAP_GATE_TWELVE_DISTRICT_BASE`
- current authored world-map node percentages in `content/vertical_slice_01.json`

This contract distinguishes:
- **map presentation geometry**;
- **world-map node anchors**;
- **physical transition meaning**;
- **reusable art modules**;
- **reserved expansion space**.

It does not change gameplay state or routes.

## 5.1 Native district canvas

Current map master:
- width: **256 px**
- height: **144 px**
- origin: top-left `(0,0)`
- x increases rightward;
- y increases downward.

This is a presentation coordinate system.

It is not:
- a meter scale;
- a tactical-combat grid;
- a world geographic coordinate system;
- a substitute for travel-time data.

## 5.2 Locked macrozone bands

The current map base explicitly divides the canvas into:

| Macro presentation band | Y range | Height | Planning role |
| --- | ---: | ---: | --- |
| Surface Civic | 0..47 | 48 px | Workshop Row, Depot Plaza, Archive |
| Depot / Service | 48..94 | 47 px | Platform Nine, Workbench, Gate Twelve, upper Trace/service geometry |
| Lower Maintenance | 95..143 | 49 px | Quiet Stair and deeper maintenance field |

These band boundaries are now **production-stable**.

They may be visually softened through materials, transitions and overlays, but asset production must not casually move whole locations across bands.

Changing a band boundary requires:
- explicit geometry-change proposal;
- map-art update;
- affected location review;
- route/anchor review;
- phone-scale QA.

## 5.3 Confirmed perimeter infrastructure

Upper perimeter street:
- base road envelope: `y=5..11`
- lighter road treatment inside that envelope: around `y=7..8`

Lower perimeter street:
- base road envelope: `y=126..133`
- lighter road treatment: around `y=128..129`

These are environmental infrastructure.

They do not automatically represent player-travel edges.

Production rule:
- keep both streets visually continuous;
- use modular asphalt/road, edge/curb and service-seam assets;
- do not paint reachability or quest availability into them.

## 5.4 Confirmed location footprint envelopes

The following outer envelopes are taken directly from current map-art construction.

| Location | Confirmed presentation envelope | Notes |
| --- | --- | --- |
| Workshop Row | `x=49..102, y=8..29` | four attached practical bays; front service strip extends around `x=48..103, y=28..30` |
| Depot Plaza | paving `x=105..143, y=8..39`; frontage `x=108..140, y=31..43` | public hub; open-space identity must be preserved |
| Municipal Archive | `x=151..196, y=6..33` | institutional building/courtyard zone |
| Platform Nine | `x=20..83, y=37..72` | depot mass; track envelope extends beyond building |
| Platform Nine tracks | approx. `x=18..85, y=68..78` | permanent infrastructure, not state overlay |
| Relay Workbench | `x=75..105, y=31..58` | annex overlaps the depot/public transition area visually |
| Gate Twelve | `x=119..154, y=56..85` | threshold landmark |
| Quiet Stair | `x=88..118, y=89..123` | lower egress/shaft |
| Service Tunnel | `x=161..199, y=78..108` | lower restricted infrastructure |
| Trace Chamber | `x=194..237, y=40..71` | functionally Depot/Gate Core despite crossing presentation-band logic |

### Footprint rule

These envelopes are now **asset-fit targets**.

A new facade, tile family, landmark or map module should fit the envelope rather than moving the location merely to accommodate artwork.

Allowed inside an envelope without geometry migration:
- window placement;
- door ornament;
- surface texture;
- awning;
- small equipment;
- signage;
- vegetation;
- local wear;
- small decorative projections that do not alter route readability.

Not allowed without explicit geometry revision:
- moving a whole named location;
- swapping Workshop Row and Archive sides;
- changing the depot/gate/maintenance ordering;
- closing a required visual path with permanent architecture;
- consuming an expansion boundary with an irreversible landmark;
- moving map-node semantic anchors because art looks better elsewhere.

## 5.5 Node render anchors

The authored world-map uses percentage coordinates.

On the 256x144 map master those project approximately to:

| Stable location | Authored % | Presentation anchor |
| --- | --- | --- |
| `WORKSHOP_ROW` | (29,16) | (~74,23) |
| `DISTRICT_PLAZA` | (48,18) | (~123,26) |
| `DISTRICT_ARCHIVE` | (66,16) | (~169,23) |
| `PLATFORM_NINE` | (18,36) | (~46,52) |
| `RELAY_WORKBENCH` | (34,31) | (~87,45) |
| `GATE_TWELVE` | (53,48) | (~136,69) |
| `EVAC_STAIR` | (40,70) | (~102,101) |
| `SERVICE_TUNNEL` | (70,61) | (~179,88) |
| `TRACE_CHAMBER` | (82,39) | (~210,56) |

These are **semantic marker anchors**, not necessarily doorway coordinates.

Map marker/touch behavior must continue to derive from the projected world map.

Do not move a marker to a decorative door merely because that looks visually convenient unless the underlying node coordinate is deliberately migrated.

## 5.6 Current route geometry

Current map art mirrors the authored graph with these service-route presentation segments:

- `(46,52) -> (87,45)` — Platform Nine to Relay Workbench;
- `(46,52) -> (136,69)` — Platform Nine to Gate Twelve;
- `(46,52) -> (102,101)` — Platform Nine to Quiet Stair;
- `(136,69) -> (179,88)` — Gate Twelve to Service Tunnel;
- `(136,69) -> (210,56)` — Gate Twelve to Trace Chamber;
- `(179,88) -> (210,56)` — Service Tunnel to Trace Chamber.

Surface boulevard presentation:
- `(70,23) -> (123,26)`;
- `(123,26) -> (169,23)`.

The visual route system does not own route legality.

When route art is rebuilt:
1. render neutral physical path/material;
2. render graph edge if the UI uses an explicit route overlay;
3. render discovered/current/reachable/unavailable markers separately;
4. keep selected/travel preview separate.

## 5.7 Depot Plaza -> Platform Nine target connector

Step 3 established:

`DISTRICT_PLAZA <-> PLATFORM_NINE`

as required for the target circulation model.

Geometry decision:
- **do not create a new named location solely to bridge them**;
- treat the transition as public exterior/plaza -> depot entrance -> Platform Nine interior;
- preserve the existing Depot Plaza frontage and Platform Nine depot mass;
- a later authored route edge may connect the two semantic nodes;
- scene art should communicate the entrance/threshold;
- district-map art does not need a literal wide road cutting through the intervening annex geometry.

This avoids distorting the existing map merely to make the connection visually obvious.

Implementation remains deferred:
- no gameplay edge added in this documentation step;
- no travel time chosen;
- no unlock state chosen.

## 5.8 Transition-anchor classes

Each transition receives one of four anchor classes.

### T1 — semantic node anchor
Used by:
- map marker;
- selection;
- hit testing.

### T2 — physical scene entrance
Used by:
- doorway;
- stair;
- corridor mouth;
- gate.

### T3 — map-to-world expansion boundary
Used by:
- larger-world transition;
- future adjacent region.

### T4 — state transition overlay anchor
Used by:
- Echo response;
- blackout;
- powered/unpowered treatment;
- temporary event art.

Do not overload one coordinate to serve all four jobs.

## 5.9 Reserved expansion boundaries

### Depot Plaza surface-world boundary

Status:
- world-facing attachment remains required;
- exact parent-city direction is **not yet decided**.

Geometry rule:
- preserve an outer-facing visual route from the plaza;
- do not surround the plaza with permanent art that makes future surface-world attachment implausible;
- exact edge/coordinate will be selected only after the parent city layout exists.

### Quiet Stair external boundary

Status:
- egress-facing;
- destination not authored.

Geometry rule:
- preserve the shaft/stair sense of continuation;
- keep lower/outward connection visually plausible;
- do not label a destination yet.

### Service Tunnel deep boundary

Status:
- deeper-infrastructure expansion stub;
- Directional Trace supports “deeper below mapped service level.”

Geometry rule:
- preserve a visual continuation/depth cue;
- do not hard-close every corridor end in base art;
- exact deeper map coordinate waits for the next region.

## 5.10 Reusable surface modules

Required surface families:

### Civic surface family
- civic slab;
- curb;
- asphalt;
- utility seam;
- drainage;
- restrained lane/municipal marking;
- civic wear decal.

Primary consumers:
- Depot Plaza;
- Archive frontage;
- Workshop Row approaches;
- perimeter streets.

### Depot/service family
- depot concrete;
- platform edge;
- rail steel;
- sleeper/track support;
- painted utility metal;
- service channel;
- depot wall panel.

Primary consumers:
- Platform Nine;
- Workbench annex;
- Gate Twelve approaches.

### Lower maintenance family
- dark municipal concrete;
- maintenance floor panel;
- wall support;
- vent;
- drain;
- pipe channel;
- cable tray;
- rail;
- service plate.

Primary consumers:
- Quiet Stair;
- Service Tunnel;
- Trace Chamber.

Rule:
shared materials should look related without making every location identical.

## 5.11 Reusable building modules

Recommended families:

### Municipal public
- door;
- practical window;
- civic facade panel;
- institutional trim;
- notice/sign plate.

### Workshop
- bay shell;
- shutter;
- awning;
- repair aperture;
- work apron;
- tool/scrap cluster.

### Depot
- broad frame;
- roof/support;
- platform panel;
- service door;
- track-edge module.

### Restricted service
- reinforced door frame;
- heavy panel;
- access hatch;
- support rib;
- service indicator;
- maintenance seam.

A named landmark may combine shared modules with a unique silhouette.

## 5.12 Prop anchor policy

Reusable props require:
- stable asset ID;
- origin/pivot;
- native size;
- perspective;
- intended surface;
- z-order;
- state ownership;
- allowed locations or material family.

Current stable prop families already include examples such as:
- depot door;
- relay workbench;
- Gate Twelve door;
- tunnel pipes/cables;
- Trace apparatus;
- archive shelf/terminal;
- workshop bench;
- district notice board.

Do not duplicate an existing prop under a new ID because a later scene needs a slightly different placement.

Create a variant only when:
- state differs;
- view differs;
- scale/perspective differs;
- material identity genuinely differs.

## 5.13 Scene geometry versus district-map geometry

District map:
- 256x144;
- communicates place relationships and landmark masses.

Narrative scene:
- 128x64;
- communicates one location's readable environment, actors and state.

Character gameplay:
- 32x48.

Portrait:
- 64x64.

Therefore:
- do not crop district map geometry and call it the scene master;
- do not position room actors using district-map coordinates;
- do not infer a room doorway from the map node marker;
- each layer has its own documented coordinate space.

## 5.14 Actor placement geometry

Current transitional room-actor implementation uses 32x48 actors placed inside 128x64 scene masters.

Known examples on a later actor branch:
- Platform Nine opening: wounded courier + Tamsin;
- Platform Nine decision: Tamsin;
- Relay Workbench recovery: Tamsin;
- Service Tunnel opening: Tamsin.

Target rule:
- current placements may be preserved as visual evidence;
- long-term actor presence must move to player-safe projected actor data;
- room-actor anchors should be defined per scene/location, not hard-coded as a hidden gameplay rule.

Required future scene packet field:
- actor safe zones;
- actor ground line;
- foreground occlusion zones;
- interaction focal anchor;
- portrait/panel safe zone.

## 5.15 Geometry safe zones for UI and panels

The world art must not be designed as if every pixel will remain unobstructed on phone.

Each 128x64 scene production packet should reserve:
- primary landmark zone;
- actor zone;
- interaction prop zone;
- noncritical background zone;
- text/panel-safe crop zone where possible.

The app may overlay panels, but critical character faces, door landmarks or interaction props should not consistently sit beneath permanent UI.

Specific per-scene safe-zone coordinates remain Step 7 asset-packet work rather than being invented globally here.

## 5.16 Geometry that may be improved during art production

Allowed without reopening the entire map plan:
- facade detail;
- paving pattern;
- road texture;
- material breakup;
- window spacing;
- small doorway position inside the same named footprint;
- trees/lamps;
- small props;
- drains;
- decals;
- light fixtures;
- surface wear;
- map route line styling as presentation;
- scene composition inside a location master.

## 5.17 Geometry that requires explicit migration

Requires an approved geometry-change record:
- moving a named-location footprint;
- changing relative ordering of major locations;
- changing a semantic node coordinate;
- adding/removing a gameplay route;
- changing a route's destination;
- adding a world exit;
- blocking a current route;
- changing map master resolution;
- changing map projection semantics;
- changing touch/hit-test coordinate mapping.

## 5.18 Geometry-change record template

Every intentional geometry revision must include:

1. change ID;
2. affected stable locations;
3. old bounds;
4. new bounds;
5. reason;
6. affected map nodes;
7. affected edges;
8. affected scene art;
9. affected props;
10. affected actor anchors;
11. affected UI/hit testing;
12. affected save/content IDs;
13. tests;
14. screenshot evidence;
15. rollback plan.

## 5.19 Asset-production consequence

Step 5 unlocks detailed art production planning.

After this step, asset briefs may safely assume:
- map canvas;
- bands;
- named-location footprint targets;
- semantic anchors;
- existing route geometry;
- shared surface families;
- building module families;
- separation of map/scene/actor coordinate systems.

It does **not** yet lock:
- final local palettes;
- exact material ramps;
- final lighting;
- exact actor safe-zone coordinates;
- final animation;
- final loading cells;
- final app UX.

Those belong to Steps 6–10.

## 5.20 Step 5 locked decisions

1. The current 256x144 map master is the production geometry scaffold.
2. Three macro presentation bands remain stable.
3. Current named-location footprint envelopes are asset-fit targets.
4. Authored percentage map nodes remain semantic marker anchors.
5. Route art does not own travel legality.
6. Depot Plaza -> Platform Nine should be represented as a depot entrance transition without forcing a major map-layout rewrite.
7. World-facing expansion boundaries remain reserved but unlabeled until parent geography exists.
8. Reusable surface/building/prop modules must preserve perspective, scale, material family and state ownership.
9. District-map, scene, character and portrait coordinates remain separate coordinate spaces.
10. Dynamic actors/panels may not convert hard-coded visual placement into hidden gameplay authority.
11. Small decorative geometry can improve freely inside the contract.
12. named footprints, semantic nodes, gameplay routes, exits and map projection require explicit migration when changed.

---



# 6. Material and visual language

Status: **COMPLETE — GATE TWELVE VISUAL LANGUAGE LOCKED FOR ASSET DECOMPOSITION**

This step defines what Gate Twelve should look and feel like before individual production packets are created.

Sources:
- `docs/VISUAL_BIBLE.md`;
- `docs/assets/PIXEL_ASSET_MASTER_PLAN.md`;
- `docs/assets/PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md`;
- current Gate Twelve map palette and geometry;
- owner-supplied external map/settlement references as non-authoritative structural inspiration;
- owner direction that the game should look like a cohesive pixel-art RPG and **not** default to cyberpunk/neon shorthand.

## 6.1 Core visual identity

Gate Twelve is:

**grounded municipal infrastructure under emergency pressure**

It is not:
- cyberpunk nightclub architecture;
- neon city spectacle;
- fantasy medieval settlement copied from the external reference;
- sterile sci-fi laboratory everywhere;
- abstract UI geometry pretending to be world art.

The area should communicate:
- public civic infrastructure at the surface;
- functional depot/transport engineering in the middle;
- restricted maintenance systems below;
- age, use and practical repair;
- emergency conditions through state layers;
- technological capability through believable infrastructure rather than excessive glow.

## 6.2 Pixel-art density

Final visible world art must use deliberate pixel clusters.

Rules:
- no anti-aliased shipping raster edges;
- no smooth painting run through a pixel filter;
- no tiny one-pixel noise fields used as texture;
- silhouettes first;
- material breaks second;
- accents last;
- nearest-neighbor/integer-safe scaling when source art is enlarged;
- source-native map/scene/character grids remain separate.

Map:
- 256x144 native master.

Narrative scene:
- 128x64 native master.

Gameplay character:
- 32x48.

Portrait:
- 64x64.

World art may use denser local clusters than a character sprite, but the visual language should still read as intentional pixel art at 1x and at phone scale.

## 6.3 Global light logic

Gate Twelve uses one principal visual-lighting rule:

**environmental form is readable without emissive accents.**

Emissive/status lights support form; they do not create it.

### Surface Civic
Default:
- broader ambient illumination;
- softer contrast;
- practical warm/neutral civic fixtures;
- daylight/ambient-world compatibility once the wider world is defined.

Blackout/emergency:
- darker base;
- localized emergency red/orange;
- sparse surviving warm lamps;
- no full-scene saturated red wash.

### Depot / Gate Core
Default:
- controlled industrial lighting;
- stronger hard-edged shadows;
- practical warm-white/amber indicators;
- cooler service spaces only where material/fixture logic supports it.

Emergency/Trace:
- red/orange emergency light;
- cyan/blue-green Trace response only in bounded areas;
- active effects never recolor the entire architecture.

### Lower Maintenance
Default:
- lower value;
- isolated service lights;
- visible silhouettes;
- deeper shadow pockets;
- practical guidance/maintenance illumination.

State effects:
- signal/aftershock/Trace response remains overlay-driven.

## 6.4 UI colors versus world colors

Current UI anchors include:
- Ink;
- Deep;
- Panel;
- PanelAlt;
- Paper;
- Muted;
- Cyan;
- Gold;
- Danger;
- resource colors.

Decision:
- these are **interface/feedback anchors**, not a mandatory world palette.

World art may use related ramps, but:
- Cyan is not “the color of all technology”;
- Gold is not “the color of all lights”;
- Danger is not permanently painted onto every emergency-related object;
- panels should not make the environment look like a glowing HUD.

## 6.5 Existing map palette status

The current `PixelMapArtCatalog` palette establishes a useful grounded baseline:
- dark ink/charcoal;
- service gray;
- muted concrete;
- worn road brown-gray;
- pale civic/stone values;
- muted vegetation;
- warm practical yellow;
- restrained light neutral.

Status:
- **direction accepted**;
- exact current colors may be refined;
- palette relationships matter more than preserving every hex.

Any replacement palette must preserve:
- readable value separation;
- material distinction;
- macrozone distinction;
- marker/UI readability;
- non-neon world identity.

## 6.6 Material families

### 6.6.1 Civic masonry / slab

Consumers:
- Depot Plaza;
- Archive;
- public approaches.

Visual properties:
- medium-light neutral stone/concrete;
- broad clean clusters;
- moderate wear at edges;
- occasional seams;
- low-frequency stains;
- no random speckle noise.

### 6.6.2 Workshop masonry / sheet metal

Consumers:
- Workshop Row.

Visual properties:
- warmer and dirtier than Archive;
- patched sheet metal;
- shutters;
- tool wear;
- localized rust/brown oxidation;
- open repair apertures.

It should feel worked-in, not abandoned.

### 6.6.3 Depot concrete / painted steel

Consumers:
- Platform Nine;
- Workbench annex;
- Gate approach.

Visual properties:
- heavy structural shapes;
- broad painted steel;
- dark track metal;
- service markings;
- worn platform edges;
- practical maintenance access.

### 6.6.4 Reinforced restricted infrastructure

Consumers:
- Gate Twelve;
- Service Tunnel.

Visual properties:
- darker concrete;
- heavy panel seams;
- ribs/supports;
- access plates;
- cable/pipe channels;
- restrained warning markings;
- repeated modular engineering rhythm.

### 6.6.5 Controlled technical chamber

Consumer:
- Trace Chamber.

Visual properties:
- same municipal infrastructure family as Service Tunnel;
- cleaner arrangement;
- deliberate measurement/calibration props;
- more controlled symmetry;
- bounded signal apparatus.

It must not read as an unrelated futuristic laboratory.

### 6.6.6 Rail / track steel

Consumer:
- Platform Nine.

Visual properties:
- near-black/dark steel;
- limited highlights;
- wear on contact edges;
- sleepers/crossbars visibly separate from rail.

### 6.6.7 Glass

Use sparingly.

Properties:
- dark interior value;
- one coherent reflection cluster;
- no smooth transparency gradient in ordinary pixel masters.

### 6.6.8 Cloth / character materials

Character art must remain distinct from architecture:
- softer value transitions;
- clear garment silhouettes;
- equipment layers readable against scene backgrounds.

Characters should not disappear into municipal gray.

## 6.7 Macrozone visual distinction

The three macrozones must be distinguishable even if labels are hidden.

### Surface Civic District

Dominant cues:
- lighter value range;
- more open negative space;
- trees/planters;
- public lamps;
- cleaner civic surfaces;
- readable public facade silhouettes.

Avoid:
- dense pipes everywhere;
- intense technical glow;
- dungeon-like darkness.

### Depot / Gate Core

Dominant cues:
- denser structures;
- tracks/service lines;
- steel/concrete;
- controlled access;
- stronger industrial rhythm;
- practical safety markings.

Avoid:
- making Platform Nine visually identical to Service Tunnel.

### Lower Maintenance Network

Dominant cues:
- darker values;
- narrower negative spaces;
- structural repetition;
- vents/drains/rails;
- longer depth cues;
- sparse localized light.

Avoid:
- blacking out the area so much that paths/actors are unreadable.

## 6.8 Location-specific signatures

### Depot Plaza
Signature:
- open paving;
- civic lamps/trees;
- strong depot frontage;
- clear west/east/inward directional read.

Visual priority:
negative space and orientation.

### Workshop Row
Signature:
- repeated bays;
- shutters/awnings;
- benches/tools/scrap;
- warmer repair-material accents.

Visual priority:
human work and practical activity.

### Municipal Archive
Signature:
- institutional facade;
- cleaner vertical window rhythm;
- courtyard;
- restrained backup lighting.

Visual priority:
ordered civic knowledge.

### Platform Nine
Signature:
- broad depot mass;
- tracks;
- platform safety edge;
- emergency strips during blackout;
- room actor presence during opening.

Visual priority:
evacuation pressure + transit identity.

### Relay Workbench
Signature:
- compact technical annex;
- central bench;
- diagnostic task lighting;
- relay prop as stateful focal object.

Visual priority:
precision inspection.

### Gate Twelve
Signature:
- heavy symmetric gate silhouette;
- strong center seam;
- reinforced frame;
- bounded service indicators;
- localized Echo response when active.

Visual priority:
threshold.

### Quiet Stair
Signature:
- angular stair/landing rhythm;
- rails;
- sparse guidance lights;
- empty/quiet negative space.

Visual priority:
alternate egress.

### Service Tunnel
Signature:
- depth;
- ribs;
- pipes/cables;
- access panels;
- dark corridor opening;
- restrained ambient machinery.

Visual priority:
continuation and uncertainty.

### Trace Chamber
Signature:
- municipal room shell;
- controlled apparatus;
- calibration geometry;
- bounded Trace FX.

Visual priority:
measured experimentation/training.

## 6.9 Landmark emphasis hierarchy

Tier 1:
- Depot Plaza;
- Platform Nine;
- Gate Twelve.

At phone map scale, these must remain identifiable from silhouette/value composition.

Tier 2:
- Workshop Row;
- Municipal Archive;
- Quiet Stair;
- Service Tunnel;
- Trace Chamber.

Tier 3:
- Relay Workbench.

Rule:
detail density must not make a Tier 3 feature visually dominate a Tier 1 anchor.

## 6.10 Character readability inside rooms

Room art must reserve enough contrast for:
- player sprite;
- recurring NPC;
- supporting actor.

Guidelines:
- avoid placing same-value wall mass directly behind a character's silhouette;
- use floor/ground contact shadow;
- use local contrast rather than glowing outlines;
- preserve canonical outfit colors;
- do not recolor character identity to match a room;
- state FX may overlap characters only when the gameplay state visibly affects them.

## 6.11 Character panel visual integration

Future actor/portrait panels should feel part of the same game without visually pretending to be room architecture.

Panel direction:
- dark grounded shell;
- paper/light text;
- restrained border;
- portrait uses canonical 64x64 identity;
- optional role/status markers;
- no neon hologram treatment by default;
- focused actor gets emphasis without covering the entire scene.

When a character is present:
- room sprite establishes physical presence;
- portrait/panel provides readable identity/dialogue context.

The two views must agree.

## 6.12 Environmental animation language

Ambient animation:
- small fan/vent cycle;
- lamp blink;
- steam/drip;
- subtle machinery;
- controlled sign pulse.

State-driven animation:
- Echo response;
- blackout failure/recovery;
- event-specific machinery;
- temporary damage response.

Rule:
the world should not shimmer everywhere.

Animation density must decrease rather than increase in quiet/restricted spaces unless the scene state specifically demands motion.

## 6.13 Vegetation

Gate Twelve uses restrained municipal vegetation.

Surface:
- compact street trees;
- planters;
- minimal ground growth.

Depot/service:
- little to none except incidental edge growth.

Lower maintenance:
- normally none unless moisture/neglect later justifies it.

Do not use lush fantasy greenery from external map references as a default.

## 6.14 Signage and readable text

Pixel world art should use:
- icons;
- arrows;
- plates;
- color/value codes;
- large identifying numbers only when legible and authored.

Narrative-detail text belongs to UI.

Do not fill 128x64 scene art with pseudo-text noise.

## 6.15 Wear and age

Wear should tell a material story.

Allowed:
- edge chipping;
- oil/drain marks;
- track wear;
- localized rust;
- patched panels;
- scuffed workshop apron;
- dirt in service corners.

Avoid:
- uniform noise;
- random cracks on every surface;
- “post-apocalypse” degradation unless story state requires it.

Gate Twelve is stressed infrastructure, not necessarily a ruined city.

## 6.16 Emergency-state language

Emergency visual grammar:
- localized red/orange practical warning;
- reduced ambient value;
- intermittent lamp failure;
- clear evacuation arrows;
- preserved navigation readability.

Do not:
- full-screen red tint;
- flashing every object;
- use emergency styling in the normal base asset.

## 6.17 Trace visual language

Trace/Echo is a specific phenomenon, not generic “magic tech glow.”

Visual principles:
- spatial afterimage;
- residual line/ring patterns;
- localized response;
- restrained cyan/blue-green family where current visual language already supports it;
- signal intensity represented by shape/motion as well as color;
- stronger effects reserved for confirmed active scenes.

Never use Trace FX to reveal hidden future destinations.

## 6.18 External-reference adaptation rule

The owner-supplied external map/settlement material contributes:
- modular section thinking;
- clear central orientation;
- distinct functional zones;
- asset-by-asset decomposition;
- reusable building/prop logic;
- route readability.

Rejected as authority:
- exact medieval architecture;
- exact sector count;
- exact area count;
- exact colors;
- exact dimensions;
- exact settlement identity.

The result must look like this game's municipal/industrial world, not a reskin of the external reference.

## 6.19 What may change from current visuals

Allowed and expected:
- current map palette refinement;
- current simplistic scene geometry;
- provisional building detailing;
- placeholder props;
- weak material differentiation;
- generic avatar art;
- actor scene composition;
- panel styling;
- current excessive reliance on rectangles;
- asset-specific lighting.

## 6.20 What should remain visually stable

Preserve unless explicitly migrated:
- overall pixel style;
- source-native grid philosophy;
- major Gate Twelve geometry;
- map node semantic positions;
- 32x48 character rig;
- actor identity anchors;
- equipment slot/paper-doll layering;
- player-safe state separation;
- map-marker semantic roles;
- Tier 1 landmark identities.

## 6.21 Material packet requirements

Every asset packet in Step 7 must specify:
- material family;
- local palette/ramp;
- darkest value;
- lightest value;
- accent colors;
- light direction;
- emissive behavior;
- wear level;
- texture frequency;
- neighboring asset compatibility;
- actor contrast requirement;
- state-overlay compatibility.

## 6.22 Step 6 locked decisions

1. Gate Twelve is grounded municipal infrastructure, not neon/cyberpunk.
2. World form must remain readable without emissive accents.
3. UI semantic colors do not dictate world materials.
4. Surface Civic, Depot/Gate, and Lower Maintenance use distinct value/material identities.
5. Trace effects are bounded/localized state layers.
6. emergency visuals are overlays, not permanent base styling.
7. characters preserve canonical identity and remain readable against rooms.
8. actor panels use canonical portraits and grounded pixel UI treatment.
9. wear is purposeful and localized, not random noise.
10. external reference contributes structure/modularity, not exact aesthetics.
11. current weak/provisional visual details may be replaced.
12. geometry, grids, identity anchors and state ownership remain stable unless explicitly migrated.

---



# 7. Asset decomposition

Status: **COMPLETE — PRODUCTION INVENTORY / CURRENT-STAGE AUDIT LOCKED**

Detailed evidence matrix:
`docs/assets/GATE_TWELVE_ASSET_STATUS_AND_PRODUCTION_MATRIX.md`

This step answers:
- what Gate Twelve needs;
- what already exists;
- what exact stable IDs are present;
- what manifests claim is integrated;
- what remains provisional;
- what exact planned IDs are missing;
- what later draft PRs refine;
- what must be reconciled before new art is created.

## 7.1 Core rule

Do not create a new asset merely because the visible game still looks weak.

First determine whether the weakness comes from:
- missing asset;
- provisional/low-quality asset;
- wrong runtime composition;
- missing state overlay;
- wrong actor placement;
- missing pixel-raster export;
- bad scaling;
- palette/material mismatch;
- branch drift;
- unpromoted refinement;
- missing QA.

This prevents duplicated assets and repeated redesign.

## 7.2 Stage vocabulary

For Gate Twelve production planning, use:

- **PLANNED** — catalog/brief exists only.
- **BRIEF_LOCKED** — design contract exists.
- **REFERENCE_SELECTED** — approved reference exists, not runtime art.
- **CODE_PRESENT** — exact ID appears in current audited visual catalogs.
- **INTEGRATED** — manifest/runtime binding exists on recorded implementation line.
- **OPEN_PR_REFINEMENT** — later draft branch refines an existing asset; not promoted.
- **QA_PENDING** — runtime may be integrated, but art review/phone/handset evidence remains.
- **VERIFIED** — only when the relevant manifest/evidence actually proves the required gates.
- **CANON_APPROVED** — final identity/art approval; stronger than automated runtime green.

Do not collapse these states into a single “done.”

## 7.3 Current asset-program baseline

The v1 visual plan contains exactly 500 planned units.

Batch 001 units 001–100 are the current playable-slice visual baseline.

Step 7 audited all 100 Batch 001 entries against:
- current code catalogs;
- Wave A/B/C manifests;
- current documentation branch ancestry;
- relevant open refinement lines.

The resulting matrix is the required pre-production check for this region.

## 7.4 Current integrated/provisional strengths

The current branch/manifests already provide substantial infrastructure:

- player front paper-doll base;
- starting equipment icons/layers;
- relay item/state visuals;
- nine named-location scene families, with several state overlays;
- infrastructure modules/props;
- map semantic markers;
- navigation/resource/quest icons;
- Trace FX families;
- authored district map master;
- transitional room-actor system.

Therefore the next phase is **not** “generate everything again.”

It is:
- close exact missing IDs;
- improve weak/provisional masters;
- reconcile branch drift;
- complete QA;
- create missing actor/panel/identity assets;
- then expand the world.

## 7.5 Critical identity reconciliation

Jack Wilson:
- approved reference `UI_REFERENCE_CHARACTER_APPROVED_V1` exists;
- it is now preserved in this documentation branch;
- the 32x48 rig remains valid;
- generic-player visual assumptions are superseded for final player identity;
- the approved reference is not itself a runtime sprite.

Required:
- six-view technical turnaround;
- directional masters;
- portrait family;
- animation masters only as gameplay needs them;
- equipment alignment to Jack rather than a generic silhouette.

Tamsin:
- full authored identity exists;
- a front room actor exists in code;
- Wave A still describes the full turnaround as BRIEF_LOCKED;
- manifest/code scope must be reconciled before the turnaround is declared complete.

Courier:
- current story-actor implementation exists;
- needs explicit manifest/provenance if retained as production actor art.

## 7.6 Exact current-region missing/gap priorities

High-value planned exact IDs not found in the current audited catalogs include:
- `PLATFORM_NINE_EVACUATED_SCENE`;
- `DISTRICT_ARCHIVE_TERMINAL_CLOSEUP`;
- `WORKSHOP_ROW_RUMOR_SCENE`;
- `PROP_DIAGNOSTIC_READER`;
- `FX_TRACE_STRAIN`;
- `UI_MAP_TRAVEL_TRANSITION`;
- reusable exact `EMERGENCY_LIGHT_OVERLAY`;
- reusable exact `BLACKOUT_SHADOW_OVERLAY`.

Caution:
- missing exact ID does not prove no equivalent pixels/state treatment exist under another ID;
- audit equivalents before creating anything new.

## 7.7 Naming drift identified

Batch unit 030 is planned as:
`ITEM_DEAD_RELAY_INTACT`

Current Wave B integration uses:
`ITEM_DEAD_RELAY_ICON`

This is an ID/contract reconciliation item.

Do not create a second intact relay asset merely to satisfy the planned name.

Resolve by choosing:
- canonical ID;
- compatibility alias;
- manifest/catalog correction;
- migration if necessary.

## 7.8 Open refinement lines that must not be silently promoted

Known draft refinement lines include:
- PR #22 — player silhouette/current loadout and approved Jack reference work;
- PR #27 — Service Tunnel scene refinement;
- PR #28 — Service Tunnel/infrastructure atlas composition detail;
- PR #30 — Quiet Stair scene refinement;
- PR #31 — Service Tunnel ambient animation.

They are evidence and candidate work.

They are not automatically canonical merely because they are newer.

Each must be:
1. compared to current authority;
2. reviewed for stable IDs/state ownership;
3. verified at its exact head;
4. either promoted deliberately or rejected/superseded.

## 7.9 Per-area production packets

The detailed matrix now defines the packet needs for:
- Depot Plaza;
- Workshop Row;
- Municipal Archive;
- Platform Nine;
- Relay Workbench;
- Gate Twelve;
- Quiet Stair;
- Service Tunnel;
- Trace Chamber.

Each future packet must include:
- geometry envelope;
- material family;
- palette/lighting;
- existing assets;
- missing assets;
- actors;
- props;
- state overlays;
- animation;
- panel-safe zones;
- authoritative bindings;
- QA.

## 7.10 Character panels

Step 7 confirms that character panels need their own asset/data contract.

A future room panel may require:
- canonical 64x64 portrait;
- display name;
- actor focus state;
- relationship/status summary if player-safe;
- role/faction marker if player-safe;
- dialogue/emotion state;
- interaction controls.

The room actor and portrait must share identity.

The panel cannot decide actor presence.

Target prerequisite:
a player-safe actor projection such as `GameSnapshot.actors`.

## 7.11 Production ordering

Gate Twelve production order after this audit:

### P0 — reconciliation
- approved Jack reference/blueprint;
- manifest/code drift;
- relay ID naming;
- open refinement review.

### P1 — missing current-region assets
- Platform Nine evacuated;
- Archive terminal closeup;
- Workshop rumor state;
- diagnostic reader;
- Trace Strain;
- reusable emergency/shadow overlays where no equivalent already satisfies the contract.

### P2 — art-quality replacement
- review current integrated scene masters at native scale;
- replace weak geometric/provisional masters while preserving IDs/bindings;
- review final map landmarks/materials.

### P3 — actor/panel system
- projected actor contract;
- Tamsin/Jack portraits;
- room actor variants;
- panel composition.

### P4 — animation
- keep Service Tunnel ambient loop small and reusable;
- state-driven Gate/Plaza effects;
- character animation only when consumed by gameplay.

### P5 — expansion
- world-scale tiles/buildings/characters only after world schemas are locked.

## 7.12 Step 7 locked decisions

1. Batch 001 is an inventory baseline, not permission to regenerate assets blindly.
2. Integrated runtime state and final art approval remain separate.
3. The 100-unit current-slice matrix is now the required duplication-prevention audit.
4. Jack's approved character reference is preserved as visual authority input.
5. Tamsin/courier room-actor code and manifest scope need reconciliation.
6. relay unit #030 naming drift must be resolved before duplicate production.
7. exact missing scene/state assets are explicitly tracked.
8. open PR refinements are candidates, not canonical promotion.
9. character panels require player-safe actor projection.
10. per-area asset packets are now safe to author using Steps 5–7.

---

# 8. Application UX plan

Status: **COMPLETE — GATE TWELVE PLAYER-EXPERIENCE CONTRACT LOCKED FOR LATER IMPLEMENTATION**

Parent application authority:
- `docs/android/APPLICATION_UX_MASTER_PLAN.md`

Companion visual/runtime authorities:
- `docs/assets/PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md`
- `docs/assets/ROOM_ACTOR_PANEL_OVERLAY_REUSE_STANDARD.md`
- `docs/assets/GATE_TWELVE_ASSET_STATUS_AND_PRODUCTION_MATRIX.md`

This step defines how Gate Twelve should actually feel inside the Android game: how the player sees the current place, present characters, narrative, actions, map, travel, resources, character panels, and location detail without turning Compose into a second rules engine.

No runtime code is changed by Step 8.

## 8.1 Primary experience rule

For Gate Twelve, the application should prioritize:

`place -> people -> situation -> action -> consequence -> travel/management when needed`

The player should spend most of ordinary play time in a **current-location / Story experience**, not in a management dashboard.

The application may have many supporting screens, but they must feel connected to the same world and state.

## 8.2 What is preserved from the existing application

The following concepts remain valid unless a later migration explicitly replaces them:

- authoritative gameplay outside Compose;
- player-safe projection boundary;
- stable location/item/NPC/quest IDs;
- Story as the main narrative surface;
- Map as an interactive world-navigation surface;
- separate Character / Stats / Equipment / Inventory / Skills / Quests surfaces where useful;
- save/load through engine-owned persistence;
- dynamic resource values rather than decorative static bars;
- source-native pixel rendering and nearest-neighbor scaling;
- the 32x48 player paper-doll contract;
- semantic map-node anchors and authoritative route state;
- explicit missing-asset fallback rather than crashing or inventing state;
- developer tooling separated from normal play.

Step 8 does not authorize moving any of those responsibilities into visual code merely for convenience.

## 8.3 What is expected to change

The following presentation areas are expected to be reworked materially:

### Story/current-location presentation
Current technical/prototype composition may be replaced by a richer layered room presentation that combines:
- environment master;
- structural modules;
- state overlays;
- props;
- player sprite when appropriate;
- present NPC room actors;
- temporary FX;
- focused actor panel when useful;
- narrative;
- choices/actions;
- compact resource/status information.

### Map presentation
The current geometric/technical map look is a replacement candidate.

Target:
- authored 256x144 Gate Twelve map art;
- permanent physical paths/background;
- authoritative route/state overlays;
- current-player marker;
- discovered/current/reachable/unavailable states;
- selected destination;
- location detail/arrival preview;
- travel action only when the projected state authorizes it.

### Character presentation
The generic/provisional player appearance is a replacement candidate.

Target:
- Jack-approved visual identity;
- paper-doll equipment;
- portrait identity;
- visible player-safe conditions/status;
- consistent appearance across Story, Character and panels.

### Actor presentation
Location/scene-specific hard-coded actor placement is transitional.

Target:
- player-safe projected room actors;
- actor sprites selected from canonical identity;
- panel availability driven by those projected actors;
- no hidden-flag reconstruction in Compose.

### Navigation/chrome
Permanent chrome may be reduced/reorganized if it competes with the game world.

The exact final navigation count remains an application-wide decision, but Gate Twelve requires fast access to:
- Story/current location;
- Map;
- Character management;
- Inventory/equipment;
- Quests;
- Settings/save.

## 8.4 Story screen composition contract

Default conceptual vertical order on a phone:

1. compact location/context header;
2. current-location visual stage;
3. contextual actor focus/panel when needed;
4. resource/status strip;
5. narrative/dialogue text;
6. player actions/choices;
7. secondary contextual details only when requested.

The visual stage must not become a tiny banner above an oversized wall of generic controls.

Conversely, the art must not consume so much height that choices and narrative become difficult to use.

The final exact dimensions remain responsive-layout implementation work.

## 8.5 Room visual stage

The room stage follows the runtime composition standard.

Default order:

1. environment master;
2. permanent structures/modules;
3. static props;
4. rear state overlays;
5. player sprite when composition calls for it;
6. projected NPC room actors;
7. held/equipment layers;
8. foreground occluders;
9. temporary FX;
10. focus/selection treatment;
11. UI actor panel above the world layer.

Important:
- a character is not drawn merely because the story document mentions them historically;
- a character is drawn because player-safe current state says they are present;
- the room art does not decide quest availability;
- permanent room art does not bake temporary blackout/Trace/relationship state into the base master.

## 8.6 Character-in-room and focus-panel behavior

Target actor source:

`player-safe projected actor list -> room actor -> optional portrait/focus panel`

Focus priority:

1. explicitly selected actor;
2. current speaker;
3. current interaction target;
4. party-relevant actor;
5. other present actor.

When one important named actor is present:
- show the room actor;
- allow a focused portrait/name panel where useful;
- preserve enough visible room art to maintain location context.

When multiple actors are present:
- do not open multiple large portrait panels simultaneously;
- use compact selectable actor identifiers/chips/portraits if required;
- one actor receives full focus at a time.

When no named actor is present:
- do not display a fabricated character panel.

Panel content may include only projected/player-safe information such as:
- display name;
- portrait;
- visible role/faction if intentionally known;
- visible relationship/status summary if intentionally exposed;
- dialogue/emotion;
- available authored interactions.

Panel content must not expose:
- hidden goals;
- private memories;
- secret flags;
- undiscovered faction state;
- future quest outcomes;
- raw AI/NPC simulation values.

## 8.7 Gate Twelve actor/panel expectations by area

These are composition expectations, not assertions that every actor is currently present.

### Depot Plaza
Typical target:
- public actor slots;
- temporary meeting-point NPCs only when projected;
- no permanent full-screen NPC panel.

Panel-safe priority:
- preserve central plaza orientation and depot frontage.

### Workshop Row
Typical target:
- workers/contractors when authored;
- focused worker panel only during interaction;
- tools/benches remain visible enough to preserve practical identity.

### Municipal Archive
Typical target:
- clerk/visitor actors when authored;
- research/document interaction may take focus without replacing the room permanently.

### Platform Nine
Current known actors include Tamsin and the injured courier in opening-related implementation evidence.

Target:
- strong support for one or more room actors;
- speaker/focus changes without redrawing the environment;
- evacuation-state overlays remain separate from actor art.

### Relay Workbench
Target:
- Tamsin or another technically relevant actor when projected;
- close technical interaction can use a focused panel/prop view;
- relay/diagnostic object remains a separate stateful prop.

### Gate Twelve
Target:
- actor panel is secondary to the threshold landmark;
- do not cover the gate silhouette with persistent UI.

### Quiet Stair
Target:
- normally sparse;
- actor panel appears only for authored event/encounter presence.

### Service Tunnel
Target:
- room actors may appear during investigation;
- panel should not erase tunnel depth cue or future deep-route visual stub.

### Trace Chamber
Target:
- supports training/research interactions;
- present trainer/companion panel only when authoritative state says so;
- Trace FX remain behind/around actors according to state and must not obscure action readability.

## 8.8 Portrait contract

Named recurring actors should use canonical portrait assets.

Target portrait grid:
- 64x64 source-native master unless a later global portrait migration replaces it.

Portraits must share identity with:
- room sprite;
- gameplay sprite;
- equipment/outfit state;
- permanent marks;
- hair/face silhouette;
- role markers.

The portrait is not a different redesign of the character.

Emotion variants may change:
- mouth/eyes/brow;
- small pose/angle details;
- controlled lighting where scene-appropriate.

They must not silently change:
- identity;
- outfit ownership;
- permanent marks;
- body/face structure.

## 8.9 Text, world signage and “text-art”

Three different text responsibilities remain separate.

### Narrative/UI text
Rendered as readable UI typography.
Used for:
- dialogue;
- narration;
- choices;
- labels;
- descriptions;
- system messages.

### World signage
Part of an environment/prop asset.
Used for:
- arrows;
- location numbers;
- public/service symbols;
- large short identifiers.

World signage must match:
- area perspective;
- pixel density;
- material/lighting.

### PixelSprite/text-map source definitions
A code/text representation of pixel rows may remain a legitimate source master when intentionally authored.

It is not treated as UI text and does not need to be replaced merely because its pixels are stored textually.

## 8.10 Reuse and overlay UX rule

The app should prefer compositing over duplicating entire screens/scenes.

Reuse a base environment when:
- architecture is unchanged;
- state difference is temporary;
- the same perspective/scale remains valid.

Apply overlays for:
- blackout;
- emergency light;
- powered/unpowered state when projected;
- Trace/Echo state;
- smoke/steam;
- temporary damage;
- selection/focus;
- map current/reachable/selected state.

Use a new full master only when:
- architecture materially changes;
- perspective changes;
- silhouette changes enough that an overlay cannot preserve truth.

This keeps the world visually coherent and prevents dozens of near-duplicate rooms from drifting apart.

## 8.11 Map screen — Gate Twelve district mode

Gate Twelve uses the 256x144 district master as its local map surface.

Default district-mode decision:
- fit the complete Gate Twelve district into the primary phone map viewport when practical;
- do **not** require zoom merely to understand the nine current nodes;
- secondary labels/details may appear only after selection;
- touch targets may be larger than visible markers;
- map marker positions remain tied to semantic node anchors.

The current district is small enough that comprehension should come before elaborate camera controls.

Future world/city maps may require pan/zoom; this step does not force that model onto Gate Twelve.

## 8.12 Map visual stack

Default order:

1. district authored base;
2. permanent route/surface geometry;
3. permanent landmarks;
4. safe environmental state overlays;
5. discovered-node markers;
6. current/reachable/unavailable state;
7. player marker;
8. selected destination;
9. optional travel-preview route;
10. location detail UI.

The base map must not permanently encode:
- current node;
- reachable status;
- quest status;
- selected destination.

## 8.13 Location selection and travel UX

Selecting a discovered location should:
- visually focus the node;
- show player-facing title;
- show player-facing description;
- show arrival/location preview if available;
- show travel availability/reason from authoritative projection;
- provide travel action only when legal.

Selecting does **not** immediately travel.

Travel remains a deliberate action.

Travel action must:
- call authoritative engine/domain travel;
- consume authoritative time/cost;
- return the resulting snapshot;
- update Story/current location;
- update map state.

No Compose-only teleport rule.

## 8.14 Proposed Depot Plaza <-> Platform Nine connector UX

Step 3 requires this future authored route.

Until the content graph contains it:
- map art may imply the physical depot entrance;
- UI must not show it as a normal traversable edge;
- no travel button may be fabricated.

After content migration:
- the route appears through normal projected adjacency;
- selection/travel behavior needs no special hidden UI exception.

## 8.15 Story <-> Map relationship

Gate Twelve should make Story and Map feel like two views of one world.

Target behavior:
- Story shows current place and current situation;
- Map shows spatial relationship and travel choices;
- selecting/traveling changes authoritative current location;
- returning to Story shows the new location/state.

No duplicated independent “current location” state in Android.

## 8.16 High-use actions and contextual shortcuts

High-use location-specific actions should remain near the location that owns them.

Examples:
- Trace training belongs to Trace Chamber;
- record research belongs to Archive;
- relay diagnostics belongs to Workbench;
- district notices belong to Depot Plaza.

The app may offer a shortcut to a known location/action only if it still routes through authoritative state and does not bypass travel/access rules.

Avoid one universal “Activities” menu that erases the meaning of place unless the final application UX later proves that such an aggregation is necessary.

## 8.17 Resource/status presentation

Story should keep a compact resource/status view.

Requirements:
- values come from projection;
- bars reflect current/max;
- color is not the only indicator;
- exact numeric values remain readable where useful;
- new ability-specific resource displays appear only when player-facing and relevant.

The resource strip should not become a giant dashboard that pushes room/narrative content off-screen.

## 8.18 Choice/action presentation

Actions must communicate:
- action text;
- enabled/disabled state;
- player-safe disabled reason where available;
- important cost/time information only when intentionally exposed;
- selected interaction context.

Do not expose:
- hidden difficulty formulas;
- secret future outcomes;
- raw branch conditions.

Large action sets should use grouping/progressive disclosure rather than dozens of identical cards.

## 8.19 Location detail / arrival preview

Each named Gate Twelve location should eventually support a compact detail packet:

- location ID;
- player-facing title;
- short purpose/description;
- current/discovered/reachable state;
- preview art;
- selected state;
- available travel action;
- relevant visible activity badge only when projected;
- known actor presence only if the application intentionally exposes it.

The detail packet does not own gameplay.

## 8.20 Navigation decision for this region

Gate Twelve does not lock the final global navigation count.

It does lock these usability requirements:
- Story and Map are one-tap/high-priority destinations;
- Settings/save are not allowed to dominate the play surface;
- developer tools remain hidden/separate from ordinary play;
- management surfaces must preserve a direct return to current Story/location;
- contextual actor/location panels are not permanent global tabs.

## 8.21 Phone-first behavior

Gate Twelve must remain usable at small phone widths.

Requirements:
- no horizontal scrolling for ordinary narrative text;
- primary choices have touch-safe targets;
- map nodes have touch-safe hit regions;
- focused portrait/panel can collapse;
- long descriptions scroll independently without moving critical actions unpredictably;
- pixel art scales by integer/nearest-neighbor strategy where possible;
- no tiny embedded labels required for map comprehension;
- no full-screen panel that permanently hides the location art.

Galaxy A03-class constraints remain a performance/QA consideration, not proof of physical-device success.

## 8.22 Motion and animation UX

Animation supports state; it does not delay every interaction.

Rules:
- local/short-beat travel should not require long transitions;
- ambient loops remain subtle;
- reduced-motion mode must have a static/low-motion equivalent;
- State-driven Trace/emergency FX may be stronger but bounded;
- character animation should only be produced when a runtime interaction consumes it;
- avoid whole-screen video for ordinary room animation.

## 8.23 Loading and failure behavior

Every Gate Twelve visual surface must have a safe degradation path.

If environment art is missing:
- use a documented fallback;
- preserve location identity and actions;
- do not crash.

If an actor sprite is missing:
- preserve actor presence in text/panel where safe;
- use an explicit fallback only if the actor asset contract permits it;
- do not silently show the wrong character.

If a portrait is missing:
- compact text identity is preferable to a wrong portrait.

If map art is missing:
- preserve authoritative node/route interaction with fallback presentation.

Missing art must never change gameplay truth.

## 8.24 Accessibility requirements

Gate Twelve UI must support:
- scalable/readable text;
- sufficient contrast;
- non-color-only state communication;
- reduced motion;
- touch target sizing;
- narration/audio compatibility;
- readable numeric resource status.

Pixel-art authenticity is not an excuse for inaccessible text or ambiguous state.

## 8.25 Application-state ownership table

| Concern | Owner | Android responsibility |
| --- | --- | --- |
| current location | engine/world | render projected value |
| actor presence | engine/player-safe projection | compose room actors/panels |
| route legality | engine/world map | show projected reachable state, invoke travel |
| quest availability | engine/quest/narrative | render available authored actions |
| resources | engine/stats/powers | render values/bars |
| environment identity | visual asset system | render correct master/module |
| blackout/Trace state | engine projection + visual binding | select safe overlay |
| actor identity | character blueprint/assets | render canonical sprite/portrait |
| map selection | UI-local ephemeral state | highlight selected projected node |
| panel focus | UI-local ephemeral state constrained to projected actors | choose which present actor is focused |
| hidden NPC goals | engine private state | never render unless deliberately projected |

## 8.26 Area packet UX additions

Each Gate Twelve area production packet must now include:

- Story visual-stage composition;
- actor-safe ground positions;
- portrait/panel-safe zone;
- expected panel side/collapse behavior;
- map arrival preview;
- location-detail text ownership;
- available overlay classes;
- animation/reduced-motion variant;
- fallback behavior;
- phone screenshot target;
- projected fields required by the area;
- explicit statement of fields that remain hidden.

This extends the Step 7 asset packet into an application-consumable packet.

## 8.27 What remains undecided after Step 8

Still open:
- exact final global navigation bar/drawer structure;
- final orientation support;
- world-map pan/zoom model beyond Gate Twelve;
- final portrait panel dimensions at every breakpoint;
- actor chip visual design;
- exact transition animation timing;
- low-memory cache implementation;
- whether Relationships/People and Knowledge/Logs become dedicated global surfaces;
- whether future Activities gets a dedicated screen;
- final tactical-combat entry/exit UX.

Those decisions belong to application-wide work or later systems, not this region step.

## 8.28 Step 8 locked decisions

1. Story/current-location is the primary Gate Twelve play surface.
2. Map is the primary spatial/travel companion surface.
3. Room actors and actor panels are driven only by player-safe projected presence.
4. One focused actor panel at a time is the default when multiple actors are present.
5. Jack/Tamsin/other recurring portraits must match room/gameplay identity.
6. UI text, world signage and textual PixelSprite source definitions remain separate concepts.
7. State changes use overlays whenever architecture is unchanged.
8. Gate Twelve district map defaults toward complete-district comprehension without mandatory zoom.
9. Selection does not equal travel; travel remains an explicit authoritative action.
10. Depot Plaza <-> Platform Nine must not appear as a legal route until the engine/content graph contains it.
11. Story and Map share one authoritative current-location state.
12. Location-owned activities remain contextual rather than being flattened into one generic menu by default.
13. Current geometric/provisional Story/Map presentation may be replaced while stable IDs/state contracts remain.
14. Missing visual assets degrade presentation, never gameplay truth.
15. Phone readability/accessibility outrank decorative density.

---

# 9. State-layer plan

Status: **COMPLETE — VISUAL/GAMEPLAY STATE OWNERSHIP LOCKED**

This step defines which Gate Twelve changes belong in permanent art, which belong in reusable visual layers, which belong in actor/equipment layers, and which must remain engine-only. It exists to prevent two failures: duplicating entire scenes for small state changes, and leaking hidden gameplay state into presentation.

## 9.1 State ownership rule

The visual stack may reflect state only when that state is intentionally player-safe.

Target flow:

`authoritative engine/world state -> player-safe projection -> visual binding -> asset/layer composition`

The inverse is prohibited:

`pixel color / hidden flag guess / Compose heuristic -> gameplay conclusion`

Art never becomes the source of truth for:
- discovery;
- reachability;
- quest completion;
- actor presence;
- item ownership;
- relationship state;
- ability discovery;
- route legality;
- hidden world events.

## 9.2 Permanent base-art state

Permanent base art owns what is physically stable for the location.

Examples:
- architecture;
- floors;
- roads;
- tracks;
- structural supports;
- fixed material families;
- permanent signage frames;
- stable landmark silhouettes;
- non-stateful furniture.

Base art must not permanently encode:
- blackout;
- current quest;
- selected map destination;
- temporary damage;
- temporary NPC presence;
- Trace activation;
- route availability;
- current player position.

## 9.3 Reusable environment-overlay classes

Gate Twelve uses reusable overlays for temporary environmental state.

Required classes:

### Power / blackout
Examples:
- blackout shadow;
- emergency-light contribution;
- restored-power contribution;
- bounded lamp/indicator changes.

### Access / mechanical state
Examples:
- powered/off indicator;
- door locked/open/closed only when projected;
- terminal active/inactive.

### Damage / emergency
Examples:
- temporary damage;
- smoke;
- steam;
- debris;
- emergency guidance.

### Trace / signal
Examples:
- Echo-active response;
- Signal Pulse;
- Directional Trace;
- Trace Strain;
- residual signal afterimage.

### Event decoration
Examples:
- evacuation remnants;
- temporary notice;
- temporary work setup;
- event-specific safe prop.

A full alternate base master is used only when physical architecture or major silhouette changes enough that overlays are no longer honest.

## 9.4 Actor state layer

Actor presence is a separate state layer.

Target projected actor data should support:
- stable actor/NPC ID;
- room/location ID;
- visible pose;
- visible expression;
- visible outfit/equipment state;
- room-sprite asset ID or resolvable identity;
- portrait asset ID where available;
- player-safe interaction/focus information.

Room actor rendering must not infer presence from hidden quest flags.

Tamsin, courier and future actors use the same rule.

## 9.5 Equipment state layer

Player/NPC identity masters remain separate from visible equipment.

For Jack:
- base body/identity remains stable;
- equipment overlays attach through the 32x48 rig;
- held-object layers use documented anchors;
- status effects are not painted into the identity master.

If an item has no authored visual layer:
- it remains logically equipped;
- the UI may state that the visual is unavailable;
- no invented generic shape is added.

## 9.6 Prop state layer

Stateful props remain separate where practical.

Examples:
- dead relay intact/opened/damaged/signal-lost;
- diagnostic reader;
- Gate Twelve door state;
- archive terminal state;
- notice board content/state.

A prop-state change should not force a duplicated full environment master unless its physical footprint changes the scene materially.

## 9.7 Map-state layer

The district map keeps permanent geography separate from player state.

Permanent:
- road/surface geometry;
- building/landmark silhouettes;
- neutral physical route cues.

Projected state:
- discovered;
- current;
- reachable;
- unavailable;
- player marker;
- selected destination;
- travel preview;
- safe visible event marker if later authored.

Undiscovered/hidden destinations must not be named or revealed by a permanent label.

## 9.8 UI-local ephemeral state

The following may remain local to Android presentation because they do not change game truth:
- selected map node;
- currently focused actor among projected actors;
- expanded/collapsed panel;
- scroll position;
- selected inventory item;
- selected stat/skill detail;
- temporary tab/surface choice.

UI-local state must be discarded/rebuilt safely from the authoritative snapshot when game state changes.

## 9.9 State precedence

When multiple visual layers overlap, use this conceptual precedence:

1. permanent environment;
2. permanent modules/props;
3. environment-state overlays;
4. stateful interaction props;
5. room actors;
6. equipment/held layers;
7. actor status layers;
8. transient ability/event FX;
9. selection/focus treatment;
10. UI panels/text/actions.

Rules:
- a state overlay may darken or illuminate actors only through a documented visual effect;
- an FX layer may not hide required interaction information;
- selection/focus never permanently mutates source art;
- UI panel visibility does not change actor presence.

## 9.10 Gate Twelve location-state expectations

### Depot Plaza
Expected states:
- normal/open civic state;
- blackout/emergency state;
- public notice/event overlays;
- projected public actors.

### Workshop Row
Expected states:
- default working state;
- rumor/event-specific presentation if authored;
- worker actors only when projected.

### Municipal Archive
Expected states:
- default backup-power room;
- terminal/research focus;
- conditional record availability in UI, not painted spoilers.

### Platform Nine
Expected states:
- blackout opening;
- post-evacuation state;
- room actors/crowd strategy;
- emergency lighting;
- relay/courier event props.

### Relay Workbench
Expected states:
- default;
- relay open/damaged/signal-lost prop state;
- diagnostic focus;
- Tamsin presence when projected.

### Gate Twelve
Expected states:
- sealed/default;
- Echo-active;
- future powered/open variants only when engine state supports them.

### Quiet Stair
Expected states:
- sparse default;
- guidance/emergency state;
- event actor only when projected.

### Service Tunnel
Expected states:
- default;
- aftershock;
- ambient machinery;
- projected investigators/companions;
- deeper-continuation cue without revealing undiscovered destination.

### Trace Chamber
Expected states:
- idle;
- training;
- Signal/Directional Trace FX;
- Trace Strain;
- projected actors;
- research/training availability through authoritative actions.

## 9.11 State-binding registry requirement

Before broad visual implementation, every stateful asset should have a binding record with:
- visual asset ID;
- owner system;
- player-safe projected field;
- allowed values;
- fallback;
- z-order/layer class;
- locations consuming it;
- whether animation exists;
- reduced-motion behavior;
- QA case.

This may live in a data manifest or generated registry after the schema is audited.

## 9.12 Hidden-state leak tests

Required future regression cases:
- undiscovered node does not reveal its name through art/UI;
- unreachable route does not receive normal active-route treatment;
- absent NPC does not appear because a scene once used them;
- private NPC goal/memory does not change visible panel unless explicitly projected;
- future quest objective is not shown early;
- Trace FX does not point to a hidden destination unless the technique result is known;
- disabled action reason contains only player-safe explanation.

## 9.13 Step 9 locked decisions

1. permanent art owns stable physical identity only;
2. blackout/emergency/Trace/event changes are layered when architecture is unchanged;
3. actor presence is an explicit player-safe state layer;
4. equipment remains separate from character identity;
5. stateful props use variants/overlays before whole-scene duplication;
6. map geography and map gameplay state remain separate layers;
7. UI focus/selection is local ephemeral state, not gameplay authority;
8. every stateful visual needs an auditable binding;
9. hidden-state leak tests are mandatory before final integration.

---

# 10. Performance and section-loading strategy

Status: **COMPLETE — MOBILE/SECTION STRATEGY LOCKED AT ARCHITECTURAL LEVEL**

This step defines how Gate Twelve remains responsive while keeping modular pixel art and future world growth possible.

It does not choose a final cache implementation or claim measured Galaxy A03 performance.

## 10.1 Asset-size philosophy

Keep source-native masters compact:
- district map: 256x144;
- narrative scene: 128x64;
- gameplay actor: 32x48;
- portrait: 64x64;
- icons/props at documented source-native grids.

Scale for display using nearest-neighbor/integer-safe methods where practical.

Do not ship oversized smooth reference images as runtime substitutes.

## 10.2 Loading unit

The player-facing geography remains:
`Region -> Macrozone -> Named Subzone`

Technical loading may be finer.

Recommended Gate Twelve loading unit:
- one current narrative room/subzone packet;
- actors/props/overlays required by that room;
- shared UI/icon resources;
- district map master and lightweight marker assets;
- optionally the immediately likely next-room packets if profiling proves useful.

Do not load all future world art merely because the world registry exists.

## 10.3 Macrozone sections

The three macrozones are useful technical grouping candidates:
- Surface Civic District;
- Depot / Gate Core;
- Lower Maintenance Network.

They are **not** hard loading walls by default.

A player should not see an artificial “section boundary” unless a real physical transition supports it.

## 10.4 Shared asset cache direction

Shared reusable assets should be addressable by stable asset ID.

Candidates for reuse:
- infrastructure tiles;
- doors;
- pipes/cables;
- signs;
- marker icons;
- resource icons;
- actor portraits;
- common equipment;
- overlays/FX.

Target behavior:
- avoid decoding/recreating identical assets for every scene;
- evict or release non-current heavy assets when needed;
- preserve tiny common assets when cheaper than reload.

Exact LRU/cache size remains implementation/profiling work.

## 10.5 Animation budget

Animation is bounded.

Rules:
- small ambient loops;
- limited simultaneous animated layers;
- no whole-scene continuous video;
- reduced-motion alternative;
- state-driven animation stops when state ends;
- off-screen/non-current room animations do not run;
- frame count/rate chosen from visual need, not maximal smoothness.

## 10.6 Compose recomposition discipline

Android implementation should:
- keep authoritative snapshot stable/structured;
- avoid rebuilding raster masters every recomposition;
- remember/cache decoded art appropriately;
- isolate frequently changing UI state from static scene art;
- avoid per-frame recomposition for simple pixel loops when a bounded animation primitive is sufficient;
- avoid large allocations during every text reveal tick.

These are implementation requirements to verify, not claims about current code.

## 10.7 Map performance

Gate Twelve district map is small.

Target:
- one 256x144 base;
- lightweight overlays/markers;
- selection/focus state;
- no need for an expensive tiled world renderer at this scale.

Future city/world maps may need tile/LOD streaming; Gate Twelve should not prematurely adopt that complexity.

## 10.8 Actor/panel performance

Room actors:
- only current-room actors are required;
- portrait assets load when focus/panel needs them or remain in a small character cache if profiling supports it;
- do not preload every world NPC portrait.

## 10.9 Low-memory/failure behavior

If memory pressure occurs:
- drop non-current scene caches first;
- preserve current room;
- preserve UI/navigation essentials;
- reload non-critical previews on demand;
- use explicit fallback rather than corrupted/smoothed art.

## 10.10 Performance evidence gates

Before claiming mobile-ready:
- Android unit/build passes;
- emulator runtime passes;
- 320dp/low-width screenshot QA;
- memory/CPU observations on representative emulator;
- physical Galaxy A03 install/start separately;
- current-room transition timing observed;
- animation/reduced-motion observed;
- no visible smoothing/scaling corruption.

## 10.11 Step 10 locked decisions

1. Gate Twelve remains source-native and compact.
2. current-room packet is the primary content-loading unit.
3. macrozones may group resources but are not artificial player-visible loading walls.
4. common assets use stable IDs and may be cached.
5. animation is bounded and off-screen animation stops.
6. district map remains simple; world-scale tiling is deferred.
7. low-memory fallback must preserve gameplay truth.
8. physical Galaxy A03 evidence remains a separate acceptance gate.

---

# 11. Implementation order and dependency graph

Status: **COMPLETE — SAFE EXECUTION ORDER LOCKED**

The documented target is now detailed enough to define implementation order, but not to skip exact-head audits.

## 11.1 Phase A — exact current-state reconciliation

Before code changes:
- inspect live implementation branch/PR heads;
- inspect open visual refinements;
- compare current catalogs/manifests;
- confirm current Story/Map/actor consumers;
- confirm Jack approved-reference branch state;
- confirm test/CI baseline.

Required output:
- updated exact-head rework matrix;
- no assumptions from stale handoffs.

## 11.2 Phase B — data/projection contracts

Implement or formalize player-safe fields needed by documented UX:
- projected room actors;
- projected safe visual state;
- projected prop/door state where needed;
- safe map route/discovery/reachability;
- safe visible relationship/status fields only if approved.

Do this before UI begins guessing state.

## 11.3 Phase C — asset/provenance reconciliation

Resolve:
- Jack final runtime identity path;
- Tamsin room/portrait provenance;
- courier manifest gap;
- relay ID naming drift;
- missing exact overlay equivalence;
- Service Tunnel/Quiet Stair refinement branches;
- missing current-region exact assets.

Do not regenerate existing assets blindly.

## 11.4 Phase D — Story/current-location composition

Rework Story in bounded slices:
1. layered scene host;
2. actor rendering from safe projection;
3. focused actor panel;
4. resource/status integration;
5. prop/state overlays;
6. fallback behavior;
7. phone layout.

Keep choices/narrative authoritative.

## 11.5 Phase E — Map presentation

Rework map presentation while preserving:
- semantic node positions;
- hit targets;
- discovered/reachable state;
- authoritative travel.

Sequence:
1. authored base;
2. permanent routes/landmarks;
3. marker/state overlays;
4. selection/detail;
5. arrival preview;
6. explicit travel;
7. phone QA.

## 11.6 Phase F — Character identity and equipment visuals

Integrate:
- Jack canonical gameplay master;
- directional masters only when consumed;
- equipment layers;
- portrait;
- status overlays;
- Character-screen replacement of provisional/generic art.

No equipment rule duplication in UI.

## 11.7 Phase G — missing Gate Twelve production assets

Create only after equivalence/provenance audit:
- Platform Nine evacuated state;
- Archive terminal closeup;
- Workshop rumor state;
- diagnostic reader;
- Trace Strain;
- reusable emergency/blackout overlays if true equivalents do not exist;
- required actor/portrait assets.

## 11.8 Phase H — route/content migration

Only after content decisions are finalized:
- add Depot Plaza <-> Platform Nine authoritative connection;
- choose travel time;
- choose discovery/unlock semantics;
- validate graph;
- update tests;
- update map projection.

Do not special-case the route solely in Android.

## 11.9 Phase I — animation

After static composition is verified:
- Service Tunnel ambient;
- emergency/Trace state animation;
- actor animation only when gameplay consumes it;
- reduced-motion paths.

## 11.10 Phase J — verification/evidence

Run all Step 12 gates and record:
- exact branch;
- exact SHA;
- workflow;
- artifacts;
- screenshots;
- known gaps.

## 11.11 Dependency summary

Critical chain:

`exact audit -> safe projection -> asset reconciliation -> Story/Map composition -> missing art -> route/content migration -> animation -> full verification`

Independent/parallel where safe:
- documentation/world catalogs;
- non-conflicting asset authoring after packet lock;
- test authoring;
- performance instrumentation.

## 11.12 Step 11 locked decisions

1. exact audit precedes implementation;
2. projection contracts precede actor/panel UI;
3. provenance reconciliation precedes duplicate asset generation;
4. Story and Map are rebuilt in bounded independent slices;
5. Jack identity/equipment integration remains a dedicated slice;
6. the Plaza/Platform route is a content migration, not a UI shortcut;
7. animation follows static correctness;
8. verification/evidence closes every major slice.

---

# 12. Verification plan

Status: **COMPLETE — REGIONAL ACCEPTANCE MATRIX LOCKED**

## 12.1 Documentation verification

Before implementation:
- all referenced documents exist;
- no contradictory active authority remains unmarked;
- asset IDs resolve or are explicitly missing;
- planned/current/refinement states are distinct;
- world/gameplay unknowns remain labeled.

## 12.2 Engine verification

For runtime changes:
- Python unit/regression suite;
- content validation;
- save/load tests;
- route/discovery tests;
- actor projection privacy tests;
- equipment/prop state tests;
- hidden-state redaction tests.

Historical passing counts do not prove a new head.

## 12.3 Android verification

For UI changes:
- Android unit tests;
- instrumentation compile;
- debug APK assembly;
- package/resource checks;
- representative emulator startup;
- interaction smoke;
- screenshot capture.

## 12.4 Story-specific QA

Required cases:
- no actor;
- one actor;
- multiple actors;
- focused actor changes;
- missing portrait fallback;
- missing room sprite fallback;
- blackout;
- Trace FX;
- long narrative;
- many choices;
- disabled choice;
- reduced motion;
- resource changes.

## 12.5 Map-specific QA

Required cases:
- undiscovered node;
- discovered current node;
- reachable node;
- unavailable node;
- selected node;
- travel confirmation/action;
- post-travel current-location update;
- missing preview;
- route connector after migration;
- touch targets at phone width.

## 12.6 Pixel-art QA

For every production asset:
- source-native size;
- nearest-neighbor display;
- no anti-aliasing/smoothing;
- scale consistency;
- perspective consistency;
- lighting/material compatibility;
- actor contrast;
- panel-safe composition;
- overlay compatibility;
- provenance.

## 12.7 State/privacy QA

Must prove:
- hidden NPC data remains hidden;
- hidden destinations remain hidden;
- UI does not derive actor presence from raw flags;
- base art does not reveal unavailable route;
- future quest state is not exposed;
- fallback art does not imply false state.

## 12.8 Performance QA

Observe:
- startup;
- room switch;
- map open/selection;
- panel focus switch;
- animation;
- memory pressure/fallback;
- no continuous off-screen loops;
- low-end emulator behavior where available.

## 12.9 Physical handset gate

Galaxy A03 testing is separate.

Record:
- APK SHA;
- install success;
- cold start;
- current-room render;
- map;
- Story choices;
- save/load;
- actor panels;
- performance;
- orientation if supported;
- screenshots/photos where useful.

Never infer this gate from emulator evidence.

## 12.10 Exact-head evidence record

Every verified implementation slice records:
- repository;
- branch;
- commit SHA;
- base SHA;
- relevant PR;
- workflow run ID;
- job results;
- artifact IDs;
- APK SHA-256;
- screenshot artifact;
- tests;
- known gaps.

## 12.11 Step 12 locked decisions

1. docs, engine, Android, pixel, privacy, performance and handset each have separate evidence.
2. exact-head evidence is mandatory.
3. screenshot QA is part of visual acceptance.
4. emulator and physical handset evidence are not interchangeable.
5. fallback/privacy cases are first-class tests.
6. “builds” is not equivalent to “finished.”

---

# 13. Migration / replacement / removal plan

Status: **COMPLETE — REGIONAL KEEP/EXTEND/REWORK/REPLACE/REMOVE CONTRACT LOCKED**

This is the Gate Twelve regional migration layer. The final application-wide disposition remains governed by the APK reconstruction documents.

## 13.1 KEEP

Preserve unless later explicit migration proves otherwise:
- stable Gate Twelve location IDs;
- quest/item/NPC/knowledge stable IDs;
- authoritative Python/domain ownership;
- player-safe projection principle;
- versioned save/persistence boundary;
- authored route legality;
- 256x144 Gate Twelve presentation scaffold;
- 128x64 narrative scene source-native contract;
- 32x48 character paper-doll rig;
- 64x64 portrait target;
- equipment slot semantics;
- map semantic node anchors;
- nearest-neighbor/source-native pixel policy;
- existing verified tests/evidence as historical exact-head records.

## 13.2 EXTEND

Extend:
- player-safe projection with room actors/visual state;
- asset manifests/provenance;
- actor/portrait mappings;
- location-detail/arrival-preview packets;
- world hierarchy around Gate Twelve;
- state-binding registry;
- visual QA/evidence metadata;
- accessibility/reduced-motion support.

## 13.3 REWORK

Expected substantial rework:
- Story/current-location layout;
- Map visual presentation;
- Character visual presentation;
- actor focus/panel presentation;
- scene composition host;
- hard-coded actor placement once safe actor projection exists;
- current asset catalog organization if scale proves it unmaintainable;
- navigation chrome if it obstructs the primary world experience.

Rework means the responsibility remains but structure/presentation changes.

## 13.4 REPLACE

Replacement candidates once verified alternatives exist:
- generic/provisional Jack visuals;
- flat geometric scene art where approved source-native art replaces it;
- flat geometric district-map blocks where authored modular map art replaces them;
- incorrect/duplicate raster exports;
- scene-ID-specific actor heuristics superseded by projected actor presence;
- duplicated flattened blackout/Trace scenes where a base+overlay stack accurately represents the same physical room.

## 13.5 REMOVE

Remove only after consumer audit, replacement and verification:
- dead placeholder assets;
- duplicate asset IDs/aliases after migration;
- obsolete geometric renderer branches for locations fully covered by approved art;
- stale UI components superseded by the final Story/Map composition;
- unused debug-only presentation;
- deprecated hard-coded visual-state rules;
- obsolete tests that assert intentionally removed presentation rather than authoritative behavior.

Removal does not erase Git history or provenance documents.

## 13.6 ARCHIVE

Archive/reference-only:
- superseded concept boards;
- rejected external-reference adaptations;
- historical branch/PR screenshots;
- old V6 status reports outside their exact evidence role;
- superseded asset masters.

Archive means “not active authority,” not “delete evidence.”

## 13.7 Intentional breakage policy

Presentation code may be intentionally broken/replaced when:
- the replacement contract is documented;
- old consumers are known;
- authoritative state is preserved;
- migration can be tested;
- rollback is possible through Git.

High-risk boundaries require stronger gates:
- save schema;
- stable IDs;
- quest logic;
- stat/progression schema;
- inventory/equipment semantics;
- hidden-state projection.

Those are not changed merely to simplify UI work.

## 13.8 Save/content migration rule

If a later system change affects durable state:
1. document old schema;
2. document new schema;
3. map IDs/fields;
4. provide migration or explicitly document incompatibility;
5. test old-save upgrade;
6. test new-save round trip;
7. reject unsupported versions safely;
8. preserve backup/export strategy where appropriate.

## 13.9 Gate Twelve connector migration

The planned Plaza <-> Platform Nine route requires:
- content graph update;
- travel cost;
- discovery/unlock semantics;
- route validation;
- map projection;
- tests;
- migration review if existing saves persist discovered/reachable graph state.

It is not an art-only change.

## 13.10 Step 13 locked decisions

1. stable IDs/state authority are KEEP by default.
2. Story/Map/Character presentation are authorized for major rework.
3. generic/geometric visuals may be replaced after verified art exists.
4. projected actor presence replaces hidden/scene heuristic logic.
5. deletions occur only after replacement and consumer audit.
6. save/content breaks require explicit migration.
7. Git/history/provenance are preserved even when active assets are superseded.

---

# 14. Execution handoff

Status: **COMPLETE — GATE TWELVE DOCUMENTATION PHASE 1–14 FINISHED**

Gate Twelve now has a complete first-pass region-to-implementation plan.

This does **not** mean the region is fully implemented or visually finished.

## 14.1 Required reading order for execution

Before Gate Twelve implementation:
1. `README.md`;
2. `AGENTS.md`;
3. `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`;
4. `docs/MASTER_DIRECTIVE_EXECUTION_BREAKDOWN.md`;
5. `docs/EXISTING_STATE_REWORK_DECISION_MATRIX.md`;
6. `docs/assets/GATE_TWELVE_REGION_MASTER_PLAN.md`;
7. `docs/assets/GATE_TWELVE_ASSET_STATUS_AND_PRODUCTION_MATRIX.md`;
8. `docs/assets/PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md`;
9. `docs/assets/ROOM_ACTOR_PANEL_OVERLAY_REUSE_STANDARD.md`;
10. `docs/android/APPLICATION_UX_MASTER_PLAN.md`;
11. relevant source/tests;
12. live PR/branch/CI state.

Live source/evidence overrides stale planning text and must cause documentation correction.

## 14.2 First implementation action

Do **not** start by drawing every missing asset.

First implementation action:

**Exact current-state visual/runtime reconciliation.**

Record:
- current intended implementation parent/head;
- Story consumer;
- Map consumer;
- current actor-placement implementation;
- current player-safe projection fields;
- current visual catalogs/manifests;
- Jack/Tamsin/courier asset provenance;
- open PR refinements and exact heads;
- exact tests/CI baseline.

Then update:
- `docs/EXISTING_STATE_REWORK_DECISION_MATRIX.md`;
- `docs/assets/GATE_TWELVE_ASSET_STATUS_AND_PRODUCTION_MATRIX.md`.

## 14.3 First code-bearing slice after reconciliation

Preferred first code-bearing slice:

**player-safe room-actor projection contract**, if live source confirms it is still absent.

Acceptance:
- stable actor IDs;
- current-room presence;
- visible pose/expression/outfit fields only as needed;
- no hidden goals/memory;
- Android consumes projection;
- existing Story behavior remains functional;
- tests cover absent/one/multiple actors;
- exact-head verification.

If live source already has an equivalent safe actor projection, do not duplicate it. Move to the next unsatisfied dependency.

## 14.4 Next implementation slices

After actor projection:
1. Story layered host + actor panel;
2. Jack canonical player visual integration;
3. authored Gate Twelve map composition while preserving map semantics;
4. missing current-region asset reconciliation/production;
5. state overlays;
6. Plaza <-> Platform Nine content migration after travel/unlock decision;
7. bounded animation;
8. full regional regression/performance;
9. physical handset gate.

## 14.5 Decisions still intentionally open

Gate Twelve documentation does not fabricate answers for:
- Plaza <-> Platform Nine travel minutes;
- connector discovery/unlock timing;
- parent city/world coordinates;
- exact future Quiet Stair destination;
- exact deeper Service Tunnel destination;
- final global navigation count;
- global world-map zoom/LOD implementation;
- final portrait panel dimensions at every device width;
- final asset-cache implementation;
- which open refinement PRs are promoted after exact-head comparison;
- final Jack turnaround pixels before source production/approval;
- large-world NPC/city/kingdom population records.

These must be decided in the relevant parent system/world documents or exact implementation audit.

## 14.6 Standing permissions

Within routine reversible project engineering, work may:
- create/rework/remove presentation code;
- create original assets;
- migrate visual catalogs;
- add tests/tooling;
- create branches/commits;
- replace weak provisional art;
- redesign Android screens;
- expand engine projections safely;
- build original world/system content under documented schemas.

Standing restrictions remain:
- no silent `main` promotion;
- no force-push/shared-history rewrite;
- no hidden-state leaks;
- no silent stable-ID/save break;
- no copyrighted map/art/character/UI copying;
- no unrelated repository treated as authority without migration record;
- no Code Assistant workflow previously prohibited;
- no physical-device claim from emulator evidence.

## 14.7 Documentation result

Gate Twelve Steps 1–14 now define:
- authority;
- spatial hierarchy;
- circulation;
- per-zone function;
- geometry;
- materials;
- asset inventory;
- application UX;
- state layers;
- performance/loading;
- implementation order;
- verification;
- migration/removal;
- execution handoff.

This makes Gate Twelve the first complete proof-region planning packet for the wider documentation program.

## 14.8 Next repository-level priority

After this regional documentation packet:
1. perform exact existing-state repository audit;
2. produce reproducible documentation/world/asset inventory;
3. reconcile Gate Twelve open visual/runtime branches;
4. begin bounded implementation only where contracts are satisfied;
5. continue controlled population of world catalogs from the already-created geography/political/settlement/ecosystem/beast/population/balance schemas;
6. keep final APK reconstruction late-stage until domain contracts and migrations are mature.

---

# Continuity footnote / next-session handoff

**Gate Twelve documentation:** Steps 1–14 COMPLETE on the master documentation branch.

**Current repository priority:** `jbob-coder/Text-rpg-game`.

**Current program branch:** `docs/master-game-development-program`.

**Implementation status:** documentation complete does not mean runtime implementation complete.

**Next exact action:** audit the live implementation heads and reconcile current code/assets against the complete Gate Twelve contract before creating or deleting runtime content.

**Key non-negotiables:** preserve authoritative engine ownership, player-safe projection, stable IDs/save compatibility unless explicitly migrated, source-native pixel-art rules, provenance, exact-head verification, and separation between emulator and physical handset evidence.

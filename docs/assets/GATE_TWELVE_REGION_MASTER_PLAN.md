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

# 3. Planned authoring sequence

The remaining master plan will be completed in this order:

1. **Authority and design mandate** — COMPLETE.
2. **Spatial hierarchy** — COMPLETE.
3. **Circulation** — primary/secondary routes, player flow, landmark visibility.
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

**Completed:** Step 1 — authority and design mandate; Step 2 — spatial hierarchy.

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

**Next unfinished step:** Step 3 — define circulation: primary/secondary routes, player flow, transition pacing, route hierarchy, and landmark visibility. Step 3 must evaluate the proposed `DISTRICT_PLAZA <-> PLATFORM_NINE` connector without adding it to gameplay yet.

**Do not skip directly to asset production before Steps 3–5 are documented.**

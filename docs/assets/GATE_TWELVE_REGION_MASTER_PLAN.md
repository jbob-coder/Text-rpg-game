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

# 2. Planned authoring sequence

The remaining master plan will be completed in this order:

1. **Authority and design mandate** — COMPLETE.
2. **Spatial hierarchy** — macrozones, subzones, adjacency, entrances/exits.
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

**Completed:** Step 1 — authority and design mandate.

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

**Next unfinished step:** Step 2 — define the spatial hierarchy (macrozones + subzones + adjacency + world-facing entrances/exits) using the nine existing named locations and the three confirmed spatial bands.

**Do not skip directly to asset production before Step 2–5 are documented.**

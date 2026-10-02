# THE GAME — Pixel Art Production & Reuse Ledger

Status: **ACTIVE / PRODUCTION AUTHORITY COMPANION**  
Parent: `PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md`  
Region proof: `GATE_TWELVE_REGION_MASTER_PLAN.md`

## 1. Purpose

This ledger answers:
- what visual material already exists;
- what stage it is in;
- what must still be created;
- how room/environment/player/NPC/panel art composes;
- what may be overlaid or reused;
- what must never be reused because identity, perspective, scale, material, or state semantics would be wrong.

## 2. Production stages

Use these exact stage labels:
- PLANNED
- BRIEF_LOCKED
- REFERENCE_SELECTED
- SOURCE_MASTER_PRESENT
- RASTER_PRESENT
- CODE_PRESENT
- INTEGRATED
- OPEN_PR_REFINEMENT
- QA_PENDING
- VERIFIED
- CANON_APPROVED
- DEFERRED_INTEGRATION
- SUPERSEDED
- REJECTED

One asset may have several statuses in different branches. Record branch/HEAD when that distinction matters.

## 3. Runtime composition stack

From back to front:

1. environment/base scene;
2. structural modules;
3. permanent props;
4. ambient decals;
5. room actors;
6. actor equipment/held-object layers;
7. player-safe state overlays;
8. transient FX;
9. UI focus/panel layer;
10. text/interaction layer.

Rules:
- base art never owns reachability;
- overlays never invent hidden state;
- actor panels never decide actor presence;
- UI text is not baked into world art unless it is intentionally large environmental signage;
- state-specific effects remain separable when architecture is unchanged.

## 4. Compatibility signature for reuse

An asset can be reused without looking out of place only when the consuming scene is compatible in:
- native pixel density;
- perspective/camera;
- scale;
- anchor/pivot;
- palette/value range;
- light direction;
- material family;
- outline/edge treatment;
- environment wear;
- semantic role;
- state meaning;
- z-order;
- actor contrast;
- animation cadence if animated.

If one of these mismatches, adapt the asset or create a variant. Do not stretch/smooth/recolor blindly.

## 5. Text-art and overlay reuse

### World text
Use only when:
- large enough to read at native scale;
- actually exists in-world;
- authored for the location.

Preferred:
- arrows;
- numbers;
- symbols;
- plates;
- route icons.

Avoid:
- dense pseudo-text;
- UI paragraphs painted into a scene;
- random glyph noise.

### UI text
Keep separate from pixel world art:
- dialogue;
- narrative;
- item names;
- stats;
- quest text;
- actor details;
- tooltips.

### Overlay reuse
Reusable overlays are appropriate when:
- architecture stays the same;
- the event/state only changes lighting, damage, power, weather, Trace response, emergency status, or another bounded visual layer.

Create a new base scene when:
- geometry changes;
- major objects move;
- space function changes;
- perspective changes;
- permanent damage materially changes silhouette.

## 6. Character in-room model

A named character in a room may require three visual representations:

### A. Room actor
- full-body or scene-scale sprite;
- physically anchored to the environment;
- displays pose/equipment/state visible in-world.

### B. Character portrait
- 64x64 canonical identity;
- expression/emotion variant;
- must match hair, skin, marks, visible head/neck equipment.

### C. Focus panel
May show only player-safe:
- name;
- portrait;
- role/faction if known;
- relationship/status if intentionally exposed;
- dialogue/interactions;
- visible condition.

Presence source:
a player-safe actor projection from the engine.

Compose must never infer presence by reading hidden story flags.

## 7. Player / Jack production list

### Existing foundations
- 32x48 paper-doll rig;
- current player base/silhouette on visual branches;
- equipment slot/z-order contract;
- current starting equipment layers/icons;
- approved Jack external visual reference recorded in repository documentation.

### Still required for final identity
- Jack front production master;
- back master;
- left/right directional masters;
- three-quarter/reference turnaround as needed for authoring;
- 64x64 portrait neutral;
- focused;
- concerned;
- hurt;
- determined;
- surprised or final approved emotion set;
- movement frames consumed by gameplay;
- crouch/interaction/combat poses only when mechanics consume them;
- held-object anchors;
- final equipment alignment passes;
- injury/status overlays;
- portrait/equipment synchronization.

The approved reference is input, not a runtime sprite.

## 8. Tamsin production list

Existing:
- authored canonical identity;
- room-actor/front implementation evidence;
- outfit/satchel/mark specifications.

Required/reconciliation:
- confirm source master provenance;
- full turnaround;
- directional room actors if needed;
- 64x64 portrait family;
- diagnostic-reader pose;
- emotion variants;
- equipment/tool anchors;
- manifest/code status reconciliation.

## 9. Supporting actor production

Courier/current opening actor:
- preserve only with provenance;
- document identity level;
- decide whether recurring or scene-specific;
- create portrait only if the UI needs focused dialogue/identity;
- do not promote a temporary silhouette into a canonical recurring character without design authority.

Future NPCs:
- shared rig allowed;
- shared generic clothing modules allowed when role-appropriate;
- face/hair/identity marks are separate;
- role uniforms may be shared through exact faction/profession contracts.

## 10. Current Gate Twelve visual inventory

Current documentation/branches indicate these families already exist in some stage:
- player paper-doll base;
- Depot Jacket;
- Work Gloves;
- Signal Ring;
- Courier Neck Tag;
- Maintenance Seal;
- Dead Relay and relay-state visuals;
- nine named-location scene families;
- Gate Twelve/Service Tunnel/Trace state overlays;
- infrastructure props;
- depot door/signage/ambient decal families;
- maintenance corridor connector;
- municipal archive exterior;
- municipal infrastructure 32x32 tile atlas;
- map current/discovered/reachable/unavailable/player markers;
- nav/resource/quest icons;
- Trace FX families;
- Gate Twelve district map master;
- room-actor system;
- Service Tunnel refined scene candidate;
- Quiet Stair refined scene candidate;
- Service Tunnel ambient animation candidate.

Do not call all of these CANON_APPROVED. Their exact status belongs in manifests and the Gate Twelve asset status matrix.

## 11. Known high-value missing/reconciliation items

Tracked gaps include:
- Jack final production identity set;
- Tamsin full turnaround/portrait set;
- courier actor provenance;
- `PLATFORM_NINE_EVACUATED_SCENE`;
- `DISTRICT_ARCHIVE_TERMINAL_CLOSEUP`;
- `WORKSHOP_ROW_RUMOR_SCENE`;
- `PROP_DIAGNOSTIC_READER`;
- `FX_TRACE_STRAIN`;
- reusable `EMERGENCY_LIGHT_OVERLAY` if no current equivalent satisfies it;
- reusable `BLACKOUT_SHADOW_OVERLAY` if no current equivalent satisfies it;
- `UI_MAP_TRAVEL_TRANSITION`;
- relay intact/icon naming reconciliation;
- actor panel assets/data contract;
- world-scale building/tile/prop sets after world schemas.

## 12. Gate Twelve per-area packet requirements

### Depot Plaza
Need:
- civic ground modules;
- depot-facing landmark;
- notice/public-context focal point;
- surface-world expansion edge;
- restrained emergency-state overlay;
- optional public NPC actor anchors.

### Workshop Row
Need:
- workshop facades;
- benches/tool clutter;
- repair/salvage prop family;
- worker actor anchors;
- rumor/state overlay only if a safe projected state exists.

### Municipal Archive
Need:
- archive facade/interior identity;
- shelves/records/terminal props;
- terminal closeup if authored;
- clerk/actor anchors if later used;
- backup-power state layer.

### Platform Nine
Need:
- platform/depot scene master;
- evacuation signage;
- depot-door props;
- workbench adjacency;
- actor anchors for Tamsin/courier/player;
- evacuated state only with safe state binding.

### Relay Workbench
Need:
- focused workbench prop;
- relay state variants;
- diagnostic reader;
- task light;
- actor/tool pose anchors.

### Gate Twelve
Need:
- gate base;
- door/panel elements;
- Echo/state overlays;
- threshold route cues;
- no hidden destination revelation.

### Quiet Stair
Need:
- stair/landing modules;
- rail/signage;
- sparse practical light;
- external continuation implication;
- no invented destination.

### Service Tunnel
Need:
- corridor modules;
- ribs/pipes/cables;
- infrastructure atlas details;
- ambient fan/panel/drip animation where verified;
- aftershock/Trace overlays;
- deeper continuation implication.

### Trace Chamber
Need:
- controlled chamber shell;
- apparatus;
- training/research props;
- bounded Trace FX;
- player/NPC training pose anchors;
- no generic all-skill training visuals.

## 13. Map pixel-art model

The map is modular, not a flattened illustration.

Layers:
1. terrain/material field;
2. region/structure silhouettes;
3. roads/routes;
4. landmark sprites/modules;
5. environmental detail;
6. player-safe route/state overlays;
7. markers;
8. selection/current-player overlay;
9. UI labels/detail panel.

Benefits:
- routes can change without repainting geography;
- discovery can change without duplicating base art;
- world regions can share compatible modules;
- a selected location can receive richer arrival/detail art.

## 14. Reuse classes

- **R0 Exact reuse** — same asset, same role, same grid.
- **R1 Palette/material variant** — same geometry, local material adaptation.
- **R2 Structural kit reuse** — doors/walls/tiles/props recomposed.
- **R3 Animation reuse** — same motion rig, character/prop-specific art.
- **R4 Semantic family reuse** — same UI role, different icon/art.
- **NO-REUSE** — identity-specific, unique landmark, story-state-specific, incompatible perspective.

Every production packet should declare its reuse class.

## 15. Visual QA gates

Before CANON_APPROVED:
- native-scale inspection;
- nearest-neighbor inspection;
- phone screenshot;
- actor/background silhouette check;
- palette/material coherence;
- overlay state check;
- hidden-state safety check;
- branch/HEAD provenance;
- manifest update;
- physical-device review when required.

## 16. Production order

1. reconcile current assets/status;
2. finish Jack/Tamsin identity foundation;
3. finish Gate Twelve missing state/prop assets;
4. actor/panel contract;
5. improve weak area masters;
6. bounded animation;
7. world schema;
8. world-scale kits;
9. settlement-specific landmarks;
10. NPC population art families;
11. combat-specific character/effect art after combat contract.

This ledger must be updated rather than replaced when new batches are created.

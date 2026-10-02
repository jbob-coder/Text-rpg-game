# World canon decision queue

Parent: [World master index](WORLD_DEVELOPMENT_MASTER_INDEX.md).
Scope: baseline program branch at `4d596bcd27b6e2f8ef9ce3a93b9dab22f5f4812e`.
These are repository decisions and proposals, not imported Godot/MVS lore.

## 1. Established versus provisional

The playable content identifies itself as `provisional_canon`. Existing named places and relationships are confirmed implementation facts at this baseline; that does not freeze every story detail as final world canon.

| Area ID | Display name | Current map x,y | Existing identity | Creation needed |
| --- | --- | --- | --- | --- |
| PLATFORM_NINE | Platform Nine | 18,36 | Municipal tram-depot evacuation platform | Area packet, actor anchors, blackout variants |
| RELAY_WORKBENCH | Relay Workbench | 34,31 | Maintenance bench / dead relay investigation | Relay layers, prop anchors, interaction panel |
| GATE_TWELVE | Service Gate Twelve | 53,48 | Sealed maintenance entrance below depot | Threshold/access variants without baked-in legality |
| SERVICE_TUNNEL | Service Tunnel | 70,61 | Restricted infrastructure under evacuation route | Reconcile newer art, fan/panel/drip layers |
| EVAC_STAIR | Quiet Stair | 40,70 | Alternate maintenance egress | Reconcile later stair art, actor/occlusion anchors |
| TRACE_CHAMBER | Trace Chamber | 82,39 | Trace reproduction/stabilization space | Progression-state overlays, safe research panel |
| DISTRICT_PLAZA | Depot Plaza | 48,18 | Public temporary meeting point | Arrival facade, public crowd/presence contract |
| DISTRICT_ARCHIVE | Municipal Archive | 66,16 | Records annex on backup power | Exterior/interior packet, records interactions |
| WORKSHOP_ROW | Workshop Row | 29,16 | Repair shops / municipal contractors | Modular frontage, doors, authored service contracts |

Coordinates are the exact `world_map.nodes` presentation/map values in `content/vertical_slice_01.json`. They are not meters, world positions, tactical cells, or a finalized scale conversion.

Eight authored edge records exist: Platform–Workbench, Platform–Gate, Platform–Stair, Gate–Tunnel, Gate–Chamber, Tunnel–Chamber, Plaza–Archive (8 minutes), Plaza–Workshop (7 minutes). These are edge records; directionality/reachability remain engine rules. The content graph has two undirected structural components. This is an audit observation, not automatic authority to add a connector. The proposed Plaza–Platform link needs an explicit route/content decision and quest/save/map checks.

## 2. Decision dependency queue

| Decision ID | Open decision | Safe current position | Depends on / unblocks | Required output |
| --- | --- | --- | --- | --- |
| WD-001 | World identity / parent settlement | Gate Twelve remains parentless at macro scale | Unblocks city/geography/political naming | Original canon record + scope |
| WD-002 | Technology and world physics | Local tram/maintenance infrastructure is evidenced; global baseline unknown | WD-001; ecology/resources/combat | Technology limits and everyday examples |
| WD-003 | Regional coordinate scale | Keep existing map coordinates separate | WD-001; travel/settlement maps | Units, origin, bounds, transforms |
| WD-004 | Political authority and borders | No kingdom fabricated | WD-001/002; law/citizenship/economy | Governance and institutions packet |
| WD-005 | Gate Twelve route connector | No silent graph rewrite | Existing quests/discovery/travel; WD-003 | Before/after route map and migration |
| WD-006 | Climate/resources/ecosystems | Schema exists; regional distribution unknown | WD-002/003; beasts/settlements | Regional ecological rationale |
| WD-007 | Beast taxonomy and populations | No imported novel/game monsters | WD-006; combat/loot | Original species + habitat records |
| WD-008 | Citizen status and discrimination | Institutional, cultural, individual layers separate | WD-004; NPC/social/access | Rights, causes, regional variation, agency |
| WD-009 | Classes / ranks / mastery | Current attributes preserved; final trees unknown | Progression master; WD-008 | Distinct namespaces + prerequisites |
| WD-010 | Tactical rules and regional danger | No invented enemy numbers | WD-007/009; items/equipment | Calibration encounters + escape options |
| WD-011 | Economy / loot / accessories | Existing item IDs retained | WD-006/010; legal ownership | Source/sink/provenance model |
| WD-012 | NPC schedules / recurring adversaries | Current NPC memory retained | WD-004/008/010; originality review | Deterministic schedule and aftermath rules |

Recommended first authoring scope: one proposed Gate Twelve parent settlement with infrastructure, water/food, routes, law, resource dependencies and adjacent districts. Mark it PROPOSED until accepted; do not attach arbitrary world-scale coordinates or thousands of settlements before scale decisions.

## 3. Area expansion unit

Each populated area must link place -> parent -> routes -> activities -> NPC presence -> resources/hazards -> items/loot -> progression band -> tactical spaces -> visual packet -> consuming screen -> tests. Missing links stay explicit UNKNOWN. At world scale, political control is a relation, not necessarily spatial containment: disputed/overlapping control must not force duplicate place IDs.

A batch is accepted only after duplicate IDs, missing parents/endpoints, invalid coordinate spaces, unintended disconnected routes, resource dependencies, ecological rationale and hidden-state projections are checked. Numerical balance requires actual rules fixtures; plausible prose is insufficient.

# Gate Twelve parent-world proposal

Status: **PROPOSAL / OWNER CANON DECISION REQUIRED**  
Parent: `docs/world/WORLD_CANON_DECISION_QUEUE.md`  
Primary dependencies: WD-001, WD-003, WD-004, WD-005, WD-006  
Repository: `jbob-coder/Text-rpg-game`

## 1. Purpose

This packet proposes the minimum parent geography and civic context needed to place Gate Twelve inside a coherent larger world without pretending the proposal is already canon.

It intentionally does **not** define the whole world, a kingdom, global technology limits, final beast ecology, exact population, exact distances, or global politics. Existing Gate Twelve local IDs, nine map nodes, eight route records and 256x144 W3 presentation geometry remain unchanged.

## 2. Evidence that constrains the proposal

Existing implemented/local facts support:

- a municipal tram/depot function at Platform Nine;
- maintenance infrastructure at Relay Workbench, Gate Twelve, Service Tunnel and Quiet Stair;
- a public Depot Plaza;
- a Municipal Archive/records annex;
- Workshop Row with repair shops / municipal contractors;
- local emergency/evacuation context;
- two currently disconnected structural route components in authored content;
- current local map coordinates are presentation values, not meters.

These facts justify an urban civic/transit parent. They do not prove a sovereign state, continent, currency, world scale, species model or climate.

## 3. Proposed containment

The following names are **working names**, not locked canon.

| Layer | Proposed ID | Working name | Proposed role | Canon state |
| --- | --- | --- | --- | --- |
| WORLD | `WORLD_PRIMARY_01` | unnamed | global container | name intentionally open |
| MACROREGION | `MACROREGION_LOWLAND_01` | unnamed lowland belt | broad geographic parent | structure only |
| REGION | `REGION_ALDER_BASIN_01` | Alder Basin | temperate low-basin transport region | PROPOSED |
| POLITICAL/ADMIN | `ADMIN_ARDEN_MUNICIPAL_01` | Arden Municipal Authority | local civic administration | PROPOSED local authority only |
| SETTLEMENT | `SETTLEMENT_ARDEN_CROSSING_01` | Arden Crossing | medium transit/repair city | PROPOSED |
| DISTRICT | existing Gate Twelve proof region | Gate Twelve District | depot/maintenance/civic edge district | existing local content; parent proposed |

The higher-order sovereign polity remains deliberately unresolved. The municipal authority can explain local depot, archive, contractor, emergency and maintenance institutions without fabricating a kingdom/state before WD-004 is approved.

## 4. Settlement role proposal

**Arden Crossing** is proposed as a medium city built around an old regional transport junction rather than a megacity.

Primary functions:

- passenger and municipal transit;
- repair/maintenance labor;
- records/administration;
- contractor workshops;
- storage/logistics;
- ordinary residential/commercial districts outside the current proof region.

Gate Twelve sits at the infrastructure-heavy edge of the city core where public transit, workshops and below-grade maintenance systems meet. This preserves the current local atmosphere without forcing the entire city to look industrial.

## 5. Terrain and climate proposal

Proposed regional physical logic:

- broad shallow basin / low valley;
- low ridges outside the settlement footprint;
- reliable surface water somewhere in the parent region, exact river/lake alignment still open;
- cool-to-mild temperate conditions;
- regular rainfall sufficient to justify drainage, covered maintenance access and weather-sensitive infrastructure;
- no permanent snow/desert/tropical condition locked by this proposal.

This is a worldbuilding candidate, not evidence from existing runtime art. It should be accepted, modified or rejected before ecology/resource population.

## 6. Coordinate policy

Do **not** convert current Gate Twelve node values such as `PLATFORM_NINE (18,36)` into meters.

Proposed coordinate separation:

- W1 region: abstract regional coordinate grid; units remain unset until WD-003.
- W2 settlement: city/district placement grid; origin and unit remain unset until the first Arden Crossing settlement map is approved.
- W3 Gate Twelve: retain existing 256x144 presentation scaffold and existing node coordinates exactly.
- W4 tactical: separate encounter geometry; no automatic transform from W3.

A later W2->W3 transform must be explicit and versioned. Until then, Gate Twelve can be parented by ID without inventing physical distance.

## 7. Parent-facing route stubs

The current eight local route records remain untouched.

Proposed future parent links, all **UNIMPLEMENTED**:

| Proposed route | Local anchor | Parent destination concept | Access |
| --- | --- | --- | --- |
| `ROUTE_GT_SURFACE_TRANSIT_01` | `DISTRICT_PLAZA` | city surface transit/concourse network | public when normal |
| `ROUTE_GT_WORKSHOP_STREET_01` | `WORKSHOP_ROW` | contractor/service street network | public/service mix |
| `ROUTE_GT_UPPER_EGRESS_01` | `EVAC_STAIR` | upper maintenance street / emergency egress | restricted/state-dependent |
| `ROUTE_GT_DEEP_UTILITY_01` | `SERVICE_TUNNEL` | deeper utility infrastructure | restricted; destination intentionally open |

No travel minutes, distance, toll, permit, encounter rate or discovery timing is assigned here.

The proposed `DISTRICT_PLAZA <-> PLATFORM_NINE` local connector remains a separate WD-005 decision. Do not use the new parent stubs to bypass that migration.

## 8. Political ownership proposal

Local authority only:

- Arden Municipal Authority owns/operates or regulates the civic transit/depot infrastructure and Municipal Archive.
- Workshop Row may contain private contractors operating under municipal leases/contracts.
- Maintenance tunnels and Gate Twelve can have restricted access without implying military ownership.
- Local security/emergency services may exist as municipal institutions.

Not decided:

- sovereign country/state;
- national borders;
- citizenship law;
- military hierarchy;
- currency;
- taxation;
- discrimination policy;
- inter-state conflict.

This gives current places an institutional owner while keeping WD-004 open at higher scale.

## 9. Economy/resource implications

Safe local implications if the proposal is accepted:

- repair labor and municipal contracting are plausible;
- salvage/maintenance materials can have provenance through infrastructure and workshops;
- transit/logistics employment is plausible;
- archive/records services are civic, not generic shops.

Do not infer:

- crystal economy;
- beast-derived materials;
- black market;
- global currency;
- specific wages/prices;
- resource deposits.

Those require economy/ecology decisions.

## 10. Visual implications

If accepted, Gate Twelve area packets may safely plan for:

- weather-capable exterior overlays at Depot Plaza and Workshop Row;
- drainage/wear language in service infrastructure;
- surface-vs-below-grade lighting distinction;
- municipal signage family shared across depot/archive/maintenance spaces;
- contractor variation within Workshop Row;
- reserved outward-facing street/transit edges without drawing unreachable final districts into current art.

The proposal does not authorize new final city panoramas or population art.

## 11. What this proposal would unblock

After owner/canon approval or revision:

- WD-001 parent settlement identity;
- a bounded WD-003 settlement-coordinate packet;
- local portion of WD-004 institutional ownership;
- ecology/resource design for the parent region;
- settlement district catalog expansion;
- area-packet anchoring for the nine Gate Twelve locations;
- later NPC/service population with clear institutional context.

It does **not** by itself unblock global mass generation, final world politics, final route travel times, beast taxonomy or tactical balance.

## 12. Decision checklist

The owner/canon pass needs explicit decisions on:

1. accept/change/reject working settlement name `Arden Crossing`;
2. accept/change/reject working region name `Alder Basin`;
3. accept/change/reject basin/temperate/rainfall physical logic;
4. accept/change/reject municipal parent authority model;
5. decide whether Gate Twelve is central-city, inner-edge, or outer-edge infrastructure;
6. decide whether the proposed four parent-facing route stubs are valid concepts;
7. decide whether higher sovereign polity remains deferred;
8. only then assign W2 settlement coordinates and begin bounded catalog population.

Until those decisions are made, this file remains a proposal and no downstream document may cite its working names as confirmed canon.

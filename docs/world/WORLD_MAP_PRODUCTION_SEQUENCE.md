# World Map Production Sequence

Status: DOCUMENTED / PROCESS

## Purpose

Build the future world map without generating a giant map first and retrofitting meaning later.

## Sequence

1. World-level hierarchy and political/physical envelopes.
2. Region identities and boundaries.
3. Major settlement placement.
4. Inter-region routes.
5. Settlement functions/economies/ecosystems.
6. District hierarchy.
7. Named locations.
8. Local routes and travel costs.
9. Resource/beast zones.
10. World-state variants.
11. Visual map masters/modules.
12. Runtime projection.
13. Mobile interaction.
14. QA and migration.

## Dependency rule

Do not draw high-detail city blocks before the city/region role is known.

Do not create route art before the route entity and endpoints exist.

Do not create hidden destinations in visible art before discovery rules are decided.

## Detail levels

### L0 — world
Major geography/polities/routes.

### L1 — region
Settlements, ecosystem/resource/threat zones.

### L2 — settlement
Districts, major streets, gates/exits.

### L3 — district
Named locations, local circulation.

### L4 — location
Interior/sub-location/interaction anchors when required.

Each level may use its own coordinate space.

## Pilot reuse

Gate Twelve validates L3 district methodology.

Its lessons should be generalized only after conflicts with the future world architecture are checked.

## Production gate

A map level moves to asset production after:
- entities have stable IDs;
- parent/child hierarchy is clear;
- routes are authored/proposed explicitly;
- coordinate space is declared;
- major gaps are visible;
- visual language is documented.

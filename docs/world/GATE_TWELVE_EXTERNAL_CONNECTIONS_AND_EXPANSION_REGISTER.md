# Gate Twelve External Connections and Expansion Register

Status: **ACTIVE REVIEWABLE CHILD / UNKNOWN-EDGE REGISTER**  
Parents:
- `docs/assets/GATE_TWELVE_REGION_MASTER_PLAN.md`
- `docs/world/WORLD_CANON_DECISION_QUEUE.md`
- `docs/world/GATE_TWELVE_PARENT_WORLD_PROPOSAL.md`
- `docs/world/WORLD_TRAVEL_AND_ROUTES.md`

## 1. Purpose

Own the boundary between the documented Gate Twelve district and the still-unconfirmed larger world.

This file does not confirm the working names or parent geography proposed in the parent-world proposal. It records known outward interfaces and the gate required before they become gameplay routes.

## 2. Current boundary rule

Gate Twelve is the W3 proof district. Existing local location IDs and eight authored route records remain authoritative implementation facts for the current slice.

External expansion must connect through stable destination and route IDs. Decorative map edges never create gameplay reachability.

## 3. Outward interfaces

### GT-EXT-001 — Depot Plaza surface connection

Known:
- Depot Plaza is the public surface-facing hub.
- It is the safest local anchor for a future connection into the parent settlement.

Unknown until canon decision:
destination ID/name; W2 placement; route class; distance/time; discovery/access; world-state variants; final art.

Parent-world proposal interaction:
the proposed `ROUTE_GT_SURFACE_TRANSIT_01` is a candidate route stub, not confirmed canon.

### GT-EXT-002 — Quiet Stair egress

Known:
- Quiet Stair is an alternate maintenance/evacuation branch.

Unknown:
whether it reaches a street, another district, service infrastructure or another parent layer; route identity; access; travel; world-state variants.

Parent-world proposal interaction:
`ROUTE_GT_UPPER_EGRESS_01` remains proposed only.

### GT-EXT-003 — Service Tunnel deeper continuation

Known:
- Service Tunnel points deeper into utility infrastructure.

Unknown:
destination identity/parent; whether it remains inside the settlement/district; travel model; hazards; ecology/resource relation; eventual loading boundary.

Parent-world proposal interaction:
`ROUTE_GT_DEEP_UTILITY_01` remains proposed only.

### GT-EXT-004 — Workshop Row outward street network

Known:
- Workshop Row contains repair/contractor functions and has an outward-facing settlement edge.

Unknown:
the exact W2 street/district destination and route record.

Parent-world proposal interaction:
`ROUTE_GT_WORKSHOP_STREET_01` remains proposed only.

### GT-EXT-005 — Depot Plaza <-> Platform Nine internal bridge

This is **not** an external route.

It remains the separate WD-005 internal graph migration. Do not use an external parent route to bypass its content/save/map decision.

## 4. Route creation gate

An outward interface becomes a gameplay route only when:
1. destination stable entity ID exists;
2. parent hierarchy placement exists;
3. route stable ID exists;
4. endpoint coordinate spaces are declared;
5. directionality is known;
6. discovery/access rules are known;
7. time/distance/cost is defined or explicitly deferred by the route contract;
8. hazards/state variants are defined where required;
9. map/UI representation is specified;
10. persistence/migration impact is assessed;
11. verification exists.

Otherwise it stays UNKNOWN/PROPOSED/BLOCKED.

## 5. Expansion safety

Do not:
- draw a canonical external destination merely to fill a map edge;
- infer sovereign geography from municipal infrastructure;
- turn a proposed parent-world working name into confirmed canon;
- expose hidden destinations before discovery rules permit;
- change existing Gate Twelve local IDs/routes as a shortcut.

## 6. Revision triggers

Revise when:
- owner accepts/revises the parent-world proposal;
- a destination receives a stable ID;
- WD-005 is decided;
- W2/W1 coordinate systems are instantiated;
- travel/discovery rules are locked;
- a route becomes runtime content.

## 7. Acceptance

A future agent must be able to inspect every Gate Twelve expansion edge and distinguish existing local fact from proposed parent-world content without relying on chat memory.

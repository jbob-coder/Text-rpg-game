# THE GAME — Adversary Territory, Movement & Routing Standard

Status: **APPROVED FIRST-PASS V09 CONTRACT / WORLD-ROUTE DEPENDENT**
Parent:
- docs/systems/PERSISTENT_ADVERSARY_WORLD_MEMORY_MASTER_PLAN.md
Related:
- docs/world/WORLD_TRAVEL_AND_ROUTES.md
- docs/systems/NPC_SCHEDULE_PRESENCE_STANDARD.md

## 1. Purpose

Define how recurring adversaries occupy and move through world space so recurrence follows geography, routes, assignments, goals and knowledge rather than teleporting into arbitrary scenes.

## 2. Spatial ownership

Adversary movement uses world location IDs and route authority.

Tactical cells exist only inside an encounter and are not persistent world routes.

## 3. Territory record

Optional adversary territory may define:
- territory_id;
- owning actor/faction;
- included locations/regions;
- access rules;
- patrol/risk weighting;
- known/unknown status;
- start/end provenance;
- contest/control state.

Territory is not required for every adversary.

## 4. Current location

Persistent actor state needs a current world location or an explicit coarse unknown/in-transit state once runtime supports it.

Do not infer location from the last UI scene where the actor was drawn.

## 5. Movement plan

A movement plan may contain:
- origin;
- destination;
- route/path;
- departure time;
- expected arrival;
- reason/goal;
- interruption policy;
- travel mode.

The world route system validates reachability/travel time.

## 6. Off-screen movement

Off-screen travel may resolve abstractly at event/time boundaries.

It does not require rendering every step.

But the actor cannot cross disconnected components without an authored route/migration.

## 7. Pursuit

Pursuit requires:
- adversary goal;
- enough player-location knowledge;
- valid routes;
- lifecycle availability;
- time.

Knowing the player exists is not the same as knowing where the player is.

## 8. Avoidance

An adversary may avoid:
- dangerous locations;
- faction-controlled areas;
- locations associated with a significant memory;
only if their knowledge and goals support that decision.

## 9. Encounter eligibility

A recurring encounter candidate must pass:
- same/compatible location context;
- route/timing;
- lifecycle;
- faction/goal;
- encounter-type constraints;
- cooldown if used.

## 10. Gate Twelve graph rule

The current Gate Twelve map has two disconnected components until a later route migration connects them.

A future adversary cannot move between those components through a route that current world authority does not contain.

Proposed Plaza/Platform connectivity remains proposal-only until implemented.

## 11. Player-safe intel

The player may know:
- last seen location;
- rumored territory;
- public assignment;
- observed pursuit.

Never show exact hidden route or destination without a knowledge source.

## 12. Tests

Required:
- disconnected route rejection;
- valid route travel;
- pursuit requires location knowledge;
- lifecycle blocks travel;
- deterministic route choice;
- off-screen time advancement;
- hidden destination redaction;
- save/load current location/plan when durable state is implemented.

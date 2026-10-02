# THE GAME — World NPC Population Standard

Status: **ACTIVE / WORLD-NPC INTEGRATION STANDARD**  
Parents:
- `docs/world/WORLD_POPULATION_AND_CITIZEN_HIERARCHY.md`
- `docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md`

## 1. Purpose

This standard defines how NPCs are distributed through world geography, how many are simulated at each fidelity tier, how location/schedule state persists, and how named characters connect to visual assets and player-safe panels.

## 2. NPC world record

Each persistent NPC may reference:
- NPC ID;
- home settlement;
- current location;
- workplace/duty location;
- faction/institution;
- social status;
- schedule;
- goals;
- relationships;
- knowledge;
- inventory/resources only when relevant;
- travel routes;
- danger-response behavior;
- visual identity packet;
- room actor asset;
- portrait/focus panel asset;
- tactical actor packet if combat-capable.

## 3. Simulation fidelity

### High
Near player, active quest, combat, or major event.

### Medium
Named recurring NPCs off-screen; schedule/goals update at coarse intervals.

### Low/aggregate
Ordinary supporting population represented statistically until promoted.

This protects mobile performance and save size.

## 4. Schedules

Schedules may include:
- work;
- travel;
- rest;
- meals only if modeled;
- training;
- social contact;
- faction duties;
- event response.

Schedules yield to authored emergency/story state.

## 5. Location consistency

NPCs cannot be in two rooms simultaneously unless the narrative explicitly uses a nonphysical representation.

Player-facing room actors use projected current presence.

## 6. Promotion

A supporting NPC promoted to named recurring status should preserve:
- stable ID/seed where possible;
- known encounters;
- injuries;
- faction;
- relationships;
- prior location history.

## 7. Death/absence

Persistent removal requires state:
- dead;
- missing;
- captured;
- traveling;
- hospitalized/recovering;
- retired;
- relocated.

UI must not silently respawn absent NPCs.

## 8. Persistent rivals

Adversaries use this world-location model plus the social/rival system.

They may travel, recover, change faction standing, or reappear based on authoritative state.

## 9. Visual integration

Every named actor intended for scene display should eventually have:
- room sprite;
- identity blueprint;
- portrait/focus panel;
- state/equipment variants where needed.

The visual layer consumes presence/state; it does not decide NPC simulation.

## 10. Gate Twelve status

Tamsin already has persistent social/story state and a character identity definition.

The full local population and schedule distribution of Gate Twelve remain to be authored after the district's parent settlement and population context are known.

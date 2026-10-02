# THE GAME — World Balance and Level Bands

Status: **ACTIVE / BALANCE STANDARD**  
Parents:
- `docs/world/WORLD_DEVELOPMENT_MASTER_INDEX.md`
- `docs/systems/WORLD_BALANCE_INTEGRATION_PLAN.md`

## 1. Purpose

This standard defines how regions communicate danger, progression expectations, economic reward and escape options without forcing every enemy to scale exactly with the player.

## 2. Balance dimensions

Each region/zone may define:
- environmental danger;
- ordinary civilian baseline;
- law/security strength;
- common hostile threat;
- beast threat;
- elite/unique threat;
- resource hazard;
- travel difficulty;
- equipment availability;
- training availability;
- economic reward;
- recovery/support access;
- escape/avoidance options.

## 3. Objective danger

Preferred principle:
- the world has persistent danger differences;
- the player can encounter areas beyond current capability;
- danger is telegraphed;
- avoidance/escape exists where design supports it;
- progression improves options rather than causing every enemy to magically match the player.

## 4. Band record

Each balance band requires:
- stable band ID;
- intended meaning;
- expected stat/skill/equipment context;
- threat examples from original content;
- reward/resource range;
- typical encounter complexity;
- escape/retreat expectation;
- UI label if any.

Names are not copied from another IP.

## 5. Player progression relation

A zone may be:
- below player capability;
- appropriate;
- challenging;
- severe;
- effectively inaccessible without special preparation.

These are design relations, not necessarily player-facing labels.

## 6. NPC survival logic

High-threat regions need world explanations:
- fortifications;
- patrols;
- safe routes;
- schedules;
- deterrents;
- technology/abilities;
- economic necessity;
- evacuation behavior.

Do not place ordinary settlements inside lethal zones without explaining survival.

## 7. Reward logic

Higher danger may correlate with:
- rare resources;
- strategic routes;
- quest importance;
- valuable beast materials;
- political conflict.

But not every dangerous place must be a loot fountain.

## 8. Tactical integration

Combat encounter packets consume regional balance but also account for:
- actor composition;
- terrain;
- objective;
- surprise;
- cover;
- status;
- retreat.

Do not derive encounter difficulty solely from sum of character levels.

## 9. Gate Twelve status

Gate Twelve has authored stats, resources, Trace progression and current scenes, but no final world-level band has been locked.

Do not retroactively label it with a rank until the global band system is approved.

# Off-Screen Simulation Rules

Status: ACTIVE_CAMPAIGN_PROTOCOL
Created: 2026-09-29

## Objective

Make the world continue to exist when Jack is not looking, without generating arbitrary noise or creating impossible continuity.

## Simulation unit

Off-screen simulation proceeds in bounded steps tied to elapsed live-game time.

For each step:
1. identify clocks allowed to advance;
2. inspect active actors/pressures;
3. choose actions based on goals, resources, knowledge, constraints, and prior events;
4. resolve direct effects;
5. propagate secondary effects;
6. determine whether the player could notice them;
7. persist only meaningful state changes.

## Actor model

Important actors should eventually have stable records containing:
- goal;
- current plan;
- resources;
- constraints;
- allies/enemies;
- knowledge;
- risk tolerance;
- current location or operational region;
- next decision trigger.

Institutions and factions may use the same structure at larger scale.

## Event budget

Do not advance every subsystem every scene.

Prefer:
- 0-2 major off-screen events per meaningful time block;
- several minor state changes only when causally necessary;
- no event simply to force drama.

## Dormant vs active pressures

A pressure is not an event.

Pressure example:
`postwar security anxiety`

Possible events only after causal activation:
- Academy increases screening;
- a faction recruits aggressively;
- a law changes;
- a student is investigated;
- a portal checkpoint closes.

This distinction prevents the repository from confusing story possibilities with things that already happened.

## Consequence horizon

Track consequences as:
- IMMEDIATE — affects current/next scene.
- SHORT — likely within hours/days.
- MEDIUM — weeks/months.
- LONG — months/years or historical arc.

Unresolved consequences remain in the event ledger until resolved, canceled, or superseded.

## Fairness rule

The world may surprise Jack, but important outcomes should come from existing causes, discoverable clues, or reasonable uncertainty. Hidden information may be withheld; causality should not be fabricated after the fact merely to punish or rescue the player.

## Academy coupling

When the Academy clock is active, it should interact with wider clocks rather than operate as a sealed theme park.

Examples:
- political pressure changes training rules;
- ecology affects field exercises;
- market shortages affect equipment;
- classified events alter security;
- interworld relations influence curriculum or student tensions.

These are templates only until actual events are recorded.

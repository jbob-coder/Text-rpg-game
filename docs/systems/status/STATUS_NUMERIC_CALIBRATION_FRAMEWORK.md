# THE GAME — Status Numeric Calibration Framework

Status: **PHASE-C CALIBRATION FRAMEWORK / NUMBERS NOT LOCKED / NOT IMPLEMENTED**

Purpose: define how numeric values will be chosen after governing laws and state ownership are stable.

## Core rules
- Rarity is not a universal numeric multiplier.
- Level does not automatically increase ability output unless the Level standard later authorizes that relationship.
- Use `TBD` instead of false precision.
- Capacity, rate, range, duration, area, precision, complexity, setup time, resource cost, recovery, and failure thresholds are separate dimensions.
- Not every mechanic uses every dimension.

## Temporary design bands
For comparison only: `MINIMAL`, `LOW`, `MODERATE`, `HIGH`, `VERY_HIGH`, `EXTREME`.

These bands are not player-facing power scores and do not replace final numbers.

## Ability calibration
Before choosing a value, identify:
- parameter ID;
- parent ability/technique;
- state owner;
- unit or abstract unit;
- what increases/decreases the value;
- hard cap/floor;
- scenario tests;
- adjacent-tier comparison;
- resource/counterplay implications.

Reserve-based abilities calibrate capacity, input rate, output rate, efficiency, decay, and recharge source separately.

## Passive calibration
A passive should modify one named resolver term whenever possible.

For overlapping modifiers:
- use the shared cross-family composition standard;
- reject duplicate ownership;
- apply a cap;
- test the cap boundary directly.

## Unlock thresholds
Wave-001 compact unlock numbers remain proposals.

Final thresholds should be tested against:
- expected gameplay time;
- frequency of legitimate qualifying content;
- training/access availability;
- recovery/time requirements;
- anti-farm protections;
- whether ordinary play can realistically satisfy them.

## Scenario matrix
Calibrate mechanics under at least:
- novice user;
- trained user;
- high mastery user;
- low-resource state;
- favorable environment;
- unfavorable environment;
- informed counterplay;
- repeated-use pressure.

The objective is coherent, explainable outcomes rather than equal outcomes.

## Versioning
Once implemented, authoritative balance values require versioning and explicit save-migration behavior when changed.

Android/presentation must consume authoritative projected values rather than reconstruct hidden balance math.

## Promotion boundary
A mechanic may be well-defined in law while some runtime-required numbers remain `TBD`, but implementation cannot be certified until required values are resolved and tested.

This framework assigns no final numbers and canon-promotes no Wave-001 record.
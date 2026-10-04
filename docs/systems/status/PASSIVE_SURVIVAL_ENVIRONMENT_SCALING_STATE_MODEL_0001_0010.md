# THE GAME — Survival / Environmental Passive Scaling & State Model 0001–0010

Status: **PHASE-C CALIBRATION / NOT CANON / NOT IMPLEMENTED**

Purpose: define bounded scaling and authoritative state categories for `PASSIVE_SUR_0001`–`PASSIVE_SUR_0010`.

## Shared state

Future implementation should distinguish:
- `qualification_state`;
- `ownership_state`;
- `environment_context`;
- `acclimation_state`;
- `recovery_state`;
- `travel_state`;
- `resource_need_state`;
- `weather_observation_state`;
- `terrain_familiarity`;
- `projection_state`.

## Per-record model

| ID | Effect input | Scaling direction | Hard cap |
|---|---|---|---|
| SUR_0001 | heat-related performance penalty | valid acclimation history | harm thresholds still apply |
| SUR_0002 | cold-related performance penalty | valid acclimation history | harm thresholds still apply |
| SUR_0003 | elevation-related performance penalty | acclimated elevation-band history | no instant adaptation to every elevation |
| SUR_0004 | hydration/rationing decision inefficiency | reviewed limited-supply travel | does not create water or remove hydration need |
| SUR_0005 | short-term hunger distraction | legitimate scarcity/recovery history | nutrition deficits remain |
| SUR_0006 | short-term limited-sleep performance penalty | legitimate exposure/recovery history | chronic deprivation remains harmful |
| SUR_0007 | recognition error for previously known warning patterns | confirmed prior exposure/learning | unknown hazards remain unknown |
| SUR_0008 | weather-cue interpretation burden | repeated confirmed weather observation | no guaranteed forecast |
| SUR_0009 | rough-terrain travel inefficiency | terrain-family familiarity | severe terrain constraints remain |
| SUR_0010 | routine field-task overhead | practiced camp/maintenance history | does not replace required materials/tools |

## Qualification rules

The compact records require controlled or unavoidable exposures, completed recovery, and survivable conditions.

Future qualification must:
1. use stable exposure/event IDs;
2. count an event once;
3. reject trivial repeat loops;
4. require the defined recovery state;
5. keep exact progress hidden from ordinary Status projection.

## Cross-family overlap watchlist

- Heat/Cold Tolerance ↔ Resistance family;
- Altitude Acclimation ↔ Recovery/Physical families;
- Water Discipline / Hunger Management ↔ Survival skill;
- Sleep Scarcity Tolerance ↔ Mental/Will / Recovery;
- Storm Sense ↔ Sensory / Survival skill;
- Rough Terrain Adaptation ↔ Movement;
- Wilderness Routine ↔ Technical/Craft / Profession.

Same-resolver effects use one capped composition path.

## Required tests

- acclimation only applies to valid environment bands;
- dangerous thresholds remain authoritative;
- repeated exposure does not bypass recovery requirements;
- no survival passive creates missing resources;
- unknown hazard information is not fabricated;
- save/load preserves acclimation/qualification exactly once;
- hidden progress stays out of player-safe projection.

No runtime module is claimed here.

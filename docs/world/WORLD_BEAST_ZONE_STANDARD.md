# THE GAME — World Beast Zone Standard

Status: **ACTIVE / WORLD + COMBAT INTEGRATION STANDARD**  
Parent: `docs/world/WORLD_DEVELOPMENT_MASTER_INDEX.md`

## 1. Purpose

This standard defines beast zones, species distribution, ecology, threat, drops/resources, travel impact, and later tactical-combat integration.

It does not create copied monsters from another IP.

## 2. Beast-zone record

Each zone requires:
- `beast_zone_id`;
- bounds;
- parent ecosystem/region;
- habitat;
- species present;
- ordinary fauna interactions;
- nesting/lair sites;
- migration routes;
- activity periods if simulated;
- population state;
- aggression/territorial behavior;
- resource relationships;
- human/faction pressure;
- nearby settlements/routes;
- threat band;
- avoidance/escape options;
- loot/material provenance;
- tactical terrain requirements;
- visual asset kit;
- current world-state variants.

## 3. Beast species record

Each persistent species needs:
- `beast_id`;
- original name;
- taxonomy/body plan;
- size band;
- senses;
- movement;
- diet;
- habitat;
- social behavior;
- reproduction/lifecycle where relevant;
- territorial behavior;
- attacks;
- defenses;
- status resistances/vulnerabilities;
- intelligence/learning band;
- resource/drop anatomy;
- threat band;
- variants;
- tactical AI needs;
- visual/animation packet.

## 4. Threat is multidimensional

Track separately:
- lethality;
- durability;
- mobility;
- perception;
- group behavior;
- environmental advantage;
- anomaly/power capability;
- aggression probability;
- escape difficulty.

A single “level” may summarize for UI, but balance should not collapse these dimensions internally.

## 5. Body-part resources

If the final combat/loot system supports body-part targeting or preservation, each relevant beast part may define:
- part ID;
- function;
- armor/hardness;
- break/sever eligibility;
- preservation conditions;
- material output;
- quality loss rules;
- combat effect when disabled.

This remains conditional until combat/loot contracts explicitly enable it.

## 6. Encounter generation

No procedural encounter system is assumed.

If later implemented, encounter selection consumes:
- zone;
- time;
- weather;
- population;
- migration;
- noise/player behavior;
- faction activity;
- story state;
- threat/balance rules.

## 7. World persistence

Persistent named/unique beasts use stable IDs.

Ordinary populations may be aggregate records unless promoted to persistent entities.

## 8. Human interaction

Document:
- hunting;
- domestication if any;
- avoidance;
- culling;
- research;
- worship/fear if authored;
- illegal trade;
- resource dependency;
- settlement defenses.

## 9. Originality rule

Broad monster-hunting, ecology, body-part, and tactical concepts may inspire design.

Do not copy:
- protected species;
- names;
- silhouettes;
- attack animations;
- lore;
- exact drop tables;
- UI;
- distinctive proprietary behavior from another game.

## 10. Gate Twelve status

No world-scale beast ecology is yet established for Gate Twelve.

Do not inject beasts into the district merely because the broader game will contain beast zones.


## 11. Selective moving-base schema extraction — 2026-10-03

Status: **PROPOSED DESIGN / SCHEMA SUPPORT / IMPLEMENTATION DEPTH UNDECIDED**

Source provenance:
- `docs/settlement-region-build-plan@65d2db8538c1b8302c314f2fbe9eb7a1b585b51d`;
- `docs/world/BEAST_ZONE_AND_ECOSYSTEM_SCHEMA.md`;
- source blob `edfb5dc7fcf9d43216932bf698a37e2b5d3bda98`;
- selectively extracted under D-044.

These additions refine the existing beast-zone schema. They do not claim that world-scale beast simulation is implemented.

### 11.1 Planning density vocabulary

Before numeric population simulation exists, a zone/species relationship may use a qualitative density state:

- `absent`;
- `trace`;
- `sparse`;
- `ordinary`;
- `dense`;
- `concentrated`;
- `migration_surge`;
- `displaced`.

This is planning/state vocabulary, not a hidden numeric level scale.

If exact population counts are later required, they must be authored by the population/ecosystem system rather than inferred from these labels.

### 11.2 Beast migration is not player travel

A beast migration route and a player travel route are separate records.

A beast migration relationship may define:

- origin zone;
- destination zone;
- timing or trigger;
- corridor;
- blocking conditions;
- settlement impact;
- encounter impact.

A player-facing map may visualize migration only when player-safe knowledge/projection authorizes it.

Do not make a route traversable by the player merely because beasts use it.

### 11.3 Repopulation model options

The schema supports multiple future models:

- authored reset;
- time-based recovery;
- resource-driven recovery;
- migration-driven refill;
- persistent depletion;
- event-driven change.

**UNKNOWN / OWNER-SYSTEM DECISION REQUIRED:** no global repopulation model is selected by this extraction.

A concrete zone may adopt one only when its world/ecosystem design and persistence contract support it.

### 11.4 Hunting/harvesting pressure

When the final systems choose to simulate pressure, authored hunting/harvesting pressure may influence:

- local density;
- species behavior;
- resource quality;
- migration;
- settlement economy;
- quests/events;
- faction response.

Exact formulas remain outside this standard until the economy/ecology/balance owners define them.

### 11.5 Resource-result boundary

A beast-zone record may reference resource opportunities but must not invent loot results.

Target relationship, if the final loot/harvest system adopts it:

`beast state + encounter outcome + harvest method + preservation/damage + player/tool state -> resource result`

The item/loot/economy authority owns the actual result schema and values.

### 11.6 Implementation-readiness gate

A specific beast zone is not `IMPLEMENTATION_READY` merely because it has a name.

For the scoped runtime behavior being implemented, establish at minimum:

- stable zone ID;
- parent region/ecosystem;
- coordinate/boundary space;
- species set needed by the slice;
- threat/density semantics needed by the slice;
- encounter-generation or authored-encounter relationship;
- resource/loot relationship needed by the slice;
- discovery/map behavior;
- persistence requirements;
- player-safe scene-presence boundary;
- unresolved runtime-required decisions.

Fields that are irrelevant to a bounded implementation may be explicitly `not applicable`; they must not be silently guessed.

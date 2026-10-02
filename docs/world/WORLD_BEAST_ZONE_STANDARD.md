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

# Beast Zone and Ecosystem Schema

Status: **REVIEWABLE / GLOBAL SCHEMA**
Domains: World / Ecosystem / Beasts / Economy / Combat
Authority: `docs/program/13_BEAST_ENTITY_ECOSYSTEM_AND_SCENE_PRESENCE_STANDARD.md`

## Purpose

Define the minimum information required to document an ecosystem and a beast zone without inventing species, geography, or balance values that have not been decided.

## Ecosystem record

Required fields:

- `ecosystem_id`
- display name
- parent region IDs
- coordinate/boundary space
- terrain classes
- climate conditions
- water/energy/resource sources
- flora families
- beast families/species present
- predator/prey/competition relationships where relevant
- major resources
- hazards
- settlement/human pressure
- migration corridors
- seasonal/time variation if used
- world-state variants
- linked beast zones
- linked resource zones
- visual/material identity
- unresolved decisions
- implementation status

## Beast-zone record

Required fields:

- `beast_zone_id`
- parent ecosystem/region
- coordinate space
- boundary geometry/reference
- known species IDs
- density band by species where known
- threat band
- migration entrances/exits
- habitat drivers
- key resources
- hazards
- settlement/faction access
- hunting/harvesting pressure
- repopulation model
- event/quest hooks
- map-marker/discovery behavior
- visual-state variants
- encounter-generation relationship
- loot/resource relationship
- unresolved decisions

## Threat band

A threat band is descriptive planning data until the balance system defines exact combat meaning.

It must not silently become:
- enemy level scaling;
- guaranteed encounter difficulty;
- player level requirement;
- drop rarity.

Those relationships belong to world balance/combat/economy documents.

## Population/density state

Density should support qualitative planning before formulas exist:

- absent
- trace
- sparse
- ordinary
- dense
- concentrated
- migration surge
- displaced

Exact numeric population simulation remains optional and requires a separate implementation decision.

## Migration

Migration routes are distinct from player travel routes.

A beast migration route may contain:
- origin zone;
- destination zone;
- timing/trigger;
- corridor;
- blocking conditions;
- settlement impact;
- encounter impact.

A map may visualize migration only when player knowledge/state permits.

## Repopulation

The schema supports multiple future models:

- authored reset;
- time-based recovery;
- resource-driven recovery;
- migration-driven refill;
- persistent depletion;
- event-driven change.

No model is selected globally yet.

## Hunting/harvesting pressure

When used, pressure can affect:
- local density;
- species behavior;
- resource quality;
- migration;
- settlement economy;
- quests/events;
- faction reaction.

Exact formulas remain undecided.

## Beast-resource linkage

A beast-zone record may reference resource outputs but must not invent loot.

Source of truth should eventually be:

`beast state + encounter outcome + harvesting method + preservation/damage + player/tool state -> resource result`

## Scene and encounter linkage

Beast zones do not place visible beasts directly in UI.

They constrain authored/simulated encounter state.

Visible scene presence still follows:

`authoritative encounter/scene state -> player-safe presence -> visual composition`.

## Persistence

If ecosystem or beast-zone state changes permanently, persistence must define:
- stable state field;
- save compatibility;
- history/audit entry where useful;
- migration if schema changes.

## Implementation readiness checklist

A specific beast zone becomes implementation-ready when:
- [ ] stable zone ID exists;
- [ ] parent region/ecosystem exists;
- [ ] coordinate/boundary space exists;
- [ ] species list exists;
- [ ] threat/density semantics are known;
- [ ] encounter relationship is defined;
- [ ] resource/loot relationship is defined enough for that zone;
- [ ] discovery/map behavior is defined;
- [ ] persistence requirements are clear;
- [ ] unknowns required by runtime are resolved.

## Unknown global decisions

- final ecosystem count;
- actual region/ecosystem geography;
- actual beast species catalog;
- final population/repopulation model;
- final migration simulation depth;
- exact relationship between threat bands and world level;
- exact harvesting/loot formulas.

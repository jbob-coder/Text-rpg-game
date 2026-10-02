# World Level and Balance Architecture

Status: **REVIEWABLE / BALANCE PHILOSOPHY**
Domain: World / Progression / Combat / Beasts / Economy

## 1. Goal

Define how the game communicates and maintains challenge without making the world feel as if every enemy automatically scales to the player.

## 2. Core direction

Target philosophy: **world-anchored challenge with limited contextual adaptation**, not unrestricted global level scaling.

Regions, beast zones, factions and encounters should have identity.

The player can become stronger than old challenges and can encounter dangerous areas before being ready.

## 3. Balance layers

Separate:
- player progression;
- equipment power;
- ability/mastery;
- party strength;
- enemy/beast capability;
- encounter composition;
- environment;
- objective difficulty;
- region threat;
- world-state modifiers.

Do not compress these into one “power score” unless it is only a UI summary.

## 4. Region threat

A region may have a threat profile containing:
- minimum ordinary threat;
- typical threat;
- upper ordinary threat;
- exceptional threats;
- environmental hazards;
- faction/beast pressure.

Exact numbers remain unresolved.

## 5. Beast-zone threat

Beast-zone threat may be influenced by:
- species;
- density;
- pack behavior;
- terrain;
- migration surge;
- persistent adversary presence;
- resource scarcity/competition;
- time/world event.

Threat band is not automatically enemy level.

## 6. Encounter adaptation

Limited adaptation may respond to:
- party size;
- story stage;
- repeated farming;
- world state;
- alert/faction state.

Adaptation should change composition/context more often than silently inflating every stat.

## 7. Fixed threats

Some enemies/bestias/locations should remain fixed or mostly fixed to preserve world credibility.

This allows:
- danger foreshadowing;
- retreat;
- later return;
- progression payoff.

## 8. Difficulty controls

Player-facing difficulty settings, if adopted, should modify defined parameters such as:
- damage multipliers;
- AI behavior allowance;
- resource pressure;
- information assistance;
- save/checkpoint constraints.

They must not silently rewrite canon world identity.

Final difficulty-setting design remains unresolved.

## 9. Anti-grind considerations

Potential controls:
- diminishing low-risk rewards;
- ecosystem depletion;
- time cost;
- training caps;
- mastery requiring varied conditions;
- resource scarcity;
- quest/world progression gates.

No specific anti-grind formula is selected yet.

## 10. Progression ceilings

Need future decisions for:
- attribute caps;
- skill caps;
- ability/mastery caps;
- class/specialization limits;
- equipment tiers;
- beast/adversary upper bounds.

## 11. Loot/economy balance

Loot value must align with:
- threat;
- scarcity;
- preservation;
- access;
- regional economy;
- farming pressure.

Rare loot cannot be balanced independently from the economy.

## 12. World-level terminology

Avoid one ambiguous global `world_level` variable unless it has a precise role.

Potential explicit concepts:
- story progression stage;
- regional threat tier;
- faction alert;
- ecosystem pressure;
- player progression band;
- encounter difficulty band.

Each must have separate ownership.

## 13. Player communication

The player may learn danger through:
- map warnings;
- NPC knowledge;
- bestiary/journal;
- visible environmental cues;
- prior encounter evidence;
- faction notices.

The UI should not reveal hidden exact values unless the design intentionally exposes them.

## 14. Failure/retreat

Balance assumes retreat/failure can be valid.

Future combat/encounter design should specify:
- retreat conditions;
- pursuit;
- injury;
- resource loss;
- quest/world consequences;
- recovery.

## 15. Implementation readiness gaps

- numeric stat ranges;
- encounter math;
- progression caps;
- threat-band scale;
- region profiles;
- difficulty settings;
- loot/economy curves;
- anti-grind formulas;
- retreat/recovery values.

## 16. Acceptance expectation

The balance system becomes implementation-ready when at least one region and encounter family can be simulated/tested with:
- player progression bands;
- threat profile;
- encounter composition;
- reward profile;
- failure/retreat;
- progression outcome;
- deterministic test cases.

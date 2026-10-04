# THE GAME — Ability / Passive Cross-Reference

Status: **ACTIVE CALIBRATION MAP / NOT CANON UNTIL INDIVIDUAL LINKS ARE PROMOTED**

Parents:
- `PRIMARY_ABILITY_REGISTRY_SCHEMA.md`
- `PASSIVE_REGISTRY_SCHEMA.md`
- `ABILITY_CONTENT_AUTHORING_GUIDE.md`
- `PASSIVE_CONTENT_AUTHORING_GUIDE.md`

Purpose: record explicit ability/passive relationships so synergies, conflicts, cost modifiers, and duplicate effects do not remain implicit.

## 1. Relationship vocabulary

Use these relationship classes:

- `PROPOSED_SYNERGY` — likely compatible and beneficial;
- `PROPOSED_CONTROL_SYNERGY` — improves precision/stability rather than raw output;
- `PROPOSED_RESOURCE_SYNERGY` — modifies cost/recovery behavior if later approved;
- `PROPOSED_WORLD_SYNERGY` — useful together in profession/world content but not necessarily a mechanical multiplier;
- `PROPOSED_CONFLICT` — effects may interfere or create a tradeoff;
- `OVERLAP_REVIEW_REQUIRED` — records may duplicate the same mechanic;
- `MUTUAL_EXCLUSION_CANDIDATE` — only if later physiology/design supports exclusivity;
- `NO_DIRECT_LINK` — coexistence without a designed interaction.

No relationship in this file grants ownership or unlock credit.

## 2. Initial Common-ability calibration map

| Ability | Passive | Relationship | Reason / guardrail | Status |
|---|---|---|---|---|
| ABILITY_COM_001 Kinetic Palm | PASSIVE_PHY_0009 Core Bracing | PROPOSED_CONTROL_SYNERGY | Better bracing can reduce self-stagger during strong impulses; it must not raise the ability's force ceiling automatically. | CALIBRATION_PROPOSAL |
| ABILITY_COM_001 Kinetic Palm | PASSIVE_SYN_0003 Cast Stability | PROPOSED_CONTROL_SYNERGY | Repeated controlled activation may reduce instability; no free resource generation. | CALIBRATION_PROPOSAL |
| ABILITY_COM_001 Kinetic Palm | PASSIVE_SYN_0006 Precision Scaling | PROPOSED_CONTROL_SYNERGY | Low-output precision applications may become easier without creating remote telekinesis. | CALIBRATION_PROPOSAL |
| ABILITY_COM_002 Thermal Sight | PASSIVE_SEN_0006 Thermal Discrimination | PROPOSED_CONTROL_SYNERGY | Improves interpretation of close thermal differences; must not create new sensor bands. | CALIBRATION_PROPOSAL |
| ABILITY_COM_002 Thermal Sight | PASSIVE_COG_0001 Pattern Compression | PROPOSED_WORLD_SYNERGY | Helps learn recurring thermal patterns after study; no automatic diagnosis. | CALIBRATION_PROPOSAL |
| ABILITY_COM_002 Thermal Sight | PASSIVE_SYN_0009 Ability Familiarity | PROPOSED_RESOURCE_SYNERGY | Familiar low-complexity use may reduce focus overhead after mastery. | CALIBRATION_PROPOSAL |
| ABILITY_COM_003 Grip Field | PASSIVE_PHY_0006 Grip Endurance | PROPOSED_SYNERGY | Better forearm endurance supports long high-friction contact; tendon/joint limits remain. | CALIBRATION_PROPOSAL |
| ABILITY_COM_003 Grip Field | PASSIVE_PHY_0007 Joint Stability | PROPOSED_SYNERGY | Strong grip can transfer larger loads into joints; stability reduces minor instability but does not prevent overload. | CALIBRATION_PROPOSAL |
| ABILITY_COM_003 Grip Field | PASSIVE_MOV_0004 Balance Recovery | PROPOSED_CONTROL_SYNERGY | Helps recover from intentional low-friction movement without preventing falls. | CALIBRATION_PROPOSAL |
| ABILITY_COM_004 Skin Reinforcement | PASSIVE_PHY_0007 Joint Stability | PROPOSED_SYNERGY | Supports movement around reinforced areas; no internal armor. | CALIBRATION_PROPOSAL |
| ABILITY_COM_004 Skin Reinforcement | PASSIVE_SYN_0004 Overuse Warning | PROPOSED_CONTROL_SYNERGY | Better recognition of stiffness/metabolic warning signs can reduce unsafe sustained use. | CALIBRATION_PROPOSAL |
| ABILITY_COM_004 Skin Reinforcement | PASSIVE_DEF_0005 Guard Integrity | PROPOSED_WORLD_SYNERGY | Defensive training can make better use of selective reinforcement without changing protection values. | CALIBRATION_PROPOSAL |
| ABILITY_COM_005 Lumen Pulse | PASSIVE_SYN_0006 Precision Scaling | PROPOSED_CONTROL_SYNERGY | Supports precise signaling/brightness control; no hard-light effect. | CALIBRATION_PROPOSAL |
| ABILITY_COM_005 Lumen Pulse | PASSIVE_COG_0006 Procedural Chunking | PROPOSED_WORLD_SYNERGY | Helps execute learned signal sequences efficiently. | CALIBRATION_PROPOSAL |
| ABILITY_COM_005 Lumen Pulse | PASSIVE_SEN_0003 Peripheral Discipline | PROPOSED_CONTROL_SYNERGY | May help the user manage visual context while aiming light; no resistance to self-dazzle by default. | CALIBRATION_PROPOSAL |
| ABILITY_COM_006 Static Reservoir | PASSIVE_TEC_0003 Diagnostic Habit | PROPOSED_WORLD_SYNERGY | Supports safe interpretation of electrical systems; does not reveal hidden circuit truth automatically. | CALIBRATION_PROPOSAL |
| ABILITY_COM_006 Static Reservoir | PASSIVE_SYN_0004 Overuse Warning | PROPOSED_CONTROL_SYNERGY | Helps recognize unsafe reservoir states before overcapacity. | CALIBRATION_PROPOSAL |
| ABILITY_COM_006 Static Reservoir | PASSIVE_RES_0003 Electric Tolerance | OVERLAP_REVIEW_REQUIRED | Electrical tolerance may reduce disruption from low-level exposure, but must not become immunity or erase reservoir hazards. | CALIBRATION_PROPOSAL |
| ABILITY_COM_007 Echo Map | PASSIVE_SEN_0004 Sound Separation | PROPOSED_CONTROL_SYNERGY | Improves interpretation in overlapping acoustic environments; no omniscient mapping. | CALIBRATION_PROPOSAL |
| ABILITY_COM_007 Echo Map | PASSIVE_COG_0001 Pattern Compression | PROPOSED_WORLD_SYNERGY | Helps learn recurring echo structures and navigation patterns. | CALIBRATION_PROPOSAL |
| ABILITY_COM_007 Echo Map | PASSIVE_SYN_0006 Precision Scaling | PROPOSED_CONTROL_SYNERGY | Supports low-output/focused scan precision. | CALIBRATION_PROPOSAL |
| ABILITY_COM_008 Water Draw | PASSIVE_SUR_0004 Water Discipline | PROPOSED_WORLD_SYNERGY | Better water-management habits improve practical use but do not add control strength. | CALIBRATION_PROPOSAL |
| ABILITY_COM_008 Water Draw | PASSIVE_SYN_0007 Dual-Task Control | PROPOSED_CONTROL_SYNERGY | May support maintaining a simple flow while performing a familiar second task. | CALIBRATION_PROPOSAL |
| ABILITY_COM_008 Water Draw | PASSIVE_TEC_0005 Material Sense | PROPOSED_WORLD_SYNERGY | Better understanding of containers/materials can improve safe transfer planning. | CALIBRATION_PROPOSAL |
| ABILITY_COM_009 Impact Cushion | PASSIVE_PHY_0009 Core Bracing | PROPOSED_SYNERGY | Bracing may improve how the user survives/positions for impacts; it does not expand cushion capacity automatically. | CALIBRATION_PROPOSAL |
| ABILITY_COM_009 Impact Cushion | PASSIVE_DEF_0007 Stagger Resistance | OVERLAP_REVIEW_REQUIRED | Both can reduce disruption from impacts; damage mitigation and stagger mitigation must remain separate. | CALIBRATION_PROPOSAL |
| ABILITY_COM_009 Impact Cushion | PASSIVE_SYN_0004 Overuse Warning | PROPOSED_CONTROL_SYNERGY | Helps detect saturation/recovery warning signs. | CALIBRATION_PROPOSAL |
| ABILITY_COM_010 Thread Command | PASSIVE_TEC_0002 Fine Motor Calibration | PROPOSED_CONTROL_SYNERGY | Supports delicate line manipulation; does not increase controlled mass automatically. | CALIBRATION_PROPOSAL |
| ABILITY_COM_010 Thread Command | PASSIVE_TEC_0005 Material Sense | PROPOSED_WORLD_SYNERGY | Better knowledge of line/material properties improves safe tension use. | CALIBRATION_PROPOSAL |
| ABILITY_COM_010 Thread Command | PASSIVE_SYN_0007 Dual-Task Control | PROPOSED_CONTROL_SYNERGY | May support one simple maintained line action while performing a familiar secondary task. | CALIBRATION_PROPOSAL |

## 3. Cross-reference authoring requirements

Every promoted link must eventually define:
- source ability/passive ID;
- target ability/passive ID;
- relationship class;
- mechanical effect if any;
- activation conditions;
- scaling;
- cap;
- whether stacking is permitted;
- whether the relationship changes unlock requirements;
- whether world knowledge of the relationship is public/secret;
- implementation owner;
- tests.

## 4. Overlap audit rules

A link requires explicit overlap review when:
- both records reduce the same resource cost;
- both records reduce the same injury/stagger state;
- one passive appears to reproduce a technique;
- one passive could bypass a declared ability counter;
- several multipliers could compound into immunity or unlimited output.

## 5. Hidden-information rule

The engine may know a synergy exists before the player does.

The player-facing Status may reveal:
- owned passive;
- known compatible technique;
- discovered synergy;

only when knowledge/reveal rules permit.

Do not expose a hidden passive requirement merely because it would synergize with the player's ability.

## 6. Future expansion

Next cross-reference waves should cover:
1. Uncommon abilities;
2. Rare abilities;
3. higher rarity abilities;
4. all 23 passive families;
5. explicit conflicts/exclusions;
6. Level-100 replacement compatibility;
7. equipment and profession-mediated synergies.

The map should become machine-checkable if/when the catalog moves to structured data.

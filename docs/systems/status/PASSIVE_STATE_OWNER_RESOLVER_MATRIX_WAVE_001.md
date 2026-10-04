# THE GAME — Passive State Owner & Resolver Matrix — Wave 001

Status: **PHASE-C NORMALIZATION STANDARD / CONCEPTUAL OWNERS ONLY / NOT CANON / NOT IMPLEMENTED**

Parents:
- `PASSIVE_REGISTRY_SCHEMA.md`
- `PASSIVE_CROSS_FAMILY_COMPOSITION_STANDARD.md`
- `PASSIVE_WAVE_001_PHASE_C_FAMILY_COVERAGE_AUDIT.md`

Purpose: assign each Wave-001 passive family to a conceptual authoritative state domain and primary resolution stage before any runtime-module mapping is attempted.

Important:
- these are **conceptual owners**, not claims about current code modules;
- one passive can read several domains, but should have one primary effect owner;
- implementation mapping remains deferred.

## Conceptual owner domains

- `BODY_ADAPTATION_STATE` — durable physical conditioning/adaptation.
- `CORE_RESOURCE_STATE` — Health/Stamina/Focus/Resolve transitions.
- `MOVEMENT_ACTION_STATE` — traversal/movement execution.
- `PERCEPTION_EVIDENCE_STATE` — observations, interpreted signals, confidence.
- `MENTAL_PRESSURE_STATE` — stress/fear/pain-distraction/task degradation.
- `KNOWLEDGE_LEARNING_STATE` — learned information, familiarity, study/error history.
- `COMBAT_ACTION_STATE` — combat timing, posture, attention, encounter action transitions.
- `EQUIPMENT_HANDLING_STATE` — equipment-class familiarity and handling.
- `DEFENSIVE_REACTION_STATE` — guard/brace/evasion/balance defensive transitions.
- `ENVIRONMENT_EXPOSURE_STATE` — acclimation, terrain/environment exposure.
- `SOCIAL_CONTEXT_STATE` — social observations, rapport/reputation-known state, interaction recovery.
- `TEAM_COORDINATION_STATE` — team identity, assignments, trusted role, formation.
- `TECHNICAL_TASK_STATE` — tools, procedures, materials, diagnostics, quality review.
- `MEDICAL_CASE_STATE` — supervised cases, protocol, patient observation, rehabilitation.
- `ABILITY_EXECUTION_STATE` — primary-ability technique use, mastery, strain, recovery.
- `HAZARD_RESISTANCE_STATE` — bounded hazard-family adaptation/resistance.
- `CREATURE_FIELD_KNOWLEDGE_STATE` — species familiarity, tracks, behavior observations.
- `INJURY_REHABILITATION_STATE` — documented injury, stable limitation, rehab/adaptation.
- `PROFESSION_WORK_STATE` — profession identity, shifts, recurring work tasks, competency review.
- `INSTITUTIONAL_SERVICE_STATE` — institution/faction role, protocol, credential/clearance context.
- `WORLD_EVENT_LEDGER` — unique authored historical/event qualification.
- `STATUS_SYSTEM_EVENT_LEDGER` — authored Status/cosmic event qualification.
- `CLASSIFIED_AUTHORIZATION_STATE` — compartment packet, authorization, redaction/audit state.

## Family matrix

| Family | IDs | Primary effect stage | Conceptual authoritative owner | Qualification evidence owner | Primary overlap risk |
|---|---|---|---|---|---|
| Physical | PHY_0001–0010 | EXECUTION / STATE_RECOVERY | BODY_ADAPTATION_STATE | training/adaptation history | Recovery, Defense, Resistance |
| Recovery | REC_0001–0010 | RESOURCE_RECOVERY / STATE_RECOVERY | CORE_RESOURCE_STATE | exertion/recovery history | Physical, Mental, Ability Synergy |
| Movement | MOV_0001–0010 | EXECUTION / FAMILIARITY | MOVEMENT_ACTION_STATE | traversal practice history | Physical, Defense, Survival |
| Sensory | SEN_0001–0010 | SIGNAL_INPUT / INTERPRETATION | PERCEPTION_EVIDENCE_STATE | observation/sensory history | Cognitive, Beast, Investigation |
| Mental / Will | WIL_0001–0010 | DECISION / STATE_RECOVERY | MENTAL_PRESSURE_STATE | pressure/recovery history | Recovery, Combat, Social |
| Cognitive / Learning | COG_0001–0010 | KNOWLEDGE_RECALL / INTERPRETATION | KNOWLEDGE_LEARNING_STATE | study/error/mentor history | Sensory, Technical, Medical |
| Combat Habit | CBT_0001–0010 | DECISION / EXECUTION | COMBAT_ACTION_STATE | meaningful encounter history | Defense, Weapon, Leadership |
| Weapon Familiarity | WPN_0001–0010 | FAMILIARITY / EXECUTION | EQUIPMENT_HANDLING_STATE | equipment-specific practice | Combat, Technical, Physical |
| Defensive Adaptation | DEF_0001–0010 | RESISTANCE / EXECUTION | DEFENSIVE_REACTION_STATE | defensive-event history | Physical, Combat, Resistance |
| Survival / Environmental | SUR_0001–0010 | FAMILIARITY / STATE_RECOVERY | ENVIRONMENT_EXPOSURE_STATE | exposure/travel/recovery history | Resistance, Movement, Recovery |
| Social / Behavioral | SOC_0001–0010 | INTERPRETATION / DECISION | SOCIAL_CONTEXT_STATE | meaningful social-case history | Mental, Leadership, Reputation |
| Leadership / Coordination | LDR_0001–0010 | DECISION / EXECUTION | TEAM_COORDINATION_STATE | team-operation history | Social, Combat, Faction |
| Technical / Craft | TEC_0001–0010 | EXECUTION / INTERPRETATION | TECHNICAL_TASK_STATE | task/output/quality-review history | Cognitive, Profession, Medical |
| Medical / Recovery Practice | MED_0001–0010 | EXECUTION / INTERPRETATION | MEDICAL_CASE_STATE | supervised case/protocol history | Technical, Recovery, Cognitive |
| Ability Synergy | SYN_0001–0010 | RESOURCE_COST / EXECUTION / STATE_RECOVERY | ABILITY_EXECUTION_STATE | ability/technique/mastery history | Recovery, Cognitive, Mental |
| Resistance | RES_0001–0010 | RESISTANCE | HAZARD_RESISTANCE_STATE | controlled exposure/recovery history | Survival, Physical, Mental |
| Creature / Beast Interaction | BST_0001–0010 | INTERPRETATION / KNOWLEDGE_RECALL | CREATURE_FIELD_KNOWLEDGE_STATE | encounter/field-note evidence | Sensory, Survival, Cognitive |
| Injury / Scar Adaptation | INJ_0001–0010 | FAMILIARITY / STATE_RECOVERY / EXECUTION | INJURY_REHABILITATION_STATE | documented injury/rehab history | Medical, Physical, Movement |
| Profession | PRO_0001–0010 | FAMILIARITY / EXECUTION | PROFESSION_WORK_STATE | shift/task/competency history | Technical, Social, Faction |
| Faction / Institutional | FAC_0001–0010 | AUTHORIZATION_WORKFLOW / KNOWLEDGE_RECALL | INSTITUTIONAL_SERVICE_STATE | authorized service/protocol history | Leadership, Profession, Classified |
| Unique Event | UEV_0001–0010 | event-specific | WORLD_EVENT_LEDGER | one authored unique-event ID | Cosmic, world history |
| Cosmic / System | COS_0001–0010 | INTERPRETATION / RESISTANCE | STATUS_SYSTEM_EVENT_LEDGER | authored system-event + confirmation | Unique Event, Status governance |
| Unknown / Classified | CLS_0001–0010 | AUTHORIZATION_WORKFLOW / event-specific | CLASSIFIED_AUTHORIZATION_STATE | classified requirement packet | Faction, Status governance |

## Owner boundary rules

### Core resources
Only `CORE_RESOURCE_STATE` owns final Health/Stamina/Focus/Resolve values.

Other families may propose modifiers to a resource transition but do not own the final resource total.

### Damage and injury
Physical, Defense, Resistance, Mental, and Injury/Scar records may modify different stages around an incident.

The underlying injury/damage state remains authoritative outside those passive families unless a passive explicitly targets the damage resolver.

### Observation and truth
Sensory, Social, Beast, Cognitive, Medical, and Technical records may improve observation or interpretation.

They do not own objective world truth.

### Authorization
Faction/Institutional, Profession, Classified, and Cosmic/System records may read authorization context.

Only the authoritative credential/role/system-governance state determines actual permission.

### Ability identity
Ability Synergy can modify use of the one existing primary ability.

It does not own or alter primary-ability identity.

## Cross-owner transaction rule

When an effect crosses owner domains, use a transaction with:
1. source state read;
2. eligibility validation;
3. proposed modifier/state transition;
4. target-owner validation;
5. authoritative commit;
6. audit record;
7. player-safe projection.

No passive may directly write another domain's protected state without an explicit authored interface.

## Qualification evidence ownership

Hidden qualification evidence should be stored with the domain that can verify it, not with Android/UI.

Examples:
- combat events → COMBAT_ACTION_STATE or event ledger;
- supervised medical case → MEDICAL_CASE_STATE;
- institution service → INSTITUTIONAL_SERVICE_STATE;
- unique event → WORLD_EVENT_LEDGER;
- system event → STATUS_SYSTEM_EVENT_LEDGER.

## Implementation-map gate

Before mapping a passive to runtime code, its record must identify:
- primary conceptual owner;
- primary effect stage;
- read dependencies;
- write target;
- qualification evidence source;
- same-term overlap set;
- save persistence requirement;
- player-safe projection fields.

This matrix does not claim any runtime module currently exists and does not canon-promote any passive.

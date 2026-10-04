# THE GAME — Leadership / Coordination Passive Scaling & State Model 0001–0010

Status: **PHASE-C CALIBRATION / NOT CANON / NOT IMPLEMENTED**

Purpose: define bounded scaling and authoritative state categories for `PASSIVE_LDR_0001`–`PASSIVE_LDR_0010`.

## Shared state

Future implementation should distinguish:
- `qualification_state`;
- `ownership_state`;
- `team_identity`;
- `trusted_role_state`;
- `operation_context`;
- `assignment_state`;
- `formation_state`;
- `known_teammate_capabilities`;
- `team_resolve_state`;
- `projection_state`.

## Per-record model

| ID | Effect input | Scaling direction | Hard cap |
|---|---|---|---|
| LDR_0001 | command clarity/audibility loss | reviewed command use under pressure | cannot force obedience |
| LDR_0002 | formation-gap recognition burden | practiced formation history | no hidden-position awareness |
| LDR_0003 | assignment cognitive overhead | repeated valid delegation to known teammates | cannot grant missing teammate skill |
| LDR_0004 | nearby trusted-team Resolve degradation | legitimate trusted-team history | no Resolve creation or mind control |
| LDR_0005 | role-sequencing error in familiar rescue procedure | reviewed rescue operations | no substitute for medical/rescue expertise |
| LDR_0006 | timing variance in rehearsed coordinated action | practiced team execution | no free actions or perfect synchronization |
| LDR_0007 | briefing clarity/retention burden | validated concise-plan practice | cannot make a bad plan correct |
| LDR_0008 | urgent assignment overhead | known competency/role history | unknown competency remains unknown |
| LDR_0009 | recall burden for demonstrated teammate capability/role | stable team-operation history | cannot infer hidden capability |
| LDR_0010 | procedural errors inside familiar command hierarchy | legitimate institutional/team experience | unfamiliar structures receive limited/no benefit |

## Qualification rules

The compact records require:
- team operations;
- trusted role;
- coordination successes.

Future qualification must:
1. bind evidence to stable team/operation IDs;
2. verify that the role was genuinely trusted/recognized;
3. count a coordination success once;
4. reject scripted trivial loops;
5. keep hidden qualification out of normal Status projection.

## Cross-family overlap watchlist

- Command Voice ↔ Presence / Leadership skill;
- Formation Awareness ↔ Tactical skill / Sensory awareness;
- Delegation Habit ↔ Crisis Clarity;
- Morale Anchor ↔ Social/Mental-Will recovery effects;
- Rescue Coordination ↔ Medical / Profession systems;
- Shared Timing ↔ Combat Rhythm;
- Tactical Briefing ↔ Cognitive Deep Recall / Field Synthesis;
- Crisis Assignment ↔ Threat Prioritization;
- Team Memory ↔ Cognitive memory passives;
- Chain-of-Command Fluency ↔ faction/institutional passives.

Same-resolver effects use one capped composition path.

## Required tests

- no passive forces teammate behavior;
- unknown teammate capability is not fabricated;
- Resolve modifiers cannot create unlimited Resolve;
- duplicate operation IDs do not double-count;
- unfamiliar organizations do not receive full command-structure familiarity;
- save/load preserves progress exactly once;
- player-safe projection does not reveal hidden team data.

No runtime module is claimed here.

# THE GAME — CBT Passive Scaling & State Model 0001–0010

Status: **PHASE-C CALIBRATION / NOT CANON / NOT IMPLEMENTED**

Purpose: define bounded scaling and authoritative state categories for `PASSIVE_CBT_0001`–`PASSIVE_CBT_0010`.

## Shared state

Future implementation should distinguish:
- `qualification_state`;
- `ownership_state`;
- `encounter_context`;
- `action_state`;
- `attention_state`;
- `distance_state`;
- `resource_state`;
- `pattern_familiarity`;
- `projection_state`.

## Per-record model

| ID | Effect input | Scaling direction | Hard cap |
|---|---|---|---|
| CBT_0001 | post-action posture transition | validated practiced transitions | cannot remove all recovery time |
| CBT_0002 | attention switch overhead | confirmed multi-target experience | no hidden-target discovery |
| CBT_0003 | avoidable Stamina loss from breathing inefficiency | meaningful pressure history | no Stamina creation |
| CBT_0004 | deceptive-pattern recognition | varied confirmed pattern exposure | novel patterns remain uncertain |
| CBT_0005 | timing variance in practiced sequences | validated sequence repetition | no automatic initiative |
| CBT_0006 | unnecessary follow-through/overcommitment | reviewed encounter history | no forced decision override |
| CBT_0007 | distance-maintenance error | trained style/equipment history | physical reach/mobility remain authoritative |
| CBT_0008 | prioritization burden among visible concerns | reviewed tactical history | no hidden-information access |
| CBT_0009 | recognition of resource-recovery opportunity | encounter pacing history | recovery amount still uses resource rules |
| CBT_0010 | response timing after recognized action | trained response history | no response without recognition and valid execution |

## Qualification rules

The existing compact unlock records use meaningful encounters, relevant successful actions, and exclusion of trivial farming.

Future qualification must:
1. use stable encounter/event IDs;
2. count an event once;
3. reject trivial repeated loops;
4. preserve hidden progress outside ordinary player projection;
5. survive save/load without duplicate credit.

## Cross-family overlap watchlist

- Guard Recovery ↔ Defensive Adaptation;
- Pressure Breathing ↔ Physical/Recovery families;
- Feint Recognition ↔ Sensory/Cognitive families;
- Threat Prioritization ↔ Crisis Clarity / Tactics;
- Recovery Window ↔ Recovery family and core-resource rules;
- Counter Timing ↔ weapon familiarity and skill-specific timing.

Same-resolver effects use one capped composition path.

## Required tests

- duplicate encounter IDs do not double-count;
- trivial repeated input does not qualify;
- hidden qualification data does not appear in normal Status projection;
- distance and target-attention effects do not reveal hidden information;
- resource-related effects cannot create free Stamina/Focus;
- save/load preserves ownership and progress exactly once.

No runtime module is claimed here.

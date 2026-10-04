# THE GAME — Social / Behavioral Passive Scaling & State Model 0001–0010

Status: **PHASE-C CALIBRATION / NOT CANON / NOT IMPLEMENTED**

Purpose: define bounded scaling and authoritative state categories for `PASSIVE_SOC_0001`–`PASSIVE_SOC_0010`.

## Shared state

Future implementation should distinguish:
- `qualification_state`;
- `ownership_state`;
- `social_context`;
- `observable_reaction_state`;
- `relationship_state`;
- `reputation_knowledge_state`;
- `focus_state`;
- `resolve_state`;
- `social_recovery_state`;
- `projection_state`.

## Per-record model

| ID | Effect input | Scaling direction | Hard cap |
|---|---|---|---|
| SOC_0001 | visible composure degradation | reviewed familiar-pressure cases | internal emotion/stress remains real |
| SOC_0002 | recall of known contradiction patterns | confirmed prior pattern observations | no automatic lie detection |
| SOC_0003 | broad audience-mood interpretation | varied group-observation history | no individual mind reading |
| SOC_0004 | Focus/Resolve loss in long negotiation | legitimate structured-negotiation history | no free resources or automatic persuasion |
| SOC_0005 | post-encounter recovery burden | completed legitimate recovery cycles | no instant emotional reset |
| SOC_0006 | overshoot/poor calibration of deliberate pressure | reviewed controlled-pressure cases | no forced compliance |
| SOC_0007 | rapport-maintenance inconsistency | established-relationship practice | cannot create rapport from nothing |
| SOC_0008 | missed explicit/strong boundary cues | varied legitimate interactions | subtle/ambiguous cues remain uncertain |
| SOC_0009 | de-escalation execution error | reviewed dialogue-based conflict cases | cannot force dialogue when none is possible |
| SOC_0010 | recall failure for known reputation consequences | public-choice/reputation history | no knowledge of unknown consequences |

## Qualification rules

The compact records currently require:
- meaningful social cases;
- reflection or feedback cycles;
- exclusion of coercive exploit loops.

Future qualification must:
1. use stable case/event IDs;
2. count meaningful cases once;
3. require reflection/feedback where specified;
4. reject trivial scripted farming;
5. reject qualification loops based on repeatedly exploiting a captive or non-meaningful participant;
6. keep exact progress hidden from normal Status projection.

## Cross-family overlap watchlist

- Calm Presence ↔ Mental/Will Stress Lock;
- Lie Pattern Memory ↔ Investigation / Cognitive Error Memory;
- Audience Reading ↔ Empathy / Sensory interpretation;
- Negotiation Stamina ↔ Cognitive Endurance;
- Social Recovery ↔ Emotional Recovery;
- Controlled Intimidation ↔ Intimidation skill;
- Rapport Habit ↔ Persuasion/Empathy;
- Conflict De-escalation ↔ Leadership/coordination;
- Reputation Awareness ↔ faction/institution passives.

Same-resolver effects use one capped composition path.

## Required tests

- hidden relationship/reputation truth does not leak into player projection;
- contradiction memory never returns an automatic true/false deception verdict;
- audience mood remains probabilistic/observational;
- no passive overrides NPC/player agency;
- duplicate social-case IDs do not double-count;
- save/load preserves qualification and ownership exactly once;
- Focus/Resolve effects cannot create free resource restoration.

No runtime module is claimed here.

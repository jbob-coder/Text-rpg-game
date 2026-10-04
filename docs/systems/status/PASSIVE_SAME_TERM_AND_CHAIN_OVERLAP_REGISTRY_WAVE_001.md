# THE GAME — Passive Same-Term & Chain-Interaction Registry — Wave 001

Status: **PHASE-C NORMALIZATION / PROVISIONAL OVERLAP SETS / NOT CANON / NOT IMPLEMENTED**

Parents:
- `PASSIVE_CROSS_FAMILY_COMPOSITION_STANDARD.md`
- `PASSIVE_STATE_OWNER_RESOLVER_MATRIX_WAVE_001.md`
- `calibration/PASSIVES_WAVE_001.md`

Purpose: distinguish true same-term stacking from multi-stage interactions so the 230-passive corpus does not collapse into a universal bonus pool.

## Classification

- `SAME_TERM`: multiple passives can plausibly modify the same authoritative term in the same transaction. Use one capped composition resolver.
- `CHAIN_INTERACTION`: records act at different stages of one situation. Keep their effects separate.
- absence from this registry means no current cross-family normalization group has been identified; it does not prove permanent isolation.

## SAME_STAMINA_COST — SAME_TERM

Normalized term/chain: **authoritative Stamina cost/drain**

Members:
- `PASSIVE_PHY_0004` — Load Bearer
- `PASSIVE_PHY_0008` — Sprint Economy
- `PASSIVE_MOV_0005` — Vault Habit
- `PASSIVE_MOV_0006` — Climb Economy
- `PASSIVE_CBT_0003` — Pressure Breathing

Rule:
Combine only when the same action's Stamina-cost term is actually being modified; apply one capped cost resolver.

## SAME_FOCUS_COST — SAME_TERM

Normalized term/chain: **authoritative Focus cost/drain**

Members:
- `PASSIVE_WIL_0010` — Cognitive Endurance
- `PASSIVE_COG_0008` — Study Momentum
- `PASSIVE_SOC_0004` — Negotiation Stamina
- `PASSIVE_TEC_0009` — Calibration Patience
- `PASSIVE_SYN_0009` — Ability Familiarity

Rule:
These may touch different contexts. Stack only when they converge on the same Focus transition; never create negative cost.

## SAME_RESOLVE_DRAIN — SAME_TERM

Normalized term/chain: **authoritative Resolve drain**

Members:
- `PASSIVE_WIL_0008` — Resolve Reserve
- `PASSIVE_SOC_0004` — Negotiation Stamina
- `PASSIVE_LDR_0004` — Morale Anchor

Rule:
Validate target and context first. A user's Resolve modifier and a teammate-targeted modifier are not automatically the same transaction.

## SAME_STAMINA_RECOVERY — SAME_TERM

Normalized term/chain: **authoritative Stamina recovery**

Members:
- `PASSIVE_REC_0001` — Second Wind
- `PASSIVE_REC_0002` — Rapid Lactate Clearance
- `PASSIVE_REC_0003` — Deep Recovery
- `PASSIVE_SYN_0005` — Recovery Channel

Rule:
Use the core-resource recovery resolver; opportunity recognition alone does not increase recovery amount.

## SAME_FOCUS_RECOVERY — SAME_TERM

Normalized term/chain: **authoritative Focus recovery**

Members:
- `PASSIVE_REC_0003` — Deep Recovery
- `PASSIVE_REC_0006` — Sleep Efficiency
- `PASSIVE_SYN_0005` — Recovery Channel

Rule:
Apply context eligibility, then one capped Focus-recovery resolver.

## SAME_BALANCE_OR_REORIENTATION_RECOVERY — SAME_TERM

Normalized term/chain: **balance/reorientation recovery**

Members:
- `PASSIVE_MOV_0004` — Balance Recovery
- `PASSIVE_DEF_0007` — Stagger Resistance
- `PASSIVE_RES_0010` — Disorientation Resistance

Rule:
Only combine if the event model maps them to the same recovery term; injury-driven imbalance remains separate.

## SAME_TASK_PROGRESS_INTERRUPTION — SAME_TERM

Normalized term/chain: **task-progress loss from interruption/distraction**

Members:
- `PASSIVE_WIL_0005` — Interruption Resistance
- `PASSIVE_WIL_0006` — Patience Engine
- `PASSIVE_PRO_0010` — Professional Focus

Rule:
Context eligibility precedes composition; no passive prevents a genuinely invalidated task from failing.

## CHAIN_GUARD_BRACE_DEFENSE — CHAIN_INTERACTION

Normalized term/chain: **posture/brace/guard chain**

Members:
- `PASSIVE_PHY_0009` — Core Bracing
- `PASSIVE_CBT_0001` — Guard Recovery
- `PASSIVE_DEF_0002` — Brace Reflex
- `PASSIVE_DEF_0005` — Guard Integrity

Rule:
Keep anticipation, bracing, guard integrity, and post-action recovery as separate stages; do not collapse them into one defense bonus.

## CHAIN_HEAT_EXPOSURE — CHAIN_INTERACTION

Normalized term/chain: **heat exposure -> harm/performance -> recovery**

Members:
- `PASSIVE_REC_0004` — Heat Recovery
- `PASSIVE_SUR_0001` — Heat Tolerance
- `PASSIVE_RES_0001` — Heat Resistance

Rule:
Resistance, tolerance, and recovery act at different stages. Environmental injury remains authoritative.

## CHAIN_COLD_EXPOSURE — CHAIN_INTERACTION

Normalized term/chain: **cold exposure -> harm/performance -> recovery**

Members:
- `PASSIVE_REC_0005` — Cold Recovery
- `PASSIVE_SUR_0002` — Cold Tolerance
- `PASSIVE_RES_0002` — Cold Resistance

Rule:
Keep tolerance, resistance, and recovery separate; no immunity.

## CHAIN_PAIN — CHAIN_INTERACTION

Normalized term/chain: **pain signal -> interpretation/distraction -> recovery**

Members:
- `PASSIVE_WIL_0003` — Pain Compartmentalization
- `PASSIVE_REC_0008` — Pain Recovery
- `PASSIVE_MED_0005` — Pain Assessment
- `PASSIVE_INJ_0004` — Pain Map

Rule:
Pain assessment, distraction control, self-pattern recognition, and recovery are distinct stages.

## CHAIN_THREAT_RESPONSE — CHAIN_INTERACTION

Normalized term/chain: **detected threat -> localization -> prioritization -> response**

Members:
- `PASSIVE_SEN_0009` — Threat Localization
- `PASSIVE_WIL_0007` — Crisis Clarity
- `PASSIVE_CBT_0008` — Threat Prioritization
- `PASSIVE_DEF_0003` — Cover Instinct
- `PASSIVE_LDR_0008` — Crisis Assignment

Rule:
No stage may infer a hidden threat. Preserve signal, interpretation, decision, and team-assignment boundaries.

## CHAIN_DISTANCE_POSITIONING — CHAIN_INTERACTION

Normalized term/chain: **spacing/position selection**

Members:
- `PASSIVE_WPN_0003` — Polearm Reach
- `PASSIVE_CBT_0007` — Distance Habit
- `PASSIVE_DEF_0010` — Protective Positioning

Rule:
Physical reach, preferred combat distance, and protective positioning are separate constraints.

## CHAIN_PATTERN_LEARNING — CHAIN_INTERACTION

Normalized term/chain: **observation -> pattern recognition -> retained correction**

Members:
- `PASSIVE_COG_0001` — Pattern Compression
- `PASSIVE_COG_0003` — Error Memory
- `PASSIVE_CBT_0004` — Feint Recognition
- `PASSIVE_TEC_0004` — Failure Pattern Library
- `PASSIVE_BST_0001` — Beast Tell Reader
- `PASSIVE_BST_0006` — Predation Pattern Memory
- `PASSIVE_SYN_0008` — Counter-Feedback

Rule:
Do not turn pattern recognition into objective truth or future prediction.

## CHAIN_KNOWLEDGE_RECALL — CHAIN_INTERACTION

Normalized term/chain: **acquired information -> retention -> context recall**

Members:
- `PASSIVE_SEN_0010` — Detail Retention
- `PASSIVE_COG_0005` — Deep Recall
- `PASSIVE_LDR_0009` — Team Memory
- `PASSIVE_BST_0010` — Threat Species Recall
- `PASSIVE_PRO_0004` — Route Memory
- `PASSIVE_FAC_0001` — Protocol Memory
- `PASSIVE_FAC_0009` — Internal Network Memory

Rule:
Each record remains domain-scoped; one recall passive does not grant global memory.

## CHAIN_PROCEDURAL_EFFICIENCY — CHAIN_INTERACTION

Normalized term/chain: **known procedure -> execution efficiency/compliance**

Members:
- `PASSIVE_COG_0006` — Procedural Chunking
- `PASSIVE_WPN_0006` — Reload Memory
- `PASSIVE_TEC_0007` — Clean Assembly
- `PASSIVE_MED_0003` — Sterile Routine
- `PASSIVE_MED_0007` — Medication Discipline
- `PASSIVE_PRO_0006` — Safety Routine
- `PASSIVE_PRO_0008` — Documentation Discipline
- `PASSIVE_FAC_0010` — Security Habit

Rule:
Required steps, permissions, materials, and safety checks remain required.

## CHAIN_FINE_MOTOR — CHAIN_INTERACTION

Normalized term/chain: **precision motor control in domain-specific tasks**

Members:
- `PASSIVE_TEC_0002` — Fine Motor Calibration
- `PASSIVE_MED_0006` — Stabilization Hands
- `PASSIVE_WPN_0007` — Grip Transition

Rule:
General motor steadiness and domain technique are separate; no automatic cross-domain proficiency.

## CHAIN_STRESS_COMPOSURE — CHAIN_INTERACTION

Normalized term/chain: **stress/emotion -> visible composure -> task/team consequences**

Members:
- `PASSIVE_WIL_0001` — Stress Lock
- `PASSIVE_SOC_0001` — Calm Presence
- `PASSIVE_LDR_0004` — Morale Anchor
- `PASSIVE_MED_0010` — Patient Calm

Rule:
Internal emotion, visible behavior, teammate effect, and patient communication remain distinct.

## CHAIN_FATIGUE_ENDURANCE — CHAIN_INTERACTION

Normalized term/chain: **exertion/time -> fatigue -> performance/recovery**

Members:
- `PASSIVE_PHY_0010` — Repetition Tolerance
- `PASSIVE_REC_0002` — Rapid Lactate Clearance
- `PASSIVE_SUR_0006` — Sleep Scarcity Tolerance
- `PASSIVE_RES_0009` — Fatigue Resistance
- `PASSIVE_PRO_0001` — Shift Endurance
- `PASSIVE_WIL_0010` — Cognitive Endurance

Rule:
Physical, sleep, cognitive, and occupational fatigue are not one universal meter unless a later core model explicitly unifies them.

## CHAIN_ENVIRONMENT_ADAPTATION — CHAIN_INTERACTION

Normalized term/chain: **environment exposure -> acclimation/resistance**

Members:
- `PASSIVE_SUR_0001` — Heat Tolerance
- `PASSIVE_SUR_0002` — Cold Tolerance
- `PASSIVE_SUR_0003` — Altitude Acclimation
- `PASSIVE_RES_0001` — Heat Resistance
- `PASSIVE_RES_0002` — Cold Resistance
- `PASSIVE_RES_0004` — Pressure Tolerance

Rule:
Acclimation bands and resistance types remain specific to environment or hazard.

## CHAIN_TOXIN — CHAIN_INTERACTION

Normalized term/chain: **toxin warning recognition -> physiological resistance**

Members:
- `PASSIVE_SUR_0007` — Toxin Familiarity
- `PASSIVE_RES_0005` — Toxin Resistance

Rule:
Recognition and physiological resistance are separate. Neither implies universal toxin knowledge or immunity.

## CHAIN_AUDIO — CHAIN_INTERACTION

Normalized term/chain: **auditory signal -> separation/filtering -> impairment tolerance**

Members:
- `PASSIVE_SEN_0004` — Sound Separation
- `PASSIVE_RES_0006` — Sonic Tolerance
- `PASSIVE_BST_0008` — Beast Noise Filter
- `PASSIVE_INJ_0007` — Hearing Compensation

Rule:
Signal discrimination, creature-call filtering, injury compensation, and sound tolerance are separate.

## CHAIN_VISUAL — CHAIN_INTERACTION

Normalized term/chain: **visual signal -> discrimination/tracking -> impairment recovery**

Members:
- `PASSIVE_SEN_0001` — Low-Light Acuity
- `PASSIVE_SEN_0002` — Motion Focus
- `PASSIVE_SEN_0003` — Peripheral Discipline
- `PASSIVE_RES_0007` — Flash Resistance
- `PASSIVE_INJ_0006` — Vision Compensation

Rule:
Do not convert remaining-sense compensation or flash recovery into new sensory input.

## CHAIN_RECOVERY_BEHAVIOR — CHAIN_INTERACTION

Normalized term/chain: **recovery opportunity -> behavior -> resource/state recovery**

Members:
- `PASSIVE_REC_0010` — Recovery Discipline
- `PASSIVE_CBT_0009` — Recovery Window
- `PASSIVE_SYN_0001` — Resource Cycling
- `PASSIVE_SYN_0005` — Recovery Channel
- `PASSIVE_INJ_0010` — Rehabilitation Strength

Rule:
Opportunity recognition, compliance, ability-use cycling, and rehabilitation remain separate stages.

## CHAIN_RESOURCE_WASTE — CHAIN_INTERACTION

Normalized term/chain: **resource handling -> avoidable waste**

Members:
- `PASSIVE_WPN_0010` — Ammunition Discipline
- `PASSIVE_TEC_0006` — Repair Economy
- `PASSIVE_PRO_0005` — Inventory Habit

Rule:
Ammunition, repair consumables, and inventory handling use different resource owners even if all reduce avoidable waste.

## CHAIN_AUTHORIZATION — CHAIN_INTERACTION

Normalized term/chain: **institutional knowledge -> credential/clearance workflow -> authorized action**

Members:
- `PASSIVE_FAC_0002` — Credential Navigation
- `PASSIVE_FAC_0005` — Clearance Awareness
- `PASSIVE_FAC_0010` — Security Habit
- `PASSIVE_CLS_0001` — Black Ledger
- `PASSIVE_CLS_0003` — Red Index
- `PASSIVE_CLS_0005` — Null Stamp
- `PASSIVE_CLS_0006` — Grey Circuit
- `PASSIVE_CLS_0007` — Closed Hand
- `PASSIVE_CLS_0008` — Night Archive

Rule:
Familiarity or secrecy discipline never creates rank, credential, clearance, or admin authority.

## CHAIN_TEAM_COORDINATION — CHAIN_INTERACTION

Normalized term/chain: **team knowledge -> assignment/formation/timing**

Members:
- `PASSIVE_LDR_0002` — Formation Awareness
- `PASSIVE_LDR_0003` — Delegation Habit
- `PASSIVE_LDR_0006` — Shared Timing
- `PASSIVE_LDR_0008` — Crisis Assignment
- `PASSIVE_LDR_0009` — Team Memory
- `PASSIVE_FAC_0004` — Unit Cohesion

Rule:
Team familiarity, institutional unit cohesion, assignment, and synchronized timing remain separate.

## CHAIN_ABILITY_RECOVERY_CONTROL — CHAIN_INTERACTION

Normalized term/chain: **ability use -> strain warning/control -> recovery**

Members:
- `PASSIVE_SYN_0001` — Resource Cycling
- `PASSIVE_SYN_0003` — Cast Stability
- `PASSIVE_SYN_0004` — Overuse Warning
- `PASSIVE_SYN_0005` — Recovery Channel
- `PASSIVE_SYN_0009` — Ability Familiarity

Rule:
Stability, warning, resource overhead, and recovery are separate; no passive bypasses parent ability law.

## Global rule

A future resolver must:
1. identify the actual authoritative term being resolved;
2. select only eligible `SAME_TERM` members for that transaction;
3. apply one cap/floor;
4. keep `CHAIN_INTERACTION` members in their own stages;
5. record contributing IDs for debug/audit;
6. expose only player-safe results.

No passive is canon-promoted by this registry.

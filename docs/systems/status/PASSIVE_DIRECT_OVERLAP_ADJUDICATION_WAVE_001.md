# THE GAME — Passive Direct-Overlap Adjudication — Wave 001

Status: **PHASE-C NORMALIZATION / 93 CANDIDATE PAIRS ADJUDICATED / NOT CANON / NOT IMPLEMENTED**

Parents:
- `PASSIVE_RECORD_READ_DEPENDENCY_OVERLAP_MATRIX_WAVE_001_A.md`
- `PASSIVE_RECORD_READ_DEPENDENCY_OVERLAP_MATRIX_WAVE_001_B.md`
- `PASSIVE_RECORD_READ_DEPENDENCY_OVERLAP_MATRIX_WAVE_001_C.md`
- `PASSIVE_SAME_TERM_AND_CHAIN_OVERLAP_REGISTRY_WAVE_001.md`

Purpose: convert the 93 direct candidate overlap pairs in the record-level dependency matrices into an explicit normalization decision.

## Classification meanings

- `SAME_TERM` — use one capped resolver when both are eligible in the same transaction.
- `PARTIAL_SAME_TERM` — only one subcomponent can collide; scope/eligibility must be checked before shared resolution.
- `CHAIN_INTERACTION` — different stages of one process; do not collapse into one bonus.
- `ADJACENT_DISTINCT` — same context/domain, but no shared resolver is currently justified.
- `POTENTIAL_DUPLICATE_REVIEW` — identities are close enough to require a design decision before canon promotion.

## Result

Total candidate pairs: **93**.

- CHAIN_INTERACTION: **72**
- PARTIAL_SAME_TERM: **10**
- SAME_TERM: **8**
- POTENTIAL_DUPLICATE_REVIEW: **1**
- ADJACENT_DISTINCT: **2**

## Pair adjudication

| Record A | Record B | Classification | Normalization decision |
|---|---|---|---|
| PASSIVE_BST_0006 — Predation Pattern Memory | PASSIVE_COG_0005 — Deep Recall | **CHAIN_INTERACTION** | Domain-specific predation-pattern memory can benefit from general learned-information recall, but the two operate on different knowledge scopes. |
| PASSIVE_BST_0008 — Beast Noise Filter | PASSIVE_SEN_0004 — Sound Separation | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_AUDIO. Keep stages separate. |
| PASSIVE_BST_0010 — Threat Species Recall | PASSIVE_COG_0005 — Deep Recall | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_KNOWLEDGE_RECALL. Keep stages separate. |
| PASSIVE_CBT_0002 — Target Transition | PASSIVE_SEN_0002 — Motion Focus | **CHAIN_INTERACTION** | Sensory tracking supplies the target signal; Target Transition governs attention switching between confirmed targets. |
| PASSIVE_CBT_0003 — Pressure Breathing | PASSIVE_REC_0007 — Breath Reserve | **CHAIN_INTERACTION** | Breathing efficiency during combat stress and tolerance to short oxygen-demand spikes are distinct physiological/action stages. |
| PASSIVE_CBT_0003 — Pressure Breathing | PASSIVE_WIL_0001 — Stress Lock | **CHAIN_INTERACTION** | Stress Lock limits task degradation while Pressure Breathing limits breathing-related Stamina waste. |
| PASSIVE_CBT_0005 — Combat Rhythm | PASSIVE_LDR_0006 — Shared Timing | **CHAIN_INTERACTION** | Combat Rhythm is individual sequence timing; Shared Timing is practiced team synchronization. |
| PASSIVE_CBT_0005 — Combat Rhythm | PASSIVE_WPN_0005 — Draw Economy | **CHAIN_INTERACTION** | Draw Economy modifies a specific ready/draw transition; Combat Rhythm governs broader practiced action-response timing. |
| PASSIVE_CBT_0007 — Distance Habit | PASSIVE_SEN_0008 — Range Estimation | **CHAIN_INTERACTION** | Range Estimation supplies distance information; Distance Habit uses known spacing to maintain an engagement band. |
| PASSIVE_CBT_0007 — Distance Habit | PASSIVE_WPN_0003 — Polearm Reach | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_DISTANCE_POSITIONING. Keep stages separate. |
| PASSIVE_CBT_0008 — Threat Prioritization | PASSIVE_LDR_0008 — Crisis Assignment | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_THREAT_RESPONSE. Keep stages separate. |
| PASSIVE_CBT_0008 — Threat Prioritization | PASSIVE_SEN_0009 — Threat Localization | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_THREAT_RESPONSE. Keep stages separate. |
| PASSIVE_CBT_0008 — Threat Prioritization | PASSIVE_WIL_0007 — Crisis Clarity | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_THREAT_RESPONSE. Keep stages separate. |
| PASSIVE_CBT_0009 — Recovery Window | PASSIVE_REC_0001 — Second Wind | **CHAIN_INTERACTION** | Recovery Window identifies an opportunity; Second Wind modifies recovery after eligibility is satisfied. |
| PASSIVE_CBT_0009 — Recovery Window | PASSIVE_SYN_0005 — Recovery Channel | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_RECOVERY_BEHAVIOR. Keep stages separate. |
| PASSIVE_CLS_0001 — Black Ledger | PASSIVE_FAC_0001 — Protocol Memory | **CHAIN_INTERACTION** | Protocol Memory recalls ordinary institutional procedure; Black Ledger is constrained to an authorized protected-information procedure. |
| PASSIVE_CLS_0003 — Red Index | PASSIVE_COS_0001 — Status Intuition | **CHAIN_INTERACTION** | Status Intuition interprets already visible Status information; Red Index concerns one authorized high-risk classification flag. |
| PASSIVE_CLS_0003 — Red Index | PASSIVE_FAC_0005 — Clearance Awareness | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_AUTHORIZATION. Keep stages separate. |
| PASSIVE_CLS_0007 — Closed Hand | PASSIVE_FAC_0010 — Security Habit | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_AUTHORIZATION. Keep stages separate. |
| PASSIVE_CLS_0008 — Night Archive | PASSIVE_COG_0005 — Deep Recall | **CHAIN_INTERACTION** | Night Archive adds authorization/compartment gating to knowledge retrieval; Deep Recall cannot bypass that authorization. |
| PASSIVE_CLS_0010 — White Room | PASSIVE_WIL_0006 — Patience Engine | **PARTIAL_SAME_TERM** | Both may reduce Focus/performance degradation during long isolation/precision contexts, but White Room is packet/context specific. |
| PASSIVE_COG_0003 — Error Memory | PASSIVE_SOC_0002 — Lie Pattern Memory | **CHAIN_INTERACTION** | Error Memory retains reviewed mistakes/corrections; Lie Pattern Memory retains contradiction patterns in social evidence. |
| PASSIVE_COG_0003 — Error Memory | PASSIVE_SYN_0008 — Counter-Feedback | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_PATTERN_LEARNING. Keep stages separate. |
| PASSIVE_COG_0003 — Error Memory | PASSIVE_TEC_0004 — Failure Pattern Library | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_PATTERN_LEARNING. Keep stages separate. |
| PASSIVE_COG_0005 — Deep Recall | PASSIVE_FAC_0001 — Protocol Memory | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_KNOWLEDGE_RECALL. Keep stages separate. |
| PASSIVE_COG_0005 — Deep Recall | PASSIVE_FAC_0009 — Internal Network Memory | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_KNOWLEDGE_RECALL. Keep stages separate. |
| PASSIVE_COG_0005 — Deep Recall | PASSIVE_LDR_0007 — Tactical Briefing | **CHAIN_INTERACTION** | Tactical Briefing improves plan communication/retention; Deep Recall affects retrieval of already learned information. |
| PASSIVE_COG_0005 — Deep Recall | PASSIVE_LDR_0009 — Team Memory | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_KNOWLEDGE_RECALL. Keep stages separate. |
| PASSIVE_COG_0005 — Deep Recall | PASSIVE_MED_0009 — Injury Pattern Memory | **CHAIN_INTERACTION** | Injury Pattern Memory is domain-specific case recall; Deep Recall is general studied-information retrieval. |
| PASSIVE_COG_0005 — Deep Recall | PASSIVE_PRO_0004 — Route Memory | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_KNOWLEDGE_RECALL. Keep stages separate. |
| PASSIVE_COG_0005 — Deep Recall | PASSIVE_SEN_0010 — Detail Retention | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_KNOWLEDGE_RECALL. Keep stages separate. |
| PASSIVE_COG_0006 — Procedural Chunking | PASSIVE_SUR_0010 — Wilderness Routine | **CHAIN_INTERACTION** | Procedural Chunking reduces transition overhead in a learned sequence; Wilderness Routine is domain-specific field-task efficiency. |
| PASSIVE_COG_0006 — Procedural Chunking | PASSIVE_SYN_0002 — Technique Compression | **CHAIN_INTERACTION** | Technique Compression is restricted to a mastered ability technique; Procedural Chunking is general learned-procedure efficiency. |
| PASSIVE_COG_0006 — Procedural Chunking | PASSIVE_WPN_0006 — Reload Memory | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_PROCEDURAL_EFFICIENCY. Keep stages separate. |
| PASSIVE_COG_0007 — Analytical Habit | PASSIVE_TEC_0003 — Diagnostic Habit | **CHAIN_INTERACTION** | Analytical Habit governs assumption checking; Diagnostic Habit governs completion of a technical diagnostic sequence. |
| PASSIVE_COG_0008 — Study Momentum | PASSIVE_WIL_0010 — Cognitive Endurance | **SAME_TERM** | Shared same-term group(s): SAME_FOCUS_COST. Use one capped resolver when both are eligible in the same transaction. |
| PASSIVE_COS_0002 — Hidden Prompt Sensitivity | PASSIVE_COS_0008 — System Error Recognition | **CHAIN_INTERACTION** | Prompt occurrence sensitivity and system-anomaly recognition are separate observation/interpretation events. |
| PASSIVE_COS_0009 — Cosmic Pressure Resistance | PASSIVE_RES_0008 — Fear Resistance | **PARTIAL_SAME_TERM** | Both can reduce disruption to a qualifying fear/pressure response, but Cosmic Pressure Resistance is signature-specific and must not become generic fear resistance. |
| PASSIVE_DEF_0002 — Brace Reflex | PASSIVE_PHY_0009 — Core Bracing | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_GUARD_BRACE_DEFENSE. Keep stages separate. |
| PASSIVE_DEF_0006 — Evasion Recovery | PASSIVE_MOV_0004 — Balance Recovery | **PARTIAL_SAME_TERM** | A successful evasion can include balance recovery, so both may touch post-movement recovery time in some actions; eligibility remains distinct. |
| PASSIVE_DEF_0007 — Stagger Resistance | PASSIVE_MOV_0004 — Balance Recovery | **SAME_TERM** | Shared same-term group(s): SAME_BALANCE_OR_REORIENTATION_RECOVERY. Use one capped resolver when both are eligible in the same transaction. |
| PASSIVE_DEF_0007 — Stagger Resistance | PASSIVE_PHY_0005 — Shock Acclimation | **CHAIN_INTERACTION** | Shock Acclimation reduces post-shock performance loss; Stagger Resistance targets balance disruption from survivable impacts. |
| PASSIVE_DEF_0007 — Stagger Resistance | PASSIVE_RES_0010 — Disorientation Resistance | **SAME_TERM** | Shared same-term group(s): SAME_BALANCE_OR_REORIENTATION_RECOVERY. Use one capped resolver when both are eligible in the same transaction. |
| PASSIVE_DEF_0008 — Shield Habit | PASSIVE_WPN_0008 — Weapon Retention | **PARTIAL_SAME_TERM** | Shield Habit includes retention efficiency for a shield; Weapon Retention can modify the same contested-hold subterm when the shield qualifies as held equipment. |
| PASSIVE_DEF_0010 — Protective Positioning | PASSIVE_LDR_0005 — Rescue Coordination | **CHAIN_INTERACTION** | Protective Positioning handles spatial placement around a protected ally; Rescue Coordination handles team-role sequencing. |
| PASSIVE_FAC_0006 — Chain Familiarity | PASSIVE_LDR_0010 — Chain-of-Command Fluency | **POTENTIAL_DUPLICATE_REVIEW** | Both reduce mistakes inside a familiar formal responsibility/command chain. Their current identities may be too close and require an explicit scope split or consolidation decision. |
| PASSIVE_FAC_0010 — Security Habit | PASSIVE_PRO_0006 — Safety Routine | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_PROCEDURAL_EFFICIENCY. Keep stages separate. |
| PASSIVE_INJ_0004 — Pain Map | PASSIVE_MED_0005 — Pain Assessment | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_PAIN. Keep stages separate. |
| PASSIVE_INJ_0005 — Joint Protection | PASSIVE_PHY_0007 — Joint Stability | **CHAIN_INTERACTION** | Joint Stability affects trained joint stability broadly; Joint Protection is a compensatory movement habit around a documented prior injury. |
| PASSIVE_INJ_0007 — Hearing Compensation | PASSIVE_SEN_0004 — Sound Separation | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_AUDIO. Keep stages separate. |
| PASSIVE_INJ_0008 — Breath Compensation | PASSIVE_REC_0007 — Breath Reserve | **CHAIN_INTERACTION** | Breath Compensation paces around a stable respiratory limitation; Breath Reserve handles short oxygen-demand spikes in otherwise valid activity. |
| PASSIVE_INJ_0010 — Rehabilitation Strength | PASSIVE_PHY_0003 — Efficient Recruitment | **CHAIN_INTERACTION** | Rehabilitation Strength applies inside an authorized rehab plan; Efficient Recruitment is general trained muscle recruitment. |
| PASSIVE_LDR_0001 — Command Voice | PASSIVE_SOC_0009 — Conflict De-escalation | **ADJACENT_DISTINCT** | Command audibility/clarity and conflict de-escalation are different social/team outputs even if both use communication. |
| PASSIVE_LDR_0004 — Morale Anchor | PASSIVE_WIL_0008 — Resolve Reserve | **SAME_TERM** | Shared same-term group(s): SAME_RESOLVE_DRAIN. Use one capped resolver when both are eligible in the same transaction. |
| PASSIVE_LDR_0005 — Rescue Coordination | PASSIVE_MED_0001 — Triage Reflex | **CHAIN_INTERACTION** | Triage Reflex orders patient urgency; Rescue Coordination sequences team roles around the response. |
| PASSIVE_LDR_0008 — Crisis Assignment | PASSIVE_MED_0001 — Triage Reflex | **CHAIN_INTERACTION** | Triage can provide urgency information; Crisis Assignment allocates known teammates/tasks. |
| PASSIVE_LDR_0008 — Crisis Assignment | PASSIVE_WIL_0007 — Crisis Clarity | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_THREAT_RESPONSE. Keep stages separate. |
| PASSIVE_MED_0001 — Triage Reflex | PASSIVE_WIL_0007 — Crisis Clarity | **CHAIN_INTERACTION** | Crisis Clarity supports prioritization under emergency pressure; Triage Reflex applies a medical triage procedure. |
| PASSIVE_MED_0003 — Sterile Routine | PASSIVE_TEC_0007 — Clean Assembly | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_PROCEDURAL_EFFICIENCY. Keep stages separate. |
| PASSIVE_MED_0006 — Stabilization Hands | PASSIVE_TEC_0002 — Fine Motor Calibration | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_FINE_MOTOR. Keep stages separate. |
| PASSIVE_MED_0010 — Patient Calm | PASSIVE_SOC_0001 — Calm Presence | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_STRESS_COMPOSURE. Keep stages separate. |
| PASSIVE_MOV_0001 — Sure Foot | PASSIVE_SUR_0009 — Rough Terrain Adaptation | **CHAIN_INTERACTION** | Sure Foot reduces slips/minor footing errors; Rough Terrain Adaptation reduces broader travel inefficiency. |
| PASSIVE_MOV_0004 — Balance Recovery | PASSIVE_RES_0010 — Disorientation Resistance | **SAME_TERM** | Shared same-term group(s): SAME_BALANCE_OR_REORIENTATION_RECOVERY. Use one capped resolver when both are eligible in the same transaction. |
| PASSIVE_MOV_0006 — Climb Economy | PASSIVE_PHY_0006 — Grip Endurance | **CHAIN_INTERACTION** | Grip Endurance controls grip fatigue; Climb Economy modifies climbing Stamina/efficiency. |
| PASSIVE_MOV_0007 — Terrain Reader | PASSIVE_SUR_0009 — Rough Terrain Adaptation | **CHAIN_INTERACTION** | Terrain Reader chooses movement lines from observed hazards; Rough Terrain Adaptation modifies execution/travel efficiency. |
| PASSIVE_MOV_0008 — Long Stride | PASSIVE_SUR_0009 — Rough Terrain Adaptation | **PARTIAL_SAME_TERM** | Both can affect long-distance travel efficiency on rough terrain; one is stride/endurance travel and the other terrain-specific adaptation. |
| PASSIVE_PHY_0006 — Grip Endurance | PASSIVE_WPN_0008 — Weapon Retention | **CHAIN_INTERACTION** | Grip Endurance affects fatigue accumulation; Weapon Retention affects contested control of held equipment. |
| PASSIVE_PHY_0010 — Repetition Tolerance | PASSIVE_PRO_0001 — Shift Endurance | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_FATIGUE_ENDURANCE. Keep stages separate. |
| PASSIVE_PHY_0010 — Repetition Tolerance | PASSIVE_RES_0009 — Fatigue Resistance | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_FATIGUE_ENDURANCE. Keep stages separate. |
| PASSIVE_PRO_0001 — Shift Endurance | PASSIVE_RES_0009 — Fatigue Resistance | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_FATIGUE_ENDURANCE. Keep stages separate. |
| PASSIVE_PRO_0003 — Customer Read | PASSIVE_SOC_0003 — Audience Reading | **ADJACENT_DISTINCT** | Customer Read concerns explicit client needs; Audience Reading concerns broad group mood. Neither should inherit the other's scope. |
| PASSIVE_PRO_0006 — Safety Routine | PASSIVE_TEC_0010 — Workshop Discipline | **PARTIAL_SAME_TERM** | In a workshop, workplace Safety Routine and Workshop Discipline may both modify procedure-compliance error; the latter remains broader than safety alone. |
| PASSIVE_PRO_0007 — Negotiation Routine | PASSIVE_SOC_0004 — Negotiation Stamina | **CHAIN_INTERACTION** | Negotiation Routine modifies routine professional execution; Negotiation Stamina modifies resource degradation during prolonged negotiation. |
| PASSIVE_PRO_0008 — Documentation Discipline | PASSIVE_TEC_0010 — Workshop Discipline | **PARTIAL_SAME_TERM** | Workshop Discipline can include documentation routine compliance, overlapping Documentation Discipline only in qualifying workshop workflows. |
| PASSIVE_PRO_0010 — Professional Focus | PASSIVE_WIL_0010 — Cognitive Endurance | **PARTIAL_SAME_TERM** | Both may reduce Focus/performance degradation during prolonged professional reasoning or vigilance; context and source of degradation must remain explicit. |
| PASSIVE_REC_0001 — Second Wind | PASSIVE_SYN_0005 — Recovery Channel | **SAME_TERM** | Shared same-term group(s): SAME_STAMINA_RECOVERY. Use one capped resolver when both are eligible in the same transaction. |
| PASSIVE_REC_0003 — Deep Recovery | PASSIVE_REC_0006 — Sleep Efficiency | **SAME_TERM** | Shared same-term group(s): SAME_FOCUS_RECOVERY. Use one capped resolver when both are eligible in the same transaction. |
| PASSIVE_REC_0004 — Heat Recovery | PASSIVE_RES_0001 — Heat Resistance | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_HEAT_EXPOSURE. Keep stages separate. |
| PASSIVE_REC_0004 — Heat Recovery | PASSIVE_SUR_0001 — Heat Tolerance | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_HEAT_EXPOSURE. Keep stages separate. |
| PASSIVE_REC_0005 — Cold Recovery | PASSIVE_RES_0002 — Cold Resistance | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_COLD_EXPOSURE. Keep stages separate. |
| PASSIVE_REC_0005 — Cold Recovery | PASSIVE_SUR_0002 — Cold Tolerance | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_COLD_EXPOSURE. Keep stages separate. |
| PASSIVE_REC_0006 — Sleep Efficiency | PASSIVE_SUR_0006 — Sleep Scarcity Tolerance | **CHAIN_INTERACTION** | Sleep Efficiency improves restorative value when sleep is adequate; Sleep Scarcity Tolerance mitigates short-term limited-sleep performance loss. |
| PASSIVE_RES_0001 — Heat Resistance | PASSIVE_SUR_0001 — Heat Tolerance | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_HEAT_EXPOSURE, CHAIN_ENVIRONMENT_ADAPTATION. Keep stages separate. |
| PASSIVE_RES_0002 — Cold Resistance | PASSIVE_SUR_0002 — Cold Tolerance | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_COLD_EXPOSURE, CHAIN_ENVIRONMENT_ADAPTATION. Keep stages separate. |
| PASSIVE_RES_0005 — Toxin Resistance | PASSIVE_SUR_0007 — Toxin Familiarity | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_TOXIN. Keep stages separate. |
| PASSIVE_RES_0008 — Fear Resistance | PASSIVE_WIL_0002 — Fear Processing | **CHAIN_INTERACTION** | Fear Resistance reduces disruption during familiar fear stimuli; Fear Processing improves decision recovery after fear is recognized/processed. |
| PASSIVE_SEN_0008 — Range Estimation | PASSIVE_WPN_0003 — Polearm Reach | **CHAIN_INTERACTION** | Range Estimation supplies observed distance; Polearm Reach uses practiced equipment spacing. |
| PASSIVE_SOC_0001 — Calm Presence | PASSIVE_WIL_0001 — Stress Lock | **CHAIN_INTERACTION** | Shared chain group(s): CHAIN_STRESS_COMPOSURE. Keep stages separate. |
| PASSIVE_SOC_0004 — Negotiation Stamina | PASSIVE_WIL_0010 — Cognitive Endurance | **SAME_TERM** | Shared same-term group(s): SAME_FOCUS_COST. Use one capped resolver when both are eligible in the same transaction. |
| PASSIVE_SOC_0005 — Social Recovery | PASSIVE_WIL_0009 — Emotional Recovery | **PARTIAL_SAME_TERM** | A demanding social encounter can also be an intense emotional event, so both may touch return-to-baseline recovery; Social Recovery remains context-specific. |
| PASSIVE_SYN_0003 — Cast Stability | PASSIVE_WIL_0004 — Focus Under Fire | **CHAIN_INTERACTION** | Focus Under Fire protects concentration under external threat; Cast Stability governs primary-ability technique instability. |
| PASSIVE_SYN_0007 — Dual-Task Control | PASSIVE_WIL_0005 — Interruption Resistance | **CHAIN_INTERACTION** | Interruption Resistance reduces task-progress loss from minor interruptions; Dual-Task Control reduces performance loss while intentionally maintaining two tasks. |
| PASSIVE_TEC_0009 — Calibration Patience | PASSIVE_WIL_0006 — Patience Engine | **PARTIAL_SAME_TERM** | Both may reduce Focus/performance degradation during long calibration/precision work; Calibration Patience is technical-task specific. |

## Highest-priority design review

`PASSIVE_FAC_0006 Chain Familiarity` ↔ `PASSIVE_LDR_0010 Chain-of-Command Fluency` is flagged `POTENTIAL_DUPLICATE_REVIEW`.

Before either record is canon-promoted, decide whether:
1. Faction/Institutional owns **institution-specific responsibility-chain procedure**, while Leadership owns **command execution/coordination under formal authority**; or
2. one record is deprecated with its stable ID reserved.

Do not keep both as effectively identical bonuses.

## Implementation gate

No implementation mapping should combine overlap candidates until this adjudication and the parent cross-family composition standard are applied.

No passive is canon-promoted by this audit.

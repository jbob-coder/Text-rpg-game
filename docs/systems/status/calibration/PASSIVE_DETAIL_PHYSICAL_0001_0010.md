# THE GAME — Passive Detail Wave 001: Physical Adaptation 0001–0010

Status: **RECONSTRUCTION-GRADE CALIBRATION DRAFT / NOT CANON UNTIL PROMOTED / NOT IMPLEMENTED**

Parents:
- `../PASSIVE_REGISTRY_SCHEMA.md`
- `../PASSIVE_REQUIREMENT_LANGUAGE.md`
- `../STATUS_KNOWLEDGE_VISIBILITY_STANDARD.md`
- `PASSIVES_WAVE_001.md`
- `PASSIVE_UNLOCK_PATHS_WAVE_001.md`
- `PASSIVE_KNOWLEDGE_WAVE_001.md`

Purpose: deepen the first ten Physical Adaptation passive records and prove the full authoring pattern before scaling refinement across the remaining 220 passives.

Global rules:
- hidden requirements remain hidden from the player until qualification/discovery permits disclosure;
- numeric thresholds remain calibration proposals;
- self-harm, trivial repetition, save/reload duplication, and engineered exploit loops do not count;
- no passive is canon until explicitly promoted.

---

## PASSIVE_PHY_0001 — Iron Tendons

### Identity
- family: `physical_adaptation`
- tags: `[tendon, load_tolerance, conditioning, injury_prevention]`
- version: `0.1-calibration`
- design status: `CALIBRATION_PROPOSAL`
- canon status: `NOT_CANON_UNTIL_PROMOTED`
- implementation status: `NOT_IMPLEMENTED`

### Effect
- summary: reduces tendon-strain accumulation during repeated high-load movement;
- mechanical intent: raises the sustainable workload before tendon-strain penalties begin, without increasing raw muscle strength;
- scaling: `TBD`; should scale from adaptation history rather than Level alone;
- stack rule: does not stack additively with duplicate copies;
- cap rule: must never remove tendon-injury risk;
- activation: always-on when relevant;
- resources affected: injury/strain state, indirect stamina preservation;
- world effect: improves long-duration high-load work/training;
- tactical effect: slightly delays degradation during repeated explosive actions, but does not grant burst power.

### Acquisition
Linked proposal: `UNLOCK_PHY_0001`.

Internal requirement:
`all(activity_sessions >= 8, intensity_min = high_but_legitimate, recovery_completed >= 4, no_catastrophic_injury = true)`

Difficulty: moderate disciplined conditioning.
Risk: overuse/injury if training is rushed.
Lethal-risk expectation: low under legitimate training; not a design target.
Recovery burden: meaningful.
Exploit control: self-damage and trivial load loops excluded.

### Visibility
Before qualification: fully hidden.
On qualification: reveal to owner.
Exact threshold: not automatically shown.
Knowledge link: `KNOW_PHY_0001`.

### Knowledge
- public: known in broad method;
- school: known;
- government: known;
- military/security: `TBD`;
- research: `TBD`;
- faction: mixed;
- classified level: none by default;
- false rumors: `TBD`;
- historical cases: `TBD`.

### Significance
- prevalence: expected non-unique;
- requirement rarity: low-to-moderate;
- power significance: low individually, strong over long training careers;
- secrecy: low;
- danger: low if trained correctly;
- historical uniqueness: none authored.

### Interactions
Synergizes with load-bearing, grip endurance, sprint economy, weapon retention, and physically demanding professions. Must not multiply injury resistance into immunity.

### Evolution
No evolution authored. A future advanced version may improve adaptation efficiency, but must preserve injury realism.

### Implementation/content needs
Strain-state hooks, training-session evidence, recovery-state evidence, anti-farm checks, reveal event, and at least one tutorial/example distinguishing adaptation from instant stat gain.

---

## PASSIVE_PHY_0002 — Dense Bone

### Identity
- family: `physical_adaptation`
- tags: `[bone, fracture_resistance, conditioning, recovery]`
- version/statuses: `0.1-calibration / CALIBRATION_PROPOSAL / NOT_CANON_UNTIL_PROMOTED / NOT_IMPLEMENTED`

### Effect
Improves resistance to fracture and skeletal stress after legitimate long-term loading adaptation.

Mechanical constraints:
- does not increase muscle force;
- does not prevent joint, organ, or soft-tissue injury;
- does not make bones unbreakable;
- scaling/cap: `TBD`;
- activation: always-on.

### Acquisition
Link: `UNLOCK_PHY_0002`.
Requirement:
`all(activity_sessions >= 9, intensity_min = high_but_legitimate, recovery_completed >= 5, no_catastrophic_injury = true)`

Training must include recovery and progressive loading. Repeated intentional fracture or unsafe self-harm is explicitly invalid.

### Visibility / knowledge
Knowledge link: `KNOW_PHY_0002`.
Public: rumored.
School/government: known.
Faction: known.
Military/research: `TBD`.
Public rumor is incomplete and must not expose the exact threshold.

### Significance
Prevalence moderate; secrecy low; power significance moderate for careers with impact/load exposure; danger arises mainly from unsafe training.

### Interactions
Pairs with Skin Reinforcement or Impact Cushion only as separate systems; combined defenses must still permit internal injury and overload.

### Evolution
None authored.

### Implementation/content needs
Bone-stress/injury model integration, training provenance, medical recovery checks, anti-self-harm rule, and fracture-resolution tests when implemented.

---

## PASSIVE_PHY_0003 — Efficient Recruitment

### Identity
- tags: `[neuromuscular, efficiency, strength_expression, technique]`
- statuses: calibration proposal only.

### Effect
Improves how efficiently the character recruits already available muscle during trained movement patterns.

Does:
- reduce wasted effort;
- improve consistency of force expression;
- modestly improve performance in practiced movement.

Does not:
- create new muscle mass;
- bypass Might/strength development;
- apply equally to unfamiliar movement.

Scaling is familiarity-dependent and `TBD`.

### Acquisition
Link: `UNLOCK_PHY_0003`.
Requirement:
`all(activity_sessions >= 10, intensity_min = high_but_legitimate, recovery_completed >= 6, no_catastrophic_injury = true)`

### Visibility / knowledge
Link: `KNOW_PHY_0003`.
Public unknown; school rumored; government known; faction secret. Military/research `TBD`.

### Risk / exploit control
Meaningful progressive training required. Repeating a zero-challenge motion does not qualify. Injury and overtraining reduce or invalidate qualifying evidence.

### Significance
Moderate performance value; low secrecy at full world maturity unless later worldbuilding says otherwise.

### Interactions
Can improve weapon handling, sprint mechanics, lifting technique, and ability-adjacent physical control without modifying the primary ability's law.

### Evolution
Could become movement-specific advanced recruitment profiles; no route approved.

### Implementation needs
Movement-tagged training history, familiarity tracking, performance evaluator hook, and no direct stat mutation.

---

## PASSIVE_PHY_0004 — Load Bearer

### Identity
- tags: `[load, carrying, posture, endurance]`
- statuses: calibration proposal only.

### Effect
Reduces stamina and posture penalties from carrying sustained external load.

Constraints:
- does not reduce the actual mass;
- does not negate encumbrance entirely;
- does not protect against overloaded joints, falls, or crushed tissue;
- applies only within trained load ranges;
- scaling/cap `TBD`.

### Acquisition
Link: `UNLOCK_PHY_0004`.
Requirement:
`all(activity_sessions >= 11, intensity_min = high_but_legitimate, recovery_completed >= 4, no_catastrophic_injury = true)`

### Visibility / knowledge
Link: `KNOW_PHY_0004`.
Public/school unknown; government/faction classified in the current calibration profile. Military/research `TBD`.
This classification is itself a proposal and must be justified during world integration.

### Risk
Unsafe overloading is invalid. Qualification requires completed load-bearing sessions and recovery.

### Significance / interactions
High utility in military, rescue, logistics, construction, exploration, and heavy equipment use. Synergy with Endurance is allowed; direct encumbrance formula remains `TBD`.

### Evolution
None authored.

### Implementation needs
Encumbrance/load-state ownership, posture/fatigue modifiers, qualifying-session recorder, and overload safety tests.

---

## PASSIVE_PHY_0005 — Shock Acclimation

### Identity
- tags: `[impact, acclimation, recovery, stability]`
- statuses: calibration proposal only.

### Effect
Reduces performance loss after repeated non-catastrophic blunt shocks while preserving actual injury risk.

Important distinction:
- this is acclimation to disruption/stagger;
- it is not damage immunity;
- it does not duplicate Impact Cushion;
- internal injury remains authoritative.

### Acquisition
Link: `UNLOCK_PHY_0005`.
Requirement:
`all(activity_sessions >= 12, intensity_min = high_but_legitimate, recovery_completed >= 5, no_catastrophic_injury = true)`

### Visibility / knowledge
Link: `KNOW_PHY_0005`.
Public false belief; school partial; government known; faction mixed. Exact false belief remains `TBD` and must be authored rather than improvised.

### Risk / exploit control
Intentional uncontrolled beatings/self-harm do not count. Valid sources are supervised conditioning or legitimate field history within survivable bounds.

### Significance
Moderate tactical value, potentially strong for contact sports/security/combat roles.

### Interactions
Can reduce stagger duration or task disruption; cannot reduce authoritative injury numbers unless another system does.

### Evolution
None authored.

### Implementation needs
Separate damage vs stagger state, event provenance, supervision/context tags, anti-abuse filter.

---

## PASSIVE_PHY_0006 — Grip Endurance

### Identity
- tags: `[grip, forearm, climbing, weapon_retention]`
- statuses: calibration proposal only.

### Effect
Slows grip-fatigue accumulation during climbing, carrying, tool use, and weapon retention.

Constraints:
- no increase to maximum grip force by itself;
- local fatigue still accumulates;
- nerve/tendon injury remains possible;
- exact reduction/cap `TBD`.

### Acquisition
Link: `UNLOCK_PHY_0006`.
Requirement:
`all(activity_sessions >= 8, intensity_min = high_but_legitimate, recovery_completed >= 6, no_catastrophic_injury = true)`

### Visibility / knowledge
Link: `KNOW_PHY_0006`.
Public/school/government/faction known in existence, but exact hidden qualification remains concealed until permitted.

### Significance / interactions
Useful across climbing, combat, industrial work, rescue, crafting. Strong synergy with Grip Field must be capped so the combination does not erase forearm/tendon limits.

### Evolution
None authored.

### Implementation needs
Grip-specific fatigue channel or tagged stamina cost, qualifying activity evidence, retention/climbing integration tests.

---

## PASSIVE_PHY_0007 — Joint Stability

### Identity
- tags: `[joint, stability, balance, injury_prevention]`
- statuses: calibration proposal only.

### Effect
Improves joint stability under trained ranges of motion and reduces minor instability penalties.

Does not:
- prevent ligament tears;
- protect against extreme leverage;
- restore damaged joints;
- apply fully outside trained ranges.

### Acquisition
Link: `UNLOCK_PHY_0007`.
Requirement:
`all(activity_sessions >= 9, intensity_min = high_but_legitimate, recovery_completed >= 4, no_catastrophic_injury = true)`

### Visibility / knowledge
Link: `KNOW_PHY_0007`.
Public rumored; school/government partial; faction secret. Military/research `TBD`.

### Risk
Qualifying training must prioritize control and recovery. Intentional destabilization/injury farming is invalid.

### Significance / interactions
Useful for athletics, climbing, combat, rehabilitation, and load-bearing. Can reduce minor instability events but never replace injury state.

### Evolution
Potential joint-specific specialization is open, not authored.

### Implementation needs
Joint/injury tags, movement-range context, rehabilitation compatibility, hidden progress.

---

## PASSIVE_PHY_0008 — Sprint Economy

### Identity
- tags: `[sprint, stamina, locomotion, conditioning]`
- statuses: calibration proposal only.

### Effect
Reduces stamina cost of repeated sprint mechanics after extensive conditioning.

Boundaries:
- does not directly raise top speed;
- does not remove heat, oxygen, muscle, or recovery limits;
- strongest for practiced locomotion conditions;
- scaling `TBD`.

### Acquisition
Link: `UNLOCK_PHY_0008`.
Requirement:
`all(activity_sessions >= 10, intensity_min = high_but_legitimate, recovery_completed >= 5, no_catastrophic_injury = true)`

### Visibility / knowledge
Link: `KNOW_PHY_0008`.
Public/school/government/faction currently unknown in calibration profile. This unusual knowledge state must be justified or revised during audit.

### Significance / interactions
Strong exploration/combat-mobility utility; synergizes with Agility/Endurance training but must not replace movement skill.

### Evolution
None authored.

### Implementation needs
Sprint stamina-cost hook, conditioning evidence, terrain-context validation, heat/recovery interaction.

---

## PASSIVE_PHY_0009 — Core Bracing

### Identity
- tags: `[core, brace, lifting, impact]`
- statuses: calibration proposal only.

### Effect
Improves trunk stabilization against sudden force and heavy lifting.

Constraints:
- no blanket damage reduction;
- requires an appropriate brace opportunity;
- cannot stop overwhelming force;
- poor timing can still fail.

### Acquisition
Link: `UNLOCK_PHY_0009`.
Requirement:
`all(activity_sessions >= 11, intensity_min = high_but_legitimate, recovery_completed >= 6, no_catastrophic_injury = true)`

### Visibility / knowledge
Link: `KNOW_PHY_0009`.
Public/school known; government has classified detail; faction mixed. Exact restricted detail remains `TBD`.

### Significance / interactions
Useful in lifting, grappling, recoil management, impact preparation, rescue. Synergizes with Guard/Brace behaviors but not with surprise attacks where no brace occurs.

### Evolution
None authored.

### Implementation needs
Anticipation/brace state, force event timing, posture condition, training evidence.

---

## PASSIVE_PHY_0010 — Repetition Tolerance

### Identity
- tags: `[repetition, work_capacity, endurance, familiar_task]`
- statuses: calibration proposal only.

### Effect
Reduces performance decay from repeated familiar physical work while preserving recovery requirements.

Boundaries:
- applies only to familiar repeated work patterns;
- does not raise peak output;
- does not erase sleep/nutrition/recovery needs;
- does not protect against overuse injury.

### Acquisition
Link: `UNLOCK_PHY_0010`.
Requirement:
`all(activity_sessions >= 12, intensity_min = high_but_legitimate, recovery_completed >= 4, no_catastrophic_injury = true)`

### Visibility / knowledge
Link: `KNOW_PHY_0010`.
Public false belief; school rumored; government classified; faction secret. False theory and classification rationale remain `TBD`.

### Significance / interactions
High economic/professional utility; useful for manufacturing, logistics, training, farming, rescue, and long operations. Must not become generic unlimited stamina.

### Evolution
No route authored.

### Implementation needs
Task-familiarity tagging, repetition counters, fatigue curve integration, recovery gate, exploit checks.

---

# Family-level consistency rules

All ten Physical Adaptation records must obey:
1. adaptation is earned through legitimate history, not granted instantly;
2. passives modify performance/state resolution, not primary ability identity;
3. hidden progress remains engine-authoritative and player-invisible until legitimately revealed;
4. injury remains real; these passives may reduce strain or improve tolerance but do not create invulnerability;
5. duplicated effects must be reviewed against stats, equipment, primary abilities, and other passives;
6. numeric thresholds in `PASSIVE_UNLOCK_PATHS_WAVE_001.md` are calibration proposals and require later balance validation;
7. knowledge profiles are worldbuilding placeholders until mapped to named institutions/factions.

# Next refinement gate

Before these ten passives can be promoted:
- define exact scaling/cap rules;
- complete military/research knowledge fields;
- author false rumors where referenced;
- map historical cases or explicitly record none known;
- connect each passive to actual runtime state owners;
- define tests for hidden progress, reveal timing, save persistence, and anti-farm behavior;
- run overlap review against recovery, resistance, injury, profession, and combat passive families.

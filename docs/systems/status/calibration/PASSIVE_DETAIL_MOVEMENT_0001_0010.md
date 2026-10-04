# THE GAME — Passive Detail Wave 001: Movement 0001–0010

Status: **RECONSTRUCTION-GRADE CALIBRATION DRAFT / NOT CANON UNTIL PROMOTED / NOT IMPLEMENTED**

Parents:
- `../PASSIVE_REGISTRY_SCHEMA.md`
- `../PASSIVE_REQUIREMENT_LANGUAGE.md`
- `../STATUS_KNOWLEDGE_VISIBILITY_STANDARD.md`
- `PASSIVES_WAVE_001.md`
- `PASSIVE_UNLOCK_PATHS_WAVE_001.md`
- `PASSIVE_KNOWLEDGE_WAVE_001.md`

Purpose: deepen Movement 0001–0010 into bounded, reconstructable movement adaptations without turning passives into superhuman movement abilities.

Global rules:
- all ten remain calibration proposals;
- exact unlock thresholds in the compact wave remain balance proposals;
- trivial repetition, unsafe self-endangerment, and save/reload duplication do not count;
- hidden progress remains player-invisible before legitimate qualification;
- movement passives improve trained execution, efficiency, or recovery; they do not grant a second primary ability;
- Level does not directly scale them unless later approved.

## PASSIVE_MOV_0001 — Sure Foot

Identity:
- family: `movement`
- tags: `[footing, balance, terrain, traversal]`

Effect:
Reduces slips and minor footing errors on familiar unstable terrain by improving trained placement and weight transfer.

Does:
- improve stability on familiar loose/uneven surfaces;
- reduce minor correction cost;
- improve consistency during ordinary traversal.

Does not:
- make every surface safe;
- negate severe environmental hazards;
- prevent falls caused by overwhelming force;
- replace Perception or Traversal skill.

Acquisition:
Linked proposal: `UNLOCK_MOV_0001`.
Qualifying history should include varied legitimate traversal sessions and successful footing corrections. Repeating a trivial safe step does not qualify.

Visibility/knowledge:
Linked profile: `KNOW_MOV_0001`.
Before qualification: hidden.
After qualification: reveal according to Status rules.

Significance:
Broad practical value; expected non-unique; low secrecy if world institutions teach terrain movement.

Interactions:
Agility, Perception, Traversal, footwear/equipment, environmental conditions.

Evolution:
None authored.

Implementation needs:
surface familiarity, movement failure classification, traversal evidence, anti-farm validation, bounded resolver modifier.

## PASSIVE_MOV_0002 — Quiet Landing

Identity:
- tags: `[landing, noise, impact_control, stealth]`

Effect:
Reduces noise and unnecessary impact during controlled landings that are already within the character's trained survivable envelope.

Does:
- improve landing posture/timing;
- reduce avoidable landing noise;
- reduce unnecessary movement disruption.

Does not:
- make unsafe heights safe;
- negate authoritative fall consequences;
- create silence;
- replace Stealth skill.

Acquisition:
Linked proposal: `UNLOCK_MOV_0002`.
Only legitimate controlled landing practice and field use count. Dangerous height escalation is not a valid optimization route.

Visibility/knowledge:
`KNOW_MOV_0002`.

Significance:
Useful for exploration, stealth, athletics, rescue, and occupational movement.

Interactions:
Agility, Traversal, Stealth, footwear, carried load, terrain.

Evolution:
None authored.

Implementation needs:
landing context, noise resolver, valid-height/training envelope, movement evidence, exploit checks.

## PASSIVE_MOV_0003 — Lateral Burst

Identity:
- tags: `[lateral, first_step, agility, acceleration]`

Effect:
Improves first-step efficiency when initiating a practiced lateral movement.

Does:
- reduce hesitation/wasted motion;
- improve force transfer into the first lateral step;
- improve response quality in familiar movement patterns.

Does not:
- directly raise top speed;
- grant teleportation or dash mechanics;
- ignore traction or body mechanics;
- apply fully to unfamiliar movement.

Acquisition:
`UNLOCK_MOV_0003`.
Requires meaningful lateral movement success across training/field contexts rather than repeated zero-pressure side steps.

Visibility/knowledge:
`KNOW_MOV_0003`.

Significance:
Moderate tactical and athletic utility.

Interactions:
Agility, Athletics, Traversal, combat footwork, terrain traction.

Evolution:
None authored.

Implementation needs:
movement-initiation state, direction tags, familiarity state, first-step cost/timing resolver.

## PASSIVE_MOV_0004 — Balance Recovery

Identity:
- tags: `[balance, recovery, stumble, posture]`

Effect:
Shortens recovery from non-injury balance loss by improving trained postural correction.

Does:
- reduce time/cost to regain stable movement after a minor stumble;
- improve transition back into locomotion.

Does not:
- cancel actual injury;
- ignore severe displacement;
- prevent every knockdown;
- restore balance while unconscious or otherwise unable to act.

Acquisition:
`UNLOCK_MOV_0004`.
Qualifying evidence comes from legitimate balance challenges and successful recoveries, not engineered repeated falls.

Visibility/knowledge:
`KNOW_MOV_0004`.

Significance:
Broad mobility value; current compact classification appears unusually secretive and requires review.

Interactions:
Agility, Traversal, conditions affecting balance, equipment/load, combat displacement.

Evolution:
None authored.

Implementation needs:
separate balance-loss versus injury/knockdown state, recovery timing authority, movement evidence.

## PASSIVE_MOV_0005 — Vault Habit

Identity:
- tags: `[vault, obstacle, efficiency, traversal]`

Effect:
Reduces stamina and hesitation cost for practiced vaulting motions over appropriate obstacles.

Does:
- improve consistency and economy;
- reduce unnecessary setup in familiar vault patterns.

Does not:
- allow vaulting obstacles outside physical capability;
- ignore carried load, reach, traction, or injury;
- replace obstacle evaluation.

Acquisition:
`UNLOCK_MOV_0005`.
Meaningful vault practice must vary enough to demonstrate actual skill adaptation; trivial obstacle loops do not qualify.

Visibility/knowledge:
`KNOW_MOV_0005`.

Significance:
Useful for exploration, urban traversal, athletics, emergency movement.

Interactions:
Agility, Athletics, Traversal, load state, obstacle geometry.

Evolution:
None authored.

Implementation needs:
obstacle/vault classification, stamina-cost hook, familiarity state, invalid repetition filter.

## PASSIVE_MOV_0006 — Climb Economy

Identity:
- tags: `[climbing, stamina, route_familiarity, traversal]`

Effect:
Reduces stamina waste during sustained climbing on familiar surface/route classes.

Does:
- improve pacing and movement economy;
- reduce unnecessary grip/posture expenditure.

Does not:
- increase maximum grip force by itself;
- ignore route difficulty;
- negate fall risk;
- remove equipment requirements;
- grant wall-clinging.

Acquisition:
`UNLOCK_MOV_0006`.
Requires legitimate climbing history with meaningful route completion and safe recovery.

Visibility/knowledge:
`KNOW_MOV_0006`.

Significance:
High exploration/rescue/professional value.

Interactions:
Grip Endurance, Athletics, Traversal, equipment, terrain familiarity, stamina.

Evolution:
None authored.

Implementation needs:
climb-specific stamina channel/tags, route familiarity, grip/fatigue interaction, equipment context.

## PASSIVE_MOV_0007 — Terrain Reader

Identity:
- tags: `[terrain, route_selection, perception, traversal]`

Effect:
Improves movement-line selection after observing terrain hazards and possible routes.

Does:
- reduce avoidable route-selection mistakes;
- improve expected efficiency/safety of a chosen line when enough terrain information is available.

Does not:
- reveal hidden terrain automatically;
- guarantee the best route;
- replace Investigation/Perception;
- predict future terrain changes perfectly.

Acquisition:
`UNLOCK_MOV_0007`.
Requires varied terrain observation followed by meaningful movement outcomes. Pure observation without applied traversal is insufficient.

Visibility/knowledge:
`KNOW_MOV_0007`.

Significance:
Strong exploration and tactical-positioning utility without direct speed gain.

Interactions:
Perception, Investigation, Traversal, world map/environment tags, hazards.

Evolution:
None authored.

Implementation needs:
terrain observation state, route-choice context, hazard visibility, evidence linking observation to traversal outcome.

## PASSIVE_MOV_0008 — Long Stride

Identity:
- tags: `[travel, gait, endurance, efficiency]`

Effect:
Improves long-distance walking/running efficiency without directly increasing top speed.

Does:
- reduce avoidable energy cost over sustained travel;
- improve gait economy over familiar movement conditions.

Does not:
- create unlimited stamina;
- raise sprint speed;
- erase sleep, nutrition, heat, terrain, or recovery demands;
- apply equally under every load/terrain condition.

Acquisition:
`UNLOCK_MOV_0008`.
Requires meaningful accumulated travel with adequate recovery and varied legitimate conditions.

Visibility/knowledge:
`KNOW_MOV_0008`.
The current “unknown everywhere” knowledge posture is likely too strong for a broadly trainable movement adaptation and should be reviewed.

Significance:
High exploration/logistics value; low direct combat power.

Interactions:
Endurance, Athletics, Traversal, load, environment, Sprint Economy.

Evolution:
None authored.

Implementation needs:
travel-distance/context evidence, locomotion stamina resolver, gait familiarity, heat/load interaction.

## PASSIVE_MOV_0009 — Fall Roll

Identity:
- tags: `[landing, roll, force_distribution, traversal]`

Effect:
Improves controlled distribution of force during survivable falls where a valid landing/roll opportunity exists.

Does:
- reduce avoidable landing disruption within a trained envelope;
- improve transition from landing into recovery/movement.

Does not:
- negate dangerous fall energy;
- make extreme falls survivable by default;
- replace injury resolution;
- activate when terrain/body position makes a roll impossible.

Acquisition:
`UNLOCK_MOV_0009`.
Only supervised/legitimate movement practice and naturally occurring survivable events count. Deliberate unsafe falls are explicitly invalid evidence.

Visibility/knowledge:
`KNOW_MOV_0009`.

Significance:
Important traversal/rescue/athletic utility with meaningful safety boundaries.

Interactions:
Quiet Landing, Balance Recovery, Impact Cushion, Agility, Traversal, injury system.

Evolution:
None authored.

Implementation needs:
fall severity/envelope, landing opportunity, injury resolver separation, valid training provenance, anti-self-harm filter.

## PASSIVE_MOV_0010 — Direction Change

Identity:
- tags: `[turning, momentum, agility, footwork]`

Effect:
Reduces avoidable momentum loss during practiced rapid changes of direction.

Does:
- improve foot placement and body alignment;
- preserve more useful speed through a practiced change of direction.

Does not:
- cancel inertia;
- enable impossible turn radius;
- ignore traction;
- grant Momentum Bank or other kinetic ability behavior.

Acquisition:
`UNLOCK_MOV_0010`.
Requires meaningful direction-change practice under varied legitimate movement conditions.

Visibility/knowledge:
`KNOW_MOV_0010`.
Current misinformation/secrecy posture requires justification during knowledge audit.

Significance:
Moderate athletics/combat/traversal utility.

Interactions:
Agility, Athletics, Traversal, Lateral Burst, terrain traction, carried load.

Evolution:
None authored.

Implementation needs:
direction-change event classification, incoming/outgoing velocity state, traction, familiarity, stamina/momentum resolver.

# Family-level consistency rules

Movement 0001–0010 must obey:
1. no passive grants supernatural locomotion by itself;
2. top speed, jump height, fall tolerance, inertia, traction, injury, and stamina remain authoritative systems;
3. familiarity/context matters where stated;
4. duplicate ownership never stacks;
5. passives that touch the same movement resolver use capped composition rather than multiplicative stacking;
6. hidden qualification evidence remains engine-authoritative and absent from normal player projection;
7. unsafe self-endangerment is never the optimal unlock path;
8. exact compact-wave thresholds remain calibration proposals.

# Primary overlap watchlist

- Sure Foot ↔ Balance Recovery — prevention versus post-loss recovery.
- Quiet Landing ↔ Fall Roll — controlled low-impact landing/noise versus survivable-fall force distribution.
- Lateral Burst ↔ Direction Change — movement initiation versus preserving momentum during an existing turn.
- Vault Habit ↔ Climb Economy — discrete obstacle traversal versus sustained climb economy.
- Terrain Reader ↔ sensory/investigation passives — route choice support must not become hidden-hazard detection.
- Long Stride ↔ Sprint Economy — sustained travel efficiency versus repeated sprint efficiency.

# Promotion blockers

Before canon promotion:
- exact scaling/caps;
- stacking order;
- authoritative movement-state owners;
- knowledge-profile review;
- world institutions/training sources;
- numeric unlock calibration;
- save/projection/test mapping.

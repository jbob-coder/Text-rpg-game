# THE GAME — Passive Detail Wave 001: Sensory 0001–0010

Status: **RECONSTRUCTION-GRADE CALIBRATION DRAFT / NOT CANON UNTIL PROMOTED / NOT IMPLEMENTED**

Parents:
- `../PASSIVE_REGISTRY_SCHEMA.md`
- `../PASSIVE_REQUIREMENT_LANGUAGE.md`
- `../STATUS_KNOWLEDGE_VISIBILITY_STANDARD.md`
- `PASSIVES_WAVE_001.md`
- `PASSIVE_UNLOCK_PATHS_WAVE_001.md`
- `PASSIVE_KNOWLEDGE_WAVE_001.md`

Purpose: deepen Sensory 0001–0010 into bounded adaptations that improve interpretation of available sensory input without creating supernatural perception by default.

Global rules:
- all remain calibration proposals;
- exact compact-wave thresholds remain balance proposals;
- false-positive review is required because better sensitivity without discrimination creates bad information;
- hidden progress remains invisible before qualification;
- these passives do not automatically create new sensory organs or new physical signal channels;
- ability-assisted input may be improved only where explicitly stated;
- Level does not directly scale these passives by default.

## PASSIVE_SEN_0001 — Low-Light Acuity

Effect:
Improves visual discrimination in low light while remaining inside ordinary biological/optical limits.

Does:
- improve recognition of contrast/detail when some usable visible light exists;
- reduce avoidable identification errors after adaptation.

Does not:
- provide night vision in total darkness;
- see through obstacles;
- replace Thermal Sight;
- remove glare or eye-injury limits.

Acquisition:
`UNLOCK_SEN_0001`.
Requires legitimate low-light drills and field confirmations with false-positive review. Staring into unsafe light/darkness conditions is not valid evidence.

Knowledge:
`KNOW_SEN_0001`.

Interactions:
Perception, Investigation, Stealth, environmental lighting, vision conditions/equipment.

Implementation needs:
light-level context, visible-information resolver, adaptation/familiarity, false-positive tracking.

## PASSIVE_SEN_0002 — Motion Focus

Effect:
Improves tracking of one moving target amid visual clutter.

Does:
- improve continuity of attention on one already seen target;
- reduce distraction from irrelevant movement.

Does not:
- reveal hidden/invisible targets;
- track unlimited targets;
- predict future motion;
- replace Perception.

Acquisition:
`UNLOCK_SEN_0002`.
Requires repeated meaningful tracking tasks and confirmation review.

Knowledge:
`KNOW_SEN_0002`.

Interactions:
Perception, ranged/combat skills, Investigation, visual clutter, occlusion.

Implementation needs:
target-lock attention state, occlusion rules, clutter level, false-positive/misidentification handling.

## PASSIVE_SEN_0003 — Peripheral Discipline

Effect:
Improves awareness of meaningful movement entering peripheral vision.

Does:
- improve chance/speed of noticing qualifying peripheral movement;
- support attention shifts.

Does not:
- grant 360-degree vision;
- identify unseen details automatically;
- detect motion outside actual visual field;
- override blindness/occlusion.

Acquisition:
`UNLOCK_SEN_0003`.
Requires legitimate drills and field confirmations that distinguish real cues from false movement.

Knowledge:
`KNOW_SEN_0003`.

Interactions:
Perception, threat awareness, combat positioning, visibility/lighting.

Implementation needs:
visual-field model, peripheral cue classification, attention shift, false-positive control.

## PASSIVE_SEN_0004 — Sound Separation

Effect:
Improves separation of overlapping audible sound sources after repeated listening practice.

Does:
- improve identifying distinct sources in a mixed sound field;
- improve attention switching between known/meaningful sources.

Does not:
- increase raw hearing range by default;
- hear through impossible barriers;
- create sonar;
- perfectly isolate arbitrary frequencies.

Acquisition:
`UNLOCK_SEN_0004`.
Requires varied legitimate listening tasks and confirmation against known source truth.

Knowledge:
`KNOW_SEN_0004`.

Interactions:
Perception, Investigation, stealth detection, environmental acoustics, Sound Bend if present.

Implementation needs:
audible-source mix, occlusion/reverberation context, source-separation resolver.

## PASSIVE_SEN_0005 — Scent Memory

Effect:
Improves recognition and recall of previously learned odors.

Does:
- improve matching a present odor to a legitimately learned reference;
- improve short/long-term odor association according to later memory rules.

Does not:
- increase the physical strength/range of smell by default;
- identify unknown chemicals perfectly;
- track a scent trail automatically;
- bypass masks/contamination.

Acquisition:
`UNLOCK_SEN_0005`.
Requires learned odor references and field confirmations.

Knowledge:
`KNOW_SEN_0005`.

Interactions:
Perception, Survival, Investigation, environmental contamination, creature tracking.

Implementation needs:
odor identity/reference memory, contamination/mixing, confidence state.

## PASSIVE_SEN_0006 — Thermal Discrimination

Effect:
Improves discrimination between nearby temperature cues sensed through ordinary means or a compatible ability-assisted channel.

Does:
- improve interpretation of small thermal differences within an available signal;
- improve comparison/classification of observed temperature patterns.

Does not:
- create thermal vision on its own;
- extend sensor range;
- make an inaccurate source accurate;
- grant immunity to heat/cold.

Acquisition:
`UNLOCK_SEN_0006`.
Requires confirmed thermal comparison tasks with false-positive review.

Knowledge:
`KNOW_SEN_0006`.

Interactions:
Thermal Sight, medicine, survival, engineering, environmental sensors.

Implementation needs:
thermal-signal source tags, discrimination threshold, ability-assisted source compatibility.

## PASSIVE_SEN_0007 — Vibration Sense

Effect:
Improves detection and interpretation of repeated vibrations through surfaces the character is physically contacting.

Does:
- improve noticing qualifying repeated vibration patterns;
- improve direction/pattern interpretation where the contact geometry permits.

Does not:
- create ranged seismic vision;
- detect through no contact;
- identify every source;
- bypass damping/soft materials.

Acquisition:
`UNLOCK_SEN_0007`.
Requires contact-based vibration drills and field confirmation.

Knowledge:
`KNOW_SEN_0007`.

Interactions:
Perception, engineering, creature detection, machinery, terrain material.

Implementation needs:
contact state, vibration propagation, damping, source confidence.

## PASSIVE_SEN_0008 — Range Estimation

Effect:
Improves visual distance estimation for observed targets and landmarks.

Does:
- reduce estimation error within practiced distance/visibility conditions;
- improve practical ranging for navigation and aiming support.

Does not:
- provide exact measurement;
- see hidden targets;
- ignore perspective/terrain/visibility;
- replace dedicated instruments.

Acquisition:
`UNLOCK_SEN_0008`.
Requires observed targets with known/confirmed distance truth and review.

Knowledge:
`KNOW_SEN_0008`.
The current “unknown everywhere” posture likely requires revision or strong world justification.

Interactions:
Perception, ranged skill, navigation, mapping, terrain.

Implementation needs:
distance truth, estimation error band, visibility and reference cues.

## PASSIVE_SEN_0009 — Threat Localization

Effect:
Improves speed of locating the likely direction of an **already detected** threat cue.

Does:
- shorten directional localization after a qualifying cue is perceived;
- improve cue-to-direction response.

Does not:
- detect threats that produced no perceivable cue;
- guarantee the cue is truly hostile;
- identify exact attacker position through cover by default;
- replace investigation/target identification.

Acquisition:
`UNLOCK_SEN_0009`.
Requires confirmed cue-direction exercises and real field confirmations with false-positive review.

Knowledge:
`KNOW_SEN_0009`.

Interactions:
Perception, combat awareness, Sound Separation, Peripheral Discipline, conditions affecting senses.

Implementation needs:
detected-cue state, source-direction confidence, threat classification kept separate.

## PASSIVE_SEN_0010 — Detail Retention

Effect:
Improves short-term retention of observed physical details relevant to investigation or navigation.

Does:
- preserve more observed detail for a bounded short interval;
- reduce avoidable loss before note-taking/review.

Does not:
- create photographic memory;
- guarantee details were perceived correctly;
- preserve information indefinitely;
- reveal unseen information.

Acquisition:
`UNLOCK_SEN_0010`.
Requires observation, later confirmation, and false-positive/error review.

Knowledge:
`KNOW_SEN_0010`.

Interactions:
Investigation, Perception, navigation, Memory Echo only as a separate source, note-taking tools.

Implementation needs:
observation event state, short-term retention window, confidence/error tagging, memory handoff.

# Family-level consistency rules

Sensory 0001–0010 must obey:
1. improved interpretation does not equal new signal generation;
2. no passive automatically bypasses darkness, occlusion, range, damping, contamination, or sensory injury;
3. false positives remain possible and review matters;
4. passive confidence must be separable from objective truth;
5. ability-assisted signals must declare compatibility explicitly;
6. duplicate ownership never stacks;
7. same-resolver effects use capped composition;
8. exact unlock thresholds remain calibration proposals.

# Overlap watchlist

- Low-Light Acuity ↔ Thermal Sight — visible-light discrimination versus thermal signal generation/interpretation.
- Motion Focus ↔ Peripheral Discipline — sustained target tracking versus noticing peripheral movement.
- Sound Separation ↔ Threat Localization — separating audible sources versus locating an already detected threat cue.
- Thermal Discrimination ↔ Thermal Sight — interpretation passive versus primary ability input.
- Vibration Sense ↔ Echo Map — contact vibration interpretation versus active echo-based spatial sensing.
- Range Estimation ↔ ranged skills/equipment — learned estimation versus instrumented measurement.
- Detail Retention ↔ cognitive/memory passives — short-term observed physical detail versus broader learning/memory systems.

# Promotion blockers

Before canon promotion:
- exact signal/error models;
- scaling/caps;
- knowledge-profile review;
- authoritative sensory state owners;
- false-positive rules;
- ability-assisted compatibility;
- named institutions/training contexts;
- save/projection/test mapping.

# THE GAME — Primary Ability Detail Wave 001: Uncommon 001–010

Status: **RECONSTRUCTION-GRADE CALIBRATION DRAFT / NOT CANON UNTIL PROMOTED / NOT IMPLEMENTED**

Parents:
- `../PRIMARY_ABILITY_REGISTRY_SCHEMA.md`
- `../ABILITY_RARITY_STANDARD.md`
- `../AWAKENING_EVENT_STANDARD.md`
- `../LEVEL_AND_XP_STANDARD.md`
- `../LEVEL_100_EXCEPTION_STANDARD.md`
- `PRIMARY_ABILITIES_WAVE_001.md`
- `PRIMARY_ABILITY_DETAIL_COMMON_001_010.md`
- `../COMMON_ABILITY_RARITY_OVERLAP_AUDIT_001_010.md`

Purpose: deep-author the ten Uncommon primary-ability calibration records and resolve the Common↔Uncommon adjacency questions identified in the first rarity/overlap audit.

Global rules:
- all records remain proposals;
- exact numeric ranges, mass ceilings, resource costs, and cooldowns remain `TBD` unless owner-approved later;
- Level does not automatically scale ability output until Level rewards are canonically defined;
- every technique must stay inside the parent ability law;
- Level-100 replacement behavior is inherited from the Level-100 standard and is not invented here.

---

## ABILITY_UNC_001 — Vector Nudge

### Identity
- display name: **Vector Nudge**
- aliases: `[]`
- rarity: **Uncommon**
- family: `kinetic`
- stable version: `0.1-calibration`
- design status: `CALIBRATION_PROPOSAL`
- canon status: `NOT_CANON_UNTIL_PROMOTED`
- implementation status: `NOT_IMPLEMENTED`

### Core law
The user alters the direction and, within tighter limits, magnitude of an object's **existing velocity vector** without being able to initiate motion from rest.

### Capability boundaries
- allowed: deflect an already moving object; soften or amplify an existing motion within bounded output; adjust trajectory; redirect a moving thrown object; alter a moving person's path if mass/speed/control permit;
- forbidden: starting a stationary target from rest; sustained telekinesis; freezing motion to absolute zero by default; arbitrary acceleration without an existing motion state; controlling internal body motion through intact matter;
- range: proposed short-to-medium line-of-sight range; exact maximum `TBD`;
- target: already moving discrete object/person within mass/speed limits;
- line of sight: yes by default;
- contact: not required in the current proposal;
- area: single target by default;
- duration: impulse-scale vector correction;
- persistence: altered trajectory persists physically after the correction;
- stacking: repeated corrections may be possible but cost/control burden compounds;
- simultaneous effects: one primary vector correction at a time until later calibrated.

### Common adjacency resolution
Compared with `ABILITY_COM_001 Kinetic Palm`:
- Kinetic Palm can initiate a brief impulse on a stationary target but is touch/near-contact;
- Vector Nudge cannot start stationary motion but can operate at a proposed non-contact LOS range;
- Vector Nudge should have superior moving-target trajectory control;
- Kinetic Palm should have superior immediate contact-force utility.

This distinction is required for Uncommon rarity to remain meaningful.

### Awakening
The first manifestation should occur when an already moving object unexpectedly changes direction or speed near the user. Safe ceremony design should use controlled moving test objects after the initial anomaly is recognized.

### Rarity rationale
Uncommon because the ability manipulates motion remotely and with higher trajectory precision than Common kinetic effects, while retaining the severe restriction that it cannot act on stationary targets.

### Level interaction
- raw vector-change ceiling: `TBD`;
- range growth: not assumed;
- speed/mass tolerance: mastery-related unless later Level rules say otherwise;
- technique capacity: mastery/knowledge driven;
- Level 100: inherited exception only.

### Attribute interactions
- Perception: target acquisition and motion estimation;
- Intellect: trajectory prediction;
- Will: stable correction under stress;
- Agility: user timing and tactical coordination;
- Endurance: repeated-use tolerance;
- Might/Presence: no direct ability-law scaling authored.

### Skill interactions
Tactics, ranged-combat knowledge, sports/ballistics knowledge, engineering/physics knowledge, Powers knowledge.

### Resource model
Focus dominant. High-speed, high-mass, or large-angle corrections should increase burden. Exact cost function `TBD`.

### Mastery structure
1. obvious slow moving target;
2. small angle correction;
3. magnitude adjustment;
4. faster/smaller target control;
5. chained corrections within resource limits.

### Technique direction
Proposed techniques should include:
- simple deflection;
- precision redirect;
- deceleration assist;
- advanced chained trajectory correction.

### Evolution
Any evolution must preserve "existing motion required" unless the evolution explicitly transforms the core law and receives separate rarity review.

### Counters / weaknesses
Stationary targets, LOS denial, excessive speed/mass, cluttered multi-target environments, erratic motion, concentration pressure, decoys.

### Failure / danger
Wrong-vector correction can redirect danger toward allies, accelerate a target unintentionally, destabilize moving people/vehicles, or cause collision cascades.

### World knowledge / law
Likely important to sports, transport safety, security, rescue, and projectile defense. Legal treatment of interfering with vehicles/projectiles must be explicit later.

### Known users
`TBD`.

### Visual / content
Trajectory cue should communicate altered motion without displaying omniscient future paths unless the character legitimately predicts them.

---

## ABILITY_UNC_002 — Heat Shaping

### Identity
- rarity: **Uncommon**
- family: `thermal`
- stable version/status: `0.1-calibration / CALIBRATION_PROPOSAL / NOT_CANON_UNTIL_PROMOTED / NOT_IMPLEMENTED`

### Core law
The user redistributes existing thermal energy between nearby materials, surfaces, or bounded zones without creating net thermal energy.

### Capability boundaries
- may move heat from one valid target/zone to another;
- may warm one region while cooling another;
- cannot generate net heat from nothing;
- cannot reduce a target below physically supported limits without somewhere for energy to go;
- cannot automatically know exact temperature;
- living tissue is a valid but high-risk target only if later safety/target rules approve it;
- range, transfer rate, and total energy moved are `TBD`;
- insulation, vacuum, geometry, and user control affect practical transfer.

### Common adjacency
Unlike `ABILITY_COM_002 Thermal Sight`, Heat Shaping changes thermal state rather than sensing it. Thermal Sight may help a separate user observe outcomes but is not bundled into Heat Shaping.

### Awakening
Nearby surfaces develop an unexpected hot/cold split while total heat remains conserved within the event context. Primary hazard is burns, cold injury, or damage to equipment.

### Rarity rationale
Uncommon because direct thermal redistribution has broader tactical, industrial, medical-support, survival, and environmental consequences than Common sensory heat perception.

### Level / attributes / skills
Intellect and Perception support safe thermal planning; Will supports control; Endurance supports repeated strain. Technical Systems, survival, medicine, materials knowledge, and Powers knowledge are relevant.

### Resource model
Focus + stamina. Transfer rate, temperature differential, thermal mass, and duration should affect cost. The ability does not receive free energy from the Status.

### Mastery
Localized transfer → paired source/sink selection → controlled gradients → sustained balancing → multi-zone shaping.

### Technique direction
- heat pull;
- heat push;
- thermal equalization;
- controlled gradient field.

### Counters / failure
Insulation, large thermal mass, no safe sink/source, vacuum-related transfer constraints, fast-moving targets, concentration disruption.

Failure may cause:
- burns/frost injury;
- unintended brittle materials;
- condensation/steam;
- fire ignition through secondary physics;
- user thermal strain.

### World integration
Heating/cooling, emergency response, industry, food/logistics, medical support, stealth/signature management. Regulations likely matter around people and infrastructure.

### Known users
`TBD`.

### Visual/content
Show source/sink relationship rather than generic fire/ice magic.

---

## ABILITY_UNC_003 — Stonehide

### Identity
- rarity: **Uncommon**
- family: `biological`
- stable version/status: `0.1-calibration / CALIBRATION_PROPOSAL / NOT_CANON_UNTIL_PROMOTED / NOT_IMPLEMENTED`

### Core law
The user temporarily mineralizes layers of their outer skin into a denser armor-like biological-mineral structure.

### Capability boundaries
- self-only;
- outer tissue only;
- does not mineralize internal organs;
- does not heal;
- does not create detached stone projectiles;
- mineralized coverage increases weight and stiffness;
- transition speed, coverage, hardness, and duration `TBD`;
- joints/eyes/airway require safe coverage rules;
- repeated transformation may have metabolic/mineral-resource burdens.

### Common adjacency resolution
Compared with `ABILITY_COM_004 Skin Reinforcement`:
- Skin Reinforcement strengthens existing outer tissue without material conversion;
- Stonehide changes tissue into a mineralized armor state;
- Stonehide should have a higher protection ceiling and more severe weight/stiffness/metabolic tradeoffs;
- Skin Reinforcement should remain more flexible and efficient at lower protection.

This distinction is required before numeric balance is locked.

### Awakening
A small patch of skin mineralizes visibly, commonly on a hand/forearm under stress. Medical staff must verify reversibility and circulation/tissue safety.

### Rarity rationale
Uncommon because it performs temporary biological material transformation rather than simple reinforcement.

### Level / attributes / skills
Endurance supports sustained body burden; Will controls coverage; Agility becomes negatively affected by high coverage. Medicine, defense training, Powers knowledge, and materials knowledge may help.

### Resource model
Stamina + biological/mineral reserve concept; exact physiology `TBD`. The user cannot create unlimited mass without a defined source/balance rule.

### Mastery
Small patch → selective plating → joint-safe patterning → mobile armor → high-coverage emergency state.

### Technique direction
- Stone Patch;
- Jointed Plate;
- Mobile Carapace;
- Heavy Shell.

### Counters / failure
Joint attacks, internal shock, weight, water/airway hazards, heat, immobilization, sustained crushing, unarmored sensory organs.

### World integration
Security, hazardous labor, military, rescue, mining/construction. Medical monitoring and mineral/nutrition consequences require later world design.

### Known users
`TBD`.

### Visual/content
Distinct mineralized pixel-art texture, but not copied from existing franchise designs.

---

## ABILITY_UNC_004 — Motion Trace

### Identity
- rarity: **Uncommon**
- family: `sensory`
- stable version/status: `0.1-calibration / CALIBRATION_PROPOSAL / NOT_CANON_UNTIL_PROMOTED / NOT_IMPLEMENTED`

### Core law
The user perceives short-lived spatial traces associated with recent movement through an area.

### Capability boundaries
- perceives movement paths, not memories, thoughts, identity, or motives;
- traces decay with time;
- overlapping traffic creates ambiguity;
- trace age, range, resolution, and persistence are `TBD`;
- cannot detect a stationary target merely because it exists;
- cannot reconstruct events before the trace persistence window;
- exact phenomenon underlying the trace remains an in-world research question unless later canon defines it.

### Common adjacency
- Echo Map senses present geometry through sound;
- Thermal Sight senses present/recent heat patterns;
- Motion Trace senses an ability-specific residue of movement itself.

This more unusual information domain supports Uncommon classification.

### Awakening
The user sees streaks/paths around recently moving people or objects and may initially confuse them with visual afterimages.

### Rarity rationale
Uncommon because it accesses a less ordinary sensory phenomenon and enables tracking/reconstruction even when no conventional acoustic or thermal trace remains.

### Level / attributes / skills
Perception and Intellect are primary interpretation aids; Will resists overload. Investigation, tracking, forensics, tactics, and Powers knowledge are relevant.

### Resource model
Focus. Wider temporal windows or denser scenes should increase cognitive burden.

### Mastery
Fresh single trace → direction/speed interpretation → overlapping traces → older/weaker trace discrimination → bounded scene reconstruction.

### Technique direction
- Fresh Trail;
- Direction Read;
- Traffic Separate;
- Trace Reconstruction.

### Counters / failure
Crowds, deliberate movement clutter, long delays, teleportation/no ordinary path where applicable, moving environments, focus disruption.

### World integration
Investigation, search/rescue, security, hunting, sports, battlefield tracking. Privacy/evidence law must distinguish trace interpretation from guaranteed historical truth.

### Known users
`TBD`.

### Visual/content
Traces need age/uncertainty cues; UI must avoid presenting inference as confirmed history.

---

## ABILITY_UNC_005 — Blink Step

### Identity
- rarity: **Uncommon**
- family: `spatial`
- stable version/status: `0.1-calibration / CALIBRATION_PROPOSAL / NOT_CANON_UNTIL_PROMOTED / NOT_IMPLEMENTED`

### Core law
The user instantly relocates their body a short distance to a visible, valid, unoccupied destination.

### Capability boundaries
- self-only in the current proposal;
- line of sight required;
- destination must be spatially valid and unoccupied;
- cannot cross sealed spatial barriers solely because the endpoint is visible through an indirect image;
- maximum distance `TBD`;
- carrying/equipment mass rules `TBD`;
- whether touched passengers are ever legal is **not assumed**;
- momentum behavior is a critical unresolved design variable and must be specified before implementation;
- orientation behavior is also `TBD`;
- no long-distance travel.

### Awakening
A short involuntary displacement to a visible nearby point. Ceremony safety requires open buffer space and obstacle-free containment.

### Rarity rationale
Uncommon because even short-range teleportation changes mobility, escape, traversal, and combat positioning in ways Common movement abilities cannot.

### Level / attributes / skills
Agility/Perception support destination selection; Will/Intellect support spatial control. Movement, tactics, navigation, and Powers knowledge are relevant.

### Resource model
Focus + stamina. Distance, carried mass, rapid repetition, and unstable posture may increase cost. Exact model `TBD`.

### Mastery
Short static step → precise landing → combat-timed step → repeated step with recovery → difficult terrain use.

### Technique direction
- Short Blink;
- Precision Landing;
- Evasive Blink;
- Chain Step.

### Counters / failure
LOS denial, enclosed clutter, destination denial, spatial anchors, traps covering valid landing zones, rapid resource pressure.

### Critical implementation blocker
Do not code Blink Step until the design decides:
- momentum preserved/changed/reset;
- collision resolution;
- vertical displacement;
- moving-platform reference frame;
- carried objects;
- partial obstruction;
- what happens if the destination becomes occupied during resolution.

### World integration
Security architecture, sports, rescue, policing, military tactics, prison design, access law.

### Known users
`TBD`.

### Visual/content
Short spatial discontinuity effect; avoid long portal visuals unless a technique specifically requires them.

---

## ABILITY_UNC_006 — Magnetic Grip

### Identity
- rarity: **Uncommon**
- family: `magnetic`
- stable version/status: `0.1-calibration / CALIBRATION_PROPOSAL / NOT_CANON_UNTIL_PROMOTED / NOT_IMPLEMENTED`

### Core law
The user attracts or repels ferromagnetic objects within a bounded magnetic-control field.

### Capability boundaries
- controls ferromagnetic response, not all metals;
- nonmagnetic matter is unaffected directly;
- cannot arbitrarily generate electricity;
- cannot rewrite electronics or data;
- mass and distance strongly reduce controllability;
- field range `TBD`;
- reaction force on the user/environment must be respected unless later physics design explicitly differs;
- simultaneous targets `TBD`;
- target must contain sufficient responsive material.

### Common adjacency
Unlike Thread Command, this does not require flexible lines. Unlike Grip Field, it can operate remotely but only on ferromagnetic matter.

### Awakening
Nearby small ferromagnetic items shift, jump, or repel unpredictably. Event safety must remove dangerous loose metal after detection.

### Rarity rationale
Uncommon because remote material-specific force control has significant tactical and industrial depth.

### Level / attributes / skills
Perception/Intellect support target discrimination; Will controls multi-object force; Endurance helps repeated high-load use. Technical, engineering, crafting, weapons knowledge, and Powers knowledge are relevant.

### Resource model
Focus, with stamina rising for high force/mass. Exact field-energy model `TBD`.

### Mastery
Small object pull → push/pull precision → held hover-like balance through opposing forces if physically legal → multi-object sorting → high-load controlled movement.

### Technique direction
- Metal Pull;
- Repulse;
- Magnetic Hold;
- Field Sort.

### Counters / failure
Nonmagnetic materials, distance, low ferromagnetic content, anchoring, excessive mass, magnetic shielding/field interference if world physics supports it.

### World integration
Manufacturing, salvage, maintenance, security, disarmament, logistics. Firearms/weapons interactions need careful tactical and legal design.

### Known users
`TBD`.

### Visual/content
Effect should identify the controlled metal rather than imply general telekinesis.

---

## ABILITY_UNC_007 — Sound Bend

### Identity
- rarity: **Uncommon**
- family: `acoustic`
- stable version/status: `0.1-calibration / CALIBRATION_PROPOSAL / NOT_CANON_UNTIL_PROMOTED / NOT_IMPLEMENTED`

### Core law
The user redirects, concentrates, disperses, or dampens **existing** sound waves inside a bounded controlled area.

### Capability boundaries
- requires existing acoustic energy;
- cannot create sound from nothing;
- requires a sound-carrying medium;
- does not read thoughts through voice;
- cannot make every sound perfectly silent at arbitrary scale;
- area/range/amplitude ceiling `TBD`;
- extreme amplitude can overwhelm control;
- changing sound path does not change unrelated physical objects except through ordinary acoustic effects.

### Common adjacency
Echo Map emits/interprets sound for sensing. Sound Bend manipulates propagation. It should not automatically grant echolocation.

### Awakening
Voices/noise near the user unexpectedly shift direction, become muffled, or focus into a surprising location.

### Rarity rationale
Uncommon because acoustic-path control supports stealth, communication, defense, misdirection, and high-skill tactical applications.

### Level / attributes / skills
Perception, Intellect, Will. Audio engineering, stealth, communication, tactics, performance, Powers knowledge.

### Resource model
Focus. Larger area, stronger amplitude change, and multiple simultaneous sound sources increase burden.

### Mastery
Single-source redirection → damping → focused delivery → multi-source handling → shaped acoustic zone.

### Technique direction
- Whisper Route;
- Damp Zone;
- Focused Sound;
- Acoustic Screen.

### Counters / failure
Vacuum, overwhelming noise, broad-spectrum chaotic sources, nonacoustic sensors, concentration disruption.

### World integration
Privacy, entertainment, rescue communications, security, espionage, hearing protection. Legal doctrine must distinguish speech redirection from recording.

### Known users
`TBD`.

### Visual/content
Because sound is invisible, UI/FX should communicate player-known acoustic paths without revealing hidden speakers/sources.

---

## ABILITY_UNC_008 — Vapor Sculpt

### Identity
- rarity: **Uncommon**
- family: `vapor`
- stable version/status: `0.1-calibration / CALIBRATION_PROPOSAL / NOT_CANON_UNTIL_PROMOTED / NOT_IMPLEMENTED`

### Core law
The user shapes existing mist, steam, fog, and suspended water vapor into controlled low-density flows and distributions.

### Capability boundaries
- cannot create water mass;
- cannot directly control bulk liquid water;
- does not automatically change temperature or phase;
- no free steam generation;
- strong airflow disrupts control;
- humidity/source density matters;
- volume/range/flow complexity `TBD`;
- distributed vapor can be shaped over an area, but total controlled mass remains bounded.

### Common adjacency resolution
Compared with `ABILITY_COM_008 Water Draw`:
- Water Draw controls denser liquid water but over a short, source-dependent range;
- Vapor Sculpt controls lower-density distributed water suspended through an area;
- Uncommon distinction should come from spatial complexity, multi-point shaping, concealment/airflow interaction, and area coverage—not from raw mass or damage.

This rationale must be preserved during numeric calibration.

### Awakening
Nearby mist, breath condensation, steam, or humid vapor forms an abnormal coherent flow around the user when sufficient vapor exists. In a dry environment the manifestation may be weak and harder to classify.

### Rarity rationale
Uncommon because it can coordinate distributed low-density material across space in ways Water Draw cannot, creating broader control/utility despite lower mass.

### Level / attributes / skills
Perception and Intellect support flow reading; Will controls distributed shapes; Endurance supports duration. Weather knowledge, stealth, rescue, industrial safety, and Powers knowledge are relevant.

### Resource model
Focus dominant; area, turbulence, volume, and precision drive cost.

### Mastery
Local swirl → directional sheet → shape retention → multi-zone distribution → large bounded concealment/flow structure.

### Technique direction
- Mist Gather;
- Vapor Screen;
- Channel Flow;
- Distributed Veil.

### Counters / failure
Dry air, strong wind, ventilation, heat gradients, large open spaces, no vapor source.

### World integration
Fire/industrial safety, cooling/ventilation support, concealment, agriculture, environmental work. Does not grant weather control.

### Known users
`TBD`.

### Visual/content
Vapor density should not become opaque supernatural smoke unless enough physical vapor exists.

---

## ABILITY_UNC_009 — Weight Shift

### Identity
- rarity: **Uncommon**
- family: `gravity_self`
- stable version/status: `0.1-calibration / CALIBRATION_PROPOSAL / NOT_CANON_UNTIL_PROMOTED / NOT_IMPLEMENTED`

### Core law
The user changes their own effective gravitational weight within a bounded positive range.

### Capability boundaries
- self-only;
- changes weight response, not inertial mass;
- does not automatically change gravity direction;
- zero gravity is not assumed;
- negative/reversed gravity is not assumed;
- no external target effect;
- maximum increase/decrease `TBD`;
- duration and transition rate `TBD`;
- traction, momentum, collision, and structural load remain physical consequences.

### Awakening
The user suddenly feels much lighter or heavier, producing an unexpected jump, stumble, fall, or floor-loading event.

### Rarity rationale
Uncommon because direct self-gravity modification enables unusual movement, anchoring, jumping, fall management, and force-transfer strategies while remaining self-limited.

### Level / attributes / skills
Agility/Perception for movement timing; Endurance for high-weight load; Intellect for momentum planning. Athletics, climbing, tactics, Powers knowledge.

### Resource model
Focus + stamina, especially at extreme weight changes or sustained duration.

### Mastery
Small adjustment → rapid switching → movement integration → high/low-weight transitions → complex momentum-aware use.

### Technique direction
- Light Step;
- Heavy Stance;
- Drop Weight;
- Momentum Switch.

### Counters / failure
Inertia, poor traction, weak floors, high-weight joint strain, low-weight vulnerability to external force, confined spaces, concentration loss.

### Rare-tier guardrail
The ability must not expand into external gravity wells or mass inversion. Those laws belong to higher-tier gravity abilities.

### World integration
Construction, rescue, climbing, sports, security, tactical movement. Building/floor safety may matter at high weight.

### Known users
`TBD`.

### Visual/content
Weight changes need movement/impact cues rather than generic gravity auras.

---

## ABILITY_UNC_010 — Knit Flesh

### Identity
- rarity: **Uncommon**
- family: `healing`
- stable version/status: `0.1-calibration / CALIBRATION_PROPOSAL / NOT_CANON_UNTIL_PROMOTED / NOT_IMPLEMENTED`

### Core law
The user accelerates the natural tissue-repair processes of themselves or a directly touched living target.

### Capability boundaries
- contact required for external targets;
- accelerates repair rather than creating arbitrary new anatomy;
- cannot resurrect;
- cannot restore missing organs/limbs by default;
- cannot replace lost blood/nutrients/energy from nothing;
- cannot automatically cure toxins, infection, disease, or genetic conditions;
- poorly aligned tissue can heal incorrectly if stabilization is bad;
- tissue type, injury severity, age, nutrition, circulation, and contamination should matter;
- rate/volume/resource demand `TBD`.

### Awakening
A minor wound begins closing unusually fast, or accidental contact accelerates healing of a small stabilized injury. Medical observation is required to determine the actual ability law.

### Rarity rationale
Uncommon because direct biological healing has high civilian, medical, military, and social value even with strict natural-repair limits.

### Level / attributes / skills
Intellect/Perception support injury assessment; Will supports fine control; Endurance affects user burden. Medicine is especially important: the ability does not grant medical knowledge.

### Resource model
Focus + stamina + target biological reserves. Severe healing may demand calories, hydration, blood supply, rest, and medical stabilization.

### Mastery
Minor superficial repair → controlled soft-tissue healing → deeper stabilized wounds → reduced scarring/repair errors if later approved → multi-stage serious-injury support.

### Technique direction
- Close Cut;
- Tissue Knit;
- Stabilized Repair;
- Recovery Assist.

### Counters / failure
Massive trauma, missing tissue, ongoing bleeding, contamination, poison, poor alignment, insufficient biological resources, interrupted contact.

### Super-Rare adjacency
`ABILITY_SRR_003 Adaptive Regeneration` should remain categorically superior through:
- self-regenerative depth;
- adaptation to survived injury patterns;
- higher restoration speed/scale;
- broader serious-injury capability;
while still respecting its own costs and death boundary.

### Failure / danger
Accelerated incorrect healing, scar formation, trapped contamination, metabolic collapse, masking a deeper injury, exhaustion of patient reserves.

### World integration
Healthcare, emergency response, military medicine, insurance, licensing, malpractice, criminal coercion, sports. Medical regulation is mandatory future world design.

### Known users
`TBD`.

### Visual/content
Healing FX should remain biological and restrained; severe injury should not vanish instantly without corresponding cost/time.

---

# Uncommon slice cross-record audit

## Law uniqueness

No Uncommon 001–010 pair currently shares the same core law.

Closest relationships:
- Vector Nudge / Kinetic Palm: remote existing-motion correction versus near-contact impulse;
- Heat Shaping / Thermal Sight: manipulation versus perception;
- Stonehide / Skin Reinforcement: mineral transformation versus tissue reinforcement;
- Motion Trace / Echo Map: movement-residue sensing versus acoustic geometry;
- Magnetic Grip / Thread Command: ferromagnetic force versus flexible-line control;
- Sound Bend / Echo Map: acoustic manipulation versus acoustic sensing;
- Vapor Sculpt / Water Draw: suspended vapor-area control versus bulk liquid movement;
- Weight Shift / higher gravity: self-weight only versus external gravity;
- Knit Flesh / Adaptive Regeneration: externally usable natural-repair acceleration versus higher-tier adaptive self-regeneration.

## Rarity-fit result

Provisional:
- Vector Nudge — **PASS if non-contact LOS range is retained**
- Heat Shaping — **PASS**
- Stonehide — **PASS if protection ceiling exceeds Skin Reinforcement with stronger drawbacks**
- Motion Trace — **PASS**
- Blink Step — **PASS, but momentum rules are a blocker**
- Magnetic Grip — **PASS**
- Sound Bend — **PASS**
- Vapor Sculpt — **PASS if distributed-area complexity is the rarity rationale**
- Weight Shift — **PASS**
- Knit Flesh — **PASS**

## Critical blockers before promotion
1. numeric output/range/cost bands;
2. Blink Step momentum/collision/reference-frame rules;
3. Stonehide biological mass/mineral accounting;
4. Static/Lightning and Water/Vapor adjacent numeric calibration;
5. medical safety doctrine for Knit Flesh;
6. historical occurrence/known-user data;
7. institution/legal/world integration.

No Uncommon record is promoted to canon by this file.

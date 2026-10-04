# THE GAME — Rare Ability Detail 006–010

Status: **CALIBRATION DRAFT / NOT CANON / NOT IMPLEMENTED**

Parents:
- `../PRIMARY_ABILITY_REGISTRY_SCHEMA.md`
- `../ABILITY_RARITY_STANDARD.md`
- `PRIMARY_ABILITIES_WAVE_001.md`
- `PRIMARY_ABILITY_DETAIL_COMMON_001_010.md`
- `PRIMARY_ABILITY_DETAIL_UNCOMMON_001_010.md`

Purpose: deepen Rare 006–010 while preserving explicit design blockers.

Global constraints:
- numeric values remain `TBD`;
- Level scaling is not assumed;
- all entries remain `CALIBRATION_PROPOSAL`;
- world-dependent mechanics must stay blocked until their parent world documents exist.

## ABILITY_RAR_006 — Spatial Anchor

Core law:
Fixes a target or bounded zone to a defined local spatial reference, resisting forced displacement and short-range spatial relocation.

Boundaries:
- does not prevent ordinary damage;
- anchor strength is finite;
- reference frame must be defined;
- range, target size, consent/contact/LOS rules, and duration remain `TBD`;
- cannot anchor unlimited scale;
- interaction with higher-tier spatial abilities requires explicit contest rules.

Uncommon adjacency:
`ABILITY_UNC_005 Blink Step` performs short-range self relocation. Spatial Anchor is Rare because it can oppose relocation or displacement for another target or zone.

Critical design blockers:
- local reference frame;
- moving platform/vehicle behavior;
- anchor break threshold;
- interaction with Blink Step, future Fold Step, and future Gate abilities;
- movement outcome when a relocation attempt is denied.

Relevant attributes/skills:
Will, Intellect, Perception; spatial knowledge, Tactics, Engineering, Powers knowledge.

Resource model:
Focus, with possible Resolve interaction for high-strength anchors if later approved.

Progression:
self/object anchor → reference selection → stronger anchor → bounded zone → spatial-effect contest.

Counters:
finite strength, concentration, range, reference complexity, stronger spatial effects.

World roles:
transport safety, secure facilities, containment, rescue, research, anti-spatial doctrine.

Promotion blockers:
reference-frame model and interaction matrix.

## ABILITY_RAR_007 — Memory Echo

Core law:
Reads fragmentary residual impressions associated with emotionally intense past contact on objects or locations.

Boundaries:
- not living mind reading;
- impressions are incomplete and biased;
- no guaranteed identity, chronology, or objective truth;
- residue can decay or overlap;
- cannot alter memories;
- range, persistence, and fidelity are `TBD`.

Rarity rationale:
Rare because it accesses information outside ordinary senses and can materially affect investigation, history, research, and intelligence.

Relevant attributes/skills:
Perception, Intellect, Will; Investigation, History, Empathy, Factions, Powers knowledge.

Resource model:
Focus, with Resolve burden for intense impressions.

Progression:
strong echo → isolate impression → filter overlap → contextual reconstruction → controlled deep reading.

Counters:
weak residue, time decay, overlapping events, deliberate decoys, user bias, missing context.

World roles:
forensics, archives, research, intelligence, history, privacy/evidence systems.

Promotion blockers:
evidence reliability rules, knowledge uncertainty model, historical occurrence.

## ABILITY_RAR_008 — Momentum Bank

Core law:
Absorbs a bounded portion of kinetic energy from qualifying motion events, stores it in a personal kinetic reserve, and later releases that stored energy through controlled output.

Boundaries:
- kinetic energy only;
- cannot absorb static pressure;
- hard reserve ceiling;
- not all incoming energy is necessarily absorbable;
- residual force can still affect the user;
- cannot create net kinetic energy;
- reserve decay, release mode, efficiency, and delivery range remain `TBD`.

Common adjacency resolution:
`ABILITY_COM_009 Impact Cushion` dissipates part of sudden impact and never stores usable kinetic energy. Momentum Bank is Rare because it converts captured motion into a later strategic reserve.

Relevant attributes/skills:
Endurance, Perception, Will, Intellect; Athletics, Defense, Tactics, Powers knowledge.

Resource model:
Kinetic reserve + stamina.

Progression:
small absorption → reserve awareness → controlled release → larger-event capture → multi-event reserve management.

Counters:
static force, non-kinetic effects, reserve saturation, excessive incoming energy, no available motion source.

World roles:
impact safety, transport, industrial work, rescue, research, security.

Promotion blockers:
reserve accounting, release rules, interaction with defensive systems.

## ABILITY_RAR_009 — Umbra Veil

Core law:
Redirects visible light around a bounded subject or area to reduce direct visual detection.

Boundaries:
- visible spectrum by default;
- does not block thermal, acoustic, scent, radar, touch, or other nonvisual detection automatically;
- no perfect all-angle invisibility by default;
- fast movement and changing lighting degrade stability;
- area, subject count, duration, and observer-angle complexity remain `TBD`;
- does not create darkness as a material.

Common adjacency:
`ABILITY_COM_005 Lumen Pulse` emits visible light. Umbra Veil is Rare because it manipulates multi-angle light paths for concealment.

Relevant attributes/skills:
Perception, Intellect, Will, Agility; Stealth, Tactics, Investigation, Powers knowledge.

Resource model:
Focus. Burden rises with area, movement, lighting complexity, and observer geometry.

Progression:
small stationary patch → self veil → slow movement → multi-angle correction → bounded moving concealment.

Counters:
nonvisual sensors, environmental particulates, changing lighting, rapid movement, concentration pressure.

World roles:
security, privacy, rescue, research, entertainment, surveillance/counter-surveillance.

Promotion blockers:
multi-angle visibility model, sensor interaction, legal/world doctrine.

## ABILITY_RAR_010 — Crystal Resonance

Core law:
Senses and alters resonant states in compatible crystalline materials and crystal-based devices.

Boundaries:
- compatible crystalline structure required;
- no general matter control;
- no automatic device understanding;
- cannot create crystal mass;
- can sense, tune, dampen, or excite resonance only inside calibrated limits;
- compatibility taxonomy, range, amplitude, energy coupling, and device consequences remain `TBD`.

World-design dependency:
This record cannot be canon-promoted until THE GAME explicitly defines:
- what crystal materials and devices exist;
- their role in technology and society;
- resonance behavior;
- safety and energy rules.

Do not import crystal lore from another project unless the owner explicitly adopts it into THE GAME.

Rarity rationale:
Potentially Rare because resonance control may have broad technical/material significance, but final classification depends on THE GAME's own crystal canon.

Relevant attributes/skills:
Intellect, Perception, Will; Technical Systems, Engineering, Crafting, materials knowledge, Powers knowledge.

Resource model:
Focus plus any external energy already present in the compatible system.

Progression:
sense → tune/dampen → controlled excitation → multi-component tuning → advanced stable resonance.

Counters:
no compatible material, isolation/damping, distance, unfamiliar structure, mixed materials, overload.

World roles:
`BLOCKED PENDING CRYSTAL WORLD CANON`.

Promotion blockers:
world crystal ontology, device taxonomy, resonance rules, institutional use.

## Rare slice audit

Resolved boundaries:
- Blink Step ↔ Spatial Anchor: relocation versus position-lock/counter-domain.
- Impact Cushion ↔ Momentum Bank: dissipation versus storage/release.
- Lumen Pulse ↔ Umbra Veil: emission versus redirection/concealment.

Provisional rarity:
- Spatial Anchor — PASS, reference-frame blocker.
- Memory Echo — PASS if impressions remain fragmentary.
- Momentum Bank — PASS if reserve ceiling stays hard.
- Umbra Veil — PASS if nonvisual counters stay meaningful.
- Crystal Resonance — CONDITIONAL on THE GAME crystal canon.

No canon promotion is implied.

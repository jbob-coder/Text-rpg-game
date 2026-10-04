# THE GAME — Rare Ability Detail 001–005

Status: **CALIBRATION DRAFT / NOT CANON / NOT IMPLEMENTED**

Parents:
- `../PRIMARY_ABILITY_REGISTRY_SCHEMA.md`
- `../ABILITY_RARITY_STANDARD.md`
- `PRIMARY_ABILITIES_WAVE_001.md`
- `PRIMARY_ABILITY_DETAIL_COMMON_001_010.md`
- `PRIMARY_ABILITY_DETAIL_UNCOMMON_001_010.md`

Purpose: deepen Rare 001–005 without inventing numeric balance.

Global constraints:
- exact ranges, costs, durations, capacities, and thresholds remain `TBD`;
- Level scaling is not assumed until the Level reward model is locked;
- every technique must remain inside the parent ability law;
- all records remain `CALIBRATION_PROPOSAL`.

## ABILITY_RAR_001 — Gravity Well

Core law:
Creates a short-lived localized gravity point that pulls nearby matter toward it.

Boundaries:
- finite radius, strength, and duration;
- no gravity reversal;
- no inertia cancellation;
- no permanent field;
- ordinary environmental consequences still apply;
- exact simultaneous-field count is `TBD`.

Rarity boundary:
- `ABILITY_UNC_009 Weight Shift` is self-only;
- Gravity Well is Rare because it creates an external multi-target field.

Progression:
placement → radius control → strength control → repeated pulses → advanced field timing.

Resources:
Focus-dominant. Cost should scale with field size, strength, affected mass, and duration.

Relevant attributes/skills:
Perception, Intellect, Will; Tactics, Engineering, rescue/physics knowledge, Powers knowledge.

Counters:
range, duration, concentration, environmental complexity, anchored structures.

World roles:
rescue, construction, transport, research, containment, controlled industrial applications.

Promotion blockers:
numeric field model, institutional rules, historical occurrence, known-user records.

## ABILITY_RAR_002 — Phase Edge

Core law:
Creates a thin bounded phase boundary that partially decouples from ordinary matter, allowing controlled penetration through compatible material.

Boundaries:
- thin edge only;
- no full-body intangibility;
- no large-volume phasing;
- no permanent spatial opening;
- stability, length, penetration, and material rules remain `TBD`.

Rarity rationale:
Rare because matter-decoupling creates exceptional precision and access utility while remaining tightly bounded.

Progression:
short edge → stable edge → moving edge → material-aware control → sustained precision.

Resources:
Focus. Cost rises with edge length, duration, material resistance, and precision demand.

Relevant attributes/skills:
Will, Perception, Intellect, Agility; Engineering, materials knowledge, Powers knowledge.

Counters:
small geometry, material resistance, stability limits, concentration burden.

World roles:
research, industrial work, controlled access, specialized technical applications.

Promotion blockers:
material compatibility model, safe-use rules, institutional regulation.

## ABILITY_RAR_003 — Lightning Conduit

Core law:
Routes existing electrical energy through selected conductive paths.

Boundaries:
- requires stored or external energy;
- no unlimited generation;
- no automatic immunity to electrical side effects;
- conductivity, grounding, geometry, and distance matter;
- does not control unrelated technology;
- throughput and path count are `TBD`.

Common adjacency:
- `ABILITY_COM_006 Static Reservoir` stores limited personal charge and uses short discharge;
- Lightning Conduit is Rare because it can route larger existing electrical sources through selected paths.

Progression:
small safe route → selected conductor → controlled branching → sustained route → complex path control.

Resources:
Focus plus available electrical energy.

Relevant attributes/skills:
Intellect, Perception, Will; Technical Systems, Engineering, electrical systems knowledge, Powers knowledge.

Counters:
no source, insulation, grounding, distance, path ambiguity, overload.

World roles:
utilities, infrastructure, maintenance, research, emergency systems.

Promotion blockers:
throughput/path model, reserve interaction, world regulation.

## ABILITY_RAR_004 — Cryo Sink

Core law:
Extracts thermal energy from a target zone and stores part of it in a bounded personal thermal reserve.

Boundaries:
- removes heat rather than creating an independent cold effect;
- reserve has a hard ceiling;
- no instant unlimited cooling;
- transfer geometry, material, insulation, and environment matter;
- reserve capacity and release behavior remain `TBD`.

Uncommon adjacency:
- `ABILITY_UNC_002 Heat Shaping` redistributes heat between external regions;
- Cryo Sink is Rare because it introduces dedicated internal storage and stronger one-sided extraction.

Progression:
small extraction → precision cooling → sustained sink → rapid controlled extraction → reserve management.

Resources:
Focus + thermal reserve.

Relevant attributes/skills:
Perception, Intellect, Will, Endurance; Engineering, Medicine, Survival, Powers knowledge.

Counters:
insulation, thermal mass, limited transfer path, reserve saturation.

World roles:
cold-chain systems, industry, emergency response, medicine, research.

Promotion blockers:
thermal reserve accounting, transfer limits, institutional rules.

## ABILITY_RAR_005 — Bioelectric Overdrive

Core law:
Temporarily amplifies and synchronizes the user's neuromuscular signaling for unusually fast and forceful coordinated movement.

Boundaries:
- self-only;
- tissue durability does not automatically increase;
- no external electrical projection;
- no healing;
- duration, amplification, recovery, and strain remain `TBD`.

Passive distinction:
- `PASSIVE_PHY_0003 Efficient Recruitment` improves trained ordinary recruitment;
- Bioelectric Overdrive actively exceeds ordinary operating levels for a short period and therefore has a larger recovery burden.

Progression:
localized burst → coordinated limb use → whole-body burst → controlled sequence → precision overdrive.

Resources:
Stamina + focus + recovery strain.

Relevant attributes/skills:
Agility, Might, Endurance, Perception, Will; Athletics, Medicine, movement/combat skills, Powers knowledge.

Counters:
strain accumulation, limited duration, recovery windows, poor coordination, existing injury state.

World roles:
research, emergency response, high-performance training, security.

Promotion blockers:
strain/recovery model, numeric amplification limits, medical/world doctrine.

## Slice result

Current adjacency outcomes:
- Weight Shift ↔ Gravity Well: self gravity versus external field.
- Static Reservoir ↔ Lightning Conduit: personal storage/discharge versus routed existing energy.
- Heat Shaping ↔ Cryo Sink: external redistribution versus internal thermal storage.

No canon promotion is implied.

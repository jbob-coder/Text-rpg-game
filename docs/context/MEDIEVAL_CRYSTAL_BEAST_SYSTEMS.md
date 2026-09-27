# Medieval Crystal-Beast Combat, Equipment, and Living-World Contract

Status: [DIRECTION] ACCEPTED / [DESIGNED] NOT IMPLEMENTED

Purpose: define the medieval-era combat, equipment, crystal, beast-progression, and living-world direction without prematurely changing the current V6 runtime. This is design documentation, not an implementation claim.

## 1. World technology and theme

[DIRECTION] Ordinary material culture is medieval: forged metal, leather, wood, cloth, bows, crossbows, polearms, shields, fortifications, mines, workshops, caravans, villages, keeps, roads, forests, caves, and hand-built infrastructure.

[DIRECTION] Crystal power is the exceptional technology layer. It augments medieval craft rather than replacing it with modern or cybernetic technology.

Crystals have two primary sources:

1. Mine crystals — natural deposits extracted from veins, caves, mountains, and deep mines.
2. Beast heart crystals — biologically integrated crystals growing beside or around a beast's heart/core region. They carry stronger species-specific traits but are harder to harvest intact.

[DESIGNED] Mine crystals are generally more stable, predictable, and standardized. Beast crystals are generally more specialized, potent, and behaviorally distinctive.

This supports an economy around miners, hunters, scouts, smiths, crystal appraisers, caravans, guilds, lords, armies, poachers, healers, and beast territories.

## 2. Stat architecture for medieval combat

The current executable seven-stat model remains authoritative until DEC-STAT-001 is resolved. This design maps to it without forcing a migration.

### Current attribute responsibilities

- Might — raw weapon force, grappling pressure, shield impacts, heavy-tool use, armor burden support, breaking objects, forceful control.
- Agility — footwork, balance, recovery, evasive movement, rapid position changes, body control, weapon repositioning under the current seven-stat model.
- Endurance — sustained exertion, injury tolerance, fatigue resistance, prolonged armor use, recovery support, survival under accumulated wounds.
- Intellect — crystal appraisal, forge planning, engineering, beast study, tactical analysis, identifying equipment/crystal interactions.
- Will — pain/fear resistance, concentration, crystal-resonance control, maintaining techniques under stress, resisting mental or resonance disruption.
- Perception — recognizing openings, reading posture, locating weak anatomy, reacting to feints, tracking, ranged target acquisition.
- Presence — command pressure, morale, intimidation, negotiation, leadership, social control of allies, factions, and intelligent beasts.

[DESIGNED] If Dexterity is later split from Agility, fine weapon handling, precision manipulation, difficult crystal fitting, bow/crossbow handling, and exact weak-point work should move primarily to Dexterity while Agility keeps locomotion, balance, evasion, and body positioning.

### Proposed skill expansion

The existing skill catalog should not be silently replaced. Future migration may add or refine:

- blades
- axes_hammers
- polearms
- ranged
- shields / defense
- unarmed / grappling
- athletics
- riding
- stealth
- survival
- tracking
- beast_lore
- tactics
- command
- smithing
- armorsmithing
- crystalcraft
- mining
- appraisal
- field_medicine
- engineering
- crafting

Weapon-family skills represent learned handling and do not replace core attributes.

### Candidate derived combat values

- weapon handling
- attack recovery
- guard integrity
- poise / stagger resistance
- armor burden
- armor penetration support
- break power
- wound resistance
- target acquisition
- ranged stability
- crystal control
- resonance tolerance
- crystal output efficiency
- movement under load

[PROVISIONAL] These should not all become permanent UI numbers. Only values that materially improve player decisions deserve primary display.

## 3. Weapons as forged physical objects

[DIRECTION] Weapons are not interchangeable damage-number containers. Physical form changes what targets they can reach, recovery time, armor interaction, and battle positioning.

Initial weapon families may include sword/longsword, dagger, axe, mace/hammer, spear, halberd/polearm, staff, bow, crossbow, shield, and improvised/tool weapons.

A weapon instance can carry:

- stable item ID
- weapon family
- material
- forge quality
- condition/durability
- weight
- reach
- handling
- balance
- momentum
- guard value
- penetration profile
- cutting / piercing / blunt profile
- stamina burden
- recovery time
- minimum/optimal range
- usable targeting tags
- armor-interaction tags
- crystal housing/socket layout
- integrated crystal IDs
- resonance stability
- active/passive crystal effects
- provenance, smith, and origin

[DIRECTION] Weapon properties create tradeoffs. A heavy war hammer can dominate armor breaking but recover slowly. A spear controls distance and exposes different body zones. A dagger is weak at open reach but strong after a grapple or armor gap creates access.

## 4. Armor and equipment coverage

Armor uses body coverage rather than one universal defense number.

Candidate internal coverage regions:

- head
- face
- neck
- shoulders
- chest
- abdomen
- back
- upper arms
- forearms
- hands
- hips
- thighs
- knees
- shins
- feet

Player-facing equipment slots can remain simpler than the internal coverage model.

Armor may track:

- material/layers
- covered zones
- cut resistance
- pierce resistance
- blunt mitigation
- durability
- weight/burden
- flexibility
- noise
- heat/fatigue burden
- movement penalties
- crystal channels/sockets
- crystal stability
- special protection tags

[DESIGNED] Layering may support cloth/padding, leather, mail, plate, beast hide, or crystal-treated materials, but the first implementation should avoid simulating historical layers that do not create meaningful choices.

## 5. Crystal taxonomy and acquisition

Every crystal instance should have durable identity and provenance.

Candidate fields:

- crystal instance ID
- crystal family/definition ID
- source type: mine / beast
- source location or beast ID
- grade
- purity
- size
- resonance
- stability
- charge/capacity where applicable
- recharge behavior
- affinities/tags
- active trait
- passive trait
- incompatibilities
- harvesting damage
- instability state where applicable
- appraisal state: unknown / partial / known

### Mine crystals

Mine-crystal quality may depend on deposit depth, vein quality, extraction method, contamination, fractures, and miner skill. They favor repeatable trade, infrastructure, and standardized forge recipes.

### Beast heart crystals

Beast crystals sit near the heart/core region and can preserve species-specific traits.

Quality can depend on:

- beast species
- beast level/development
- crystal maturity
- beast evolution
- wounds near the heart/core
- whether the crystal was directly struck
- time between kill and extraction
- harvesting method
- hunter/crystalcraft skill

[DIRECTION] This creates a combat/loot tradeoff: attacking the heart/core may be the fastest lethal option but can damage or destroy the most valuable crystal.

A hunter seeking a pristine core may instead disable limbs, exhaust the beast, trap it, penetrate another vital region, or use a more difficult finishing method.

## 6. Forging and crystal integration

Equipment creation is a staged craft rather than one recipe check:

1. choose base material
2. forge/shape the physical item
3. temper/finish structure where relevant
4. create crystal housing/channel
5. appraise/select compatible crystal
6. fit, bind, or fuse crystal
7. stabilize resonance
8. final quality inspection

Final equipment performance derives from:

base design + material + smith skill + forge quality + crystal properties + integration quality + current condition

Crystal effects should not only increase damage. Examples include edge retention, impact discharge, heat/cold effects, enhanced guard, reduced apparent weight, armor penetration, short mobility bursts, sensing/resonance effects, resistance to a beast family, and technique-enabling effects.

[DESIGNED] Some crystal fittings can be replaceable sockets. Stronger fusions may be permanent or destructive to remove.

## 7. Spatial combat and body-zone targeting

[DIRECTION] The player cannot freely select every body part on every turn.

A body zone is targetable only when combat geometry and current battle state make it reachable.

Targetability derives from:

- relative facing: front / flank / rear
- range band: grapple / close / weapon reach / ranged
- elevation
- attacker stance
- defender stance/posture
- weapon reach and targeting tags
- defender body configuration
- cover
- terrain
- obstruction
- grapple/control state
- stagger/knockdown state
- armor/body damage already created
- current battle phase/environment state

A quadruped beast might have head, eyes, jaw, neck, shoulders, chest, forelegs, abdomen, hind legs, tail, back, and heart/core region.

A winged beast may add wing roots, membranes, and talons. A giant humanoid beast may make its head unreachable to a normal sword while standing but reachable after knockdown, climbing, elevation advantage, forced kneel, or terrain interaction.

[DIRECTION] The UI asks the rules layer for currently reachable target zones. It must not display every anatomical weak point as immediately selectable.

## 8. Body-zone consequences

Zones produce consequences beyond raw HP.

Examples:

- eye/sense damage -> reduced perception/accuracy
- jaw/throat damage -> reduced bite/voice/breath attack
- arm/foreleg damage -> weaker attacks/guard
- leg/joint damage -> reduced movement, charge, jump, or turning
- wing damage -> degraded/lost flight
- tail damage -> reduced balance or tail attacks
- armor break -> exposes underlying zone
- abdomen wounds -> stamina/bleeding pressure
- head trauma -> stagger/confusion/command disruption
- heart/core -> high lethality plus high crystal-damage risk

[DESIGNED] Wounds change future actions and positioning so combat evolves instead of repeating the same optimal attack.

## 9. Battle-state topology

Combat is a changing state graph rather than a static menu.

Candidate CombatState components:

- arena/encounter location
- local terrain node
- range band
- relative facing
- elevation difference
- attacker/defender posture
- control/grapple state
- cover
- hazards
- environmental objects
- currently exposed zones
- disabled/damaged zones
- battle phase
- escape routes

Examples of transitions:

- sidestep around a charge -> flank exposure
- spear brace -> changes charge outcome/range
- beast climbs wall -> removes ground-only targets
- collapse scaffolding -> forces knockdown/exposure
- enter narrow doorway -> prevents wide attacks
- mud/water -> alters footwork/charge
- pin a limb -> temporarily opens throat/side
- beast retreats into den -> new terrain, darkness, allies, traps
- player climbs rubble -> head becomes reachable

[DIRECTION] Some body zones remain completely unavailable until the battle setting changes.

## 10. Retreat, memory, and adaptation

[DIRECTION] Retreat is a persistent world event, not a combat reset.

A surviving beast may remember the player and encounter.

Encounter memory can record:

- player identity if known
- party members
- weapon families used
- crystal effects observed
- common opening actions
- frequent target zones
- common defensive reactions
- preferred range
- damage types received
- techniques witnessed
- traps/tools witnessed
- whether the player retreated
- wounds suffered
- allies killed
- terrain used
- encounter result
- confidence in each observation

### Adaptation rule

Beasts do not receive arbitrary omniscient counters.

Adaptation depends on intelligence, memory capacity, learning aptitude, observation count/confidence, species biology, existing traits, time, food/territory/crystals/allies, injury state, and evolution potential.

Possible adaptations:

Behavioral:
- guard a repeatedly attacked limb
- change opening attack
- avoid a known trap
- keep distance from a weapon class
- bait a familiar dodge/parry
- attack a support character
- retreat earlier when badly wounded

Tactical:
- choose terrain that restricts the player's weapon
- ambush rather than charge
- bring pack members
- block an escape route
- protect a damaged side
- move the fight toward den/territory advantage

Biological/evolutionary:
- stronger hide/plate in repeatedly damaged regions
- changed crystal resonance
- improved sensory organ
- altered limb/attack specialization

Biological adaptations require substantially more time/resources than tactical learning.

[DESIGNED] Low-intelligence beasts learn simple associations and habits. Highly intelligent beasts can form explicit plans. Memory can be incomplete or wrong, allowing the player to change style and exploit expectations.

## 11. Beast progression and persistent entities

A persistent beast can track:

- stable beast ID
- species
- age/development stage
- level
- experience/development progress
- attributes
- skills
- resources
- intelligence
- temperament/personality
- injuries/scars
- crystal/core state
- techniques
- adaptations
- encounter memories
- territory
- den/location
- social group
- rank/role
- followers
- rivals
- kills/victories
- current goals
- voice/language tier
- alive/dead/missing state

### Beast level

[DIRECTION] Beast level is a progression summary/gate, not the sole source of power.

Beasts can develop through meaningful battles, hunts, rival victories, territory defense/expansion, learning/training for intelligent species, appropriate resource consumption, maturation, and crystal evolution.

Routine repetition gives diminishing progression value. Injuries, starvation, age, lost territory, or damaged crystals can reduce current combat capability without reducing historical level.

## 12. Beast intelligence and capability

Intelligence influences planning and social complexity but does not replace every stat.

Candidate tiers:

- Tier 0 — instinctive: stimulus-response behavior, simple threat memory, vocalizations.
- Tier 1 — cunning animal: pattern recognition, basic ambush/avoidance, pack signals.
- Tier 2 — advanced hunter: multi-step tactics, target prioritization, coordinated hunting, limited symbolic communication.
- Tier 3 — near/sapient: planning, traps/tools where anatomy permits, simple language, negotiation in suitable species.
- Tier 4 — commander: long-term memory, counter-planning, organized followers, territory strategy, complex speech.
- Tier 5 — exceptional strategist: regional planning, deception, diplomacy, multi-group command, long-horizon adaptation.

[DESIGNED] Species/body plan still matters. Intelligence alone does not grant human-like tool use, speech anatomy, or social organization.

## 13. Beast hierarchy, chiefs, and commanders

Possible roles:

- solitary
- pack member
- veteran
- hunter/guardian
- alpha/chieftain
- war leader / commander
- territory ruler
- regional apex

Promotion depends on intelligence, level/development, victories, social capability, followers, territory, reputation/fear, survival, and resource access.

[DIRECTION] A high-level beast does not automatically become a commander. Leadership requires cognitive and social capability.

A commander can reorganize patrols, move nests, control hunting grounds, attack settlements/rivals, block roads, set ambushes, collect strong beasts, defend crystal/mining territory, and retaliate against repeated hunters.

## 14. Beast-versus-beast world simulation

Beasts can fight, displace, kill, injure, and learn from other beasts while the player is absent.

Off-screen encounters use coarse deterministic simulation rather than full turn-by-turn combat.

Inputs may include level, attributes/skills, injuries, group strength, intelligence/tactics, terrain, crystal traits, hunger/resources, morale, leadership, species matchup, and exhaustion.

Outcomes may change wounds, deaths, XP/development, territory ownership, pack membership, leadership, resources, migration, rivalries, and evolution opportunities.

[DESIGNED] World simulation should be region-scoped/event-driven so thousands of creatures do not require continuous full simulation.

## 15. Dynamic beast voice and dialogue

Runtime generative AI is not required.

Dialogue is produced from authored template families plus structured beast state.

Candidate speech tiers:

- Tier 0: roars, clicks, growls, body-language descriptions
- Tier 1: recognizable calls/signals and repeated short expressions
- Tier 2: simple words/commands if the species permits language
- Tier 3: situational sentences, threats, negotiation
- Tier 4: tactical commands, remembered references, deliberate taunts
- Tier 5: nuanced strategy, diplomacy, deception, titles, long-term references

High-intelligence beasts may reference prior player retreat, previously used weapons, repeatedly attacked limbs, slain pack members, old scars, territory violations, the player's known name/title, or a changed combat style.

The projection concept is:

voice template + intelligence tier + emotion + social role + memory tags + encounter state

[DIRECTION] Gameplay text remains deterministic/inspectable. Future audio generation can sit above this text contract without becoming authoritative game logic.

## 16. Recommended runtime entities

Future implementation should separate authored definitions from mutable runtime instances.

Candidate objects:

- WeaponDefinition
- EquipmentInstance
- CrystalDefinition
- CrystalInstance
- BeastSpeciesDefinition
- BeastRuntimeState
- BodyZoneDefinition
- BodyZoneRuntimeState
- CombatState
- EncounterMemory
- AdaptationState
- TerritoryState
- WorldRegionState

Persistent instances require stable IDs.

## 17. Important balancing and exploit controls

Crystal farming:
- pristine cores are not guaranteed
- direct core attacks can reduce crystal quality
- extraction requires time/skill/tools
- stronger beasts may produce stronger cores but create greater risk

Retreat farming:
- repeated enter/leave behavior cannot provide unlimited beast XP
- use meaningful-event thresholds, diminishing novelty, capped survival learning, and development costs

Adaptation fairness:
- adaptations require observed evidence
- low-confidence observations can create imperfect counters
- major biological evolution requires time/resources
- the player can change strategy

Equipment stacking:
- crystals need socket/integration limits
- resonance incompatibility can prevent infinite stacking
- weight, stability, durability, or maintenance create counter-costs

Target-zone dominance:
- use exposure rules, posture, protective behavior, armor, reach, weapon constraints, retaliation risk, and loot-damage tradeoffs

World runaway:
- constrain off-screen development with food/resources, carrying capacity, injuries, rivals, aging, migration, mortality, and soft regional ceilings

## 18. Integration with current architecture

The existing principle remains:

GameState -> authoritative rules/systems -> player-safe projection -> UI

Future combat flow:

GameState + CombatState + Equipment + BeastState -> CombatRules -> PlayerSafeCombatView -> UI

Future ecology flow:

WorldRegionState + PersistentBeasts + deterministic seed/time -> WorldSimulation -> durable state events

The UI must not independently calculate target availability, adaptation, forge outcomes, or crystal effects.

## 19. Stage-gate rule

[DECISION] Do not implement this expansion into V6 while the Stage 3 exact-runtime verification gate remains unresolved.

Current V6 promotion command:

PYTHONPATH=src python -m unittest discover -s tests -v

This medieval/crystal expansion is accepted design direction and backlog scope, but executable work should begin from a verified integration baseline or an explicitly isolated prototype branch that cannot be confused with the promotion candidate.

## 20. Initial implementation order

After the current runtime gate is green:

1. freeze canonical combat/equipment data contracts
2. resolve or isolate the seven-vs-eight stat question
3. add crystal/item registries and instance schemas
4. add coverage-based armor/equipment definitions
5. add body-zone definitions and reachability queries
6. add minimal CombatState position/range/posture model
7. implement deterministic target-zone availability
8. implement zone consequences/injuries
9. implement weapon physical properties and damage profiles
10. implement crystal integration/forging
11. add persistent beast runtime state
12. add encounter memory
13. add constrained adaptation
14. add beast XP/level progression
15. add territory/social roles
16. add coarse beast-vs-beast simulation
17. add authored dynamic bark/dialogue projection
18. create one end-to-end medieval hunt vertical slice
19. add save/load migrations and full regression coverage
20. only then expand content breadth and balance

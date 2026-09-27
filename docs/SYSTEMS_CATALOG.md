# Systems Catalog — Foundation v0.2

This document is the canonical high-level map for player statistics and the first non-combat simulation systems. It exists to keep future content authors, UI work, and balancing consistent.

## Core attributes

All core attributes use a 0–100 scale and are intentionally slow-moving.

- `might`: raw physical force.
- `agility`: movement, coordination, reaction.
- `endurance`: fatigue tolerance and physical resilience.
- `intellect`: reasoning and technical learning.
- `will`: discipline, mental resistance, pain tolerance.
- `perception`: environmental awareness, danger recognition, tells.
- `presence`: social force, confidence, leadership pressure.

A core attribute should not jump substantially from one dialogue choice or one short training action.

## Skills

Skills also use a 0–100 scale but advance faster than attributes.

Combat:
- unarmed
- blades
- ranged
- defense
- tactics

Physical:
- athletics
- stealth
- traversal
- survival

Technical:
- engineering
- technical_systems
- medicine
- crafting

Social:
- persuasion
- deception
- intimidation
- empathy
- leadership

Knowledge:
- investigation
- history
- factions
- powers
- creatures

## Derived values

Derived values are calculated from the character state rather than independently leveled.

Current baseline formulas:

- Max Health = 50 + Endurance × 2.0 + Will × 0.5
- Max Stamina = 40 + Endurance × 1.5 + Athletics × 0.5
- Max Focus = 30 + Intellect × 0.8 + Will × 0.7
- Max Resolve = 25 + Will × 1.1 + Presence × 0.35 + Leadership × 0.15
- Initiative = Agility × 0.7 + Perception × 0.3
- Accuracy = Perception × 0.55 + Agility × 0.20 + Ranged × 0.25
- Evasion = Agility × 0.65 + Perception × 0.20 + Athletics × 0.15
- Guard = Endurance × 0.45 + Might × 0.25 + Defense × 0.30
- Carry Capacity = 10 + Might × 0.8 + Endurance × 0.2

These formulas are provisional balancing values, not final canon numbers.

## Resources

The initial universal resources are:

- Health
- Stamina
- Focus
- Resolve

Power-specific resources may exist separately. A power does not have to use a universal mana pool.

## Training

Training is time-based and consumes resources.

Skill training:
- requires a real duration
- consumes stamina and focus
- supports intensity and mentor bonuses
- uses diminishing returns at high skill
- writes a durable training event to history

Core attribute training:
- requires longer focused sessions
- progresses far slower than skill training
- is deliberately resistant to “one click = huge stat gain”

## Conditions and injuries

Conditions are explicit state records with:

- stable condition ID
- severity 1–5
- optional remaining duration
- source
- tags
- numeric modifiers
- time applied

Timed conditions expire through world-time advancement. Permanent injuries or scars can use `duration_minutes = null` and require authored treatment/recovery events.

## Recovery

Recovery:
- advances world time
- restores resources by explicit per-hour rates
- can use a quality multiplier
- never exceeds calculated maxima

The current rates are provisional and will be tuned after a playable loop exists.

## Equipment

Equipment uses fixed slots:

- head
- body
- hands
- legs
- feet
- main_hand
- off_hand
- accessory_1
- accessory_2

An equipped item can carry:

- stable item ID
- slot
- quality
- stat/skill modifiers
- requirements
- tags
- equipment set ID
- active ability reference
- passive perk references
- provenance/source

Equipment requirements are checked before equipping.

## Equipment sets

Set bonuses are threshold-based. A two-piece effect and four-piece effect can coexist when both thresholds are reached.

Set bonuses are data, not hard-coded into item logic.

## Power runtime

Powers now have separate overall ability mastery and per-technique mastery.

A technique may define:
- minimum ability rank/mastery
- minimum technique stage
- attribute/skill/knowledge/perk/flag/item prerequisites
- universal or power-specific resource costs
- world-time cooldown
- mastery gained from use
- condition drawbacks such as strain, injury, or fatigue

Technique stages currently progress:
- discovered
- unstable
- learned
- practiced
- mastered

Ability evolution is authored rather than automatic. An evolution can require a combination of rank, mastery, learned facts, perks, attributes, skills, flags, items, and technique mastery. Successful evolution can change form/tags, consume required items, grant source-tracked perks, and establish a persistent rank floor.

## Ability-specific power resources

Power resources are authored per ability rather than forcing every power through a universal mana pool.

A power definition can specify:
- a numeric path under `player.power_resources`
- maximum value
- starting value
- recovery per hour
- technique-specific costs that can combine that resource with universal resources such as Focus

The first provisional example is `ABILITY_TRACE_ECHO`:
- resource: `power_resources.trace_resonance`
- start/max: 10
- baseline recovery: 2 per hour
- `TECHNIQUE_SIGNAL_PULSE`: costs 2 Trace Resonance + 3 Focus
- cooldown: 10 world minutes
- active-use drawback: `COND_ECHO_STRAIN` for 20 minutes, temporarily reducing Perception and Will
- first 30-minute quiet recovery restores only 1 Trace Resonance at baseline quality

Recovery advances the same simulation clock used by cooldowns and timed conditions. This means resource recovery and drawback expiry cannot drift onto separate clocks.

A stronger provisional technique, `TECHNIQUE_DIRECTIONAL_TRACE`, is defined but not granted. Its authored requirements include later ability rank/mastery, specific knowledge, a tolerance perk, improved Perception/Will, and Power skill. This preserves the rule that stronger techniques are earned rather than automatically unlocked by discovering the ability.

## Technique discovery gates

Technique discovery is now distinct from technique use.

A technique can define `discovery_requirements` using:
- ability rank and mastery XP
- required knowledge
- required perks
- attribute/skill minimums
- flags
- inventory items
- mastery stage of prerequisite techniques

Runtime discovery refuses to create the technique record until those requirements are satisfied. Choices can also use the `technique_discoverable` condition to present the opportunity as locked/available without duplicating the underlying rules.

The provisional `TECHNIQUE_DIRECTIONAL_TRACE` contract currently requires:
- Trace Echo rank 1
- 100 ability mastery XP
- `KNOW_TRACE_ECHO_PATTERN_STABLE`
- `PERK_TRACE_TOLERANCE`
- Perception 45
- Will 45
- Powers skill 10
- `TECHNIQUE_SIGNAL_PULSE` at least `learned`

These values remain provisional balancing data.

## Stable content registries

A content pack may define stable registries for:
- knowledge
- perks
- items
- conditions

When registries are present, authored scene gates/effects and power requirements/drawbacks are cross-checked against them before play. Initial inventory, player knowledge, perks, and conditions are also checked by the content loader.

Registries provide ID integrity and metadata ownership; they do not automatically grant the registered content.

## Trace Echo stabilization loop

The current provisional playable branch demonstrates how a stronger technique is earned through multiple systems rather than a single unlock button.

After the first Signal Pulse use, the player can begin `QUEST_TRACE_STABILIZATION`. The hub supports:
- repeated two-hour Signal Pulse practice sessions;
- two-hour Powers-skill training sessions;
- eight-hour universal-resource recovery;
- stable-pattern analysis once Signal Pulse reaches `learned`;
- a six-hour sensory tolerance protocol;
- Directional Trace discovery only when its complete discovery contract is satisfied.

`PERK_TRACE_TOLERANCE` is granted by the tolerance protocol, not by registration or debug state. It currently contributes +5 effective Perception and +5 effective Will. Power prerequisite checks use effective attribute/skill values, so this specialized training can qualify the character without rewriting base attributes.

The provisional Directional Trace discovery contract is:
- Trace Echo ability mastery >= 20
- Signal Pulse stage >= learned
- Powers skill >= 10
- `KNOW_TRACE_ECHO_PATTERN_STABLE`
- `PERK_TRACE_TOLERANCE`
- effective Perception >= 45
- effective Will >= 45

The training hub intentionally allows repetition and recovery until the contract is met. This is a mechanics prototype; pacing may later be broken into day/session milestones instead of exposing the loop as one continuous hub.

The first Directional Trace use is also authored:
- cost: 5 Focus + 4 Trace Resonance
- cooldown: 30 world minutes
- first-use mastery: +3 technique XP and +2 overall Trace Echo mastery
- drawback: severity-2 `COND_ECHO_STRAIN` for 35 minutes
- information result: `KNOW_DIRECTIONAL_TRACE_POINTS_DEEPER`
- one hour of quiet power recovery restores 2 Trace Resonance and clears the temporary strain through normal time advancement

Discovery does not imply mastery. Directional Trace begins at 0 mastery XP and remains `discovered` after its first +3 XP use.

## Ability discovery and practice

Ability discovery is separate from mastery.

A discovery event creates an ability shell at rank 0 and mastery 0. It may establish family, form, tags, and authored metadata, but it does not silently grant competence.

Technique discovery is also separate from technique mastery. Newly discovered techniques begin at the earliest stage.

Technique practice:
- requires an already discovered ability and technique
- requires at least 30 minutes
- consumes stamina and focus
- advances the world clock
- respects technique recovery/cooldown time
- supports bounded intensity and mentor bonuses
- uses diminishing returns as technique mastery rises
- grants technique mastery faster than overall ability mastery

The current baseline is deliberately slow: one ordinary hour from zero technique mastery grants 8 technique XP, which is not enough to leave the `discovered` stage. This value is provisional balancing data and exists to enforce the design rule that major progression is earned across repeated time, training, experimentation, and use.

## Quest graphs

Quests are authored graphs rather than a single integer stage.

Each quest can define:
- stable quest ID
- stable stage IDs
- objectives per stage
- required vs optional objectives
- objective prerequisites
- objective-specific branches
- stage-level completion routes
- objective/stage failure routes
- terminal completed/failed stages

Runtime quest state records current stage, completed/failed objectives, status, timestamps, and transition history.

Static validation checks graph references before play. Whole-content-pack validation also verifies that scene `quest_stage` effects reference real quest/stage IDs.

## NPC goals, story state, and relationships

Important NPCs can now maintain:
- independent relationship axes bounded to -100..100
- minimum and maximum relationship gates
- explicit goals with priority/progress/status
- guarded story-state tracks that only transition from authored prior states
- durable history entries for relationship, goal, and story transitions

This keeps NPC development inspectable and authored rather than deriving behavior from one generic friendship score.

## NPC memory and knowledge

Important NPCs have separate state for:

- personality
- private knowledge
- memories
- goals
- story state
- relationship axes

NPC knowledge is not automatically the same as player knowledge.

A secret can therefore be:

- known by the player only
- known by one NPC only
- known by several characters
- deliberately shared
- leaked later through an authored propagation event

## Secret propagation

The current system does not randomly invent gossip.

Instead, it can deterministically calculate eligible leak targets based on:
- who currently knows the information
- secrecy level
- the holder’s discipline/honesty profile
- an authored social network

Story content still decides whether a propagation event fires. Once it does, the runtime can execute the authored leak deterministically:
- candidate eligibility is recalculated from the current state
- explicit authored recipients must be eligible
- otherwise recipients are selected from the sorted eligible list
- the existing knowledge record is copied rather than invented or rewritten
- recipients receive a leak-tagged memory
- the event records candidates and actual recipients in durable history

## Design constraint

These systems exist to make narrative consequences mechanically real. They are not intended to turn the project into a spreadsheet simulator. UI should surface only the information relevant to the current decision and keep deeper sheets expandable.

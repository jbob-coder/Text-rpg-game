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

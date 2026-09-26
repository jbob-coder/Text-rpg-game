# Systems Catalog — Foundation v0.3

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

Capacity-style derived values currently have explicit non-negative floors: max Health, max Stamina, max Focus, max Resolve, and carry capacity cannot resolve below zero. Contest-style scores such as initiative, accuracy, evasion, and guard may go below zero under severe penalties; that preserves meaningful failure margins instead of silently erasing penalties.

## Effective-value pipeline

Checks and derived values use one additive modifier pipeline. A modifier is not written back into the permanent base attribute/skill.

Current modifier sources:
- equipped-item modifiers
- active equipment-set threshold bonuses
- perks
- active conditions/injuries

Canonical paths:
- attributes: `attributes.<id>` such as `attributes.might`
- skills: `skills.<id>` such as `skills.ranged`
- direct derived modifiers: `derived.<id>` such as `derived.max_health`

These paths are validated against centralized attribute, skill, and derived-stat registries. Unknown IDs, unsupported namespaces, and malformed nested paths are authoring errors rather than silently ignored modifiers.

A derived calculation first reads effective attributes/skills, then applies any direct `derived.*` modifier exactly once. This prevents the same equipment/perk/condition bonus from being baked into permanent state and then counted again.

The modifier layer can return a per-source breakdown (`base`, equipment slot, set threshold, perk ID, condition ID, total). This is intended for debugging and player-facing inspection.

Derived formulas are also centralized as data. `derived_stat_breakdown()` exposes the formula constant, each effective input and weight, the direct `derived.*` contributions, any domain-floor adjustment, and the final total. `RulesEngine.explain_player_value()` provides one entry point for explaining either a base/effective attribute or skill, or a fully calculated derived value.

Condition severity is metadata in the current contract. The authored numeric modifier is already the final magnitude; severity does not silently multiply it.

Equipment requirements deliberately use permanent/base attributes and skills rather than effective values. This avoids circular builds where one equipped item qualifies another item and makes equip order affect validity.

## Resources

The initial universal resources are:

- Health
- Stamina
- Focus
- Resolve

Power-specific resources may exist separately. A power does not have to use a universal mana pool.

Resource maxima come from derived values, so effective attributes/skills and direct derived modifiers can change maximum resources. Recovery and training accept the same set-definition context so set bonuses can be reflected consistently.

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

Condition modifiers participate in the same effective-value pipeline as equipment, sets, and perks.

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

Set bonuses are data, not hard-coded into item logic. Active set modifiers feed the unified effective-value pipeline when set definitions are supplied by the caller/rules context.

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

Story content still decides whether the leak event actually fires.

## Design constraint

These systems exist to make narrative consequences mechanically real. They are not intended to turn the project into a spreadsheet simulator. UI should surface only the information relevant to the current decision and keep deeper sheets expandable.

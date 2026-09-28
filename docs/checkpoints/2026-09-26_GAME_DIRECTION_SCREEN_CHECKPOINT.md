# Checkpoint — Game Direction + Screen Contract

Date: 2026-09-26

## CURRENT_OBJECTIVE

Preserve the requested game direction, stat architecture, and screen/interface behavior in repository-backed documentation so later chats can reconstruct the intended design without relying on chat memory.

## VERIFIED_STATE

Verified from the current repository foundation:
- seven slow-moving core attributes: might, agility, endurance, intellect, will, perception, presence
- skills grouped into combat, physical, technical, social, and knowledge categories
- universal resources: health, stamina, focus, resolve
- derived values currently include max health, max stamina, max focus, max resolve, initiative, accuracy, evasion, guard, carry capacity
- ability mastery is separate from character stats and uses mastery XP/stages/rank
- conditions, timed recovery, training, equipment slots, equipment modifiers, set bonuses, relationships, knowledge, NPC state, quests, abilities, perks, and deterministic choice checks exist in the current rules foundation

## DIRECTION_LOCKED

The design direction now explicitly records:
- text-first RPG / life-sim / decision RPG
- persistent consequences and authoritative gameplay state
- slow attribute growth and faster skill growth
- ability mastery distinct from character level
- meaningful information/knowledge as gameplay state
- same primary screen shell across narrative, life-sim/exploration, and combat
- compact top status strip
- left contextual action area
- central narrative area
- right contextual tabs/panels
- bottom event log
- command/input bar for text-assisted play
- deeper status view organized by identity, attributes, resources, derived values, skills, abilities, equipment, conditions, relationships, and knowledge
- progression should expand options/reliability/mastery, not only inflate numbers

## AUTHORITY_RULE

Repository files outrank chat memory when they conflict. Design documentation does not by itself prove implementation. Every system should be classified as DIRECTION, DESIGNED, IMPLEMENTED, or VERIFIED.

## ARTIFACTS

- `docs/GAME_DIRECTION_AND_SCREEN_CONTRACT.md`

## NEXT_ACTION

Continue the stat/system work by defining a single effective-value/modifier pipeline for base attributes/skills + equipment + set bonuses + perks + conditions, then add tests that prove modifiers are applied exactly once to checks and derived values.

## RISKS

- double-counting modifiers across equipment/set/perk/condition layers
- UI exposing internal values that are not actually authoritative
- confusing character level, ability rank, mastery stage, and skill/attribute progression
- documentation drift if later chats modify behavior without updating checkpoints

## UNKNOWNS

- final numerical balance for derived formulas
- final UI visual styling/theme details beyond the structural screen contract
- final combat action taxonomy and enemy-information reveal rules
- which optional context tabs should be available in the earliest playable slice

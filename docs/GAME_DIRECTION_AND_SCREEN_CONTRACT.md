# Game Direction and Screen Contract

Status: canonical design-direction document for the shared game-context layer.

Authority rule: repository files outrank chat memory when they conflict. This document records the current intended direction; implemented behavior must still be verified against code and tests.

## 1. Core game identity

The game is a text-first RPG / life-sim / decision RPG in which choices alter durable state. The player should not receive large, arbitrary gains from one short action. Growth should be earned through time, training, experience, equipment, knowledge, relationships, and ability mastery.

The intended experience is not a spreadsheet simulator. Systems may be deep internally, but the screen should show the information relevant to the current decision and allow deeper inspection when the player asks for it.

Consequences are persistent. Important decisions can affect character state, relationships, knowledge, injuries/conditions, equipment, abilities, quests, factions/world state, and future available choices.

## 2. Authoritative-state principle

There should be one authoritative gameplay state for a playthrough. UI is presentation and input: it renders state and sends player intent; it must not invent hidden game truth independently.

Durable state includes at minimum:
- player attributes and skills
- current/max resources
- abilities and mastery
- equipment and inventory
- perks
- conditions and injuries
- relationships
- player knowledge
- NPC knowledge/memory where relevant
- quests and flags
- time/world progression
- history of consequential events

## 3. Character progression model

### Core attributes

The current foundation uses seven slow-moving attributes on a 0–100 scale:
- Might — raw physical force
- Agility — movement, coordination, reaction
- Endurance — fatigue tolerance and physical resilience
- Intellect — reasoning and technical learning
- Will — discipline, mental resistance, pain tolerance
- Perception — environmental awareness, danger recognition, tells
- Presence — social force, confidence, leadership pressure

These are long-horizon character properties. They should not jump substantially because of one dialogue choice or one short training action.

### Skills

Skills advance faster than attributes and represent learned competence. Current categories include combat, physical, technical, social, and knowledge skills.

Combat: unarmed, blades, ranged, defense, tactics.

Physical: athletics, stealth, traversal, survival.

Technical: engineering, technical systems, medicine, crafting.

Social: persuasion, deception, intimidation, empathy, leadership.

Knowledge: investigation, history, factions, powers, creatures.

### Derived values

Derived values are calculated from character state and should not be independently leveled. Current foundation includes max health, max stamina, max focus, max resolve, initiative, accuracy, evasion, guard, and carry capacity.

Exact formulas are balancing data and remain provisional until validated through a playable loop.

### Resources

Universal resources currently include:
- Health
- Stamina
- Focus
- Resolve

Power-specific resources should remain separate when appropriate. The game should not force every ability into one generic mana bar.

### Ability progression

Character level and ability mastery are separate concepts. Abilities should grow through use, training, knowledge, prerequisites, and authored breakthroughs rather than instant unlock buttons.

Ability state should be able to track:
- rank
- mastery XP / mastery stage
- unlocked techniques
- energy/resource requirements when applicable
- control
- efficiency
- range
- power
- cooldown or recovery constraints
- knowledge/perk/story prerequisites
- evolution/breakthrough conditions when the design needs them

The current mastery direction is staged progression: discovered → unstable → learned → practiced → mastered. Exact thresholds are balancing values, not immutable canon.

## 4. Training, recovery, injury, and conditions

Training consumes real in-game time and resources. Skill training can use intensity, mentors, and diminishing returns. Core-attribute training is deliberately slower and requires longer focused sessions.

Conditions and injuries are explicit state, not flavor text. A condition should be able to carry:
- stable ID
- severity
- duration or permanence
- source
- tags
- numeric modifiers
- time applied
- treatment/recovery requirements where needed

Recovery advances world time and restores resources according to explicit rates and quality. Permanent injuries/scars require authored recovery or treatment rather than silently expiring.

## 5. Equipment and build identity

Equipment occupies explicit slots and can modify stats/skills, impose requirements, provide active abilities, provide passive perks, and participate in data-driven set bonuses.

The system must avoid double-counting equipment, set, perk, or condition modifiers. There should be one effective-value pipeline for checks and derived calculations.

## 6. Relationships, knowledge, secrets, and NPC state

NPCs are not simple relationship meters. Important NPCs may have personality, private knowledge, memories, goals, story state, and multiple relationship axes.

Player knowledge and NPC knowledge are separate. A secret may be known by the player, one NPC, several NPCs, deliberately shared, or later leaked through authored world events.

Information should matter mechanically: knowledge can unlock choices, techniques, safer plans, dialogue options, investigations, or different interpretations of events.

## 7. Decision and consequence contract

A meaningful choice should be capable of producing three layers:
1. immediate state change
2. character/world response
3. later possibility or consequence

Checks should be deterministic from authoritative state plus the game seed where randomness is used, so the same saved state can be reproduced and debugged.

Choices may be gated by attributes, skills, relationships, knowledge, party composition, abilities, perks, items, conditions, time, or authored world flags.

## 8. Screen architecture

The screen should remain readable, serious, text-first, and uncluttered even as systems become deep.

The preferred shell keeps the same primary window across normal narrative, exploration/life-sim management, and combat rather than constantly replacing the entire interface.

### Persistent screen regions

#### Top status strip

Show a compact overview of the player's current condition. It should be able to expose, without overwhelming the player:
- character name
- level / progression summary where applicable
- current condition
- Health
- Stamina
- Focus
- Resolve
- critical status effects or warnings
- current time/date when relevant
- location when relevant

The top strip is for immediate state, not the full character sheet.

#### Left action area

Primary available actions belong on the left side. This area changes with context but keeps the same role:
- dialogue/action choices
- travel/exploration actions
- training/study/work/rest actions
- interaction options
- combat actions

Locked choices may remain visible when useful, with a clear requirement/reason rather than silently disappearing unless secrecy itself is intentional.

#### Central narrative area

The central panel is the main experience. It presents:
- scene narration
- dialogue
- consequences
- discoveries
- combat descriptions
- environmental information
- authored system messages when they matter

The game should not dump raw internal state here unless it is relevant to the player's current situation.

#### Right context panel / tabs

The right side is for deeper context without leaving the main scene. Tabs can expose relevant subsets such as:
- Character / Status
- Skills
- Abilities / Mastery
- Equipment
- Inventory
- Relationships
- Knowledge / Intel
- Quests / Objectives
- Map / Location context when the project needs it

Only useful tabs need to be shown at a given stage. The design should scale without forcing all data onto the screen at once.

#### Bottom event log

A compact event/history log records recent mechanical events and important state changes so the player can reconstruct what just happened.

Examples: condition gained/expired, resource loss/recovery, training result, relationship change, item gained/lost, ability mastery change, quest/world update.

#### Command/input bar

A bottom command/input area may support direct player commands in ChatGPT-assisted or text-input play while still preserving authored legal actions and state validation.

## 9. Character/status screen

The deeper Status view should distinguish categories rather than mixing every number together.

Recommended sections:
- Identity: name, level, origin/background/path, current condition
- Attributes: Might, Agility, Endurance, Intellect, Will, Perception, Presence
- Resources: Health, Stamina, Focus, Resolve with current/max values
- Derived combat/utility values: initiative, accuracy, evasion, guard, carry capacity, and later validated derived values
- Skills: grouped by category
- Abilities: rank, mastery, techniques, resource/cooldown constraints
- Equipment: slot-based loadout and effective modifiers
- Conditions/Injuries: severity, duration, effects, source, treatment where known
- Relationships / reputation summary
- Knowledge / discoveries relevant to current goals

The status screen is an inspection tool. It should not become the only way to understand the character; immediate critical information must still appear in the main shell.

## 10. Combat-screen behavior

Combat should reuse the same shell rather than becoming a disconnected game mode.

The center continues to narrate the encounter. The left action area becomes combat choices. The top strip shows immediate combat resources/status. The right context panel can expose enemy information only to the extent the player has perceived or learned it.

Combat decisions should be able to depend on:
- attributes
- combat skills
- equipment
- conditions/injuries
- position/state
- knowledge of the enemy
- abilities and mastery
- stamina/focus/other resource cost
- party state

The screen should communicate why an action is unavailable or risky when the character would reasonably know that information.

## 11. Life-sim and world-management behavior

The same interface must also support non-combat play such as:
- eating
- sleeping/resting
- studying/training
- working
- traveling
- money/resource management
- schedules/time management
- social interaction
- investigation
- preparation before dangerous encounters

These systems should advance world time and allow consequences elsewhere rather than freezing the world until the player acts.

## 12. Progression philosophy

Progression should primarily expand options, reliability, mastery, access, and strategic possibilities—not only inflate numbers.

Examples:
- higher skill enables safer or more sophisticated choices
- knowledge reveals hidden approaches
- relationships create help, access, obligations, or conflict
- equipment changes tactical options
- mastery changes how an ability can be used
- injuries and conditions can temporarily narrow options
- time investment creates opportunity cost

## 13. Presentation rules

- Do not expose every internal calculation by default.
- Surface causes and consequences clearly enough that the player can make informed decisions.
- Use expandable detail for deeper numbers.
- Keep terminology stable across UI, docs, saves, and code.
- Use stable IDs internally while presenting readable names to the player.
- Avoid giant permanent HUDs full of low-value numbers.
- Important warnings should be visible without opening menus.
- The interface should preserve continuity: the player should always know where they are, what happened, what they can do next, and what immediate risks/resources matter.

## 14. Reference influence versus original game identity

External fiction or games may be studied for system patterns such as status presentation, progression pacing, ability mastery, equipment interaction, consequence design, or information gating. Those references are design research only.

Do not copy protected names, story, characters, prose, UI wording, or setting identity into the original game. Derived mechanics must be adapted to the project's own rules and terminology.

## 15. Implementation/verification boundary

This document contains intended direction and currently known foundation concepts. A feature is not considered implemented merely because it appears here.

For every system, future work should label it as one of:
- DIRECTION — requested design intent
- DESIGNED — sufficiently specified but not yet integrated
- IMPLEMENTED — code exists
- VERIFIED — behavior has been tested/observed against the current repository state

When chat memory and repository files conflict, repository files are authoritative. When two repository documents conflict, the newer explicit decision/checkpoint should supersede the older one and record that relationship.

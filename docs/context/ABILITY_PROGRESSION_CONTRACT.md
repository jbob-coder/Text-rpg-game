# Ability and Progression Contract

Status: [DESIGNED] system architecture. No claim that the full contract is implemented.

Purpose: define how powers/abilities grow without collapsing character progression into one level number or allowing instant, consequence-free unlocks.

## 1. Separation of progression lanes

The game should treat these as different systems:

- character-wide progression
- core attributes
- skills
- ability rank
- ability mastery
- techniques
- ability-specific resources
- evolution/breakthrough state

They may influence one another, but they are not aliases.

Example:

```text
High Willpower
!= high ability mastery
!= high ability rank
!= every technique unlocked
```

A character may have natural aptitude but poor control, or extensive practice with a weak/low-rank ability.

## 2. Ability identity

Every ability uses a stable ID.

Recommended underlying record:

```text
ability_id
family/category
rank
mastery_xp
mastery_stage
control
efficiency
power_state
resource_state
cooldowns
known_techniques
discovered_properties
known_drawbacks
evolution_state
history/provenance
```

Player-facing name and description are separate presentation fields.

Stable IDs must survive text/UI renaming.

## 3. Rank

Rank represents a broad capability tier.

Rank may control:
- maximum output
- available technique tiers
- range ceiling
- resource capacity ceiling
- evolution eligibility
- interaction with defenses/resistances

Rank should not automatically increase from one arbitrary use.

Possible rank progression inputs:
- accumulated mastery
- training
- mentor instruction
- story discovery
- prerequisite knowledge
- specific breakthrough event
- resource/body adaptation
- dangerous trial

[PROVISIONAL] Exact thresholds remain content/balance data.

## 4. Mastery

Mastery represents practiced familiarity and control.

Mastery should usually improve through:
- meaningful use
- focused training
- experimentation
- instruction
- successful technique execution
- surviving failure/drawback states when authored

Mastery should not simply equal total character XP.

Possible mastery stages:
- discovered
- unstable
- learned
- practiced
- mastered

Current foundation already has a mastery-stage concept; final naming/thresholds remain balanceable.

Mastery can improve:
- reliability
- control
- efficiency
- resource cost
- recovery time
- precision
- technique stability

It does not need to increase raw destructive power every time.

## 5. Control

Control is the ability to produce the intended effect.

Control may be influenced by:
- ability mastery
- Willpower
- relevant skill
- condition/injury penalties
- environmental interference
- technique difficulty

Control failure can result in:
- reduced effect
- resource waste
- wrong target/area
- backlash
- extended cooldown
- condition
- narrative exposure

[DIRECTION] Failure should remain deterministic/inspectable under the authored rules model, not generated arbitrarily.

## 6. Efficiency

Efficiency measures how much useful effect is achieved per resource/cost.

Higher efficiency can:
- reduce energy cost
- reduce Stamina/Focus strain
- reduce cooldown
- reduce backlash probability/severity where deterministic rules use such thresholds
- allow sustained use

Efficiency provides progression that is meaningful without constant number inflation.

## 7. Power / effect strength

Ability output can depend on:

```text
ability rank
+ technique definition
+ relevant effective attributes
+ mastery/control
+ temporary modifiers
+ context
```

Do not use one universal formula for every ability family.

A physical enhancement, sensory power, information power, movement power, healing power, or reality-altering effect may need different governing factors.

## 8. Ability resources

Not every ability must use universal mana.

Possible resource models:
- dedicated energy pool
- Stamina
- Focus
- Health sacrifice
- charges
- stored material
- cooldown-only
- environmental requirement
- hybrid cost

Ability resource record may include:
- current
- maximum
- regeneration/recovery
- reserve/locked amount
- overdraw state
- source

[DIRECTION] The resource model is part of ability identity.

## 9. Costs

Costs can be:
- immediate
- sustained per time unit
- deferred
- conditional
- escalating
- failure-only

Examples:
- 5 energy on activation
- 2 Focus per minute while maintained
- temporary Stamina reduction
- injury/backlash after overuse
- longer recovery after repeated use

Cost calculation should be explainable when shown to the player.

## 10. Cooldowns and recovery

Cooldown is not the same as resource depletion.

Possible states:
- ready
- active
- recovering
- locked
- suppressed

Cooldown/recovery may depend on:
- technique
- mastery
- efficiency
- conditions
- equipment/perks
- previous overuse

Cooldown state belongs in persistent game state if time passing can change it outside the current scene.

## 11. Techniques

Technique = a specific learned application of an ability.

Recommended technique states:

- undiscovered
- discovered
- learning
- usable
- practiced
- mastered
- sealed/temporarily unavailable

Technique record can define:
- technique ID
- parent ability
- rank requirement
- mastery requirement
- knowledge requirement
- perk/mentor requirement
- cost
- cooldown
- control difficulty
- range
- target rules
- outcomes
- drawbacks
- progression data

A technique should not automatically unlock because the player reached a generic character level unless that is deliberately authored.

## 12. Technique discovery

Discovery paths can include:
- experimentation
- observing another user
- mentor instruction
- written/researched information
- story event
- combination of mastered fundamentals
- environmental trigger

A technique may be known conceptually but not yet usable.

This supports:

```text
DISCOVERED -> UNDERSTOOD -> PRACTICED -> RELIABLE
```

rather than binary locked/unlocked progression.

## 13. Evolution / breakthrough

Evolution is a structural change, not a routine level-up.

Evolution may:
- alter resource model
- add a new branch/family
- change costs
- remove/add drawbacks
- unlock higher rank ceiling
- transform existing techniques
- change interactions with world systems

Evolution requirements can combine:
- rank
- mastery
- specific techniques
- permanent stats
- story state
- knowledge
- rare event
- condition/state
- item/material
- relationship/mentor
- previous decision

## 14. Hidden evolution requirements

Not every requirement should be shown.

Each requirement needs a disclosure state:

- hidden
- hinted
- partially discovered
- known
- satisfied

The UI must consume a player-visible evolution projection, never dump raw requirement data.

Example:

```text
Evolution Progress

Mastery                Satisfied
Control                72 / ???
Unknown Requirement    ???
```

Only if the player has actually discovered that such a requirement exists.

## 15. Drawbacks

Abilities should be allowed meaningful drawbacks.

Possible drawback classes:
- resource drain
- physical injury
- mental strain
- detection/exposure
- environmental limitation
- restricted target
- preparation time
- recovery lockout
- social/legal consequence
- permanent risk in exceptional abilities

Drawbacks should have stable rules/state and not exist only as prose if later systems need to react to them.

## 16. Overuse

Overuse should not be represented only by "not enough mana."

Possible overuse progression:

```text
Normal
-> Strained
-> Overloaded
-> Backlash
-> Injury / temporary lock
```

Thresholds may use:
- remaining resource %
- repeated uses in time window
- accumulated strain
- failed control
- current injuries

[DESIGNED] If implemented, strain should be explicit persistent state.

## 17. Ability checks

A technique may require a deterministic check.

Example architecture:

```text
effective governing attribute
+ ability mastery contribution
+ technique proficiency
+ situational modifiers
vs difficulty
```

Do not automatically use Willpower for every power.

Examples:
- control-heavy ability -> Willpower
- precision projection -> Dexterity
- sensory expansion -> Perception
- analytical manipulation -> Intellect
- physical transformation -> Constitution/Strength depending mechanic

This is one reason the core-stat responsibility boundaries matter.

## 18. Character-level relationship

[QUESTION] Overall character Level/EXP is still unresolved.

If retained, character level should provide broad pacing/gating, not directly replace all ability progression.

Acceptable uses:
- content difficulty band
- broad milestone rewards
- maximum points available
- story progression signal

Avoid:
- every ability instantly ranks up on character level
- all skills increase together
- evolution occurs automatically at a generic level threshold

## 19. Attribute relationship

Core attributes are slow-moving.

An ability may read effective core attributes during use, but the ability must not permanently overwrite them unless an explicitly authored progression/evolution effect does so.

Temporary ability buffs should pass through the modifier system.

Permanent transformations that truly change the body/character require explicit persistent progression events.

## 20. Skill relationship

Abilities can use normal skills when appropriate.

Examples:
- ranged skill for aimed projection
- medicine for healing application
- stealth for concealed activation
- engineering for technology-linked ability use
- investigation/powers knowledge for analysis

Ability mastery remains distinct from these skills.

## 21. Equipment/perk/condition interaction

The effective-value pipeline should be reusable by abilities.

Possible paths later:

```text
abilities.<ability_id>.control
abilities.<ability_id>.efficiency
abilities.<ability_id>.resource_max
techniques.<technique_id>.cost
```

[QUESTION] Do not add these modifier namespaces until the exact path contract is designed. Current canonical modifier namespaces remain attributes, skills, and derived values.

Equipment/perk/condition effects may instead modify governing attributes/derived values until ability-specific modifier paths are formally introduced.

## 22. Progression anti-exploit rules

Required constraints:

- no mastery from zero-cost spam unless the action is meaningfully eligible
- no XP from repeatedly targeting invalid/non-threatening dummy states unless training is explicitly modeled
- no negative-cost exploit
- no cooldown bypass through save/load
- no duplicated rewards from replaying the same one-time event
- no permanent attribute gain from ordinary temporary modifiers
- no technique unlock from hidden requirements the player never actually satisfied

Deterministic event IDs/history can help enforce one-time progression.

## 23. Training

Ability training should consume meaningful game resources:

- time
- Stamina/Focus/ability resource
- mentor access
- equipment/materials where applicable
- opportunity cost

Training outcome may depend on:
- current mastery
- mentor quality
- training method
- conditions
- repeated diminishing returns

This supports the global slow-progression direction.

## 24. Failure and learning

Failure can still progress mastery, but not necessarily at the same rate as success.

Possible authored model:
- successful meaningful use -> full mastery XP
- controlled near-failure -> partial XP
- immediate invalid attempt -> no XP
- catastrophic failure -> little XP plus consequence

This prevents optimization around intentional failure spam.

## 25. Save-state requirements

If implemented fully, save state must preserve enough information to reconstruct:

- rank
- mastery XP/stage
- known techniques
- technique mastery
- current ability resource
- strain/overuse
- cooldown/recovery timestamps
- discovered ability properties
- known drawbacks
- discovered/hinted evolution requirements
- satisfied irreversible prerequisites
- one-time progression event history

Do not persist only a displayed power score.

## 26. Status-screen projection

Primary ability card:

```text
ABILITY NAME
Rank        <visible rank>
Mastery     <stage / visible progress>
Resource    current / max
State       Ready / Recovering / Strained
Techniques  X known
```

Expandable detail:
- control
- efficiency
- cost
- cooldown
- known drawbacks
- techniques
- discovered evolution information

Hidden data is filtered before it reaches the UI.

## 27. Debug projection

Developer-only ability inspection may show:
- stable IDs
- raw mastery XP
- exact thresholds
- hidden requirements
- cooldown timestamps
- resource formulas
- internal flags
- progression history
- modifier sources

Never reuse developer projection for normal player UI.

## 28. Implementation order

Recommended safe order:

1. define ability record schema
2. define ability-specific resource/cost model
3. define cooldown state
4. formalize mastery gain rules
5. formalize technique state machine
6. add player-visible projection
7. add evolution requirement engine
8. add strain/overuse if required by the first playable ability
9. add ability-specific modifier namespaces only when concrete needs justify them
10. build one complete ability vertical slice before generalizing further

## 29. Acceptance criteria

The ability architecture is not complete until:

1. rank/mastery/techniques/evolution are mechanically distinct
2. resources/costs persist correctly
3. cooldown/time progression is deterministic
4. hidden ability data cannot leak through UI
5. progression cannot be spammed trivially
6. drawbacks can create durable consequences
7. state is save-compatible
8. relevant effective stat modifiers apply exactly once
9. player-visible explanations come from the rules layer
10. at least one ability can progress end-to-end through use/training/technique/evolution without bespoke exceptions

Related:
- `GAME_DIRECTION_AND_UI.md`
- `STATUS_SCREEN_DATA_CONTRACT.md`
- `STAT_SCHEMA_EVALUATION.md`
- `DEC-DIR-001`
- `DEC-STATE-001`

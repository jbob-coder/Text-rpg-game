# Core Stat Schema Migration Plan

Status: [DESIGNED] migration architecture only. No executable stat-schema migration has been authorized or applied.

Related decision: `DEC-STAT-001`

Current executable foundation schema:
- might
- agility
- endurance
- intellect
- will
- perception
- presence

Current long-term candidate:
- strength
- constitution
- agility
- dexterity
- perception
- intellect
- willpower
- presence

## 1. Purpose

If the eight-stat candidate becomes canonical, the migration must be treated as a save/content/API migration, not a simple rename.

The change affects:
- persistent player attributes
- authored requirements
- modifier paths
- derived formulas
- validation registries
- equipment requirements/modifiers
- perks
- conditions
- power requirements
- scenes/checks
- tests
- status UI metadata
- existing save files

No code should silently interpret an old stat ID as a new one without a versioned migration rule.

## 2. Stable semantic mapping

The low-ambiguity mappings are:

- `might -> strength`
- `endurance -> constitution`
- `agility -> agility`
- `intellect -> intellect`
- `perception -> perception`
- `presence -> presence`
- `will -> willpower`

The unresolved migration is:

- **new `dexterity`**

Old Agility currently carries some responsibilities that the candidate schema would split between Agility and Dexterity.

Therefore an existing `agility` value cannot be copied into both stats without an explicit design decision.

## 3. Dexterity bootstrap options

### Option A — copy old Agility into both

```text
new_agility = old_agility
new_dexterity = old_agility
```

Advantages:
- preserves existing character competence
- simple migration
- old saves do not suddenly become bad at precision tasks

Disadvantages:
- duplicates progression value
- effectively grants a free new high stat
- may inflate derived values if both stats contribute

Status: [PROVISIONAL] easy but balance-distorting.

### Option B — split old Agility

Example concept:

```text
new_agility = round(old_agility * body_movement_share)
new_dexterity = round(old_agility * precision_share)
```

Advantages:
- avoids duplicating total attribute investment

Disadvantages:
- existing characters become weaker in both categories
- requires choosing a mathematically arbitrary split
- old Agility was not necessarily earned under that semantic model

Status: [PROVISIONAL] mechanically tidy but semantically risky.

### Option C — preserve Agility and initialize Dexterity from a neutral baseline

```text
new_agility = old_agility
new_dexterity = baseline
```

Advantages:
- does not rewrite what old Agility meant
- avoids duplicating earned value
- easy to explain as a newly modeled capability

Disadvantages:
- existing high-skill characters may temporarily underperform in precision systems

Mitigation:
- relevant skills can preserve specialist competence
- migration can grant a one-time character-specific Dexterity adjustment if strong historical evidence exists

Status: [CURRENT MIGRATION CANDIDATE].

### Option D — infer Dexterity from existing specialization

Example inputs:
- ranged
- blades
- crafting
- medicine
- technical_systems
- stealth where fine manipulation is relevant

Advantages:
- preserves character identity better than a flat baseline

Disadvantages:
- complex
- risks double-counting skill investment as attribute investment
- migration becomes content/profile dependent

Status: [PROVISIONAL] useful only as a bounded adjustment, not a direct conversion formula.

## 4. Recommended migration shape if eight stats are accepted

[PROVISIONAL RECOMMENDATION]

Use a hybrid of C + bounded D:

1. rename low-ambiguity attributes directly
2. preserve old Agility as new Agility
3. create Dexterity from the normal new-character baseline
4. optionally grant a small bounded migration adjustment based on established precision-specialist history/skills
5. never copy full skill values into Dexterity
6. record the migration event in save metadata/history

This avoids both arbitrary stat splitting and full duplicate-value inflation.

Exact baseline/adjustment numbers remain unset until the eight-stat schema itself is accepted.

## 5. Save schema versioning

Migration requires a new save schema version.

Concept:

```text
schema_version N
  seven-stat save

load
  -> detect N
  -> validate old schema
  -> migrate attributes/modifier paths/content-owned persistent records
  -> validate new schema
  -> write/return N+1 state
```

Never mutate an old save in place before the migrated state validates.

Recommended migration procedure:

1. deserialize old save
2. deep-copy source state
3. run deterministic migration on the copy
4. validate all new attribute IDs and numeric ranges
5. validate modifier paths
6. validate ability/perk/condition records
7. validate resources/derived state
8. set new schema version
9. record migration metadata
10. only then return/save the migrated state

## 6. Persistent paths requiring rewrite

Potential old -> new path mapping:

```text
attributes.might       -> attributes.strength
attributes.endurance   -> attributes.constitution
attributes.will        -> attributes.willpower
attributes.agility     -> attributes.agility
attributes.intellect   -> attributes.intellect
attributes.perception  -> attributes.perception
attributes.presence    -> attributes.presence
```

New:
```text
attributes.dexterity
```

The same mapping must be applied wherever canonical modifier paths are stored persistently:
- equipped-item records if saves retain modifier maps
- perks
- active conditions
- persistent ability/evolution-granted modifiers
- any other state-owned authored modifier record

Authored source content should be migrated separately in repository data rather than at save-load time.

## 7. Derived formula migration

Seven-stat formulas must not be mechanically string-renamed only.

Each derived value needs semantic review.

Candidate eight-stat ownership:

- max_health -> Constitution + secondary Willpower if retained
- max_stamina -> Constitution + Athletics
- max_focus -> Intellect + Willpower
- max_resolve -> Willpower + Presence/Leadership
- initiative -> Agility + Perception
- accuracy -> Dexterity + Perception + Ranged
- evasion -> Agility + Perception + Athletics
- guard -> Constitution + Strength + Defense
- carry_capacity -> Strength + Constitution

Exact coefficients are balance data and remain [PROVISIONAL].

## 8. Requirement migration

Every authored requirement must be reviewed by intent.

Examples:

Old:
```text
attributes.agility >= X
```

May become:
- Agility if the requirement concerns movement/evasion/balance
- Dexterity if it concerns precision/manipulation/aim

Therefore global search-and-replace of `attributes.agility` is prohibited.

This applies to:
- scenes
- power technique discovery/use requirements
- evolution requirements
- equipment requirements
- checks
- perks/conditions
- authored training gates

## 9. Skill preservation

Skills should normally migrate unchanged.

The new Dexterity attribute must not replace:
- ranged
- blades
- medicine
- engineering
- crafting
- stealth
- technical_systems

A specialist remains specialized because skill is a separate progression layer.

## 10. Ability compatibility

Ability records should not require a schema rewrite unless they persist canonical attribute paths.

Ability requirements in authored definitions must be reviewed semantically.

Examples:
- precise projection -> Dexterity candidate
- sustained control -> Willpower candidate
- sensory expansion -> Perception
- physical transformation tolerance -> Constitution
- force amplification -> Strength

No universal "powers use Willpower" rule should be introduced during migration.

## 11. UI compatibility

The status contract is registry-driven.

Therefore UI should receive:
- attribute ID
- display name
- grouping/order metadata
- base/effective value
- role/help text

It must not hard-code seven rows.

Candidate eight-stat grouping:

Physical:
- Strength
- Constitution
- Agility
- Dexterity

Mental / Awareness:
- Perception
- Intellect
- Willpower

Social:
- Presence

## 12. Migration tests required

Before acceptance:

1. old seven-stat save loads into deterministic eight-stat state
2. original save input is not mutated on failed migration
3. all old canonical attribute paths are either migrated or explicitly rejected
4. no obsolete `might/endurance/will` paths remain in migrated persistent modifiers
5. Agility requirements are manually classified, not globally renamed to Dexterity
6. Dexterity bootstrap is deterministic
7. skills remain unchanged unless a separate migration says otherwise
8. resources remain within valid maxima
9. derived values use the new formula registry exactly once
10. ability/equipment/perk/condition requirements still validate
11. save round-trip after migration is stable
12. old schema cannot masquerade as new schema
13. status projection renders all eight attributes without client formula changes

## 13. Content migration audit

A migration report should enumerate every changed authored reference:

```text
file
stable content ID
old path
new path
reason
review status
```

Agility -> Dexterity changes require an explicit reason.

## 14. Rollback

Until the migration is promoted:
- keep seven-stat branch/history intact
- do not delete old schema migration code
- do not rewrite user saves irreversibly
- retain a fixture for the final seven-stat save version

If the eight-stat model fails playtesting, rollback should be a branch/schema decision rather than an attempt to reverse already-overwritten saves.

## 15. Acceptance gate

Do not execute the migration until all are true:

1. DEC-STAT-001 explicitly resolves to eight stats
2. final canonical names/IDs are accepted
3. Dexterity bootstrap policy is accepted
4. every derived formula has an eight-stat definition
5. authored Agility references have been semantically classified
6. migration function and fixtures exist
7. full suite passes before migration
8. migration tests pass
9. full suite passes after migration
10. status projection and playable slice are manually reviewed

Until then the seven-stat executable schema remains authoritative.

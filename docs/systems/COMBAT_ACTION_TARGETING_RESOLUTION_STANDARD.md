# THE GAME — Combat Action, Targeting & Resolution Standard

Status: **APPROVED FIRST-PASS CONTRACT / PHASE 1 RESOLUTION DEFAULTS**
Parents:
- docs/systems/TACTICAL_COMBAT_MASTER_PLAN.md
- docs/systems/TURN_INITIATIVE_ACTION_BUDGET_STANDARD.md
- docs/systems/LOS_DETECTION_AND_COMBAT_KNOWLEDGE_STANDARD.md
- docs/systems/DIRECTIONAL_COVER_TERRAIN_STANDARD.md
Current-stat integration:
- src/textrpg/schema.py
- src/textrpg/core.py

## 1. Purpose

Define one deterministic authoritative pipeline for validating and resolving attacks, abilities, items, interactions, and other tactical actions.

## 2. Actor combat-stat interface

Player and NPC actors must expose:
- initiative;
- accuracy;
- evasion;
- guard;
- current health;
- max health;
- action budget;
- movement allowance.

The current player schema already defines initiative, accuracy, evasion, and guard. NPCs need equivalent resolved values without pretending to be player records.

## 3. Action definition

Minimum fields:
- action_id;
- label;
- kind;
- budget_cost;
- target_kind;
- range_min/max;
- range_metric;
- requires_los;
- required_awareness;
- resource_costs;
- cooldown policy;
- offense source;
- defense source;
- base_power;
- damage_type;
- penetration;
- status effects;
- movement/interaction payload;
- tags.

UI receives only a safe legal-action projection.

## 4. Target kinds

Phase 1:
- SELF;
- ACTOR;
- CELL;
- INTERACTABLE;
- NONE.

Actions may further restrict ally/enemy/neutral/living/incapacitated/identified/detected targets.

## 5. Legality pipeline

Before cost payment:
1. encounter active;
2. actor exists and has action authority;
3. actor not incapacitated;
4. action exists;
5. enough budget;
6. resource/cooldown requirements;
7. target kind/existence;
8. faction/condition requirements;
9. range;
10. path requirement;
11. LOS;
12. awareness/knowledge;
13. occupancy/interactable state;
14. special authored requirements.

Failure means no cost and no mutation.

## 6. Deterministic event roll

Recommended digest:
seed | encounter_id | round_index | activation_index | event_index | actor_id | action_id | target_key

Use SHA-256, consistent with the current engine's deterministic check philosophy.

Phase 1 attack variance:
-10.0 to +10.0.

No wall-clock/platform RNG may decide authoritative results.

## 7. Attack contest

offense = resolved action offense + situational modifiers.

defense = target evasion + directional cover + situational modifiers.

margin = offense - defense + deterministic variance.

Initial degrees:
- critical_hit: margin >= 20;
- hit: margin >= 0;
- graze: margin >= -10;
- miss: margin < -10.

## 8. Phase 1 ranged baseline

- offense = derived.accuracy;
- defense = derived.evasion;
- cover = +0/+10/+20;
- variance = +/-10.

Other action families may define other score sources later.

## 9. Damage

Degree multiplier:
- critical_hit 1.5;
- hit 1.0;
- graze 0.5;
- miss 0.

raw_damage = base_power * multiplier.

protection = max(0, guard * 0.10 + armor_flat - penetration)

final_damage = max(0, raw_damage - protection)

Round authoritative final values to three decimals after complete calculation.

These are prototype tuning formulas.

## 10. Health and incapacitation

Health clamps at minimum zero.

Zero health => INCAPACITATED by default, not automatic death.

Death/capture/surrender/stabilization belong to encounter/aftermath rules.

## 11. Resource payment and rollback

Costs pay only after full legality validation.

Any exception after payment restores authoritative snapshot and appends no committed event.

Consumable inventory follows the same transaction.

## 12. Area actions

Area anchor validates first. Affected targets resolve in stable actor_id order unless definition specifies another deterministic order.

Preview cannot leak hidden occupants.

## 13. Conditions

Combat should reuse the existing condition system when compatible. It must not create a second incompatible status store for convenience.

## 14. Preview

Safe preview may include legality, costs, range, cover class, known target state, and later an approved hit/damage estimate.

Commit always revalidates.

## 15. Combat events

Committed events should include event index, round, actor, action, target, costs, degree/result, damage/effects, resulting state, and reaction IDs.

Audit event and player-facing log may be separate projections.

## 16. Tests

Required:
- legality order;
- no cost on illegal action;
- deterministic hash;
- degree thresholds;
- cover integration;
- damage/protection;
- health clamp;
- rollback;
- area ordering;
- hidden preview redaction;
- condition integration;
- same seed/state/action => same result.

## 17. Later tuning

Base powers, armor, penetration, exact UX probability, melee/power formulas, resistance types, and combat healing remain tunable. The structural pipeline is locked.

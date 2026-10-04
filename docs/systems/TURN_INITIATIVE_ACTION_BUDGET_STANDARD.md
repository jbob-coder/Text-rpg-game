# THE GAME — Turn, Initiative & Action-Budget Standard

Status: **APPROVED FIRST-PASS CONTRACT / PHASE 1 DEFAULTS LOCKED FOR PROTOTYPE**
Parents:
- docs/systems/TACTICAL_COMBAT_MASTER_PLAN.md
- docs/systems/CAMERA_AND_TACTICAL_PRESENTATION_STANDARD.md
- docs/systems/TACTICAL_COORDINATE_OCCUPANCY_STANDARD.md

## 1. Purpose

Define tactical rounds, activations, initiative, action budget, reactions, and reinforcement timing so the simulation is deterministic and readable on phone.

The numbers below are Phase 1 tuning defaults, not save-data identity.

## 2. Round model

A round:
1. snapshots eligible actors;
2. computes initiative order;
3. gives each eligible actor at most one normal activation;
4. allows valid reactions;
5. resolves end-of-round effects;
6. advances if the encounter remains active.

round_index starts at 1.

An actor incapacitated before its activation is skipped. New reinforcements normally join next round.

## 3. Initiative

The current schema already defines derived.initiative from Agility and Perception. Phase 1 uses that resolved value when available.

Ordering:
- higher initiative first;
- snapshot at round start;
- mid-round modifiers affect next round;
- ties resolve by stable actor_id ascending.

First-round surprise/preparation modifiers must be explicit encounter data.

## 4. Action budget

Phase 1 default:
- 4 budget units per activation.

Baseline costs:
- Move: 1;
- Basic Attack: 2;
- Interact: 1;
- Brace/Defend: 1;
- Sprint: 2;
- Assist: 1;
- End Activation: 0;
- Prepare Reaction: normally reserves 1;
- Ability/Technique: authored 1..4;
- Item: authored 1..4.

The action definition owns the exact cost. UI never hardcodes it.

## 5. Move and budget separation

Move spends action budget and grants movement points. Traversal consumes movement points rather than additional action-budget units.

This separates activation strategy from terrain cost.

## 6. Activation state machine

States:
- pending;
- active;
- resolving_action;
- waiting_reaction;
- complete;
- skipped.

Only the active actor may initiate a normal action.

Action transaction:
1. validate;
2. snapshot;
3. pay/reserve costs;
4. resolve;
5. trigger reactions/effects;
6. commit;
7. append event.

Failure rolls back the action transaction.

## 7. Ending activation

Activation ends when:
- player/AI chooses End Activation;
- budget reaches zero and no zero-cost legal action remains;
- actor becomes incapacitated;
- encounter ends;
- a rule explicitly ends activation.

Unused budget expires except budget explicitly reserved for a reaction.

## 8. Reactions

A reaction is not a free extra turn.

Phase 1:
- actor reserves budget through Prepare Reaction or has an explicit zero-reserve trait;
- trigger is authored;
- legality is rechecked when triggered;
- reserve is consumed when reaction fires;
- unused reserve expires at the actor's next activation start.

Reaction queue:
1. trigger priority;
2. higher round initiative;
3. actor_id ascending;
4. reaction_id ascending.

## 9. Delay and reinsertion

Phase 1 does not require free-form delay/reinsert. Prepared reactions cover the initial need without timeline complexity.

## 10. Reinforcements

Arrival modes:
- next_round: default;
- immediate_after_current: authored exception;
- scripted_boundary: encounter-specific.

No insertion retroactively reorders completed activations.

## 11. Companion control

Jack receives direct commands.

Recurring companions use constrained orders that modify AI utility rather than bypassing the same turn/action rules.

## 12. Determinism

No unordered container iteration may decide activation order, reaction order, reinforcement order, or AI ties. Stable IDs are final tie-breakers.

## 13. Player-safe projection

Android may receive round number, visible initiative order, active actor, remaining budget, visible reaction reserve, legal actions, and end-activation availability.

Undetected enemies must not leak through the initiative list.

## 14. Tests

Required:
- initiative descending;
- stable tie-break;
- round snapshot;
- mid-round initiative change deferred;
- 4-unit reset;
- no overspending;
- rollback on failed action;
- reaction reserve/consume/expire;
- deterministic reaction ordering;
- incapacitated skip;
- reinforcement default;
- hidden actor redaction.

## 15. Phase 1 locked defaults

- one activation per eligible actor per round;
- round-start initiative snapshot;
- derived.initiative;
- actor_id tie-break;
- 4 action-budget units;
- no free-form delay;
- reserved-budget reactions;
- reinforcements default to next round.

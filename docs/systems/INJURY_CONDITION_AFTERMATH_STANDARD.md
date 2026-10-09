# THE GAME — Injury, Condition & Combat Aftermath Standard

Status: **APPROVED FIRST-PASS CONTRACT / PERSISTENCE-CRITICAL**
Parents:
- docs/systems/TACTICAL_COMBAT_MASTER_PLAN.md
- docs/systems/COMBAT_ACTION_TARGETING_RESOLUTION_STANDARD.md
- docs/systems/SAVE_AND_CONTENT_MIGRATION_MASTER_PLAN.md
Current compatible runtime:
- src/textrpg/simulation.py
- src/textrpg/core.py
- src/textrpg/social.py

## 1. Purpose

Define how tactical damage becomes durable injury/condition state and how encounter consequences commit back into the RPG world.

Combat is not a detached minigame.

## 2. Reusable condition foundation

Current player conditions already support stable ID, severity 1..5, optional world-minute duration, source, tags, modifiers, and applied_at.

The first tactical implementation should reuse this contract where compatible.

NPC injury persistence needs a compatible NPC-side contract before implementation.

## 3. Phase 1 body zones

Baseline:
- head;
- torso;
- arms;
- legs.

No body-part targeting is required for every normal attack.

When not explicitly targeted, generic deterministic weights may be:
- torso 45;
- legs 25;
- arms 20;
- head 10.

Special creatures can override later.

## 4. Injury trigger

Check injury when:
- action explicitly causes one;
- result is critical_hit;
- post-mitigation damage >= 25% max health;
- target reaches 0 health.

Initial severity floor:
- >= 25% => 1;
- >= 40% => 2;
- >= 60% => 3;
- >= 80% => 4;
- catastrophic/authored lethal trauma => 5.

Critical hit may raise severity by one if allowed, capped at 5.

## 5. Injury definition

Fields:
- condition_id;
- zone;
- severity band;
- label;
- player_visible;
- modifiers;
- recovery class;
- treatment tags;
- can_worsen;
- persistence policy.

Typical intent:
- leg -> movement/traversal;
- arm -> weapon/interaction;
- head -> perception/focus;
- torso -> endurance/stamina.

Exact conditions/modifiers need an authored catalog.

## 6. Incapacitation versus death

Health 0 means incapacitated by default.

Death requires explicit lethal outcome, catastrophic injury rule, authored execution/story result, or later system decision.

NPC death/capture/escape must be deliberate durable state.

## 7. Recovery

Recovery may require time, rest, medicine, facility, item, NPC help, or ability.

Current recover/time primitives do not by themselves define injury healing.

Phase 1 must author one actual injury with a defined recovery/removal path.

## 8. Atomic aftermath transaction

Build aftermath plan before durable mutation.

Possible writes:
- player resources;
- conditions/injuries;
- inventory/loot;
- equipment state;
- NPC injury/death/capture/escape;
- memories;
- relationships;
- knowledge;
- quest state;
- flags/world state;
- adversary state;
- time_minutes;
- history.

Process:
1. validate planned writes;
2. deep snapshot;
3. apply;
4. validate resulting state;
5. append one aftermath history record;
6. commit;
7. rollback all on failure.

Partial aftermath is forbidden.

## 9. World time

Phase 1 encounter records include time_cost_minutes.

Prototype default if omitted: 5 minutes.

Tactical rounds do not directly equal world minutes.

## 10. Loot

Loot must come from authored item/world/encounter provenance. Combat cannot invent items from visuals.

## 11. NPC memory/social consequences

Aftermath may use current social primitives for memory, relationships, and knowledge.

Only deliberate durable facts are stored; private AI internals are not copied wholesale.

## 12. Rival hooks

A surviving recurring adversary may persist encounter result, injury, escape/capture, observed player tactics, and relationship/emotional consequences once V09 contracts exist.

## 13. Save policy

Phase 1:
- no required mid-combat save;
- durable saves before combat and after aftermath;
- interruption may restart from pre-combat checkpoint.

Future mid-combat save requires schema/version, migration, event/RNG state, occupancy, initiative, and reaction persistence.

## 14. Player-safe aftermath

Android receives visible outcome, injuries, known loot, visible quest/world changes, and only player-facing relationship/reputation summaries.

## 15. Tests

Required:
- injury thresholds;
- severity cap;
- deterministic zone;
- zero health not auto-death;
- condition validator integration;
- aftermath rollback;
- world time;
- loot provenance;
- NPC memory hook;
- hidden consequence redaction;
- save-before/after policy.

## 16. Phase 1 acceptance — current checkpoint

The specific Gate Twelve proposal now exists in `docs/systems/GATE_TWELVE_PHASE1_TACTICAL_ENCOUNTER_PACKET.md`:
- proposed ID `COND_TUNNEL_LEG_INJURY`;
- qualifying severity-1/severity-2 leg-injury fixture trigger;
- proposed Agility/Athletics modifiers;
- proposed `FIELD_TREATMENT`-style recovery taking 120 world minutes;
- atomic condition removal after valid recovery;
- aftermath/save-load test expectations.

This moves requirement #10 from “missing specific injury design” to **SPECIFIC INJURY/RECOVERY PROPOSAL EXISTS**. It does **not** make the injury current runtime/canon content.

Current implementation boundary:
- D-072 is the separately owned durable-aftermath transaction task and remains the live prerequisite at this checkpoint;
- OR-034 permits `COND_TUNNEL_LEG_INJURY` to be used as explicitly `PROVISIONAL_INTEGRATION` material in D-073 only after D-072 is genuinely DONE;
- provisional use does not canonize wording, numeric balance, item requirements or long-term recovery design;
- Phase 1 requirement #10 is not implementation-verified until the accepted integration proves trigger -> durable condition -> save/load -> authored recovery/removal without partial aftermath or hidden-state leakage.

Use the live Bulletin for D-072/D-073 ownership/readiness; this contract does not reserve either task.

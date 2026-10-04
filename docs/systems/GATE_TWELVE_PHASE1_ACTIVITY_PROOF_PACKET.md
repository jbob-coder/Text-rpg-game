# THE GAME — Gate Twelve Phase 1 Activity Proof Packet

Status: **CURRENT-STATE GROUNDED / PHASE 1 ACTIVITY CONTRACT / NO NEW RUNTIME REQUIRED FOR FIRST PROOF**
Parents:
- docs/systems/PLAYER_ACTIVITIES_AND_LIFE_LOOP_MASTER_PLAN.md
- docs/systems/TRAINING_AND_PRACTICE_ACTIVITY_STANDARD.md
- docs/systems/RECOVERY_REST_TREATMENT_ACTIVITY_STANDARD.md
- docs/systems/WORK_STUDY_RESEARCH_ACTIVITY_STANDARD.md
Phase 1:
- docs/PHASE_1_SOLO_PLAYABLE_PARALLEL_TRACK.md
Current source:
- content/vertical_slice_01.json
- src/textrpg/simulation.py
- src/textrpg/powers.py

## 1. Purpose

Choose one bounded activity path that satisfies Phase 1 requirement #8 using current Gate Twelve content and existing engine primitives rather than inventing a job/economy system.

## 2. Selected proof loop

The Phase 1 proof activity is:

**Trace Chamber controlled practice + recovery**

Current content already provides:
- TRACE_CHAMBER location;
- Trace Echo ability;
- TECHNIQUE_SIGNAL_PULSE;
- practice flow;
- focus and Trace Resonance costs;
- COND_ECHO_STRAIN drawback;
- 30-minute recovery;
- later Directional Trace training/recovery;
- quest integration.

This is the strongest current proof because it already integrates time, resources, progression, condition/recovery, knowledge, and quest state.

## 3. Activity identities

Target normalized IDs for later activity-registry migration:
- ACTIVITY_TRACE_SIGNAL_PULSE_PRACTICE
- ACTIVITY_TRACE_RESONANCE_RECOVERY
- ACTIVITY_DIRECTIONAL_TRACE_PRACTICE
- ACTIVITY_TRACE_CHAMBER_ANALYSIS

These are proposed normalization IDs. Current scene/effect behavior remains authoritative until migration.

## 4. Signal Pulse practice

Execution class:
- timed active.

Location:
- TRACE_CHAMBER.

Consumes:
- world time from authored technique practice;
- technique-defined resources.

Requirements:
- ABILITY_TRACE_ECHO discovered;
- TECHNIQUE_SIGNAL_PULSE available;
- any current technique requirements.

Outputs:
- technique mastery/progress;
- ability mastery where current power rules specify;
- quest objective progress where authored;
- COND_ECHO_STRAIN or other current drawback exactly as the power definition specifies.

No generic XP reward is added.

## 5. Recovery

After technique strain, the current activity loop may use power-specific recovery, general recovery when appropriate, world time advancement, and timed-condition decay.

The existing 30-minute Trace Resonance recovery path is the Phase 1 proof.

Recovery must not erase unrelated injuries/conditions unless their own duration/treatment rules permit it.

## 6. Cross-domain proof

This one loop proves integration with:
- V06 progression: mastery/technique;
- V10 activities: timed action;
- resources: focus/Trace Resonance;
- conditions: Echo Strain;
- quests: Gate Twelve Echo;
- world/location: Trace Chamber;
- knowledge: Trace Echo interpretation;
- save/load: ability, quest, condition/time consequences;
- Android: contextual action presentation later.

## 7. Phase 1 acceptance scenario

From a valid save:
1. arrive at Trace Chamber through current legal content flow;
2. verify Signal Pulse practice is available;
3. begin practice;
4. world time advances;
5. costs are paid;
6. mastery/progression changes;
7. strain/drawback applies;
8. quest state updates where appropriate;
9. perform the authored recovery action;
10. time advances again;
11. resources recover according to current rules;
12. save;
13. reload;
14. confirm time, ability/progression, quest and relevant condition/resource state are preserved.

## 8. Atomicity

The practice engine call must be atomic.

If requirements/resources fail:
- no mastery gain;
- no partial cost;
- no time advancement;
- no quest progress.

Recovery follows the same validate-before-commit principle.

## 9. UI contract

Future activity presentation may show:
- activity name;
- location;
- duration;
- known costs;
- current resource sufficiency;
- known drawback summary;
- broad expected progression result;
- start action.

It must not show hidden technique thresholds, hidden future unlocks, or secret quest outcomes.

## 10. Performance

No continuous simulation is needed.

The entire Phase 1 proof resolves through bounded Python calls and ordinary state projection, making it appropriate for Galaxy A02-class targets by design. This is not measured device evidence.

## 11. Existing versus missing

CURRENT:
- location;
- power/technique;
- practice/recovery primitives;
- time;
- resource costs;
- condition drawback;
- quest flow.

PENDING NORMALIZATION:
- reusable activity registry;
- generic activity projection;
- Android activity-specific presentation;
- dedicated normalized-activity tests.

Phase 1 requirement #8 can be satisfied by validating this current integrated loop even before the generic activity registry exists, provided exact-head tests prove the behavior.

## 12. Tests

Required for Phase 1 closure:
- practice requirements;
- resource insufficiency rollback;
- mastery gain;
- time advancement;
- drawback application;
- recovery;
- quest progression;
- save/load persistence;
- player-safe preview;
- no UI-owned mutation.

## 13. Result

This packet selects an existing original Gate Twelve gameplay loop as the Phase 1 activity proof.

Do not block Phase 1 on a full employment/calendar/background-activity system.

# THE GAME — Recovery, Rest & Treatment Activity Standard

Status: **APPROVED FIRST-PASS V10 CONTRACT / CURRENT RESOURCE RECOVERY EXISTS**
Parents:
- docs/systems/PLAYER_ACTIVITIES_AND_LIFE_LOOP_MASTER_PLAN.md
- docs/systems/INJURY_CONDITION_AFTERMATH_STANDARD.md
Current source:
- src/textrpg/simulation.py
- src/textrpg/powers.py

## 1. Purpose

Separate ordinary resource recovery, ability-specific recovery, rest, medical treatment, and injury rehabilitation so “rest” does not become one universal cure button.

## 2. Current foundations

Current simulation.recover:
- consumes world minutes;
- restores health/stamina/focus/resolve using authoritative maxima;
- accepts quality;
- advances timed conditions.

Current powers recover_power_resource handles ability-specific recovery.

Current content includes:
- 30-minute Trace Resonance recovery;
- 60-minute Directional Trace recovery;
- 8-hour general resource recovery.

## 3. Recovery categories

Use:
- RESOURCE_RECOVERY;
- ABILITY_RESOURCE_RECOVERY;
- REST;
- SLEEP when calendar/needs require it;
- FIELD_TREATMENT;
- MEDICAL_TREATMENT;
- REHABILITATION.

Not all categories need Phase 1 runtime.

## 4. Recovery definition

Fields:
- activity_id;
- category;
- duration;
- allowed location/facility;
- quality;
- resources affected;
- condition requirements;
- condition effects;
- item/tool requirements;
- participant/medical skill requirement;
- interruption policy;
- repeat rule.

## 5. General resource recovery

Must preserve:
- derived maxima;
- clamping;
- time advancement;
- condition duration handling.

Recovery should not grant progression unless explicitly authored.

## 6. Ability-specific recovery

Ability resource recovery uses its own definition.

General rest must not refill a special resource merely because UI labels both “rest,” unless the ability contract says so.

Current Trace Resonance recovery remains separate evidence.

## 7. Treatment

Treatment can:
- reduce severity;
- remove condition;
- stabilize condition;
- change duration.

It requires a condition-specific rule.

No generic treatment may remove every injury.

## 8. Proposed Phase 1 combat injury

GATE_TWELVE_PHASE1_TACTICAL_ENCOUNTER_PACKET proposes COND_TUNNEL_LEG_INJURY.

For documentation proof, treatment may use:
- 120 world minutes;
- a safe recovery context;
- no mandatory medical item until V07 approves one.

Before implementation, exact condition modifiers/removal rule must be added to a condition/treatment catalog.

## 9. Safe/unsafe rest

Later world systems may modify quality based on:
- location;
- shelter;
- danger;
- medical facility;
- interruption risk.

Phase 1 does not need survival-rest simulation.

## 10. Interruption

If recovery is atomic in current content:
- validate and complete as one transaction.

Future long rest may be interruptible:
- elapsed time remains;
- partial resource gain policy explicit;
- events/encounters may interrupt.

## 11. Conditions

Time passing may expire timed conditions.

Persistent injuries with no duration do not disappear simply because general recovery restored health.

## 12. NPC assistance

Medical/mentor assistance requires NPC availability and capability.

Relationship alone is not medical competence.

## 13. Player-safe preview

Show:
- duration;
- known resources restored qualitatively or numerically;
- treatment target;
- known item/facility requirement;
- interruption risk if known.

Hidden complications remain hidden unless the player can know them.

## 14. Tests

Required:
- maxima clamping;
- zero/invalid duration policy;
- ability-specific vs general recovery separation;
- timed-condition expiry;
- persistent injury not auto-cleared;
- treatment-specific removal;
- interruption transaction;
- save/load;
- current Trace recovery fixtures.

## 15. Phase 1

Current resource/Trace recovery already provides the basic time-cost proof.

The new combat injury requires one dedicated treatment path before requirement #10 becomes runtime-ready.

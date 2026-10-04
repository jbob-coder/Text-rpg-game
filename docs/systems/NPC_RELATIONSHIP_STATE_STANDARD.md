# THE GAME — NPC Relationship State Standard

Status: **APPROVED FIRST-PASS V05 CONTRACT / CURRENT RUNTIME FOUNDATION EXISTS**
Parent:
- docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md
Current source:
- src/textrpg/social.py
- src/textrpg/core.py

## 1. Purpose

Define multidimensional relationships so social consequences remain explainable and do not collapse into one universal approval score.

## 2. Current authoritative axes

Current source axes:
- trust;
- respect;
- affection;
- fear;
- suspicion;
- debt;
- loyalty.

These seven axes are the first-pass runtime-compatible taxonomy.

Potential older suggestions such as hostility/rivalry are not added to this base container until migration/design proves a need.

## 3. Range

Each axis is clamped to -100..100.

Zero means no directional weight, not necessarily stranger status.

## 4. Axis meanings

Trust:
reliability/safety/dependability.

Respect:
regard for competence, conviction, status, or conduct.

Affection:
emotional fondness/care.

Fear:
perceived threat/danger.

Suspicion:
expectation of hidden or misleading motives/information.

Debt:
perceived obligation.

Loyalty:
willingness to maintain commitment to this specific target.

Axes may conflict. High respect plus high fear is valid. High affection plus high suspicion is valid.

## 5. Relationship vs personality

Relationship loyalty is target-specific.

Personality loyalty is a general behavioral tendency.

Never substitute one for the other.

## 6. Relationship events

Every meaningful update should identify:
- npc_id;
- source event/choice;
- axis deltas;
- before;
- after;
- turn/time;
- optional memory link.

Current adjust_relationship supports bounded atomic multi-axis updates and history.

Content-level single-axis effects should eventually route through the same hardened primitive.

## 7. Change sizing guidance

Authoring guidance:
- 1..3 small signal;
- 4..8 meaningful;
- 9..15 major;
- >15 exceptional and explicitly justified.

Do not farm one trivial repeatable action for unbounded relationship gain.

## 8. Gates

Social requirements can combine axes.

Current opening recovery already uses:
- trust minimum;
- suspicion maximum.

The engine owns gating. UI only displays safe availability/reason.

## 9. Qualitative tiers

Future UI may show qualitative tiers.

If introduced:
- domain layer computes them;
- Compose does not independently bucket raw values;
- hidden axes may remain hidden.

## 10. Negative values

Negative trust/loyalty are allowed when justified.

Fear and suspicion use higher positive values for more fear/suspicion, so negative values require deliberate semantics rather than generic friendliness.

## 11. Decay

No universal passive decay in Phase 1.

Future decay requires axis-specific policy, elapsed world time, deterministic rules, floors/caps, and story exceptions.

## 12. Faction reputation

Faction reputation is not a fake NPC relationship.

It belongs to a separate faction/reputation authority and may influence individual NPCs only through explicit rules.

## 13. Combat/social integration

Combat aftermath may alter relationship axes only through authored consequences.

Do not universally reward winning with respect.

## 14. Player-safe projection

Exact axis values may remain hidden.

Potential safe outputs:
- qualitative relationship;
- visible recent changes;
- social gate reason where transparency is intended.

## 15. Tamsin current baseline

Current starting values:
- trust 15;
- respect 5;
- affection 0;
- fear 0;
- suspicion 5;
- debt 0;
- loyalty 0.

Current authored events:
- recovery help increases trust by 2;
- invitation can increase trust by 3 or 1 depending route;
- withholding Gate Twelve increases suspicion by 4.

These are regression fixtures.

## 16. Tests

Required:
- only valid axes;
- clamping;
- atomic multi-axis update;
- min/max gates;
- conflicting axes independent;
- history source;
- no UI mutation;
- save/load;
- Tamsin opening regression.

## 17. Migration

Preserve current seven axes and stable NPC IDs.

If rivalry/hostility later appears, first decide whether it is derived, adversary-specific, faction state, or a new relationship axis.

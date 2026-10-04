# THE GAME — Adversary Lifecycle & Recurrence Standard

Status: **APPROVED FIRST-PASS V09 CONTRACT**
Parent:
- docs/systems/PERSISTENT_ADVERSARY_WORLD_MEMORY_MASTER_PLAN.md
Related:
- docs/systems/NPC_SCHEDULE_PRESENCE_STANDARD.md
- docs/systems/INJURY_CONDITION_AFTERMATH_STANDARD.md

## 1. Purpose

Define when a persistent adversary is active, unavailable, recovering, captured, displaced, retired or dead, and when they can logically recur.

## 2. Lifecycle vocabulary

First-pass states:
- active;
- injured;
- recovering;
- displaced;
- captured;
- retired;
- dead;
- unknown.

These states describe world availability, not player knowledge.

## 3. State transitions

Examples:
active -> injured
- significant aftermath injury.

injured -> recovering
- removed from active recurrence while treatment/time proceeds.

recovering -> active
- recovery condition/time/facility satisfied.

active -> captured
- encounter/social/legal outcome.

captured -> active/displaced/retired
- escape/release/transfer event.

active -> dead
- authoritative permanent death.

active -> retired
- authored non-death permanent exit.

## 4. Recurrence query

An adversary is recurrence-eligible only if:
- lifecycle permits;
- location/route permits;
- goal/faction permits;
- time/cooldown rule permits;
- quest/world state permits;
- encounter type supports that actor;
- actor has not been permanently removed.

## 5. No forced cameo

The system must be allowed to return:
- no eligible adversary.

Do not insert a recurring actor into an unrelated scene solely because the feature should be visible.

## 6. Recovery time

Recovery must use world time/condition rules.

No instant full restoration between encounters unless an explicit canon mechanism says so.

## 7. Capture

Captured state should define:
- custodian/location;
- legal/faction state;
- escape/release conditions;
- player-safe knowledge;
- reference safety.

Captured does not mean erased.

## 8. Death and retirement

Dead/retired state is durable.

Future content must not resurrect/reuse the same identity accidentally.

Successors use new IDs.

## 9. Unknown location

unknown means world authority does not currently expose/track a precise location at the chosen simulation scale.

It is not permission to teleport the actor.

## 10. Determinism

Recurrence candidate selection is deterministic for identical authoritative state.

If random variety is used:
- seed is stable;
- selected result is persisted when consequence-bearing.

## 11. Performance

Evaluate recurrence on event boundaries rather than continuously.

Potential boundaries:
- travel;
- time-window transition;
- quest/faction event;
- encounter generation;
- explicit pursuit event.

## 12. Tests

Required:
- dead/retired never recur;
- recovering blocked until valid;
- captured blocked unless release/escape;
- valid route/location required;
- no eligible candidate supported;
- deterministic candidate order;
- save/load lifecycle.

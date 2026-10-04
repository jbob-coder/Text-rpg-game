# THE GAME — NPC Schedule, Location & Presence Standard

Status: **APPROVED FIRST-PASS V05 CONTRACT / TARGET SYSTEM NOT IMPLEMENTED**
Parents:
- docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md
- docs/world/WORLD_NPC_POPULATION_STANDARD.md
World movement:
- docs/world/WORLD_TRAVEL_AND_ROUTES.md
Player-safe actor projection:
- docs/android/PLAYER_SAFE_ROOM_ACTOR_PROJECTION_CONTRACT.md

## 1. Purpose

Define where a persistent NPC is, what they are normally doing, how schedules yield to emergencies/goals/quests, and how room presence becomes player-safe actor projection.

The system must prevent one NPC from appearing in multiple physical locations and must stay cheap enough for low-end Android.

## 2. Current reality

Current GameState has no dedicated universal schedule field.

Current NPC state has personality, knowledge, memories, goals, and story_state.

Current opening content can add/remove NPC_TAMSIN from party and move her story track through states.

Current Android actor presence still has transitional scene/location heuristics documented elsewhere.

Therefore schedule/location is a target contract, not a current full runtime subsystem.

## 3. Authoritative location state

A persistent physical NPC needs one authoritative current location reference.

Target runtime fields may include:
- current_location_id;
- location_since_minutes;
- current_activity_id;
- schedule_entry_id;
- presence_mode;
- travel_route_id when in transit;
- override reason.

Do not infer authoritative presence from UI sprite state.

## 4. Presence modes

Recommended:
- PRESENT;
- IN_TRANSIT;
- OFFSCREEN_KNOWN;
- OFFSCREEN_UNKNOWN;
- PARTY;
- UNAVAILABLE;
- REMOVED.

PARTY is a special presence mode synchronized with state.party.

REMOVED requires lifecycle reason such as dead, captured, hospitalized, relocated, retired, or story-removed.

## 5. Schedule record

A schedule entry should define:
- schedule_entry_id;
- start condition/time window;
- end condition/time window;
- location_id;
- activity_id;
- recurrence;
- priority;
- prerequisites;
- interruption policy;
- travel requirement;
- fallback behavior.

A schedule may be daily/weekly/event-based, but Phase 1 should not simulate a full calendar before needed.

## 6. Time granularity

For low-end performance:
- near-player/high-fidelity NPC: evaluate when world time crosses relevant boundary or scene changes;
- recurring off-screen NPC: evaluate coarse scheduled events;
- aggregate population: statistical simulation only.

Do not tick every NPC every frame or every in-game minute.

## 7. Precedence

Suggested precedence from strongest to weakest:
1. death/capture/permanent lifecycle;
2. active tactical combat/critical emergency;
3. explicit story/quest override;
4. party membership/player travel;
5. high-priority urgent goal;
6. institutional/faction duty override;
7. normal schedule;
8. fallback/home behavior.

A lower layer cannot silently teleport over a higher one.

## 8. Travel

If schedule moves an NPC between locations:
- route must exist or a valid abstract off-screen route must be documented;
- travel consumes world time logically;
- NPC cannot appear at destination before travel completion;
- encounter interruption may pause/replace travel.

For Phase 1 Gate Twelve, avoid simulating unknown external routes.

## 9. Room presence

Room actor projection must be derived from authoritative current presence plus player visibility/knowledge.

Presence record may project:
- actor_id;
- semantic placement anchor;
- visual family;
- interaction availability;
- safe context status.

It must not expose private destination, goal, or schedule entry.

## 10. Party membership

When NPC is in state.party:
- party state and presence must agree;
- player travel moves the NPC according to party rules;
- schedule is suspended or overridden;
- leaving party requires a resolved location/fallback.

Current Tamsin party_add/party_remove behavior becomes the Phase 1 migration proof.

## 11. Goal and emergency override

A goal may request schedule override only through a deterministic rule.

Example:
GOAL_UNDERSTAND_GATE_TWELVE may justify Tamsin entering the tunnel only after story/party conditions allow it.

Curiosity alone must not teleport her to Gate Twelve.

## 12. Unknown player knowledge

Jack may not know where an off-screen NPC is.

Internal location is not automatically player-visible.

UI may project:
- “not here”;
- last known location;
- expected schedule;
only if Jack legitimately knows it.

## 13. Persistence

Current location, transit state, relevant schedule override, and durable availability must survive save/load once this system is implemented.

The schedule definition itself belongs to content/registry, not copied wholesale into every save.

## 14. Tests

Required:
- no double physical presence;
- party/presence consistency;
- schedule boundary transition;
- story override precedence;
- travel duration;
- emergency override;
- removed NPC never respawns from schedule;
- player-safe unknown location;
- save/load;
- low-frequency off-screen update.

## 15. Phase 1 scope

Phase 1 does not require a city-wide daily routine.

For NPC_TAMSIN it needs:
- presence in opening depot scenes;
- party-follow state when she joins;
- remaining at depot when player asks her to stay;
- no duplicate actor after branch divergence;
- future post-encounter location explicitly resolved.

That is enough to prove the schedule/presence architecture before larger world simulation.

# THE GAME — Persistent Adversary Schema & API Migration Packet

Status: **APPROVED MIGRATION DESIGN / D-032 V09 CHILD / IMPLEMENTATION NOT STARTED**
Repository: jbob-coder/Text-rpg-game
Parents:
- docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md
- docs/systems/PERSISTENT_ADVERSARY_WORLD_MEMORY_MASTER_PLAN.md
- docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md
- docs/systems/SAVE_AND_CONTENT_MIGRATION_MASTER_PLAN.md
- docs/android/ANDROID_CONSUMER_AND_PROJECTION_MAP.md

Related:
- docs/systems/ADVERSARY_ELIGIBILITY_IDENTITY_STANDARD.md
- docs/systems/ADVERSARY_ENCOUNTER_MEMORY_ADAPTATION_STANDARD.md
- docs/systems/ADVERSARY_LIFECYCLE_RECURRENCE_STANDARD.md
- docs/systems/ADVERSARY_HIERARCHY_SUCCESSION_STANDARD.md
- docs/systems/ADVERSARY_TERRITORY_ROUTING_STANDARD.md
- docs/systems/ADVERSARY_PLAYER_SAFE_INTEL_STANDARD.md
- docs/systems/GATE_TWELVE_ADVERSARY_PROOF_PACKET.md

## 1. Purpose

Map V09 persistent-adversary/world-memory target design onto the current Python GameState, social primitives, strict save contract, Android bridge and player-safe projection boundary without creating a second gameplay authority or forcing an unnecessary top-level save migration.

This is an implementation-specific migration contract. It does not create a canonical recurring enemy, implement runtime behavior, approve a faction ladder, or make V09 a Phase 1 requirement.

## 2. Current source reality

Current durable GameState contains 17 top-level fields:

- seed;
- scene_id;
- turn;
- time_minutes;
- player;
- flags;
- relationships;
- knowledge;
- inventory;
- quests;
- npcs;
- party;
- abilities;
- equipment;
- perks;
- schema_version;
- history.

Current social.py already provides durable primitives for:

- ensure_npc;
- add_memory;
- npc_learn;
- share_knowledge;
- eligible_leak_targets;
- execute_leak_event;
- adjust_relationship;
- relationship_meets;
- set_goal;
- update_goal_progress;
- transition_story_state.

ensure_npc currently normalizes these NPC-owned containers:

- personality;
- knowledge;
- memories;
- goals;
- story_state.

It does not yet define a persistent-adversary record.

Current persistence.py:

- uses CURRENT_SCHEMA_VERSION = 1;
- serializes the entire GameState snapshot;
- rejects unknown top-level save fields;
- accepts existing GameState fields such as npcs;
- validates only the current top-level GameState structure before save/load.

Current AndroidGameSession:

- owns the authoritative GameState;
- builds a player-safe view through _view_for;
- exposes status, inventory, quests, map, visuals and metadata;
- has no adversary-intel projection or adversary action API.

## 3. Core migration decision

The first persistent-adversary implementation should extend the existing per-NPC durable record rather than add a new top-level GameState field.

Preferred first implementation boundary:

`state.npcs[npc_id]["adversary"]`

This keeps stable NPC identity as the root identity and prevents a second actor registry from competing with social/world state.

This is compatible with the current top-level save schema v1 only if implementation proves all of the following:

1. old saves with no adversary nested record still load unchanged;
2. the nested record is strict-JSON serializable;
3. validate_game_state_structure remains valid;
4. social.py operations preserve unknown-but-valid sibling NPC fields;
5. save -> load round-trip preserves the nested record exactly;
6. malformed nested adversary state is rejected by new dedicated validation before it can be used.

This packet is the required migration contract for that nested extension.

A new top-level GameState field such as `adversaries` is **not** approved by this packet. That change would require an explicit save schema v2+ migration.

## 4. Ownership boundaries

NPC identity/profile owns:
- stable NPC ID;
- identity;
- personality;
- relationships;
- general memories;
- knowledge;
- goals;
- social/story state.

V09 adversary record owns only adversary-specific persistence:
- eligibility provenance;
- lifecycle;
- recurrence bookkeeping;
- adaptation records/references;
- persistent-adversary encounter references;
- removal/retirement state;
- V09-specific routing/territory references when those owners exist.

World/social authorities continue to own:
- canonical faction membership;
- faction rank/role;
- world location IDs;
- route legality;
- political hierarchy;
- schedules/presence.

Combat owns:
- transient tactical cells;
- current activation state;
- tactical LOS/cover;
- encounter-local actors.

The V09 record references those authorities; it does not copy them into a rival-only parallel world model.

## 5. Nested adversary record

Recommended first-pass runtime shape:

```text
npcs[npc_id].adversary = {
  record_version,
  eligibility,
  lifecycle,
  encounter_refs,
  adaptations,
  recurrence,
  routing_refs,
  hierarchy_refs,
  removal
}
```

Fields may be absent until meaningful. Do not populate invented defaults merely to fill the shape.

### record_version

Start with integer 1 for the nested V09 record.

This is not GameState.schema_version.

It allows future adversary-record migration while the top-level save envelope remains schema v1.

## 6. Eligibility block

Minimum:

- status;
- eligibility_rule_id;
- source_event_id;
- source_actor_id when promoted from encounter-local actor;
- promoted_at_turn/time;
- allowed_adaptation_families;
- allowed_recurrence_contexts;
- canon_status/provenance when content requires it.

Eligibility creation must be explicit.

Survival of an encounter alone does not create this block.

## 7. Lifecycle block

Minimum:

- state;
- entered_at_turn/time;
- source_event_id;
- reason;
- recovery/unavailable-until reference when applicable.

Allowed vocabulary comes from ADVERSARY_LIFECYCLE_RECURRENCE_STANDARD.md.

Lifecycle state is world truth.

Player knowledge of that state is separate.

## 8. Encounter references

Do not copy the full tactical event log.

Store only stable references/summaries needed for V09 causality, for example:

- encounter_id;
- aftermath_event_id;
- memory_ids;
- knowledge_ids;
- outcome category;
- last significant encounter time.

Detailed remembered facts continue to live in npc.memories.

Beliefs/known facts continue to live in npc.knowledge.

## 9. Adaptation records

Recommended map:

`adaptations[adaptation_id]`

Each record references:

- source_memory_id and/or source_knowledge_id;
- adaptation category;
- selected authored option;
- applied_at turn/time;
- cost/resource/time reference when applicable;
- expiration/permanence;
- rationale/provenance.

Do not store hidden "player counter" omniscience.

An adaptation is invalid if its source memory/knowledge cannot justify it.

## 10. Recurrence state

Recommended fields:

- last_encounter_id;
- last_encounter_turn/time;
- next_eligible_time only if a cooldown rule is adopted;
- blocked_reason;
- last_recurrence_event_id.

Recurrence eligibility must be a query over:

- lifecycle;
- valid world location/route;
- goals/faction assignment;
- quest/world state;
- authored timing rule;
- encounter context.

Querying eligibility must not mutate state.

"No eligible adversary" is a valid result.

## 11. Routing and territory references

Do not store tactical coordinates.

V09 may retain:

- current_location_ref only if the NPC/world presence owner has not yet been normalized;
- territory IDs;
- active movement-plan ID;
- route/path references;
- pursuit target knowledge reference.

Preferred long-term direction:
- normalized NPC presence/world-location authority owns current location;
- V09 keeps only recurrence/routing intent and references.

Until that owner exists, any temporary V09 location field must be marked transitional in code/tests and must use existing world location IDs.

## 12. Hierarchy references

Do not duplicate canonical faction rank inside the V09 record.

V09 may retain:
- faction membership reference;
- assignment/role reference;
- last promotion/demotion event ID;
- succession event references.

The faction/social registry remains authoritative for actual membership/rank once implemented.

A successor receives a new stable NPC ID.

No successor inherits private memories automatically.

## 13. Proposed Python module boundary

Recommended:

src/textrpg/adversaries.py
- validate_adversary_record;
- promote_adversary_candidate;
- transition_adversary_lifecycle;
- record_adversary_encounter;
- apply_adversary_adaptation;
- adversary_recurrence_eligible;
- select_eligible_adversaries;
- remove_or_retire_adversary;
- build_player_safe_adversary_intel.

Optional later split only if complexity proves it necessary:
- adversary_schema.py;
- adversary_routing.py;
- adversary_selection.py.

Do not create many files merely to mirror documentation headings.

## 14. API behavior

### promote_adversary_candidate

Inputs:
- persistent npc_id;
- eligibility rule/provenance;
- optional source encounter-local actor ID;
- source event.

Preconditions:
- stable NPC identity exists or is created through the character authority;
- eligibility rule is authored;
- no incompatible existing adversary record.

Writes:
- nested adversary record;
- one durable history event;
- only legitimate migrated memory/knowledge/injury references.

Must be atomic.

### record_adversary_encounter

Consumes validated aftermath, not raw Compose state.

May:
- add deliberate npc memory through add_memory;
- add learned facts through npc_learn;
- update V09 encounter_refs;
- update lifecycle;
- propose/apply an authored adaptation;
- append one durable V09 summary event.

Must not persist the full tactical log.

### transition_adversary_lifecycle

Validates old -> new transition and provenance before mutation.

Permanent dead/retired states block recurrence unless a separate canon mechanism explicitly overrides that rule.

### adversary_recurrence_eligible

Read-only.

Must not:
- create NPC shells;
- create memories;
- move the actor;
- consume RNG state;
- reveal hidden data.

## 15. Determinism

If multiple adversaries are eligible, ordering/selection must be deterministic for the same authoritative inputs.

Preferred deterministic key includes:

- state.seed;
- recurrence context ID;
- location ID;
- world time bucket or exact time input;
- candidate stable IDs;
- committed event index if random selection is required.

Preview/UI queries must not advance randomness or mutate history.

Authored deterministic selection is preferred for the first proof.

## 16. Content schema

Do not add V09 definitions to the current fixed registries object without a validator/migration decision.

Preferred target content section:

- adversary_profiles

Optional section; old packs remain valid when absent.

A profile may define:
- profile_id;
- eligible NPC/source actor refs;
- eligibility rules;
- allowed adaptation families/options;
- recurrence contexts;
- lifecycle constraints;
- territory/faction references;
- canon status.

content.py must explicitly read and validate the section before runtime consumes it.

If implementation instead embeds V09 authoring in character records, document and validate that choice first. Do not silently rely on ignored raw fields.

## 17. Save compatibility decision

First implementation target:

- GameState.schema_version remains 1;
- nested npc.adversary record uses record_version 1;
- missing nested record means "not a persistent adversary";
- old saves remain valid;
- new saves round-trip in the current envelope.

Mandatory tests before claiming compatibility:

1. load historical/current schema-v1 save without adversary fields;
2. add valid nested adversary record;
3. save;
4. load;
5. compare snapshot exactly;
6. reject malformed nested record before V09 runtime action;
7. ensure unrelated NPC/social actions preserve the nested record.

If any current validator/consumer cannot safely preserve nested state, stop and create explicit schema v2 migration instead of weakening validation.

## 18. Android projection

Add no raw V09 state to Compose.

Preferred Python projection:

`adversary_intel`

This is optional and player-safe.

Potential records:
- contact ID safe for UI;
- identity discovery state;
- known name/alias;
- known faction/role;
- last known location with confidence/time;
- last encounter summary;
- visible injuries;
- observed equipment/techniques;
- learned/rumored behavior;
- known lifecycle status only when learned;
- source/confidence labels where useful.

Never project:
- hidden current location;
- private goals;
- adaptation candidates;
- recurrence cooldown internals;
- hidden faction orders;
- exact utility/selection scores;
- succession candidates;
- unknown abilities.

## 19. AndroidGameSession

No generic mutation API such as setAdversaryState.

If/when player actions need V09 interaction, expose domain actions, for example:

- inspect_adversary_intel(contact_id);
- investigate_adversary(contact_id, action_id);
- resolve authored encounter/quest action through existing engine APIs.

Most V09 changes should be consequences of:
- encounter aftermath;
- world events;
- faction events;
- authored choices;
- time/simulation events.

The UI does not directly promote, adapt, move, rank or revive adversaries.

## 20. Kotlin / Compose boundary

When adversary_intel is added:

- define typed DTOs;
- mapper treats missing field as empty/not available for backward compatibility;
- reject malformed required fields;
- keep confidence/source semantics explicit;
- no hidden/raw map crosses to Compose.

D-049 still owns final screen placement.

This packet does not finalize a Nemesis-style hierarchy screen or any equivalent branded presentation.

## 21. Phase 1 boundary

Phase 1 does not require a persistent adversary.

The current proposed Service Tunnel encounter may remain entirely encounter-local.

GATE_TWELVE_ADVERSARY_PROOF_PACKET.md is a later proof candidate.

Therefore:
- do not block Phase 1 tactical implementation on V09 runtime;
- do not auto-promote either unknown contact;
- do not invent a faction or stable enemy identity to demonstrate V09.

Phase 1 requirement #11 world-state consequence may continue using existing flags/scene/actor consequences without requiring the full adversary network.

## 22. World-memory integration

V09 world memory is not one global omniscient dictionary.

Use existing owners:
- state.history for durable authoritative event summaries;
- npc.memories for remembered experiences;
- npc.knowledge for belief/known-fact state;
- relationships for social deltas;
- flags/quests for authored world/quest consequences;
- V09 record for adversary-specific lifecycle/recurrence/adaptation references.

Future faction/world memory should gain its own owner only when its schema and consumers are defined.

## 23. Performance boundary

Low-end target behavior must be event-driven.

Do not tick every persistent adversary every frame.

Preferred triggers:
- world-time boundary;
- travel completion;
- quest/world event;
- encounter aftermath;
- explicit simulation step.

Recurrence query should operate on a bounded candidate set filtered by:
- region/location;
- lifecycle;
- assignment/territory;
- relevant context.

No Galaxy A02/A03 compatibility claim is allowed until measured.

## 24. Failure and rollback

Every multi-write V09 operation must snapshot/validate before durable mutation.

On failure:
- no partial memory;
- no partial lifecycle transition;
- no partial adaptation;
- no partial history event.

Until a canonical adversary is authored, the entire V09 runtime can be absent without breaking current Gate Twelve story play.

If the first implementation is reverted:
- remove V09 module/actions/projection;
- ignore/remove authored adversary_profiles through content migration;
- schema-v1 saves without V09 records remain unchanged;
- saves containing V09 nested records require an explicit downgrade/compatibility decision before destructive removal.

## 25. Tests

Python unit:
1. nested record validation;
2. eligibility promotion atomicity;
3. stable identity preserved across display/faction/location changes;
4. deliberate encounter memory only;
5. perception/knowledge boundary;
6. adaptation requires traceable source;
7. lifecycle legal/illegal transitions;
8. recurrence query read-only;
9. deterministic candidate selection;
10. permanent removal blocks recurrence;
11. successor does not inherit memories;
12. disconnected-route rejection;
13. player-safe intel redaction;
14. malformed V09 content rejected.

Persistence:
15. old schema-v1 save loads;
16. nested V09 record round-trips;
17. social operations preserve nested record;
18. post-encounter V09 state survives save/load;
19. malformed nested record cannot drive runtime.

Android/JVM:
20. missing adversary_intel remains backward compatible;
21. valid intel maps to typed DTO;
22. hidden fields are absent;
23. malformed intel fails safely.

Instrumentation later:
24. discover/inspect known adversary intel;
25. save/reload known intel;
26. verify no hidden current location/goal appears.

## 26. Implementation order

Smallest safe sequence:

1. add adversary nested-record validator;
2. add read-only eligibility/lifecycle/recurrence query helpers;
3. add explicit promotion transaction;
4. reuse social memory/knowledge primitives for encounter aftermath;
5. add adaptation validation;
6. add optional adversary_profiles validation;
7. add save round-trip/regression tests;
8. add player-safe Python intel projection;
9. add typed Kotlin mapping only when a real UI consumer exists;
10. author/select one canon-approved proof adversary only after owner/content approval;
11. integrate routing/faction hierarchy only against their authoritative registries;
12. profile bounded recurrence selection.

## 27. Gate to implementation

Implementation may start only when:

- this packet remains consistent with current branch/HEAD;
- the V09 first-pass contract layer is synchronized into master records;
- no canonical recurring enemy is invented as part of plumbing work;
- intended files/tests are recorded in the task register;
- stable-ID and save compatibility tests are included in the first code-bearing slice.

## 28. Result

D-032 now has a persistent-adversary/world-memory migration child at first-pass implementation depth.

Still separate:
- progression migration;
- broader social migration;
- item/economy migration;
- V09 runtime implementation;
- selection of a canonical Gate Twelve adversary;
- final adversary UI;
- final APK teardown/rebuild.

This packet changes no runtime behavior and no save data.

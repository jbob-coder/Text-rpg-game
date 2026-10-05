# THE GAME — Social Schema & API Migration Packet

Status: **APPROVED MIGRATION DESIGN / D-032 V05 CHILD / IMPLEMENTATION NOT STARTED**  
Repository: `jbob-coder/Text-rpg-game`  
Authority branch: `docs/master-game-development-program`  
Task: **D-062 — broader social schema/API migration child**

Parents:
- `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`
- `docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md`
- `docs/systems/SAVE_AND_CONTENT_MIGRATION_MASTER_PLAN.md`
- `docs/android/ANDROID_CONSUMER_AND_PROJECTION_MAP.md`

Related:
- `docs/systems/NPC_CHARACTER_IDENTITY_PROFILE_STANDARD.md`
- `docs/systems/NPC_MEMORY_EVENT_STANDARD.md`
- `docs/systems/NPC_KNOWLEDGE_BELIEF_PRIVACY_STANDARD.md`
- `docs/systems/NPC_RELATIONSHIP_STATE_STANDARD.md`
- `docs/systems/NPC_GOALS_DECISION_STANDARD.md`
- `docs/systems/NPC_SCHEDULE_PRESENCE_STANDARD.md`
- `docs/systems/TAMSIN_PHASE1_SOCIAL_PROOF_PACKET.md`
- `docs/systems/PERSISTENT_ADVERSARY_SCHEMA_API_MIGRATION_PACKET.md`

## 1. Purpose

Map the current NPC/social runtime and the V05 target contracts onto one implementation path without creating a second gameplay authority, leaking private NPC state, or forcing an unnecessary save-schema migration.

This packet is implementation-specific. It defines:
- current state ownership;
- stable-ID preservation;
- authoritative mutation APIs;
- content-effect migration;
- save compatibility;
- player-safe projection boundaries;
- Android mapping requirements;
- Phase 1 Tamsin compatibility;
- rollback and test requirements;
- the order in which code should change.

This packet does **not** implement D-065, D-064, final social UI, schedules, factions, or persistent-adversary runtime.

## 2. Current source reality

Current `GameState` durable top-level fields include:
- `relationships`;
- `knowledge`;
- `npcs`;
- `party`;
- `history`;
- the remaining established gameplay fields;
- `schema_version = 1`.

Current ownership is already split correctly in principle:

- `state.knowledge` = Jack/player knowledge;
- `state.relationships[npc_id]` = player-to-NPC relationship axes;
- `state.npcs[npc_id]` = NPC-owned mutable social/runtime state;
- `state.party` = current durable party membership;
- authored `characters[npc_id]` content = identity/profile source, not mutable runtime social state.

Current `ensure_npc` normalizes these NPC-owned containers:
- `personality`;
- `knowledge`;
- `memories`;
- `goals`;
- `story_state`.

Current relationship axes are:
- trust;
- respect;
- affection;
- fear;
- suspicion;
- debt;
- loyalty.

Current `social.py` authoritative primitives are:
- `ensure_npc`;
- `add_memory`;
- `npc_learn`;
- `share_knowledge`;
- `eligible_leak_targets`;
- `execute_leak_event`;
- `adjust_relationship`;
- `relationship_meets`;
- `set_goal`;
- `update_goal_progress`;
- `transition_story_state`.

Current `persistence.py`:
- uses `CURRENT_SCHEMA_VERSION = 1`;
- serializes the full `GameState.snapshot()`;
- rejects unknown top-level save fields;
- rejects unsupported schema versions;
- validates current top-level structure on save/load.

Current `AndroidGameSession._view_for` exposes:
- scene;
- status;
- inventory;
- quests;
- map;
- visuals;
- meta.

It does **not** currently expose:
- raw `state.npcs`;
- raw `state.relationships`;
- raw NPC knowledge;
- raw NPC memories;
- raw NPC goals;
- raw NPC story-state containers.

Current Kotlin `GameSnapshot` likewise has no general NPC-social/private-state payload.

That absence is currently privacy-safe and must not be replaced by raw state exposure.

## 3. Current authored Tamsin proof

Stable identity:
- `NPC_TAMSIN`.

Current starting relationship:
- trust 15;
- respect 5;
- affection 0;
- fear 0;
- suspicion 5;
- debt 0;
- loyalty 0.

Current Tamsin runtime shell contains:
- personality;
- knowledge;
- memories;
- goals;
- story_state.

Current knowledge proof:
- `KNOW_RELAY_DESTINATION_SERVICE_GATE_12`.

Current story track:
- `TRACK_RELAY_CASE`.

Current goal:
- `GOAL_UNDERSTAND_GATE_TWELVE`.

Current authored branches already exercise:
- relationship minimum/maximum gates;
- independent Jack/Tamsin knowledge;
- `npc_knows` / `npc_not_knows`;
- Tamsin relationship changes;
- Tamsin goal creation/progress;
- Tamsin story-state transitions;
- party join/stay divergence.

The missing Phase 1 social behavior remains explicit durable memory plus later memory-reactive behavior.

## 4. Migration decisions

### 4.1 Do not add a new top-level social state owner

The first social migration must keep the existing durable owners:
- `relationships`;
- `knowledge`;
- `npcs`;
- `party`;
- `history`.

Do not add top-level containers such as:
- `social`;
- `npc_memories`;
- `npc_knowledge`;
- `npc_goals`;
- `characters_runtime`.

Those would duplicate existing authority and would require broader save migration.

### 4.2 Preserve save schema v1 for the bounded migration

The D-062 target can remain compatible with save schema v1 because:
- relationship state already exists;
- NPC knowledge already exists under `state.npcs`;
- memory list already exists under `state.npcs`;
- goals already exist under `state.npcs`;
- story state already exists under `state.npcs`;
- party already exists;
- identity remains content-owned.

Schema v1 preservation is conditional on:
1. no new top-level field;
2. nested records remain strict-JSON-compatible;
3. old saves missing newly optional nested metadata still validate/use defaults;
4. new dedicated nested validators reject malformed migrated records before use;
5. old/new save round-trip tests pass.

Any new top-level durable field requires a deliberate schema v2+ migration.

### 4.3 Preserve stable IDs

Do not rename:
- `NPC_TAMSIN`;
- `KNOW_RELAY_DESTINATION_SERVICE_GATE_12`;
- `TRACK_RELAY_CASE`;
- `GOAL_UNDERSTAND_GATE_TWELVE`;
- existing scene/choice IDs;
- current relationship axis names.

Identity cleanup must not rewrite save/content references cosmetically.

## 5. Current mutation inconsistency that must be removed

There are currently two mutation styles.

Hardened social API style:
- `adjust_relationship` validates all axes before mutation, clamps values, and appends history;
- `npc_learn` validates knowledge metadata;
- `set_goal`, `update_goal_progress`, and `transition_story_state` validate through `social.py`;
- `execute_leak_event` snapshots/rolls back the affected social containers.

Direct content-effect style in `core.py`:
- `relationship` mutates `state.relationships` directly;
- `npc_learn` mutates `state.npcs[npc]["knowledge"]` directly.

This split should not remain after the migration.

It creates avoidable divergence in:
- validation;
- history/audit behavior;
- metadata defaults;
- corruption handling;
- future memory linkage;
- future privacy reasoning.

## 6. Required content-effect routing migration

### 6.1 `relationship`

Current authored shape is retained:

```json
{
  "type": "relationship",
  "npc": "NPC_TAMSIN",
  "axis": "trust",
  "value": 3
}
```

Target engine dispatch:

```python
adjust_relationship(
    state,
    effect["npc"],
    {effect["axis"]: effect["value"]},
    source=<stable authored source>,
)
```

Required behavior:
- same axis;
- same numeric delta;
- same -100..100 clamp;
- same stable NPC ID;
- no UI-side calculation;
- one relationship history event;
- failed validation cannot partially mutate state.

The authored source passed to `adjust_relationship` should be deterministic and traceable. Prefer a scene/choice/effect-derived source supplied by the transaction layer rather than free-form presentation text.

### 6.2 `npc_learn`

Current authored shape remains valid:

```json
{
  "type": "npc_learn",
  "npc": "NPC_TAMSIN",
  "knowledge_id": "KNOW_RELAY_DESTINATION_SERVICE_GATE_12",
  "source": "PLAYER",
  "confidence": 1
}
```

Target dispatch must call `social.npc_learn`.

Migration defaults:
- `truth = "unknown"`;
- `secrecy = 0`.

Optional future authored `truth` / `secrecy` may be accepted only after content validation is expanded consistently.

Important:
NPC knowledge remains NPC-private even when secrecy is zero. `secrecy` affects social sharing behavior; it is not permission to expose the entire record to Android.

### 6.3 `npc_goal_create`, `npc_goal_progress`, `npc_story_transition`

These already route through `social.py`.

Preserve that direction.

Do not replace them with direct nested-dictionary writes.

### 6.4 `personality`

Current content can mutate NPC personality directly.

The broader social migration should not expand personality mutation during D-065 unless the proof requires it.

If future authored personality mutation remains supported, it should receive a dedicated validator/API rather than becoming a generic path write.

## 7. Explicit NPC memory write path

Phase 1 requires an explicit durable Tamsin memory.

The current `add_memory` primitive is sufficient for the first bounded implementation if the content effect is added as a semantic operation rather than raw nested mutation.

Recommended new authored effect type:

`npc_memory_add`

Minimum fields:
- `npc`;
- `memory_id`;
- `importance`;
- `tags`;
- optional `data`.

Target dispatch:

```python
add_memory(
    state,
    effect["npc"],
    effect["memory_id"],
    importance=effect.get("importance", 1),
    tags=effect.get("tags", ()),
    data=effect.get("data"),
)
```

D-062 does not canonize an exact new memory ID.

D-065 should select one semantic memory tied to an existing authored Tamsin event after confirming the final content change.

Allowed proof categories from the existing packet:
- Jack willingly shared Gate Twelve;
- Jack concealed the route and left;
- Tamsin and Jack entered the tunnel together.

The first implementation does not require memory decay, event provenance expansion, or a second memory registry.

## 8. Atomic social-event boundary

`GameEngine.apply_choice` already deep-copies the authoritative `GameState` snapshot before applying effects and restores it if any effect fails.

Therefore a single authored choice can safely combine:
- relationship update;
- NPC knowledge update;
- memory write;
- goal change;
- story transition;
- party mutation;
- quest consequence;

provided each effect:
- validates before unsafe partial mutation where practical;
- throws on failure;
- does not commit external side effects outside `GameState`.

This existing choice transaction is the preferred Phase 1 event boundary.

Do not create a second transaction manager for D-065.

For direct social API calls outside a choice transaction:
- multi-container operations must keep their own rollback behavior where needed;
- `execute_leak_event` remains the current example.

## 9. Identity migration boundary

Current authored identity is content-owned under stable character IDs.

Target normalized identity work must:
- keep `NPC_TAMSIN`;
- preserve existing visual/body/outfit identity content;
- avoid copying immutable identity fields into mutable `state.npcs`;
- allow player-safe known-name/role projection later;
- preserve unknown/alias behavior when identity is not fully known.

D-062 does not require a new save field for identity.

The content registry remains the authoritative identity source for the bounded migration.

## 10. Relationship migration boundary

Keep the seven current axes unchanged.

Do not add:
- hostility;
- rivalry;
- faction reputation;

to the base relationship container in this task.

Future rivalry may be:
- derived;
- adversary-owned;
- faction-owned;
- or an explicitly migrated new axis.

All content relationship writes should converge on `adjust_relationship`.

All relationship gates remain engine-owned.

## 11. Knowledge and privacy boundary

The following ownership rule is mandatory:

### Player knowledge
Owner:
- `state.knowledge`.

May influence:
- Jack-visible choices;
- Jack-visible interpretation;
- explicitly player-safe projections.

### NPC private knowledge
Owner:
- `state.npcs[npc_id]["knowledge"]`.

May influence:
- NPC behavior;
- authored `npc_knows` / `npc_not_knows` gates;
- goals/story consequences;
- rumor/leak logic.

Must not be projected wholesale.

### World truth
Must not be inferred from either player or NPC knowledge containers.

Where a hidden authoritative truth exists, it belongs to its owning world/content system.

Android must never receive raw NPC knowledge records merely so Compose can decide what the NPC should do.

## 12. Memory privacy boundary

NPC memories are private by default.

Never project:
- full memory list;
- memory IDs not deliberately revealed;
- hidden tags;
- private event metadata;
- causal notes intended for engine logic.

Allowed future player-safe consequences include:
- changed dialogue/choice availability;
- a visible reaction;
- a deliberately authored qualitative relationship cue;
- a known event summary explicitly revealed by game design.

D-065 must test that the durable memory can affect later authoritative behavior without the memory object itself crossing the bridge.

## 13. Goal privacy boundary

Current goal records contain:
- goal ID;
- priority;
- progress;
- status;
- source;
- timestamps;
- data.

These remain engine-private by default.

Android must not receive:
- exact hidden priority;
- exact private progress;
- private goal data;
- hidden goal source.

A future player-safe goal consequence must be separately authored, not derived in Compose from raw goal records.

## 14. Story-state boundary

NPC `story_state` is authoritative durable branching state.

The UI may consume only consequences deliberately projected through:
- visible scene/choice changes;
- room/actor projection under D-064;
- other explicit safe DTOs.

Do not add raw NPC story-state maps to `GameSnapshot`.

## 15. Player-safe social projection design

D-062 does not require immediate Android social UI implementation.

When a social projection is implemented, use an explicit root such as:

```text
social
  actors[]
  relationship_cues[]
  recent_visible_events[]
```

or an equivalent accepted DTO.

Minimum rule:
the projection contains only values already approved for player visibility.

Potential safe fields:
- stable actor reference when the player is allowed to identify the actor;
- known display label;
- visible role/faction;
- presence/interactability;
- deliberately exposed qualitative relationship cue;
- deliberately exposed recent relationship delta;
- explicitly communicated fact/claim.

Forbidden raw fields:
- `state.npcs`;
- exact personality axis map;
- exact hidden goal priority/progress;
- full memory list;
- full NPC knowledge map;
- secrecy;
- hidden truth relation;
- hidden story-state track map;
- AI utility/decision state.

D-064 room/actor projection remains a separate task and should not be implemented by D-062.

## 16. Android mapping boundary

Current Python bridge has no social root.

Current Kotlin `GameSnapshot` has no general social/NPC-private DTO.

Migration order when social presentation is later needed:
1. Python builds explicit player-safe social/actor projection;
2. Python tests redaction and semantic content;
3. Kotlin adds strict DTOs for only the approved fields;
4. mapper rejects malformed types/enums;
5. ViewModel stores projection as presentation state only;
6. Compose renders it;
7. no Compose rule determines social truth or mutates authoritative state directly.

Do not add generic `Map<String, Any?>` passthrough for raw social state.

## 17. Save migration contract

The first implementation should keep schema v1.

Required save tests:
1. old save without explicit memory still loads;
2. new save with Tamsin memory round-trips;
3. current relationships round-trip unchanged;
4. current player knowledge round-trips unchanged;
5. current NPC knowledge round-trips unchanged;
6. Tamsin goal/story-state round-trip unchanged;
7. party membership round-trips;
8. malformed nested social container is rejected before gameplay use;
9. unknown top-level save fields remain rejected;
10. unsupported schema versions remain rejected.

If implementation introduces stricter nested validation, it must distinguish:
- valid old minimal NPC shells;
- malformed records;
- optional new metadata.

Backward-compatible absence must not be mistaken for corruption.

## 18. Validation migration

### Content validation

Continue validating stable references for:
- NPC IDs;
- knowledge IDs;
- goal IDs;
- relationship axes;
- story-track transitions.

Add validation for `npc_memory_add` if adopted:
- non-empty NPC ID;
- non-empty memory ID;
- importance integer 1..5;
- tags iterable/list of non-empty strings;
- data object when present.

If `npc_learn` gains optional `truth` / `secrecy` authored fields:
- confidence finite 0..1;
- truth non-empty supported text/value;
- secrecy integer 0..5.

### Runtime validation

Do not rely on content validation alone.

Runtime social APIs remain responsible for rejecting malformed dynamic state.

## 19. Tamsin Phase 1 implementation path

D-065 should use the existing Tamsin route rather than author a new recurring NPC.

Recommended bounded proof:

1. start from current `NPC_TAMSIN` relationship and runtime shell;
2. choose one existing opening interaction to create one explicit durable memory;
3. preserve existing relationship/knowledge/story/goal consequences;
4. add one later authored condition/reaction that checks the durable consequence through engine logic;
5. save;
6. load;
7. verify the later reaction still occurs;
8. verify the private memory record is not present in player-safe bridge payload;
9. verify the allowed visible consequence still is.

The reaction may use:
- explicit memory query;
- or a dedicated derived story/social consequence created from that memory.

Do not make Compose inspect memory IDs.

## 20. Query API requirement for memory-reactive content

D-065 needs a read-only memory query.

Do not write conditions directly against raw list indices.

Recommended API:

```python
npc_remembers(
    state,
    npc_id,
    memory_id=None,
    tags=(),
) -> bool
```

Requirements:
- no state creation;
- no mutation;
- deterministic;
- validates existing NPC/memory structure;
- supports exact semantic memory checks;
- future-compatible with normalized metadata.

If content needs memory gating, add a semantic condition such as `npc_remembers` only after the query API and validator exist.

## 21. Mutation API matrix

| Domain operation | Current durable owner | Current mutation path | Migration decision |
| --- | --- | --- | --- |
| player knowledge | `state.knowledge` | core `learn` effect | keep owner; preserve player-safe semantics |
| NPC knowledge | `state.npcs[id].knowledge` | direct core effect + `social.npc_learn` | route content effect through `npc_learn` |
| relationship | `state.relationships[id]` | direct core effect + `adjust_relationship` | route content effect through `adjust_relationship` |
| memory | `state.npcs[id].memories` | `add_memory` API only | add semantic authored effect/query for Phase 1 |
| goal | `state.npcs[id].goals` | `set_goal` / `update_goal_progress` | keep |
| story state | `state.npcs[id].story_state` | `transition_story_state` | keep |
| personality | `state.npcs[id].personality` | direct content effect exists | do not expand; harden separately if future mutation needed |
| party | `state.party` | core party effects | keep; social state may react but does not own party |
| identity | authored `characters[id]` | content registry | keep content-owned |
| player-safe social view | none today | none | future explicit projection only |

## 22. File-by-file implementation order

### Stage A — social API convergence
Files:
- `src/textrpg/core.py`;
- `src/textrpg/social.py`;
- `tests/test_social.py`;
- focused core/content regression tests.

Work:
1. route `relationship` content effects through `adjust_relationship`;
2. route `npc_learn` content effects through `npc_learn`;
3. preserve current authored output and Tamsin branch behavior;
4. verify choice-level rollback remains intact.

### Stage B — explicit memory effect/query
Files:
- `src/textrpg/social.py`;
- `src/textrpg/validation.py`;
- `src/textrpg/core.py`;
- `tests/test_social.py`;
- `tests/test_validation.py`.

Work:
1. add read-only memory query;
2. add semantic content effect if required by D-065;
3. add semantic memory condition only if later content uses it;
4. validate malformed memory records/effects.

### Stage C — Tamsin content proof
Files:
- `content/vertical_slice_01.json`;
- social/content tests;
- Phase 1 proof documentation.

Work:
1. add exactly one bounded durable memory path;
2. add one later authoritative reaction;
3. keep current IDs/relationship/knowledge/story behavior.

### Stage D — save/load proof
Files:
- `tests/test_persistence.py`;
- relevant vertical-slice/save-resume tests.

Work:
- prove old/new nested social state round-trips without schema bump.

### Stage E — player-safe projection
Only when required by the accepted implementation slice.

Files may include:
- `src/textrpg/android_bridge.py`;
- Python bridge tests;
- `GameEngine.kt`;
- mapper tests;
- later Compose consumers.

Work:
- project consequences, not private containers.

D-064 remains the owner of room/actor projection.

## 23. Required regression tests

### Social API
- current seven-axis relationship behavior preserved;
- invalid relationship axis rejected before mutation;
- relationship history source recorded;
- NPC knowledge metadata bounds enforced;
- speaker-must-know sharing preserved;
- leak eligibility remains deterministic and read-only;
- multi-recipient leak rollback preserved;
- goal identity/progress behavior preserved;
- illegal story transition rejected without shell creation.

### Content integration
- Tamsin starting relationship exact;
- recovery gate trust >= 10 and suspicion <= 40;
- recovery trust +2;
- direct disclosure trust +3;
- secret route suspicion +4;
- known-route invite trust +1;
- `npc_knows` / `npc_not_knows` branch equivalence;
- current goal creation/progress values;
- current legal story transitions;
- party join/stay divergence.

### Memory proof
- chosen memory written once according to explicit duplicate policy;
- read-only query does not create state;
- later content reacts;
- save/load preserves memory;
- invalid memory payload rolls back the whole choice;
- memory remains absent from player-safe bridge payload.

### Privacy
- full NPC knowledge map absent from Android projection;
- full memory list absent;
- goal priority/progress absent unless explicitly designed for exposure;
- raw personality axes absent;
- raw story-state map absent;
- permitted visible consequence survives projection.

## 24. Rollback boundary

Before implementation:
- preserve current `core.py` content-effect behavior behind tests;
- capture Tamsin opening regression fixtures.

During implementation:
- change one effect family at a time;
- run focused tests after each change;
- do not combine D-064 actor projection changes with social mutation migration.

Safe rollback point:
- before adding the first new content memory/reaction, API convergence can be reverted independently.

After Tamsin content changes:
- rollback must restore both the new memory effect/condition and the authored content references together.

No save-schema migration is expected in the approved bounded path.

## 25. Interaction with D-064

D-062 defines social privacy/ownership.

D-064 owns:
- room/actor projection runtime;
- semantic placement;
- Python/Kotlin room-actor mapping;
- opening actor equivalence.

D-062 must not preempt D-064.

If D-064 exposes Tamsin as a room actor, it may consume only player-safe identity/presence fields and must not expose private social records.

## 26. Interaction with D-065

D-062 is the direct migration dependency for D-065.

D-065 may proceed after this packet is accepted because:
- durable state owner is defined;
- memory write/query path is defined;
- relationship/knowledge authority is defined;
- save boundary is defined;
- privacy projection boundary is defined;
- rollback/test order is defined.

D-065 still must implement and prove the actual memory-reactive behavior.

## 27. Interaction with persistent adversary work

V09 reuses the same NPC identity, memory, knowledge, goal, relationship, and privacy foundations.

The persistent-adversary packet may extend:
- `state.npcs[npc_id]["adversary"]`.

It must not:
- duplicate base NPC knowledge;
- duplicate general memory;
- duplicate relationship state;
- expose private adversary/social state through Android.

D-062 therefore remains the base social migration authority beneath V09.

## 28. Explicit non-goals

This packet does not:
- implement runtime changes;
- add final schedules;
- add factions;
- add social reputation;
- add hostility/rivalry axes;
- select a canonical recurring enemy;
- implement room/actor projection;
- implement tactical companion AI;
- redesign Android UI;
- expose raw NPC state;
- change save schema;
- promote proposal-only world/canon decisions.

## 29. Acceptance checklist

D-062 documentation acceptance is met when this packet establishes:

- [x] stable social state owners;
- [x] identity/runtime separation;
- [x] current relationship axes preservation;
- [x] player/NPC knowledge separation;
- [x] explicit memory migration path;
- [x] goals/story-state ownership;
- [x] authoritative mutation convergence plan;
- [x] save schema and migration boundary;
- [x] Android/player-safe redaction boundary;
- [x] Tamsin-compatible Phase 1 path;
- [x] rollback boundary;
- [x] exact implementation order;
- [x] required regression/privacy tests;
- [x] D-064 collision boundary;
- [x] D-065 dependency handoff.

Implementation evidence remains separate and must not be inferred from this document.

## 30. Next implementation action

After D-062 closes, the direct social Phase 1 implementation task is D-065.

Before changing runtime:
1. fetch live HEAD;
2. verify D-062 packet remains current;
3. verify D-064 ownership before touching room/actor projection;
4. implement API convergence and focused tests first;
5. add one explicit Tamsin memory and one later reaction;
6. prove save/load and privacy;
7. update Phase 1 evidence.

Do not broaden the first implementation into a complete social simulator.

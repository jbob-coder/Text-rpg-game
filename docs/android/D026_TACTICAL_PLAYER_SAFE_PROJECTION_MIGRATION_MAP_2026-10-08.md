# D-026 — Tactical player-safe projection / Android migration map

Status: **P8 WAVE-2 DOCUMENTATION DELIVERABLE / CURRENT SOURCE + FUTURE CONTRACT SEPARATED / NOT RUNTIME IMPLEMENTATION**  
Owner: **Kestrel** (canonical Player-AI PLAYER_KESTREL)  
Claim: **P8 / D-026**, Bulletin CLAIM_HEAD `35546e6c8cd524d213cdb4d75be35a15f4a5ce94`  
Inspected source authority: `docs/master-game-development-program@7390ea5320b08afcadd110d10c108d9f23935584`  
Parent authority: [Android Consumer & Projection Map](ANDROID_CONSUMER_AND_PROJECTION_MAP.md), Master Register D-026, Bulletin P8.  
Related: [Phase 1 combat migration packet](../systems/PHASE_1_COMBAT_SCHEMA_API_MIGRATION_PACKET.md), [Gate Twelve encounter packet](../systems/GATE_TWELVE_PHASE1_TACTICAL_ENCOUNTER_PACKET.md), [LOS/knowledge standard](../systems/LOS_DETECTION_AND_COMBAT_KNOWLEDGE_STANDARD.md), [Camera/tactical presentation standard](../systems/CAMERA_AND_TACTICAL_PRESENTATION_STANDARD.md), [Overseer rulings](../PROJECT_OVERSEER_DECISION_LOG.md) OR-010, OR-015, OR-034 and OR-035.

## 1. Purpose, authority, and status language

This is the bounded D-026 *migration map* that future D-073 (Python content/bridge) and D-074 (Android tactical UI) implement and verify. It maps **producers, allowed player-safe fields, action ownership, existing consumers, proposed types, and executable acceptance paths**. It does not create a new gameplay API, canon content, save field, visual asset, or task authority.

Definitions throughout:

- **EXISTS @ inspected HEAD**: actual source API or test; does not assert its integration into the Android bridge.
- **APPROVED DIRECTION**: accepted contract/ruling, not executed source.
- **D-073 TO DEFINE/PROVE**: bridge projection, action dispatch, content binding and redaction that do not yet exist.
- **D-074 TO IMPLEMENT/PROVE**: Kotlin DTO/mapper, action delegation, Compose/UI, JVM and instrumentation evidence, gated on D-073 DONE.
- **PROVISIONAL_INTEGRATION**: OR-034 permits a bounded non-canonical Gate Twelve fixture for D-073 **after D-072 DONE**. Fixture IDs/actions never silently turn into canon.

OR-035 explicitly authorizes this *documentation-only P8 lane* while D-072 remains Silex's IN_PROGRESS implementation. No D-073/D-074 primary ownership transfers to P8.

## 2. Grounded producer -> consumer path and file owner matrix

| Stage / file | Existing responsibility (EXISTS) | Future consumer / migration boundary |
| --- | --- | --- |
| `src/textrpg/combat_schema.py`, `combat_grid.py`, `combat_state.py` | Tactical map cells/coordinates, occupancy/LOS/path geometry and transient `CombatSession`/turns; not Android DTOs | Python keeps authoritative cells, movement legality, action budgets and deterministic events; no raw `CombatSession` serialization |
| `src/textrpg/combat_knowledge.py::CombatKnowledge.player_view` | Observer-filtered `round`, `action_budget`, `contacts`, `visible_cells`, token-safe `initiative`, `active_contact` | D-073 may adapt **these allowlisted outputs**, not its private `session.actors`/contact map |
| `src/textrpg/combat_rules.py::EncounterRules.player_view` | Wraps knowledge view with controller-owned `objectives` and `encounter_status` | D-073 must verify viewer/controller binding and supply any further player-safe command options |
| `src/textrpg/android_bridge.py::AndroidGameSession._view_for` | Currently returns `scene/status/inventory/quests/map/room/visuals/meta`; **no `combat` domain or combat methods** | D-073 adds optional `combat` projection and explicit commands only under its claim and engine transaction boundary |
| `android/app/src/main/java/com/thegame/rpg/engine/PythonGameEngine.kt` | `PythonSessionGateway` invokes approved Python session methods and maps snapshots; today no tactical gateway methods | D-074 extends narrow gateway / `GameEngine` calls only after D-073 methods/parameters are accepted |
| `android/app/src/main/java/com/thegame/rpg/engine/GameEngine.kt` | `GameSnapshot`, typed room/status/etc DTOs, `BridgeSnapshotMapper.fromMap`; **no typed combat DTO** | D-074 adds nullable typed `CombatSnapshot` and strict mapper; retains older narrative snapshot compatibility |
| `android/app/src/main/java/com/thegame/rpg/GameViewModel.kt` | Existing `GameUiState` + suspend `GameEngine` request/result flow and busy/error state | D-074 delegates explicit tactical intents to engine; keeps only selection/busy/error in UI state |
| `android/app/src/main/java/com/thegame/rpg/ui/GameScreen.kt` and `TheGameRoot` | Current narrative `PixelGameShell`; **no tactical mode** | D-074 contextual tactical surface only when projected combat exists, with accessible selection and server-authoritative legal actions |
| `docs/assets/PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md` + OR-010 | Static room `placement_key` is presentation-slot mapping, not simulation coordinate | Tactical grid cells use approved public tactical coordinates and a **separate** rendering adapter; do not reuse room actor placement slots as world truth |

Legacy root snapshot `meta.schema_version` denotes save/state compatibility; it is **not** the tactical projection version. OR-015 calls for additive `meta.projection_versions` without root-payload rewrite or schema-v1 save migration.

## 3. Exact EXISTING D-071 player-safe source contract

`CombatKnowledge.player_view(observer_id)` returns:

| Python key (exists) | Shape/source | Player-safe constraint / planned typed interpretation |
| --- | --- | --- |
| `round` | `CombatSession.round_index` integer | Project as non-negative integer; not a clock or world time |
| `action_budget` | observer's transient budget | Numeric budget of **authorized observer** only; display, never recompute in UI |
| `contacts[]` | `contact_id`, `awareness` | Public contact tokens (e.g. CONTACT_n), **not** raw actor IDs; documented awareness states include `DETECTED`, `IDENTIFIED`, `SUSPECTED` |
| `contacts[].coord` | present only on currently detected/identified contacts | Tactical coord key, e.g. `x,y,z`; expose only when current detection is valid |
| `contacts[].last_known_coord`, `last_seen_round` | on suspected/stale contacts | Historical public coordinate only. Never refresh from hidden current actor movement |
| `contacts[].identity` | allowlisted `KnownIdentity`, when supplied | Optional `name` and `faction` only after knowledge authorization; no inferred faction from actor ID |
| `visible_cells[]` | observer LOS-filtered public coord keys | Cell visibility is not actor detection or identification |
| `initiative[]`, `active_contact` | filtered token map (`SELF` or detected contact tokens) | No unknown roster/hidden actor count via turn order; absent active contact remains nullable |
| `objectives[]`, `encounter_status` | `EncounterRules.player_view` additions | Own-controller objectives: `objective_id`, `kind`, `status`; result from authoritative rules, not locally derived |

This is **not yet** the final D-073 `combat` JSON schema: encounter title/ID, legal action options, exits, public known cover/hazards, path previews and combat-log summaries are not all present in this exact view. D-073 must author, version and prove their semantics. The production wrapper must not simply `deepcopy(session.__dict__)` or serialize transient event/history internals.

## 4. Proposed D-073 -> D-074 field and producer matrix

Names in this table for **new bridge fields are proposed migration labels**, not implemented exact API keys. D-073 owns the final approved JSON field names. D-074 must bind its typed DTO to the actual accepted D-073 packet.

| Player-facing need | Authority / producer | D-073 projection gate | D-074 typed/UI consumer and test |
| --- | --- | --- | --- |
| `encounter_id/title` | validated D-073 authored fixture, `CombatSession.encounter_id` | Explicit `PROVISIONAL_INTEGRATION` provenance; no permanent enemy identity | `CombatSnapshot` header; verify title/id are allowlisted, not raw content internals |
| `round / action_budget / encounter_status` | knowledge + rules public view | Reuse exact source values; validate range/terminal lifecycle | Typed integers/enums; no Kotlin turn arithmetic |
| `active_contact / initiative[]` | `CombatKnowledge.player_view` | Only `SELF` and currently detected public tokens | Turn indicator; hidden actor absent from text, order and semantics tree |
| `visible_cells[] / known_cells[]` | knowledge + filtered tactical map | Separate visible-now from previously-known when supported; never treat LOS as detection | `CombatCellView` map; camera pan/zoom may be local; visibility never reveals actor silhouettes |
| `contacts[] / visible_actors[]` | observer contact view and explicit known identity | Tokens, awareness, coord versus stale last_known; optional identity | `CombatActorView` typed public projection; no raw participant ID, private faction or AI profile |
| `cover/hazards` | grid geometry evaluated through player knowledge | Only actually known public cover/hazard facts; preserve no-information state for unseen cells | `CombatCellView`; draw only known cues, do not inspect raw map |
| `legal_move_cells / path_preview` | `CombatKnowledge.preview_movement` and authoritative rules | Only approved visible/known preview; no hidden occupancy leak from solver feedback | Highlight/selection, no Compose pathfinding or authoritative legality calculation |
| `legal_actions / target_options` | `CombatSession` + `EncounterRules` validation & knowledge | Explicit public action IDs/arguments with safe options; no unknown authored action rules | `CombatActionView`; call back exact ID/target, do not derive hit/damage |
| `objectives/exits / retreat` | `EncounterRules` objective and retreat methods | Public objective/exit availability; no secret branches or private AI retreat threshold | Typed objective/exits; actionable retreat only on authorized bridge command |
| `companion_order_options` | existing D-071 AI/order constraints | Only actual controllable, available, player-known companion orders | Typed order view; no raw NPC goals, personality or alternate AI plan |
| `visible_conditions` | Python transient combat + approved player status | Projection whitelist; never assume proposed leg-injury ID is canon | Visible condition labels; no private NPC injury payload |
| `combat_log[]` | event owner + knowledge-filtered formatter (D-073 must create) | **New safe summary only**, not raw committed tactical event log | `CombatLogEntryView` display and accessible narration, hidden contacts omitted |
| `aftermath` | Silex D-072 authoritative GameState transaction; D-073 adapter | Only committed public result, not private effects; rollback/no result on failed commit | Existing narrative/status/quest refresh plus scoped encounter result, no UI durable mutation |

### Projection envelope/version migration decision (OR-015)

- **Legacy narrative packet:** no `combat`, no `meta.projection_versions`; map as today with nullable combat absent. Existing `GameSnapshot` consumers must still work.
- **New tactical packet:** D-073 supplies explicit optional `combat` and additive domain-version manifest, conceptually `meta.projection_versions.combat = 1`; D-074 accepts only declared supported version when combat is present.
- **Unsupported/ill-typed required version:** reject entire tactical mapping through a stable **public projection error**, not partial UI, fallback to raw nested `Map`, or an attempt to infer version.
- **Malformed/private nested combat keys:** fail closed at typed boundary using an allowlist once D-073 seals the schema. Reject duplicate contact tokens, impossible awareness/coordinate shapes and mismatched references.
- **No hidden empty-domain policy loophole:** absent combat is legacy-compatible; **present** combat without required supported version is not silently treated as legacy.
- **No save migration:** the manifest is presentation compatibility, not new durable GameState ownership; D-073 controls interruption/rollback policy.

The actual wire schema/enum values remain a D-073 acceptance decision. D-026 intentionally cannot pretend version `1`, exact new field names, or error codes are already shipped.

## 5. Explicit action migration / authority graph

Existing action path: `TheGameRoot` -> `GameViewModel.choose/save/load/travel/...` -> `GameEngine` -> `PythonGameEngine` -> `PythonSessionGateway` -> `AndroidGameSession` -> Python rules -> player-safe `_view_for`.

Recommended **future** D-073 entry points in the approved migration packet, with D-074 mirrored callbacks:

| Future Android event | Future Python session route | Authoritative validation | Required UI reaction |
| --- | --- | --- | --- |
| `startCombat(encounterId)` | `start_combat(encounter_id)` | Authored location/trigger/fixture and pre-combat checkpoint | Busy -> updated safe snapshot or stable error; never assume combat started on request |
| `moveCombatActor(path)` | `combat_move(path)` | Current controller/turn/budget/movement/occupancy recheck | Replace safe snapshot; path preview cannot guarantee commit |
| `useCombatAction(actionId,target)` | `combat_action(action_id,target)` | Rules/action target/LOS/knowledge/cost/hit from Python | Display only returned public result; no Kotlin damage/cover math |
| `endCombatActivation()` | `combat_end_activation()` | D-070 turns/activation and D-071 decisions | Render returned state; don't locally increment round |
| `issueCompanionOrder(npcId,order,target?)` | `combat_companion_order(npc_id,order,target?)` | Authorized companion, known target, actual legal order | Display resulting public order; do not expose private goals |
| `retreatCombat()` | `combat_retreat()` | D-071 legal exit/objective/departure and D-072 commit boundary | Show accepted outcome; no local world consequence |
| `restartCombat()` | `combat_restart()` | Pre-combat restore policy and no tactical save-v1 leakage | Return authoritative narrative-safe snapshot |

These are **approved migration recommendations**, not callable current endpoints. D-073 final method signatures and legal path encoding must be consumed unchanged by D-074. No `setCombatState` or arbitrary state-mutation endpoint.

Presentation-only local state: selected public cell/contact, bounded pan/zoom, highlighting, narration focus, accessibility preference, pending/busy/error. Server-owned: active actor, initiative, legal moves, costs, hit/cover/damage, detection, objectives, aftermath, world time and persistent data.

## 6. Tactical visual and provisional-content boundary

The camera design calls for fixed-orientation higher three-quarter orthographic combat, square cells, bounded pan/zoom, readable cover and tap-first phone controls. Rendering projection cells into pixels is Android **presentation**, never a second grid/movement engine. Static room-actor `placement_key` cannot be repurposed as combat world position (OR-010).

Under OR-034, `CONTACT_SERVICE_FORK_A/B` may exist as encounter-local fixture participants but are **not** named permanent NPCs or canon enemies. Provisional markers in tests do not certify final sprite identity or canonical encounter art. Character art remains governed by the pixel composition standard's authored-character requirement; no permanent opponent art before canon approval.

## 7. Test/validation and merge gate for future consumers

| Test owner / file path | Required proof (future, NOT executed by D-026) |
| --- | --- |
| Python `tests/test_combat_knowledge.py`, `tests/test_combat_objectives.py`, `tests/test_combat_ai.py` | Reuse existing D-071 identity/stale-contact/knowledge/objective/AI traps; none is by itself a bridge test |
| D-073 new bridge-focused Python test (path **TBD by claimant**) | Only allowlisted public `combat` fields; hidden contact absent from actors, initiative, targets, paths, logs, status; unknown actor ID versus hidden ID gives same public rejection; no accidental memory/condition leakage |
| D-073 fixture/save regression (path **TBD**) | Pre-combat checkpoint; app interruption/restart from pre-combat state; no schema-v1 mid-combat save; committed aftermath visible only after authoritative transaction, with rollbacks on failure |
| Kotlin `android/app/src/test/java/com/thegame/rpg/engine/` (new D-074 test file) | Missing/legacy combat maps; supported version maps typed DTO; absent-required/unknown version fails; malformed type/range/coordinate/token/reference/private extra fields fail; no raw maps reach UI |
| Kotlin `PythonGameEngineContractTest.kt` or scoped new gateway test | Request parameters forwarded **exactly once** with no derived gameplay result; busy/failure/error conversion never smuggles technical private data |
| ViewModel unit test (new D-074 test file) | Success publishes returned snapshot; failure retains safe prior state and clears busy flag; duplicate requests prevented; save/restart policy reflected correctly |
| Compose instrumentation `android/app/src/androidTest/java/com/thegame/rpg/ui/GameScreenTest.kt` or scoped new suite | Hidden contact absent from pixels, overlay labels and accessibility semantics; detected/last-known states distinct; focus, large text and reduced-motion guards; no hidden roster/target feedback |
| Presentation screenshot/emulator evidence | 320dp/low-end-safe layout, selection and touch interactions; screenshot cannot stand in for redaction test or physical-phone validation |
| Merge-state CI | Use existing `.github/workflows/android-pixel-client.yml` PR integration gate for runtime D-073/D-074; task-local green alone insufficient |

Commands to run **when consumer code exists** (none run for this documentation-only lane):

```sh
PYTHONPATH=src python -m unittest discover -s tests -v
gradle -p android testDebugUnitTest --stacktrace
gradle -p android :app:assembleDebugAndroidTest --stacktrace
gradle -p android :app:assembleDebug --stacktrace
```

Physical-device acceptance must be separately observed; emulator checks are not phone checks. No synthetic successful test evidence is claimed by this document.

## 8. Execution order and acceptance handoff

1. D-072 Silex: finish durable aftermath with exact-head proof and repository handoff. P8 does not implement or inspect uncommitted branch work as authority.
2. D-073: claim after Bulletin READY, materialize OR-034 fixture and approved content schema; define exact player-safe `combat` wire format/manifest/action signatures; run hidden-contact and interruption tests. This document must be amended to match **actual D-073 API**, not vice versa.
3. D-074: claim after D-073 DONE; add typed Kotlin DTOs, strict mapper/version handling, thin gateway and ViewModel delegation, minimal tactical Compose, accessibility/visibility regression and Android CI evidence.
4. D-076/D-077: consume verified cross-domain persistence and Android gap closure, not this planning map as proof.
5. Final canon/visual acceptance: separately authorize or replace the provisional opponents, knowledge, injuries and art if any are to ship as canon.

**D-026 P8 completion boundary:** this migration document is the planned file/field/action/test handoff and materially advances D-026; it does **not** complete all D-026 remaining projections (activity, hierarchical map, adversary, advanced status), D-073, D-074 or the final APK. Update Master Task Register and parent consumer map with a scoped pointer only; preserve the larger D-026 `IN_PROGRESS` status. P8 lane may be DONE when this packet, references, claim/evidence and required Learning/Coordination handoff are verified.

# P17 / D-026 — Persistent-adversary intel player-safe projection migration

**Status:** OR-037 Wave-4 P17 bounded documentation target; NOT an implemented domain, Android feature, canonical adversary or save migration.
**Player-AI:** Kestrel / PLAYER_KESTREL / SESSION_KESTREL_20261008T1752-0400_S02.
**Authority:** `docs/AI_TASK_BULLETIN_BOARD.md` P17, Master D-026, OR-037; source baseline `05c4a64f70cc33c191257f0761e5e93c62caf2d0` (recheck HEAD on any implementation).
**Parent:** [Android Consumer & Projection Map](ANDROID_CONSUMER_AND_PROJECTION_MAP.md).
**V09 authorities:** [Persistent-adversary master](../systems/PERSISTENT_ADVERSARY_WORLD_MEMORY_MASTER_PLAN.md), [schema/API migration](../systems/PERSISTENT_ADVERSARY_SCHEMA_API_MIGRATION_PACKET.md), [player-safe intel](../systems/ADVERSARY_PLAYER_SAFE_INTEL_STANDARD.md), [Gate Twelve future proof](../systems/GATE_TWELVE_ADVERSARY_PROOF_PACKET.md).
**Adjacent:** [Tactical migration](D026_TACTICAL_PLAYER_SAFE_PROJECTION_MIGRATION_MAP_2026-10-08.md); [hierarchical-map migration](P13_D026_HIERARCHICAL_WORLD_MAP_PROJECTION_MIGRATION_2026-10-08.md).

## 1. Current / target / proposal — enforce the distinction

| Layer | CURRENT source evidence | TARGET / NOT IMPLEMENTED |
| --- | --- | --- |
| Durable data | `src/textrpg/core.py::GameState` includes `npcs`, `knowledge`, `relationships`, `history`; `src/textrpg/social.py::ensure_npc`, `add_memory`, `npc_learn`, `share_knowledge` and other social operations own ordinary NPC memory/knowledge. | V09 migration packet proposes a nested `state.npcs[npc_id]["adversary"]` record with eligibility, lifecycle, encounter references, adaptations, recurrence, routing, hierarchy and removal; it does not exist as approved production behavior. |
| Persistence | `src/textrpg/persistence.py` uses existing save schema v1 and a strict existing top-level GameState boundary. | Dedicated V09 nested-record validation, old-save compatibility, round-trip, rollback and migration tests must precede a live V09 data owner. A new top-level `adversaries` owner is NOT authorized. |
| Python bridge | `src/textrpg/android_bridge.py::AndroidGameSession._view_for` returns `scene`, `status`, `inventory`, `quests`, `map`, `room`, `visuals`, `meta`; there is no `adversary_intel` field or V09 action method. | A future Python observer-filtered `adversary_intel` domain, only when the V09 owner exists, is proposed by the V09 migration packet. Do NOT serialize the nested NPC/adversary record. |
| Kotlin gateway and DTO | `android/app/src/main/java/com/thegame/rpg/engine/GameEngine.kt` contains the current typed `GameSnapshot` (21 fields), no adversary DTO or inspect/investigate-adversary methods; `PythonGameEngine.kt::PythonSessionGateway` has no V09 action. | Add a typed optional `AdversaryIntelSnapshot` consumer only after a real Python payload/version is accepted. Do not pass raw nested map objects to Compose. |
| ViewModel / UI | `GameViewModel.kt` delegates established player actions; `GameScreen.kt` currently has Story/Quests/Map and room/tactical-independent presentation, not adversary-intel screens. | A knowledge-gated journal/contact detail or map rumor marker may reuse current surfaces; D-049 owns final UX placement. No compulsory hierarchy/rival screen. |
| Gate Twelve | `GATE_TWELVE_ADVERSARY_PROOF_PACKET.md` is PROPOSED and not Phase 1 required. Encounter contacts are not canonical persistent NPCs. | One surviving contact is only a future eligibility *candidate*, never an auto-promoted adversary. OR-034 provisional D-073 contact identifiers must remain encounter-local. |

No existing V09 test suite, live `adversary_intel` wire format, persistent enemy roster, or V09 UI behavior is established by this P17 document. The V09 master and its approved migration design remain future work.

## 2. Authority graph and discovery gate

Authoritative first implementation sequence from V09: eligible world actor -> meaningful encounter -> committed aftermath -> perceptible memory and knowledge -> bounded adaptation and lifecycle -> routing/recurrence evaluation -> observer-safe intel. `GameState.npcs` retains identity, social and memory owner; V09 adds nested *adversary-specific* records only. World owner validates place and route IDs; faction owner validates rank/role; combat owns transient combatants and perception; the player-side knowledge source controls what can be disclosed.

A public intel record requires: (1) a legitimate player-visible evidence/knowledge source, (2) disclosure permission for each field, (3) a safe public contact token, (4) confidence/freshness classification when relevant. A raw stable `npc_id`, adversary eligibility record or gameplay fact is not itself disclosure evidence. Do not use private NPC memories as a substitute for the player's knowledge. Sorting or filtering must not indirectly reveal hidden actor counts, future routes, or factions.

## 3. Proposed public wire and Kotlin DTO — NOT CURRENT API

Following `ADVERSARY_PLAYER_SAFE_INTEL_STANDARD.md` and `PERSISTENT_ADVERSARY_SCHEMA_API_MIGRATION_PACKET.md` §18, a possible *optional* domain is `adversary_intel`. Proposed type names/JSON keys below are migration guidance, not an approved existing schema. The Python producer and Kotlin consumer must agree on the final wire contract before implementation.

| Proposed public field | Eligibility / producer | Kotlin/Compose boundary |
| --- | --- | --- |
| `contacts[].contact_id` | Stable **public** contact token issued after observer disclosure; never raw `npc_id` unless separately authorized | Nonempty unique typed reference, not a permission grant or guaranteed permanent identity. |
| `identity_level`, optional `display_name`, `alias` | V09 public-knowledge identity progression: unknown -> recognized -> alias/role -> identified | Controlled finite states; unknown never gets secret name, fallback art, faction, or revealing ID. |
| `known_faction`, `known_role` | Individually observed, learned or published public facts | Optional public labels; no private membership, rank succession or guessing from internal ID. |
| `last_known_location` with `knowledge_time`, `freshness`, `confidence` | Direct observation, informed testimony, authored record or rumor with source; distinct from hidden current location | Show "last known", "reported", "stale" or "confirmed" explicitly. Do not refresh on unseen movement. Do not imply live tracking. |
| `last_encounter_summary` | Public *knowledge-filtered* encounter/aftermath summary | No raw tactical event log, hidden contact identities, unseen actions or private damage. |
| `observed_injuries`, `observed_equipment`, `observed_techniques` | Only seen or authoritatively learned, each item with evidence | No private severity, recovery countdown, unknown item IDs or hidden abilities. |
| `known_behavior` / `rumors` | Bounded observed tactic, testimony and rumor sources | Clearly attribute reliability; never claim an internal adaptation reason as player knowledge. |
| `known_status` | Learned captured/dead/retired etc., not current hidden lifecycle truth | Distinguish *known or reported* from actual internal lifecycle; stale status remains stale. |
| `visual_id` / `silhouette_key` (optional) | Only a known, provenance-approved presentation asset | No art-based identity leak or new permanent sprite for OR-034 fixture contacts. |
| `source_label`, `confidence` | Approved visibility-safe evidence only | Strip internal source IDs and NPC-private publisher details if not independently public. |

**Proposed typed families:** `AdversaryIntelSnapshot(contacts)`, `PublicAdversaryContact`, `KnownIdentityLevel`, `IntelEvidenceLabel`, `PublicLastKnownLocation`. A public contact may exist with an unknown display identity; no fake actor profile is required.

**Denylist — never pass through:** `state.npcs` raw records; private `memories`, `knowledge`, `personality`, `goals`, `story_state`; V09 `eligibility`, `adaptations`, `recurrence`, `routing_refs`, `hierarchy_refs`, unpublished `lifecycle`, internal `encounter_refs`; hidden current coordinate/location, private faction orders, undiscovered combat abilities, AI utility/weights, cooldowns, adaptation candidates, succession candidates, unknown actor counts and identities. If a value is separately learned, project an explicitly sanitized public *fact*, never its internal owner container.

## 4. Additive version and legacy migration (OR-015)

Legacy narrative packets currently omit `adversary_intel` and `meta.projection_versions`: Kotlin must preserve existing `GameSnapshot`, Story, Quests, Map, navigation, save/load and current public mapping without constructing fake contacts or requiring a new domain. Existing `meta.schema_version` / persistence schema v1 is not a projection-domain version.

For a future nonempty `adversary_intel`, OR-015 calls for a separate additive domain version, conceptually `meta.projection_versions.adversary_intel = 1`. The key and version value are a **proposal**, not shipped values. Make a typed version allowlist, and reject any *present* adversary domain with absent, malformed or unsupported required version through a stable, nonsensitive public mapping error. A malformed contact array, duplicate public token, invalid identity/freshness enum, negative or impossible time, inconsistent field/disclosure state, or unexpected private field fails closed; do not silently discard secrets into Compose, mask as legacy, or return raw nested maps.

When mapping is rejected: no partial adversary cards, metadata/tooltips, labels, map markers, logs or accessibility nodes should leak the rejected content. Error messages must not encode hidden identity, actor count, factions or location. Maintain a last-known-good player-safe UI snapshot only under an explicit accepted consumer policy; do not present a malformed new packet as current verified intel. No save schema change is authorized here.

## 5. Future player action / UI graph

Current real path: `GameScreen`/Compose -> `GameViewModel` -> `GameEngine` -> `PythonGameEngine`/`PythonSessionGateway` -> `AndroidGameSession` -> authoritative Python domain -> `_view_for` -> typed Kotlin mapper -> Compose.

| User intent | FUTURE API / owner | Acceptance condition |
| --- | --- | --- |
| Open journal/contact details | If payload is wholly present, local selection of public `contact_id`; optional future `inspect_adversary_intel(contact_id)` from V09 migration packet | Python revalidates contact visibility on every query. Opening already-published detail has no world-time, relation, NPC-memory or recurrence mutation. |
| Investigate known intel | Optional future `investigate_adversary(contact_id, action_id)` via explicit authored engine choice | Python validates authored action, source knowledge, reachability, costs, time and consequences. UI shows server-confirmed safe result only. |
| Travel toward reported location | Existing `GameEngine.travel(locationId)` **only** for independently discovered and currently reachable public map nodes | Stale/rumored intel does not create routes, unlock areas, move actors or expose hidden edges. The world-map projection remains authoritative for travel affordance. |
| Engage contact in combat | Future D-073/D-074 combat adapter (when unlocked) | Combat tactical `CONTACT_n` token is **not automatically** the persistent V09 contact token; any link requires deliberate authorized identity proof. |
| Show visible changes / aftermath | Current Python authoritative story/quest/status projection; future V09 public update after committed transaction | No Android promotion, movement, adaptation, forced recurrence, injury arithmetic or private knowledge writes. |

Application-only selected contact, panel expansion, scroll, filter and tab are transient Compose/ViewModel state; the authoritative reveal status and evidence remain Python/world/knowledge-owned. On payload/version change, clear stale selection rather than dereference a hidden contact. Rich maps or illustrations may not draw a hidden current actor location merely because a sprite exists.

## 6. Test and accessibility acceptance matrix — FUTURE, NOT RUN

| Future test owner / existing source path | Required proof |
| --- | --- |
| `tests/test_social.py`; `src/textrpg/social.py` | NPC-private memory/knowledge never converts into player-side intel absent an explicit witnessed/reported/learned source; no mutation on read-only projection. |
| New V09 Python tests + `tests/test_persistence.py` | Nested validation, old schema-v1 save, round trip, no new top-level field, event provenance, no auto-promoted Gate Twelve contacts, rollback, old-save absent domain. |
| `tests/test_android_bridge.py`; `src/textrpg/android_bridge.py` | No V09 view today; future tests: allowlisted only, unknown identity/hidden location/adaptation/cooldown redaction, stale location not silently refreshed, known-vs-rumor distinctions, no secret error side channel. |
| `android/app/src/main/java/com/thegame/rpg/engine/GameEngine.kt`; `PythonGameEngine.kt` and new engine mapper tests | Absent old domain remains compatible; supported version typed mapping; present-without-version, unsupported version, malformed/duplicate/private nested fields rejected; no raw `Map` in `GameSnapshot` or Compose. |
| `android/app/src/main/java/com/thegame/rpg/GameViewModel.kt`; new ViewModel tests | UI selection/query does not mutate gameplay; known contact requests alone; busy/error replacement and visibility revocation; reject stale token with stable public error. |
| `android/app/src/main/java/com/thegame/rpg/ui/GameScreen.kt`, `android/app/src/androidTest/java/com/thegame/rpg/ui/GameScreenTest.kt` | Unknown identity silhouette/label only; testimony/stale intel explicitly labeled, no hidden location or counts in UI, resource strings, art, semantics, screenshots, narration, focus order or large-text/reduced-motion states. |
| Future V09 + D-073/D-074 integration | Observer mismatch and actor-to-public-contact token linkage cannot reveal private actor IDs, future path, hidden tactical contact, actual cooldown or AI adaptation. |
| Current-head CI + representative emulator / physical target separately | Run Python unit and Android unit tests; then integration/Compose instrumentation and merge-state CI. Emulator green is not device proof. No such tests were run by P17 documentation. |

The source paths listed here are implementation/test owners or extant test sources, **not passing evidence** for the future behavior. Final action names, public identity levels, projection wire keys, enum spellings, rendering surface and any schema change remain gated decisions of their domain owners.

## 7. Completion and non-overlap boundary

P17 is a **documentation-only migration contract** satisfying the Wave-4 player-safe intel field/version/privacy/action/test map. It does not implement V09, select a canonical persistent enemy, create a persistent encounter, finish Master D-026, or satisfy Phase 1 combat/Android performance/device acceptance.

Master D-026 remains IN_PROGRESS for activity, evolved status, APK destination components and runtime/merge-state evidence. Master V09/D-032 owns any future adversary state implementation. The ordinary NPC and world sources continue to own memory, knowledge, locations, factions and save; D-072 aftermath, D-073 tactical bridge, D-074 Android combat and other active Wave-4 lanes are unchanged.

**Next implementer shortcut:** before code, revalidate V09 migration §§17–20 against fresh source HEAD, confirm authored legitimate identity/knowledge evidence and a real consumer, approve exact domain-version and public IDs, implement a strict Python read-only observer projection with dedicated redaction tests, then typed Kotlin mapper, ViewModel/Compose UI, merge-state evidence and Android/phone gates. Keep this document future-facing until those proofs exist.

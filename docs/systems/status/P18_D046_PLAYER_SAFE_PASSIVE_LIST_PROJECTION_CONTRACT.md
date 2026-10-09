# P18 / D-046 — Player-Safe Passive-List Projection and Privacy Contract

**Status:** TARGET DESIGN CONTRACT / DOCUMENTATION-ONLY / NOT CANON / NOT IMPLEMENTED  
**Owner:** Veyr (`PLAYER_VEYR`), session `SESSION_VEYR_20261008T1747-0400_S02`  
**Task:** OR-037, Wave-4 P18/D-046, live Bulletin claim `2a6beeb9a6f12eb409c374202728a1e971b576c1`  
**Scope:** Phase-C-to-Phase-F migration definition for a future owned-and-revealed passive list; **no schema/DTO/runtime changes**. This contract consumes P14 rather than re-authoring social reputation.

## 1. Decision, priority, and non-goals

THE GAME requires a player-facing passive list, but **an authoritative owned passive, a discovered fact about one, and permission to display it are different decisions**. The future engine, not Android, must evaluate qualification, ownership, visibility, provenance, and authorized effect descriptions before producing a detached player-safe projection. Unknown passives, undiscovered unlock requirements, classified events, and NPC-private assertions do not become visible merely because they are stored or affect a visible numeric value.

This document defines projection responsibilities, fail-closed rules, consumer separation, proposed version/error behavior, migration limits, and later executable acceptance cases. It **does not** introduce `status.passives` into `build_status_view`, add a `GameState` field, edit Kotlin/Compose, award a passive, define progression thresholds, canonize `PASSIVE_SOC_0007` or `PASSIVE_SOC_0010`, or turn P14's design into a runtime publication service.

## 2. CURRENT / TARGET / UNRESOLVED source authority

| Concern | CURRENT, verified in repository | TARGET design | UNRESOLVED gate |
|---|---|---|---|
| Durable acquired effects | `GameState.perks` survives `snapshot`/save. `RulesEngine._apply_effects` supports bounded `add_perk`; `modifiers.perk_modifiers` composes validated additive paths. | Reuse that container **only** for its approved acquired/effect responsibilities; obtain more complex qualifications from their domain owners. | Complete passive-definition schema and safe old-save migration; no general 230-passive runtime exists. |
| Status owner | `src/textrpg/status.py::build_status_view` returns identity, attributes, resources, derived, skills, abilities and conditions, **not passives**. | A new *derived projection* for a particular viewer, computed from approved authoritative owners and knowledge/reveal rules. | Owner-approved implementation API and target serialization. |
| Hidden attribution | `inspect_status_value` emits a visible perk contribution where authorized; hidden IDs are aggregated as `unidentified_modifier`. `tests/test_status.py` contains visibility/save-resume regression assertions. | Preserve current math/redaction; list projection must not reverse the anonymization by matching effects to secret records. | A compatible non-leaky explanation contract for nonadditive domain effects. |
| Bridge | `AndroidGameSession._view_for` projects a fixed scene/status/inventory/quests/map/room/visuals/meta map. | Project an additive, strictly validated safe passive-view fragment; do not serialize `state.perks`, owner ledgers, or all passive definitions. | Independent domain-version policy, public error handling, backward compatibility. |
| Kotlin/UI | `docs/android/ANDROID_CONSUMER_AND_PROJECTION_MAP.md` reports no passive-list member of typed `GameSnapshot`; current mapper can understand **perk contribution kind**, not an owned passive catalog. | Python projection → strict mapper/DTO → `GameViewModel` immutable view → Compose read-only rendering. | Product-approved visual/interaction design and Kotlin acceptance suite. |
| Social source | P9/D-075 supplies a Tamsin-specific known branch precedent; P14 separates occurrence, NPC observation, publication, social-passive qualification, and disclosure. | A passive projection reads **authorized** qualification and reveal state without publishing NPC thoughts or inventing town-wide consensus. | No approved public publisher, `SOC` qualification ledger/effect API, replay identity or canon threshold. |

**Current source precedence:** exact runtime/source and exact test evidence first; `PASSIVE_RUNTIME_OWNER_PROJECTION_DISPOSITION_WAVE_001.md`, `STATUS_KNOWLEDGE_VISIBILITY_STANDARD.md`, `PASSIVE_STATE_OWNER_RESOLVER_MATRIX_WAVE_001.md`, P14 packet, and the current Android consumer map constrain proposed design.

## 3. Eligibility and visibility are independent

Four logical conditions must be distinguished even if future durable storage uses fewer objects:

1. **Existence:** target registry contains a proposed/passive definition. Not sufficient to display its ID, family, count, slot, or prerequisites.
2. **Qualification:** a relevant authoritative domain verifies authored evidence. Not sufficient to grant ownership or reveal. Source-specific qualification cannot be inferred from number of UI visits, saved history row counts, NPC rumor, or player actions unsupported by the approved record.
3. **Ownership:** an approved Status/ability transaction makes a passive available to the holder. Does **not** automatically confer public/institutional knowledge or all future stage details.
4. **Player reveal:** the engine proves that **this player viewer** has a permitted discovery/reveal. Only then does the passive become a list entry, with each field separately filtered.

**Phase-C default:** no visible passive-list entry before approved ownership **and** authorized reveal. A separately authored discovery of an unowned passive's *existence* may eventually have its own explicit player-knowledge presentation channel. That is **not** permission to display an unearned passive among acquired passives or show its exact unlock method. Whether such a channel should exist is undecided.

**Case distinctions:** owned but hidden → omitted; qualified but not owned → omitted; known rumor but never qualified → omitted; owned and revealed → allowlisted player-known fields only; owned and revealed with a later secret evolution → display acquired stage alone, not future stage metadata; classified/public label conflict → player's own view follows independently authorized self-knowledge, never an implied public dossier.

A player's *absence of visible passives* does not establish an empty `GameState.perks`, and an unrevealed mechanical modifier may still be part of authoritative math without revealing its source ID.

## 4. Proposed player-safe wire contract — NOT a live API

To make review concrete, the **candidate** extension is an additive, server-produced Status fragment `status.passives` with its own independent `projection_version` and `entries`. The wire names below are **proposals for future API approval**, not existing source fields or stable canonical IDs. `projection_version = 1` is a *suggested initial domain contract number*, not the save schema version.

| Candidate field | Release condition | Redaction policy |
|---|---|---|
| `projection_version` | Always for the **new domain** after version acceptance. | Type-checked exact supported integer; no fallback to latest or raw owner metadata. |
| `entries` | An array of already authorized visible acquired passives only; deterministic ordering by safe public ID. | **No hidden placeholder rows or undiscovered count**, empty array is allowed. |
| `id` | Stable *player-revealable* passive ID, approved by definition + viewer permission. | Unknown/classified IDs omitted; never publish unapproved internal identifier. |
| `name` | Verified display label authorized for this holder/viewer. | No registry fallback that expands hidden identity; unknown label blocks/omits entry according to accepted contract. |
| `family` | Optional coarse known family when source authorizes it. | No inferred classified family or internal owner/write-target domain. |
| `effect_summary` | Optional authored, player-known plain-language effect, not generated from raw modifiers. | No exact hidden coefficient, NPC private context, implementation path or unrevealed synergy. |
| `source_summary` | Optional public-safe provenance text only after dedicated viewer-visible source permission. | No private source actor/recipient, secret event ID, hidden qualification case, raw history, or institutional classified packet. |
| `revealed_stage` | Optional and **only** after an approved stage/stack/level mechanic and precise reveal policy. | No hidden next stage, percent progress, cooldown or threshold by default. |

Fields such as `is_owned`, `qualifier_progress`, `unknown_count`, `requirement_ids`, `raw_effects`, `modifier_map`, `owner_domain`, `unlock_case`, `npc_observer`, `private_truth`, and `internal_tags` are **not** part of this minimal wire model. A visible-list entry already implies authorized ownership; a redundant `is_owned` flag creates another possible contradiction.

The candidate minimal shape for one purely fictional, *noncanonical* example is:

```json
{
  "projection_version": 1,
  "entries": [
    {
      "id": "PERK_EXAMPLE_VISIBLE",
      "name": "Example Visible Perk",
      "effect_summary": "An authorized, player-known effect"
    }
  ]
}
```

This is an illustrative schema **only**; `PERK_EXAMPLE_VISIBLE` is not a real game content record and must not enter any canonical content registry. If no passives can lawfully be shown, the candidate domain is `{"projection_version":1,"entries":[]}`, **not** a list of secret locked slots.

## 5. Denylist and side-channel rules

The projection MUST NOT contain any of the following in any nested entry, diagnostic surface, error message, count, sort behavior, tooltip, or derived badge:

- an undiscovered passive name/ID/icon/slot, exact requirement, hidden method, threshold, event source or qualification percentage;
- private `state.perks` blobs; modifier maps, implementation paths, hidden `visible` flags, internal owner/ledger names, secret definitions, unapproved raw logs;
- NPC-specific `knowledge`, `memories`, `goals`, relationship axes, secrecy flags, rumor confidence/truth, actor identities learned only through NPC-private records;
- classified authorization material, unrevealed rarity, institutional dossiers, future evolution branches, redacted/mistaken world truths masquerading as facts;
- a total catalog size, hidden count, stable ordering positions for omitted records, or timing/size changes from invisible passives that create a client-observable enumeration oracle.

Current deep Status inspection of hidden modifiers remains anonymized. The future list must not enable correlation from visible `effect_summary` or stable internal indices to the hidden contributor. UI debugging/developer settings must use separate authorized surfaces, never silent injection into player snapshots.

## 6. Provenance and P14 social boundary

Future qualification/storage truth stays with the appropriate domain; the projection consumes a *detached approved view*. For non-social cases, an event owner supplies accepted evidence to Status acquisition and reveal gates; the UI never back-computes a qualifier from quests or stats. For social cases, consume P14's chain:

`authored occurrence → authorized observer knowledge → optional authorized public publication → approved passive qualification → independent player disclosure`.

Neither `NPC_TAMSIN` interaction nor `ASK_TAMSIN_ABOUT_SHARED_ENTRY` authorizes public reputation; neither `PASSIVE_SOC_0007` nor `PASSIVE_SOC_0010` is granted by this document. SOC_0010, if ever implemented, may recall **known** precedent, not reveal unlearned NPC goals or automatically publish rumors.

Source provenance shown to the player is a deliberately authored explanation, *not* a serialized receipt from internal domain ledgers. Redaction also applies to error text and any future inspect-passive endpoint. Replayed UI loads or duplicated requests must not alter acquisition, truth, public standing or a passive qualifier.

## 7. Version negotiation, error boundary, migration

- **Independent domain version:** an explicit future passive-view version is separate from `GameState.schema_version` and existing room/other domain versions. Once approved, it must be validated on Python producer and Kotlin mapper; unknown/newer versions **reject the passive domain safely** with a documented user-safe error, never reinterpret new fields as old semantics.
- **Older compatible client:** it may ignore an unknown *new domain* only if existing envelope policy explicitly permits doing so; it must never convert missing `passives` to a fabricated acquired catalog. Other existing sections should remain functional.
- **Malformed known version:** reject duplicates, booleans in version fields, unsupported types, unknown keys if strict payload contract mandates; do not implicitly coerce unsafe data into disclosed entries. A future design owner must specify whether the rejection is whole-view `VIEW_ERROR` versus an isolated unavailable-status state, but **no partial private data may be returned**.
- **Legacy save:** old `perks` continue their existing gameplay/math and Status inspection behavior. A missing new reveal ledger is **not evidence of reveal**; do not assume any `visible` default grants disclosure without definition+viewer checks. Migration of ambiguous records requires explicit owner decisions and compatibility tests, not guesswork.
- **IDs and definitions:** unknown/deprecated IDs, renamed passives, collisions, authored false classifications and partial knowledge need a migration/alias policy before enabling any new wire entry.
- **No save expansion by this packet:** no `GameState.passives`, `qualification_ledger`, `revealed_passives` or revised `perks` structure has been added. Save schema v1 stays unchanged.

## 8. Future Python → bridge → Kotlin → UI ownership

| Layer | Future responsibility; implementation NOT DONE | Minimum consumer/gate |
|---|---|---|
| Authoritative Python domain and Status | Validate approved ownership, definition, classification, holder/viewer, field-level reveal and authored visible source. Construct deep-copied projection, deterministic visible order. | No new side effects during repeated view; hidden IDs absent from serialized output. |
| `AndroidGameSession._view_for` | Add only the approved detached fragment after schema/version acceptance. Current eight-key envelope persists compatibly. | Raw `state.perks`, `state.npcs`, provenance ledgers and hidden definitions are never returned. |
| Kotlin `BridgeSnapshotMapper` / `GameSnapshot` | Future typed DTO with strict numeric/array/type validation and no generic map fallback. Reject/ignore version only as explicitly specified. | Unknown fields and hidden provenance cannot propagate into state/logs. |
| `GameViewModel` | Hold immutable safe snapshot; expose loading/unavailable state where needed; no local passive eligibility/qualification logic. | Save/load/refresh does not modify owner state or grant a passive. |
| Compose Status / Character consumers | Render exactly authorized entries and safe text, with accessible empty/unavailable feedback. No locked-secret slots, client-registry lookups or inferential badges. | Screen-reader semantics must not expose secret IDs or reveal timing from placeholders. |
| Integration/security verification | Exercise Python rules, bridge JSON, mapper DTO, Compose tests and snapshot parity at exact tested heads. | Distinguish source-only validation, CI executed, emulator and physical-device evidence. |

**Interface choice not yet fixed:** whether the future passive domain nests under `status` or ships as a separately versioned root object is left to the D-026/Android migration owner, with explicit review to avoid collisions. This document proposes `status.passives` to make gates testable, not as silently accepted wire canon.

## 9. Future acceptance matrix — PLANNED / NOT EXECUTED

| ID | Setup | Expected assertion |
|---|---|---|
| PV-01 | No owned/revealed passives; registry has many secret records | `entries=[]`; no hidden names, IDs, placeholder count, slots or total. |
| PV-02 | `state.perks` has a current visible additive perk approved for reveal | Only stable player-safe fields emitted; source raw modifiers and hidden tags not copied. |
| PV-03 | `state.perks` contains hidden perk that modifies displayed stat | Current arithmetic unaffected; deep stat inspection remains `unidentified_modifier`; no hidden list entry/ID in any bridge JSON. |
| PV-04 | Owned-but-unrevealed vs qualified-but-not-owned vs discovered-existence-only | All three absent from acquired passive list; no implied qualification/progress. |
| PV-05 | Revealed passive has classified higher stage/unpublished source | Only allowed present stage/effect summary; no future-stage/secret-source leakage. |
| PV-06 | One NPC has learned a rumor; another has not; player knows no public publisher | Neither observer memory nor rumor confidence/truth leaks; no SOC qualification or public reputation fabricated. |
| PV-07 | D-075 cooperative vs solo Tamsin branch after save/reload | Preserve known choice divergence; no automatic SOC_0007/SOC_0010 entry or private memory ID. |
| PV-08 | Same view requested twice, after retry and after save/load | Byte-stable safe projection for stable state; no owner/qualifier mutation. |
| PV-09 | Unknown/boolean/wrong-type passive domain version, duplicate/unknown IDs | Fail-closed and player-safe error/no disclosure according to accepted version policy; no raw diagnostics. |
| PV-10 | Legacy schema-v1 save with perk record lacking target reveal metadata | Existing game behavior preserved; no invented acquisition or inferred reveal; migrate only with explicit approval. |
| PV-11 | Kotlin mapper sees safe version plus injected unknown/private fields | Strict DTO contains only approved keys; UI and logs contain none of the injections. |
| PV-12 | Compose empty/visible/unavailable states and accessibility | No secret counting, alt text, label, tooltip, analytics or announced hidden condition. |
| PV-13 | Legitimate visible perk contribution and future passive list both appear | Consistent display without double-counting the rule effect; UI does not calculate stats. |
| PV-14 | Failed late social qualification/publication transaction | All durable world/quest/social/status state and player view remain unchanged, per P14 rollback design. |

**Existing source/test leads, not executed here:** `tests/test_status.py` (hidden perk and deep inspection); `tests/test_android_bridge.py` (current eight-key view and redaction); `tests/test_phase1_quest_branch_world_consequence.py` (Tamsin save/reload and private-memory redaction); `docs/systems/status/PASSIVE_RUNTIME_OWNER_PROJECTION_DISPOSITION_WAVE_001.md`. Kotlin parser/Compose tests and a new passive-list Python suite are future work; no test class is invented.

## 10. Closure, compatibility and next decision

This P18 child closes **only** the ambiguity of the proposed player-safe passive-list boundary: distinct qualification/ownership/reveal; strict allowlist/denylist; no private/canon leakage; independent version/migration rules; explicit Python/bridge/Android responsibilities and 14 reviewable future test cases. P14's public-reputation provenance and all unresolved canon questions remain intact.

**Master D-046 remains IN_PROGRESS.** Future approved owner work must settle definition+reveal owner semantics, projected-domain location, version and error contract, old-save migration/alias rules, authored source explanation and Android/Status consumer design. Only then may runtime tests or a DTO be implemented under a separately claimed task. Do not infer a completed gameplay feature or a new schema from this design artifact.

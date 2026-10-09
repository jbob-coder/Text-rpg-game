# P18 / D-046 — Passive-List Projection Source Evidence and Verification Limits

**Player-AI:** Veyr / PLAYER_VEYR, session SESSION_VEYR_20261008T1747-0400_S02.  
**Authority:** OR-037 P18, Bulletin claim commit 2a6beeb9a6f12eb409c374202728a1e971b576c1, CLAIM_HEAD 8e0286b83d17087917d1f3a7eceb1eb718a8b7ec.  
**Output:** docs/systems/status/P18_D046_PLAYER_SAFE_PASSIVE_LIST_PROJECTION_CONTRACT.md.  
**Class:** documentation-only target design, NOT implemented or canon, NOT executable test evidence.

## Verified exact-source anchors

| Source | Git blob at inspection | Confirmed source statement |
|---|---|---|
| src/textrpg/core.py | 608b37e58fb652b78c921c0459fceb3753131ce3 | GameState owns durable perks/snapshot; separate player, world and NPC state owners remain. |
| src/textrpg/status.py | 3f06f670134e0e71b0d1bf3642fab32f5869585a | build_status_view emits identity/attributes/resources/derived/skills/abilities/conditions, no passives. inspect_status_value is a safe explanation API rather than raw state access. |
| src/textrpg/android_bridge.py | 73aa4c59edb18ef4c413976d5a71cdd2879a399e | _view_for projects scene/status/inventory/quests/map/room/visuals/meta; no passive list currently. |
| tests/test_status.py | 785a6b8db92c7c92fc036ea36be71b922592032c | test_hidden_perk_provenance_is_redacted_after_save_resume and definition-hidden derived breakdown test exercise source-level visibility assertions. |
| tests/test_android_bridge.py | bd389dc04ae19990d7049f65818a3e8f843869d6 | test_new_session_returns_player_safe_scene_and_status expects current eight keys and checks forbidden authored keys. |
| docs/systems/status/PASSIVE_RUNTIME_OWNER_PROJECTION_DISPOSITION_WAVE_001.md | b69518e2dca770f395710f6e468292855ca9f351 | Existing perks are narrow additive owner; the future passive-list projection does not exist and needs explicit safe domain/version/migration decisions. |
| docs/systems/status/PASSIVE_STATE_OWNER_RESOLVER_MATRIX_WAVE_001.md | c8d9027bfb082dec01d5334056c910cb33625c49 | Conceptual owner domains and qualification evidence must not be invented as 23 new state containers or Android-owned data. |
| docs/systems/status/STATUS_KNOWLEDGE_VISIBILITY_STANDARD.md | 19e94ad9273ac44432abae144bed9b7a6a9b0f68 | Prequalification hides name/icon/slot/progress/requirement; reveal and public disclosure are distinct. |
| docs/systems/status/SOCIAL_PASSIVE_EVIDENCE_PUBLICATION_QUALIFICATION_CONTRACT_P14.md | 9c8281c7a893c4a8839914aedaf36b586161c229 | World occurrence, NPC-held knowledge, authorized publication, qualification and disclosure are separate, unimplemented gates. |
| docs/android/ANDROID_CONSUMER_AND_PROJECTION_MAP.md | b505e490246f2eee3ae08c27d7c494ae7d63e124 | Current Kotlin GameSnapshot contains 21 listed fields; BridgeSnapshotMapper is typed, but does not contain passive-list DTO/consumer. |

## Acceptance-source checklist — document review, NOT runtime PASS

- A1: CURRENT vs TARGET vs unresolved source owners stated in §2.
- A2: qualification/ownership/reveal independent and prequalification invisibility established in §3.
- A3: explicitly proposed and noncanonical wire fragment, per-field allowlist in §4.
- A4: denylist covers requirements, source, owner writes, NPC-private state and count/timing side-channels in §5.
- A5: P14 five-gate social provenance reused without new publisher in §6.
- A6: independent domain version, strict error/missing/legacy policy and schema-v1 guard in §7.
- A7: Python -> bridge -> typed Kotlin -> ViewModel -> Compose responsibilities and migration conflict guard in §8.
- A8: PV-01..PV-14 named future cases and explicit no-run status in §9.
- A9: parent Master D-046 remains IN_PROGRESS; no runtime/canon/save-schema change in §10.
- A10: source references in this packet were individually retrieved by GitHub connector; textual authority and pre-existing test definitions, not observed current execution.

## Limits

The packet's projection_version=1, status.passives, entries and PERK_EXAMPLE_VISIBLE are **hypothetical review placeholders**, not authorized protocol IDs, stable game content or a migration. No test, CI, Gradle, emulator, device, APK, Android DTO, current Kotlin compile, save-schema migration, runtime social qualifier or public publisher was executed or created by this pass.

The named current tests were read, not run. No actual passive-list feature or target acceptance test is presently asserted green. Version/fail-closed policy choices require implementation-owner review prior to coding. All current gameplay proof tasks and dependency gates retain their existing status.

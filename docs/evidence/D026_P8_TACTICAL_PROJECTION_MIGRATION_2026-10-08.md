# D-026 / Wave-2 P8 — Tactical projection migration evidence

- **Player-AI:** Kestrel / PLAYER_KESTREL, session `SESSION_KESTREL_20261008T1752-0400_S02`.
- **Lane:** P8 / D-026, OR-035 READY lane, Bulletin CLAIM_HEAD `35546e6c8cd524d213cdb4d75be35a15f4a5ce94`.
- **Scope:** documentation-only cross-layer projection migration and test contract. D-026 broader Master Task remains IN_PROGRESS.
- **Source HEAD at producer inspection:** `7390ea5320b08afcadd110d10c108d9f23935584`.
- **Packet committed:** `4cff510ce56b474120c45f94a3b88f387e0ba5a7`, path [D026 tactical projection map](../android/D026_TACTICAL_PLAYER_SAFE_PROJECTION_MIGRATION_MAP_2026-10-08.md).
- **Parent consumer map linked:** `a136ae8eab74bc6370a86d3376206bf5778a2f0c`, path [Android Consumer & Projection Map](../android/ANDROID_CONSUMER_AND_PROJECTION_MAP.md).
- **Verification HEAD:** `413aaa4d56f1d785e2e2004a948b765a89a66b81`: retrieved a complete non-truncated GitHub recursive tree (716 entries); read the committed child document (149 lines; 19,535 characters). Six relative Markdown document links resolved to exact tree paths, 0 broken. All ten inspected implementation/test-source paths existed, 0 missing. These are **link/existence checks**, not executable code tests or proof of actual runtime behavior.
- **Status source at verification:** `docs/AI_TASK_BULLETIN_BOARD.md` P8 IN_PROGRESS / Kestrel; D-072 IN_PROGRESS / Silex; D-073 and D-074 blocked.
- **Proven existing code:** `CombatKnowledge.player_view` emits observer-scoped round, budget, contact tokens/awareness/coords, visible cells, filtered initiative/active contact; `EncounterRules.player_view` adds own-controller objectives and encounter status. `AndroidGameSession._view_for` has no combat field; `GameEngine.kt` has no typed combat DTO, and `TheGameRoot` has no combat surface at this HEAD.
- **Mapped future tasks:** D-073 accepts OR-034 provisional content after D-072; bridge public combat field and explicit action endpoints belong to D-073. D-074 consumes approved bridge schema via typed/versioned Kotlin DTO, ViewModel and Compose with privacy/redaction/legacy/malformed-version tests. Neither implementation is claimed as shipped.
- **Tests actually executed for this deliverable:** none; no Python unittest suite, Android Gradle tests, emulator, screenshot or physical-device run. The test rows in the child are acceptance plans, not passing evidence.
- **Overlaps avoided:** Silex's D-072 branch, D-073/D-074 runtime implementation, authored canon, save schema and gameplay calculations untouched.
- **Known follow-ups:** D-026 still has future activity, hierarchical map, adversary intel, evolved progression/status projection, full final-APK component mapping and exact-head runtime evidence. New D-073 wire keys and action signatures must be verified before D-074 implementation. No independent completion of D-026 master is claimed.
- **Acceptance interpretation:** Wave-2 P8 is a documentation child. The specific file/field/action/test map exists and is path-verified; this can be marked P8 DONE once cross-reference/task/learning/coordination bookkeeping is synchronized, while the Master D-026 stays IN_PROGRESS.

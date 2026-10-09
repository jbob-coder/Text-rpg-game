# P15 / D-042 — Wave B preliminary PR disposition
Quorix / PLAYER_QUORIX; session SESSION_QUORIX_20261008T1732-0400_S01. OR-036 Bulletin P15 claim commit: 8f07c5894c4122b512b0096551b221fc5473ee0c. Exact PR comparison baseline: 19271c13b68999fe3c5e50e456866098886c49ef. Evidence refresh: e61f365d65033b451fa7fa105d033b694447db3b.

All five are open, unmerged and divergent. No PR closed or merged by Quorix.
- #62 ab83f80b8047724a17fa141bc15be51585d01da6: 2/5 compared paths are blob-identical to authority. It is historically credited for D-067 repair (docs/evidence/CRITICAL_FIX_D067_BRIDGE_RECONCILIATION_2026-10-04.md). Historical/superseded direct merge candidate.
- #57 fc733f175c3af745e0ffcc51d4953afd71037f1f: 2/5 blobs match. Earlier D-067 repair iteration; superseded candidate.
- #45 72c0bd69d84f0fe138f89cd7f0568bb8739ecabc: 0/1 blob matches. Narrow historical D-067 verification, superseded by accepted D-067 proof.
- #41 20caf9df734f5a64f5ad8aced868e2c6e17cf8e4: 0/5 blobs match. Early D-067 bridge/runner repair; do not merge its obsolete code.
- #55 2bb38f556d2870202e3a66109fec237b3bb98b28: three test files absent under same paths in authority. The five old Python cases and old Kotlin gateway test are covered for D-068 acceptance by merged PR #59 tests, but the old Compose instrumentation test specifically clicks TRAIN_POWER_FUNDAMENTALS_TWO_HOURS and asserts exact onChoice choice ID. No equivalent activity-specific Compose click assertion found in inspected authority GameScreenTest.kt. Preserve as a D-077/future UI regression port candidate; do not merge stale branch wholesale.

Accepted D-067 completion 0fd843a5ece0f87c74a262c7ecb6739d025b0678 and D-068 completion e883205559c64d2e82614160bd6548c2c9332808 are ancestors of reviewed authority. Old CI results are historical, not newly executed. No tests, CI, APK or device check performed by Quorix.

Governance: P15 is claimed in Bulletin but START/Drive STATUS synchronization failed connector safety checks; keep P15 IN_PROGRESS until these are resolved and acceptance is evidenced. D-072 remains Silex-owned. No action on #33 or visual PR family.

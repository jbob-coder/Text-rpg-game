# P12 / D-045 — Training / Mentor / Facility Progression Standard Evidence

Status: **DOCUMENTATION EVIDENCE / NO RUNTIME CHANGE / NOT CANON IMPLEMENTATION**  
Player-AI: **Veyra / PLAYER_VEYRA**  
Session: `SESSION_VEYRA_20261007T1140-0400_S02`  
Task: **Parallel P12 / D-045**  
Claim commit: `6e68d10bf8365486782755089e580364ef8a829d`  
Claim HEAD: `e2af38474fdec3298f3c669569bd582c214ea0be`  
Primary creation commit: `a61f920296bd4d11eefb83595e77ce339609ea39`

## Primary artifact

`docs/systems/TRAINING_MENTOR_FACILITY_PROGRESSION_STANDARD.md`

Readback blob:

`7430a51a13c9f02161e0bdab6a92a35ab628b7b4`

Readback length at verification: **34,971 characters**.

## Source authority readback

| Source | Blob SHA | P12 use |
|---|---|---|
| `src/textrpg/schema.py` | `895115279918f48b6bed1e12d0ca51b368828c46` | authoritative 23 current skill IDs/categories |
| `EVOLVED_SKILL_REGISTRY.md` | `e39ffedde044fa7402715061a9a707ff6fcd27ff` | target training direction for the 23-skill foundation |
| `COMBAT_CLASS_CATALOG.md` | `b063d3f8691a142e169e124cfeaafe13587bd897` | seven target class families and training/facility dependencies |
| `PROFESSION_RANK_STATUS_NAMESPACE_STANDARD.md` | `c399c0f7bc61855565e603fa46f075e1a9ec98b9` | namespace separation, stable-ID policy and explicit P12 next-child authority |
| `TRAINING_AND_PRACTICE_ACTIVITY_STANDARD.md` | `e4d7ee4ffd5a632ec8a5e1e536d6a7b7e04cb650` | existing training/practice, mentor, facility and player-safe preview owner |
| `ACTIVITY_RECORD_AND_STATE_STANDARD.md` | `c166225920e3cc1315f944ced28eab618af39b58` | `ACTIVITY_*` identity, availability and durable-activity boundaries |
| `ACTIVITY_TIME_COST_ATOMICITY_STANDARD.md` | `2d54df17a07b62e778b7f9afe011b27bb1dace66` | world-time/resource ownership and transaction atomicity |
| `PHASE_1_PROGRESSION_SCHEMA_API_MIGRATION_PACKET.md` | `8ffb07c30abc95fbf6d823fe106b4b25149c7704` | schema-v1/no-new-top-level-owner boundary |

## Structural validation performed

Repository readback checks against the committed primary artifact found:

- CURRENT REALITY marker: **present**;
- TARGET DESIGN marker: **present**;
- PROPOSAL marker: **present**;
- existing `ACTIVITY_<IDENTITY>` owner retained: **present**;
- schema-v1 preservation boundary: **present**;
- direct next child `Gate Twelve Progression Proof Packet`: **present**;
- explicit no-runtime implementation statement: **present**.

### Current skill coverage — 23 / 23

The primary artifact contains every current runtime skill ID exactly as a mapped row:

1. `unarmed`
2. `blades`
3. `ranged`
4. `defense`
5. `tactics`
6. `athletics`
7. `stealth`
8. `traversal`
9. `survival`
10. `engineering`
11. `technical_systems`
12. `medicine`
13. `crafting`
14. `persuasion`
15. `deception`
16. `intimidation`
17. `empathy`
18. `leadership`
19. `investigation`
20. `history`
21. `factions`
22. `powers`
23. `creatures`

Missing IDs: **0**.

### Target class-family coverage — 7 / 7

The class training matrix contains one row each for:

1. Vanguard
2. Skirmisher
3. Operator
4. Field Specialist
5. Investigator
6. Envoy
7. Ability Specialist

Missing class families: **0**.

## Acceptance reconciliation

### Stable IDs / ownership

Satisfied.

P12 preserves existing `ACTIVITY_*` ownership and introduces only explicitly PROPOSAL target namespaces:

- `TRAINING_PATH_*`
- `MENTOR_CAP_*`
- `EVAL_CAP_*`
- `FACILITY_CAP_*`
- `TRAINING_REQ_*`

Capability identity is explicitly separated from NPC identity, location identity, profession/class identity and availability query output.

### Training prerequisites

Satisfied.

The standard defines a read-only legality pipeline covering:

- subject/activity resolution;
- world/location access;
- facility capabilities;
- mentor/evaluator capabilities and schedule/presence;
- social/membership/rank access through owning systems;
- knowledge/discovery;
- equipment/tools;
- injury/condition restrictions;
- plateau/entry evidence;
- time/resource preflight.

### Facility / mentor capability model

Satisfied.

Mentor/evaluator capability is not an NPC identity. Facility capability is not a location or institution identity. Concrete world/NPC bindings must resolve through their authoritative owners.

### CURRENT / TARGET / PROPOSAL

Satisfied explicitly in section 2 and reinforced throughout stable-ID and implementation boundaries.

### Migration / test seams

Satisfied.

The standard retains D-061 schema-v1 authority, treats available-training lists as derived query state by default, defines the conditions that would require future durable migration, and supplies registry/availability/transaction/save/projection test gates.

### Next D-045 child

Explicit:

**Gate Twelve Progression Proof Packet**, followed by the **Progression UX Contract**.

## Boundaries preserved

P12 does **not**:

- implement a new training formula;
- rebalance current training;
- add a runtime progression field;
- add a save-schema version;
- create a canon mentor NPC;
- create a canon institution/faction;
- create a canon facility location;
- change Android DTOs;
- edit D-072/D-073 tactical implementation;
- claim Python/Android/CI/emulator/device/APK test execution.

## Validation class

**DOCUMENTATION_READBACK / SOURCE-CONTRACT CROSS-CHECK**

No Python, Android, Gradle, CI, emulator, physical-device or APK tests were executed for P12.

The evidence supports completion of the bounded P12 documentation child only. Master D-045 remains IN_PROGRESS.

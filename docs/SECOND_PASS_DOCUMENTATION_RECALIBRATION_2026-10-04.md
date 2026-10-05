# THE GAME — Second-Pass Documentation Recalibration — 2026-10-04

Status: **ACTIVE / D-060 RECALIBRATION / FIRST-PASS FLOOR CLOSED**
Repository: `jbob-coder/Text-rpg-game`
Branch: `docs/master-game-development-program`
Evidence source: `docs/evidence/repository_inventory_d060_exact_revision_2026-10-04.json`
Measured immutable source HEAD: `4570005b4d544f56db1222623955139a3b23c01a`

## 1. Purpose

D-058 proved that the first-pass semantic documentation floor reached 148 / 148 units. D-060 converts that floor into a second-pass program direction using current immutable-revision evidence rather than increasing file counts for their own sake.

The first-pass quota matrix remains historically and semantically valid. It is no longer the default growth target.

Second-pass work is measured by **closure gates**, structured records, migration readiness, executable proof, and integration evidence.

## 2. Fresh immutable-revision checkpoint

At source HEAD `4570005b4d544f56db1222623955139a3b23c01a`:

- tracked files: **561**;
- tracked blob bytes: **5,810,858**;
- files under `docs/`: **416**;
- Markdown files repository-wide: **387**;
- Markdown files under `docs/`: **385**;
- structured documentation paths: **24**;
- PNG files: **24**;
- Python files: **43**;
- Kotlin/KTS files: **68**;
- JSON files: **26**;
- Python/Kotlin test-source paths: **52**;
- world Markdown files: **18**;
- system Markdown files: **263**;
- asset Markdown files: **35**;
- Android Markdown files: **14**.

Compared with the prior immutable D-019 checkpoint at `991cd9b29ea0752fa1c303a19e8f210713efe4b5`, the repository gained 71 tracked files, 67 Markdown files, 47 system Markdown files and 9 Android Markdown files. That growth does **not** imply equivalent semantic completion.

Exact Markdown word/heading totals are not claimed for this source HEAD because the connected execution environment does not expose a complete local checkout. D-019 retains that execution item.

## 3. Inventory-control correction

`tools/documentation_inventory.py` now:

- resolves the requested revision to an immutable commit SHA;
- reads committed content from that revision rather than walking the working directory;
- excludes untracked and uncommitted state by construction;
- records the measured source SHA in output;
- measures Markdown headings in addition to words;
- retains legacy keys where practical for downstream compatibility.

Regression coverage proves:

1. dirty edits, untracked Markdown and an untracked output file do not alter the revision report;
2. two different committed revisions produce distinct correct counts.

This closes the working-tree contamination defect that motivated D-060.

## 4. Recalibrated second-pass rule

Do **not** create more documents merely to raise V00–V12 file counts.

A domain advances in second pass only when work closes one or more of these evidence classes:

- **schema/ownership** — authoritative state owner, stable IDs and validation are implementation-ready;
- **migration** — current -> target mapping, save compatibility, rollback and deprecation boundaries are explicit;
- **structured content** — records exist under a validated schema rather than prose-only placeholders;
- **runtime proof** — authoritative behavior is implemented and deterministic where required;
- **projection/privacy** — player-facing consumers receive only safe normalized state;
- **persistence** — save/load behavior is proven for durable state;
- **consumer evidence** — Android/CLI/UI mappings and actions are directly verified;
- **asset provenance/QA** — source, raster, consumer, stage and approval evidence are reconciled;
- **performance/device** — bounded workload is profiled with emulator/device distinctions;
- **integration** — Phase 1 behavior works across subsystem boundaries on one exact HEAD.

The 148-unit first-pass floor is retained as a coverage baseline, not expanded into a larger arbitrary flat-document quota.

## 5. Domain second-pass closure gates

| Area | Second-pass closure gate | Phase 1 impact | Priority |
| --- | --- | --- | --- |
| V00 — authority/governance | keep master/register/board/evidence synchronized; no duplicate authority | indirect | P0 control |
| V01 — repository truth | exact-revision inventory, migration/evidence reconciliation, reproducible current-state proofs | direct program trust | P0 control |
| V02 — visual/assets | provenance-normalized survivor decisions, runtime consumers, QA and approval boundaries | room/actor/equipment presentation | P1 unless blocking |
| V03 — Gate Twelve | integrated proof-region content/assets/state/verification rather than additional planning volume | direct | P0 |
| V04 — world | validated structured entities/routes/resources beyond the nine-node proof region; avoid filler | limited for initial Phase 1 | P1 |
| V05 — social/NPC | implementation-ready social migration plus durable Tamsin memory/privacy proof | requirements 3–4 | P0 |
| V06 — progression | progression migration packet plus persistent deterministic Phase 1 proof | requirement 5 | P0 |
| V07 — items/economy | current item/equipment migration and exact-head integrated proof; full economy may remain deferred | requirement 6 | P0 |
| V08 — tactical combat | schemas -> pure grid -> transient engine -> AI -> aftermath -> Gate Twelve bridge | requirements 9–12 | P0 |
| V09 — adversaries/world memory | keep contracts implementation-ready; runtime may wait until Phase 1 core is stable | nonblocking for first Phase 1 | P1 |
| V10 — activities | exact-head legality/cost/time/persistence proof for selected Trace Chamber activity | requirement 8 | P0 |
| V11 — application UX | authoritative actor/room projection plus known render/action/test-gap closure | direct Android surface | P0 |
| V12 — Android/APK | tactical consumer, integrated regression, low-end profiling, provenance/acceptance gate | exit gate | P0 late-stage |
| Cross-domain persistence | integrated save/load deterministic sequence and schema discipline | direct | P0 |
| Cross-domain evidence | exact-head tests/builds/privacy/performance/provenance artifacts | direct | P0 |

## 6. Ranked second-pass execution backlog

The campaign authority remains `docs/AI_20_TASK_EXECUTION_CAMPAIGN_2026-10-04.md`.

After D-060, the ranked execution order remains:

1. D-061 progression schema/API migration;
2. D-062 social schema/API migration;
3. D-063 items/economy schema/API migration;
4. D-064 player-safe room/actor projection runtime slice;
5. D-065 Tamsin durable-memory reactive proof;
6. D-066 Phase 1 progression proof;
7. D-067 Phase 1 inventory/equipment exact-head proof;
8. D-068 Phase 1 activity exact-head proof;
9. D-069 through D-074 tactical Python -> Android implementation chain;
10. D-075 quest/world-consequence proof;
11. D-076 integrated save/load deterministic gate;
12. D-077 Android consumer/test-gap closure;
13. D-078 low-end performance evidence;
14. D-079 integrated Phase 1 acceptance and APK provenance gate.

This ranking is dependency-aware. The bulletin board remains the claim authority.

## 7. D-058 consistency result

D-058 remains correct:

- the 148 / 148 result is a semantic first-pass floor;
- current raw file growth does not invalidate its ownership assignments;
- no domain should regain priority merely because its file count is smaller;
- no quota-filler batch is justified by the new inventory.

Therefore D-058 is not reopened.

## 8. D-019 consistency result

D-019 remains **IN_PROGRESS**, but its current checkpoint changes.

Closed by D-060:
- working-tree contamination risk in the local inventory tool;
- immutable source revision recording;
- regression proof for untracked/dirty-state exclusion;
- fresh exact-revision structural checkpoint.

Still open under D-019:
- execute/persist the full inventory tool from a complete checkout of an exact program revision;
- publish exact current-head Markdown word/heading totals from that execution;
- generalized world/place/route/political/settlement/ecosystem/beast/resource/NPC/item record extractors;
- provenance-normalized asset-stage totals;
- executed-test evidence separated from source-test path counts;
- owner acceptance/definition for the historical large numeric targets.

D-019 should not block the Phase 1 migration chain unless one of those remaining measurements is required by a specific implementation decision.

## 9. Phase 1 impact

D-060 removes a program-control blocker and allows direct accepted contracts to feed bounded implementation.

It does **not** itself prove any playable requirement.

Its operational effect is to unlock dependency-safe campaign tasks whose only outstanding control dependency was D-060, while keeping downstream runtime, Android, save, performance and owner-canon gates intact.

## 10. Next action

Use the bulletin board to claim the highest-ranked newly eligible task. Do not add another flat documentation quota wave before completing the migration and Phase 1 evidence work already ranked by the campaign.

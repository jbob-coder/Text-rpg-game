# P6 / D-019 — Exact-Revision Repository Inventory Checkpoint — 2026-10-08

**Status:** BOUNDED PARALLEL P6 EVIDENCE / D-019 PARENT REMAINS IN_PROGRESS
**Player-AI:** Nodus / PLAYER_NODUS / SESSION_NODUS_20261008T1737-0400_S02
**Repository:** jbob-coder/Text-rpg-game
**Authority branch:** docs/master-game-development-program
**Immutable source commit:** `fae4dd58c692298d8d9aadafb9704f8843359463`
**Verified Git tree SHA:** `9bfedd23f3dbbf251efb18718b4c274a878d0a5f`
**Machine-readable companion:** `docs/evidence/P6_D019_GIT_TREE_INVENTORY_2026-10-08.json`
**Source tool:** `tools/documentation_inventory.py` (blob `0a59930bee2e9ad407a6e0c3cb1931fbad60d3f5`)
**Test source:** `tests/test_documentation_inventory_tool.py` (blob `6587eecc386242f6fb45e4600ef46e9ada305156`)

## 1. Scope and method

This is a **current exact-revision structural refresh**, not a claim that the complete Git-archive inventory CLI ran or that the game is complete. Resolve the immutable source commit through the Git commit API; obtain its **tree SHA** from the commit object; obtain the recursive Git tree at that SHA; require `truncated=false`; and count only entries with `type=blob` (not directory entries). Sum `blob.size` for committed bytes. The observed recursive tree had 720 entries, including 662 file blobs, **no Git links** and **no symlinks**.

This source-compatible structural reproduction uses the same path/suffix and test-path predicates as `tools/documentation_inventory.py`. It does **not** replace that tool, D-081/D-082 `project_status_tracker.py`, the Master Task Register's semantic status, or the Master Documentation Record's documentation interpretation.

## 2. Exact source-revision counts

| Metric | Count |
| --- | ---: |
| Tracked files | 662 |
| Committed blob bytes | 7,428,218 |
| Files under `docs/` | 482 |
| Repository Markdown files | 447 |
| Markdown files under `docs/` | 445 |
| Structured docs under `docs/` (.json/.yaml/.yml/.csv) | 30 |
| D-081-style document-like paths (447 Markdown + 30 structured) | 477 |
| `docs/` asset-manifest JSON paths | 13 |
| `docs/evidence/` JSON paths | 14 |
| `docs/verification/` JSON paths | 3 |
| PNG files | 24 |
| Python files | 69 |
| Kotlin files | 72 |
| Kotlin + KTS files | 75 |
| JSON files repository-wide | 34 |
| Python/Kotlin test-source paths with `test` in path | 72 |
| `docs/world/` Markdown files | 18 |
| `docs/systems/` Markdown files | 269 |
| `docs/systems/status/` Markdown files | 205 |
| `docs/assets/` Markdown files | 36 |
| `docs/android/` Markdown files | 15 |
| `docs/GAME_CONTEXT_LOGS/` Markdown files | 13 |
| Files under `docs/evidence/` (all types) | 33 |
| Files under `docs/verification/` | 10 |
| Files under `tools/` | 4 |

**Semantic caveat:** file, heading, record, test-source, asset and document totals count different things. They cannot be substituted for a percentage of game, world, documentation-depth, art-stage or Android completion.

## 3. Historical comparison

Compare against D-060's immutable-source evidence at `4570005b4d544f56db1222623955139a3b23c01a`, *not* against an unversioned working tree:

| Metric | D-060 | P6 source | Difference |
| --- | ---: | ---: | ---: |
| Tracked files | 561 | 662 | +101 |
| Tracked blob bytes | 5,810,858 | 7,428,218 | +1,617,360 |
| Repository Markdown | 387 | 447 | +60 |
| `docs/` Markdown | 385 | 445 | +60 |
| Structured docs | 24 | 30 | +6 |
| Test-source paths | 52 | 72 | +20 |

Previous evidence remains valid for **its own source commit**; these deltas express repository growth, not retroactive corrections. D-058 first-pass semantic quota state is not reinterpreted from these raw path deltas.

## 4. Word/heading, structured records, assets and tests — explicit limits

**Word and heading totals: NOT MEASURED.** The existing tool computes `len(re.findall(r"\S+", text))` and six-level Markdown heading counts on **every** UTF-8 Markdown blob in a local `git archive`. The present environment could query the immutable tree and individual blobs but could not obtain a full local Git checkout (`git ls-remote` failed DNS resolution of github.com). A proposed complete 447-document API scan hit the connector's tool-call limit before producing a complete result. Do not backfill or estimate these values. No complete UTF-8 readability pass was executed.

**Structured world/domain record totals: NOT RE-MEASURED.** The 30 structured documentation paths are *files*, not records. The historical Status Wave-001 1,019-record and Gate Twelve 9-node/8-edge counts remain attributed only to the previously measured sources; a current cross-domain extractor is still required.

**Canonical asset stages: NOT RE-MEASURED.** The thirteen `docs/assets/manifests/*.json` paths are exact file paths, not 13 assets. Historic 104 manifest rows and 95 IDs from the older checkpoint cannot prove current canonical production-stage counts. Stage, source/master identity, variant/consumer, hash and approval remain in the asset provenance and family ledgers.

**Executed tests: NONE IN THIS CHECKPOINT.** The 72 paths are potential Python/Kotlin test *source files*, not the number of tests, passes, failures, CI checks, emulator runs or compatible devices. No full Python suite, Android build or device check was run or claimed for this P6 snapshot.

## 5. Reproduction recipe

From a **complete checkout containing the immutable source commit**:

```bash
git rev-parse fae4dd58c692298d8d9aadafb9704f8843359463^{commit}
git rev-parse fae4dd58c692298d8d9aadafb9704f8843359463^{tree}
git ls-tree -r -l fae4dd58c692298d8d9aadafb9704f8843359463
PYTHONPATH=. python -m unittest tests.test_documentation_inventory_tool -v
python tools/documentation_inventory.py --revision fae4dd58c692298d8d9aadafb9704f8843359463 --output /tmp/the-game-d019-inventory.json
```

Those commands are a **future execution recipe**, not a claim that they passed now. A complete-checkout run must compare the JSON report's `source_head`, structure and bytes to the companion evidence and then separately capture `markdown_words`, `markdown_headings`, `docs_markdown_words`, `docs_markdown_headings` and `unreadable_markdown`. If any number disagrees, investigate the cause rather than changing this historical checkpoint.

## 6. Task boundary and next safe extension

**Parallel P6 acceptance:** source-revision-bound structural refresh, persisted JSON and human interpretation, exact reproduction instructions, historical comparison and explicit execution limits. No tool semantics changed.

**Master D-019 remains IN_PROGRESS** until (a) full-checkout current-revision word/heading execution; (b) generalized structured world/domain extractors; (c) provenance-normalized asset-stage reconciliation; (d) executed-test evidence extraction distinct from source-path inventory; and (e) explicit owner-unit target mapping.

**Next player shortcut:** begin at `tools/documentation_inventory.py` and the JSON companion; reproduce the exact SHA on a full checkout before reporting word/heading totals. Continue the remaining D-019 semantic extraction, not D-081/D-082 aggregate tracker reimplementation. D-072 and the P7–P10 parallel lanes are outside P6.

# THE GAME — Project Status Tracking Standard

**Status:** ACTIVE  
**Owner task:** D-081  
**Primary tool:** `tools/project_status_tracker.py`  
**Existing corpus authority:** D-019 / `tools/documentation_inventory.py`  
**Task semantic authority:** `docs/THE_GAME_MASTER_TASK_REGISTER.md`

## 1. Purpose

This standard gives THE GAME one reproducible reporting path for:

- repository structure;
- project task status;
- conservative completion percentage;
- Phase 1 campaign completion;
- documentation/document counts;
- top-level and documentation-area file maps;
- structural implementation/test/tool counts.

It is an aggregation surface, not a replacement for existing authorities.

## 2. Authority order

For a status report:

1. exact Git revision / repository files;
2. fresh runtime/build/test evidence for implementation claims;
3. `docs/THE_GAME_MASTER_TASK_REGISTER.md` for semantic task state;
4. D-019 / `tools/documentation_inventory.py` for detailed corpus inventory;
5. `docs/MASTER_DOCUMENTATION_RECORD.md` for documentation-area interpretation;
6. generated project-status report.

If the generated report conflicts with a higher authority, fix the tracker or regenerate it. Do not edit the number by hand.

## 3. Completion percentage

The primary project percentage is intentionally conservative:

```text
Master Task Register completion % =
    tasks whose status begins with DONE
    -----------------------------------
       all registered TASK D-### entries
```

Every non-DONE state counts as incomplete, including:

- IN_PROGRESS;
- BLOCKED;
- PENDING;
- ACTIVE;
- PROPOSAL_READY;
- PLANNING;
- missing/unrecognized status.

This is an **unweighted task-register completion metric**.

It is **not** a claim that the total game, world content, art, documentation depth, Android client, final APK, or remaining engineering effort is complete by the same percentage. Tasks differ substantially in size.

A separate Phase 1 metric is reported for D-060 through D-079 using the same DONE/total rule.

## 4. Document counts

The tracker reports several document counts rather than one ambiguous total:

- **repository Markdown documents** — every tracked `.md` path;
- **docs Markdown documents** — tracked `docs/**/*.md`;
- **structured docs under docs/** — `.json`, `.yaml`, `.yml`, and `.csv` under `docs/`;
- **document-like paths** — `AGENTS.md` + `README.md` + tracked `docs/**/*.md` + the structured-document suffixes above.

Logs, PNGs, source code, build files and other evidence files are not counted as document-like paths by that final metric, even when they live under `docs/`.

A file existing does not mean its subject is semantically complete.

## 5. Repository map

Each report contains:

- tracked file count and committed blob bytes;
- file/byte totals per top-level area;
- file/byte totals per first-level `docs/` area;
- extension distribution;
- `src/` file count;
- `android/` file count;
- structural test-path count;
- `tools/` file count;
- workflow count.

All counts are bound to an immutable `source_head`.

## 6. Regenerating a report

From a complete checkout:

```bash
python tools/project_status_tracker.py \
  --revision HEAD \
  --json-output /tmp/the-game-project-status.json \
  --markdown-output /tmp/the-game-project-status.md
```

For historical evidence, replace `HEAD` with the exact commit SHA.

The tool resolves the requested revision to a commit and reads committed content through Git. Dirty or untracked working-tree files are intentionally excluded.

## 7. Required status-report format

When Nodus or another Player-AI reports project status, include at minimum:

1. source HEAD;
2. Master Task Register DONE/total and percentage;
3. D-060..D-079 DONE/total and percentage;
4. tracked file count;
5. repository Markdown count;
6. docs/ Markdown count;
7. document-like count;
8. task states by category;
9. major active/blocking tasks;
10. explicit boundary that the task percentage is not a total-content estimate.

## 8. Update rules

- Do not hand-edit a generated number to make it look current.
- Regenerate from the desired exact revision.
- When new tasks are added, the denominator legitimately changes.
- When a task changes state, the percentage changes only if the Master Task Register changes.
- Historical snapshots remain valid only for their recorded source HEAD.
- D-019 remains the detailed corpus/inventory authority; D-081 is the reporting aggregator.

## 9. Validation

Regression coverage lives at:

- `tests/test_project_status_tracker.py`;
- `tests/test_documentation_inventory_tool.py`.

The D-081 tracker must preserve exact-revision behavior and must not allow dirty/untracked local state to contaminate a revision-bound report.


## 10. Full repository manifest — D-082

D-082 extends the tracker from aggregate status into a path-by-path structural map.

Use:

~~~bash
python tools/project_status_tracker.py \
  --revision HEAD \
  --manifest-output /tmp/the-game-full-manifest.json
~~~

The manifest contains one entry for every tracked blob at the exact source revision:

- repository path;
- Git blob SHA;
- committed byte size;
- extension;
- top-level area;
- first-level documentation area when applicable;
- structural kind;
- whether the path counts as a document-like path.

The manifest is structural evidence. It does not assign gameplay semantics or replace domain authorities.

## 11. Revision-to-revision tracking

To answer "what changed since the last snapshot?" use a base revision:

~~~bash
python tools/project_status_tracker.py \
  --base-revision <OLDER_SHA> \
  --revision <NEWER_SHA> \
  --json-output /tmp/status-delta.json \
  --markdown-output /tmp/status-delta.md \
  --manifest-output /tmp/current-full-manifest.json
~~~

The delta reports:

- files added, removed and changed;
- documents added, removed and changed;
- net document-count change;
- tasks added or removed;
- task state/status transitions;
- completion-percentage movement.

"Documents created" between two revisions means document-like paths present in the newer revision but not the older revision. A rename appears as one removed path plus one added path unless Git-level rename interpretation is performed separately.

This gives Nodus two distinct answers:

- **current document count** — how many document-like paths exist now;
- **documents created since X** — how many document-like paths were added since an explicitly named base revision.

Never report a "documents created" delta without identifying the base revision.

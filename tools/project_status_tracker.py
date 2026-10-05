#!/usr/bin/env python3
"""Deterministic project-status and repository-manifest tracker for THE GAME.

Reports are built from immutable Git revisions. Working-tree state is ignored.
Task progress comes from docs/THE_GAME_MASTER_TASK_REGISTER.md at the same
revision. D-019 remains the detailed corpus-inventory authority.

Standard library only; requires requested revisions in the local Git object
database.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path, PurePosixPath

TASK_REGISTER = PurePosixPath("docs/THE_GAME_MASTER_TASK_REGISTER.md")
STRUCTURED_DOC_SUFFIXES = {".json", ".yaml", ".yml", ".csv"}
TASK_HEADING_RE = re.compile(r"^### TASK (D-\d+)\s+—\s+(.+?)\s*$")
STATUS_RE = re.compile(r"^- STATUS:\s*(?:`([^`]+)`(?:\s+.*)?|(.+?))\s*$")
PRIORITY_RE = re.compile(r"^- PRIORITY:\s*`?([^`]+?)`?\s*$")


def _git(repo_root: Path, *args: str, text: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(repo_root), *args],
        check=True,
        capture_output=True,
        text=text,
    )


def _repository_root(root: Path) -> Path:
    result = _git(root, "rev-parse", "--show-toplevel")
    return Path(result.stdout.strip()).resolve()


def _resolve_commit(repo_root: Path, revision: str) -> str:
    result = _git(repo_root, "rev-parse", "--verify", f"{revision}^{{commit}}")
    return result.stdout.strip()


def _ls_tree(repo_root: Path, source_head: str) -> list[dict]:
    """Return exact-revision tracked blobs from git ls-tree."""
    result = _git(repo_root, "ls-tree", "-r", "-l", source_head)
    rows: list[dict] = []
    for raw in result.stdout.splitlines():
        meta, path = raw.split("\t", 1)
        mode, obj_type, sha, size_text = meta.split(maxsplit=3)
        if obj_type != "blob":
            continue
        rows.append(
            {
                "path": PurePosixPath(path),
                "mode": mode,
                "sha": sha,
                "size": 0 if size_text == "-" else int(size_text),
            }
        )
    return rows


def _show_text(repo_root: Path, source_head: str, path: PurePosixPath) -> str:
    result = _git(repo_root, "show", f"{source_head}:{path.as_posix()}")
    return result.stdout


def classify_status(status: str | None) -> str:
    if not status:
        return "UNKNOWN"
    upper = status.upper().strip()
    if upper.startswith("DONE"):
        return "DONE"
    if upper.startswith("IN_PROGRESS") or upper.startswith("IN PROGRESS"):
        return "IN_PROGRESS"
    if upper.startswith("BLOCKED"):
        return "BLOCKED"
    if upper.startswith("PENDING"):
        return "PENDING"
    return "OTHER"


def parse_task_register(text: str) -> list[dict]:
    tasks: list[dict] = []
    current: dict | None = None
    for line in text.splitlines():
        heading = TASK_HEADING_RE.match(line)
        if heading:
            if current is not None:
                tasks.append(current)
            current = {
                "id": heading.group(1),
                "title": heading.group(2).strip(),
                "status": None,
                "priority": None,
            }
            continue
        if current is None:
            continue
        status = STATUS_RE.match(line)
        if status and current["status"] is None:
            current["status"] = (status.group(1) or status.group(2)).strip()
            continue
        priority = PRIORITY_RE.match(line)
        if priority and current["priority"] is None:
            current["priority"] = priority.group(1).strip()
    if current is not None:
        tasks.append(current)

    for task in tasks:
        task["state"] = classify_status(task["status"])
    return tasks


def _pct(done: int, total: int) -> float:
    return round((done / total * 100.0), 2) if total else 0.0


def _task_summary(tasks: list[dict]) -> dict:
    counts = Counter(task["state"] for task in tasks)
    done = counts.get("DONE", 0)
    return {
        "total": len(tasks),
        "by_state": dict(sorted(counts.items())),
        "done": done,
        "completion_pct": _pct(done, len(tasks)),
        "completion_definition": (
            "Conservative unweighted share of Master Task Register tasks whose "
            "status begins with DONE. All other states count as incomplete."
        ),
        "non_done": [task for task in tasks if task["state"] != "DONE"],
    }


def _campaign_summary(tasks: list[dict], first: int = 60, last: int = 79) -> dict:
    task_by_id = {task["id"]: task for task in tasks}
    selected: list[dict] = []
    missing_task_ids: list[str] = []

    for number in range(first, last + 1):
        task_id = f"D-{number:03d}"
        task = task_by_id.get(task_id)
        if task is None:
            missing_task_ids.append(task_id)
            task = {
                "id": task_id,
                "title": "Missing Master Task Register entry",
                "status": None,
                "priority": None,
                "state": "UNKNOWN",
                "missing_registration": True,
            }
        selected.append(task)

    summary = _task_summary(selected)
    summary["range"] = f"D-{first:03d}..D-{last:03d}"
    summary["expected_total"] = last - first + 1
    summary["missing_task_ids"] = missing_task_ids
    return summary


def _suffix(path: PurePosixPath) -> str:
    return path.suffix.lower() or "(none)"


def is_document_like(path: PurePosixPath) -> bool:
    if path.as_posix() in {"AGENTS.md", "README.md"}:
        return True
    return bool(
        path.parts
        and path.parts[0] == "docs"
        and (
            path.suffix.lower() == ".md"
            or path.suffix.lower() in STRUCTURED_DOC_SUFFIXES
        )
    )


def is_test_path(path: PurePosixPath) -> bool:
    posix = f"/{path.as_posix()}"
    return bool(
        (path.parts and path.parts[0] == "tests")
        or "/src/test/" in posix
        or "/src/androidTest/" in posix
    )


def path_kind(path: PurePosixPath) -> str:
    posix = path.as_posix()
    if is_document_like(path):
        return "document"
    if is_test_path(path):
        return "test"
    if posix.startswith(".github/workflows/"):
        return "workflow"
    if path.parts and path.parts[0] == "src":
        return "source"
    if path.parts and path.parts[0] == "android":
        return "android"
    if path.parts and path.parts[0] == "tools":
        return "tool"
    if path.parts and path.parts[0] == "content":
        return "content"
    if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"}:
        return "asset"
    if path.parts and path.parts[0] == "docs":
        return "documentation_evidence_or_other"
    return "other"


def manifest_entry(row: dict) -> dict:
    path: PurePosixPath = row["path"]
    return {
        "path": path.as_posix(),
        "sha": row["sha"],
        "bytes": row["size"],
        "extension": _suffix(path),
        "top_level": path.parts[0] if len(path.parts) > 1 else "(root)",
        "docs_area": (
            path.parts[1]
            if len(path.parts) > 2 and path.parts[0] == "docs"
            else "(docs-root)"
            if len(path.parts) == 2 and path.parts[0] == "docs"
            else None
        ),
        "kind": path_kind(path),
        "document_like": is_document_like(path),
    }


def build_manifest(rows: list[dict]) -> list[dict]:
    return [manifest_entry(row) for row in sorted(rows, key=lambda item: item["path"].as_posix())]


def _group_rows(rows: list[dict], key_fn) -> dict[str, dict]:
    groups: dict[str, dict] = defaultdict(lambda: {"files": 0, "bytes": 0})
    for row in rows:
        key = key_fn(row["path"])
        groups[key]["files"] += 1
        groups[key]["bytes"] += row["size"]
    return dict(sorted(groups.items(), key=lambda item: (-item[1]["files"], item[0])))


def _tasks_for_revision(repo_root: Path, source_head: str, path_set: set[str]) -> list[dict]:
    if TASK_REGISTER.as_posix() not in path_set:
        return []
    return parse_task_register(_show_text(repo_root, source_head, TASK_REGISTER))


def compare_revisions(
    repo_root: Path,
    base_head: str,
    source_head: str,
    base_rows: list[dict],
    source_rows: list[dict],
) -> dict:
    base_by_path = {row["path"].as_posix(): row for row in base_rows}
    source_by_path = {row["path"].as_posix(): row for row in source_rows}
    base_paths = set(base_by_path)
    source_paths = set(source_by_path)

    added = sorted(source_paths - base_paths)
    removed = sorted(base_paths - source_paths)
    common = base_paths & source_paths
    changed = sorted(
        path for path in common if base_by_path[path]["sha"] != source_by_path[path]["sha"]
    )

    def doc_paths(by_path: dict[str, dict]) -> set[str]:
        return {
            path
            for path, row in by_path.items()
            if is_document_like(row["path"])
        }

    base_docs = doc_paths(base_by_path)
    source_docs = doc_paths(source_by_path)
    docs_added = sorted(source_docs - base_docs)
    docs_removed = sorted(base_docs - source_docs)
    docs_changed = sorted(
        path
        for path in base_docs & source_docs
        if base_by_path[path]["sha"] != source_by_path[path]["sha"]
    )

    base_tasks = _tasks_for_revision(repo_root, base_head, base_paths)
    source_tasks = _tasks_for_revision(repo_root, source_head, source_paths)
    base_task_by_id = {task["id"]: task for task in base_tasks}
    source_task_by_id = {task["id"]: task for task in source_tasks}

    task_ids_added = sorted(set(source_task_by_id) - set(base_task_by_id))
    task_ids_removed = sorted(set(base_task_by_id) - set(source_task_by_id))
    task_transitions = []
    for task_id in sorted(set(base_task_by_id) & set(source_task_by_id)):
        before = base_task_by_id[task_id]
        after = source_task_by_id[task_id]
        if before["state"] != after["state"] or before["status"] != after["status"]:
            task_transitions.append(
                {
                    "id": task_id,
                    "title": after["title"],
                    "from_state": before["state"],
                    "to_state": after["state"],
                    "from_status": before["status"],
                    "to_status": after["status"],
                }
            )

    base_summary = _task_summary(base_tasks)
    source_summary = _task_summary(source_tasks)

    return {
        "base_head": base_head,
        "source_head": source_head,
        "files": {
            "added_count": len(added),
            "removed_count": len(removed),
            "changed_count": len(changed),
            "added": added,
            "removed": removed,
            "changed": changed,
        },
        "documents": {
            "added_count": len(docs_added),
            "removed_count": len(docs_removed),
            "changed_count": len(docs_changed),
            "net_count_delta": len(source_docs) - len(base_docs),
            "added": docs_added,
            "removed": docs_removed,
            "changed": docs_changed,
        },
        "tasks": {
            "base_total": base_summary["total"],
            "source_total": source_summary["total"],
            "base_done": base_summary["done"],
            "source_done": source_summary["done"],
            "base_completion_pct": base_summary["completion_pct"],
            "source_completion_pct": source_summary["completion_pct"],
            "completion_pct_delta": round(
                source_summary["completion_pct"] - base_summary["completion_pct"], 2
            ),
            "added_task_ids": task_ids_added,
            "removed_task_ids": task_ids_removed,
            "transitions": task_transitions,
        },
    }


def build_report(
    root: Path,
    revision: str = "HEAD",
    base_revision: str | None = None,
    include_manifest: bool = False,
) -> dict:
    repo_root = _repository_root(root)
    source_head = _resolve_commit(repo_root, revision)
    rows = _ls_tree(repo_root, source_head)
    paths = [row["path"] for row in rows]
    path_set = {path.as_posix() for path in paths}

    if TASK_REGISTER.as_posix() not in path_set:
        raise FileNotFoundError(f"Missing task register at {source_head}: {TASK_REGISTER}")

    tasks = _tasks_for_revision(repo_root, source_head, path_set)

    top_level = _group_rows(
        rows,
        lambda path: path.parts[0] if len(path.parts) > 1 else "(root)",
    )
    docs_rows = [row for row in rows if row["path"].parts and row["path"].parts[0] == "docs"]
    docs_areas = _group_rows(
        docs_rows,
        lambda path: path.parts[1] if len(path.parts) > 2 else "(docs-root)",
    )
    extensions = _group_rows(rows, lambda path: _suffix(path))

    markdown = [path for path in paths if path.suffix.lower() == ".md"]
    docs_markdown = [
        path for path in markdown if path.parts and path.parts[0] == "docs"
    ]
    structured_docs = [
        path
        for path in paths
        if path.parts
        and path.parts[0] == "docs"
        and path.suffix.lower() in STRUCTURED_DOC_SUFFIXES
    ]
    document_like = [path for path in paths if is_document_like(path)]
    tests = [path for path in paths if is_test_path(path)]

    report = {
        "schema_version": 2,
        "requested_revision": revision,
        "source_head": source_head,
        "inventory_mode": "git_ls_tree_exact_revision",
        "working_tree_included": False,
        "repository": {
            "tracked_files": len(rows),
            "tracked_blob_bytes": sum(row["size"] for row in rows),
            "top_level": top_level,
            "extensions": extensions,
            "source_files": sum(1 for p in paths if p.parts and p.parts[0] == "src"),
            "android_files": sum(1 for p in paths if p.parts and p.parts[0] == "android"),
            "test_paths": len(tests),
            "tool_files": sum(1 for p in paths if p.parts and p.parts[0] == "tools"),
            "workflow_files": sum(
                1 for p in paths if p.as_posix().startswith(".github/workflows/")
            ),
        },
        "documentation": {
            "documentation_scope_paths": sum(
                1
                for p in paths
                if p.as_posix() in {"AGENTS.md", "README.md"}
                or (p.parts and p.parts[0] == "docs")
            ),
            "repository_markdown_documents": len(markdown),
            "docs_markdown_documents": len(docs_markdown),
            "structured_docs_under_docs": len(structured_docs),
            "document_like_paths": len(document_like),
            "document_like_definition": (
                "AGENTS.md + README.md + docs/**/*.md + structured docs under docs/ "
                "with .json/.yaml/.yml/.csv suffixes."
            ),
            "areas": docs_areas,
        },
        "tasks": _task_summary(tasks),
        "phase1_campaign": _campaign_summary(tasks),
        "notes": [
            "Repository counts are bound to source_head and ignore working-tree state.",
            "Completion percentages are task-register metrics, not semantic estimates of total game/content completion.",
            "A document path existing does not prove its domain or runtime implementation is complete.",
            "Executed test pass counts require separate test evidence; test_paths is structural only.",
            "D-019 remains the detailed corpus/inventory authority; this tracker aggregates status for reporting.",
        ],
    }

    if include_manifest:
        report["manifest"] = build_manifest(rows)

    if base_revision is not None:
        base_head = _resolve_commit(repo_root, base_revision)
        base_rows = _ls_tree(repo_root, base_head)
        report["delta"] = compare_revisions(
            repo_root,
            base_head,
            source_head,
            base_rows,
            rows,
        )

    return report


def render_markdown(report: dict) -> str:
    repo = report["repository"]
    docs = report["documentation"]
    tasks = report["tasks"]
    phase1 = report["phase1_campaign"]

    lines = [
        "# THE GAME — Project Status Snapshot",
        "",
        f"Source HEAD: `{report['source_head']}`",
        f"Inventory mode: `{report['inventory_mode']}`",
        "",
        "## Executive status",
        "",
        f"- Master Task Register completion: **{tasks['completion_pct']:.2f}%** "
        f"({tasks['done']}/{tasks['total']} DONE).",
        f"- Phase 1 D-060..D-079 completion: **{phase1['completion_pct']:.2f}%** "
        f"({phase1['done']}/{phase1['total']} DONE).",
        f"- Tracked files: **{repo['tracked_files']}**.",
        f"- Repository Markdown documents: **{docs['repository_markdown_documents']}**.",
        f"- Markdown documents under docs/: **{docs['docs_markdown_documents']}**.",
        f"- Structured documentation records under docs/: **{docs['structured_docs_under_docs']}**.",
        f"- Document-like paths: **{docs['document_like_paths']}**.",
        "",
        "Completion % is deliberately conservative: DONE tasks divided by all registered tasks. "
        "It is not a claim that the total game, world content, art, Android release, or documentation depth is equally complete.",
        "",
    ]

    if "delta" in report:
        delta = report["delta"]
        lines.extend(
            [
                "## Revision delta",
                "",
                f"Base HEAD: `{delta['base_head']}`",
                f"- Files added / removed / changed: **{delta['files']['added_count']} / "
                f"{delta['files']['removed_count']} / {delta['files']['changed_count']}**.",
                f"- Documents added / removed / changed: **{delta['documents']['added_count']} / "
                f"{delta['documents']['removed_count']} / {delta['documents']['changed_count']}**.",
                f"- Net document-count delta: **{delta['documents']['net_count_delta']:+d}**.",
                f"- Completion change: **{delta['tasks']['completion_pct_delta']:+.2f} percentage points**.",
                "",
            ]
        )

    lines.extend(["## Task states", ""])
    for state, count in sorted(tasks["by_state"].items()):
        lines.append(f"- {state}: **{count}**")

    lines.extend(["", "## Phase 1 task states", ""])
    for state, count in sorted(phase1["by_state"].items()):
        lines.append(f"- {state}: **{count}**")
    if phase1["missing_task_ids"]:
        lines.append(
            "- Missing task registrations: "
            + ", ".join(f"`{task_id}`" for task_id in phase1["missing_task_ids"])
        )

    lines.extend(["", "## Top-level repository map", ""])
    for name, item in repo["top_level"].items():
        lines.append(f"- `{name}`: {item['files']} files / {item['bytes']} bytes")

    lines.extend(["", "## Documentation-area map", ""])
    for name, item in docs["areas"].items():
        lines.append(f"- `docs/{name}`: {item['files']} files / {item['bytes']} bytes")

    lines.extend(
        [
            "",
            "## Structural implementation/test counts",
            "",
            f"- src/: **{repo['source_files']}** files",
            f"- android/: **{repo['android_files']}** files",
            f"- structural test paths: **{repo['test_paths']}**",
            f"- tools/: **{repo['tool_files']}** files",
            f"- GitHub workflows: **{repo['workflow_files']}**",
            "",
            "## Document-count definition",
            "",
            docs["document_like_definition"],
            "",
            "## Non-DONE tasks",
            "",
        ]
    )
    for task in tasks["non_done"]:
        lines.append(
            f"- {task['id']} — {task['state']} — {task['title']} "
            f"(raw status: {task['status'] or 'NOT_RECORDED'})"
        )

    lines.extend(["", "## Reporting boundaries", ""])
    for note in report["notes"]:
        lines.append(f"- {note}")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Path inside the repository checkout")
    parser.add_argument(
        "--revision",
        default="HEAD",
        help="Git revision resolved to an immutable commit before reporting",
    )
    parser.add_argument(
        "--base-revision",
        help="Optional historical revision used to report file/document/task deltas",
    )
    parser.add_argument("--json-output", help="Optional JSON status output path")
    parser.add_argument("--markdown-output", help="Optional Markdown status output path")
    parser.add_argument(
        "--manifest-output",
        help="Optional JSON file containing every tracked path and classification",
    )
    args = parser.parse_args()

    report = build_report(
        Path(args.root),
        args.revision,
        base_revision=args.base_revision,
        include_manifest=bool(args.manifest_output),
    )

    if args.manifest_output:
        manifest_payload = {
            "schema_version": report["schema_version"],
            "source_head": report["source_head"],
            "tracked_files": report["repository"]["tracked_files"],
            "manifest": report.pop("manifest"),
        }
        Path(args.manifest_output).write_text(
            json.dumps(manifest_payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    json_payload = json.dumps(report, indent=2, sort_keys=True) + "\n"
    markdown_payload = render_markdown(report)

    if args.json_output:
        Path(args.json_output).write_text(json_payload, encoding="utf-8")
    if args.markdown_output:
        Path(args.markdown_output).write_text(markdown_payload, encoding="utf-8")
    if not args.json_output and not args.markdown_output:
        print(json_payload, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

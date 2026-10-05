#!/usr/bin/env python3
"""Deterministic exact-revision inventory for THE GAME repository.

The report is built from an immutable Git commit rather than the working tree, so
untracked files and uncommitted edits cannot contaminate revision-bound evidence.
Standard library only; requires the requested revision to exist in the local Git
object database.
"""

from __future__ import annotations

import argparse
import io
import json
import re
import subprocess
import tarfile
from collections import Counter
from pathlib import Path, PurePosixPath

WORD_RE = re.compile(r"\S+")
HEADING_RE = re.compile(r"(?m)^ {0,3}#{1,6}[ \t]+\S.*$")
STRUCTURED_DOC_SUFFIXES = {".json", ".yaml", ".yml", ".csv"}


def _git(repo_root: Path, *args: str, text: bool = False) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(repo_root), *args],
        check=True,
        capture_output=True,
        text=text,
    )


def _repository_root(root: Path) -> Path:
    result = _git(root, "rev-parse", "--show-toplevel", text=True)
    return Path(result.stdout.strip()).resolve()


def _resolve_commit(repo_root: Path, revision: str) -> str:
    result = _git(repo_root, "rev-parse", "--verify", f"{revision}^{{commit}}", text=True)
    return result.stdout.strip()


def _revision_files(repo_root: Path, source_head: str) -> list[tuple[PurePosixPath, bytes]]:
    archive = _git(repo_root, "archive", "--format=tar", source_head).stdout
    files: list[tuple[PurePosixPath, bytes]] = []
    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:") as tar:
        for member in tar:
            if not member.isfile():
                continue
            extracted = tar.extractfile(member)
            if extracted is None:
                continue
            files.append((PurePosixPath(member.name), extracted.read()))
    return files


def is_test_source(path: PurePosixPath) -> bool:
    return path.suffix.lower() in {".py", ".kt", ".kts"} and "test" in path.as_posix().lower()


def inventory(root: Path, revision: str = "HEAD") -> dict:
    """Inventory the exact committed tree for *revision*.

    Working-tree state is intentionally ignored. The revision is resolved to an
    immutable commit SHA first, and all content is read from ``git archive`` for
    that commit.
    """

    repo_root = _repository_root(root)
    source_head = _resolve_commit(repo_root, revision)
    revision_files = _revision_files(repo_root, source_head)
    paths = [path for path, _ in revision_files]

    by_extension = Counter((p.suffix.lower() or "(none)") for p in paths)
    markdown_entries = [(p, data) for p, data in revision_files if p.suffix.lower() == ".md"]
    docs_markdown = [(p, data) for p, data in markdown_entries if p.parts and p.parts[0] == "docs"]

    markdown_words = 0
    docs_markdown_words = 0
    markdown_headings = 0
    docs_markdown_headings = 0
    unreadable_text_files: list[str] = []

    for rel, data in markdown_entries:
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            unreadable_text_files.append(rel.as_posix())
            continue
        words = len(WORD_RE.findall(text))
        headings = len(HEADING_RE.findall(text))
        markdown_words += words
        markdown_headings += headings
        if rel.parts and rel.parts[0] == "docs":
            docs_markdown_words += words
            docs_markdown_headings += headings

    total_bytes = sum(len(data) for _, data in revision_files)

    def count_markdown(prefix: str) -> int:
        normalized = prefix.rstrip("/") + "/"
        return sum(1 for p, _ in markdown_entries if p.as_posix().startswith(normalized))

    def count_paths(prefix: str) -> int:
        normalized = prefix.rstrip("/") + "/"
        return sum(1 for p in paths if p.as_posix().startswith(normalized))

    structured_documentation_paths = sum(
        1
        for p in paths
        if p.parts and p.parts[0] == "docs" and p.suffix.lower() in STRUCTURED_DOC_SUFFIXES
    )

    return {
        "schema_version": 2,
        "root": str(repo_root),
        "requested_revision": revision,
        "source_head": source_head,
        "inventory_mode": "git_archive_exact_revision",
        "working_tree_included": False,
        "tracked_files": len(paths),
        "tracked_blob_bytes": total_bytes,
        # Legacy key retained for downstream compatibility. Its semantics are now
        # exact committed files at source_head rather than a working-tree walk.
        "tracked_like_files_excluding_build_and_git": len(paths),
        "total_bytes": total_bytes,
        "by_extension": dict(sorted(by_extension.items())),
        "markdown_files": len(markdown_entries),
        "markdown_words": markdown_words,
        "markdown_headings": markdown_headings,
        "docs_files": sum(1 for p in paths if p.parts and p.parts[0] == "docs"),
        "docs_markdown_files": len(docs_markdown),
        "docs_markdown_words": docs_markdown_words,
        "docs_markdown_headings": docs_markdown_headings,
        "structured_documentation_paths": structured_documentation_paths,
        "png_files": by_extension.get(".png", 0),
        "python_files": by_extension.get(".py", 0),
        "kotlin_files": by_extension.get(".kt", 0),
        "kotlin_kts_files": by_extension.get(".kt", 0) + by_extension.get(".kts", 0),
        "json_files": by_extension.get(".json", 0),
        "test_source_files": sum(1 for p in paths if is_test_source(p)),
        "world_docs": count_markdown("docs/world"),
        "system_docs": count_markdown("docs/systems"),
        "asset_docs": count_markdown("docs/assets"),
        "android_docs": count_markdown("docs/android"),
        "context_log_docs": count_markdown("docs/GAME_CONTEXT_LOGS"),
        "verification_files": count_paths("docs/verification"),
        "tools_files": count_paths("tools"),
        "unreadable_markdown": unreadable_text_files,
        "notes": [
            "Counts are derived from an immutable Git commit, not the working tree.",
            "Untracked files and uncommitted edits are intentionally excluded.",
            "Do not equate any one metric with owner-defined documentation targets.",
            "Executed test counts require separate test evidence; source-file count is not pass count.",
            "Asset production stage requires the asset ledger/manifests, not extension counts alone.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Path inside the repository checkout")
    parser.add_argument(
        "--revision",
        default="HEAD",
        help="Git revision to inventory; resolved to an immutable commit SHA before counting",
    )
    parser.add_argument("--output", help="Optional JSON output path")
    args = parser.parse_args()

    report = inventory(Path(args.root), args.revision)
    payload = json.dumps(report, indent=2, sort_keys=True)

    if args.output:
        Path(args.output).write_text(payload + "\n", encoding="utf-8")
    else:
        print(payload)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Deterministic local inventory for THE GAME repository.

Counts structural repository metrics without equating them to owner-defined
long-range documentation targets. Standard library only.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

WORD_RE = re.compile(r"\S+")


def is_test_source(path: Path) -> bool:
    return path.suffix.lower() in {".py", ".kt"} and "test" in path.as_posix().lower()


def inventory(root: Path) -> dict:
    ignored = {".git", ".gradle", "build", "__pycache__", ".idea"}
    files: list[Path] = []

    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if any(part in ignored for part in rel.parts):
            continue
        files.append(rel)

    by_extension = Counter((p.suffix.lower() or "(none)") for p in files)

    markdown = [p for p in files if p.suffix.lower() == ".md"]
    docs_markdown = [p for p in markdown if p.parts and p.parts[0] == "docs"]

    markdown_words = 0
    docs_markdown_words = 0
    unreadable_text_files: list[str] = []

    for rel in markdown:
        try:
            text = (root / rel).read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            unreadable_text_files.append(rel.as_posix())
            continue
        words = len(WORD_RE.findall(text))
        markdown_words += words
        if rel.parts and rel.parts[0] == "docs":
            docs_markdown_words += words

    total_bytes = sum((root / p).stat().st_size for p in files)

    def count_docs(prefix: str) -> int:
        return sum(
            1
            for p in markdown
            if p.as_posix().startswith(prefix.rstrip("/") + "/")
        )

    return {
        "root": str(root.resolve()),
        "tracked_like_files_excluding_build_and_git": len(files),
        "total_bytes": total_bytes,
        "by_extension": dict(sorted(by_extension.items())),
        "markdown_files": len(markdown),
        "markdown_words": markdown_words,
        "docs_files": sum(1 for p in files if p.parts and p.parts[0] == "docs"),
        "docs_markdown_files": len(docs_markdown),
        "docs_markdown_words": docs_markdown_words,
        "png_files": by_extension.get(".png", 0),
        "python_files": by_extension.get(".py", 0),
        "kotlin_files": by_extension.get(".kt", 0),
        "json_files": by_extension.get(".json", 0),
        "test_source_files": sum(1 for p in files if is_test_source(p)),
        "world_docs": count_docs("docs/world"),
        "system_docs": count_docs("docs/systems"),
        "asset_docs": count_docs("docs/assets"),
        "android_docs": count_docs("docs/android"),
        "context_log_docs": count_docs("docs/GAME_CONTEXT_LOGS"),
        "unreadable_markdown": unreadable_text_files,
        "notes": [
            "This tool counts local checkout files, not Git object reachability.",
            "Do not equate any one metric with owner-defined documentation targets.",
            "Executed test counts require separate test evidence; source-file count is not pass count.",
            "Asset production stage requires the asset ledger/manifests, not extension counts alone.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument("--output", help="Optional JSON output path")
    args = parser.parse_args()

    report = inventory(Path(args.root))
    payload = json.dumps(report, indent=2, sort_keys=True)

    if args.output:
        Path(args.output).write_text(payload + "\n", encoding="utf-8")
    else:
        print(payload)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

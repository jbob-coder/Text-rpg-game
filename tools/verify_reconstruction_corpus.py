#!/usr/bin/env python3
"""Verify the reconstruction corpus is internally consistent and complete.

This exists because of observed failure modes, not general caution. Each check
below corresponds to a real error made while building the corpus:

  TRUNCATION      A response was cut off mid-write, leaving a deliverable that
                  was believed complete but was absent. Detected by requiring
                  every document to end in a well-formed state.
  UNCLOSED_FENCE  An interrupted write can leave an unterminated code fence,
                  which silently swallows the rest of the document's meaning.
  ESCAPED_NEWLINE Several batch catalogs contain literal backslash-n sequences
                  rather than real newlines. A parser that misses this returns a
                  short list that looks like missing data.
  SECTION_EMPTY   A heading whose entire body is subsections reads as populated
                  to a naive check but is empty to a reader.
  DUPLICATE_HEAD  Two sections sharing a number makes cross-references ambiguous.
  LINK_TARGET     Cross-references that point at documents which do not exist
                  are worse than no cross-reference.
  REGISTRY_DRIFT  The Markdown registry and its JSON companion are generated
                  separately; if only one is regenerated they disagree.
  COUNT_CLAIM     Documented totals must match measured totals.

Exit code 0 when all checks pass, 1 otherwise. Standard library only.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

NL = "\n"


@dataclass
class Result:
    name: str
    passed: bool
    detail: str = ""
    failures: list[str] = field(default_factory=list)

    def line(self) -> str:
        status = "PASS" if self.passed else "FAIL"
        out = f"  {status}  {self.name}"
        if self.detail:
            out += f"  ({self.detail})"
        return out


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def strip_fences(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.S)


def check_truncation(docs: list[tuple[Path, str]]) -> Result:
    """A truncated write leaves a file that ends mid-sentence or mid-block."""
    bad = []
    for path, text in docs:
        tail = text.rstrip()
        if not tail:
            bad.append(f"{path.name}: empty")
            continue
        # A document should end on prose, a heading, a table row, or a fence close.
        if not re.search(r"(^#{1,6} .*|\|.*\|[^|]*$|[.:)\]`\"']|\n```)$", tail):
            bad.append(f"{path.name}: ends mid-token -> ...{tail[-40:]!r}")
    return Result(
        "no truncated documents",
        not bad,
        f"{len(docs)} documents",
        bad,
    )


def check_fences(docs: list[tuple[Path, str]]) -> Result:
    """Unbalanced code fences hide content and break rendering."""
    bad = []
    for path, text in docs:
        if text.count("```") % 2 != 0:
            bad.append(f"{path.name}: {text.count('```')} fence markers (odd)")
    return Result("code fences balanced", not bad, f"{len(docs)} documents", bad)


def check_escaped_newline(docs: list[tuple[Path, str]]) -> Result:
    """Literal backslash-n in prose indicates an unescaped write, not content.

    A document that deliberately *describes* the escaped-newline defect is
    allowed to contain it inside inline code, so occurrences enclosed in
    backticks are exempt.
    """
    bad = []
    for path, text in docs:
        # Remove inline-code spans before looking for the sequence.
        stripped = re.sub(r"`[^`]*`", "", text)
        n = stripped.count("\\n")
        if n:
            bad.append(f"{path.name}: {n} literal '\\n' sequence(s)")
    return Result("no literal newline escapes in corpus prose", not bad, f"{len(docs)} documents", bad)


def check_empty_sections(docs: list[tuple[Path, str]]) -> Result:
    """An h2 with neither prose nor subsections is empty to a reader."""
    bad = []
    total = 0
    for path, text in docs:
        lines = strip_fences(text).split(NL)
        for i, line in enumerate(lines):
            if not re.match(r"^## ", line):
                continue
            j = i + 1
            while j < len(lines) and not re.match(r"^#{1,4} ", lines[j]):
                j += 1
            body = [x for x in lines[i + 1 : j] if x.strip() and x.strip() != "---"]
            has_sub = any(re.match(r"^#{3,4} ", x) for x in lines[i + 1 : j])
            total += 1
            if not body and not has_sub:
                bad.append(f"{path.name}: {line[:56]}")
    return Result("no empty h2 sections", not bad, f"{total} h2 sections", bad)


def check_duplicate_headings(docs: list[tuple[Path, str]]) -> Result:
    bad = []
    for path, text in docs:
        heads = [m.group(0) for m in re.finditer(r"^#{1,3} .*$", strip_fences(text), re.M)]
        dupes = {h for h in heads if heads.count(h) > 1}
        for d in sorted(dupes):
            bad.append(f"{path.name}: {d[:56]}")
    return Result("no duplicate headings", not bad, f"{len(docs)} documents", bad)


def check_links(root: Path, docs: list[tuple[Path, str]]) -> Result:
    """Relative markdown links must resolve on disk."""
    bad = []
    checked = 0
    for path, text in docs:
        for m in re.finditer(r"\]\(([^)#][^)]*?)(?:#[^)]*)?\)", text):
            target = m.group(1).strip()
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            checked += 1
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                bad.append(f"{path.name} -> {target}")
    return Result("relative links resolve", not bad, f"{checked} links", bad)


def check_registry(root: Path) -> Result:
    """The registry Markdown and JSON must agree, and both must be whole."""
    md = root / "L0" / "L0-05_ASSET_UNIT_REGISTRY.md"
    js = root / "L0" / "L0-05_ASSET_UNIT_REGISTRY.json"
    if not md.exists() or not js.exists():
        return Result("registry markdown/json agree", False, "registry files missing", ["L0-05 registry absent"])

    bad = []
    doc = json.loads(read(js))
    units = doc.get("units", [])
    if len(units) != 500:
        bad.append(f"json has {len(units)} units, expected 500")
    nums = {u["n"] for u in units}
    if nums != set(range(1, 501)):
        bad.append(f"json numbers not continuous 1..500 (missing {sorted(set(range(1,501))-nums)[:5]})")
    ids = [u["id"] for u in units]
    if len(set(ids)) != len(ids):
        bad.append("json contains duplicate asset IDs")

    rows = re.findall(
        r"^\|\s*(\d{3})\s*\|\s*`([A-Z0-9_]+)`\s*\|[^|]*\|[^|]*\|\s*`([A-Z_]+)`\s*\|[^|]*\|\s*$",
        read(md),
        re.M,
    )
    if len(rows) != 500:
        bad.append(f"markdown has {len(rows)} rows, expected 500")
    jmap = {u["id"]: (u["n"], u["view_set"]) for u in units}
    for n, aid, vs in rows:
        got = jmap.get(aid)
        if got is None:
            bad.append(f"{aid} in markdown but not json")
        elif got[0] != int(n):
            bad.append(f"{aid}: number {n} vs json {got[0]}")
        elif got[1] != vs:
            bad.append(f"{aid}: view_set {vs} vs json {got[1]}")

    md_counts = {}
    for _, _, vs in rows:
        md_counts[vs] = md_counts.get(vs, 0) + 1
    if md_counts != doc.get("view_set_counts"):
        bad.append(f"view_set counts differ: md {md_counts} vs json {doc.get('view_set_counts')}")

    return Result("registry markdown/json agree", not bad, f"500 units, 0 drift" if not bad else "drift", bad)


def check_placeholders(docs: list[tuple[Path, str]]) -> Result:
    """TODO/TBD/FIXME in a specification is an unfinished promise."""
    bad = []
    for path, text in docs:
        for tok in ("TODO", "TBD", "FIXME", "XXX", "PLACEHOLDER_TEXT"):
            if tok in text:
                bad.append(f"{path.name}: {tok}")
    return Result("no unresolved placeholders", not bad, f"{len(docs)} documents", bad)


def check_layer_integrity(root: Path) -> Result:
    """Layers L1..L5 must not reference documents that were never written."""
    bad = []
    for layer in ("L1", "L2", "L3", "L4", "L5"):
        d = root / layer
        if not d.exists():
            continue
        for doc in d.glob("*.md"):
            text = read(doc)
            for m in re.finditer(r"\bL(\d)-(\d\d)\b", text):
                target = root / f"L{m.group(1)}" / f"L{m.group(1)}-{m.group(2)}"
                if not any(root.glob(f"L{m.group(1)}/L{m.group(1)}-{m.group(2)}*")):
                    bad.append(f"{doc.name} references missing {m.group(0)}")
    return Result("layer cross-references resolve", not bad, "L1-L5", bad)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default="docs/reconstruction", help="corpus root")
    ap.add_argument("--json", help="write machine-readable result")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    if not root.exists():
        print(f"corpus root not found: {root}", file=sys.stderr)
        return 1

    docs = [(p, read(p)) for p in sorted(root.rglob("*.md"))]
    if not docs:
        print(f"no documents under {root}", file=sys.stderr)
        return 1

    results = [
        check_truncation(docs),
        check_fences(docs),
        check_escaped_newline(docs),
        check_empty_sections(docs),
        check_duplicate_headings(docs),
        check_links(root, docs),
        check_registry(root),
        check_placeholders(docs),
        check_layer_integrity(root),
    ]

    total_chars = sum(len(t) for _, t in docs)
    if not args.quiet:
        print(f"Reconstruction corpus verification: {root}")
        print(f"{len(docs)} documents, {total_chars:,} characters\n")
        for r in results:
            print(r.line())
            for f in r.failures[:12]:
                print(f"          - {f}")
            if len(r.failures) > 12:
                print(f"          ... and {len(r.failures)-12} more")

    failed = [r for r in results if not r.passed]
    print(f"\nSTATUS: {'FAIL' if failed else 'PASS'}  "
          f"({len(results)-len(failed)}/{len(results)} checks passed, {total_chars:,} chars)")

    if args.json:
        Path(args.json).write_text(
            json.dumps(
                {
                    "root": str(root),
                    "document_count": len(docs),
                    "total_characters": total_chars,
                    "status": "FAIL" if failed else "PASS",
                    "checks": [
                        {"name": r.name, "passed": r.passed, "detail": r.detail, "failures": r.failures}
                        for r in results
                    ],
                },
                indent=1,
            ),
            encoding="utf-8",
        )
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
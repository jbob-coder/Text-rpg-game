from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.project_status_tracker import build_report, parse_task_register


def run_git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


class ProjectStatusTrackerTests(unittest.TestCase):
    def make_repo(self) -> tuple[tempfile.TemporaryDirectory, Path]:
        temp = tempfile.TemporaryDirectory()
        repo = Path(temp.name)
        run_git(repo, "init")
        run_git(repo, "config", "user.email", "status-test@example.invalid")
        run_git(repo, "config", "user.name", "Status Test")

        for directory in ("docs/world", "docs/evidence", "src", "android", "tests", "tools"):
            (repo / directory).mkdir(parents=True, exist_ok=True)

        (repo / "README.md").write_text("# Root\n", encoding="utf-8")
        (repo / "AGENTS.md").write_text("# Agents\n", encoding="utf-8")
        (repo / "docs" / "world" / "WORLD.md").write_text("# World\n", encoding="utf-8")
        (repo / "docs" / "evidence" / "sample.json").write_text("{}\n", encoding="utf-8")
        (repo / "src" / "game.py").write_text("VALUE = 1\n", encoding="utf-8")
        (repo / "android" / "App.kt").write_text("class App\n", encoding="utf-8")
        (repo / "tests" / "test_game.py").write_text("def test_x(): pass\n", encoding="utf-8")
        (repo / "tools" / "helper.py").write_text("VALUE = 1\n", encoding="utf-8")
        (repo / "docs" / "THE_GAME_MASTER_TASK_REGISTER.md").write_text(
            """# Tasks

### TASK D-060 — Done task
- STATUS: DONE
- PRIORITY: P0

### TASK D-061 — Active task
- STATUS: IN_PROGRESS / ACTIVE
- PRIORITY: P0

### TASK D-062 — Blocked task
- STATUS: BLOCKED
- PRIORITY: P1

### TASK D-063 — Pending task
- STATUS: PENDING
- PRIORITY: P1
""",
            encoding="utf-8",
        )
        run_git(repo, "add", ".")
        run_git(repo, "commit", "-m", "baseline")
        return temp, repo

    def test_task_parser_uses_conservative_states(self) -> None:
        tasks = parse_task_register(
            """### TASK D-001 — A
- STATUS: DONE / VERIFIED
### TASK D-002 — B
- STATUS: IN_PROGRESS / ACTIVE
### TASK D-003 — C
- STATUS: BLOCKED
### TASK D-004 — D
- STATUS: PENDING / QUEUED
### TASK D-005 — E
- STATUS: PROPOSAL_READY
"""
        )
        self.assertEqual(
            ["DONE", "IN_PROGRESS", "BLOCKED", "PENDING", "OTHER"],
            [task["state"] for task in tasks],
        )

    def test_exact_revision_report_ignores_dirty_and_untracked_files(self) -> None:
        temp, repo = self.make_repo()
        self.addCleanup(temp.cleanup)

        clean = build_report(repo, "HEAD")
        source_head = clean["source_head"]

        (repo / "docs" / "world" / "UNTRACKED.md").write_text("# noise\n", encoding="utf-8")
        (repo / "README.md").write_text("# dirty\nextra\n", encoding="utf-8")

        dirty = build_report(repo, source_head)

        self.assertEqual(clean["repository"], dirty["repository"])
        self.assertEqual(clean["documentation"], dirty["documentation"])
        self.assertEqual(clean["tasks"], dirty["tasks"])
        self.assertFalse(dirty["working_tree_included"])

    def test_report_counts_documents_and_completion(self) -> None:
        temp, repo = self.make_repo()
        self.addCleanup(temp.cleanup)

        report = build_report(repo, "HEAD")

        self.assertEqual(9, report["repository"]["tracked_files"])
        self.assertEqual(4, report["documentation"]["repository_markdown_documents"])
        self.assertEqual(2, report["documentation"]["docs_markdown_documents"])
        self.assertEqual(1, report["documentation"]["structured_docs_under_docs"])
        self.assertEqual(5, report["documentation"]["document_like_paths"])

        self.assertEqual(4, report["tasks"]["total"])
        self.assertEqual(1, report["tasks"]["done"])
        self.assertEqual(25.0, report["tasks"]["completion_pct"])

        self.assertEqual(4, report["phase1_campaign"]["total"])
        self.assertEqual(25.0, report["phase1_campaign"]["completion_pct"])

    def test_full_manifest_contains_every_tracked_path_and_classification(self) -> None:
        temp, repo = self.make_repo()
        self.addCleanup(temp.cleanup)

        report = build_report(repo, "HEAD", include_manifest=True)
        manifest = report["manifest"]

        self.assertEqual(report["repository"]["tracked_files"], len(manifest))
        by_path = {entry["path"]: entry for entry in manifest}
        self.assertEqual("document", by_path["README.md"]["kind"])
        self.assertTrue(by_path["docs/world/WORLD.md"]["document_like"])
        self.assertEqual("test", by_path["tests/test_game.py"]["kind"])
        self.assertEqual("source", by_path["src/game.py"]["kind"])
        self.assertEqual("android", by_path["android/App.kt"]["kind"])

    def test_revision_delta_tracks_documents_files_and_task_transitions(self) -> None:
        temp, repo = self.make_repo()
        self.addCleanup(temp.cleanup)
        base = run_git(repo, "rev-parse", "HEAD")

        (repo / "docs" / "world" / "NEW.md").write_text("# New\n", encoding="utf-8")
        (repo / "src" / "game.py").write_text("VALUE = 2\n", encoding="utf-8")
        task_path = repo / "docs" / "THE_GAME_MASTER_TASK_REGISTER.md"
        task_path.write_text(
            task_path.read_text(encoding="utf-8")
            .replace("- STATUS: IN_PROGRESS / ACTIVE", "- STATUS: DONE / VERIFIED")
            + """
### TASK D-064 — Newly registered
- STATUS: PENDING
- PRIORITY: P1
""",
            encoding="utf-8",
        )
        run_git(repo, "add", ".")
        run_git(repo, "commit", "-m", "second")
        source = run_git(repo, "rev-parse", "HEAD")

        report = build_report(repo, source, base_revision=base)
        delta = report["delta"]

        self.assertEqual(1, delta["documents"]["added_count"])
        self.assertIn("docs/world/NEW.md", delta["documents"]["added"])
        self.assertGreaterEqual(delta["files"]["changed_count"], 2)
        self.assertIn("src/game.py", delta["files"]["changed"])
        self.assertIn("D-064", delta["tasks"]["added_task_ids"])
        transition = next(item for item in delta["tasks"]["transitions"] if item["id"] == "D-061")
        self.assertEqual("IN_PROGRESS", transition["from_state"])
        self.assertEqual("DONE", transition["to_state"])
        self.assertGreater(delta["tasks"]["completion_pct_delta"], 0.0)


if __name__ == "__main__":
    unittest.main()

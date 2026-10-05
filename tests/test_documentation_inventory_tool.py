from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.documentation_inventory import inventory


def run_git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


class DocumentationInventoryRevisionTests(unittest.TestCase):
    def make_repo(self) -> tuple[tempfile.TemporaryDirectory, Path]:
        temp = tempfile.TemporaryDirectory()
        repo = Path(temp.name)
        run_git(repo, "init")
        run_git(repo, "config", "user.email", "inventory-test@example.invalid")
        run_git(repo, "config", "user.name", "Inventory Test")
        (repo / "docs").mkdir()
        (repo / "README.md").write_text("# Root\nroot words\n", encoding="utf-8")
        (repo / "docs" / "a.md").write_text("# A\nalpha beta\n", encoding="utf-8")
        run_git(repo, "add", ".")
        run_git(repo, "commit", "-m", "first")
        return temp, repo

    def test_dirty_and_untracked_worktree_cannot_change_revision_report(self) -> None:
        temp, repo = self.make_repo()
        self.addCleanup(temp.cleanup)
        clean = inventory(repo, "HEAD")

        (repo / "docs" / "a.md").write_text(
            "# A changed but uncommitted\nthis must not affect the report\n", encoding="utf-8"
        )
        (repo / "docs" / "untracked.md").write_text("# Untracked\nnoise\n", encoding="utf-8")
        (repo / "inventory-output.json").write_text("{}\n", encoding="utf-8")

        dirty = inventory(repo, "HEAD")
        for key in (
            "source_head",
            "tracked_files",
            "tracked_blob_bytes",
            "markdown_files",
            "markdown_words",
            "markdown_headings",
            "docs_markdown_files",
            "docs_markdown_words",
            "docs_markdown_headings",
        ):
            self.assertEqual(clean[key], dirty[key], key)
        self.assertFalse(dirty["working_tree_included"])

    def test_different_revisions_produce_distinct_correct_reports(self) -> None:
        temp, repo = self.make_repo()
        self.addCleanup(temp.cleanup)
        first = run_git(repo, "rev-parse", "HEAD")

        (repo / "docs" / "a.md").write_text("# A\nalpha beta gamma delta\n## Child\n", encoding="utf-8")
        (repo / "docs" / "b.md").write_text("# B\nsecond file\n", encoding="utf-8")
        run_git(repo, "add", ".")
        run_git(repo, "commit", "-m", "second")
        second = run_git(repo, "rev-parse", "HEAD")

        old_report = inventory(repo, first)
        new_report = inventory(repo, second)

        self.assertEqual(first, old_report["source_head"])
        self.assertEqual(second, new_report["source_head"])
        self.assertEqual(2, old_report["markdown_files"])
        self.assertEqual(3, new_report["markdown_files"])
        self.assertEqual(2, old_report["markdown_headings"])
        self.assertEqual(4, new_report["markdown_headings"])
        self.assertLess(old_report["markdown_words"], new_report["markdown_words"])
        self.assertNotEqual(old_report["tracked_blob_bytes"], new_report["tracked_blob_bytes"])


if __name__ == "__main__":
    unittest.main()

"""Check the behaviours needed for a reliable handbook check.

These tests use temporary files and the standard library. They do not need EPSM
packages, GitHub access, a database or EnergyPlus.
"""

from __future__ import annotations

import io
import json
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch

from scripts import check_docs


class DocumentationChecks(unittest.TestCase):
    """A broken example or local reference should fail with a useful message."""

    def check_fixture(self, files: dict[str, str]) -> tuple[int, str, str]:
        """Run the checker against a small, isolated example repository."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name, content in files.items():
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
            stdout = io.StringIO()
            stderr = io.StringIO()
            with patch.object(check_docs, "ROOT", root):
                with redirect_stdout(stdout), redirect_stderr(stderr):
                    status = check_docs.main()
            return status, stdout.getvalue(), stderr.getvalue()

    def test_missing_local_file_is_reported(self) -> None:
        status, _, errors = self.check_fixture({"README.md": "[Guide](missing.md)"})
        self.assertEqual(status, 1)
        self.assertIn("missing link target", errors)

    def test_missing_heading_is_reported(self) -> None:
        status, _, errors = self.check_fixture(
            {
                "README.md": "[Guide](guide.md#missing-section)",
                "guide.md": "# Existing section\n",
            }
        )
        self.assertEqual(status, 1)
        self.assertIn("missing heading", errors)

    def test_invalid_python_example_is_reported(self) -> None:
        status, _, errors = self.check_fixture(
            {"README.md": "```python\nif:\n```\n"}
        )
        self.assertEqual(status, 1)
        self.assertIn("Python block", errors)

    def test_future_api_example_is_not_executed(self) -> None:
        status, _, errors = self.check_fixture(
            {
                "README.md": (
                    "Illustrative API:\n```python\n"
                    "raise RuntimeError('a design sketch must not be run')\n```\n"
                )
            }
        )
        self.assertEqual(status, 0)
        self.assertEqual(errors, "")

    def test_failed_template_doctest_is_reported(self) -> None:
        status, _, errors = self.check_fixture(
            {"docs/templates/example.py.tmpl": '"""\n>>> 2 + 2\n5\n"""\n'}
        )
        self.assertEqual(status, 1)
        self.assertIn("failed doctest examples", errors)

    def test_invalid_notebook_json_is_reported(self) -> None:
        status, _, errors = self.check_fixture({"examples/01_example.ipynb": "not JSON"})
        self.assertEqual(status, 1)
        self.assertIn("notebook", errors.lower())

    def test_invalid_notebook_code_is_reported(self) -> None:
        content = json.dumps(
            {
                "nbformat": 4,
                "nbformat_minor": 5,
                "metadata": {"kernelspec": {"name": "python3", "language": "python"}},
                "cells": [
                    {
                        "cell_type": "code",
                        "metadata": {},
                        "execution_count": None,
                        "outputs": [],
                        "source": ["if:\n"],
                    }
                ],
            }
        )
        status, _, errors = self.check_fixture({"examples/01_example.ipynb": content})
        self.assertEqual(status, 1)
        self.assertIn("cell 1", errors)

    def test_valid_notebook_code_is_not_executed_by_syntax_check(self) -> None:
        content = json.dumps(
            {
                "nbformat": 4,
                "nbformat_minor": 5,
                "metadata": {"kernelspec": {"name": "python3", "language": "python"}},
                "cells": [
                    {
                        "cell_type": "code",
                        "metadata": {},
                        "execution_count": None,
                        "outputs": [],
                        "source": "raise RuntimeError('syntax check must not run this')",
                    }
                ],
            }
        )
        status, _, errors = self.check_fixture({"examples/01_example.ipynb": content})
        self.assertEqual(status, 0)
        self.assertEqual(errors, "")


if __name__ == "__main__":
    unittest.main()

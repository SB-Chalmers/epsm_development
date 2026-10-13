"""Check that the handbook examples run independently and fail clearly."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.run_examples import run_notebook


class ExampleRunnerTests(unittest.TestCase):
    """Notebook checks must not rely on earlier notebook state."""

    def write_notebook(self, path: Path, cells: list[str]) -> None:
        """Write the code cells needed for a small runner test."""
        data = {
            "cells": [
                {"cell_type": "code", "source": code} for code in cells
            ]
        }
        path.write_text(json.dumps(data), encoding="utf-8")

    def test_each_notebook_has_a_fresh_namespace(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            first = Path(directory) / "first.ipynb"
            second = Path(directory) / "second.ipynb"
            self.write_notebook(first, ["previous_notebook_value = 12"])
            self.write_notebook(second, ["assert 'previous_notebook_value' not in globals()"])
            run_notebook(first)
            run_notebook(second)

    def test_relative_input_and_original_working_folder(self) -> None:
        original_folder = Path.cwd()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "input.txt").write_text("known input", encoding="utf-8")
            notebook = root / "example.ipynb"
            self.write_notebook(
                notebook,
                ["from pathlib import Path\nassert Path('input.txt').read_text() == 'known input'"],
            )
            run_notebook(notebook)
            self.assertEqual(Path.cwd(), original_folder)

    def test_failure_names_the_cell_and_stops_later_cells(self) -> None:
        original_folder = Path.cwd()
        with tempfile.TemporaryDirectory() as directory:
            notebook = Path(directory) / "example.ipynb"
            self.write_notebook(
                notebook,
                [
                    "from pathlib import Path",
                    "raise ValueError('missing example input')",
                    "Path('should-not-exist.txt').write_text('incorrect')",
                ],
            )
            with self.assertRaisesRegex(RuntimeError, "example.ipynb, cell 2"):
                run_notebook(notebook)
            self.assertFalse((Path(directory) / "should-not-exist.txt").exists())
            self.assertEqual(Path.cwd(), original_folder)


if __name__ == "__main__":
    unittest.main()

"""Run the handbook's small plain-Python notebooks in cell order.

Each notebook gets a fresh namespace. The current folder is its own examples
folder, matching a notebook opened there. This is an offline check of the handbook
examples; it does not replace Jupyter execution for package integration notebooks.
"""

from __future__ import annotations

import json
import sys
from contextlib import chdir
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_notebook(path: Path) -> None:
    """Run a notebook's plain Python cells, stopping at the first failed cell."""
    notebook = json.loads(path.read_text(encoding="utf-8"))
    namespace = {"__name__": "__main__"}
    with chdir(path.parent):
        for index, cell in enumerate(notebook["cells"], start=1):
            if cell["cell_type"] != "code":
                continue
            source = cell["source"]
            if isinstance(source, list):
                source = "".join(source)
            try:
                code = compile(source, f"{path.name}:cell-{index}", "exec")
                exec(code, namespace)
            except Exception as error:
                raise RuntimeError(f"{path.name}, cell {index}: {error}") from error


def main() -> int:
    """Run each learning notebook and return failure when any example fails."""
    notebooks = sorted((ROOT.resolve() / "examples").glob("*.ipynb"))
    if not notebooks:
        print("No example notebooks found.", file=sys.stderr)
        return 1
    failures = 0
    for path in notebooks:
        try:
            run_notebook(path)
        except Exception as error:
            print(f"ERROR: {error}", file=sys.stderr)
            failures += 1
        else:
            print(f"Passed: {path.name}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())

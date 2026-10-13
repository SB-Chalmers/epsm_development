"""Check handbook links, Python example syntax and template doctests.

Run this file with Python 3.11 or newer. The checks use only the standard library
and do not contact services or run the illustrative future EPSM APIs.
"""

from __future__ import annotations

import ast
import doctest
import json
import re
import sys
import types
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
PYTHON_BLOCK = re.compile(r"^```python\s*\n(.*?)^```\s*$", re.MULTILINE | re.DOTALL)


def heading_ids(content: str) -> set[str]:
    """Return ordinary GitHub-style heading anchors outside code blocks."""
    identifiers: set[str] = set()
    counts: dict[str, int] = {}
    in_code = False
    for line in content.splitlines():
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        heading = re.sub(r"[^\w\- ]", "", match.group(1).lower())
        slug = heading.replace(" ", "-")
        occurrence = counts.get(slug, 0)
        counts[slug] = occurrence + 1
        identifiers.add(slug if occurrence == 0 else f"{slug}-{occurrence}")
    return identifiers


def check_notebook(path: Path) -> tuple[list[str], int]:
    """Check basic notebook fields and Python syntax without running the cells."""
    failures: list[str] = []
    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        return [f"invalid notebook JSON: {error}"], 0
    if not isinstance(notebook, dict) or notebook.get("nbformat") != 4:
        return ["notebook must use nbformat 4"], 0
    metadata = notebook.get("metadata")
    if not isinstance(metadata, dict):
        return ["notebook metadata must be an object"], 0
    kernel = metadata.get("kernelspec", {})
    if not isinstance(kernel, dict) or kernel.get("language") != "python":
        failures.append("notebook must name a Python kernel")
    cells = notebook.get("cells")
    if not isinstance(cells, list):
        return ["notebook cells must be a list"], 0
    code_count = 0
    for index, cell in enumerate(cells, start=1):
        if not isinstance(cell, dict):
            failures.append(f"cell {index}: expected an object")
            continue
        kind = cell.get("cell_type")
        if kind not in {"markdown", "code", "raw"}:
            failures.append(f"cell {index}: unknown cell type")
            continue
        source = cell.get("source")
        if isinstance(source, list) and all(isinstance(line, str) for line in source):
            source = "".join(source)
        if not isinstance(source, str):
            failures.append(f"cell {index}: source must be text or a list of text lines")
            continue
        if kind == "code":
            code_count += 1
            if not isinstance(cell.get("outputs"), list):
                failures.append(f"cell {index}: outputs must be a list")
            try:
                ast.parse(source)
            except SyntaxError as error:
                failures.append(f"cell {index}: invalid Python: {error.msg}")
    return failures, code_count


def main() -> int:
    """Run the small documentation checks and report any actionable failures."""
    root = ROOT.resolve()
    failures: list[str] = []
    link_count = 0
    block_count = 0
    example_count = 0
    notebook_cell_count = 0
    markdown_files = sorted(root.rglob("*.md"))

    for path in markdown_files:
        if ".git" in path.relative_to(root).parts:
            continue
        content = path.read_text(encoding="utf-8")
        for target in LINK.findall(content):
            target = target.strip().strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            destination = (
                (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            )
            link_count += 1
            if not destination.is_relative_to(root):
                failures.append(f"{path.relative_to(root)}: link leaves the repository: {target}")
            elif not destination.exists():
                failures.append(f"{path.relative_to(root)}: missing link target: {target}")
            elif parsed.fragment and destination.suffix == ".md":
                headings = heading_ids(destination.read_text(encoding="utf-8"))
                if unquote(parsed.fragment) not in headings:
                    failures.append(f"{path.relative_to(root)}: missing heading: {target}")
        for index, block in enumerate(PYTHON_BLOCK.findall(content), start=1):
            block_count += 1
            try:
                ast.parse(block)
            except SyntaxError as error:
                failures.append(
                    f"{path.relative_to(root)}: Python block {index}: {error.msg}"
                )

    for index, path in enumerate(sorted((root / "docs" / "templates").glob("*.py.tmpl"))):
        source = path.read_text(encoding="utf-8")
        module_name = f"epsm_documentation_template_{index}"
        module = types.ModuleType(module_name)
        module.__file__ = str(path)
        sys.modules[module_name] = module
        try:
            code = compile(source, str(path), "exec")
            exec(code, module.__dict__)
            for test in doctest.DocTestFinder().find(module):
                runner = doctest.DocTestRunner()
                runner.run(test)
                outcome = runner.summarize()
                example_count += outcome.attempted
                if outcome.failed:
                    failures.append(
                        f"{path.relative_to(root)}: {outcome.failed} failed doctest examples"
                    )
        except Exception as error:
            failures.append(f"{path.relative_to(root)}: {type(error).__name__}: {error}")
        finally:
            sys.modules.pop(module_name, None)

    notebooks = sorted((root / "examples").glob("*.ipynb"))
    notebooks += sorted((root / "docs" / "templates").glob("*.ipynb.tmpl"))
    for path in notebooks:
        notebook_failures, code_count = check_notebook(path)
        notebook_cell_count += code_count
        failures.extend(
            f"{path.relative_to(root)}: {failure}" for failure in notebook_failures
        )

    if failures:
        for failure in failures:
            print(f"ERROR: {failure}", file=sys.stderr)
        return 1

    print(
        f"Passed: {len(markdown_files)} Markdown files, {link_count} local links, "
        f"{block_count} Python examples checked for syntax, "
        f"{example_count} template doctest examples, "
        f"{len(notebooks)} notebooks/templates with {notebook_cell_count} Python cells."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

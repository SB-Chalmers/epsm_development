"""Check handbook links, Python example syntax and template doctests.

Run this file with Python 3.11 or newer. The checks use only the standard library
and do not contact services or run the illustrative future EPSM APIs.
"""

from __future__ import annotations

import ast
import doctest
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


def main() -> int:
    """Run the small documentation checks and report any actionable failures."""
    root = ROOT.resolve()
    failures: list[str] = []
    link_count = 0
    block_count = 0
    example_count = 0
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

    if failures:
        for failure in failures:
            print(f"ERROR: {failure}", file=sys.stderr)
        return 1

    print(
        f"Passed: {len(markdown_files)} Markdown files, {link_count} local links, "
        f"{block_count} Python examples checked for syntax, "
        f"{example_count} template doctest examples."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

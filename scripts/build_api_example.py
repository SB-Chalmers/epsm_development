"""Render the handbook's object and I/O templates as an API reference.

Install requirements-docs.txt first. This checks documentation rendering using
standalone teaching templates; it does not test EPSM package installation.
Generated fixture code and HTML stay in the ignored build/ directory.
"""

from __future__ import annotations

import importlib.util
import os
from pathlib import Path
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    """Build the example API page and check for its expected documentation."""
    if importlib.util.find_spec("sphinx") is None:
        print(
            "Install the documentation tools with: "
            "python -m pip install -r requirements-docs.txt",
            file=sys.stderr,
        )
        return 1

    example = ROOT / "build" / "api-example"
    package = example / "epsm_handbook_example"
    docs = example / "docs"
    output = ROOT / "build" / "api-preview"
    package.mkdir(parents=True, exist_ok=True)
    docs.mkdir(exist_ok=True)
    (package / "__init__.py").write_text(
        '"""Standalone handbook templates for checking documentation."""\n',
        encoding="utf-8",
    )
    templates = ROOT / "docs" / "templates"
    shutil.copyfile(templates / "public-entity.py.tmpl", package / "entities.py")
    shutil.copyfile(templates / "io-module.py.tmpl", package / "metadata_io.py")
    shutil.copyfile(templates / "sphinx-conf.py.tmpl", docs / "conf.py")
    page = (templates / "api-reference.rst.tmpl").read_text(encoding="utf-8")
    replacements = {
        "package_name.public_module.PublicObject":
            "epsm_handbook_example.entities.BuildingSummary",
        ":members: summary, plot, view": ":members: summary",
        "package_name.io.read_value": "epsm_handbook_example.metadata_io.read_metadata",
        "package_name.io.write_value": "epsm_handbook_example.metadata_io.write_metadata",
    }
    for placeholder, public_name in replacements.items():
        if placeholder not in page:
            raise ValueError(f"API template is missing {placeholder!r}")
        page = page.replace(placeholder, public_name)
    (docs / "index.rst").write_text(page, encoding="utf-8")

    # Only this standalone template fixture uses a source import path. Package
    # documentation builds must use the installed package and its dependencies.
    environment = {
        **os.environ,
        "PYTHONPATH": str(example),
        "PYTHONDONTWRITEBYTECODE": "1",
    }
    result = subprocess.run(
        [
            sys.executable, "-m", "sphinx", "-E", "-b", "html", "-W",
            "--keep-going", str(docs), str(output),
        ],
        env=environment,
        check=False,
    )
    if result.returncode:
        return result.returncode

    html = (output / "index.html").read_text(encoding="utf-8")
    for phrase in (
        "BuildingSummary", "Parameters", "Examples", "item_count",
        "read_metadata", "write_metadata", "Inspect the full identifier",
    ):
        if phrase not in html:
            raise ValueError(f"Generated API page is missing {phrase!r}")
    print(f"Passed: API examples rendered at {output / 'index.html'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

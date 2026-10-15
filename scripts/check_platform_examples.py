"""Execute current public authoring snippets against installed EPSM packages.

This optional check excludes simulation snippets, which need explicit weather
and engine prerequisites. It never substitutes syntax checks for engine evidence.
"""

import re
from pathlib import Path


def main():
    root = Path(__file__).resolve().parents[1]
    count = 0
    for relative in ("docs/harmonisation.md", "docs/engineering-style.md"):
        for source in re.findall(r"```python\n(.*?)```", (root / relative).read_text(), re.S):
            if "from epsm import Building" not in source or ".simulate(" in source:
                continue
            exec(compile(source, relative, "exec"), {"__name__": "__main__"})
            count += 1
    if count < 2:
        raise RuntimeError("Expected public authoring examples in both guides")
    print(f"Passed {count} installed-platform authoring examples; no engines run.")


if __name__ == "__main__":
    main()

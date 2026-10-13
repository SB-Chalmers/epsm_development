# Docstring examples and API documentation

A docstring should help someone use the code. Keep the useful detail found in EPSM Core: explain the purpose, inputs, units, assumptions, returned objects and likely errors. Then show one small example that a new user can understand.

Keep this explanation beside the implementation. An API documentation tool can read those docstrings and build reference pages, so we do not have to maintain a second copy of each function description.

## Use one familiar format

Use NumPy-style docstrings across EPSM. They are readable in a source file, in Python's `help()` and in generated documentation. See the [numpydoc style guide](https://numpydoc.readthedocs.io/en/latest/format.html) for the section format.

Start with one sentence saying what the operation does. Use the sections that help explain it:

| Section | What to explain |
| --- | --- |
| `Parameters` | Accepted values, types, units, defaults and what the quantities describe |
| `Attributes` | Public state a user can inspect on a class |
| `Returns` or `Yields` | Returned type, meaning, units and whether it shares mutable data with the input |
| `Raises` | Expected failures and why they occur |
| `Notes` | Assumptions, scientific limits, changes to inputs and file or service access |
| `Examples` | A small task, complete setup and a useful result |
| `See Also` | Related public operations, where useful |
| `References` | Sources for methods, assumptions or adopted standards |

For new classes, put constructor parameters in the class docstring. Document a method's parameters on that method. Avoid repeating the same explanation in the class and `__init__` docstrings.

Use reStructuredText inside docstrings. It is the text markup read by Sphinx. Use double backticks for code names, such as ``item_count``. Use ordinary section headings with dashed underlines. Markdown fences and Markdown links belong in Markdown files, not in docstrings intended for this renderer.

## Teach one small task

Give every public operation a useful `Examples` section. For a simple attribute or alias, the class example may already show enough; link to it instead of repeating the same code.

Explain the task in a short sentence before the example. Show the setup, call the public operation and inspect a useful result. Use descriptive variables such as `building`, `weather` and `result`. Start with small known inputs and leave advanced options for a later example.

The following is the `Examples` section from the handbook's [public-object template](templates/public-entity.py.tmpl). `BuildingSummary` is an executable teaching example, not the proposed EPSM Building API. The class itself is available to its docstring examples.

```text
Examples
--------
Inspect the full identifier and the known number of parts.

>>> item = BuildingSummary("b-1", "draft", 3)
>>> details = item.summary()
>>> details["identifier"]
'b-1'
>>> details["part_count"]
3
```

In package examples that call another public name, show its public import. Include imports for helpers such as `Path`. Do not rely on earlier notebook cells, private helpers, a sibling checkout or a file that only exists on the author's computer.

Use `>>>` for the first line of a Python statement and `...` for its continuation. A line of expected output follows the statement. An assertion has no output when it passes. Python's [doctest module](https://docs.python.org/3/library/doctest.html) runs these examples and checks the shown output.

Use temporary directories for short file examples. Name and explain any real fixture, catalogue release, database release or engine version. Keep the first example offline where possible. Longer examples involving services or simulations belong in `examples/` notebooks or integration tests, with their prerequisites stated.

Choose stable output. Inspect a value or check an assertion rather than copying an entire object dump, timestamp, machine-specific path or plot image. For numerical examples, use a stated tolerance with a comparison such as `math.isclose`. Explain that tolerance when it has scientific meaning. Do not hide incorrect values behind broad output matching or skipped doctests.

A reStructuredText `Example::` block can display code but does not by itself make it a doctest. Prefer `>>>` examples when the example should be checked. Clearly label future API sketches and keep them out of runnable docstrings until the API exists.

## A small example using today's Core API

Core's existing Footprint API is a useful model for a friendly example. This checks an area and shows that scaling leaves the original unchanged:

```python
from epsm_core import Footprint

footprint = Footprint.rectangle(10, 8)
assert footprint.area_m2 == 80.0
smaller = footprint.scaled_to_area(40)
assert round(smaller.area_m2, 2) == 40.0
assert footprint.area_m2 == 80.0
```

These dimensions are in metres and the returned area is in square metres. The values are small synthetic inputs for teaching geometry; they are not observations from a national building. The calls were checked with the current local Core installation. When placing this example in a docstring, use `>>>` prompts so it can be checked as a doctest.

## Build reference pages from the source

The starting setup is Sphinx with `autodoc` and `napoleon`. Autodoc reads Python signatures and docstrings; Napoleon understands their NumPy sections. These are included Sphinx extensions, described in the [autodoc guide](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html) and [Napoleon guide](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html).

Core provides the writing style we want. It does not currently configure a Sphinx documentation build. The setup here is a new starting point for package repositories, not a claim about Core's existing build.

1. Copy the [Sphinx configuration](templates/sphinx-conf.py.tmpl) to the package's `docs/conf.py` and replace the project name.
2. Copy the [API page](templates/api-reference.rst.tmpl) to `docs/index.rst`. Replace the example module, class and function names with the package's real public names. Add separate pages when the reference grows.
3. Install the package, its required dependencies and the repository's documented documentation dependencies in a dedicated environment. Declare Sphinx in a documentation extra or requirements file, rather than as a runtime requirement.
4. Build the pages with warnings treated as errors, using that environment's Python:

```sh
python -m sphinx -b html -W --keep-going docs build/docs
```

Keep the API member list short and intentional. Document the public methods users need, rather than publishing every generated model helper. Keep getting-started pages and notebooks alongside the generated reference; an API list alone does not teach a research workflow.

Autodoc imports the package to inspect it. Imports must not query a database, fetch weather, open a preview, configure logging or start EnergyPlus. Provide the dependencies needed for the advertised API instead of making missing imports disappear through mocks.

The starter config reads constructor details from the class docstring. For existing Core classes with useful `__init__` documentation, `autoclass_content = "both"` can preserve that detail while the docstrings are brought into the shared style. Check the rendered page for repeated sections.

## Check the examples and the pages

Run small doctests in the package's ordinary test suite. For pytest, an installed module can be checked with `python -m pytest --doctest-modules --pyargs package_name.module_name`; replace the placeholder with a real module. Agree which offline modules this check covers. Service or engine examples still need their real integration checks.

Run the documentation build in CI as well. A successful HTML build checks the rendering and imports; it does not execute the examples or establish scientific accuracy. Both checks are needed. Review a generated class page and a function page when changing the configuration or docstring style.

This handbook's `scripts/check_docs.py` executes the Python template doctests. Its ordinary checks use only the standard library. The optional [API example build](../scripts/build_api_example.py) checks the starter configuration against the public-object and I/O templates; CI runs it in a separate job. Keep documentation tools optional for readers who only want to run the handbook checks.

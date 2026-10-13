# Starting templates

These files help you start a Python module or a public object in the EPSM style. They are examples to adapt, not production platform code.

| Template | What it shows |
| --- | --- |
| [Python module](python-module.py.tmpl) | Source header, useful module documentation and a logger that leaves configuration to the application |
| [Public object](public-entity.py.tmpl) | Class and method documentation, a short `repr`, and an explicit summary using information already loaded |
| [Input and output module](io-module.py.tmpl) | Reading and writing small JSON metadata files, clear errors, and operational logs |
| [Project README](project-readme.md.tmpl) | Purpose, scope, installation, public API, tests and honest project information |
| [Notebook](notebook.ipynb.tmpl) | One small teaching task, prerequisites, plain Python cells and a check of the result |
| [Sphinx configuration](sphinx-conf.py.tmpl) | Rendering NumPy docstrings from an installed package |
| [API reference page](api-reference.rst.tmpl) | A short list of public classes and functions for Sphinx to document |
| [Branch policy](branch-policy.md.tmpl) | Shared `main`/`dev` rules, feature and experiment branches, release checks and urgent fixes |

The `.tmpl` extension marks a file to adapt. Copy a Python module into the package that owns your feature and give it a `.py` name. Put an adapted notebook in `examples/` with a numbered `.ipynb` name. Use the README template for the repository's `README.md`.

## Before using a template

1. Read the [coding and documentation guidelines](../engineering-style.md#documentation-and-boilerplate) and [Writing for people](../writing-guide.md).
2. Replace the header placeholders with truthful project, license and author information.
3. Replace the instructional docstrings with the purpose, units, assumptions and examples for your actual code.
4. Write the tests for your feature before implementing its behaviour.

The public-object example uses a small `BuildingSummary` class so its inspection examples can run without a database or EnergyPlus. It does not define the future EPSM Building API or a base class that every object must inherit.

Use [the docstring guide](../docstrings-and-api-docs.md) to write small working examples and set up generated API pages. The Sphinx templates belong in the owning package's documentation directory.

Try the [learning notebooks](../../examples/README.md) to see the object and I/O templates in use. For a real package, follow [the I/O guide](../io-and-api.md), [project guide](../project-layout.md), and [notebook guide](../examples-and-use-cases.md).

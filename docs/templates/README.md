# Starting templates

These files help you start a Python module or a public object in the EPSM style. They are examples to adapt, not production platform code.

| Template | What it shows |
| --- | --- |
| [Python module](python-module.py.tmpl) | Source header, useful module documentation and a logger that leaves configuration to the application |
| [Public object](public-entity.py.tmpl) | Class and method documentation, a short `repr`, and an explicit summary using information already loaded |

The `.tmpl` extension keeps these files outside an installed Python package. Copy the pattern into the package that owns your feature and give the file a normal `.py` name.

## Before using a template

1. Read the [coding and documentation guidelines](../engineering-style.md#documentation-and-boilerplate).
2. Replace the header placeholders with truthful project, license and author information.
3. Replace the instructional docstrings with the purpose, units, assumptions and examples for your actual code.
4. Write the tests for your feature before implementing its behaviour.

The public-object example uses a small `BuildingSummary` class so its inspection examples can run without a database or EnergyPlus. It does not define the future EPSM Building API or a base class that every object must inherit.

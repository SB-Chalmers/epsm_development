# Small Python examples

Start here to see how the handbook's code templates behave. These notebooks use real code from this repository. They are documentation examples, not the proposed EPSM Building API or an end-to-end EPSM study.

| Notebook | What you will learn |
| --- | --- |
| [01: Object inspection](01_object_inspection.ipynb) | Print loaded metadata, inspect its complete summary, and handle unknown counts and long/control text. |
| [02: Input and output](02_input_output.ipynb) | Write and read a small example JSON file in a temporary directory, then check the overwrite rule. |

## Before running

Use Python 3.11 or newer. The code uses only the Python standard library; no EPSM package or installation extra is required. A notebook interface needs Jupyter or another compatible editor installed separately. Select its Python kernel before running.

Open the notebooks from the repository root or `examples/`. Their setup finds this checkout and uses `runpy.run_path` to load the [public-object template](../docs/templates/public-entity.py.tmpl) or the [input/output template](../docs/templates/io-module.py.tmpl). This is intentional for handbook resources. Package examples should normally import their installed public APIs.

The fixtures are small, made-up metadata records. Their source IDs are stated in the notebooks. Counts are dimensionless. No random sampling, scientific parameters, database, network access or EnergyPlus installation is involved.

The input/output notebook uses an automatically cleaned temporary directory. It does not overwrite repository files. Saved notebook outputs and execution counts start empty.

## Run and check

Use **Restart Kernel and Run All** for each notebook. Every cell should complete in order, including the assertions about the result. A missing template or unexpected overwrite behaviour is an error, not a reason to skip the example.

Before saving a change, clear all outputs and execution counts. The repository checker runs offline documentation examples; release evidence should record what actually executed.

From the repository root, `python3 scripts/run_examples.py` executes both notebooks in fresh Python namespaces without Jupyter. This is a quick offline check. It does not replace the fresh-kernel check for package integration notebooks.

Read [Examples and use cases](../docs/examples-and-use-cases.md) for the progression expected in every EPSM repository, including the later notebooks that connect packages.

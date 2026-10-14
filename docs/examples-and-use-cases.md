# Examples and use cases

Every EPSM repository keeps simple Python notebooks in `examples/`. Start with what that package does on its own. Then show how it connects to other EPSM packages. Readers should be able to run one small example before planning a larger study.

Put short examples of individual public calls in [docstrings](docstrings-and-api-docs.md). Use notebooks to explain a complete task.

Use today's public APIs in runnable examples. Keep future API ideas in clearly labelled Markdown sketches. A design sketch is not a successful integration check.

## A short progression

Number notebooks so a new reader knows where to start. Use descriptive names and keep one main question per notebook.

| Number | What to show |
| --- | --- |
| `01` | The package's main operation with one small, known input. Explain the returned object and show a useful result. |
| `02` | A complete local use case. Read or prepare input, run the operation, inspect assumptions and diagnostics, and retain output when the package writes files. |
| `03` onward | Connect to another EPSM package using its installed public API. Explain what each package contributes. |
| Later | A small study, alternatives or a batch, where these fit the package's purpose. Explain failures and resume before showing a large campaign. |

Keep the first notebooks offline where possible. Use small, made-up inputs with a stated source ID, or a small fixed fixture whose origin and release are recorded. Do not copy a national dataset into an introductory notebook.

The [handbook examples](../examples/README.md) demonstrate inspection and file handling through executable code templates. They do not run EPSM simulations or define the future EPSM interface.

## Explain the setup before the code

Each repository's `examples/README.md` lists notebooks in order and states:

- The supported Python version, exact package releases and actual installation extras. Put installation commands here, outside notebook code cells.
- How to select the notebook kernel and where to start it. State whether the notebook works from an installed package or needs repository fixtures.
- Required files, source IDs, catalogue/database releases, checksums where used, and any external service or engine version.
- Output locations, overwrite rules and the checks that can be run offline.

Each notebook starts with its goal, prerequisites, input provenance, units and expected outcome. Say when values are illustrative assumptions. Explain an area, volume or time reference alongside its unit. If no physical quantities or random sampling are used, say so; do not invent a seed or scientific source.

When randomness is needed, use an explicit local generator and record its seed. Start with a bounded case count. Do not use hidden state from another notebook.

## Keep the code easy to follow

Use short Python cells in the order a researcher would work. Show the public call, inspect its result, then check a meaningful outcome. Avoid wrappers that hide the main operation, long helper functions, shell commands, package installation cells and embedded credentials.

Use temporary directories for disposable offline examples. Show an explicit caller-owned directory when retained study outputs matter. Explain what a function reads, writes or overwrites before calling it.

Printing an object should give a short description. Use its documented inspection methods for full assumptions, evidence, unresolved requirements and diagnostics. Logs help explain execution; returned results and retained artifacts establish the outcome.

Do not copy library implementations into notebooks. If an example needs a reusable helper, implement and test it in the package, then import it. The handbook's template demonstrations use an explicit `runpy.run_path` setup because `.tmpl` files are documentation resources, not installed packages.

Use the [notebook template](templates/notebook.ipynb.tmpl) as a starting point. Replace its labelled scaffold with the actual package operation before publishing an example.

## Check a fresh run

For every notebook:

1. Start a fresh kernel with the documented environment and working directory.
2. Use **Restart Kernel and Run All**. Every code cell must succeed in order without earlier manual work.
3. Check the stated result and assertions, input/source identities, units, diagnostics and expected output files.
4. Repeat in the installed-package environment used for release checks. Ordinary package examples must not succeed only because a source checkout is on the import path.
5. Clear outputs and execution counts before committing. Preserve the execution result separately in CI or the release record.

Use small assertions about useful behaviour. Do not treat a coverage percentage, a displayed plot or a log message as proof of scientific accuracy.

## Show real package connections

Start each integration notebook by explaining the handoff: the input, its units and evidence, the collaborator that owns the next operation, and the returned result. Show a single successful case before scaling up.

For example, a catalogue notebook may use `epsm_data.Catalogue.load()` and `catalogue.for_year(...)` to inspect a selected archetype. The parametric view remains available through `load_parametric_catalogue()`. A weather notebook may call `smhi2epw.read_epw()` on a declared local fixture before generating an AMY. The [harmonisation guide](harmonisation.md) identifies the current Building API; examples must state whether they target a development branch or a released package.

An integration notebook may require EnergyPlus, a database, network access or other EPSM packages. State those requirements clearly. When the notebook supports a release promise, its dedicated release check must provide those resources and fail if they are missing. Do not catch a missing dependency and report success, silently substitute made-up results or count a skipped check as passing evidence.

Record which checks actually ran, the package and collaborator versions, and the limits of the result. Offline handbook examples demonstrate documentation behaviour; they do not establish engine interoperability, national prediction accuracy, LCA completeness or future-weather support.

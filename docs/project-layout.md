# A Clear Package Layout

Use the same familiar starting shape across EPSM packages. A new contributor should be able to find the public API, calculations, file/service access, tests and examples without learning a different layout in every repository.

This is a guide to adapt, not a requirement to create empty files or folders. Read the [engineering style](engineering-style.md) for the coding rules and the [common use cases](../use_cases/README.md) for the behaviour we want packages to support together.

## Start small

For a Python library that reads or writes data, a small repository might look like this:

```text
package-repository/
  README.md
  pyproject.toml
  LICENSE
  AGENTS.md
  src/
    package_name/
      __init__.py
      io.py
      domain.py
  tests/
    unit/
    integration/
    fixtures/
  docs/
  examples/
    README.md
    01_basic_use.ipynb
    02_inputs_outputs.ipynb
    03_package_handoff.ipynb
  data/
  output/
```

Use only the parts the package needs. A few tests can live directly in `tests/`; create `unit/` and `integration/` when that split helps people run real groups of tests. Add examples, fixtures and data only when there is something useful to put there.

`domain.py` is one option for a small set of related objects. Use focused modules such as `geometry.py`, `records.py` or `results.py` when they make the responsibilities clearer. A large package can grow focused subpackages; it does not need a framework before its first feature.

### What belongs where

| Place | Purpose |
| --- | --- |
| `__init__.py` | A small, advertised public interface; importing it does not fetch data, configure logging or run a study |
| `io.py` | Reading/writing files, querying services and translating external formats at this package's boundary |
| `plotting.py` or `visualization/` | Render the package's own objects using the shared plot and preview conventions |
| Domain or focused modules | Objects, rules and calculations that belong to the package |
| `tests/` | Tests of that package's behaviour, including its real collaborators where needed |
| `tests/fixtures/` | Small known inputs, with provenance and permission to store them |
| `docs/` | API explanations, design notes, operations and validation limits |
| `examples/` | Simple Python notebooks that teach the public API, followed by examples using other EPSM packages |
| `data/` | Explicit inputs or data locations; not a substitute for packaging required runtime resources |
| `output/` | Generated runs, exports, logs and reports, normally ignored by Git |

Most EPSM packages need an `io.py` boundary because they handle files or services. A purely numerical package may need no I/O module. Do not add an empty module to satisfy the tree. If I/O grows, split it into a focused `io/` package and keep one understandable public route.

Keep I/O separate from ordinary calculations. A method that loads an EPW or queries PostGIS says so in its name and documentation. Reading an already loaded attribute or printing an object must not quietly contact a service.

Required small catalogue files, schemas, SQL or viewer assets belong inside the installed package and its declared package data. Large licensed source releases remain outside the wheel, at documented configurable locations. Keep credentials and private source data out of Git. Explain which files are tracked, downloaded, retained externally or regenerated.

Number notebooks to show the reading order. Start with a small notebook using the package's main modules, then show inputs and outputs, then a connection to another EPSM package. Short `.py` helpers are optional when they make a notebook easier to follow. An example uses public imports, states its prerequisites and shows an outcome. It must not depend on a neighbouring checkout, hidden notebook variables or a developer's absolute file paths. Follow the [examples guide](examples-and-use-cases.md).

## Use the same branches

Each repository keeps `main` for stable releases and `dev` for shared development. Feature and experiment branches start from `dev` and return there after review and tests. A checked release moves into `main` and receives a version tag. Follow [branches and releases](branches-and-releases.md) and use the [branch-policy template](templates/branch-policy.md.tmpl).

## Explain the project before the code

Start the README with the package's purpose and the people it serves. State what it owns, what it calls elsewhere and what is outside its scope. Use the [project README template](templates/project-readme.md.tmpl), and adapt the [source templates](templates/README.md) for modules and objects.

Keep these project facts accurate:

- Repository/display name, distribution name, import name and any command names.
- Maintainer or team, contact route and truthful authorship/research attribution.
- MIT license for EPSM-owned code and documentation, actual copyright holders, separate source/third-party terms, and citation or research reference where applicable.
- Version and release status, with one source of truth for the package version.
- Supported Python version, required dependencies and optional features/extras.
- Public API, installation route, example inputs and validation limits.

`pyproject.toml` holds build and package metadata. Declare the name, purpose, version source, Python requirement, dependencies, optional dependencies, entrypoints and packaged resources there. Declare the MIT license and license files using the supported metadata fields; follow [the licensing guide](licensing.md). Supply the README, maintainers/contact and project URLs using the supported fields. Use truthful authorship, citation and supported Python information. Preserve separate licenses where the package includes third-party material.

Keep metadata and the README consistent. Use exact versions of the other packages when running integration tests so the checks can be repeated. Explain which version ranges the reusable library supports and why. Optional database, engine, plotting and weather features should have declared installation extras rather than imports that unexpectedly fail during basic use.

## Test packages separately, then test them together

Each package owns its unit tests, numerical reference checks and relevant integration tests. Its CI checks supported Python versions, installation and packaged resources. Test from a built wheel in a clean environment so files available only in the repository cannot hide a packaging problem.

The EPSM umbrella tests common use cases with actual installed collaborating packages. These tests check that passing data between packages preserves records, assumptions, units, calendars and error details, along with the identifiers that link results to their runs and inputs. These tests do not replace the owner's tests. Use real EnergyPlus/PostGIS/weather artifacts when their behaviour is the subject of the test; small offline tests can exercise other routes and failure handling.

Publish which package combination was tested and what prerequisites it used. A required integration that cannot run is still unverified. When an API changes, update its package tests, public examples, migration note and the affected umbrella use cases together.

The `epsm_development` handbook keeps the shared standards and use-case index. It is not another simulation library or a home for copied package tests. Named experiments and paper analyses belong in `epsm_studies`, where their research question, inputs and reproducibility record can stay together.

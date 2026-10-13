# I/O, public APIs and package handoffs

**Status:** Working draft, 13 October 2026.

This page helps you decide where reading, writing and conversion code belongs. The aim is simple: each package should work on its own, and the next package should receive an object it can understand without guessing.

These are proposed working rules for EPSM development. The package layout examples are suggestions, not a claim that today's repositories already have these modules. The accompanying [I/O template](templates/io-module.py.tmpl) is a working, standalone Python example. It is not a new EPSM API.

If you are starting a change, first read [package responsibilities](engineering-style.md#responsibility-boundaries). Then decide what your package receives, what it returns and which package owns the next step.

## A module is a file; a package groups modules

A Python **module** is normally one `.py` file. A **package** groups related modules under an import name, such as `epsm_core`. A **repository** holds the source, tests and documentation that a team develops together. The repository name and Python import name need not be identical.

A modelling package might use this layout:

```text
src/package_name/
  __init__.py       # the small, recommended public import surface
  building.py       # building objects and their rules
  geometry.py       # physical geometry calculations
  io.py             # reading and writing the package's stored formats
tests/
examples/
docs/
```

Names in this layout are examples. Choose names that explain the actual job of your module.

Keep `__init__.py` deliberate and small. Export the few stable objects or functions that most users need. Keep advanced operations in named modules. Do not use wildcard imports to expose everything, or make import order decide which implementation a user receives.

For example, a package that actually owns these classes could advertise:

```python
from .building import Building
from .results import Result

__all__ = ["Building", "Result"]
```

This illustrates an export pattern; it does not introduce those classes into the current packages. Importing the package must not open a database, read a catalogue, download weather, configure logging or launch a simulation.

## Give reading and writing a clear home

Use `io.py` for a few related readers and writers. When there are several formats, use an `io/` package with named modules such as `io/json.py` or `io/parquet.py`. Split by real needs, not by an imagined future format system.

| Put in the I/O module | Keep with the owning domain operation |
| --- | --- |
| Open the explicit file or service requested by the caller | Choose an archetype, assumptions or renovation policy |
| Decode text, bytes or rows | Calculate geometry, energy, quantities or lifecycle impacts |
| Check the stored format version and required fields | Decide how evidence and assumptions form a model |
| Call the package's existing object validation | Implement physical validation rules and their scientific meaning |
| Encode the package's documented file format | Schedule runs, interpret study outcomes or choose retention policy |
| Stage and publish a complete file safely | Coordinate a whole database transaction or study checkpoint |

The I/O module may call a pure validator owned by its package. It must not copy that validator or quietly fill missing fields with scientific assumptions. A reader that discovers a missing weather file must not choose another year or download a replacement behind the user's back.

Readers should return the public object the package promises, with no open file handle attached. Writers should receive that object or a documented value mapping. Raw dictionaries are appropriate where source files enter the system, but convert them into named objects before passing recurring building information between packages.

An ordinary method that shows already loaded state should do no I/O. Reading, querying, exporting and saving are explicit operations. Document their paths, service calls, validation, overwrite rules and failure behaviour.

## Pass values, not a live environment

A **handoff** is the information one package gives another. A good handoff names its type, meaning and required evidence. It must not depend on an open database connection, a notebook variable in another cell or a neighbouring source checkout.

| Information to preserve | Why it matters |
| --- | --- |
| Named input and output types | The receiving package can validate the agreed object rather than guess dictionary keys |
| Units | Metres, millimetres, joules and kWh are not interchangeable |
| Coordinate reference system (CRS), origin and orientation | Footprints and neighbours must be placed in the same physical frame |
| Area, volume and time reference bases | Atemp, gross floor area and zone area describe different quantities; weather and results must share the intended calendar |
| Missing values, conflicts and their reasons | Zero must not replace missing data, and an unresolved conflict must not disappear |
| Source links and measured/inferred/assumed status | A selected catalogue value remains an assumption, even after conversion |
| Database snapshot, catalogue release and weather content identity | Another researcher can recover the inputs used for the case |
| Stored-format version and producer package version | A reader can distinguish file compatibility from a software release |

CRS means the coordinate reference system used to interpret coordinates. A reference basis says what a value describes: for example, annual heating per square metre of heated floor area. Record that basis alongside the units.

Prefer transformations that receive values and return new values without fetching data or changing their input. Such a transformation is called **pure**. This makes it easier to test conversion separately from file access or database queries.

Keep database and service connections, including authentication, on client objects. Portable records, profiles and submitted cases hold data and safe source references. Do not save credentials, connection objects, open cursors or notebook state with them. Use stable source identifiers rather than connection URLs containing a password.

Use [Shared terms and models](terminology-and-models.md) when agreeing field meanings, model ownership and versions.

## One owner for each conversion

Within the proposed ecosystem, each source package owns its own file readers and factual definitions. The `epsm` integration layer owns conversions that assemble Database, Catalogue and Weather objects into Core inputs.

| Step | Owner |
| --- | --- |
| Source files or database rows become validated building observations | Database, including its ingestion and I/O modules |
| Catalogue files become versioned profiles, constructions, factors and measures | Catalogue |
| Provider data becomes an inspected weather artifact | Weather package |
| Building observations, chosen assumptions and weather become a Core input | EPSM integration adapter |
| A Core input becomes geometry, epJSON and interpreted simulation results | Core |
| Run results become retained study results, checkpoints and aggregate reports | Workflows |

The table defines responsibilities, not final method or type names. Core still checks the inputs it needs before running. For example, an upstream weather inspection does not remove Core's obligation to verify the file identity and simulation calendar at execution.

Keep one implementation of each integration conversion. A convenience method may call that implementation; it must not grow its own mapping or default-selection rules. Database and Catalogue remain usable without Core, and lower-level packages must not import `epsm` in return.

Inside a package, ordinary imports between its modules are fine. Between packages, import an installed, declared dependency through its supported API. Do not add a sibling repository to `sys.path`, assume `../epsm_core` exists, or import another package's private helpers. If you need an operation it does not expose, agree a public handoff with that package's owner.

## Safe file operations

Every reader or writer documents the following choices:

- The exact path or directory it uses, and whether relative paths refer to the caller's working directory.
- The file format, encoding, supported versions and the object returned.
- Whether it creates a directory. Create directories only as an explicit part of the requested operation.
- Whether an existing file is refused, replaced or deliberately merged. The default must not silently destroy existing evidence.
- Which failures leave temporary files or incomplete work, and where the caller can inspect them.

Validate and encode a new file before publishing it. Write the complete content to a temporary file in the destination directory, then publish it with an operation suited to the chosen overwrite rule. Do not expose a partially written final file.

For no-overwrite behaviour, a check such as `if not path.exists()` is insufficient: another writer could create the destination before the write. The operation that publishes the file must enforce the rule. The template uses a hard link for this and atomic replacement for explicit overwrite. If the filesystem does not support the required operation, it fails rather than falling back to a partial direct write.

An atomic file operation means readers see the old complete file or the new complete file. It is not a transaction across several files, and it does not by itself guarantee recovery after a power failure. Shared database tables use their database's transaction rules. A study checkpoint needs its own validation and completion rules; publish its completion marker only after the required artifacts have been checked.

Reject malformed input and nonfinite numbers such as NaN or infinity. Retain the original failure cause, give a useful error and leave existing evidence unchanged until publication succeeds. Do not suppress failures to make a file appear successfully loaded or saved.

Use the [shared logging fields](engineering-style.md#events-and-fields): `epsm_event`, `epsm_context` and `epsm_details`. Log counts, identifiers that are safe to share, and the locations or IDs of saved outputs. Do not log complete records or secrets. The application configures handlers; the I/O module does not. Report a failure and its traceback once, at the layer that handles it.

## Package releases and stored formats are separate

Each package may develop and release independently. Declare the dependency versions it supports, and test the combinations you advertise. EPSM does not need every package to carry the same version number.

A stored artifact has a documented format version independent of the producer's package version. Readers check it before interpreting the file. Users should be able to load a saved object through the package's public operation; they should not have to construct an internal validation schema themselves.

When a stored format changes, state which earlier versions remain readable. If a migration is needed, make it explicit and test it with fixed old files. Do not guess the version, silently reinterpret a field or automatically rewrite the user's evidence. It is acceptable to reject an unsupported experimental format with a clear explanation.

When a public API changes, explain the change and its migration separately from stored-file compatibility. An object printed by `repr()` is not a stored format. Logs, input files and result files have their own documented roles.

## Test the package alone and the connection between packages

Start behaviour changes with a failing test. The [test-driven development guide](engineering-style.md#test-driven-development) describes the sequence.

| Test | What it should establish |
| --- | --- |
| Installed package on its own | Public imports and ordinary offline operations work without a sibling checkout or undeclared dependency |
| Reader/writer round trip | Valid values, evidence and units survive saving and loading without hidden assumptions |
| Invalid and unsupported files | Bad JSON, wrong types, duplicate fields, nonfinite numbers, missing fields and unsupported versions fail clearly |
| Write failures and overwrite | Old files survive rejected writes; explicit replacement works; temporary files are handled as documented |
| Pure conversions | Source objects remain unchanged; units, CRS, reference bases and evidence are preserved or deliberately converted |
| Cross-package agreement | Real exported objects from the producer are accepted by the consumer for the advertised dependency versions |
| Portable case bundle | A fresh process can load the prepared case without the author's notebook, credentials or live connections |
| Real engine or database check | The behaviour controlled by that dependency works with declared versions and fixed inputs |

Keep fast tests independent of services. Use mocks to exercise I/O failures, but do not mock away the actual conversion in a test of a package handoff. Integration tests use representative fixed inputs and preserve their release identities.

Mark engine, database, network and slow tests. A missing service may skip an optional development check; it must fail a release gate that requires that check. Report the command, versions, pass/fail/skip counts and the limits of the evidence.

Tests shared by two packages check that the object returned by one can be used by the other. Keep them small and agree them with both package owners. One successful end-to-end example does not replace either package's own tests.

## Each repository teaches its own public API

Each package repository should include a short introduction, executable examples and notebooks using its public API. These help developers test the package independently before connecting it to EPSM.

Start with an offline example wherever the package supports one. Show reading/writing when the package owns a file format. Include a separate integration example when an engine, database or service is needed, with the exact prerequisites stated.

Run notebooks from a fresh kernel against an installed package. Do not hide a sibling import path in a setup cell. Use small declared fixtures, explicit output directories and fixed catalogue/data releases. Saved output alone does not show that the current notebook works.

Keep reusable implementation in the package. Examples and notebooks call it; they do not copy another reader, converter or physics calculation. Label future API sketches clearly and exclude them from claims of executable coverage.

## Try the standalone template

The template contains `read_metadata(path)` and `write_metadata(metadata, path, overwrite=False)`. They read and write exactly three example fields: `format_version`, `identifier` and `item_count`. This small file format has no physical units, assumptions or EPSM model.

From this handbook repository's root, this code runs using only Python's standard library:

```python
from pathlib import Path
from tempfile import TemporaryDirectory
import runpy

operations = runpy.run_path("docs/templates/io-module.py.tmpl")
read_metadata = operations["read_metadata"]
write_metadata = operations["write_metadata"]

with TemporaryDirectory() as directory:
    path = Path(directory) / "metadata.json"
    original = {"format_version": 1, "identifier": "offline-example", "item_count": 2}
    write_metadata(original, path)
    restored = read_metadata(path)
    assert restored == original
```

Its doctests also cover refused overwrite, explicit replacement, malformed/nonfinite JSON, unsupported versions, missing directories and a failed publication that preserves old content. The handbook checks run these examples. They establish the template's behaviour, not a live Database-to-Core integration.

When adopting the template, replace its example format with the format your package owns, complete the attribution header and add that package's own tests. Keep the useful explanations and explicit failure rules. Do not turn this small example into a universal file-format framework.

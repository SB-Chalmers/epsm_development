# EPSM Engineering and API Style

**Status:** Draft v0.3

**Date:** 14 October 2026

**Audience:** Developers, researchers and coding agents contributing to EPSM

Welcome to EPSM. Our aim is to make each library easy to understand, test and use. Each part should have one clear job. Source code should explain the building and research ideas behind its calculations. Documentation, logs and printed objects should help people see what is happening during a study.

This draft sets working rules for new development and planned refactors across EPSM. Existing repositories may not meet every rule yet. Use it to plan and review a specific change; it is not a claim that the current packages already work this way.

The Building, construction, renovation and evaluation APIs described in [Harmonisation](harmonisation.md) are implemented in the coordinated package releases. Broader inspection, logging and presentation rules below remain requirements for adoption; this handbook does not claim that every existing object meets them.

The existing Core documentation shows the depth of explanation we want. Keep extensive, useful docstrings and examples. Explain the actual code, and check that examples advertised as working really run. Follow [Writing for people](writing-guide.md) when adding or reviewing text.

## Start here

If you are new to EPSM, follow this path:

1. Read [responsibility boundaries](#responsibility-boundaries) to find the package that owns your change.
2. Read [domain vocabulary](#domain-vocabulary-and-containment) and [public interface behaviour](#public-interface-behaviour) to understand the objects a researcher will use.
3. Write the expected behaviour and a failing test using [test-driven development](#test-driven-development).
4. Use [human-readable source](#human-readable-source) and [documentation and boilerplate](#documentation-and-boilerplate) while writing the implementation. Start new files and public objects from the linked templates.
5. Add the relevant [logs](#uniform-logging), [object inspection](#object-representation-and-inspection) and [error handling](#errors-and-scientific-meaning).
6. Check [repository and review conventions](#repository-and-review-conventions) before asking for review.

For practical instructions, use [project layout](project-layout.md), [I/O and package APIs](io-and-api.md), and [example notebooks](examples-and-use-cases.md). The [common use cases](../use_cases/README.md) show which behaviours package tests should cover.

Some terms used below:

- **Evidence** is a source observation or document supporting a value. **Provenance** records where a value came from, including any selection, assumption or transformation.
- A **pinned input** names a fixed release or content identity. A **snapshot** is the fixed set of inputs used for a run; later edits must not change it.
- An **artifact** is a retained file, such as weather, model inputs, diagnostics or results.
- A **contract** is a stated agreement about inputs, outputs and behaviour. A **package handoff** is where one package passes information to another.
- A **schema** describes the fields and rules of a stored or exchanged format. It is an implementation detail unless the user needs to inspect that format.
- An **entity** is a meaningful object, such as a Building or Study. An **archetype** groups documented assumptions for a type of building.
- A **fixture** is a known test input. An **invariant** is a rule that must remain true, such as conserving material mass.
- A **release gate** is a check that must pass before publishing a release. A skipped required check does not pass the gate.

## Responsibility boundaries

Write down the job of every package and module. Before adding a feature, identify its owner, the behaviour a user can observe and what is outside the change. When packages exchange data, write down what they pass. Keep each calculation or decision in one package.

| Package | Owns | Delegates |
| --- | --- | --- |
| `epsm` | Researcher-facing entities and conveniences, evidence-to-model assembly, cross-package handoffs and application logging configuration | Evidence retrieval, catalogue definitions, physical algorithms, simulation and durable study execution |
| `epsm_db` | Source ingestion, building identity, evidence linkage, normalized factual observations, provenance, coverage, validation, queries and evidence releases | Model assumptions, simulation assembly, weather generation and study execution |
| `epsm_data` | Current archetypes, shared construction classes, construction recipes, operating assumptions, material and assessment factors, measure definitions and source evidence | Individual building observations, engine-specific conversion, simulation and lifecycle calculations |
| `epsm_core` | Physical Building and elements, geometry, validation, quantities, transformations, Weather, EnergyPlus authoring, execution and result interpretation | Database access, catalogue lookup, weather acquisition, batch scheduling and study storage policy |
| `epsm_rc` | Explicit reduction of the same physical Building and reduced-order thermal calculation | Physical construction ownership, evidence retrieval, lifecycle assessment and study orchestration |
| `smhi2epw` | Provider acquisition, historical AMY generation, EPW inspection and weather provenance | Building modelling and study policy; additional weather methods require explicit future scope |
| `epsm_workflows` | Reusable experiment designs, renovation search, prepared cases, local and Slurm execution, checkpoints, attempts, failures, collection and durable study-result artifacts | Source ingestion, direct catalogue selection, physical calculations and engine compilation |
| `epsm_studies` | Generic PaperStudy protocol setup and persistence; named research records and archives | Reusable execution, parametric/GSA and renovation search in Workflows; physical calculations in their owning packages |
| `epsm_lca` | Lifecycle assessment methods and the meaning of assessment results | Physical quantities, factor catalogues and study orchestration |

These are the agreed package boundaries; the [harmonisation guide](harmonisation.md) records the current implementation. The package names were confirmed on 14 October 2026. Legacy import names remain only where a documented compatibility route is needed. Outdated named study implementations and their imports are archived under the [study archive decision](study-archive-policy.md); generic study tools remain maintained. The handbook is `epsm_development` and the web application is `epsm_studio`. AMY means actual meteorological year: weather for a selected historical year. EPW is the weather file format; epJSON and IDF are EnergyPlus building-model formats.

`epsm` calls and connects these libraries. Core imports Data’s lightweight construction classes; those imports do not load a catalogue. Database and Catalogue represent their own objects without Core or EPSM. New lower-level implementations must not depend on EPSM. Existing optional compatibility forwarders are named migration exceptions and load EPSM only when that legacy integration is requested. Workflows receives prepared cases and explicit services or evaluators.

A user-facing workflow may request records through an EPSM integration step. That does not move database retrieval or building assembly into the Workflows library.

Core and RC define their engine outputs; EPSM normalizes the common demand and delivered-energy boundary. LCA defines what an environmental assessment result means. Workflows stores study results, combines them and manages how long they are retained. Database may link published study artifacts to their buildings and evidence releases.

Do not introduce a universal `Entity` base class, a general plugin system or another shared package until two real users of that code show why it is needed. The umbrella should call the owning implementation, not copy its algorithms.

### Scope note for a change

Record the following before implementation, in the issue, design note or pull request:

```text
Owner:
User-visible behaviour:
Inputs and outputs:
Delegated responsibilities:
Excluded behaviour:
Acceptance scenarios:
Evidence and artifact changes:
```

If a change involves more than one owner, describe what passes between them and test that agreement. A test of the connection does not replace the tests within each package.

## Domain vocabulary and containment

Public interfaces use building and research concepts. A researcher should be able to start with a footprint or database record, inspect missing information and prepare the model one step at a time.

| Entity | Meaning | Contains or references |
| --- | --- | --- |
| Record | Portable building evidence from a pinned database release | Components, observations, conflicts, quality findings and evidence references |
| Footprint | An identified geometry with a coordinate reference and units | Outline, holes and disconnected parts as appropriate |
| Building | A physical research model being authored from evidence and declared assumptions | Geometry, fabric, operation, systems and provenance; EPSM adds assessment configuration and Results |
| Catalogue | The current library of sourced assumptions and definitions | Archetypes, materials, constructions, profiles and measures; evaluations save the actual values used |
| Weather | A weather artifact and its origin | Calendar, location, content identity and provenance |
| Scenario | An alternative to a baseline | An independent Building, renovation path and assumptions; dates are optional study information |
| Study | A concrete research investigation | Question, selection, scenarios, pinned inputs, workflow executions and results |
| Workflow | A reusable procedure for conducting a study or a stage | Named steps and their input/output contracts |
| Run | One requested execution using frozen inputs | Input identities, execution attempts, status, diagnostics and result/artifact references |
| Result | An outcome attributable to a run | Named metrics with units, time series, diagnostics and provenance |

A Study states what is investigated. A Workflow describes how it is carried out. A study may execute several workflows, and a workflow may be reused by several studies.

When objects contain or refer to information, preserve who or what that information describes. Several buildings may refer to one energy certificate. Do not copy the certificate's energy into each building and label those copies as independent measurements.

Every modelled quantity in a Building keeps its reference basis and its selection or assumption history. For example, an energy value per square metre must say which floor area and time period it uses.

Keep live database or service connections on client objects. Records and submitted case bundles must be usable in another process or machine. Do not save credentials, open connections or notebook state inside them.

Use [Shared terms and models](terminology-and-models.md) for the full glossary, model ownership and cross-package data rules.

## Public interface behaviour

Name objects after the concepts researchers use, and name operations with ordinary verbs. Prefer `building`, `weather`, `study`, `record` and `result` in examples. Put validation schemas, compiler objects and engine-specific names in advanced interfaces.

Teach one recommended way to do each common task. Convenience methods call the same implementation and return compatible objects. Do not maintain several competing sets of builders, retrieval helpers or wrappers for the same task.

Properties show state already available on the object. Methods perform work: retrieval, preparation, inspection that needs calculation, execution or export.

Document every method that reads files, uses the network, queries a database, writes artifacts or starts another process. This is often called input/output, or I/O. A constructor clearly named for retrieval may perform that work when documented. An ordinary constructor receiving values must not contact external services.

Let researchers inspect incomplete Buildings. Check supplied values when they enter the model. Provide an explicit check that explains what is still needed for simulation.

Simulation requires a complete, validated snapshot. The common simulation operation should create that snapshot, compile it and run it, without requiring users to perform those internal steps themselves.

For every editing operation, say whether it changes the object or returns a new one. Changing an object in place is called mutation. An editable draft is allowed, but editing it must never change an existing Run or Result. A renovation scenario keeps its baseline unchanged.

Do not describe an object as fully immutable just because it is a frozen dataclass or Pydantic model. Dictionaries and arrays inside it may still be editable.

Keep the reasons for missing, conflicting or unavailable values. Zero is a value, not a marker for missing data. Record explicit overrides and where they came from. Catalogue defaults may fill gaps, but those values remain assumptions rather than observations.

### Current Building API

These calls use the current API. `Building()` creates an empty draft; the named
illustrative preset supplies explicit teaching assumptions. A footprint or record can remain incomplete while the researcher supplies its constructions, systems and profiles.

```python
from epsm import Building
from shapely.geometry import Polygon

reference = Building(preset="illustrative-reference")
blank = Building.empty()
building = Building.from_footprint(
    Polygon([(0, 0), (20, 0), (20, 12), (0, 12)]),
    storeys=3,
    storey_height_m=2.8,
)
building.construction_set = reference.construction_set
building.facade = reference.facade
print(building.readiness("quantities"))
print(building.quantities().by_material())
```

Supply inspected weather to the calculation. It belongs to the retained evaluation, outside the physical Building snapshot. This example needs an EPW file and EnergyPlus installation; complete LCA additionally requires explicit assessment settings and factors.

```python
from epsm import Building, Weather

building = Building(preset="illustrative-reference")
weather = Weather.from_epw("weather.epw")
result = building.simulate(
    engine="energyplus", weather=weather, directory="outputs/baseline"
)
print(result.energy.annual_delivered_energy_kwh)
print(result.lca.status, result.lca.requirements)
assert building.results.latest is result
```

Use `Building.from_record(record, ...)` for evidence conversion and `baseline.renovate(*measures)` for an independent alternative. `epsm_workflows` owns prepared execution and renovation search; `epsm_studies.PaperStudy` stores a named research protocol. There is no public SimulationRequest step or `epsm.Study`/`epsm.Workflow` facade. See the [common use cases](../use_cases/README.md) and [review register](harmonisation-review.md) for the scope actually checked.

## Test-driven development

Test-driven development means writing the expected behaviour as a test before implementing it. For a new behaviour or bug fix:

1. Write a test for something a user can observe or a scientific rule that must hold.
2. Run it and confirm that it fails for the intended reason.
3. Make the smallest complete change that passes it.
4. Refactor for clarity while keeping the relevant tests passing.
5. Update examples, docstrings and input/output agreements in the same change.

Before reorganizing code without changing its behaviour, write tests that record the important current behaviour. These are called characterization tests. Keep scientific inputs the same and compare outputs with explained tolerances.

If you intend to change physics or accounting, identify that change separately from code cleanup. A tolerance must have a reason; it must not merely make a failing test pass.

When only documentation changes, check the relevant text, links and examples. Do not add artificial behaviour tests for a prose edit.

### What to test

| Layer | Required evidence |
| --- | --- |
| Pure domain behaviour | Ordinary cases, boundaries, units, missing values, invalid input and relevant invariants |
| Scientific calculations | Independently derived reference cases, conservation/accounting checks and explained tolerances |
| Entity behaviour | Containment, mutation, baseline preservation, incomplete-state handling and run snapshot isolation |
| Package handoffs | Evidence and units survive conversion; identities and returned types agree |
| I/O and execution | Malformed artifacts, unavailable collaborators, interruption, restart and retained failures |
| Logging and representation | Correct context, bounded output, no secret disclosure, no unintended I/O and no duplicate events |
| Installation and public examples | Advertised paths work from installed wheels and a fresh process or notebook kernel |

Use small, made-up inputs for fast tests. For tests that connect packages, use representative fixed inputs and record their source, release and assumptions. Test with the real engine or database when their behaviour determines the outcome.

Use `pytest` for tests, shared fixtures for known inputs, `tmp_path` for temporary files and `caplog` for captured logs.

In a unit test, a mock replaces an external service or operation so the test can control its response. Use mocks to test failures and keep unit tests independent. In an integration test, do not replace the behaviour that the test claims to verify. Expected answers must not simply repeat the implementation's calculation.

Mark tests that require `energyplus`, `postgis`, `network` or `slow` resources. Ordinary development tests must be useful offline. If a release requires an integration check, its gate must fail when the required resource is missing. A skipped test is not evidence that the connection works.

Report the command, environment and relevant engine/service versions, pass/fail/skip counts, and what those checks establish. Coverage reports show which code was exercised. A coverage percentage alone does not show that the software is correct.

For a package release, report both statement and branch coverage. Statement coverage shows which lines ran; branch coverage shows which choices, such as success and failure, were exercised. Test normal use, missing inputs, boundary values and expected failures for every new public operation. Explain meaningful gaps and keep skipped checks visible. A test that repeats the code's calculation adds little evidence.

Each package keeps its own tests and must pass them when installed on its own. The umbrella keeps tests of real package handoffs using declared versions and small, fixed inputs. Both use the [common use cases](../use_cases/README.md); one does not replace the other.

## Human-readable source

Use English `snake_case` names for modules, functions and attributes, and `PascalCase` names for public classes. Prefer building and research terms over unexplained abbreviations.

Put units in physical quantity names: `height_m`, `area_m2`, `energy_kwh` and `temperature_c`. Also explain which area, volume or time period a value refers to.

Write straightforward steps, pass dependencies explicitly, check inputs early and give each function one clear job. Split code when the jobs differ.

Avoid compressed one-line blocks, surprising changes in return type, hidden global state, imports that depend on each other in a circle, and broad exception handlers that hide failures.

Add type annotations to public inputs/outputs and important internal conversions. Use named objects for recurring building or research information. Raw source dictionaries and JSON are appropriate when importing data or storing files, provided their format and conversion are explained.

Give numerical constants names and source references. Make clear whether each value is a physical constant, an adopted standard, a provisional assumption or a study parameter. Keep expensive calculations out of properties and printed object descriptions.

Comments explain why a step exists, its assumptions, its numerical reasoning and important changes between stages. A reader should understand the code without chasing a chain of tiny helpers or first learning hidden framework rules.

## Documentation and boilerplate

Each module has a Core-style source header and an explanatory module docstring. A docstring is the quoted documentation immediately inside a module, class or function. Use the accompanying [module template](templates/python-module.py.tmpl) as the starting point.

The header records the file, purpose, MIT license identifier, actual copyright holder and author, research attribution, and truthful creation/modification dates. Follow [the shared MIT policy](licensing.md), including separate terms for source data and third-party material. Keep a short file changelog for meaningful changes; Git retains the complete history. Do not copy inaccurate authorship or invent original creation dates.

Use NumPy-style docstrings, with the sections and formatting described in the [numpydoc style guide](https://numpydoc.readthedocs.io/en/latest/format.html). EPSM also requires units, an explanation of how evidence is handled, and a description of work that changes state or reads/writes outside the object.

| Location | Required content |
| --- | --- |
| Module | Responsibility, delegated responsibilities, inputs/outputs, units, assumptions, I/O and validation boundary; meaningful example |
| Public class | Domain meaning, attributes, containment, lifecycle, mutation/ownership and a useful usage sequence |
| Public method/function | Every parameter, units and reference basis, choices/defaults, return meaning, specific failures, mutation/I/O and an example |
| Nontrivial private algorithm | Purpose, invariants, numerical/source reasoning, assumptions and consequential edge cases |

Use `Parameters`, `Attributes`, `Returns`, `Yields`, `Raises`, `Notes`, `Examples` and `References` where relevant. Explain what a default means scientifically, as well as its literal value. Do not add sections that say nothing useful just to fill the template.

Examples use public APIs and show a useful outcome or assertion. State the required fixtures, files, services, catalogue releases and engine versions.

Put a small working example in the `Examples` section of public docstrings. Use doctests for small offline examples: these run example code and check its shown output. Use executable tests or notebooks for examples that connect packages or services. Keep future API sketches labelled as illustrative; do not count them as working example coverage.

Follow [Docstring examples and API documentation](docstrings-and-api-docs.md) for friendly examples, NumPy formatting and automatic documentation generation.

Update function signatures, units, return types, examples and limitations together. Extensive documentation is valuable when it explains the actual implementation. Repeated generic text and stale examples do not meet this standard.

## Inputs outputs and package APIs

Most packages need an `io.py` module for reading and writing their data. If several file formats need separate code, use a small `io/` folder instead. A package that only calculates values does not need an empty I/O module.

Keep reading and writing separate from calculations. I/O code handles paths, text encoding, stored formats, external services and useful errors. The module that owns a calculation or model checks its physical meaning. Reading a file should not also choose assumptions, change geometry or start a simulation.

Give each package a small public API. Put the main names in `__init__.py` and explain them in its README. Other packages should use those public names rather than import private helpers or depend on a neighbouring checkout.

When one package sends a model to another, state the accepted object or file type, units, coordinate system, known/missing values, and source versions. Keep the producer's information. Put any required conversion in one named place, and test that handoff from both sides.

Use [I/O and package APIs](io-and-api.md) for the full rules and the [I/O template](templates/io-module.py.tmpl) as a starting point. The public Building API can stay simple while the packages agree how to pass information internally.

## Plots and previews

Use `.plot()` for 2D figures and `.view()` for 3D previews where meaningful. Keep rendering in a focused module in the owning package. Use the shared palette, labels and terminology. Follow [Plots and 3D previews](plotting-and-previews.md) for return types, display choices, notebook use and checks.

## Uniform logging

### Package events and application configuration

Logs describe what the software did, when it did it and which study or building was involved. All packages use Python's standard `logging` module. A module that performs meaningful operations creates its own logger:

```python
import logging

logger = logging.getLogger(__name__)
```

Logger names follow the package and module name: `epsm`, `epsm_core`, `epsm_data`, `epsm_db`, `epsm_rc`, `epsm_lca`, `epsm_workflows`, `epsm_studies` and `smhi2epw`, with module names beneath them. Compatibility modules may retain their documented legacy logger names. A library does not need the umbrella installed to emit ordinary Python logs.

A handler decides where a log goes, such as the terminal or a file. On import, a library may add one `NullHandler` at its package root; this handler emits nothing. Libraries and their ordinary public calls must not install terminal/file handlers, call `basicConfig`, force levels, create log directories or print progress.

The command-line interface (CLI), application or an explicitly invoked notebook setup configures logging. Python's [logging reference](https://docs.python.org/3.11/library/logging.html) explains how child loggers pass records to their parents, called propagation.

The umbrella will provide one explicit function for configuring logging. Its exact name is still to be designed. When the application selects this EPSM-managed setup, the default destinations are:

- An INFO console handler on stderr with short, readable messages. Stderr is the terminal stream used for status and errors, separate from command output.
- A DEBUG JSONL file handler when the caller supplies a study/output directory. JSONL stores one JSON record per line.
- Application-owned handlers shared across the package names. Disable propagation at those package roots while this setup is active, so a record is not emitted twice.
- Repeated configuration calls update or replace only EPSM-owned handlers, including their levels and destinations. Calling setup twice must not add duplicate handlers.

Leave unrelated handlers in the host application unchanged. When EPSM-managed setup is not selected, ordinary host-managed Python logging must still work.

If an existing, unmanaged handler on an EPSM logger conflicts with setup, report the conflict. Do not silently duplicate or discard its output. Standalone CLIs follow the same event and output rules in their entrypoint.

The application owns logging configuration. This must not create an import from a lower-level package back to `epsm`. During implementation, consider a shared formatter or helper only if it is needed. This reference requires common behaviour; it does not require another logging package.

### Events and fields

Each event has a readable message and a stable event name that software can recognize. Put additional fields in `extra` using `epsm_event`, `epsm_context` and `epsm_details`. These names avoid overwriting fields reserved by Python's `LogRecord`.

```python
logger.info(
    "Prepared study %s with %s cases",
    study_id,
    case_count,
    extra={
        "epsm_event": "study.prepare.completed",
        "epsm_context": {"study_id": study_id},
        "epsm_details": {"case_count": case_count},
    },
)
```

The EPSM-managed JSONL formatter writes each event in this format. `schema_version` identifies the version of the format:

```json
{
  "schema_version": 1,
  "timestamp": "2026-10-13T10:25:31.123Z",
  "level": "INFO",
  "logger": "epsm_workflows.execution",
  "event": "study.prepare.completed",
  "message": "Prepared study example with 12 cases",
  "context": {"study_id": "example"},
  "details": {"case_count": 12}
}
```

Every record includes `schema_version`, `timestamp`, `level`, `logger`, `event` and `message`. Use UTC ISO-8601 timestamps, as shown above. `context`, `details` and a structured `exception` are optional.

When writing JSON, reject nonfinite numbers such as NaN or infinity. Do not turn an arbitrary building or research object into a string just to make it fit. For third-party records without EPSM fields, use `event="python.log"` and keep their original logger and message.

Context identifies the work being logged. Include available `study_id`, `workflow_id`, `run_id`, `case_id`, `building_id`, `operation_id`, `parent_operation_id`, `stage`, `attempt`, `worker_id` and Slurm job/task identifiers. Slurm is the job scheduler used for cluster execution.

Put relevant release identities and artifact references in context or details. Omit values that are unavailable. IDs connect related events; timestamps alone cannot prove the order of events on different machines.

Use names such as `database.query.completed`, `catalogue.resolve.completed`, `weather.compile.started`, `building.assemble.completed`, `simulation.failed`, `study.checkpoint.saved` and `study.completed`. Other software may rely on these names and diagnostic codes. If they change, explain how existing consumers should migrate.

Measure elapsed time with a monotonic clock, which measures duration without being affected by a clock-time adjustment. Store it as `duration_s`.

Never log passwords, connection URLs containing credentials, access tokens, complete source records or large numerical arrays. Remove sensitive information from exception output at the layer that reports it, before publishing logs.

### Levels and coverage

| Level | Meaning |
| --- | --- |
| DEBUG | Per-case choices, conversions, cache decisions, detailed counts, timing and diagnostic context |
| INFO | Study/stage starts and completion, release selections, durable artifacts and aggregated progress |
| WARNING | Accepted but degraded/reconstructed outcomes or an explicit fallback requiring inspection |
| ERROR | An operation or case failed; include its category, identifiers and retained evidence reference |
| CRITICAL | The application cannot continue reliably, such as unavailable required checkpoint storage |

Log every important stage across the repositories: source and release selection, data validation, assumption selection, geometry preparation, compilation, weather recovery, engine execution, result extraction, scheduling, checkpoints, resume, cancellation and collection. A checkpoint is retained progress from which execution can resume. Simple accessors and arithmetic helpers need no routine INFO events.

When processing many buildings, keep per-building detail at DEBUG and report batch summaries at INFO. Report overall progress at most once every ten seconds, plus a final update.

Choose one layer to report a failure and its traceback. Other layers raise the error or add context without logging the same traceback again. Study summaries may count failures without repeating their details.

Include warnings and failures in returned diagnostics and saved operation records, using the same codes as the logs. A receipt records the outcome and evidence for an operation. Logs explain execution; result artifacts, provenance, diagnostics and checkpoints remain the source of truth.

### Processes and retained logs

For local execution in several processes, workers send log records through `QueueHandler`. One application-owned `QueueListener` receives them and writes terminal/file output. A worker must not also keep another file handler for that destination.

Pass the IDs that connect events explicitly into threads and newly started workers. Python's [logging cookbook](https://docs.python.org/3.11/howto/logging-cookbook.html) shows the queue patterns used here.

Each Slurm task writes its own JSONL file, called a log shard. Several tasks or nodes must not append to one shared log file. The coordinator records task summaries and links to these files. Collection may merge or index them, but must not claim a proven order for all events across the cluster.

Use a predictable study layout:

```text
study/
  manifest.json
  logs/
    study.jsonl
    tasks/<task-id>/attempt-<n>.jsonl
  runs/<run-id>/attempt-<n>/
    engine.stdout.log
    engine.stderr.log
    diagnostics.json
```

This layout sets a convention for logs and artifact locations. It does not define the complete result format. Keep raw engine output separate from structured application logs. Log the engine exit status and links to that output.

Keep logs with their study artifacts until an explicit retention or archive operation. If logs are rotated or deleted, the configured policy must state what is kept and record the operation. Resuming a study must preserve earlier attempts and their logs.

### Logging acceptance tests

Test normal log capture with `caplog` and check that imports create no output or files. Also test:

- Host-managed logging and repeated EPSM-managed setup without duplicate output.
- Changes to levels actually taking effect, valid JSONL records and missing optional fields.
- Context staying with the correct operation and reaching threads/workers correctly.
- Separate task log files and a failure traceback being reported once.
- Warning codes agreeing with returned diagnostics.

## Object representation and inspection

When you inspect an object in Python, its `__repr__` method supplies the text shown by `repr(object)`. Its `__str__` method supplies `str(object)` and ordinary printing. Both should help someone understand what they have.

Python's optional `reprlib` module can shorten container output; it does not define EPSM's objects. See Python's [data model](https://docs.python.org/3.11/reference/datamodel.html#object.__repr__) for these methods.

Important public objects provide the following inspection behaviour:

| Interface | Purpose | Required behaviour |
| --- | --- | --- |
| `repr(object)` | Immediate developer inspection | One line with class, useful identity, relevant composition counts and current state |
| `str(object)` | Ordinary human-readable printing | Concise description; may match repr until a distinct format is useful |
| Explicit `summary()` | Detailed inspection | Structured available metadata, assumptions, evidence, unresolved requirements and diagnostics |
| Explicit report/view method | Expanded tables or geometry | Documents any computation/I/O and its prerequisites |
| Explicit serialization | Portable retained state | Versioned contract independent of representation text |

Examples of intended representation content:

```text
Record(id='ee1d78d0…', type='multifamily', components=2, release='r1')
Building(id='ee1d78d0…', parts=2, state='incomplete', unresolved=1)
Study(name='Uddevalla baseline', buildings=120, workflows=1, state='prepared')
Workflow(name='baseline', steps=4)
Run(id='7ac2…', state='failed', attempt=2)
Result(run_id='7ac2…', hours=8760, accepted=True)
```

Use `unknown` or `not_loaded` when a count or state is unavailable. State labels describe the object's actual progress. `accepted` or `ready` must not imply that predictions have been validated against measured buildings.

Keep default representations on one line and within 160 characters. This means `len(text) <= 160` for the **final formatted text**, including quotes, escaping, separators and any ellipsis. Shorten labels and identifiers with a visible ellipsis, and show collection counts instead of their contents. Full identifiers and details remain available through attributes and explicit inspection.

Clipping a raw name to 160 characters does not enforce this limit. Quotes, backslashes, control characters and nonprinting Unicode may take more characters when formatted. Escape line breaks and other control characters so the result stays on one line. Shorten values further or omit optional fields before formatting; do not leave broken escape sequences or unmatched quotes. Test the final output with long and unusual Unicode inputs.

Printed representations use information already loaded on the object. They must not access a database, network or filesystem; compile a model; run a simulation; configure logging; or repeat an expensive calculation. They must remain useful for empty, incomplete and failed objects. They must not expose credentials or whole source records.

Replace verbose default dataclass/Pydantic representations where needed. Use `repr=False` for large or private fields. Deliberately define both repr and str behaviour, including for Pydantic objects. Changing printed text must not change serialization, equality, validation or identity hashes.

A richer notebook display is optional. If provided, it follows the same no-I/O rule, escapes displayed text and shows a bounded summary. Opening more detail remains an explicit operation.

The accompanying [public entity template](templates/public-entity.py.tmpl) demonstrates bounded repr/str and an explicit summary using loaded metadata. It is a template, not a universal base class or an implemented Building API. Any use of it must meet the final-format limit above.

Test `repr` and `str` with incomplete objects, large objects and unusual names. Check that they show useful fields, stay within the length limit, reveal no secrets and perform no I/O. Assertions should check the promised behaviour rather than incidental spaces.

## Errors and scientific meaning

Public errors name what failed and the input the user can act on. Prefer “Weather is missing for building X” over a raw schema traceback. Keep the original exception cause for debugging, plus a structured error code and context in execution records.

Explain conditions the software can recover from, fallback choices, unsupported cases and what happens when work is interrupted. Keep the source and reason for defaults and fallbacks.

Record an outcome for every attempted case. Do not silently remove failed models when reporting how many study cases succeeded or computing study totals.

Distinguish these statuses in APIs, documentation, logs and results:

- Source/evidence availability and quality.
- Model input completeness and structural validity.
- Numerical/simulation acceptance.
- Scientific prediction accuracy and validation scope.

Geometry checks, a complete weather calendar or an accepted engine run do not establish accuracy against measured buildings. Keep demand, delivered energy, electricity, costs and global warming potential (GWP) distinct. Each has its own units and describes a different physical or assessment boundary.

## Repository and review conventions

Use `main` for stable releases and `dev` as the shared home for development. Start feature and experiment branches from `dev`, review and test them, then merge them back into `dev`. Promote a tested release to `main` and tag its final commit. The [branch guide](branches-and-releases.md) explains this process, release checks and urgent fixes.

Use `src/`, `tests/`, `examples/` and `docs/` consistently. Put external inputs in explicit data/artifact locations and generated study artifacts in output directories ignored by Git. Keep research protocols with their study records.

Every repository has an `examples/` folder and a short index. Use simple Python notebooks: begin with the package's main modules, then show how it works with the other EPSM packages. Give each notebook one task, small declared inputs, plain explanations and checks of the result. Run it from a fresh kernel before publishing it. Follow [the examples guide](examples-and-use-cases.md).

Document project name, purpose, scope, supported Python version, installation, optional features, license, maintainer contact and how to cite the work. Keep the facts in the README and `pyproject.toml` consistent. The [project guide](project-layout.md) and [README template](templates/project-readme.md.tmpl) show what to include.

Include required runtime resources in the package. Test them from an installed wheel, the distributable package file, rather than relying on files available only in a source checkout.

Use Ruff for consistent formatting, import order and the project's agreed lint checks. Where it helps review, separate style-only edits from changes to calculations or behaviour.

Declare every dependency imported by an advertised feature. Put dependencies for optional features in package extras, so users can install them explicitly without making them mandatory for everyone.

A contribution is ready for review when its job is clear and limited, its tests check useful behaviour, its documentation and examples are current, important operations emit the prescribed logs, and its public objects are easy to inspect. Include evidence that package handoffs, missing-data handling and retained artifacts still work correctly.

Adopt this reference through small, named changes: one group of related objects, one operation or one package handoff at a time. Do not mix a repository-wide logging/docstring rewrite with changes to scientific behaviour.

## Extending the agreed API

The initial Building interface is agreed and implemented. For each additional geometry, system, assessment or study feature, first agree a small example covering:

- Exact public constructors, operation names and how users reach contained objects.
- How authoring edits behave and how independent scenarios are created.
- How assumptions are selected and inspected.
- How database/engine/artifact configuration is supplied.
- How checks, execution handles and result inspection appear in notebooks.

Write those examples first as small acceptance tests. Extend the agreed ownership and public operations; record any necessary compatibility change explicitly.

# EPSM Engineering and API Style

**Status:** Draft v0.1  
**Date:** 13 October 2026  
**Audience:** Developers and researchers contributing to the EPSM platform

EPSM development should produce narrowly scoped, well-tested libraries and an intuitive researcher interface. Code should explain the physical and research concepts it implements. Documentation, logs and object representations should make behaviour inspectable throughout a study.

This reference establishes engineering conventions for new development and planned refactors across the ecosystem. The public entity vocabulary is a design direction. Examples labelled **illustrative API** describe the intended experience; their constructors and method names are not yet implemented or approved contracts.

The existing Core documentation is the reference for the depth of explanation. Preserve extensive, useful docstrings and examples. Their accuracy, relevance and executability are part of code quality.

## Responsibility boundaries

Every package and module must have a written responsibility. A feature starts with an owner, observable behaviour and explicit exclusions. Shared responsibilities should be small integration contracts with one authoritative implementation.

| Package | Owns | Delegates |
| --- | --- | --- |
| `epsm` | Researcher-facing entities and conveniences, evidence-to-model assembly, cross-package handoffs and application logging configuration | Evidence retrieval, catalogue definitions, physical algorithms, simulation and durable study execution |
| `epsm_database` | Source ingestion, building identity, evidence linkage, normalized factual observations, provenance, coverage, validation, queries and evidence releases | Model assumptions, simulation assembly, weather generation and study execution |
| `epsm_catalogue` | Versioned archetypes, construction recipes, operating assumptions, material and assessment factors, measure definitions and source evidence | Individual building observations, engine-specific conversion, simulation and lifecycle calculations |
| `epsm_core` | Physical entities and algorithms, geometry, model validation, epJSON authoring and IDF export, single simulation execution, quantities, physical transformations and simulation-result interpretation | Database access, catalogue lookup, weather acquisition, batch scheduling and study storage policy |
| `smhi2epw` | Provider acquisition, historical AMY generation, EPW inspection and weather provenance | Building modelling and study policy; additional weather methods require explicit future scope |
| `epsm_workflows` | Reusable execution procedures, prepared cases, local and Slurm execution, checkpoints, attempts, failures, collection and durable study-result artifacts | Source ingestion, direct catalogue selection, physical calculations and engine compilation |
| `epsm_studies` | Named research questions, selection and calibration protocols, experiment designs, analysis and paper reports | Reusable platform implementations |
| Future `epsm_lca` | Lifecycle assessment methods and the meaning of assessment results | Physical quantities, factor catalogues and study orchestration |

`epsm` may compose these libraries. Lower-level libraries must not import `epsm`. Database and Catalogue remain usable without Core. Workflows accepts prepared cases and explicit collaborators. A user-facing workflow can request records through an EPSM integration step; that does not give the Workflows library ownership of database acquisition or model assembly.

Simulation output definitions belong to Core; assessment definitions belong to the relevant method package. Workflows owns persisted study results, their aggregation and retention. Database can index published study artifacts by building and evidence release.

Avoid universal `Entity` base classes, general plugin systems and new shared packages until two concrete consumers demonstrate the need. Reuse domain implementations rather than reproducing algorithms inside the umbrella.

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

If a change crosses owners, identify the handoff and the contract test. An integration test does not replace either owner's tests.

## Domain vocabulary and containment

Public interfaces use research and building concepts. Researchers should be able to begin with a footprint or a record, inspect incomplete information, and progressively prepare a model.

| Entity | Meaning | Contains or references |
| --- | --- | --- |
| Record | Portable building evidence from a pinned database release | Components, observations, conflicts, quality findings and evidence references |
| Footprint | An identified geometry with a coordinate reference and units | Outline, holes and disconnected parts as appropriate |
| Building | A research model being authored from evidence and declared assumptions | Geometry, fabric, operation, systems, weather reference and provenance |
| Catalogue | A versioned library of assumptions and definitions | Archetypes, materials, constructions, profiles and measures |
| Weather | A weather artifact and its origin | Calendar, location, content identity and provenance |
| Scenario | A declared alternative to a baseline | Measures, relevant dates, assumptions and an independent model revision |
| Study | A concrete research investigation | Question, selection, scenarios, pinned inputs, workflow executions and results |
| Workflow | A reusable procedure for conducting a study or a stage | Named steps and their input/output contracts |
| Run | One execution attempt using frozen inputs | Input identities, status, diagnostics and result/artifact references |
| Result | An outcome attributable to a run | Named metrics with units, time series, diagnostics and provenance |

A Study states what is investigated. A Workflow describes how it is carried out. A study may execute several workflows, and a workflow may be reused by several studies.

Containment must preserve factual ownership. Several building records can reference one certificate; certificate energy is not copied into independently measured building observations. A Building contains a modelled quantity only with its reference basis and selection or assumption history.

Keep live connections on clients. Records and submitted case bundles must remain portable and must not serialize credentials, open connections or notebook state.

## Public interface behaviour

Use domain nouns for objects and ordinary verbs for operations. Prefer `building`, `weather`, `study`, `record` and `result` in researcher examples. Validation schemas, compiler objects and engine object names belong in advanced interfaces.

Use one advertised path for each common task. Convenience entrypoints delegate to the same implementation and return compatible objects. Do not maintain several equivalent builder, fetcher and wrapper families.

Properties expose already available state. Explicit methods perform retrieval, preparation, inspection requiring computation, execution or export. Document every method that reads files, uses the network, queries a database, writes artifacts or starts a subprocess. An explicitly named retrieval constructor may perform I/O when documented; an ordinary value constructor must not contact external services.

Support incomplete Buildings for inspection. Validate supplied values as they enter the model; explain missing simulation requirements through an explicit check. Simulation requires a complete validated snapshot. Snapshot creation, compilation and execution should happen behind the common simulation operation.

Document mutation for every authoring operation. Authoring may use an editable draft, but editing that draft must never change an existing Run or Result. A renovation scenario preserves its baseline. A frozen dataclass or Pydantic model does not establish deep immutability of contained dictionaries and arrays.

Missing, conflicting and unavailable values retain their reasons. Zero is a value, not a missing-data marker. Explicit overrides remain traceable; catalogue defaults fill gaps without reclassifying assumed values as observations.

### Illustrative API

The following examples are design sketches, not executable documentation for the current packages. They should guide future acceptance tests before method names are adopted.

```python
import epsm

record = database.get_building(building_id)
building = epsm.Building.from_record(record)
building.assume(catalogue.profile("swedish-existing"))
building.weather = weather

building.view()
building.check()
result = building.simulate(output="runs/baseline")
print(result.annual.heating_demand_kwh)
```

The source-free authoring route should be similarly direct:

```python
building = epsm.Building(
    footprint=polygon,
    storeys=3,
    storey_height_m=2.8,
    use="apartments",
    construction_year=1965,
)
```

A Study and Workflow should make their relationship visible:

```python
study = epsm.Study(name="Uddevalla baseline", buildings=buildings)
workflow = epsm.Workflow.baseline(weather=weather, assumptions=profile)
execution = study.execute(workflow, output="runs/uddevalla")
results = execution.results
```

These examples leave database configuration, weather selection, execution configuration and exact constructor behaviour open for the next API design exercise. They do not imply automatic weather acquisition or successful modelling of every record.

## Test-driven development

For a new behaviour or bug fix:

1. Write a test expressing an observable requirement or scientific invariant.
2. Run it and confirm that it fails for the intended reason.
3. Implement the smallest coherent change that passes it.
4. Refactor for clarity while keeping the relevant tests passing.
5. Update examples, docstrings and contracts in the same change.

For a behaviour-preserving refactor, establish characterization tests before changing the implementation. Preserve scientific inputs and compare outputs using justified tolerances. Identify intentional physical or accounting changes separately from structural cleanup.

Documentation-only changes require documentation and example checks appropriate to their content. They do not require artificial behavioural tests.

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

Use small synthetic fixtures for fast tests. Pin representative integration fixtures, their source/release identities and the assumptions they support. Use real engine and database checks for the behaviours those collaborators actually determine.

Use `pytest`, shared fixtures, `tmp_path` and `caplog`. Mock external boundaries to exercise failures and isolate unit tests; do not mock away the behaviour an integration test claims to verify. Avoid assertions that merely reproduce the implementation.

Mark tests requiring `energyplus`, `postgis`, `network` or `slow` resources. The ordinary development suite must be useful offline. A release gate requiring an integration must fail when its prerequisite is absent. A skipped test is not evidence that the integration works.

Report the command, environment or collaborator versions, pass/fail/skip counts and acceptance boundary. Coverage reports identify gaps; a coverage percentage alone is not an acceptance criterion.

## Human-readable source

Use English `snake_case` for modules, functions and attributes, and `PascalCase` for public classes. Use domain names rather than unexplained abbreviations. Physical quantities use unit suffixes, such as `height_m`, `area_m2`, `energy_kwh` and `temperature_c`, and document area, volume and time reference bases.

Prefer straightforward control flow, explicit collaborators, early validation and cohesive functions. Split code when responsibilities differ. Avoid compressed one-line blocks, dynamic return-type tricks, hidden globals, circular imports and broad exception suppression.

Type public boundaries and important internal transformations. Use named objects for stable domain structures. Raw source dictionaries and JSON are appropriate at ingestion/artifact boundaries, where their schema and conversion are explicit.

Keep numerical constants named and sourced. Distinguish physical constants, adopted standards, provisional assumptions and study parameters. Keep expensive calculations out of property access and object representation.

Comments explain intent, assumptions, numerical reasoning and consequential stage transitions. Source should remain understandable without following a chain of tiny helpers or decoding framework conventions.

## Documentation and boilerplate

Each module has the Core-style source header and an explanatory module docstring. Use the accompanying [module template](templates/python-module.py.tmpl) as the starting point.

The header records file, purpose, project-approved license, actual copyright holder and author, research attribution, and truthful creation/modification dates. Retain a short file changelog for consequential changes. Git retains the complete history. Do not copy inaccurate authorship or invent original creation dates.

Use NumPy-style docstrings. Their sections and formatting follow the [numpydoc style guide](https://numpydoc.readthedocs.io/en/latest/format.html). EPSM additionally requires domain-specific units, evidence treatment and side-effect descriptions.

| Location | Required content |
| --- | --- |
| Module | Responsibility, delegated responsibilities, inputs/outputs, units, assumptions, I/O and validation boundary; meaningful example |
| Public class | Domain meaning, attributes, containment, lifecycle, mutation/ownership and a useful usage sequence |
| Public method/function | Every parameter, units and reference basis, choices/defaults, return meaning, specific failures, mutation/I/O and an example |
| Nontrivial private algorithm | Purpose, invariants, numerical/source reasoning, assumptions and consequential edge cases |

Use `Parameters`, `Attributes`, `Returns`, `Yields`, `Raises`, `Notes`, `Examples` and `References` where relevant. Explain a default's scientific meaning as well as its literal value. Do not add irrelevant sections just to fill a template.

Examples must use public APIs and show a useful outcome or assertion. State required fixtures, files, services, catalogue releases and engine versions. Use ordinary doctests for small offline examples and executable tests/notebooks for integration examples. Illustrative future API sketches must remain labelled and excluded from claims of executable coverage.

Update signatures, units, return types, examples and limitations together. Extensive documentation is valuable when it explains the implementation accurately. Repetitive generic text and stale examples do not meet the standard.

## Uniform logging

### Package events and application configuration

All packages use Python's standard `logging` module. Meaningful operational modules create a module logger:

```python
import logging

logger = logging.getLogger(__name__)
```

Use the package's import namespace and module children: `epsm`, `epsm_core`, `epsm_catalogue`, `epsm_database`, `epsm_workflows` and `smhi2epw`. Current package names keep their actual namespaces until a rename is implemented. Libraries do not need the umbrella installed to emit normal Python log records.

Library imports may add one `NullHandler` at their package root. Libraries and their ordinary public calls do not install console/file handlers, call `basicConfig`, force levels, create log directories or print progress. Configuration belongs to the CLI or explicitly invoked application/notebook setup. Python's [logging reference](https://docs.python.org/3.11/library/logging.html) explains logger hierarchy and propagation.

The umbrella will provide one explicit logging configuration entrypoint. Default EPSM-managed routing uses:

- An INFO console handler on stderr with short, readable messages.
- A DEBUG JSONL file handler when the caller supplies a study/output directory.
- Application-owned handlers shared across the package namespaces, with package-root propagation disabled while this managed routing is active.
- Idempotent reconfiguration that updates or replaces only EPSM-owned handlers, including levels and destinations.

Preserve unrelated host application handlers. Ordinary host-managed Python logging remains supported when EPSM-managed routing is not selected. Configuration must diagnose a conflicting unmanaged handler on an EPSM package hierarchy rather than silently create duplicate output or discard it. Standalone CLIs follow the same event and output conventions at their entrypoints.

Logging configuration is an application concern, not a new dependency from lower packages back to `epsm`. A shared formatter/helper distribution can be evaluated during implementation; this reference requires common behaviour, not a new logging package.

### Events and fields

Emit a human-readable message and stable machine-readable event name. Put additional fields in `extra` under the prefixed attributes `epsm_event`, `epsm_context` and `epsm_details`. Do not overwrite reserved `LogRecord` attributes.

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

The managed JSONL formatter normalizes each event into this versioned record shape:

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

`schema_version`, UTC ISO-8601 `timestamp`, `level`, `logger`, `event` and `message` are required. `context`, `details` and structured `exception` are optional. JSON serialization must reject nonfinite values and avoid stringifying arbitrary domain objects. Third-party records lacking EPSM fields use `event="python.log"` and retain their logger/message.

Context carries available `study_id`, `workflow_id`, `run_id`, `case_id`, `building_id`, `operation_id`, `parent_operation_id`, `stage`, `attempt`, `worker_id` and Slurm job/task identifiers. Release identities and artifact references belong in context or details when relevant. Omit unavailable values. IDs support correlation; timestamps do not establish strict ordering across machines.

Use event names such as `database.query.completed`, `catalogue.resolve.completed`, `weather.compile.started`, `building.assemble.completed`, `simulation.failed`, `study.checkpoint.saved` and `study.completed`. Treat event names and diagnostic codes as contracts; changing them requires migration notes.

Measure elapsed durations with a monotonic clock and record them as `duration_s`. Never log passwords, connection URLs containing credentials, access tokens, complete source payloads or large numerical arrays. Sanitize exception output at the reporting boundary before publishing logs.

### Levels and coverage

| Level | Meaning |
| --- | --- |
| DEBUG | Per-case choices, conversions, cache decisions, detailed counts, timing and diagnostic context |
| INFO | Study/stage starts and completion, release selections, durable artifacts and aggregated progress |
| WARNING | Accepted but degraded/reconstructed outcomes or an explicit fallback requiring inspection |
| ERROR | An operation or case failed; include its category, identifiers and retained evidence reference |
| CRITICAL | The application cannot continue reliably, such as unavailable required checkpoint storage |

Log all consequential stages across repositories: source and release selection, data validation, assumption resolution, geometry preparation, compilation, weather recovery, engine execution, result extraction, scheduling, checkpoints, resume, cancellation and collection. Pure accessors and arithmetic helpers need no routine INFO events.

High-volume per-building work uses DEBUG detail plus INFO batch summaries. Aggregate progress emits at most once every ten seconds, plus a final update. One failure boundary records the traceback; intermediate layers raise or add context without logging the same traceback again. Study summaries can count failures without repeating them.

Warnings and failures also survive in returned diagnostics and retained receipts with the same codes. Logs explain execution; result artifacts, provenance, diagnostics and checkpoints remain authoritative.

### Processes and retained logs

Local process workers send records through `QueueHandler` to one application-owned `QueueListener` that writes console and file output. A worker must not retain a second file handler for the same destination. Transfer correlation context explicitly into threads and spawned workers. Python's [logging cookbook](https://docs.python.org/3.11/howto/logging-cookbook.html) provides the underlying queue patterns.

Slurm tasks write distinct JSONL shards. Multiple tasks or nodes must not append to a common log file. The coordinator records task summaries and shard references; collection may merge or index shards without claiming a total distributed event order.

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

This is a logging/artifact layout convention, not a complete result-storage schema. Engine transcripts remain separate from structured application logs. Log exit status and transcript references.

Logs remain with their study artifacts until an explicit retention/archive operation. A configured rotation or deletion policy must declare what is retained and record that operation. Resuming a study must preserve earlier attempts and their logs.

### Logging acceptance tests

Verify normal capture with `caplog`, no import-time output/files, host-managed logging, no duplicate output after repeated managed configuration, effective level changes, valid JSONL records, missing optional fields, context isolation/transfer, distinct task shards, and once-only exception reporting. Check agreement between warning event codes and returned diagnostics.

## Object representation and inspection

Python uses the `__repr__` method through `repr(object)` for the developer representation. `__str__` controls `str(object)` and ordinary printing. The optional standard-library `reprlib` module can shorten containers; it is not the platform's object model. See Python's [data model](https://docs.python.org/3.11/reference/datamodel.html#object.__repr__) for the underlying methods.

Important public entities implement a concise representation contract:

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
Building(id='ee1d78d0…', parts=2, weather='AMY 2023', state='incomplete', unresolved=1)
Study(name='Uddevalla baseline', buildings=120, workflows=1, state='prepared')
Workflow(name='baseline', steps=4)
Run(id='7ac2…', state='failed', attempt=2)
Result(run_id='7ac2…', hours=8760, accepted=True)
```

Use `unknown` or `not_loaded` when counts/state are unavailable. State labels must describe the actual lifecycle; `accepted` or `ready` must not imply empirical validation.

Keep default representations within 160 characters; shorten labels, identifiers and collections with an explicit ellipsis. Display compact counts instead of nested payloads. Full identifiers and details remain available through attributes and explicit inspection.

Representation must use already loaded metadata. It performs no database, network or filesystem access, model compilation, simulation, logging configuration or expensive recomputation. It must remain useful for empty, incomplete and failed objects. It must not expose credentials or whole source records.

Override verbose default dataclass/Pydantic representations where necessary. Use `repr=False` for heavy/private fields. Define both repr and str deliberately, including Pydantic objects. Changing representation must not change serialization, equality, validation or identity hashes.

Notebook rich display is optional. If supplied, it follows the same no-I/O rule, escapes displayed text and shows a bounded summary. Detailed expansion remains an explicit operation.

The accompanying [public entity template](templates/public-entity.py.tmpl) demonstrates bounded repr/str and explicit summary using loaded metadata. It is an example, not a universal base class or a new production Building type.

Test informative fields and output bounds, partial/large cases, absence of sensitive values and zero I/O. Formatting assertions should target the representation contract rather than incidental whitespace.

## Errors and scientific meaning

Public errors name the failed domain operation and the actionable input. Prefer a message such as “Weather is missing for building X” over an unprocessed schema traceback. Retain the original exception cause for debugging and a structured error code/context for execution records.

Explicitly document recoverable conditions, fallbacks, unsupported cases and interruption behaviour. Defaults and fallback choices retain their source and reason. Every attempted case has an outcome; failed models are not silently removed from study denominators.

Distinguish these statuses in APIs, documentation, logs and results:

- Source/evidence availability and quality.
- Model input completeness and structural validity.
- Numerical/simulation acceptance.
- Scientific prediction accuracy and validation scope.

Geometry checks, a completed weather calendar or an accepted engine run cannot establish measured-building accuracy. Demand, delivered energy, electricity, costs and GWP retain distinct units and boundaries.

## Repository and review conventions

Use `src/`, `tests/`, `examples/` and `docs/` consistently. External input files belong in explicit data/artifact locations; generated study artifacts belong in ignored output directories. Research protocols live with their study records. Required runtime resources must be packaged and tested from installed wheels.

Use Ruff for consistent formatting/imports and the project's agreed lint rules. Keep style-only changes separate from numerical or behavioural changes when that improves review. Dependency declarations cover every import required by an advertised feature, with optional capabilities isolated in extras.

Each contribution is reviewable when its responsibility is narrow, acceptance tests are meaningful, documentation/examples are current, consequential operations emit the prescribed logs, and public entities have useful inspection. Include evidence that package handoffs, missing-data behaviour and retained artifacts remain correct.

Adopt this reference through explicit, bounded work items: one entity family, one operation or one package boundary at a time. Avoid a repository-wide logging/docstring rewrite that changes scientific behaviour along the way.

## Decisions for the next API design exercise

Before implementing the new umbrella interface, agree executable usage stories for a footprint model, a database building, an incomplete record, a small study and a renovation comparison. Settle:

- Exact public constructors, verbs and containment paths.
- How authoring edits behave and how independent scenarios are created.
- How assumptions are selected and inspected.
- How database/engine/artifact configuration is supplied.
- How checks, execution handles and result inspection appear in notebooks.

Express those stories first as small acceptance tests and examples. The conventions above constrain their implementation without prematurely fixing the full EPSM interface.

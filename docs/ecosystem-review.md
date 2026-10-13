# EPSM Ecosystem Review

**Snapshot: 13 October 2026.** This review records the state found during the ecosystem discussion and local audits. It is a starting point for shared development, not a claim that every checkout, release or scientific result has been independently validated.

EPSM is intended to become the research group's Swedish national urban building energy modelling platform. The packages already contain useful building physics, assumptions, weather processing, evidence and study machinery. The main problem is that they grew separately: several packages assemble models or interpret the same evidence, while researchers encounter different public APIs, documentation and readiness claims.

Read the [roadmap](roadmap.md) for the agreed direction and the [engineering and API style](engineering-style.md) for development conventions. That reference separates the working engineering rules from future API examples whose precise behaviour still needs to be designed.

## What exists today

| Tool | Local version | Current role and public interface | Publication check |
| --- | --- | --- | --- |
| `epsm_core` | `0.1.0.dev0` | Typed building specifications, geometry, EnergyPlus epJSON compilation, execution and results; researchers currently see considerable specification/compiler detail | PyPI JSON endpoint returned 404 |
| `epsm_data` | `0.3.0.dev1` | Parametric and layered archetypes, constructions, operating references, renovation definitions and model-facing resolvers; several object, dictionary and export interfaces coexist | PyPI JSON endpoint returned 404 |
| `epsm_workflows` | `0.1.0.dev0` | Study execution and campaign machinery, alongside growing stock, diagnosis, calibration, sensitivity and research-specific implementations | PyPI JSON endpoint returned 404 |
| `sweden-ubem` / `sweden_ubem` | `0.0.4` | PostGIS building evidence database with ingestion, linkage, assessment, queries and immutable processed selections; also includes EPSM assembly and weather adapters | PyPI JSON endpoint returned 404 |
| `smhi2epw` | `1.1.1` | SMHI historical Actual Meteorological Year generation, EPW reading and weather provenance, through `EPWConfig`, `compile_epw` and `read_epw` | Version `1.1.1` was available |

Publication status was checked on 13 October 2026 using the public PyPI endpoints for [Core](https://pypi.org/pypi/epsm_core/json), [Data](https://pypi.org/pypi/epsm_data/json), [Workflows](https://pypi.org/pypi/epsm_workflows/json) and [Sweden UBEM](https://pypi.org/pypi/sweden-ubem/json), and the [smhi2epw project](https://pypi.org/project/smhi2epw/). A 404 means the queried distribution was unavailable at that check; it does not describe repository maturity or other publication channels. An available wheel does not establish scientific validity.

There is no established public umbrella API yet. `epsm` is the chosen researcher-facing package identity. The existing database directory is named `sweden_building_combined`, while its distribution, import namespace, command and documentation use other names. This naming inconsistency is part of the cleanup.

### Local footprint and working-tree state

These are physical Python line counts, including documentation, comments and blanks. They are useful for understanding the cleanup surface, but are not direct measures of complexity.

| Checkout | Audited source footprint | Working-tree qualification |
| --- | --- | --- |
| Core | 50 files; 19,509 physical lines | Tracked tree was clean when checked |
| Data | 42 files; 8,096 physical lines | Tracked tree was clean when checked |
| Weather | 14 files; 5,263 physical lines | Tracked tree was clean when checked |
| Database | Approximately 9,843 Python lines; 620 current SQL lines and 503 historical SQL lines | No `.git` directory was available; files changed during inspection |
| Workflows | 75 source files; 24,533 physical lines | Only 14 Python files / 3,234 lines were tracked; 61 files / 21,299 lines were untracked |

Core's count includes 9,340 docstring lines, 1,072 comment lines and 2,688 blank lines, leaving about 6,409 code lines. Preserve useful explanatory documentation; deleting it to reduce line counts would not improve the library.

Workflows also had 49 example files / 16,376 lines and 64 test files / 16,701 lines, plus existing changes to its tracked README and project metadata. Its working directory is substantially larger than its committed source. Review and preserve those research additions before moving or deleting anything; the committed package alone does not describe the ecosystem currently used.

## Where responsibilities overlap

### Evidence retrieval and model assembly

The database has two reader families: `UBEM` / `Building` return dataframe views, while `fetch_record` / `fetch_records` return records and bounded collections. They query the same public projections through different implementations. The newer reader opens a transaction that cannot change data, keeps a consistent view during the request, and returns large selections in pages using a continuation cursor. The exploration interface runs SELECT queries through ordinary connections.

The database's `epsm.py` and `weather.py` contain approximately 821 lines of optional integration. They choose floor counts, basement assumptions, roof completion, ventilation, window ratios, calendars, delivery assumptions and catalogue climate classification; resolve archetypes; create Core specifications; compile and simulate; and acquire/cache weather. These are concrete modelling and application responsibilities rather than database maintenance.

Keep database-owned source units, ownership, accepted links, component/footprint evidence, conservative type inference, provenance and quality findings. Move evidence-to-model choices and package conversion into thin EPSM integration modules. The database must remain usable without Core or simulation dependencies.

Database planning also has both an older source-file path and the current database-backed path. The CLI uses the latter; older tests still exercise the former. Compare their behaviour with tests before retiring old selection code, and keep helpers still needed for ingestion.

### Assumption catalogues and physical implementation

Data currently offers several representations and model-facing handoffs, including Core/native and Honeybee-oriented conversion. Core also contains versioned operating-reference loading and application-facing helpers. Decide once which package owns a definition and which owns conversion. Catalogue definitions belong in the Catalogue; physical calculations belong in Core; conversion between them belongs in EPSM.

The Catalogue should not perform lifecycle calculations merely because it holds carbon or cost factors. Core should not acquire building evidence merely because it can model a building. Each package should expose a small useful interface and delegate the rest.

### Reusable workflows and individual research studies

Workflows contains reusable execution as well as named research procedures, calibrations, diagnostics, notebooks/examples and study-specific assumptions. Several studies have their own execution, caching and failure-handling code. Its public functions and commands therefore require different amounts of knowledge about the underlying machinery.

The reusable-looking campaign code also contains study-specific rules: its CLI fixes the Vera seed, site count and Core revision, while its weather storage assumes 8,760 rows and a 2018 calendar. These rules need to stay with that study. The general library should respect each weather artifact's declared calendar.

Move named experiments, selection protocols, analyses and publication reports to `epsm_studies`. Keep reusable preparation/execution contracts, scheduling, checkpoints, attempts, failures and collection in Workflows. Reusable code discovered inside a study should return to its proper platform owner with tests and documentation.

Do not replace the established PostGIS evidence schema with a separate starter database found in Workflows. Compare useful ideas and interfaces, then consolidate around the existing evidence implementation.

## Database readiness and reproducibility

The database already distinguishes national source import, processing and publication. It keeps certificate values attached to their certificate, records checksums and locations for original sources, identifies each component's geometry, and records assessment dates and processing rules. Published selections are kept unchanged. This is more than raw storage: it is the authoritative evidence and linkage layer.

Important limits remain. SCB income/context coverage is not uniformly national; the documented income coverage includes Uddevalla. Height coverage and publication have unresolved gates. Original LM and detailed measurement evidence may require the retained source bundle, whose files are explicitly verified. A database backup alone does not preserve all original evidence.

The current schema baseline is `0.0.4`, while the exported evidence-contract constant is `0.0.3`. Package version, physical schema baseline, public record/export contract and evidence-release identity must be documented separately. Existing names such as `national` and `uddevalla` are dataset identifiers, not enough on their own to identify a maintained sequence of releases.

The supported update direction is a shared research database with restricted read access and manually prepared evidence releases. Changed bundles, mappings or source interpretation may require a fresh backing database. Prepare the update separately from the accepted release, check it, and keep the previous release and original source files. Then explicitly select which release new queries should use by default. Resolve and pin that default before preparing a study.

The current reader directly requests catalogue metadata even though the advertised read-only role is granted only public `mart` access. Expose required release/layer metadata through public read-only projections and verify the installed reader with a restricted login.

## Documentation, installation and validation

Core's detailed docstrings are a useful reference for explaining physical meaning and constraints. Across packages, however, documentation mixes quickstarts, historical results, operational instructions and changing public APIs. The database manual begins with an older version and excludes simulation responsibilities that its newer README documents. Workflows has substantial research documentation outside its committed package.

Adopt common quickstarts, public examples, API references, operations notes, validation statements and migration notes. Preserve useful explanations while making advertised examples executable. Follow the [engineering and API style](engineering-style.md) for docstrings, logging, inspection and testing.

Installation also needs independent checks. The database locates SQL/configuration through repository-relative paths without declaring those resources as package data. Optional integration dependencies and public examples need testing from installed wheels rather than only neighbouring editable checkouts.

### Checks performed during this review

| Package | Observed test result | What it does and does not establish |
| --- | --- | --- |
| Core | 724 passed; one viewer-related failure in the sandbox; 9 skipped; 21 deselected | The sandbox denied the viewer's loopback server; this is not an established modelling failure. Omitted integrations remain explicit |
| Data | 92 passed | Evidence for the exercised catalogue/library behaviour |
| Database | 16 passed; 9 skipped | Targeted record, policy, physical-assessment, height-release and inventory checks; optional EPSM compiler integration was skipped |
| Workflows | 23 passed | Evidence for the exercised subset, not every untracked research addition |
| Weather | Collection could not complete because `pvlib` was unavailable | No passing weather-suite claim from this audit |

The database CI installs its test/notebook extras and synthetic PostGIS, but does not supply EPSM dependencies or the EPW needed by its optional assembly tests. Cross-package handoffs need a dedicated acceptance gate.

Historical completion of a 60,000-run study is documented; it was not independently rerun here. Data's Gothenburg multifamily, `SE.02` / F-ventilation / district-heat evidence reports 54 of 85 cases within 20% and a mean absolute error of 14.302 kWh/m²/year. Those results describe that cohort, configuration and accounting basis. They do not establish Swedish national accuracy, all building uses, all heating systems or renovation prediction validity.

Keep four claims separate everywhere: evidence availability, model completeness, accepted engine execution and empirical prediction accuracy. No result above establishes complete national coverage or nationally validated UBEM predictions.

## Direction agreed in the discussion

Retain separate focused packages and introduce a thin `epsm` interface. Rename Data to `epsm_catalogue` and the evidence service/library to `epsm_database`; keep `smhi2epw` as the independently useful weather tool. Adopt a clean API break with deliberate migration notes rather than maintaining every old interface.

Researchers should work with Records, Footprints, Buildings, Weather, Scenarios, Studies, Workflows, Runs and Results. Advanced users can still work directly with validation specifications. The usual researcher interface should handle validation and EnergyPlus compilation without requiring users to manage those details. Buildings contain meaningful subentities, and concise representations make incomplete and failed states inspectable. Exact constructors and mutation behaviour remain the next design exercise, not an API promised by this review.

Core owns simulation-result meaning; a future assessment package owns its assessment methods; Workflows owns durable study-result artifacts, collection and retention. Database may index published study outputs by building and evidence release. It should not become a second owner of simulation attempts or study storage.

Renovation pathways, lifecycle GWP and Pareto studies are the intended next research direction. First establish consistent quantities, scenario identity, factors, result boundaries and orchestration. TMY/future-weather methods and a separate EPSM Studio interface remain later projects with their own scope and validation.

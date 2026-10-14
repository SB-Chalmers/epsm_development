# EPSM development roadmap

**Historical planning snapshot, 13–14 October 2026, before implementation.** This page preserves the original sequence and unresolved questions. Its proposed names, APIs and statuses are superseded by the [current harmonisation guide](harmonisation.md), [file map](harmonisation-file-map.md) and [repository review register](harmonisation-review.md).

**Working direction: 13 October 2026.** This roadmap turns the [ecosystem review](ecosystem-review.md) into manageable work. It keeps useful implementations, gives each responsibility one owner and makes the platform easier for researchers and new contributors to understand.

**Naming decision: 14 October 2026.** Keep `epsm_data`, use `epsm_db` for the evidence database, `epsm_development` for this handbook and `epsm_studio` for the existing web application. The [harmonisation review](harmonisation.md) records current implementation and pending responsibility decisions.

The [engineering and API style](engineering-style.md) is the development reference. We have agreed to use objects such as Building, Study and Result. Their exact methods still need to be designed. First agree a few small working examples, then build the steps those examples need.

## Package identities and responsibilities

| Target | Purpose | Main change |
| --- | --- | --- |
| `epsm` | Researcher-facing entities and thin package integration | Introduce one understandable authoring/study interface; own conversions and evidence-to-model assembly without duplicating algorithms |
| `epsm_core` | Physical entities, geometry, specifications, compilation, single simulation execution, quantities and simulation-result interpretation | Keep the physics/engine implementation focused; move application/catalogue responsibilities to their owners |
| `epsm_data` | Versioned archetypes, constructions, operating assumptions, factors and measure definitions | Keep the package name; consolidate its representations and move engine-facing conversion to EPSM |
| `epsm_db` | Building evidence, ingestion, linkage, validation, queries and immutable evidence releases | Rename and consolidate `sweden_ubem`; preserve the existing evidence schema and remove simulation/weather dependencies |
| `smhi2epw` | Provider acquisition, historical AMY generation, EPW reading and provenance | Keep the current name and independent interface; make the EPSM handoff explicit |
| `epsm_workflows` | Reusable execution, scheduling, checkpointing, attempts, failures, collection and durable study artifacts | Accept prepared cases and explicit collaborators; move named research implementations out |
| `epsm_studies` | Named research questions, selection/calibration protocols, experiments, analysis and reports | Create the home for existing and future research studies |
| `epsm_development` | Shared developer handbook, design agreements and acceptance stories | Keep guidance consistent with the accepted package names and responsibilities |
| `epsm_studio` | Existing web application | Preserve its repository history; discuss integration with the Python platform separately |
| Future `epsm_lca` | Lifecycle assessment methods and assessment-result meaning | Introduce when its methods and input/output boundaries are agreed |

Use EPSM consistently as the umbrella identity. Align repository, distribution, import and command names during each rename. Check package/namespace availability before publishing; the intended names are not a claim of registry ownership.

Lower-level libraries must not import `epsm`. Database and Catalogue remain useful without Core. Workflows executes prepared cases rather than owning database ingestion or default selection. EPSM connects the packages and gives researchers a convenient interface. Each package still owns its calculations and data rules.

## First milestone: one working research route

Complete this milestone before a broad rewrite. Allow about **1–2 weeks** for a focused engineer to establish the initial route, depending on collaborator access and the agreed examples.

1. Freeze an agreed baseline of the existing checkouts. Preserve Workflows' modified and untracked research work, and recover or establish the database repository history. Record versions, source identities and existing acceptance fixtures.
2. Use [shared terms and model agreements](terminology-and-models.md) to agree usage stories for a footprint model, a database building, an incomplete Record, a small Study and a two-scenario renovation comparison. Settle the minimum public verbs, containment and edit behaviour through acceptance examples.
3. Build thin EPSM integration for a pinned database Record plus an explicit catalogue profile and weather artifact. Produce one native Core model without placing assumptions or engine conversion in the database.
4. Run a small prepared study through Workflows. Retain every attempt and failure, use Core's result interpretation and publish one understandable study summary with evidence/assumption identities.
5. Test the route from installed wheels with documented fixtures, then provide one executable notebook/example. Make missing information and unsupported cases visible.

The milestone is complete when a researcher can follow the advertised route without importing internal modules or manually coordinating competing adapter families. A successful example establishes that route, not national coverage or general prediction accuracy.

## Cleanup and consolidation

### Evidence database and manual releases

Consolidate retrieval around `DatabaseClient`, portable Records and an explicit release reference. Keep dataframe views as a presentation of the same reader rather than a second query implementation. Records carry factual observations, provenance and missing-data reasons; live connections remain on the client.

Preserve building/component identities, shared certificate ownership, source evidence and accepted linkage policies. Retire legacy source-file selection paths only after comparison tests show what remains equivalent. Do not redesign the PostGIS schema merely to match a duplicate database starter in Workflows.

Prepare manual updates beside the accepted release. The procedure is: acquire and checksum sources explicitly; build/import a candidate; process uniquely identified selections; validate coverage, source reconciliation and meaningful changes; back up and verify restoration; then explicitly promote the candidate. Preserve prior databases and original source assets for pinned studies and rollback.

Separate processing from promotion: current processing automatically activates a validated municipality dataset. Add an explicit promotion operation with the accepted validation report and previous-default identity. A default pointer must support the chosen national/shared release as well as municipality selections. Switching between physical shadow databases requires a release registry or configuration switch above them; the existing municipality pointer alone cannot do that.

Resolve the default once before preparing a Study. Save the exact database, source snapshot, processed dataset and processing release with the study inputs, so later queries and reruns can use the same versions. Subsequent pages, lookups and reruns use that reference even if the shared default changes.

Document package version, physical schema baseline, public record/export contract and evidence-release identity separately. Provide release details and the status of each evidence layer through public database views that restricted accounts can read. Test those accounts, include SQL and configuration files in the package, and check installation without the source repository.

The initial service is a **shared research database with read-only access and an explicit manual update runbook**. Automated acquisition, incremental refresh and a public HTTP API are outside this phase.

### Catalogue, Core and the EPSM interface

Keep the name `epsm_data` for the Catalogue and choose one advertised representation for each definition. Keep source evidence, versioned parameters, constructions, operational profiles, factors and measures there. Conversion to Core or other engines belongs in EPSM integration modules.

Keep physical geometry/quantity algorithms and simulation interpretation in Core. Move definitions and application-specific lookup to their owners without changing numerical meaning accidentally. First write tests that record the current behaviour and known reference cases. Explain intentional scientific changes separately from structural cleanup.

Expose Buildings and their geometry, fabric, operation, systems, weather and provenance through the common EPSM interface. Support inspection before all simulation requirements are known. Keep `BuildingSpec` and compiler internals available through an advanced interface; they should not dominate the ordinary researcher workflow.

Agree how users edit a Building and create independent versions before implementing the interface. A renovation scenario preserves its baseline, and submission freezes a validated model/input snapshot. Editing a Building cannot change an existing Run or Result. Avoid universal entity base classes and generic extension frameworks until concrete consumers need them.

Make package conversion thin and inspectable. Return structured assumption/assembly diagnostics, preserve evidence states, and never turn a fallback into a reported observation. Keep exact method names open until the usage stories are accepted.

### Workflows, studies and results

Separate reusable procedures from named research questions. Move calibration protocols, cohort selections, experiment assumptions, analysis and paper reports to `epsm_studies`, preserving their inputs, provenance and historical results. Extract reusable logic back into the correct platform owner with tests.

Workflows should execute prepared cases locally and through existing cluster/Slurm routes, retain attempts, support restart, collect outputs and report every attempted case. Bring the duplicate runners together around one agreement for prepared cases. Code needed to reproduce a historical study can stay with that study rather than remain part of the main public API.

Keep study-specific fields, fixed seeds and site counts with the study. General execution should use the calendar declared by its weather input, including a leap year when supported by the selected engine route. It must not silently reshape every year into 2018.

Core defines simulation metrics and their physical boundaries. A method package defines LCA or other assessment results. Workflows owns persisted study artifacts, collection, aggregation and retention; Studies owns research analysis. Database can index published outputs using building and evidence-release references. Do not store ordinary engine attempts in two competing systems.

### Run identity and safe result reuse

Record enough information to explain which results may be reused:

- **Engine execution:** compiled numerical inputs, weather content, engine and requested outputs.
- **Evaluated result:** the execution identity plus delivery/PV inputs and the implementation/dependencies that calculate those outputs.
- **Acceptance decision:** the validation and warning rules used to accept or reject the output.
- **Producer history:** the exact source and environment that produced the retained artifact.

A documentation edit should not force a numerical rerun. A changed delivery or PV model must not reuse the wrong evaluated output. When current code reads or evaluates a cached result, retain its original producer history and record the new consumer separately.

A compiled object should carry its validated inputs, report, weather reference and postprocessing inputs. Let the runner use it without compiling the same case a second time. Add a supported result loader so notebook users can reopen retained results.

### Documentation and release discipline

Adopt the shared style for useful explanatory docstrings, ordinary logging, bounded representations and explicit inspection. Preserve Core's documentation depth. Improve scope, accuracy and examples rather than chasing a smaller physical line count.

Add [docstring examples and generated API pages](docstrings-and-api-docs.md), then adopt [the common plotting and preview style](plotting-and-previews.md) through the owning renderers. Keep their public return types and display choices consistent.

Adopt [the MIT licensing policy](licensing.md) through each repository's license, metadata and truthful notices. Preserve source-data and bundled third-party terms.

Give each package a short purpose statement, working quickstart, public API guide, dependency/extras description, scoped validation statement and migration notes. Keep researcher usage separate from operations and historical acceptance reports.

Use a deliberate clean API break. Publish an old-to-new migration guide and update retained study routes; do not preserve every overlapping facade as a permanent alias. Before release, agree what each package passes to the next and test the supported combinations of installed package versions.

## Acceptance and effort

The full clean ecosystem is estimated at **40–70 focused person-days**, approximately **8–14 working weeks for one experienced engineer**. This is an engineering estimate, not a delivery guarantee. The initial working route is included. Migrating all existing studies adds roughly **3–6 weeks**, depending on how much untracked work needs preservation and how closely old numerical results must be reproduced.

For the database workstream alone, allow roughly 4–7 person-days for usable installed retrieval/integration and 10–17 days total for the consolidated shared reader and manual release lifecycle. These are part of the ecosystem estimate, not additional days to add blindly.

National source coverage, height publication, empirical validation and national import/restore machine time need separate assessment. Missing evidence cannot be resolved by API refactoring. Unsettled checkout changes and absent database history may also affect the baseline and schedule.

Acceptance should demonstrate:

- Installed public examples work from a fresh environment with declared optional collaborators.
- Database/Catalogue import and operate without simulation dependencies; lower libraries do not depend on EPSM.
- Restricted readers can inspect records and release metadata; records and case bundles contain no credentials or live connections.
- A default release switch does not affect an already pinned study; failed candidates leave the default untouched; rollback and old-source inspection work.
- Source evidence survives assembly unchanged, every override/default is inspectable, and shared certificate quantities remain shared.
- Authoring changes and scenario creation preserve baselines and submitted runs; results keep their run and input identities.
- Interrupted execution resumes with retained attempts; every selected case has an outcome, including failures.
- Package handoffs preserve units, area/volume bases, calendars, identities and result meaning.
- Logging and object inspection follow the shared style without hidden I/O or duplicate output.
- Scientific comparisons use independently justified reference cases/tolerances and report their validation scope.

## Later research stages

After the common route and quantity/result contracts are stable, add renovation measure application, lifecycle assessment and pathway/Pareto studies. Core supplies physical transformations and quantities; Catalogue supplies measure definitions and assessment factors; an LCA method package supplies calculation boundaries; Workflows orchestrates alternatives; Studies supplies research objectives and interpretation.

Historical AMY support is the current weather capability. TMY and future-weather methods need explicit methods, provenance and validation before being advertised as implemented. Keep weather generation independent of evidence retrieval and study preparation policy.

EPSM Studio is outside this roadmap. A graphical interface can later build on the same public entities and execution contracts; it should not delay agreement on their behaviour or create a second modelling implementation.

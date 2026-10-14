# Shared terms and models

The `epsm_development` handbook is the place to agree on the words we use and the information packages pass to each other. These agreements help independently developed packages work together and give researchers a familiar interface. Database refers to `epsm_db`; Catalogue refers to `epsm_data`.

**Status: proposed model agreements.** The ownership and meanings below guide the redesign. Exact class names, fields and file formats still need to be settled through small working examples. They are not a new implemented API.

## What we mean by a shared model

Agree on one physical building model owned by Core, with shared terms for evidence, assumptions, weather, execution and results. Each package implements the models it owns. EPSM connects them and provides convenient authoring operations.

The same Building can appear in a notebook, a study and a simulation. Those uses should preserve its identity and meaning. They do not all need the same fields or the same stored file. A Record describes evidence; a Building describes an authored model; compiled engine input describes an executable simulation.

Keep those relationships clear. The ordinary API should use familiar objects and verbs. Users should not have to fill in a platform-wide `Spec` before doing a small task. Advanced validation schemas can remain available where useful.

## Use these words consistently

| Term | Meaning |
| --- | --- |
| Real building | A building in the national stock, with a database identity when available |
| Record | Portable evidence about a real building from a specified database release; it may be incomplete |
| Observation | A source value with its subject, unit, reference basis and source history. A reported value is not necessarily measured or verified. |
| Evidence | An observation, document or source supporting a value or decision |
| Provenance | The history showing where information came from and how it was selected or changed |
| Certificate | An energy certificate and its observations. Several buildings may refer to one certificate. |
| Footprint | A plan outline with its coordinate system, units, holes and disconnected parts where needed |
| Building | A physical research model being authored, with geometry, fabric, operation, systems and weather |
| Assumption | A declared modelling choice, including an adopted default or override |
| Archetype | Documented assumptions for a type of building, with applicability and source references |
| Profile | A named set of assumptions or schedules; qualify the name when its purpose is unclear |
| Scenario | An alternative to a baseline, with declared changes, dates and an independent model revision |
| Evidence release | A fixed published selection of database evidence and its processing history |
| Model snapshot | A fixed version of an authored model; later edits do not change it |
| Weather | A weather file or artifact with location, calendar, source period and generation history |
| Case | One prepared study alternative, with fixed inputs and the evaluation requested |
| Study | A research investigation with its question, selection, scenarios, inputs and outcomes |
| Workflow | A reusable procedure that carries out a study or one of its stages |
| Run | One requested execution using fixed inputs |
| Attempt | One try at completing a Run; retries remain attached to the same request |
| Engine input | Core's compiled input, tied to the weather, engine and requested outputs |
| Result | An interpreted outcome linked to its execution, input identities and interpretation method |
| Artifact | A retained file, such as model input, weather, diagnostics, results or a report |
| Schema | The fields and rules of a stored or exchanged format; it has its own version |

Avoid using `component` without saying what it means. A database geometry component, a modelled building part and a construction layer are different things. Name the kind and explain their mapping. Likewise, use `evidence release`, `model snapshot` or `submitted inputs` when the word `snapshot` alone would be unclear.

Use the same names in public methods, docstrings, logs, plot legends and notebooks. Record older names in migration notes rather than introducing another synonym in each package.

## Give each model one owner

| Information | Owner | Must preserve |
| --- | --- | --- |
| Building Record | Database | Real building and source identities, evidence release, components, observations, subject/scope, conflicts and missing-data reasons |
| Catalogue definition | Catalogue | Definition ID and version, parameters, units, applicability and sources |
| Weather reference | Weather package | File content identity, location, simulation calendar, source period and generation history |
| Physical Building model | Core | Geometry, fabric, operation, systems, weather, physical units, reference bases and assumption history |
| Cross-package assembly | EPSM | The mapping from evidence and chosen definitions to Core inputs, with a report of choices and unresolved requirements |
| Prepared case and execution records | Workflows | Case/run IDs, fixed input references, attempts, status and retained outputs |
| Simulation Result | Core | Metric definitions, units, reference bases, periods, diagnostics and execution identity |
| LCA or other assessment Result | The method package | Method and factor versions, assessment boundaries, time basis and result meaning |
| Study outcomes and retained files | Workflows | Every case outcome, collection, aggregation and retention policy |

Use the owning package's public objects and validators. EPSM should not maintain a second physical model with a second set of validation rules. If an adapter needs a small intermediate value, explain why and keep it limited to that conversion.

Packages must remain independently usable. Database and Catalogue do not need Core to represent their evidence or definitions. Lower-level packages must not import EPSM to obtain a shared type. Agree a small shared runtime dependency only when concrete consumers need it; this handbook is not a Python model package.

## Rules that cross package boundaries

**Identity.** Keep a real `building_id` separate from a model revision, scenario, case, run and attempt. A footprint-only model may have no national building ID. Do not invent one. Use separate source IDs for certificates and components, with their publisher, dataset or release when needed to make them unique. A source-local ID is not automatically a universal EPSM identity. Content identity is an agreed checksum or identifier for the actual content, rather than its path or package version. Save both that identity and producer history where results can be reused.

**Units and meaning.** A quantity needs its value, unit and reference basis. Heated floor area, footprint area and zone area are different quantities even though all use square metres. Thermal demand and delivered energy are different metrics even though both may use kWh. An adapter may convert units, but it must retain the original value and explain the conversion.

**Geometry.** State the coordinate reference system, horizontal and vertical units, local origin, orientation and treatment of holes and disconnected parts. A preview may use a local origin for numerical stability; it must retain the mapping back to the model's coordinates.

**Time.** State the simulation calendar, timestamps, interval meaning, timezone or fixed offset, and leap-year handling. Keep the weather source period separate from the simulation calendar. This distinction will matter for a typical meteorological year (TMY), which combines representative weather periods, and for future weather. Those methods remain future scope until implemented and checked.

**Evidence and assumptions.** Preserve the source observation when selecting or overriding it. Record value origin, mapping verification, certificate scope and physical plausibility separately; one `valid` flag cannot answer all four questions. A shared certificate quantity must not become an independent measurement for every linked building.

**Missing and conflicting data.** Keep the reason a value is absent and the competing observations behind a conflict. Zero is a value. A catalogue fallback is still an assumption. Incomplete Buildings remain inspectable, while simulation requires a complete validated snapshot.

**Results and reuse.** Engine execution identity describes the numerical inputs, weather, engine and requested outputs. Evaluated-result identity also includes the inputs, calculation version and dependencies used to interpret those outputs. Keep these identities, acceptance policy and original producer history separate. A change to delivery, photovoltaic (PV) generation or lifecycle assessment (LCA) interpretation may require reevaluation even when the engine output can be reused. A new reader must not replace the recorded original producer.

**Stored formats.** Keep schema/format versions separate from package releases, database releases and catalogue releases. Each owner documents supported versions and explicit migrations. Portable records and cases contain data and safe source references, not credentials, open connections or notebook state.

For future LCA, agree quantities, factor versions, assessment stages, time horizon and global warming potential (GWP) method before comparing results. A number labelled `kg CO2e` alone does not establish that two assessments share the same boundaries.

## Walk through one small building

Use this sequence to agree the first models and tests:

1. Database returns a Record for one building from a fixed evidence release. Its certificate is still identified as the source of certificate-level observations.
2. EPSM selects documented assumptions from a fixed Catalogue release. Its assembly report shows selections, overrides, conflicts and values still missing.
3. Core receives physical inputs and checks their units, geometry and meaning. The user can inspect and edit the Building without altering its source Record.
4. Submission fixes the model, weather, engine request and evaluation inputs. Core can run a single simulation independently. When the case belongs to a Study, Workflows links it to a Run, records each attempt and references Core's execution report.
5. Core interprets simulation outputs. For a Study, Workflows retains the outputs and case outcome. EPSM makes the Result easy to inspect and plot.
6. A renovation scenario creates an independent revision. The baseline, earlier inputs and results remain available unchanged.

This is a proposed acceptance route, not a claim that the current packages implement it end to end. Use [the common use cases](../use_cases/README.md) and link real tests when each step works.

## Agree a format before implementing it

For each object or file exchanged between packages, write a short note with:

- Its purpose, owning package, producer and consumers.
- The agreed fields, units, reference bases, identities and missing-data rules.
- A small valid example, an incomplete example and an invalid example.
- The format version and how an unsupported version is reported.
- One producer/consumer test, plus the owning package's own checks.

Start with Record-to-Building assembly, prepared cases and Results. Add fields only when a real use case needs them. Keep accepted notes and small synthetic examples here; keep executable validators, authoritative file schemas and package fixtures with their owner. Update both sides and their integration checks when an agreement changes.

Before declaring a platform-wide schema stable, settle the initial authoring/edit behaviour, the exact model and run identities, and the minimum exchanges required by the first research route. Design examples are the place to work out those choices.

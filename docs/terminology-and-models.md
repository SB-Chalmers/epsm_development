# Shared terms and models

The `epsm_development` handbook is the place to agree on the words we use and the information packages pass to each other. These agreements help independently developed packages work together and give researchers a familiar interface. Database refers to `epsm_db`; Catalogue refers to `epsm_data`.

**Implemented development ownership, 15 October 2026.** The [harmonisation guide](harmonisation.md) describes the implemented development API and its limits. These shared meanings also guide future additions; individual stored formats remain owned and versioned by their packages.

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
| Building | A physical research model with geometry, fabric, operation and systems; weather is supplied to an evaluation |
| Assumption | A declared modelling choice, including an adopted default or override |
| Archetype | An immutable composition of optional construction definitions, operating profile, HVAC template and envelope assumptions, with classification and sources. Catalogue selection and custom authoring return the same type; incomplete definitions are allowed. See the [authoring guide](archetype-authoring.md). |
| ConstructionSet | Reusable `Element` or `WindowElement` definitions by role, independent of geometry, operation and installed systems |
| Material / Layer / Component / Element | The shared construction hierarchy: material constituents, layered compositions, ordered components and complete construction assemblies |
| BuildingElement | A particular physical wall, roof, floor or window with geometry and an assigned `Element` or whole-window `WindowElement` |
| OperatingProfile | Data-owned portable operating assumptions and source definitions; Core expands schedules using the caller's project calendar |
| HVACTemplate | Data-owned reusable system definition; selecting it is an explicit modelling choice and does not identify observed installed equipment |
| EnvelopePerformance | Data-owned infiltration value, reference basis and thermal-bridge assumptions; site-specific ground configuration remains separate |
| ArchetypeApplicationReport | EPSM's retained record of applied, replaced, retained and unmatched choices, sources, assumptions and unresolved requirements |
| Profile | A named set of assumptions or schedules; qualify the name when its purpose is unclear |
| Scenario | An independent Building alternative with declared changes and an identifiable renovation path; no dates or fixed stage slots are required |
| Evidence release | A fixed published selection of database evidence and its processing history |
| Model snapshot | A fixed version of an authored model; later edits do not change it |
| Weather | A weather file or artifact with location, calendar, source period and generation history |
| Case | One prepared study alternative, with fixed inputs and the evaluation requested |
| Study | A research investigation with its question, selection, scenarios, inputs and outcomes |
| Workflow | A reusable procedure that carries out a study or one of its stages |
| Run | One requested execution using fixed inputs |
| Attempt | One try at completing a Run; retries remain attached to the same request |
| Engine input | Core's compiled input, tied to the weather, engine and requested outputs |
| Evaluation | A retained combination of energy, LCA, quantities, diagnostics, fixed inputs and calculation identities |
| Results | A Building’s collection of evaluations, initially empty; later edits do not rewrite its entries |
| Result | An interpreted calculation outcome linked to its inputs and method |
| Artifact | A retained file, such as model input, weather, diagnostics, results or a report |
| Schema | The fields and rules of a stored or exchanged format; it has its own version |

Avoid using `component` without saying what it means. A database geometry component, a modelled building part and a construction layer are different things. Name the kind and explain their mapping. Likewise, use `evidence release`, `model snapshot` or `submitted inputs` when the word `snapshot` alone would be unclear.

Use the same names in public methods, docstrings, logs, plot legends and notebooks. Record older names in migration notes rather than introducing another synonym in each package.

## Give each model one owner

| Information | Owner | Must preserve |
| --- | --- | --- |
| Building Record | Database | Real building and source identities, evidence release, components, observations, subject/scope, conflicts and missing-data reasons |
| Construction and catalogue definition | Data | Material identities, fractions, physical order, profiles/templates, envelope assumptions, units, applicability and sources; saved evaluations keep the values they used |
| Weather object | Core | File content identity, location and simulation calendar; smhi2epw owns acquisition, generation and their provenance |
| Physical Building model | Core | Geometry, fabric, operation, systems, physical units, reference bases, physical occurrences and assumptions |
| Cross-package assembly | EPSM | The mapping from evidence and chosen definitions to Core inputs, with a report of choices and unresolved requirements |
| Prepared case and execution records | Workflows | Case/run IDs, fixed input references, attempts, status and retained outputs |
| Engine result | Core or RC | Engine outputs, units, periods, diagnostics, explicit approximations and execution identity |
| Combined evaluation and Results | EPSM | Common energy boundaries, physical state, renovation path, weather, assessment settings and separate energy/LCA identities |
| LCA or other assessment Result | The method package | Method and factor versions, assessment boundaries, time basis and result meaning |
| Study outcomes and retained files | Workflows | Every case outcome, collection, aggregation and retention policy |

Use the owning package's public objects and validators. EPSM should not maintain a second physical model with a second set of validation rules. If an adapter needs a small intermediate value, explain why and keep it limited to that conversion.

Packages must remain independently usable. Database and Catalogue do not need Core to represent their evidence or definitions. Data owns the lightweight construction classes shared by Core. Lower-level packages do not import EPSM to obtain a shared type. Data exposes definition selection; Core exposes physical conversion and assignment; EPSM owns their assembly. Retired integration forwarders are listed in the owning package migration guides. This handbook is not a Python model package.

## Rules that cross package boundaries

**Identity.** Keep a real `building_id` separate from a model revision, scenario, case, run and attempt. A footprint-only model may have no national building ID. Do not invent one. Use separate source IDs for certificates and components, with their publisher, dataset or release when needed to make them unique. A source-local ID is not automatically a universal EPSM identity. Content identity is an agreed checksum or identifier for the actual content, rather than its path or package version. Save both that identity and producer history where results can be reused.

**Units and meaning.** A quantity needs its value, unit and reference basis. Heated floor area, footprint area and zone area are different quantities even though all use square metres. Thermal demand and delivered energy are different metrics even though both may use kWh. An adapter may convert units, but it must retain the original value and explain the conversion.

**Geometry.** State the coordinate reference system, horizontal and vertical units, local origin, orientation and treatment of holes and disconnected parts. A preview may use a local origin for numerical stability; it must retain the mapping back to the model's coordinates.

**Time.** State the simulation calendar, timestamps, interval meaning, timezone or fixed offset, and leap-year handling. Keep the weather source period separate from the simulation calendar. This distinction will matter for a typical meteorological year (TMY), which combines representative weather periods, and for future weather. Those methods remain future scope until implemented and checked.

**Evidence and assumptions.** Preserve the source observation when selecting or overriding it. Record value origin, mapping verification, certificate scope and physical plausibility separately; one `valid` flag cannot answer all four questions. A shared certificate quantity must not become an independent measurement for every linked building.

**Missing and conflicting data.** Keep the reason a value is absent and the competing observations behind a conflict. Zero is a value. A catalogue fallback is still an assumption. Incomplete Buildings remain inspectable, while simulation requires a complete validated snapshot.

**Results and reuse.** Engine execution identity describes the numerical inputs, weather, engine and requested outputs. Evaluated-result identity also includes the inputs, calculation version and dependencies used to interpret those outputs. Keep these identities, acceptance policy and original producer history separate. A change to delivery, photovoltaic (PV) generation or lifecycle assessment (LCA) interpretation may require reevaluation even when the engine output can be reused. A new reader must not replace the recorded original producer.

**Stored formats.** Keep schema/format versions separate from package releases, database evidence releases and saved catalogue input identities. Each owner documents supported versions and explicit migrations. Portable records and cases contain data and safe source references, not credentials, open connections or notebook state.

For LCA, declare material flows, actual factors and sources, assessment modules, reference period and global warming potential (GWP) method before comparing results. A number labelled `kg CO2e` alone does not establish that two assessments share the same boundaries.

## Walk through one small building

The current local route follows this sequence:

1. Database returns a Record for one building from a fixed evidence release. Its certificate is still identified as the source of certificate-level observations.
2. The caller selects a Data catalogue archetype or authors one using the same classes, and applies it to an already configured Building through EPSM. HVAC and project calendars remain explicit choices. The application report preserves assumptions separately from source observations; saved evaluations retain the actual definitions and reports.
3. Core receives physical inputs and checks their units, geometry and meaning. The user can inspect and edit the Building without altering its source Record.
4. `building.simulate(engine=..., weather=...)` freezes physical inputs, weather and assessment settings internally. Core runs EnergyPlus or RC runs its reduced model. Workflows can prepare and execute the same evaluation with retained attempts.
5. EPSM normalizes energy outputs, runs LCA and appends the combined evaluation to `building.results`. An incomplete or failed assessment preserves the completed energy result. Workflows retains case outcomes and separate cache identities.
6. A renovation scenario creates an independent revision. The baseline, earlier inputs and results remain available unchanged.

The [review register](harmonisation-review.md) records local verification and missing deployment checks. Live database access, weather acquisition and Vera execution each need their own stated evidence; a local simulation does not verify those services. Use [the common use cases](../use_cases/README.md) when extending this route.

## Agree a format before implementing it

For each object or file exchanged between packages, write a short note with:

- Its purpose, owning package, producer and consumers.
- The agreed fields, units, reference bases, identities and missing-data rules.
- A small valid example, an incomplete example and an invalid example.
- The format version and how an unsupported version is reported.
- One producer/consumer test, plus the owning package's own checks.

Start with Record-to-Building assembly, prepared cases and Results. Add fields only when a real use case needs them. Keep accepted notes and small synthetic examples here; keep executable validators, authoritative file schemas and package fixtures with their owner. Update both sides and their integration checks when an agreement changes.

Before declaring a platform-wide schema stable, settle the initial authoring/edit behaviour, the exact model and run identities, and the minimum exchanges required by the first research route. Design examples are the place to work out those choices.

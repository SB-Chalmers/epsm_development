# Reusable dataset authoring

Status: implementation and local owner/Studio verification complete,
22 October 2026. This campaign extends the existing study
journey. It does not reproduce the archived Vera experiment or add model training
and statistical analysis to Studio. Release promotion remains a separate gate.

## Ownership and reuse

| Owner | Reuse | Small extension |
| --- | --- | --- |
| Core | Footprint factories/scaling, physical assignments, context generation, thermal insulation solver, validation | Adjust an explicitly selected physical insulation layer to a target U-value while preserving materials and quantities |
| EPSM | Building inheritance, assembly, preflight, evaluation bundles | Verify the inherited physical operation through the public Building interface; no duplicate wrapper was needed |
| Workflows | Existing samplers, scopes, owner bindings, weather mapping, prepared execution and attempts | Bind geometry and context generation, expose construction-aware targets, describe the design, and dispatch bounded remote batches |
| Studies | Verified archives, planned outcomes, attempts, scalar tables, calendars and lazy arrays | Read frozen inputs and export a joined dataset with units and an explicit hourly option |
| Studio | Existing recipe/setup/results journey and StudioClient boundary | Present tested owner descriptors and summaries, and consume reusable owner exports |

Data supplies immutable material/construction records; weather generation remains
in smhi2epw. RC and LCA retain their scientific methods and result meanings. New
scientific controls are capability-backed. Unsupported combinations fail with
actionable diagnostics rather than being silently repaired or omitted.

## Acceptance stories

1. An author selects several complete building templates or supported source
   shapes and defines shared, per-building or per-group variation. Existing
   categorical allocation and seeded sample ordering remain unchanged.
2. Sampled footprint size and height resolve through Core operations before
   geometry-dependent context generation. Invalid geometry remains visible in
   preflight, and the original templates are unchanged.
3. A U-value target identifies a physical element, component and layer. The
   resulting material graph retains identities, fractions and actual depths.
   Failed multi-element edits are atomic. Draft authoring creates no renovation
   material events.
4. A compact preview describes exact case counts, parameter ranges, categorical
   counts, fixed assumptions and representative cases without running engines.
5. Preparation freezes inputs, weather, output requests, identities and runtime.
   Bounded local/remote dispatch uses existing verification, locks and attempt
   records. Cancellation, retry and successful-case reuse retain their meaning.
6. A portable dataset joins realized parameters and scalar outputs for every
   planned evaluation, including failed and unrun cases. It retains building,
   group, sample, scenario, weather and engine identities; sample labels alone
   are not globally unique.
7. Dataset exports include units, accounting boundaries, coverage, attempts and
   a data dictionary. Hourly arrays load only when explicitly requested, retain
   the original calendar and units, and never turn missing values into zero.
8. Studio uses Buildings → Experiment → Conditions and outputs → Review → Run
   → Export. It presents these same public operations and performs no scientific
   sampling, physical validation or result calculations in the browser.

## Compatibility gates

- Existing specification serialization and IDs, seeded designs and row order,
  prepared formats, archive identities, callback routes and public return types
  retain their behavior. New features are opt-in.
- Existing export defaults stay unchanged. New dataset export is explicit and
  refuses to overwrite evidence. Old archives remain readable.
- New feature fields require compatible readers and capability discovery. Do
  not insert serialized defaults into old documents or silently reinterpret
  existing methods.
- A frozen plan still requires its captured runtime. An edited specification or
  changed runtime prepares a new plan; integrity checks are not bypassed.
- Owner tests precede implementation. Small cross-package tests exercise real
  public conversions. Owner source and handoff tests precede Studio adoption;
  final installed-wheel cohort checks gate campaign completion.

## Implemented public operations

| Owner | Candidate revision | Public interface |
| --- | --- | --- |
| Core | `b562ff5` | `solve_element_insulation()` and `Building.assign_element_u_value()` |
| EPSM | `fef5b23` | Inherited `Building.assign_element_u_value()`, verified through the integration Building |
| Workflows | `3d3c255` | Physical geometry/context/construction bindings, `log_uniform()`, `WorkflowSpec.describe_design()`, selected local execution and Vera task batching |
| Studies | `f36e1b7` | `Study.describe_design()`, `StudyResults.case_inputs()`, `design_table()` and `export_dataset()` |

### Physical variation and its assumptions

The construction operation needs an explicit element, component name and
zero-based layer index. It reuses Core's resistance solver and changes actual
layer thickness, preserving the materials, fractions and installed element
identities. The target is nominal opaque U-value in W/(m2 K), with Core's
0.17 m2 K/W surface-film resistance. It excludes thermal bridges and ground
transfer. Data's role-specific reporting films can give a different reported
value for internal constructions. Core does not guess which material is
insulation; windows, unequal-depth constituents and infeasible targets fail.
All selected elements are solved before committing a draft edit. Material
quantities follow the resulting physical depths. A renovation measure remains
necessary when installation/removal events are intended.

Workflows connects this operation through `envelope.element_u_value`. Its
selector identifies the actual element IDs, component and layer, with optional
positive thickness bounds. Several complete constructions can still be supplied
as ordinary finite choices. There is no new catalogue or physical calculation.

`geometry.footprint_area_m2` scales one explicit building part through Core,
preserving the footprint shape and holes. Ambiguous multipart shortcuts are
rejected. Sampled geometry resolves before `context.synthetic` generates its
surroundings. If the workflow also supplies a complete context or neighbour
buildings, it must explicitly choose `retain_existing=True`; otherwise preview
reports the conflict. Retention preserves the supplied buildings, context
settings and earlier generation evidence. This prevents a generated context
from silently replacing a student's supplied surroundings.
Conditions that depend on generated context before it resolves produce an
explicit diagnostic; existing conditions without generation retain their behavior.

### Sampling, review and execution

Optional `log_uniform()` provides equal probability over equal multiplicative
intervals and requires positive increasing bounds. Existing probability streams,
seeded ordering, categorical rules and other distribution defaults are unchanged.
Shared, per-building and per-group scopes remain the same public operations.

`describe_design()` reuses Workflows' case expansion to show case/design counts,
counts by experimental axis, realized input ranges or choice counts, fixed
bindings, bounded examples and diagnostics. It does not run an engine. A report
that skips readiness checks or cannot fully expand the design is not a ready
execution plan. The Studies method delegates to this owner operation.

The `epsm-evaluations describe workflow.json` command includes `source_sha256`,
the digest of the exact input file bytes. Studio can match an imported report
to its exported workflow without implementing a scientific identity algorithm.
This file match does not authorize execution or associate old results with an
edited draft. `epsm-study describe study.json` describes the composed study
through the same Workflows operation.

`run_local(..., indices=...)` executes an explicit selection while preserving
the existing whole-plan outcome counts. Vera's optional `cases_per_task` groups
contiguous cases into sequential tasks; its default remains one case per task.
Each batch verifies the complete plan and runtime, then checks individual cases
and assets before dispatch. Existing locks, retry rules and successful-case
reuse remain active. Explicit array limits reject oversized submissions; no new
scheduler or automatic multi-job submission is introduced.

### Portable datasets and the Studio boundary

`case_inputs()` verifies a frozen archived case before returning its compact
inputs. `design_table()` joins those inputs to every selected planned evaluation,
including failures and unrun cases, with per-case units and recorded weather,
energy boundaries and assessment settings. Building/group, sample, scenario,
state, weather, engine and pairing identities remain distinct. No training/test
split or analysis is inferred from them.

`export_dataset()` publishes joined evaluation CSV/JSON, typed input values,
coverage, attempts, the unchanged specification and a data dictionary. Missing
values remain unknown, not zero. Text is protected from spreadsheet formulas;
JSON retains its original values. The default reads no numerical arrays and
needs no Workflows, engine or NumPy imports. Explicit `hourly_signals=[...]`
adds original timestamps, values, units and per-case availability. Complete
owner metadata is released between cases, and hourly arrays are streamed one
case at a time. Full physical model records do not accumulate across the export.

The dataset includes the unchanged specification, including any models embedded
in that document. It references the immutable scientific archive rather than
separately copying native model files, weather bytes or engine artifacts. Share
the archive when complete evidence is needed. Existing archive identities,
formats and single-table export behavior
stay unchanged. New datasets refuse occupied destinations, publish a completion
manifest last and preserve existing evidence on failure.

Studio keeps the existing setup sections. Its controls consume owner capability
descriptions; imported previews and retained results remain separate from
editable drafts. Arbitrary drafts still require explicit platform validation
and execution. Browser forms do not implement the scientific sampler, physical
validator or result calculations.

## Delivery and evidence

Each owner commits focused tests, implementation and public documentation on a
`codex/` branch. Existing dirty checkouts are preserved in separate worktrees.
Core/EPSM operations pass before Workflows adopts them; Workflows passes before
Studies collection/export integration; Studio changes follow the owner handoff
checks. No campaign changes merge to development or main as part of this feature
implementation.

The baseline audit ran 304 selected offline tests against immutable development
source snapshots. Eight optional weather-morphing tests were skipped and four
engine/climate-generator cases were excluded. This remains dated source evidence.

The final installed-package checks passed 206 Workflows tests at
`3d3c255`, 92 Studies tests at `f36e1b7` and 58 EPSM handoff tests at `fef5b23`.
Installed Workflows statement/branch coverage was 83.59%/73.56%; Studies was
82.41%/74.55%. These checks used isolated owner-wheel installs on Python 3.12.3
with available third-party dependencies. Core's offline source suite passed
1,086 tests, with eight prerequisite skips and 33 EnergyPlus-marked checks
excluded. Seven skips need the unavailable pinned AMY weather file and one
needs an optional legacy Data adapter. Skipped checks are not passing checks.
Core statement/branch coverage was 90.69%/82.26%; its new public operations
reached 100% of both. Exact candidate revisions, wheel hashes, implementation
identities, coverage counts and qualifications are recorded in the
[verification receipt](verification/2026-10-22-training-data-authoring.json).

Studio at `3338e10` passed 114 unit tests, 21 browser journeys, its build, ten
fixture/harness tests and seven Pocket CAD asset checks. The browser handoff
exported an L-shaped teaching building with a log-uniform footprint range,
assigned weather through the public owner API and invoked the real Workflows
compact-preview CLI. It imported the four-case report, recovered it after reload
and hid stale counts immediately after a physical edit. A joined dataset download
matched the public Studies export bytes. No engines ran during that handoff.
The original fixture and artwork remained unchanged. The optional authoring pack
round-tripped three complete building models through installed owner APIs.

The 92-test Studies source run covered 82.4% of statements and 74.5% of branches.
The new dataset module covered 99.2% of statements and 95.5% of branches. CLI
subprocesses are tested but absent from these coverage totals. Checks include
failed/unrun evaluations, unknown impacts, units/boundaries, typed categories,
checksum faults, fresh-process reading without execution packages or NumPy,
spreadsheet-safe text, concurrent publication and cleanup. A public-reader
lifetime test adds a 1 MB payload to each owner record and verifies that no prior
complete record remains alive when the next case is read.

The unchanged retained six-evaluation archive reopened with its original identity
and 297 verified files. Its RC and EnergyPlus outputs exported 52,560 original
2023 hourly values with units. No engines ran during this compatibility check.

The reusable offline dispatch harness measured 128 and 512 tiny prepared Python
stub cases. With batches of 32, complete-plan verifications fell from 128 to 4
and from 512 to 16. All identities and expected stub outcomes were retained.
These measurements cover local filesystem and runtime-check overhead, not
building preparation or numerical engines. The Workflows repository retains the
captured source hashes, timings and full observations in
`docs/verification/2026-10-22-prepared-dispatch.json`.

This campaign does not establish 60,000-case performance, live Vera/Slurm behavior,
future-weather provider execution, prediction accuracy or broad release
qualification. It does not reproduce the old optimized LHS design, introduce a
model-training service or choose analysis results for students. Owner candidate
checks and historical archive compatibility are evidence for these additions;
release promotion still follows the normal package and cohort gates.

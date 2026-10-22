# Reusable dataset authoring

Status: implementation in progress, 22 October 2026. This campaign extends the
existing study journey. It does not reproduce the archived Vera experiment or
add model training and statistical analysis to Studio.

## Ownership and reuse

| Owner | Reuse | Small extension |
| --- | --- | --- |
| Core | Footprint factories/scaling, physical assignments, context generation, thermal insulation solver, validation | Adjust an explicitly selected physical insulation layer to a target U-value while preserving materials and quantities |
| EPSM | Building inheritance, assembly, preflight, evaluation bundles | Test the new physical operation through the public Building interface; add a wrapper only if inheritance is insufficient |
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
  public conversions; installed-wheel checks follow before Studio adoption.

## Delivery and evidence

Each owner commits focused tests, implementation and public documentation on a
`codex/` branch. Existing dirty checkouts are preserved in separate worktrees.
Core/EPSM operations pass before Workflows adopts them; Workflows passes before
Studies collection/export integration; Studio changes follow the owner handoff
checks. No campaign changes merge to development or main as part of this feature
implementation.

The baseline audit ran 304 selected offline tests against immutable development
source snapshots. Eight optional weather-morphing tests were skipped and four
engine/climate-generator cases were excluded. This is source-level evidence,
not a release qualification or a 60,000-case performance claim. Campaign checks,
revisions and limitations will be added as the implementation proceeds.

# Common EPSM Use Cases

This is the shared index of useful things a researcher should be able to do with EPSM. Each story gives the collaborating packages a common target, even when their implementations are developed independently.

**Status: proposed acceptance stories, 13 October 2026.** The table is a design and testing checklist. It does not claim that these exact public interfaces exist or that the complete integrations have passed. Existing capability and dated test evidence are recorded separately in the [ecosystem review](../docs/ecosystem-review.md).

Read the [package layout](../docs/project-layout.md) and [engineering style](../docs/engineering-style.md) for where implementations and tests belong. The new package names below describe the agreed direction; some current repositories still have older names.

## The first eight stories

| ID | Researcher story | Owning packages | Input and expected outcome | Evidence status |
| --- | --- | --- | --- | --- |
| UC01 | Start a Building from a footprint | EPSM interface; Core geometry/model | A polygon with coordinate reference, units and supplied floor information becomes an inspectable Building. Missing weather or assumptions remain visible. | Proposed; needs public authoring and geometry checks |
| UC02 | Retrieve a building Record | Database retrieval; EPSM integration | A building identity and pinned release return portable evidence with components, provenance, conflicts and missing-data reasons through a restricted reader. | Proposed; needs real database and release-pinning checks |
| UC03 | Apply declared assumptions | Catalogue definitions; EPSM assembly; Core validation | A Record or incomplete Building plus an explicit profile yields a model revision and an inspectable assumption report. Source observations remain unchanged. | Proposed; needs installed catalogue-to-model checks |
| UC04 | Select usable weather | `smhi2epw` weather; EPSM handoff; Core calendar checks | A supplied EPW and explicit calendar produce a weather reference with provenance and content identity. Generation is a separately requested operation. | Proposed; needs artifact/calendar and installed weather checks |
| UC05 | Simulate and inspect results | Core execution/result meaning; EPSM convenience | A complete model and fixed weather produce a retained run and readable metrics/diagnostics. Thermal demand and delivered energy retain their different meanings and units. | Proposed; needs real engine and result checks |
| UC06 | Run a small Study | EPSM Study interface; Workflows execution; Core simulation | A small prepared cohort and explicit configuration produce an outcome for every attempted case, retained run identities and a useful study summary. | Proposed; needs installed local study execution checks |
| UC07 | Compare a renovation scenario | Catalogue measure definitions; Core physical change; EPSM scenario; Workflows execution | A baseline and declared measure produce an independent alternative and energy/quantity comparison. The baseline and prior runs stay unchanged. | Proposed; needs scenario isolation and comparison checks; LCA is later scope |
| UC08 | Resume interrupted work | Workflows checkpoints/attempts; EPSM interface | An interrupted study resumes from retained state without losing earlier attempts or mixing changed inputs into existing runs. Every case keeps an outcome. | Proposed; needs interruption, restart and input-identity checks |

A story can be supported by several smaller tests. For example, UC04 has an offline artifact handoff and an explicitly requested weather-generation route that may require network access. Record which route was exercised; do not give the whole story a passing label because only one part ran.

## Where the work lives

Keep tests of a package's rules with that package. Core tests its geometry, simulation and result meaning; Database tests evidence and restricted queries; Catalogue tests definitions and their source evidence; Weather tests acquisition and weather processing; Workflows tests execution and retained attempts.

The EPSM umbrella owns tests that connect their real installed APIs. Those checks should not depend on editable sibling checkouts or replace every collaborator with a mock. Use small fixed inputs and real services/engines when their behaviour determines the expected outcome.

This handbook holds the use-case index and shared story descriptions. It does not copy platform implementations or claim that its documentation checks validate EnergyPlus, PostGIS or weather generation. Named research experiments, calibration choices and paper analyses belong in `epsm_studies`.

## Turn a story into a tested route

For each story, record:

1. **Purpose and owner:** the useful outcome and the package responsible for each step.
2. **Inputs:** small fixtures or named releases, units, calendar and required services/engines.
3. **Steps:** ordinary public operations, with file/service access made explicit.
4. **Expected outcome:** observable values, identities or invariants, including missing-data and failure cases.
5. **Evidence:** links to the owning package tests, umbrella handoff tests and runnable example.
6. **Check record:** command, tested package versions, environment, date, results and limits.

Keep the IDs stable so issues, tests, examples and release notes can refer to the same story. Exact constructors and method names are agreed through the examples, not fixed by this index.

Use plain evidence labels:

| Label | Meaning |
| --- | --- |
| Proposed | The expected behaviour is written down; acceptance evidence is not yet linked |
| In progress | Implementation or tests are being developed; the remaining work is stated |
| Passing for a stated environment | Linked checks passed for the listed versions, fixtures and prerequisites |
| Unverified or blocked | A required check has not run, or its missing prerequisite prevents a conclusion |

A skipped required integration remains unverified. Passing an acceptance story shows that the stated route works; it does not establish national source coverage or empirical building prediction accuracy.

When an API changes, the package owner updates its tests and migration note, then updates the affected common examples and umbrella checks. Test the new installed package combination before advertising that combination as working.

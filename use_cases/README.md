# Common EPSM Use Cases

This is the shared index of useful things a researcher should be able to do with EPSM. Each story gives the collaborating packages a common target, even when their implementations are developed independently.

**Status: development acceptance routes, 14 October 2026.** The table records supported local routes and remaining checks. Commands, results and limitations appear in the [repository review register](../docs/harmonisation-review.md). The earlier [ecosystem review](../docs/ecosystem-review.md) is a historical snapshot.

Read the [package layout](../docs/project-layout.md) and [engineering style](../docs/engineering-style.md) for where implementations and tests belong. The package names below follow the agreed ownership; documented legacy imports are compatibility routes.

## The common stories

| ID | Researcher story | Owning packages | Input and expected outcome | Evidence status |
| --- | --- | --- | --- | --- |
| UC01 | Start a Building from a footprint | EPSM interface; Core geometry/model | A polygon with coordinate reference, units and supplied floor information becomes an inspectable Building. Missing assumptions remain visible; weather is supplied at evaluation. | Local Core authoring/readiness tests pass; supported geometry is stated in the harmonisation guide |
| UC02 | Retrieve a building Record | Database retrieval; EPSM integration | A read-only account uses a building ID and fixed database release to retrieve components, source history, conflicts and missing-data reasons. The Record can be saved or passed on without a database connection. | Portable record/completeness tests pass; live restricted-account and release-pinning checks remain separate deployment work |
| UC03 | Apply declared assumptions | Catalogue definitions; EPSM assembly; Core validation | An incomplete Building accepts an explicit construction set, HVAC and operating profile. Source observations remain unchanged. | Shared graph, isolated assignment and evidence-override regressions pass; installed checks are recorded separately |
| UC04 | Select usable weather | `smhi2epw` weather; EPSM handoff; Core calendar checks | A supplied EPW and explicit calendar produce a weather reference with provenance and content identity. Generation is a separately requested operation. | Existing EPW/calendar handoff is exercised by local real engines; new online acquisition is not implied |
| UC05 | Simulate and inspect results | Core/RC execution; EPSM common energy boundary and Results | A complete model and fixed weather produce a retained run and readable metrics/diagnostics. Thermal demand and delivered energy retain their different meanings and units. | Both engines ran through the public Building interface; saved evaluations and incomplete/failed LCA are tested |
| UC06 | Run a small Study | Studies PaperStudy; Workflows execution; EPSM evaluation | A small prepared cohort and explicit configuration produce an outcome for every attempted case, retained run identities and a useful study summary. | Prepared local execution and PaperStudy protocols are implemented; installed/deployment evidence is recorded separately |
| UC07 | Compare a renovation scenario | Catalogue measure definitions; Core physical change; EPSM scenario; Workflows execution | A baseline and declared measure produce an independent alternative and energy, quantity and LCA comparison. The baseline and prior runs stay unchanged. | Targeted and like-for-like changes, path-specific LCA and energy reuse have local regression coverage; factors remain explicit |
| UC08 | Resume interrupted work | Workflows checkpoints/attempts; EPSM interface | An interrupted study resumes from retained state without losing earlier attempts or mixing changed inputs into existing runs. Every case keeps an outcome. | Local checkpoints and Vera transport have offline regressions; a live Vera job remains unverified |
| UC09 | Inspect and compare plots and previews | Owning package renderers; EPSM convenience | Small loaded objects produce 2D Figures or documented 3D previews with common colours, labels, units and missing-data cues. Export and browser startup are explicit; source data remain unchanged. | Proposed; needs rendering, optional-dependency and preview cleanup checks |

A story can be supported by several smaller tests. For example, UC04 includes passing an existing weather file between packages without going online. It also includes generating weather when explicitly requested; that step may need network access. Record which route was exercised; do not give the whole story a passing label because only one part ran.

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

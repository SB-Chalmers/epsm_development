# Archetype verification register

**Verified development combination, 15 October 2026.** Steps 1–13 are merged;
this final handbook PR records acceptance. All eleven archetype scenarios below
have owned tests and installed confirmation. The
[machine-readable evidence](archetype-installed-evidence-2026-10-15.json) retains
full source revisions, installed versions and paths, wheel hashes, Python and
EnergyPlus versions, engine outputs and the scope of optional exclusions.
This is software integration evidence, not a release or empirical validation.

| Acceptance | Owning evidence | Final installed confirmation |
| --- | --- | --- |
| AC01 offline authoring | Data composed-archetype tests; dependency-free wheel imports and authoring notebook | Passed: final Data-only wheel; Core/EPSM absent and blocked; three fresh-kernel notebooks |
| AC02 shared type and editing isolation | Data authoring and catalogue tests; EPSM shared application-path test | Passed: Data authoring/catalogue tests and installed EPSM suite |
| AC03 portable exchange | Data version-4 roundtrips and format 1–3 readers; EPSM application-report save/load | Passed: Data exchange/readers tests and installed portable application checks |
| AC04 geometry consumption | Core atomic-assignment and EPSM application tests | Passed: atomic Core and installed EPSM regressions; opening geometry checked by engine gate |
| AC05 modes | Core per-element replace/fill tests; EPSM retained choices and explicit zero tests | Passed: Core replace/fill regressions and installed EPSM section/zero-preservation tests |
| AC06 invalid/incomplete | Data value validation, Core partial profiles/templates and atomic rollback; EPSM no-guessed-input tests | Passed: invalid-value and rollback tests; partial requirements remain visible in runnable examples |
| AC07 physical meaning | Captured 95 construction baselines; 95 native handovers; explicit Atemp/volume tests and independent record evidence | Passed: 95 captured physical graphs; explicit area/volume and record evidence regressions |
| AC08 operating profiles | Core monthly/calendar/BEN/custom tests in normal and leap years; Python summation-tolerant historical fingerprints | Passed: 104 focused installed profile/calendar tests; full Core suite and historical fingerprints |
| AC09 history | Core lineage; EPSM reports across copy, save/load, renovation and frozen evaluations | Passed: installed EPSM report/history/cache/evaluation regressions; three-state renovation handoff |
| AC10 coverage | Data canonical categories/configurations and source variants; SE.07; DB synthetic classifications | Passed: full Data coverage, source variants and offline DB classification regressions |
| AC11 installed handoffs | EPSM required wheel, RC and EnergyPlus check; fresh-kernel examples; actual source/version/wheel receipts | Passed: clean eight-wheel installation, actual RC/EnergyPlus, eight local notebooks and hosted development receipts |

## Ordered merges

| Step | PR | Merge revision |
| --- | --- | --- |
| 1 contract | [Development #14](https://github.com/SB-Chalmers/epsm_development/pull/14) | `5caf62034d81c6bfb9c4b38169684bec2175a360` |
| 2 definitions | [Data #6](https://github.com/SB-Chalmers/epsm_data/pull/6) | `483afd9acaa66fb55a28b09d9e2b5c35a547d057` |
| 3 conversion | [Core #27](https://github.com/SB-Chalmers/epsm_core/pull/27) | `7ce1d7fa7d3f1ee352508f286e3de774d167dee6` |
| 4 composed model | [Data #10](https://github.com/SB-Chalmers/epsm_data/pull/10) | `ac486aac01759a3dccc5993713d0469eb1806f24` |
| 5 composition pilot | [Data #13](https://github.com/SB-Chalmers/epsm_data/pull/13) | `e78375fb72d37268d68968e1bb360faa10b69291` |
| 6 atomic assignment | [Core #23](https://github.com/SB-Chalmers/epsm_core/pull/23) | `ad2e031c180462678abe8c3edc783feb112e0849` |
| 7 application | [EPSM #16](https://github.com/SB-Chalmers/epsm/pull/16) | `7e9c1dc3d39c557fec1285740568d397c9cc8ac6` |
| 8 catalogue coverage | [Data #14](https://github.com/SB-Chalmers/epsm_data/pull/14) | `8484c1039e3fdca9e3f174a1880630f0eb02c8c1` |
| 9 consumers | [EPSM #17](https://github.com/SB-Chalmers/epsm/pull/17) | `2c6a3cfc55697c90905a103b6ec00fa087907d98` |
| 10 stock inspection | [DB #15](https://github.com/SB-Chalmers/epsm_db/pull/15) | `9abe1d7e38475d824c2d52c5001b154baf23fa1a` |
| 11 installed gates | [EPSM #18](https://github.com/SB-Chalmers/epsm/pull/18) | `c9c27bd54d6ef02791bdc8610bd198854093b320` |
| 12 Data cleanup | [Data #15](https://github.com/SB-Chalmers/epsm_data/pull/15) | `9f69479c1d3914d1517670d3139b822d9c88f5f3` |
| 13 Core cleanup | [Core #30](https://github.com/SB-Chalmers/epsm_core/pull/30) | `0794e365448f6348dd25c7d9a7dd3aa9f8979525` |

The final handbook PR is linked after creation; its merge identity is available
from that PR. Every implementation PR was
reviewed by a separate agent and merged normally after its required hosted checks.
Those automated reviews are identified as agent reviews, not human approvals.
Earlier Actions billing startup failures were not counted as passes. Historical
reviews and source records remain dated and unchanged.

## Final installed checks

The [final hosted run](https://github.com/SB-Chalmers/epsm/actions/runs/38715287389)
passed all five jobs, including Python 3.11 and 3.13 development combinations.
Downloaded receipts in both lanes confirm Data `9f69479`, Core `0794e36`, EPSM
`c9c27bd` and the five other full revisions recorded in the evidence JSON. Both
lanes ran catalogue/authored RC and catalogue EnergyPlus 24.2 using actual
installed wheels, plus fresh EPSM and LCA kernels. Pinned lanes deliberately
retain the earlier compatible pre-cleanup combination; they are not evidence for
the new cleanup revisions. Version numbers alone do not identify this development
combination.

A separate fresh local environment passed `pip check`, 120 installed EPSM tests
with logging integration enabled and no skips, and 970 installed Core tests.
Sixteen installed offline DB catalogue/assignment tests also passed without
skips. Nine optional Core tests skipped; 29 separate standalone engine tests were
excluded. Neither group counts as an engine pass. The required archetype gate
ran both RC cases and the EnergyPlus case with zero skips and no remaining
requirements. Five EPSM notebooks and three Data notebooks passed fresh kernels.
The final Data wheel independently passed those three notebooks with Core/EPSM
absent and import-blocked. All committed notebook outputs remain cleared.

The 95 captured construction graphs remain physically equal to the starting
baseline. The independent-record/renovation handoff retains its three annual RC
outputs and completes the LCA route. Catalogue and custom fixture energy numbers
in the JSON verify execution; they are not observed building results. Python
historical schedule comparisons normalize only sub-source-precision summation
differences; source definitions and physical recipes are unchanged.

The first broader local Core attempt lacked the declared geometry extra and
permission for a localhost viewer server. It failed and is retained as such in
the evidence. Supplying those prerequisites produced a successful rerun; the
final fresh environment included both prerequisites from the start.

Public migration details are in the
[Data API guide](https://github.com/SB-Chalmers/epsm_data/blob/9f69479c1d3914d1517670d3139b822d9c88f5f3/docs/archetype-api-migration.md)
and [Core profile guide](https://github.com/SB-Chalmers/epsm_core/blob/0794e365448f6348dd25c7d9a7dd3aa9f8979525/docs/archetype-operation.md).
The required engine command and prerequisite failure behavior are documented in
[EPSM's installed checks](https://github.com/SB-Chalmers/epsm/blob/c9c27bd54d6ef02791bdc8610bd198854093b320/docs/archetype-installed-checks.md).

## Checks before API cleanup

[EPSM #18](https://github.com/SB-Chalmers/epsm/pull/18) passed the required
installed handoff gate before removing adapters: all eight wheels, 120 EPSM tests
without skips, fresh-kernel examples, catalogue and authored RC runs, and the
catalogue EnergyPlus 24.2 case. That receipt used the pre-cleanup Data/Core
combination. It is a prerequisite for cleanup, not the final post-cleanup receipt.

The Data cleanup source suite passed 355 tests (six optional skips). Its exact
wheel passed 120 installed EPSM tests without skips, all three isolated Data
notebooks and the required real engine check. All eight Data hosted checks passed
before merging. The Core cleanup passed 970 source and 970 installed tests (nine optional skips,
29 standalone engine tests excluded), 104 independent installed focused tests
without skips, all eight hosted checks and the actual archetype engine gate.
The post-cleanup combination subsequently passed the final gates above.

## Scope and retained limits

The linked JSON retains commands, exact source commits, installed versions and
paths, wheel hashes, Python and engine versions, test counts and prerequisite failures.
Source-prototype runs are useful development evidence and remain labelled as
such; they are not final installed-package acceptance. No live database is needed.
A missing required EnergyPlus executable, missing calendar, unresolved reference
basis or failed engine run does not establish the advertised route.

Existing scientific reviews and result snapshots remain dated historical records.
The series preserves physical inputs and source evidence; it does not validate a
real building, infer installed equipment or promote a new package release.

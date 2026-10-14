# Harmonisation repository review

**Review date: 14 October 2026.** Each repository has a dedicated review agent.
Reviews run in batches because only three worker agents can run concurrently.
The reference is this `epsm_development` handbook, particularly
[ownership and API style](engineering-style.md),
[shared models](terminology-and-models.md),
[package handoffs](io-and-api.md) and
[branch policy](branches-and-releases.md).

The implementation is on coordinated `codex/harmonisation` branches. A checked
development route is not a stable release or evidence of prediction accuracy.
The [architecture guide](harmonisation.md) describes its supported scope; the
[file map](harmonisation-file-map.md) records transfers and archive destinations.

## Current archive and review status

**Scope update, 14 October 2026, after the checkpoint below.** Reusable Workflows
execution, parametric/GSA and renovation search remain active, as does Studies
`PaperStudy`. Outdated named studies and their specific scripts/import routes are
archived under the [study archive decision](study-archive-policy.md). Their earlier
test and transfer counts remain a record of that checkpoint, not a continued
compatibility or reproduction promise.

The later review found that the old campaign CLI could hash a nonexistent source
root and cohort-transfer code still referenced removed Data evidence paths. Those
implementations are archived; their repair and reproduction are outside active
maintenance. This supersedes the earlier claim below that all archived resource
references had been corrected.

The later release-preparation change captures actual worker package and handler
source identities, dependency versions, and the built-in EPSM engine identity at
preparation. Workers verify these before execution and resume, and each attempt
retains the runtime hash. Custom handlers must still identify any external engine
they use in their supplied environment. The earlier checkpoint counts below
precede this fix.

## Repository findings at the earlier checkpoint

The findings below concern ownership, public APIs, missing-data handling,
retained evidence, import dependencies and examples. They are a focused review,
not certification that every older module meets every handbook convention.

| Repository | Findings and action | Verification and remaining scope |
| --- | --- | --- |
| `epsm_data` | Shared construction classes remain Core-independent. Fixed layered-window graph roundtrips, preserved identities/order/fractions, and corrected explorer expectations after adding SE.07. One current catalogue replaces active historical override chains; preserved studies retain source history. | Construction/serialization and explorer regressions passed; all 720 established numerical source cells remain unchanged. SE.07 has independent recipes and no renovation-state selector. Final run details follow below. |
| `epsm_core` | Fixed dropped explicit zero-window-ratio facade overrides. Preserved physical quantities and occurrence identities through targeted renovations. Unsupported geometry is reported. Fixed AMY calendar inference and weather provenance/receipt preservation after the weather handoff review. | Authoring/readiness/renovation regressions and real EnergyPlus execution passed. Hosted CI still needs private Data dependency access. Complex geometry outside the new bridge remains a declared limit. |
| `epsm` | Fixed source overrides being mistaken for observations, evaluation artifact overwrites, editable result attributes and incomplete cache identities. Common energy accounting and automatic LCA retain separate identities and failures. | Both real annual engines ran through `Building.simulate`; immutable results, multiple evaluations, evidence comparison and path-specific LCA have regression coverage. Clean installed platform regressions, the full example and both real engines passed. The final record conversion regression preserves its coordinate reference system (CRS). |
| `epsm_db` | Fixed portable nested geometry decoding, Stock archetype links, optional integration dependencies, coordinate reference preservation and bounded inspection. Database/Stock/BuildingRecord keep one underlying evidence implementation. Model conversion delegates to EPSM. | Offline record/query/adapter regressions passed. No live schema migration or ingestion change was made. Live restricted-account, PostGIS and release-deployment checks are not inferred from offline tests. |
| `epsm_rc` | Preserved the standalone 5R1C numerical solver through renaming. Corrected FTX heat-recovery accounting in the Core adapter, settings identity and unsupported-input reporting. A clean wheel environment exposed a read-only solar array under pandas 3; fixed in `2139c48`. | Standalone and adapter tests passed. Reduced-order assumptions remain explicit; a successful run does not establish agreement with measured buildings or EnergyPlus. |
| `epsm_lca` | Fixed mutable nested contributions, overflow handling and unknown quantity treatment. Missing factors or quantities remain incomplete, and like-for-like replacements retain installation/removal flows. | Assessment and EPSM integration regressions passed. Implemented modules and reference period are explicit; automatic future replacements and end-of-period demolition are outside the current method. |
| `epsm_workflows` | Fixed local/Vera checkpoint identity, weather-change detection, remote result merge conflicts and runtime identity. Preserved successful attempts, added operation logging and bounded tree inspection. | Parametric/GSA, renovation search and offline transport checks exist. No live Vera job has run in this harmonisation pass. |
| `epsm_studies` | Fixed mutable nested PaperStudy protocols and unbounded inspection. Moved historical research implementations and data into their owning repository; corrected remaining archived resource references. | Protocol tests and wheel smoke checks passed. SHA manifests verified 231 Workflows files and 32 Data files at transfer. Preserved research code is not automatically a scientifically revalidated study. |
| `smhi2epw` | Package remains independent. Its monitor found the AMY year/provenance defect at the Core consumer boundary; that fix belongs to Core and EPSM. | Weather generation source remains unchanged. Its 46 offline tests and 37 Core weather handoff tests passed. Receipt/provenance conversion is corrected; new provider acquisition is not claimed. |
| `epsm_development` | Corrected conflicting ownership of weather, obsolete versioned-catalogue guidance, missing RC ownership and old umbrella API sketches. Marked original review, roadmap and synchronization reports as historical. | Required links/syntax, handbook tests and notebook runner are checked separately below. Handbook checks do not execute platform simulations. |
| `epsm_studio` | Replacement remains out of scope. The monitor recorded old `snjsomnath` README/image references, raw EnergyPlus contracts, a duplicate application database name and conflicting database documentation for the future Studio migration. | No changes made. Clean `main`, `origin/main` and the live SB-Chalmers remote all matched `9c72a53`. These deferred findings do not imply Studio already uses the new platform APIs. |

## Historical evidence record

This section preserves the completed verification checkpoint from 14 October 2026,
before the archive decision and later findings above. Counts refer to stated
commands and environments; rerunning a subset does not create an
additional independent full-suite count. Missing services, skipped tests and
deselected integration tests remain visible.

Local engine checks used EnergyPlus 24.2 from OpenStudio 3.9 and the retained RC
solver with the bundled Gothenburg EPW. The common objective is annual delivered
space-heating energy plus ventilation fan electricity. The illustrative reference
produced **31,888.201130 kWh/year with EnergyPlus** and
**27,342.393446 kWh/year with RC**. Both automatic assessments completed when
supplied deliberately synthetic factors. These are execution and accounting
checks; synthetic factors are unsuitable for research conclusions.

The package test environment is Python 3.13.5 with the coordinated development
packages installed. All nine platform packages, including the weather package,
built and installed as wheels into a clean environment. `pip check` reported no
broken requirements. All nine package imports resolved inside the clean
`/tmp/epsm-wheel-clean` environment. Installed package tests, the example and both
real engines completed. The installed catalogue roundtripped all 35 current
construction graphs, and the Studies resource smoke check resolved 9 materials.
A successful installation is reported separately from those behavioural checks.

### Scoped package checks at this checkpoint

The coordination agent supplied these results from the local development
environment. They are checkpoints, not a summed platform test count.

| Package | Check and outcome |
| --- | --- |
| Data | Final full `pytest -q`: **251 passed, 1 skipped** in 433.56 seconds. This includes the corrected explorer failures. Shared graph checks had separately passed 20 with 1 skip. |
| Core | The broad suite passed 744 with 9 skipped and 21 deselected; its sandbox-blocked viewer test then passed separately. The subsequent focused authoring/regression run passed 34. Weather calendar, provenance and receipt handoff checks passed 37. |
| EPSM | Clean installed platform suite passed **9**. The subsequent installed portable-record/CRS handoff suite passed **4** after the EPSM and DB wheels were refreshed. Actual annual EnergyPlus and RC evaluations and automatic LCA reproduced the values above. |
| Database | Offline suite passed 143 with 14 skipped and 34 deselected; a subsequent focused run passed 12. The final installed portable-record/CRS handoff suite passed 4 after the EPSM and DB wheels were refreshed. Live PostGIS checks remain separate. |
| RC | Clean installed suite passed **293**, with **23 optional legacy tests skipped** because `hplib` was absent; sandbox cache warnings were reported. All 6 installed adapter tests passed. The earlier development suite passed 315 before the new read-only-array regression. The clean environment uses pandas 3.0.6 and pvlib 0.16.1. |
| LCA | Assessment suite passed 17 both locally and from the clean installed wheel; EPSM integration subset passed 4. |
| Workflows | Focused execution/transport/resume suite and clean installed rerun each passed **20**, including logging, remote conflicts and runtime identity. |
| Studies | Protocol suite passed 6, also from the clean installed wheel. Archived resource smoke check resolved 9 materials. Transfer manifests verified all 263 archived source files. |
| smhi2epw | Offline suite passed 46. Source unchanged; no live provider acquisition was performed. |
| Handbook | `python3 scripts/check_docs.py`: 23 Markdown files, 165 local links, 10 Python syntax examples, 35 template doctests and 3 notebook/templates with 10 cells passed. `python3 -m unittest discover -s tests -v`: 11 passed. `python3 scripts/run_examples.py`: both teaching notebooks passed. |

The handbook's new footprint/quantity example was also run against the installed
development packages. It accepts an explicit metric Shapely Polygon and retains
quantity readiness before energy inputs are complete. The installed platform
walkthrough completed record conversion, quantities, renovation, simulation, LCA
and optimisation: **2 alternatives evaluated, 1 Pareto alternative**. Generated
`outputs/` directories are ignored in the affected repositories.

## Release preparation (14 October 2026)

The reviewed candidate versions are Data `0.4.0`, Core `0.2.0`, LCA `0.1.0`,
RC `0.2.0`, Database `0.1.0`, EPSM `0.1.0`, Workflows `0.2.0`, and Studies
`0.1.0`. The handbook remains draft v0.3. These versions are branch candidates,
not published releases or `main` promotions. Core's historical `v2.0.x` tags
remain untouched. Studio and smhi2epw have no harmonisation branch.

The new archive manifests matched all 1 Data, 78 Studies, and 226 Workflows
preserved files by byte count and SHA256. After removing stale generated build
folders, all eight candidate wheels built; their contents exclude the retired
cohort and legacy study imports. The eight wheels installed together, `pip check`
found no broken requirements, and installed imports resolved to the candidate
versions. The installed platform walkthrough evaluated 2 alternatives and 1
Pareto alternative. The installed reference Building produced 31,888.201130
kWh/year with EnergyPlus and 27,342.393446 kWh/year with RC. Its automatic LCA
remained incomplete without supplied factors, as designed.

After the initial wheel check, LCA and RC wheels were rebuilt for the final
module split and apartment-helper deprecation. Both reinstalled into the clean
environment; `pip check` passed and their public imports resolved. The RC wheel
emitted the intended `DeprecationWarning` for the legacy apartment helper.

Current local checks: Data 247 passed with 5 sandbox-blocked loopback tests,
then all 11 explorer tests passed outside the sandbox; Core 772 passed, 9 skipped
and 21 deselected with one version assertion updated and one sandbox-blocked
loopback test, then both focused cases passed outside the sandbox; LCA 17 passed;
RC initially had 313 passed and 3 skipped; after deprecating its illustrative
apartment helper, the complete RC suite had 293 passed and 23 skipped in the
available Python 3.12 environment; Database offline 141 passed, 14 skipped
and 37 deselected because a test database was unavailable; EPSM 9 passed; Workflows 44
passed after worker-runtime enforcement; Studies 6 passed. Handbook links,
examples and 11 unit tests passed. These commands used coordinated local source
paths or installed wheels as stated; they do not constitute hosted CI.

Required hosted CI, private Core dependency access, and the release PR checks
remain pending. Core's hosted Python 3.13 job on PR #1 failed before testing
because `EPSM_DATA_DEPLOY_KEY` is absent; its Python 3.11 job was cancelled.
Live Vera, PostGIS and SMHI acquisition were not run in this preparation. No
release tag or `main` merge is claimed here.

## Development publication

The harmonisation pull requests expose the coordinated changes for review.
Completed `dev` integrations used normal merge commits; they do not establish
release promotion or hosted CI success.

| Repository | Review | Development status |
| --- | --- | --- |
| Data | [epsm_data #1](https://github.com/SB-Chalmers/epsm_data/pull/1) | Merged to lowercase `dev` at `596705153af49bbf22789481aa610edabbe582c7`; historical `DEV` retained |
| Core | [epsm_core #1](https://github.com/SB-Chalmers/epsm_core/pull/1) | Merged to `dev` at `faac4b5b9a4a7ff22c37e127a99023e72fd24966`; hosted CI blocked on private Data access |
| LCA | [epsm_lca #1](https://github.com/SB-Chalmers/epsm_lca/pull/1) | Merged to `dev` at `f2e646713d20f0480bb245e344f86d45292efcdd` |
| Database | [epsm_db #1](https://github.com/SB-Chalmers/epsm_db/pull/1) | Merged to `dev` at `a51ab68e0ff290d743754177d0e709a78fbf7262` |
| RC | [epsm_rc #1](https://github.com/SB-Chalmers/epsm_rc/pull/1) | Merged to `dev` at `bc65cb2b5ab866ad9909a39b4b7a412beadf84e5`; illustrative apartment helper deprecated |
| EPSM | [epsm #1](https://github.com/SB-Chalmers/epsm/pull/1) | Merged to `dev` at `ec32c61acc77915322bb0a82adf8421bbc3b3def` |
| Workflows | [epsm_workflows #1](https://github.com/SB-Chalmers/epsm_workflows/pull/1) | Merged to `dev` at `a911743677e21f2a99bd738095a10bda8dd57b8e` |
| Studies | [epsm_studies #1](https://github.com/SB-Chalmers/epsm_studies/pull/1) | Merged to `dev` at `75f60e0fc9b9a874b61fec55af7152391d90cea2` |

Core's branch and review are published. Approval for private dependency
credentials remains pending before its hosted CI can pass.

## Release PR gate (14 October 2026)

The following `dev` to `main` candidates are open as drafts. Each head is the
development merge revision in the table above; none is approved for promotion.

| Repository | Release review | Hosted check at opening |
| --- | --- | --- |
| Data | [#2](https://github.com/SB-Chalmers/epsm_data/pull/2) | [Hosted workflow addition #3](https://github.com/SB-Chalmers/epsm_data/pull/3) under review; result pending |
| Core | [#2](https://github.com/SB-Chalmers/epsm_core/pull/2) | Failed before tests: missing `EPSM_DATA_DEPLOY_KEY` |
| LCA | [#2](https://github.com/SB-Chalmers/epsm_lca/pull/2) | No hosted workflow |
| RC | [#2](https://github.com/SB-Chalmers/epsm_rc/pull/2) | No hosted workflow |
| Database | [#2](https://github.com/SB-Chalmers/epsm_db/pull/2) | Existing suite manually dispatched on `a51ab68e0ff290d743754177d0e709a78fbf7262`; failed at collection because Core and EPSM are unavailable to the hosted runner |
| EPSM | [#2](https://github.com/SB-Chalmers/epsm/pull/2) | No hosted workflow |
| Workflows | [#2](https://github.com/SB-Chalmers/epsm_workflows/pull/2) | No hosted workflow |
| Studies | [#2](https://github.com/SB-Chalmers/epsm_studies/pull/2) | No hosted workflow |
| Handbook | [#3](https://github.com/SB-Chalmers/epsm_development/pull/3) | Existing docs workflow has no run on the PR at opening |

The current candidate was checked locally with `python -m pytest -q` using
coordinated package `src` paths (package-specific exclusions and unavailable
services are stated above), `python -m build --wheel --no-isolation`, clean
wheel installation followed by `python -m pip check`, installed public-import
and retired-module checks, `python examples/platform_walkthrough.py`, and both
installed RC and EnergyPlus evaluations. The handbook ran
`python3 scripts/check_docs.py`, `python3 -m unittest discover -s tests -v`,
and `python3 scripts/run_examples.py`. The same matrix must have hosted
evidence before any `main` merge. Harmonisation branches, including the
handbook's `codex/harmonisation-map`, remain until release merges and `dev`
history synchronisation are complete.

## Remaining deployment and adoption work

- Hosted Core CI is configured for read-only SSH dependency checkout using
  `EPSM_DATA_DEPLOY_KEY`. Automatic approval review rejected creating that key and
  storing its private half as a Core repository secret without explicit approval.
  No credential was created; the user approval request remains pending. Core
  PR #1 is published and merged to `dev`, but local test success is not a
  hosted CI result.
- Vera transport and resume have offline checks. SSH staging, Slurm submission
  and retrieval on the live cluster still require a deployment verification.
  Online SMHI acquisition also remains unverified in this pass.
- The new RC and LCA repositories exist privately under SB-Chalmers with checked
  baseline `main` and `dev` branches. Development changes follow the ordinary
  feature-branch review policy; this register does not claim release promotion.
- Continue adopting bounded inspection, detailed public docstrings, structured
  logging and teaching notebooks in untouched legacy modules through small
  changes. Historical study compatibility routes are archived; remaining
  maintained compatibility imports must have an explicitly documented purpose.
- Preserve the archived studies and their existing evidence. There is no active
  task to repair their paths, reproduce their results or port them to the new APIs.
- Keep custom prepared handlers' external engines explicitly identified in
  their environment declarations; the automatic engine check covers the built-in
  EPSM handler.

Update this register when a finding is fixed or a required check runs. Keep the
actual command, revision, environment and limitations with the result rather than
replacing missing evidence with a general “passed” label.

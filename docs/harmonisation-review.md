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
[file map](harmonisation-file-map.md) records transfers and retained compatibility.

## Repository findings

The findings below concern ownership, public APIs, missing-data handling,
retained evidence, import dependencies and examples. They are a focused review,
not certification that every older module meets every handbook convention.

| Repository | Findings and action | Verification and remaining scope |
| --- | --- | --- |
| `epsm_data` | Shared construction classes remain Core-independent. Fixed layered-window graph roundtrips, preserved identities/order/fractions, and corrected explorer expectations after adding SE.07. One current catalogue replaces active historical override chains; preserved studies retain source history. | Construction/serialization and explorer regressions passed; all 720 established numerical source cells remain unchanged. SE.07 has independent recipes and no renovation-state selector. Final run details follow below. |
| `epsm_core` | Fixed dropped explicit zero-window-ratio facade overrides. Preserved physical quantities and occurrence identities through targeted renovations. Unsupported geometry is reported. Fixed AMY calendar inference and weather provenance/receipt preservation after the weather handoff review. | Authoring/readiness/renovation regressions and real EnergyPlus execution passed. Hosted CI still needs private Data dependency access. Complex geometry outside the new bridge remains a declared limit. |
| `epsm` | Fixed source overrides being mistaken for observations, evaluation artifact overwrites, editable result attributes and incomplete cache identities. Common energy accounting and automatic LCA retain separate identities and failures. | Both real annual engines ran through `Building.simulate`; immutable results, multiple evaluations, evidence comparison and path-specific LCA have regression coverage. Clean wheel installation passed; final installed platform regressions and example reruns are being recorded below. |
| `epsm_db` | Fixed portable nested geometry decoding, Stock archetype links, optional integration dependencies and bounded inspection. Database/Stock/BuildingRecord keep one underlying evidence implementation. Model conversion delegates to EPSM. | Offline record/query/adapter regressions passed. No live schema migration or ingestion change was made. Live restricted-account, PostGIS and release-deployment checks are not inferred from offline tests. |
| `epsm_rc` | Preserved the standalone 5R1C numerical solver through renaming. Corrected FTX heat-recovery accounting in the Core adapter, settings identity and unsupported-input reporting. A clean wheel environment exposed a read-only solar array under pandas 3; fixed in `2139c48`. | Standalone and adapter tests passed. Reduced-order assumptions remain explicit; a successful run does not establish agreement with measured buildings or EnergyPlus. |
| `epsm_lca` | Fixed mutable nested contributions, overflow handling and unknown quantity treatment. Missing factors or quantities remain incomplete, and like-for-like replacements retain installation/removal flows. | Assessment and EPSM integration regressions passed. Implemented modules and reference period are explicit; automatic future replacements and end-of-period demolition are outside the current method. |
| `epsm_workflows` | Fixed local/Vera checkpoint identity, weather-change detection, remote result merge conflicts and runtime identity. Preserved successful attempts, added operation logging and bounded tree inspection. | Parametric/GSA, renovation search and offline transport checks exist. No live Vera job has run in this harmonisation pass. |
| `epsm_studies` | Fixed mutable nested PaperStudy protocols and unbounded inspection. Moved historical research implementations and data into their owning repository; corrected remaining archived resource references. | Protocol tests and wheel smoke checks passed. SHA manifests verified 231 Workflows files and 32 Data files at transfer. Preserved research code is not automatically a scientifically revalidated study. |
| `smhi2epw` | Package remains independent. Its monitor found the AMY year/provenance defect at the Core consumer boundary; that fix belongs to Core and EPSM. | Weather generation source remains unchanged. Its 46 offline tests and 37 Core weather handoff tests passed. Receipt/provenance conversion is corrected; new provider acquisition is not claimed. |
| `epsm_development` | Corrected conflicting ownership of weather, obsolete versioned-catalogue guidance, missing RC ownership and old umbrella API sketches. Marked original review, roadmap and synchronization reports as historical. | Required links/syntax, handbook tests and notebook runner are checked separately below. Handbook checks do not execute platform simulations. |
| `epsm_studio` | Replacement remains out of scope. The monitor recorded old `snjsomnath` README/image references, raw EnergyPlus contracts, a duplicate application database name and conflicting database documentation for the future Studio migration. | No changes made. Clean `main`, `origin/main` and the live SB-Chalmers remote all matched `9c72a53`. These deferred findings do not imply Studio already uses the new platform APIs. |

## Evidence record

This register is being completed as the final verification runs finish. Counts
refer to stated commands and environments; rerunning a subset does not create an
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
broken requirements. Installed LCA and Studies tests passed; final EPSM, Workflows,
example and engine reruns are still being recorded. A successful installation is
reported separately from those behavioural checks.

### Scoped package checks at this checkpoint

The coordination agent supplied these results from the local development
environment. They are checkpoints, not a summed platform test count.

| Package | Check and outcome |
| --- | --- |
| Data | Final full `pytest -q`: **251 passed, 1 skipped** in 433.56 seconds. This includes the corrected explorer failures. Shared graph checks had separately passed 20 with 1 skip. |
| Core | The broad suite passed 744 with 9 skipped and 21 deselected; its sandbox-blocked viewer test then passed separately. The subsequent focused authoring/regression run passed 34. Weather calendar, provenance and receipt handoff checks passed 37. |
| EPSM | Current platform regression run passed 8; actual annual EnergyPlus and RC evaluations completed as described above. |
| Database | Offline suite passed 143 with 14 skipped and 34 deselected; a subsequent focused run passed 12. Live PostGIS checks remain separate. |
| RC | Standalone and adapter suite passed 315 tests. After the pandas 3 solar-array correction, 7 installed adapter tests passed with pandas 3.0.6 and pvlib 0.16.1. |
| LCA | Assessment suite passed 17 both locally and from the clean installed wheel; EPSM integration subset passed 4. |
| Workflows | Latest focused execution/transport/resume run passed 20, including logging, remote conflicts and runtime identity. Final installed rerun is pending. |
| Studies | Protocol suite passed 6, also from the clean installed wheel. Archived resource smoke check resolved 9 materials. Transfer manifests verified all 263 archived source files. |
| smhi2epw | Offline suite passed 46. Source unchanged; no live provider acquisition was performed. |
| Handbook | `python3 scripts/check_docs.py`: 23 Markdown files, 165 local links, 10 Python syntax examples, 35 template doctests and 3 notebook/templates with 10 cells passed. `python3 -m unittest discover -s tests -v`: 11 passed. `python3 scripts/run_examples.py`: both teaching notebooks passed. |

The handbook's new footprint/quantity example was also run against the installed
development packages. It accepts an explicit metric Shapely Polygon and retains
quantity readiness before energy inputs are complete.

## Development publication

These draft pull requests expose the coordinated changes for review. They do not
record a merge, release promotion or hosted CI success.

| Repository | Draft review | Base branch |
| --- | --- | --- |
| Data | [epsm_data #1](https://github.com/SB-Chalmers/epsm_data/pull/1) | `main`, because the retained uppercase `DEV` is historical; this is a comparison base, not release promotion |
| RC | [epsm_rc #1](https://github.com/SB-Chalmers/epsm_rc/pull/1) | `dev` |
| LCA | [epsm_lca #1](https://github.com/SB-Chalmers/epsm_lca/pull/1) | `dev` |
| Database | [epsm_db #1](https://github.com/SB-Chalmers/epsm_db/pull/1) | `dev` |
| Workflows | [epsm_workflows #1](https://github.com/SB-Chalmers/epsm_workflows/pull/1) | `dev` |
| Studies | [epsm_studies #1](https://github.com/SB-Chalmers/epsm_studies/pull/1) | `dev` |
| EPSM | [epsm #1](https://github.com/SB-Chalmers/epsm/pull/1) | `dev` |

Core's branch remains local while approval for private dependency credentials is
pending. The handbook review follows this verification checkpoint.

## Remaining deployment and adoption work

- Hosted Core CI requires read access to private `epsm_data`. Automatic approval
  review rejected creating a read-only deploy key and storing its private half as
  a Core repository secret without explicit approval. The approval request is
  pending; local test success is not a hosted CI result.
- Vera transport and resume have offline checks. SSH staging, Slurm submission
  and retrieval on the live cluster still require a deployment verification.
- The new RC and LCA repositories exist privately under SB-Chalmers with checked
  baseline `main` and `dev` branches. Development changes follow the ordinary
  feature-branch review policy; this register does not claim release promotion.
- Continue adopting bounded inspection, detailed public docstrings, structured
  logging and teaching notebooks in untouched legacy modules through small
  changes. Compatibility imports are temporary, named migration routes.

Update this register when a finding is fixed or a required check runs. Keep the
actual command, revision, environment and limitations with the result rather than
replacing missing evidence with a general “passed” label.

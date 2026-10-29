# Harmonised release — 29 October 2026

**Status: RELEASED.** EPSM 0.5.0 (`v0.5.0`, main `1c15659`) is the supported
combination: its `compatibility.json` names Data 0.7.0, Core 0.9.0, RC 0.11.0,
LCA 0.3.0, Database 0.5.0, Workflows 0.5.0, Studies 0.5.0, smhi2epw 1.3.0 and
Viewer 0.1.0 at their tagged sources. The [studio readiness
record](studio-readiness-2026-10-20.md) and the [archetype release
record](archetype-release-2026-10-15.md) remain the dated evidence for the
preceding combinations. The sections below keep the preparation history; the
outcome is at the end.

## Why a coordinated release is needed

The supported combination (EPSM 0.4.0, 21 October) pins Data 0.6.0, Core 0.8.2,
RC 0.9.0 and LCA 0.2.0. Since then:

- Data `dev` replaced its layout with the lean LoD2 catalogue and added the
  renovation catalogue and `epsm_data.contract` (SB-Chalmers/epsm_data#26, #27, #28).
- Core `dev` added the thermal-bridge surcharge, physical boundary roles and
  catalogue renovation (SB-Chalmers/epsm_core#64, #65, #66). It imports
  `epsm_data.contract`, so its CI fails against the supported Data pin.
- LCA `dev` added external carbon references and renovation cost
  (SB-Chalmers/epsm_lca#22, #23). It imports Data's contract and Core's measures,
  so its CI fails against the supported pins.
- RC released 0.10.0 on 26 October without a manifest update, and its `dev` reads
  Core's per-role thermal-bridge uplifts (SB-Chalmers/epsm_rc#80).
- Database's GIS-first data lake (`codex/gis-first-data-lake`, 18 October) was never
  merged, while EPSM's record assembly already reads lake evidence; its uncommitted
  LoD2 stock work sat in a local checkout. The old national ingestion pipeline
  (`sweden_ubem`) still shipped beside the lake.
- EPSM's LoD2 handoff (SB-Chalmers/epsm#41) was opened against `main` with the
  Data, Core and LCA `dev` heads written into the supported manifest, and five
  further record-assembly commits were stranded on branches built from an older
  base (`codex/lod2-catalogue`, `claude/*`).

None of the package versions had been bumped, so the dependency bounds could
not express which combination works together.

## The candidate cohort

| Package | Candidate version | Preparation pull request | Depends on |
| --- | --- | --- | --- |
| Data | 0.7.0 | [epsm_data#29](https://github.com/SB-Chalmers/epsm_data/pull/29) | — |
| Core | 0.9.0 | [epsm_core#67](https://github.com/SB-Chalmers/epsm_core/pull/67) | Data 0.7 |
| LCA | 0.3.0 | [epsm_lca#24](https://github.com/SB-Chalmers/epsm_lca/pull/24) | Data 0.7, Core 0.9 |
| RC | 0.11.0 | [epsm_rc#81](https://github.com/SB-Chalmers/epsm_rc/pull/81) | Data 0.7, Core 0.9 (`platform` extra) |
| Database | 0.5.0 | [epsm_db#27](https://github.com/SB-Chalmers/epsm_db/pull/27): the data lake is the database; `sweden_ubem` retired under `archive/2026-10-29/` | Data 0.7 (`catalogue`), EPSM 0.5 and Core 0.9 (`epsm`) |
| EPSM | 0.5.0 | [epsm#41](https://github.com/SB-Chalmers/epsm/pull/41) and [epsm#44](https://github.com/SB-Chalmers/epsm/pull/44) (records through `epsm_db`) | Data 0.7, Core 0.9, LCA 0.3, RC 0.11, Database 0.5 |
| Weather | 1.3.0 (unchanged) | [smhi2epw#11](https://github.com/SB-Chalmers/smhi2epw/pull/11), #10, #12 restore a passing `main` | — |

Workflows 0.4.0 and Studies 0.4.0 declared `epsm_core<0.9`, so the installed
cohort could not pass `pip check`; both were brought into scope and released as
0.5.0 the same day (see the outcome below). Viewer 0.1.0 keeps its supported pin.

EPSM's `compatibility-candidate.json` on the candidate branch names the exact
heads of the preparation branches. The candidate release verification
(`Release verification` with `candidate_manifest_revision`) installs that cohort
with EnergyPlus 24.2 and runs the platform, archetype, workflow and study gates.
`compatibility.json` keeps the 0.4.0 combination until promotion.

## Evidence recorded so far

Local checks on 29 October (Python 3.11, arm64, no EnergyPlus), each package at
its preparation branch with the others at their candidates:

| Package | Check | Result |
| --- | --- | --- |
| Data 0.7.0 | `pytest` | 708 passed, 7 skipped |
| Core 0.9.0 | `pytest -m "not energyplus"` | 1094 passed, 8 skipped |
| LCA 0.3.0 | `pytest tests` and doctests | 108 passed; 13 passed |
| RC 0.11.0 | `pytest` (local maturin build) | 802 passed, 33 skipped |
| Database 0.5.0 | `pytest`; wheel contents | 73 passed, 19 skipped (PostGIS acceptance needs a validation database); wheel holds only `epsm_db` |
| EPSM 0.5.0 candidate | `pytest` with the cohort and supported Workflows/Studies/Weather tags | 501 passed, 4 deselected |
| EPSM | offline development checks and README table | 182 passed; table matches |

Hosted evidence: the preparation pull requests' own checks, and the EPSM
candidate release verification dispatched on the head of epsm#44. The first
candidate run (29 October, epsm `5e737a4`) stopped at wheel installation because
Workflows 0.4.0 declared `epsm_core<0.9`; no engine gate ran. The runs that did
install the cohort are in the outcome below. A metadata report or a local run
without EnergyPlus does not establish the engine gates.

## Release order

Each step followed [branches and releases](branches-and-releases.md): merge the
preparation pull request into `dev`, open the release pull request from `dev` to
`main`, merge it with a normal merge, tag `vX.Y.Z`, then bring `main` back into
`dev`. Steps 1 to 6 were planned on the morning of 29 October; Workflows and
Studies were brought into scope in the afternoon because their `epsm_core<0.9`
bounds stopped the cohort from installing.

## Outcome

| Package | Released | Tag commit | Release pull request | Preparation evidence |
| --- | --- | --- | --- | --- |
| Weather | 1.3.0 unchanged; `main` and `dev` at `45656c1` | — | smhi2epw#11, #13, #12 | — |
| Data | 0.7.0 | `7fb6817` | [epsm_data#30](https://github.com/SB-Chalmers/epsm_data/pull/30) | Release verification [40854119098](https://github.com/SB-Chalmers/epsm_data/actions/runs/40854119098) |
| Core | 0.9.0 | `21fbed6` | [epsm_core#69](https://github.com/SB-Chalmers/epsm_core/pull/69) | Release verification, `development_dependencies` [40859788914](https://github.com/SB-Chalmers/epsm_core/actions/runs/40859788914) |
| RC | 0.11.0 | `dcb47ba` | [epsm_rc#82](https://github.com/SB-Chalmers/epsm_rc/pull/82) | Release verification, candidate manifest [40861689808](https://github.com/SB-Chalmers/epsm_rc/actions/runs/40861689808); native wheels [40863726346](https://github.com/SB-Chalmers/epsm_rc/actions/runs/40863726346) |
| LCA | 0.3.0 | `9854bc7` | [epsm_lca#26](https://github.com/SB-Chalmers/epsm_lca/pull/26) | Release verification, `development_dependencies` [40864041148](https://github.com/SB-Chalmers/epsm_lca/actions/runs/40864041148) |
| Database | 0.5.0 | `a3dcdb7` | [epsm_db#29](https://github.com/SB-Chalmers/epsm_db/pull/29) | PR `ci` green; PostGIS acceptance run locally against the workflow's `postgis/postgis:17-3.5` image, fixture- and `epsm-db init`-initialised: 84 passed, 8 skipped. The hosted lane could not install the cohort before EPSM 0.5.0 was on `main`. |
| Workflows | 0.5.0 | `1ea589e` | [epsm_workflows#20](https://github.com/SB-Chalmers/epsm_workflows/pull/20) | Full suite locally against the cohort: 134 passed. Compatibility release only ([epsm_workflows#19](https://github.com/SB-Chalmers/epsm_workflows/pull/19)). |
| Studies | 0.5.0 | `6bccba1` | [epsm_studies#21](https://github.com/SB-Chalmers/epsm_studies/pull/21) | Full suite locally with Workflows 0.5.0: 77 passed. Compatibility release only ([epsm_studies#19](https://github.com/SB-Chalmers/epsm_studies/pull/19)). |
| EPSM | 0.5.0 | `1c15659` | [epsm#46](https://github.com/SB-Chalmers/epsm/pull/46) after [epsm#41](https://github.com/SB-Chalmers/epsm/pull/41), [#44](https://github.com/SB-Chalmers/epsm/pull/44) and the promotion [#45](https://github.com/SB-Chalmers/epsm/pull/45) | Candidate release verification at the tagged sources, Python 3.11 and 3.13, EnergyPlus 24.2: [40886432131](https://github.com/SB-Chalmers/epsm/actions/runs/40886432131) (`ed1bd7a`); earlier run on the pre-release heads [40879513275](https://github.com/SB-Chalmers/epsm/actions/runs/40879513275) |

Every repository above has `dev` and `main` at the same commit, and the merged
preparation branches are deleted.

### Deviations and findings

- **Consumer `ci` checks were red by construction.** Core, LCA, RC, Workflows and
  Studies read EPSM `main`'s supported manifest, which pinned the 0.4.0 cohort
  until EPSM 0.5.0 was promoted. Their preparation pull requests were merged on
  the release-verification evidence above, and the failed `ci` runs on the open
  fallback pull requests ([epsm_core#70](https://github.com/SB-Chalmers/epsm_core/pull/70),
  [epsm_lca#25](https://github.com/SB-Chalmers/epsm_lca/pull/25)) were rerun after
  promotion. The fallback proposal itself is [epsm_development#34](https://github.com/SB-Chalmers/epsm_development/pull/34).
- **One example was stale.** The first candidate run to install the whole cohort
  failed only in `00_geometry_and_archetype.ipynb`, which asserted that archetype
  application leaves `hvac` unset; Data 0.7.0 archetypes carry a ventilation
  template, so the example now checks the installed topology and the still
  unchosen heating delivery (epsm `8e22ce4`).
- **Formatting debt surfaced at release time.** Core (one import order), RC (2
  files) and LCA (11 files) needed `ruff` fixes before their release checks
  passed; Workflows and Studies carry no formatter in CI.
- **Hosted checks in private repositories.** From 29 October every job in
  `epsm_workflows` and `epsm_studies` ended within seconds with no step
  executed, including the dependency-light `ci`; public repositories ran
  normally. Treat this as an account spending restriction per [branches and
  releases](branches-and-releases.md): fix the configuration, do not rerun. Their
  0.5.0 releases rest on local suites and on EPSM's candidate verification, which
  installs both packages.
- **Database PostGIS acceptance** ran locally only, for the reason in the table.
  Dispatch `Release verification` on Database `main` now that EPSM 0.5.0 is
  supported, and record it here.

### Left for the maintainer

- Delete the superseded EPSM branches `codex/lod2-catalogue`,
  `claude/catalogue-templates`, `claude/lake-record-runner` and
  `claude/se07-single-state` (their commits are carried by epsm#44), and
  Database's `codex/lod2-catalogue`. They are not ancestors of `dev`, so the
  pruning rule asks for a maintainer decision.
- Create the GitHub release pages for `v0.7.0` (Data), `v0.9.0` (Core),
  `v0.11.0` (RC), `v0.3.0` (LCA), `v0.5.0` (Database, Workflows, Studies, EPSM).
- The 22 October `codex/training-data-authoring` drafts
  ([epsm#43](https://github.com/SB-Chalmers/epsm/pull/43),
  [epsm_core#68](https://github.com/SB-Chalmers/epsm_core/pull/68),
  [epsm_development#32](https://github.com/SB-Chalmers/epsm_development/pull/32))
  and the design assets on [epsm#42](https://github.com/SB-Chalmers/epsm/pull/42)
  are still undecided.
- The October catalogue validation study stays in a local Studies worktree by
  decision; it changes nothing under `src/`. Its scripts drive EnergyPlus through
  the legacy record route rather than a Workflows plan; the gaps that led there
  (catalogue application as a workflow input, cohort sampling, cross-year
  measurement weather, per-carrier EPC comparison, process execution) are a
  Workflows 0.6 topic.

# Harmonised release preparation — 29 October 2026

**Status: CANDIDATE.** This record describes the coordinated release that brings
the renovation-era work on each package's `dev` branch into one supported EPSM
combination. Nothing below is a supported combination until EPSM's candidate
release verification passes and `compatibility.json` on EPSM `main` names the
released tags. The [studio readiness record](studio-readiness-2026-10-20.md) and
the [archetype release record](archetype-release-2026-10-15.md) remain the dated
evidence for the preceding combinations.

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

Workflows 0.4.0, Studies 0.4.0 and Viewer 0.1.0 keep their supported pins. Workflows 0.4.0 and Studies 0.4.0 declare `epsm_core<0.9`, so the
installed cohort cannot pass `pip check` until those two packages release with
updated bounds; that work is outside this record.

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
Workflows 0.4.0 declares `epsm_core<0.9`; no engine gate ran. Record the run
identifiers and receipts here before promotion. A metadata report or a local run
without EnergyPlus does not establish the engine gates.

## Release order

Each step follows [branches and releases](branches-and-releases.md): merge the
preparation pull request into `dev`, open the release pull request from `dev` to
`main`, merge it with a normal merge, tag `vX.Y.Z`, then merge `main` back into
`dev`.

1. Weather: merge smhi2epw#11, then #10, then #12. No new tag.
2. Data 0.7.0 (`v0.7.0`).
3. Core 0.9.0 (`v0.9.0`). Its `dev` checks read Data's supported pin and stay red
   until step 7; use `Release verification` with `development_dependencies` as
   the release check.
4. LCA 0.3.0 (`v0.3.0`), as for Core.
5. RC 0.11.0 (`v0.11.0`), as for Core.
5b. Database 0.5.0 (`v0.5.0`): merge epsm_db#27, release with the PostGIS
   acceptance job green, then delete `codex/gis-first-data-lake` and
   `codex/lod2-catalogue` (their content is in the release).
6. EPSM: merge epsm#41 then epsm#44 into `dev`. Replace the candidate revisions
   with the released tags, run the candidate verification again, then promote
   `compatibility.json`, regenerate the README table and release 0.5.0 (`v0.5.0`).
7. Consumers adopt the promoted manifest on their next normal CI run.
8. Delete the superseded EPSM branches `codex/lod2-catalogue`,
   `claude/catalogue-templates`, `claude/lake-record-runner` and
   `claude/se07-single-state`; their commits are carried by epsm#44.

## Work preserved but not decided

The `codex/training-data-authoring` branches of 22 October are open as draft
pull requests so they are reviewable rather than stranded:
[epsm#43](https://github.com/SB-Chalmers/epsm/pull/43),
[epsm_core#68](https://github.com/SB-Chalmers/epsm_core/pull/68) (conflicts with
`dev`) and [epsm_development#32](https://github.com/SB-Chalmers/epsm_development/pull/32).
Decide whether that effort continues or is closed. Database's uncommitted stock
work is preserved as commit `fd21917` on `codex/lod2-catalogue` and carried onto the
lake stock in epsm_db#27. The design assets on
[epsm#42](https://github.com/SB-Chalmers/epsm/pull/42) follow the dev-first policy
and carry no platform change.

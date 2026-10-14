# Repository synchronization — 14 October 2026

This records the preparation requested by the maintainer before the harmonisation refactor. The maintainer explicitly requested committing the current local work, making `main` the latest baseline, and synchronizing the repositories to SB-Chalmers. This one-time baseline update does not change the ordinary [development and release policy](branches-and-releases.md) or certify a scientific release.

## Repositories

Canonical checkout names under `/Users/ssanjay/GitHub` now match their hosted names. Each has Git initialized, an SB-Chalmers `origin`, and `main` checked out. Existing public/private visibility was retained; newly created repositories are private.

| Repository | Main baseline | Preparation |
| --- | --- | --- |
| [epsm](https://github.com/SB-Chalmers/epsm) | `8d44c59b3d52` | Initialized the empty folder with README, license and ignore rules; no implemented Python API yet |
| [epsm_db](https://github.com/SB-Chalmers/epsm_db) | `cd74e7e07ab8` | Preserved local history, stock exploration, source changes, remote pipeline, tests and a cleaned notebook; created private remote |
| [epsm_data](https://github.com/SB-Chalmers/epsm_data) | `c0c5c4476bc5` | Main now matches dev_sanjay; preserved the former main as dev_djamila; published both baseline tags |
| [epsm_core](https://github.com/SB-Chalmers/epsm_core) | `f98bc40efbdd` | Published six existing local commits and committed multifamily layout experiments, scripts, tests and fixtures |
| [epsm_workflows](https://github.com/SB-Chalmers/epsm_workflows) | `1e49fa212f26` | Transferred the existing private personal repository to SB-Chalmers; published ten existing local commits and committed the remaining source, configurations, examples, tests and documentation |
| [epsm_studies](https://github.com/SB-Chalmers/epsm_studies) | `e020919276e7` | Initialized the empty folder with README, license and ignore rules; study transfers remain to be agreed |
| [smhi2epw](https://github.com/SB-Chalmers/smhi2epw) | `434d7b26de1a` | Existing main already synchronized; runtime source unchanged |
| [epsm_studio](https://github.com/SB-Chalmers/epsm_studio) | `9c72a53a6dfb` | Committed the local development Docker fix; merged main and development while retaining SAML fixes and newer modelling/UI work |
| [epsm_development](https://github.com/SB-Chalmers/epsm_development) | The commit containing this record | Published the agreed naming, implementation inventory, file map and synchronization record on main and dev |

The renamed local directories are `EPSM-Development` → `epsm_development`, `EPSM_data` → `epsm_data`, and `sweden_building_combined` → `epsm_db`. The old database path remains a compatibility symlink to `epsm_db`: active pipeline paths and the existing environment still use it. The handbook uses its new path directly.

Data's former main is preserved exactly at `ca8e2364de37375ec1bf6df019b7ad58115d48d2` on `dev_djamila`. Its new main equals `dev_sanjay` at `c0c5c4476bc5cf667a09f3b33fb47dad2c5e5f3f`. This was a fast-forward and required no forced history replacement. The published tags are `epsm-data-baseline-v1.3` and `epsm-data-baseline-v1.5.0`. The historical uppercase `DEV` branch remains unchanged; its case conflicts with a new local lowercase `dev` on this filesystem, so Data retains `dev_sanjay` as its current development line pending branch-policy cleanup.

Studio's combined main includes both the previous main and development histories. Older experimental local branches were retained separately; this synchronization does not merge every historical branch into main. Other repositories use `dev` alongside main, with Studio retaining its existing `development` name as well.

## Files retained outside Git

Ignore rules cover local environments and credentials, raw data, generated exploration runs, simulation output, caches and build products. Reusable source, tests, deliberately retained fixtures, configuration and teaching examples remain committed.

Database's generated `docs/analysis/` result files and Studio's Celery scheduler state and `backend/test_output/` geometry output were removed from the index and retained on disk. Existing historical commits were preserved; this operation does not purge artifacts already present in history. Database's original `notebooks/new_notebook.ipynb` is retained locally and ignored. Its reusable content is committed as `notebooks/explore_stock.ipynb`, with outputs cleared and the connection supplied through `UBEM_DATABASE_URL`.

No source bundle, database cluster or simulation output directory was deleted. The running database and pipeline were not restarted or migrated.

## Verification performed

| Scope | Result and limits |
| --- | --- |
| Core multifamily layouts | `tests/core/test_mfh_layouts.py`: 6 passed; 11 new Python experiment/script/test files compiled in memory |
| Database source/API operations | Remote-pipeline, snapshot-path, EPC-heating and record-API tests: 28 passed with database connections blocked; only synthetic inputs and temporary files used |
| Workflows offline baseline | Minimal-campaign, validation, EPC-publication, stock-workflow and cohort-transfer tests: 81 passed, 2 skipped, 5 failed because `pvlib` is absent from the available environment; 1 real EnergyPlus batch test deliberately excluded |
| Studio combined frontend | 5 tests passed; Vite production build passed using a temporary tracked-file checkout and existing dependencies |
| Studio merge | 16 Python files compiled in memory; retained SAML settings/views, portable Docker media paths, development GeoJSON route and Docker build changes were inspected |
| Handbook | Local-link/example checker, 11 unit tests and two teaching notebooks passed |
| Git | Working trees and remote main revisions checked after publication; ignored local artifacts do not make the working tree dirty |

These checks do not establish a fully passing platform integration suite. Workflows needs its missing weather dependency and declared real-data fixtures for the remaining checks. The Studio build reports existing bundle-size and import warnings. Live SAML authentication, production Docker deployment, source re-import and EnergyPlus scientific validation were not exercised during this Git preparation. No release tag was created for this synchronization.

## Next harmonisation step

Agree Database versus EPSM stock responsibilities and the location of reusable assumptions using [D03 and D04](harmonisation.md#decisions-to-discuss) and the [file map](harmonisation-file-map.md). Database's current distribution/import/command remain `sweden-ubem`, `sweden_ubem`, and `sweden-ubem`; their migration needs compatibility decisions and integration checks. Common data models, package transfers and public API refactors remain proposed.

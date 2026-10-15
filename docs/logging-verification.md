# Coordinated logging verification

Checked locally on 15 October 2026 using built wheels in an isolated Python
3.13 environment. Package imports resolved under `site-packages`; `pip check`
passed. Physical-result regression checks confirmed that changing logging
verbosity did not change RC scalars, run identity or the Building snapshot.

## Executed checks

| Owner | Full installed suite | Final logging-focused checks |
| --- | --- | --- |
| Data | 252 passed, 6 skipped | 6 passed |
| Core | 860 passed, 9 skipped; 29 engine tests deselected | 5 passed |
| RC | 415 passed, 28 skipped; 4 engine tests deselected | 3 passed |
| LCA | 81 passed | 28 passed |
| Database | 203 passed, 14 skipped | Includes real synthetic PostGIS ingestion, queries and native backup/restore |
| Weather | 265 passed; 12 live-provider/engine tests deselected | 20 passed, including offline provider replay and thread context |
| Studies | 10 passed | 10 passed |
| EPSM | 42 passed in the initial full run | 18 passed, including queue workers, real handoffs and numerical invariance |

The focused checks followed the final formatter, output-summary and throttled
progress changes. Final review also checked captured-context snapshots, district
worker preparation and avoidance of result-property evaluation. Full package suites and focused checks are separate results;
counts must not be added as independent scientific validation evidence.

Four EPSM notebooks, including the new logging notebook, and five LCA notebooks
ran successfully in fresh kernels. LCA's nine installed docstring checks and
Sphinx API build passed. Handbook link, unit and example checks passed. Core,
Data, EPSM, LCA and Weather checks retain their existing lint requirements.

The database tests used a separate temporary PostgreSQL 17/PostGIS instance,
synthetic fixtures and native backup tools. They did not access national source
data. Live provider acquisition, local EnergyPlus execution and Slurm execution
were not performed. Skipped tests and unperformed integrations remain unverified.

## Hosted review gates

The coordinated PRs remain drafts. GitHub refused to allocate runners for
several jobs, with an annotation stating that recent account payments failed
or the spending limit needs increasing. These jobs have no runner name, no
executed steps and no test logs; their failures do not establish a code failure.
Examples are the [LCA job](https://github.com/SB-Chalmers/epsm_lca/actions/runs/38687755896/job/116266412272),
[RC job](https://github.com/SB-Chalmers/epsm_rc/actions/runs/38687746613/job/116266384382)
and [Studies job](https://github.com/SB-Chalmers/epsm_studies/actions/runs/38687764463/job/116266438940).

Hosted checks must be rerun after the account issue is resolved before claiming
that the PRs have passed their hosted review gates. Local checks are recorded
separately above. No stable-branch promotion is part of this work.

## Source revisions

All feature branches started from freshly fetched lowercase `dev` and target
`dev` for review. Existing checkouts and their unrelated local changes were
preserved. The umbrella's `logging-compatibility.json` pins the collaborating
feature commits; its dedicated CI job records installed paths, versions and
exact source revisions before running handoff tests and notebooks.

| Repository | Development base | Logging implementation commit |
| --- | --- | --- |
| `epsm_data` | `909179951815332a3b8d3bf106e06aa4f7e969dd` | `98c1f5b4cc215545e769de7ad61788c5e1a7b831` |
| `epsm_core` | `4f7f746d1158893f73e0cf601b62fe41c35f5c73` | `339f63241999050ac7038ecfd40184ce1764b89c` |
| `epsm_rc` | `026d9fc93ad8c07913ecb56e20b57288b45dc318` | `d24c351764086f30c6c7be358d0e82a5d6019b8c` |
| `epsm_lca` | `fb4a8b6b4da8a094d98877a08de67b78b34e426b` | `7faa48f48f8da93d1ea495595b94a8d18ce5a5cf` |
| `epsm_db` | `5c67ad94dbc3c48bc8de8ba7a5688a37207f2c03` | `aa369ec11846d30bd74ab5c55b21e89c8dc8580a` |
| `smhi2epw` | `434d7b26de1a6da88e156bebc39e246c615c4ba0` | `e404efd4a095037a2fc46a11a812f90dbf21fb2f` |
| `epsm_studies` | `8abbcea3bd2c204e9e34e903ed03f3d10f0de708` | `ab14536347f7916df0e71c295f442f9f9dd409d0` |

The umbrella and handbook record their own final commits through their PR heads.
Database `dev` advanced during implementation; its metadata update to 0.2.0
was merged into the logging branch, preserving both release and logging
documentation. The logging changes introduce no schema migration.

No stable release was promoted or tagged. GitHub branch API checks reported
`protected: false` for `main` and `dev` in all nine affected repositories. This
change follows the feature/PR process; repository protection remains an
administrative policy gap, not an enforced guarantee.

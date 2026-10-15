# Coordinated logging verification

Checked locally on 15 October 2026 using built wheels in an isolated Python
3.13 environment. Package imports resolved under `site-packages`; `pip check`
passed. Physical-result regression checks confirmed that changing logging
verbosity did not change RC scalars, run identity or the Building snapshot.

## Executed checks

| Owner | Full installed suite | Final logging-focused checks |
| --- | --- | --- |
| Data | 252 passed, 6 skipped | 6 passed |
| Core | 859 passed, 9 skipped; 29 engine tests deselected | 3 passed |
| RC | 415 passed, 28 skipped; 4 engine tests deselected | 3 passed |
| LCA | 81 passed | 28 passed |
| Database | 203 passed, 14 skipped | Includes real synthetic PostGIS ingestion, queries and native backup/restore |
| Weather | 265 passed; 12 live-provider/engine tests deselected | 20 passed, including offline provider replay and thread context |
| Studies | 10 passed | 10 passed |
| EPSM | 42 passed in the initial full run | 16 passed, including queue workers, real handoffs and numerical invariance |

The focused checks followed the final formatter, output-summary and throttled
progress changes. Full package suites and focused checks are separate results;
counts must not be added as independent scientific validation evidence.

Four EPSM notebooks, including the new logging notebook, and five LCA notebooks
ran successfully in fresh kernels. LCA's nine installed docstring checks and
Sphinx API build passed. Handbook link, unit and example checks passed. Core,
Data, EPSM, LCA and Weather checks retain their existing lint requirements.

The database tests used a separate temporary PostgreSQL 17/PostGIS instance,
synthetic fixtures and native backup tools. They did not access national source
data. Live provider acquisition, local EnergyPlus execution and Slurm execution
were not performed. Skipped tests and unperformed integrations remain unverified.

## Source revisions

All feature branches started from freshly fetched lowercase `dev` and target
`dev` for review. Existing checkouts and their unrelated local changes were
preserved. The umbrella's `logging-compatibility.json` pins the collaborating
feature commits; its dedicated CI job records installed paths, versions and
exact source revisions before running handoff tests and notebooks.

| Repository | Development base | Logging implementation commit |
| --- | --- | --- |
| `epsm_data` | `909179951815332a3b8d3bf106e06aa4f7e969dd` | `1db9718423b5ded936a44292ef2eccb2caf58362` |
| `epsm_core` | `4f7f746d1158893f73e0cf601b62fe41c35f5c73` | `9bb323da9edece6a37851c7940fa5b2315b80fe8` |
| `epsm_rc` | `026d9fc93ad8c07913ecb56e20b57288b45dc318` | `f2c4fc6bd5953ba75150effae73ce571594bea77` |
| `epsm_lca` | `fb4a8b6b4da8a094d98877a08de67b78b34e426b` | `989e60030325e6d7371ee58f267f30b79b50867c` |
| `epsm_db` | `5c67ad94dbc3c48bc8de8ba7a5688a37207f2c03` | `b53d68af889d854b302c537b444039ee51202198` |
| `smhi2epw` | `434d7b26de1a6da88e156bebc39e246c615c4ba0` | `c26aa77c6b2bdc90461681a762c9941741f31000` |
| `epsm_studies` | `8abbcea3bd2c204e9e34e903ed03f3d10f0de708` | `53596c564521ab6287a2551fc64ea9827a315492` |

The umbrella and handbook record their own final commits through their PR heads.
No stable release was promoted or tagged. GitHub branch API checks reported
`protected: false` for `main` and `dev` in all nine affected repositories. This
change follows the feature/PR process; repository protection remains an
administrative policy gap, not an enforced guarantee.

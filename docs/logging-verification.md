# Coordinated logging verification

Checked locally on 15 October 2026 using built wheels in an isolated Python
3.13 environment. Package imports resolved under `site-packages`; `pip check`
passed. Physical-result regression checks confirmed that changing logging
verbosity did not change RC scalars, run identity or the Building snapshot.

## Executed checks

| Owner | Full installed suite | Final logging-focused checks |
| --- | --- | --- |
| Data | 263 passed, 6 skipped | 6 passed |
| Core | 891 passed, 9 skipped, including real EnergyPlus cases | 6 passed |
| RC | 420 passed, 28 skipped, including required annual engine comparisons | 4 passed |
| LCA | 83 passed | Includes two completion-summary regressions |
| Database | 203 passed, 14 skipped | Includes real synthetic PostGIS ingestion, queries and native backup/restore |
| Weather | 265 passed; 7 additional engine cases passed; 5 live-provider cases excluded | Offline replay, thread context, type checking and engine notebook passed |
| Studies | 10 passed | 10 passed |
| EPSM | 45 passed | Includes queue workers, real handoffs and numerical invariance |

The focused checks followed the final formatter, output-summary and throttled
progress changes. Final review also checked captured-context snapshots, district
worker preparation and avoidance of result-property evaluation. Full package
suites and focused checks are separate results;
counts must not be added as independent scientific validation evidence.

Four EPSM notebooks, including the new logging notebook, the Data operating-profile
notebook and five LCA notebooks ran successfully in fresh kernels. LCA's nine installed docstring checks and
Sphinx API build passed. Handbook link, unit and example checks passed. Core,
Data, EPSM, LCA and Weather checks retain their existing lint requirements.

The database tests used a separate temporary PostgreSQL 17/PostGIS instance,
synthetic fixtures and native backup tools. They did not access national source
data. Core and RC additionally ran against official EnergyPlus 24.2.0-e7ecb2d53b
on macOS ARM64. Weather used its exact 24.2.0-94a887817b engine after verification
against the official archive SHA256. Its EnergyPlus application notebook passed
in a fresh kernel, and a 94-event weather-to-Core trace retained the linked
operation identities and compiled model. Live provider acquisition and Slurm
execution were not performed.
Skipped tests and unperformed integrations remain unverified.

## Hosted review gates

At the maintainer's explicit request, the coordinated PRs received a manual
implementation review and local release validation before merging into `dev`
and promotion through normal release merges into `main`. This is a recorded
exception to requiring successful hosted checks; it does not turn an unrun job
into a pass or constitute a separate GitHub maintainer approval.

GitHub refused to allocate runners for several jobs, with an annotation stating
that recent account payments failed or the spending limit needs increasing.
These jobs had no runner, no executed steps and no test logs. Examples are the
[LCA job](https://github.com/SB-Chalmers/epsm_lca/actions/runs/38687755896/job/116266412272),
[RC job](https://github.com/SB-Chalmers/epsm_rc/actions/runs/38687746613/job/116266384382)
and [Studies job](https://github.com/SB-Chalmers/epsm_studies/actions/runs/38687764463/job/116266438940).
Hosted matrix checks remain unverified where they could not run. No branch
protection or billing setting was weakened to permit the manual route.

The review corrected missing RC completion identity, LCA completeness
summaries and bulk engine-event verbosity with failing tests first. It also
preserved Database ingestion method source text because that text participates in ingestion source identities.

## Source revisions

All feature branches started from freshly fetched lowercase `dev` and target
`dev` for review. Existing checkouts and their unrelated local changes were
preserved. The umbrella's `logging-compatibility.json` pins the collaborating
reviewed implementation commits; its dedicated CI job records installed paths,
versions and exact source revisions before running handoff tests and notebooks.

| Repository | Development base | Logging implementation commit |
| --- | --- | --- |
| `epsm_data` | `909179951815332a3b8d3bf106e06aa4f7e969dd` | `ac2c7b998f1b92d14650e578f31441d8e78c5f30` |
| `epsm_core` | `4f7f746d1158893f73e0cf601b62fe41c35f5c73` | `88ac5499ba41efb44e099f3579c19f64c50f62e5` |
| `epsm_rc` | `026d9fc93ad8c07913ecb56e20b57288b45dc318` | `d49c8047fa47522873f1d09dfb389db90fde43aa` |
| `epsm_lca` | `fb4a8b6b4da8a094d98877a08de67b78b34e426b` | `aff0330b0eed51477e3de3ba786f4c3fbc38c941` |
| `epsm_db` | `5c67ad94dbc3c48bc8de8ba7a5688a37207f2c03` | `6c1a38f8e4d2b1ef8bbeefc13d334a92ef89d59d` |
| `smhi2epw` | `434d7b26de1a6da88e156bebc39e246c615c4ba0` | `eced17d8c1946c42a0068e3066e39e1f709f2e37` |
| `epsm_studies` | `8abbcea3bd2c204e9e34e903ed03f3d10f0de708` | `8856f2e17987fbad701c4593997da9bf4855bb37` |

The umbrella and handbook record their own final commits through their PR heads.
Database, Data, LCA, EPSM and handbook `dev` advanced during implementation;
those changes were merged into the logging branches before the final installed
validation. The final Data suite includes its operating-profile consolidation.
Logging introduces no database schema migration.

GitHub branch API checks reported
`protected: false` for `main` and `dev` in all nine affected repositories. This
change follows the feature/PR process; repository protection remains an
administrative policy gap, not an enforced guarantee.


The [manual review receipt](logging-release-review.json) records the exact
source trees, built-wheel checksums, selected engines and known hosted-check
limitations. Release merges must preserve these tested trees. Package version
tags identify the resulting stable commits; released history is then brought
back into `dev`.

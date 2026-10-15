# Archetype releases — 15 October 2026

Data, Core, Database and EPSM are published on GitHub in the order below. Their
release and synchronization PRs used normal merge commits. Remote `main` and
`dev` have identical file contents; their history commits may differ. Handbook
0.5.0 completes the sequence using its own verified tag and source archive.
No package-index publication is included.

| Repository | Version | Released main commit | Publication |
| --- | --- | --- | --- |
| Data | 0.6.0 | `bc8449402b9e0dbe0ea85ff76c954cf36d209f86` | [GitHub release](https://github.com/SB-Chalmers/epsm_data/releases/tag/v0.6.0) |
| Core | 0.4.0 | `76b9c93978d26d5f27f0616b51fbb1ca19fb6801` | [GitHub release](https://github.com/SB-Chalmers/epsm_core/releases/tag/v0.4.0) |
| Database | 0.3.0 | `9e29a575f5495b76d5a8553bbe6e20dd4f0e1ff0` | [GitHub release](https://github.com/SB-Chalmers/epsm_db/releases/tag/v0.3.0) |
| EPSM | 0.3.0 | `5c81c88168cf3e1d70756c3ed6f1c534bfc0592e` | [GitHub release](https://github.com/SB-Chalmers/epsm/releases/tag/v0.3.0) |

The [release receipt](archetype-release-evidence-2026-10-15.json) retains exact
revisions, versions, wheel/source hashes, tagged workflow links and local result
counts. Each GitHub release carries its own verification receipt and artifacts.
The [development acceptance register](archetype-verification.md) and
[candidate receipt](archetype-release-candidate-evidence-2026-10-15.json) remain
dated historical evidence; their earlier source identities are not relabelled
as release commits.

## Changes and migration

This sequence versions the already merged archetype authoring, shared application,
atomic assignments, consumer migrations and API removals. It adds no scientific
algorithm, physical recipe or public API beyond that merged development work.
Use the current public `Catalogue`, authored archetypes and `Building.apply_archetype`
routes documented in [archetype authoring](archetype-authoring.md). Removed
loader and profile APIs require migration; each package's release notes retains
the exact removal details. Previous release notes and tags remain intact.

EPSM requires Data >=0.6.0 and Core >=0.4.0; its optional Database dependency
requires >=0.3.0. Database's Data/Core integration floors match those versions;
its EPSM extra retains >=0.2.0 as requested. The verified coordinated combination
uses EPSM 0.3.0. This receipt does not establish every older optional EPSM/Data
combination. EPSM's platform manifest, logging manifest and logging workflow use
the exact Data/Core/Database release commits above. The Database release's
pre-existing EPSM compatibility checkout is retained for its earlier compatibility
lane; the full released combination is verified by EPSM's tagged platform jobs.
RC, LCA, Studies and Weather retain their existing releases and exact source pins.

## Verification

All required hosted package jobs passed on Python 3.11 and 3.13, with pinned and
development dependency lanes. Tagged workflows verify the released commits before
publication. EPSM also requires both logging-wheel jobs. Each complete workflow
must succeed; canceled duplicate runs are not counted as passing.

The tagged Data jobs each report 356 passed and 5 skipped; Database reports
208 passed and 14 skipped. Core reports 801 passed, 178 skipped and 29 deselected
in each hosted lane; its broader locally provisioned run is recorded separately
below. EPSM reports 120 passed without skips in each platform lane and 18 passed
in each logging lane. These distinct counts are retained in the release receipt.

The hosted gates cover clean wheel installation and dependency consistency,
maintained lint, Data's independent import/notebook checks, Core's suite,
Database synthetic PostGIS and backup/restore, and EPSM's installed handoffs,
actual RC/EnergyPlus 24.2 runs and fresh-kernel EPSM/LCA notebooks.
The handbook runs documentation and examples on Python 3.11/3.13 and its separate
API-documentation job. Its installed-platform snippets also run locally.

Historical local candidate runs on Python 3.12.3 passed Data 356 (5 optional skips),
Core 970 (9 optional skips; 29 standalone engine tests excluded), Database 208
(14 optional skips) and EPSM 120 (no skips). All three Data notebooks ran with
Core/EPSM absent and blocked, five EPSM and six LCA notebooks ran in fresh kernels,
and both handbook learning notebooks, 11 handbook unit tests and three installed
public snippets passed. Initial Core version-test failure and the complete
corrected rerun remain recorded in the candidate evidence.

The final released wheels were installed together in the isolated local
environment and passed dependency consistency and the installed Database-to-RC
and renovation-LCA handoff. The catalogue and authored archetype RC cases and a
real EnergyPlus 24.2 case passed again. The local executable identified itself as
`EnergyPlus, Version 24.2.0-94a887817b`; hosted jobs retain their actual executable
identity in the uploaded reports. All eight runtime wheel payloads are byte-for-byte
identical to the last locally checked candidates. Artifact hashes may differ
because the builds retain final release metadata and source identities.

These checks establish software integration under explicit teaching assumptions.
They do not establish scientific accuracy against observed buildings. Required
checks were not replaced by skips, and jobs that initially failed to start due to
billing were subsequently rerun successfully rather than counted as passes.

## Review and manual protection gates

The maintainer explicitly authorized the agent to merge and then to resolve all
PRs and prune completed fix branches. For this dated sequence, that instruction
replaces waiting for a separate GitHub approval. No independent GitHub approval
is claimed. Required successful checks and normal release merges remain mandatory.

GitHub reported administrator access but returned HTTP 403 for classic branch
protection and repository rulesets: these private repositories use the
organization's Free plan. Hosted protection is **not enforced**. Its intended
configuration remains pending a plan upgrade: protect both `main` and `dev`, require
PRs, one independent maintainer approval, dismissal of stale approvals and current
required checks; block force pushes and branch deletion; allow normal merge
commits without a linear-history rule. No billing or visibility setting changed.

| Repository | Intended required checks |
| --- | --- |
| Data | Four `package` jobs: Python 3.11/3.13, pinned/development dependencies |
| Core | Four `unit` jobs: Python 3.11/3.13, pinned/development dependencies |
| Database | Four `synthetic` jobs: Python 3.11/3.13, pinned/development dependencies |
| EPSM | `combination`, four `platform` jobs and both `logging` jobs |
| Handbook | `documentation (3.11)`, `documentation (3.13)`, `api-documentation` |

Exact matrix names are retained in the tagged receipts. A code, metadata or pin
change requires new checks. A normal merge that changes only history can reuse
the successful source's checks after comparing the complete file tree; it does
not require repeating the same matrix. Those history-only merges use `[skip ci]`.
Each released tag still receives one explicit full verification before publication.
Do not dispatch another full workflow when a sufficient tag-triggered run already
exists. The handbook avoids duplicate branch-push/PR runs and cancels superseded
runs for the same PR or ref.

## Preserved work and cleanup

The Database primary checkout's unrelated `shm_size: 2g` deployment edit stays
outside this release; its original content hash is checked before and after any
safe fast-forward. Weather's two unpushed commits remain unpublished and unchanged.
Weather, RC, LCA, Studies, Workflows and Studio receive no release changes.

Data's historical uppercase `DEV` remains untouched. Lowercase `dev` is fetched
through the dedicated `origin-dev` alias to avoid the case-insensitive tracking
collision; no conflicting local lowercase branch is created.

Only proven completed fix branches are pruned, with archive references retained.
Six unfinished local fixes and the Database preservation branch remain. Existing
worktree files and historical branches remain available. Studio PR #27 was closed
as obsolete after checking its conflicting, outdated fixtures and placeholder
workflow; its exact patch and head were preserved rather than merged as working
coverage. Cleanup is recorded separately in the workspace audit.

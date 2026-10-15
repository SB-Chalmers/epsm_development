# Archetype release preparation — 15 October 2026

**Status: release candidates; not published.** Development acceptance remains in
the [verification register](archetype-verification.md). This preparation changes
versions, dependency requirements and release documentation, without changing
physical recipes or scientific algorithms. The preceding release records remain
dated historical evidence.

## Release sequence

| Order | Repository | Candidate version | Development acceptance revision |
| --- | --- | --- | --- |
| 1 | Data | 0.6.0 | `9f69479c1d3914d1517670d3139b822d9c88f5f3` |
| 2 | Core | 0.4.0 | `0794e365448f6348dd25c7d9a7dd3aa9f8979525` |
| 3 | Database | 0.3.0 | `9abe1d7e38475d824c2d52c5001b154baf23fa1a` |
| 4 | EPSM | 0.3.0 | `c9c27bd54d6ef02791bdc8610bd198854093b320` |
| 5 | Handbook | 0.5.0 | `8aab6e40872f53679a96f63ccbb5014441a92873` |

Prepare each change on `codex/archetype-release` from current lowercase `dev`
and submit it to `dev`. Before promoting the next package, replace its dependency
pins with the exact approved release commits and rerun the candidate checks.
Candidate or earlier development receipts do not establish tagged-release success.

The release pull request targets `main` from `dev`. Require successful checks
on the actual candidate and one independent maintainer approval before each
merge. The author cannot provide their own independent approval. Use normal
release merges, tag the resulting `main` commits with the versions above, run
checks against those tags, and publish GitHub release notes, wheels and verification
receipts. Do not publish to a package index. Bring released history back into
`dev` through reviewed synchronization pull requests.

## Required verification

Use Python 3.11 and 3.13 for the hosted package matrices. Require clean wheel
installation and dependency checks, maintained lint checks, isolated Data imports
and notebooks, Core tests, Database synthetic PostGIS tests, and EPSM's installed
RC, EnergyPlus 24.2 and fresh-kernel examples. Record exact source revisions,
versions, wheel hashes, engine identity and pass/fail/skip counts. Required checks
cannot be replaced by skips or by an earlier commit's passing workflow.

The handbook requires its documentation, unit, learning-notebook and installed
platform-example checks. API documentation checks remain required in hosted CI.
These checks establish software integration with explicit teaching assumptions;
they do not establish accuracy against observed buildings.

### Completed local candidate checks

An isolated Python 3.12.3 wheel installation passes dependency checks. Data passes
356 tests with five optional skips; Core passes 970 with nine optional skips and
29 standalone engine tests excluded; Database passes 208 with 14 optional skips;
EPSM passes 120 without skips. The Core version assertion initially expected
0.3.0; correcting it to 0.4.0 produced the complete passing rerun.

All three Data notebooks pass with Core/EPSM absent and their imports blocked.
Five EPSM and six LCA notebooks pass in fresh kernels. The installed platform
handoff, both required archetype RC cases and actual EnergyPlus 24.2 pass.
Handbook links, 11 unit tests, both learning notebooks, three installed-platform
snippets and the Sphinx API example pass.

The [candidate receipt](archetype-release-candidate-evidence-2026-10-15.json)
records candidate revisions, wheel hashes and local results. These local checks
do not replace the hosted Python 3.11/3.13 gates or the required independent
maintainer approval. Dependencies still need final approved release identities
before downstream promotion. No release tag or publication is established here.

## Hosted protection limitation and manual gates

The maintainer explicitly selected manual release gates for this synchronization.
On 15 October 2026, GitHub reported administrator access but rejected both classic
branch protection and repository rulesets with HTTP 403: the private repositories
are under the organization's Free plan. Hosted protection is **not enforced**.
No repository is made public and no billing setting is changed by this release.

After the hosting plan permits enforcement, configure both `main` and `dev` to
require pull requests, one independent maintainer approval, dismissal of stale
approvals and successful current checks. Block force pushes and branch deletion;
allow normal merge commits and avoid a linear-history requirement.

| Repository | Required checks on the actual candidate |
| --- | --- |
| Data | Four `package` jobs: Python 3.11/3.13, pinned/development dependencies |
| Core | Four `unit` jobs: Python 3.11/3.13, pinned/development dependencies |
| Database | Four `synthetic` jobs: Python 3.11/3.13, pinned/development dependencies |
| EPSM | `combination`, four `platform` jobs and both `logging` jobs |
| Handbook | `documentation (3.11)`, `documentation (3.13)`, `api-documentation` |

Read exact check names from each candidate; EPSM matrix names contain source pins
and change when those pins change. Manual review verifies current checks and an
independent maintainer approval before merging. Do not claim the unavailable
hosted settings provide an enforced guarantee.

## Preserve local work

The Database primary checkout has an unrelated `shm_size: 2g` deployment edit.
Keep that edit outside the release and verify its content after any safe
fast-forward. Weather has two local commits not on remote `main`; leave them
unpublished and unchanged. RC, LCA, Studies, Weather, Workflows and Studio receive
no release changes in this series.

On the case-insensitive Data checkout, preserve historical uppercase `DEV` and
fetch lowercase `dev` through the separate `origin-dev` remote alias. Do not
create a conflicting local lowercase branch. Preserve existing feature branches,
worktrees and published tags. Final synchronization requires matching file trees
on remote `main` and `dev`; a synchronization merge may leave distinct commit IDs.

# Study platform feature verification, 21 October 2026

**Local capture: the four coordinated scenarios passed on Python 3.11 and 3.13.
Hosted checks and promotion were pending.** This is a dated record of the
candidate scientific libraries, not a release or a deployed Studio application.
The [readiness plan](study-platform-readiness.md) defines the ownership,
supported choices, acceptance scenarios and promotion sequence. The accompanying
[machine-readable record](study-platform-feature-verification-2026-10-21.json)
retains exact source revisions, receipt checksums, wheel checksums and the
distinction between installed and source-level checks.

At the original local capture, there had been no Studio changes, campaign pull
requests, pushes, merges into `dev` or `main`, tags or releases. The publication
update below records subsequent draft pull requests without changing the
captured source or artifact identities. Existing primary working directories
and unrelated work remain intact.

## Candidate sources and ownership

The final local cohort is `candidate-feature-04.json`. The verifier's canonical
manifest digest is
`c0b005488f5346fa1cd9409654215c8f2610299a56da1f7412d3fe3ebb34b3b8`;
the raw-file SHA256 is
`5c0ff1ff08559dd4e2ed9f42b7f66ebf8986bcff129d2f13c24e14a98f9dec2d`.
Each lane built committed source archives into wheels, installed them together
in a new environment, passed `pip check`, and proved that package imports came
from that environment's `site-packages`. Source files supplied the test suites
and scenario entry points; they did not replace the installed libraries.

| Package | Candidate version | Source revision |
| --- | --- | --- |
| EPSM | 0.4.0 | `6380e38f2ff2c68d506ddcdd62b6271777576e70` |
| Data | 0.6.0 | `bc8449402b9e0dbe0ea85ff76c954cf36d209f86` |
| Core | 0.8.2 | `71e04ecccd2c431a45c8a72f03f7534d5f8774f1` |
| RC | 0.9.0 | `c4df386ec8ae2fa35c7f315826fbb30b9a1137a9` |
| LCA | 0.2.0 | `00141d0500e717b4f18a9d69e158f0af2aae1934` |
| Database | 0.3.0 | `9e29a575f5495b76d5a8553bbe6e20dd4f0e1ff0` |
| Workflows | 0.4.0 | `11c16829f0e27cc09db4f8b7a36be67a1c9bd412` |
| Studies | 0.4.0 | `7332f23c4f98f8fcb70acbe5ffbe4ef01bb07321` |
| Weather | 1.3.0 | `b8d37aa3931c2df5bf08c2c307fefa869055ee92` |

Studies owns the outer study document, protocol, portable result collection and
general summaries. Its authoring facade delegates to Workflows, which owns
templates, parameter domains, sampling, physical bindings, frozen cases and
execution attempts. EPSM assembles Buildings and combined evaluations. Core,
RC and LCA retain their calculations and the meanings of their results.

The implementation reuses the existing grid and Latin hypercube samplers,
Building construction and renovation operations, owner schemas and preflight,
prepared execution and Vera adapter, strict engine comparator, and weather
batch/morphing methods. Added interfaces compose those methods; they do not
introduce a second physical model or a separate scientific calculation in
Studies. The reusable EPSM compatibility verifier runs the existing installed,
study, archetype and workflow scenario harnesses.

## Coordinated installed scenarios

| Required scenario | Python 3.11.13 | Python 3.13.5 |
| --- | --- | --- |
| Installed platform | Passed | Passed |
| Six-evaluation study platform | Passed | Passed |
| Archetype handoff | Passed | Passed |
| Workflow handoff | Passed | Passed |

The first complete study evaluates a retained baseline, replacement windows,
and windows plus insulation with both RC and EnergyPlus: six planned cases and
six successful, verified results in each lane. Every case retains annual
delivered energy, 8,760 hourly heating values with units and calendar, and its
declared lifecycle assessment and material contributions. The retained baseline
has zero new material impact by the assessment's explicit retained-material
policy; this is a computed value, not a missing-data substitution.

The same public result collection produced three comparisons of identical
physical cases across engines and four changes from the baseline within each
engine. Required input identities, accepted output coverage, finite values,
calendar continuity and annual/hourly accounting were checked before engine
comparison. These synthetic examples verify execution and accounting; they do
not establish predictive accuracy or require the engines to agree.

A repeated resume created no new attempts. Recollection preserved the same
immutable archive identity. CSV and JSON exports were produced, and a copied
archive reopened in a fresh process with EPSM, Core, RC, LCA and Workflows
imports blocked. All six results and their arrays remained readable and the
archive verified 297 retained files in each lane. The result archive stores
relative, checksummed evidence and keeps its query path independent of the
execution libraries.

The four final gates supersede earlier candidate failures. Earlier receipts
remain unchanged, including the timestamp-text precision comparison failure
and the isolated scenario-entry-point import failure; they are not counted as
successful final gates.

## Owner tests, coverage and examples

Statement and branch coverage below are separate percentages. A coverage
percentage measures exercised code, not scientific accuracy.

| Owner check | Passed | Skipped | Statements | Branches | Provenance |
| --- | ---: | ---: | ---: | ---: | --- |
| EPSM full suite | 343 | 0 | 81.4109% | 69.3095% | Installed final04, Python 3.11 |
| Core full suite | 1,090 | 8 | 91.9230% | 83.8917% | Installed03; exact Core revision unchanged in final04 |
| Workflows full suite | 134 | 0 | 81.2231% | 70.0000% | Installed final04 |
| Studies full suite | 77 | 0 | 80.9105% | 72.2672% | Installed03 coverage; all77 tests repeated in final04 with unchanged Studies source |
| RC full suite | 610 | 0 | 86.1581% | 75.0394% | Source owner suite; final formatting commit preserves identical syntax trees |
| LCA full suite | 83 | 0 | Not collected | Not collected | Earlier owner check of the unchanged source revision |

Core's eight skips are one permanently retired optional Data adapter test and
seven explicitly gated 2018-AMY Kiva smoke cases. Those seven cases did not run
and do not pass a smoke gate. The required annual EnergyPlus checks and optional
geometry prerequisite ran successfully. The new Core output-discovery module
covered 95.3488% of statements and every branch. Existing SQLite connection
ResourceWarnings did not fail the Core suite.

Studies' CLI assertions run subprocesses; those checks pass but subprocess
lines are outside its owner-process coverage. Fresh kernels ran both the Studies
portable-study notebook and the Workflows authoring notebook using explicitly
pinned installed interpreters. Executed notebooks and import proofs remain with
the local receipts. RC's four existing numerical regression modes also matched
their pinned reference for seven annual fixtures and standalone radiation.

The Weather owner separately passed 314 offline tests, two real Future Weather
Generator tests, five provider-network tests, seven EnergyPlus tests, 31 source
doctests and 73 documentation doctests in its installed Python 3.12 environment.
Its application notebook ran in a fresh installed kernel. Batch coverage was
91.6667% statements and 85.4167% branches; morphing coverage was 85.9649% and
76.0000%. These are coverage figures for those two modules, not the whole
Weather package. Third-party JARs remain outside repositories and distributions.

### Additional checks of unchanged dependencies

The extra Data full suite recorded 352 passed, three failed and six optional
skips in 542.6 seconds. All three failures were CLI tests passing relative
`src/epsm_data/datasets` paths while the suite ran from a neutral directory.
Rerunning exactly those three cases from the trusted archived Data directory
passed all three, with isolated Python, pytest's source path setting disabled,
and an installed `site-packages` import proved before collection. The original
failure receipt remains unchanged: 355 distinct cases passed across the two
runs, rather than one clean full-suite result. Five skips require optional
Honeybee and one requires the optional NetworkX graph dependency. The longest
tests performed offline catalogue completeness/calibration and Explorer matrix
work; this was not a provider-network delay. No package source changed.

Database's extra owner run needed its pinned test helpers and repository working
directory. The corrected offline run passed 174 tests, skipped 14 optional EPW
compiler checks, and explicitly deselected 34 PostGIS cases. The retained full
attempt had 34 setup errors because `UBEM_TEST_ADMIN_URL` was absent, plus a
working-directory-dependent SQL schema assertion; it does not establish live
PostGIS coverage. The preceding collection attempt also remains recorded. These
are additional checks of unchanged Data and Database sources, separate from the
four required platform scenarios that passed in both Python lanes.

## Supported scope and remaining promotion work

The completed route supports the registered owner bindings, declared output
requirements, fixed/grid/LHS/Monte Carlo designs, frozen baselines, scoped
portfolio expansion, supplied weather and explicit supported weather acquisition,
local execution, and portable retained results. General helpers cover selection,
coverage, descriptive summaries, temporal aggregates, explicit portfolio totals,
baseline changes, engine pairing and export. Deep statistical analysis remains
outside this scope.

The original journey remains a capability map rather than a promise that every
choice can execute. TMY generation, correlated sampling, arbitrary detailed
zoning, behavioral window opening, heated-attic authoring, measured arbitrary
windows, facade/wall-offset methods and automatic U-value construction targeting
remain explicitly unavailable. Engine-specific unsupported settings and missing
required inputs block preparation. Vera behavior is covered through its public
transport interface; this record does not claim a new live cluster submission.
The capability/schema and readiness operations remain authoritative.

Local feature checks do not complete publication. At local capture, the remaining
sequence was to establish authorized hosted CI access, open the coordinated
review requests, run hosted checks, merge completed features into `dev`, check
the combined sources and conflicts there, and then perform separately reviewed
promotion to `main` and releases. The update below records the draft review
requests. No promotion has happened.

Automatic approval review rejected creating six dedicated read-only GitHub deploy
keys for EPSM, Data, Core, LCA, RC and Workflows, and storing their private keys
as Studies Actions secrets. The stated reason was that the retained instructions
did not explicitly authorize persistent repository access. Human authorization
is pending; zero keys and zero secrets were created. This record contains no
credentials. Until that access is resolved, hosted checks and campaign
publication remain pending rather than passed.

## Publication update, 21 October 2026

All seven campaign branches have since been pushed and these draft pull requests
are open against `dev`. The listed heads were read back from GitHub. This
publication phase does not change the final04 local capture above.

| Package | Draft pull request | Observed head |
| --- | --- | --- |
| Core | [59](https://github.com/SB-Chalmers/epsm_core/pull/59) | `71e04ecccd2c431a45c8a72f03f7534d5f8774f1` |
| RC | [69](https://github.com/SB-Chalmers/epsm_rc/pull/69) | `c4df386ec8ae2fa35c7f315826fbb30b9a1137a9` |
| Weather | [7](https://github.com/SB-Chalmers/smhi2epw/pull/7) | `b8d37aa3931c2df5bf08c2c307fefa869055ee92` |
| Workflows | [13](https://github.com/SB-Chalmers/epsm_workflows/pull/13) | `11c16829f0e27cc09db4f8b7a36be67a1c9bd412` |
| Studies | [13](https://github.com/SB-Chalmers/epsm_studies/pull/13) | `7332f23c4f98f8fcb70acbe5ffbe4ef01bb07321` |
| EPSM | [31](https://github.com/SB-Chalmers/epsm/pull/31) | `6380e38f2ff2c68d506ddcdd62b6271777576e70` |
| Handbook | [28](https://github.com/SB-Chalmers/epsm_development/pull/28) | `20ee9f994e35d4ba6b8567735b9396723f9336a8` before this addendum |

The `platform-candidate` label is applied to EPSM, RC, Workflows and Studies.
Their four `EPSM_CANDIDATE_MANIFEST_SHA` variables each read back as the full
`6380e38f2ff2c68d506ddcdd62b6271777576e70` revision. Prospective merge checks
against freshly fetched `dev` were clean for all seven branches; those checks
did not merge anything and must be repeated if either side changes.

Studies' [hosted run](https://github.com/SB-Chalmers/epsm_studies/actions/runs/39586854373)
passed its standalone Python 3.11 and 3.13 package checks. Its combination job
failed while checking out the private EPSM repository at the selected candidate
revision: GitHub returned `Repository not found` and Git exited 128. The
coordinated integration jobs were consequently skipped. The workflow expects
`EPSM_REPO_DEPLOY_KEY`; with that secret absent, the repository-scoped default
token cannot read the other private repository. This confirms an access failure
before integration tests ran, and does not pass the hosted integration gate.

The [Handbook hosted run](https://github.com/SB-Chalmers/epsm_development/actions/runs/39586894447)
passed documentation checks on Python 3.11 and 3.13 and its API documentation
build at the listed `20ee9f9` head. This addendum produces a new documentation
head; that head requires its own checks after it is pushed. The
[Workflows hosted run](https://github.com/SB-Chalmers/epsm_workflows/actions/runs/39586841483)
passed combination selection and both Python 3.11 and 3.13 installed-wheel
checks, including its full owner suite, at `11c16829`.

The separate EPSM [hosted display run](https://github.com/SB-Chalmers/epsm/actions/runs/39586876691)
also exposed a CI entry-point error: its command omitted the required candidate
manifest argument. That workflow repair is pending and is not counted as a
passed hosted check. Later source changes require a new candidate capture and
fresh checks; they do not rewrite the successful final04 local receipts above.

GitHub's required-check query reported no configured required checks for the
three monitored branches. That is a configuration observation, not a waiver of
the handbook's checks or maintainer review. The pull requests remain drafts.
The six deploy-key/Actions-secret creation actions remain unperformed while
human authorization is pending. There have been no campaign merges into `dev`
or `main`, tags, releases or Studio changes.

## Follow-up candidates 05 and 06

The preceding publication update records the first posted heads and their actual
hosted results. Subsequent CI repairs produced two new candidate captures; the
earlier receipts and source identities remain unchanged.

| Capture | EPSM revision | Core revision | Python 3.11 | Python 3.13 |
| --- | --- | --- | --- | --- |
| Intermediate 05 | `9def4aed9b442f2517fdd697bf77d890d2c5f33a` | `71e04ecccd2c431a45c8a72f03f7534d5f8774f1` | All four scenarios passed | All four scenarios passed |
| Final 06 | `7fe51c540edc9f489956a8af7e42a733d56d87ce` | `34c5ac1633129cec20172d02967fdccbbc38c84d` | All four scenarios passed | All four scenarios passed |

The remaining seven package revisions and all nine candidate version numbers
are unchanged from final04. Intermediate 05's canonical manifest digest is
`22632f6c53b5ea0da53ed419e919203f285033c934b347c4a520ae067a25a51d`
and its raw-file SHA256 is
`13096c5f92b0f8f6d06529b552d2de5eac4ab6ef365bb0126ab23f875b44aa84`.
Final 06's canonical manifest digest is
`6773dd8b281a63c42a8bf1110e645c055ed9a875a3fa211173d78915b341a20f`
and its raw-file SHA256 is
`dc066647aa7e45f3220ad4613ddf866b568e9bcf99cd380c13f848168408a226`.
The companion record retains each completed lane's actual receipt and wheel
checksums, scenario results, study archive identity and independent reopening.

The EPSM changes repaired its hosted display command's missing manifest argument
and metadata checkout history, then refreshed the checked Core candidate pin.
Core's output-capability test now reuses its own synthetic-weather fixture,
without importing the optional RC package into a standalone Core test. These
changes affect CI and test setup. Read-only comparisons confirm that `src/` and
`pyproject.toml` are byte-identical between the final04 and final06 revisions in
both EPSM and Core. The historical owner coverage figures above keep their
original measured heads; they are not relabelled as a new final06 coverage run.

Workflows' [manual final06 run](https://github.com/SB-Chalmers/epsm_workflows/actions/runs/39588731799)
passed combination selection and both Python 3.11 and 3.13 installed-package
jobs at the unchanged `11c16829` source. Its job log confirms the full EPSM
candidate selection `7fe51c540edc9f489956a8af7e42a733d56d87ce`.
The pushed Handbook `ee190f6` also passed both documentation lanes and its API
build in [its hosted run](https://github.com/SB-Chalmers/epsm_development/actions/runs/39587677152).
This follow-up addendum creates a later documentation head that needs fresh
hosted checks after it is pushed.

The final [Core run](https://github.com/SB-Chalmers/epsm_core/actions/runs/39588590788)
passed combination selection and both unit-test lanes at `34c5ac1`. RC's
[final candidate run](https://github.com/SB-Chalmers/epsm_rc/actions/runs/39588721778)
passed combination selection, standalone checks and both package lanes at
`c4df386`. EPSM's [final supported-package run](https://github.com/SB-Chalmers/epsm/actions/runs/39588689186)
passed combination selection, display and both platform lanes at `7fe51c5`;
its [metadata run](https://github.com/SB-Chalmers/epsm/actions/runs/39588689349)
also passed. Both EPSM hosted full suites reported 346 passed, including the
three new CI regression tests, with no skipped-test summary. These are new
hosted test results, not a new coverage measurement: the 343-test final04 owner
coverage row above retains its original provenance.

Weather's [candidate CI run](https://github.com/SB-Chalmers/smhi2epw/actions/runs/39586829408)
passed its release gate, Python 3.11 through 3.14 tests, minimum dependencies,
package/wheel, documentation and EnergyPlus jobs at `b8d37aa`. Its optional
network job and publication jobs were skipped; the separate recorded local
owner run supplies the provider-network evidence. All four candidate selector
variables now read back as `7fe51c540edc9f489956a8af7e42a733d56d87ce`.

Studies' known private-repository checkout failure remains unresolved and was
not rerun. No deploy keys or Actions secrets have been created. All seven pull
requests remain drafts, with no campaign merges, tags, releases or Studio
changes. A successful local candidate and another package's hosted pass do not
replace the blocked Studies integration checks or maintainer review.

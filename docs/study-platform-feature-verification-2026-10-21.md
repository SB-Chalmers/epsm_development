# Study platform feature verification, 21 October 2026

**Status: the four coordinated local scenarios passed on Python 3.11 and 3.13.
Hosted checks and promotion remain pending.** This is a dated record of the
candidate scientific libraries, not a release or a deployed Studio application.
The [readiness plan](study-platform-readiness.md) defines the ownership,
supported choices, acceptance scenarios and promotion sequence. The accompanying
[machine-readable record](study-platform-feature-verification-2026-10-21.json)
retains exact source revisions, receipt checksums, wheel checksums and the
distinction between installed and source-level checks.

No Studio changes, campaign pull requests, pushes, merges into `dev` or `main`,
tags or releases have been made for this campaign. Existing primary working
directories and unrelated work remain intact.

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

Local feature checks do not complete publication. The remaining sequence is to
establish authorized hosted CI access, open the coordinated review requests,
run hosted checks, merge completed features into `dev`, check the combined
sources and conflicts there, and then perform the separately reviewed promotion
to `main` and releases using the compatibility record. No promotion has happened.

Automatic approval review rejected creating six dedicated read-only GitHub deploy
keys for EPSM, Data, Core, LCA, RC and Workflows, and storing their private keys
as Studies Actions secrets. The stated reason was that the retained instructions
did not explicitly authorize persistent repository access. Human authorization
is pending; zero keys and zero secrets were created. This record contains no
credentials. Until that access is resolved, hosted checks and campaign
publication remain pending rather than passed.

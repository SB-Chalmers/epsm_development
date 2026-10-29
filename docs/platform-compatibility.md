# Platform compatibility and consumer CI

**Status: release contract, 20 October 2026.** The central interface is on EPSM
`main`; the next supported package combination is still being checked. The
[readiness record](studio-readiness-2026-10-20.md) tracks its promotion and each
consumer's adoption. This page does not certify an untested package combination.

EPSM owns the reviewed combination in
[`compatibility.json`](https://github.com/SB-Chalmers/epsm/blob/main/compatibility.json).
Each package owns its own version and dependency bounds. A changed `main` branch
is a candidate until the required installed-package, engine and handoff checks
pass. A metadata report cannot establish numerical agreement or scientific
accuracy. The handbook explains the contract; it does not keep a second current
table of package pins.

## Keep release evidence and candidates distinct

| EPSM record | Meaning |
| --- | --- |
| `compatibility.json` | Reviewed versions and immutable source revisions, promoted after the required checks |
| `platform-registry.json` | Repository identities, roles, required extras and explicit retained CI-reference exceptions |
| `build/platform-candidates.json` | Captured current-main metadata and differences from the supported combination |
| `build/ci-references.json` | Dependency references found in workflows at those captured revisions |

The lightweight metadata job reads version declarations, requirements and CI
definitions. It runs one bounded job rather than installing packages or running
engines. Full package tests keep their scientific gates. EPSM's own full workflow
uses two pinned Python lanes, 3.11 and 3.13; a requested main-dependency experiment
uses one 3.13 lane and records the actual source revisions. It does not silently
promote those revisions into the supported manifest.

## Read the manifest once per consumer run

A consumer checks out EPSM `main` read-only into `.ci/platform`, captures that
checkout's full Git SHA once, and uses the matrix generator from the same checkout.
The consumer declares the dependency names it needs; the versions and immutable
revisions come from the central manifest. Its own source remains the PR checkout
under test. For example, the Workflows dependency selection is:

```sh
PLATFORM_MANIFEST_SHA="$(git -C .ci/platform rev-parse HEAD)"
python .ci/platform/scripts/compatibility_matrix.py \
  --manifest .ci/platform/compatibility.json --consumer epsm_workflows \
  --packages epsm_data epsm_core epsm_lca epsm_rc epsm \
  --manifest-revision "$PLATFORM_MANIFEST_SHA" --mode pinned
```

The emitted rows contain `python`, `mode`, `manifest_revision` and each selected
dependency revision. EPSM's `self` entry resolves to the captured manifest checkout
SHA for an external consumer. EPSM's own workflow uses its calling checkout.
This removes the need to guess a future EPSM release-merge SHA or write a
self-referencing commit into the manifest. Unknown names, moving supported pins
and unresolved `self` fail before a matrix is emitted.

Scientific dependency lanes exclude entries with `role: display` by default.
A Core-to-Viewer display check selects the relevant packages explicitly. A
Viewer build does not need to rerun the scientific platform suite merely to
package the same neutral scene renderer.

## Adopt on the next normal CI run

After EPSM promotes a checked combination, each adopted consumer reads it on its
next applicable PR or explicit release verification. There is no cross-repository job dispatch,
callback or waiting cycle. Updating EPSM does not trigger every expensive package
suite at once. Each receipt retains both the manifest SHA and the actual source
revisions tested; an earlier passing run is not relabelled as checking a newer
combination.

Use an explicit repository-specific read-only deploy key to read private EPSM
source and explicit keys for private dependencies. Check required key presence
before checkout and fail with an actionable error if access is missing. The job's
ordinary repository token does not imply access to a sibling private repository.
Do not copy credentials or credential values into the manifest, reports or URLs.
The access setup is separate from publishing a manifest.

Use one lightweight `ci` job on PRs into `dev` or `main`, with cancellation for
superseded revisions. Do not repeat it on feature pushes, labels or merge pushes.
Run full verification explicitly before publication, and run affected integration
checks before merging behavioural changes. Preserve the engine, database,
notebook and installed-wheel checks in the manual release workflow. The
[branch and CI policy](branches-and-releases.md#keep-ci-small) defines the scope.

The [EPSM compatibility guide](https://github.com/SB-Chalmers/epsm/blob/main/docs/platform-compatibility.md)
owns the implementation details and exact guard commands. Historical receipts
and explicitly retained numerical regression references remain dated evidence;
they do not select the current supported combination.

## Development checks during a version transition

A coordinated release raises lower bounds in consumer packages before EPSM has
promoted the new combination: Core 0.9.0 declares `epsm_data>=0.7.0,<0.8` while
the supported manifest still pins Data 0.6.0, and EPSM cannot promote Data alone
while supported RC 0.9.0 declares `epsm_data<0.7`. Installing the supported pin
then fails at dependency resolution, so every consumer that raises a bound has a
red `ci` until promotion. A dependency conflict needs a configuration change, not
a repeated run, and manual dispatch checks do not replace the PR's `ci` result.

The configuration change is a deterministic cohort selection inside `ci`, made
only from committed content:

1. Check out EPSM `main` read-only into `.ci/platform` and capture its SHA once.
   Both `compatibility.json` and `compatibility-candidate.json` are read from
   that one checkout.
2. Read the consumer's own declared bounds for the sibling packages it installs
   from its `pyproject.toml` at the PR checkout under test.
3. When every supported pin satisfies those bounds, install the supported
   cohort. This is the ordinary case and stays the default.
4. Otherwise, install the whole cohort named by the candidate record at the same
   SHA, provided it is marked `kind: candidate`, names an immutable SHA-40 for
   each needed package and satisfies the bounds. Selection is per cohort, never
   per package, so the installed set is always one recorded combination.
5. When neither record satisfies the bounds, fail before installing anything
   and name the record and bound that disagree. The remedy is to publish a
   candidate record that satisfies the bounds on EPSM `main`, or to keep the
   bound within the supported combination.

No PR label, repository variable or workflow input takes part. The inputs are
the consumer's reviewed `pyproject.toml` and two committed files at one
immutable EPSM SHA, so the same PR revision always selects the same cohort and
the receipt can be reproduced from those identities. The step summary records
the EPSM SHA, the record used, the reason, and each dependency's bound, version
and revision; a later step logs the actual checked-out revisions.

A `ci` pass on the candidate cohort is still a development check of that
package. It does not verify the candidate combination, does not record a
candidate receipt for the consumer's own revision, and does not replace the
explicit `candidate_manifest_revision` release verification described below.
The rule applies to development jobs that install sibling packages from the
manifest, Core and LCA at present; RC and Database development jobs install no
siblings and select revisions only in Release verification. Each consumer's
`docs/ci.md` states which case it is in.

For the rule to take effect during a transition, the candidate record must be
on EPSM `main`, not only on a candidate branch. Publishing it is an EPSM
metadata change that leaves `compatibility.json` and every release tag
untouched. Once the combination is promoted, every bound is satisfied by the
supported manifest and the candidate record is no longer consulted.

## Feature-cohort checks before development merges

The study-platform campaign adds an explicit `candidate_manifest_revision`
manual-workflow input to EPSM, Workflows, Studies and RC. It selects a separate
`compatibility-candidate.json` at one immutable EPSM SHA. Every owner revision is
fixed; EPSM's `self` resolves to that captured manifest checkout. The generator
rejects a different consumer checkout, a moving candidate reference or combining
candidate selection with main-dependency mode. Empty input preserves supported
selection. No consumer stores another scientific pin table or dispatches its
siblings' jobs.

Select a candidate only through the explicit manual input at its recorded
consumer revision. PR labels and repository variables no longer select a cohort
or dispatch checks. Record the candidate receipt beside the PR, resolve actual
merge conflicts, and verify affected integrations at the resulting revision.
Keep failed historical runs visible. A manually dispatched candidate check does
not replace the PR's required development `ci` result.

Finish owner feature commits, capture their candidate record, publish that
record as an EPSM feature commit, then run consumer workflows at the recorded
heads. Required private read-only keys must be configured for each consumer,
including Studies' new installed integration lane. Keep local wheel receipts,
hosted check status and released compatibility distinct. After development
conflicts or merges, check the newly captured actual revisions again. See the
[study campaign](study-platform-readiness.md) for the acceptance and promotion
sequence; this paragraph does not claim that any hosted run has passed.

On 21 October 2026, read-only protection queries for these four private consumer
repositories returned HTTP 403 with GitHub's message that the feature requires
GitHub Pro or a public repository. Enforced protection could not be confirmed;
the required reviews and gates remain a manual release policy. Studies' Actions
secret-name inventory was empty at that review, so its newly added private
integration lane still needed dedicated read-only dependency access. No secret
values or hosting settings were changed during this inspection.

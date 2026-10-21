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
next normal PR, main or manual CI run. There is no cross-repository job dispatch,
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

Keep normal full checks on PRs into `dev`/`main` and pushes to `main`, with
cancellation for superseded PR updates and an appropriate timeout. A feature
push with an open PR should not create a second identical full run. Adopt these
changes in each repository's own review, preserving engine, database, notebook
and installed-wheel gates that determine its advertised behaviour.

The [EPSM compatibility guide](https://github.com/SB-Chalmers/epsm/blob/main/docs/platform-compatibility.md)
owns the implementation details and exact guard commands. Historical receipts
and explicitly retained numerical regression references remain dated evidence;
they do not select the current supported combination.

## Feature-cohort checks before development merges

The study-platform campaign adds an explicit `candidate_manifest_revision`
manual-workflow input to EPSM, Workflows, Studies and RC. It selects a separate
`compatibility-candidate.json` at one immutable EPSM SHA. Every owner revision is
fixed; EPSM's `self` resolves to that captured manifest checkout. The generator
rejects a different consumer checkout, a moving candidate reference or combining
candidate selection with main-dependency mode. Empty input preserves supported
selection. No consumer stores another scientific pin table or dispatches its
siblings' jobs.

For campaign PRs, a maintainer sets repository variable
`EPSM_CANDIDATE_MANIFEST_SHA` and applies the `platform-candidate` label. That
explicit run uses the captured PR head and checks its prospective target merge
for conflicts. Unlabelled PRs retain supported selection, even when old supported
bounds cannot accommodate the new feature. Keep their failed historical runs
visible; the candidate run must pass all agreed checks before development review.
Clear the variable and remove labels after supported release promotion.

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

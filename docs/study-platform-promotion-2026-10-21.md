# Study platform integration and publication, 21 October 2026

Studies can now read its six private dependencies in CI. The user authorized the
explicit access setup in this task. Six dedicated deploy keys were verified as
read-only; matching Studies Actions secrets were uploaded without replacing
existing keys or secrets. Dedicated SSH reads succeeded. All temporary local
private keys and their staging directory were removed. The
[non-secret receipt](study-platform-promotion-2026-10-21.json) records public key
identifiers and verification flags, without private key material.

The previously blocked [Studies feature check](https://github.com/SB-Chalmers/epsm_studies/actions/runs/39592452765)
passed its standalone and installed Python 3.11/3.13 jobs. Each installed suite
passed all 77 tests with zero failures, errors or skips. Downloaded receipts
confirm the exact feature-06 candidate and imports from installed wheels. The
earlier access failure remains in the
[feature verification history](study-platform-feature-verification-2026-10-21.md).

Final review also found one trailing blank line in Workflows' release notes.
Its removal changes no runtime source or package metadata. Feature-07 captures
that committed documentation cleanup and the corresponding EPSM candidate pin;
its exact-source checks passed before the first development merge. Both clean
Python 3.11 and 3.13 cohorts passed all four required scenarios. The final EPSM,
Workflows, RC and Studies hosted feature checks also passed; source and wheel
identities remain in the non-secret receipt.

## Integration sequence

The original task requests development integration followed by release
promotion. Review covers the owner/reuse register, schemas and capability limits,
sampling and physical assignments, retained input/result identities, output
accounting, owner tests and fresh installed examples. The recorded automated
reviews are not presented as an independent GitHub maintainer approval.

Before each promotion, refresh both branch heads, inspect the final diff and
prospective merge tree, and require its agreed checks. Preserve the primary
working directories and all unrelated edits. Merge peer feature PRs into `dev`
first, then capture their actual merge revisions in EPSM's still-open candidate
record. Check that combination before merging EPSM last. Build and verify the
actual complete development cohort before any release PR is merged into `main`.

Release PRs preserve shared history. Tags identify actual `main` commits and
never move. Verify the actual published artifacts before promoting EPSM's
supported manifest. The machine-readable receipt will retain development,
release and artifact identities separately as those actions complete.

## Peer development merges

The reviewed peer changes were merged normally into `dev`, preserving history.
Each complete merged tree matches its tested feature tree; no conflict resolution
or scientific change was needed.

| Owner | Development merge revision |
| --- | --- |
| Core | `6f7282eb4381c2d49717ec9ede92c9eae6b14504` |
| Weather | `a2c91a15e9b8a9a08dfae7a35e24060567347b3b` |
| RC | `3db4ef93e71ea9b14ea65ca0f954a8db6ed2798e` |
| Workflows | `cbb487b316d202fb18c86c95ff2a98056f6511b3` |
| Studies | `2177cdd7452666d612b397025da2f41de9bfa0b5` |

## Complete development verification

EPSM feature PR 31 and all peer feature PRs merged into development normally.
The actual full development cohort passed the installed platform, six-evaluation
study, archetype handoff and workflow handoff on Python 3.11 and 3.13. Release
notes and package descriptions were then finalized through separate development
PRs. Those release-preparation wheels and the actual complete release-ready
development heads passed the same four gates on both Python versions. The
machine-readable receipt retains their separate revisions and wheel hashes.

A stronger archive check created a fresh Python 3.13 environment containing only
Studies and NumPy. It reopened a relocated archive written by Python 3.11,
verified all 297 files, read all six hourly arrays, produced three engine
comparisons and four baseline differences, and exported CSV/JSON. EPSM, Core,
RC, LCA, Workflows, Data, DB and Weather were absent from that environment.

## Owner main promotion

Core PR 60, Weather PR 9, RC PR 71, Workflows PR 15 and Studies PR 15 merged
normally from development into main after the release-ready development gates
passed. Each prospective merge had no conflicts and every actual main tree
exactly matches its checked development tree. Actual revision identities and
preflight trees are retained in the accompanying receipt.

Exact-main wheel and owner checks are running before new release tags are
created. Automatic RC, Workflows and Studies main runs selected the preceding
supported cohort and failed its expected dependency resolution; those failures
remain separate from the explicit candidate checks. EPSM's supported manifest
remains unchanged until actual released peer artifacts pass verification.

Studio remains unchanged. Authentication, projects and UI integration remain a
later application campaign. Publication and released-history synchronization
will be recorded here as they complete; this entry does not claim them yet.

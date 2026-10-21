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
its exact-source checks must pass before the first development merge.

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

At this checkpoint, no campaign development/main merges, tags or releases have
occurred. Studio remains unchanged. Authentication, projects and UI integration
remain a later application campaign.

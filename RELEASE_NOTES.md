# Release 0.5.0 — 15 October 2026

The handbook records the implemented archetype authoring, shared application,
atomic assignment, consumer migration and API cleanup, including the AC01–AC11
acceptance register and migration routes. No new scientific behavior or public
API is introduced by this documentation release.

The coordinated releases are Data 0.6.0, Core 0.4.0, Database 0.3.0 and EPSM 0.3.0.
See the [release record and exact verification](docs/archetype-release-2026-10-15.md)
for released commits, artifact hashes, passing tagged checks and preserved work.
Earlier verification records remain dated and unchanged. Private-repository
protection is unavailable; the record states the intended configuration and the
maintainer's explicit manual merge authorization without claiming independent
GitHub approval.

Handbook CI avoids duplicate branch-push/PR matrices and cancels superseded runs.
History-only release merges reuse verified identical file trees; each release
tag still receives its required checks before GitHub publication.

# Release 0.4.0 — 15 October 2026

Implemented logging API, event registry, migration guidance and coordinated verification evidence.

The package contract specifies that libraries emit through Python's standard logging without configuring output.
Instrumented operations accept optional keyword-only `log_context`; identifiers
stay separate from scientific inputs, saved models and cache keys. INFO shows
major stages; DEBUG adds decisions and timing. Standalone commands support
`--log-level`, including `OFF`, where the package provides a command.

The EPSM application configures the combined stderr and optional DEBUG JSONL
output with `configure_logging`; `enabled=False` disables both destinations.
Existing callers and supported older collaborator signatures remain supported.
No new mandatory dependency is introduced by the logging implementation.

The coordinated release was requested for manual review and local validation
because GitHub refused to start several hosted jobs due to account billing.
Hosted checks that did not run are not counted as passes. See the
[coordinated verification record](https://github.com/SB-Chalmers/epsm_development/blob/main/docs/logging-verification.md)
for exact tested revisions, executed checks and remaining limitations.

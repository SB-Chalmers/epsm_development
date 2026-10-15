# Archetype implementation series

**Status: step 1 prepared for review, 15 October 2026.**
The [authoring contract](archetype-authoring.md) is the implementation direction.
This documentation change does not establish an implemented application API or
package test result. Migration adapters stay until consumers have moved.

## Branch and review discipline

Follow [Branches and releases](branches-and-releases.md). Each row below is a
separate `codex/` branch from that repository's current `origin/dev`, with a PR to
lowercase `dev`. Preserve active checkouts in separate worktrees. Leave Data's
historical uppercase `DEV`, Djamila history and published tags untouched.

Merge one PR at a time after checks and maintainer review. Start dependent
branches only after their predecessors merge. Refresh bases and test the actual
merged dependency revisions before changing consumers. Promotion to `main`,
versions and tags are a separate release process.

## Ordered changes

All steps after the first are pending. Branches below omit the `codex/` prefix.

| Step | Repository | Branch | Change and merge evidence |
| --- | --- | --- | --- |
| 1 | Development | `archetype-contract` | Define ownership, authoring/application behaviour and AC01–AC11; add the attributed class diagram; run handbook checks |
| 2 | Data | `profile-definitions` | Consolidate Sveby, explicit BEN DHW and labelled generic definitions/selectors; test portability, applicability, source identity and independent loading; add an offline example |
| 3 | Core | `profile-consumption` | Consume public Data definitions and convert standard/custom profiles; preserve outputs, totals, explicit calendars and area bases; retain forwarding loaders temporarily |
| 4 | Data | `composed-archetype` | Extend the existing model with optional profiles, templates, envelope assumptions and sources; support incomplete authoring and version-4 exchange with old readers; test isolation and add an authoring notebook |
| 5 | Data | `catalogue-authoring-pilot` | Resolve MF SE.02 through shared authoring independently of calibration success; compare unchanged physical values and retain target evidence |
| 6 | Core | `atomic-building-assignment` | Commit validated assignments atomically; test role-aware replace/fill, rollback, quantities, geometry/openings, snapshots and renovation lineage |
| 7 | EPSM | `apply-archetype` | Apply catalogue/custom archetypes through one operation; retain reports; demonstrate geometry → archetype → inspection |
| 8 | Data | `catalogue-all-types` | Extend to every shipped category/configuration, source variant and SE.07; attach supported profiles and expose system choices without inventing installed HVAC |
| 9 | EPSM | `archetype-consumer-migration` | Migrate record assembly, component-state selection and handovers; preserve evidence and reference-area conversions; update notebooks and renovation examples |
| 10 | DB | `catalogue-consumer-migration` | Migrate stock/exploration inspection to public Catalogue APIs; preserve classifications with offline synthetic tests; keep assembly in EPSM |
| 11 | EPSM | `archetype-installed-checks` | Require clean-wheel authoring/application/exchange and actual RC/EnergyPlus handoffs; record exact revisions and prerequisite failures before cleanup |
| 12 | Data | `archetype-api-cleanup` | Remove migrated duplicate public loaders, summary-only exchange and Data-to-EPSM forwarders; retain saved-format readers and distinct inspection; update explorer and migration guide |
| 13 | Core | `profile-api-cleanup` | Remove migrated redundant selectors; retain physical converters, schedule/calendar builders and distinct calculations; run installed regressions |
| 14 | Development | `archetype-acceptance` | Update current terminology, use cases, diagram and verification; link merged PRs and tested combinations without rewriting historical reviews |

## Checks in every change

For code changes, demonstrate a failing test of observable behaviour, then make
the smallest complete implementation. Tests must not reproduce the implementation
as their expected answer. Add public docstrings, working examples and migration
notes in the same PR.

Preserve starting material properties, thicknesses, fractions, order, U-values,
resolved schedules and source records. Compare physical meaning, ignoring
incidental representation changes. Scientific corrections need separate PRs and
independent validation.

Run package tests and existing lint/format checks appropriate to touched modules.
Verify bounded, no-I/O representations and ordinary module logging for new public
objects. Imports must not load catalogues, access networks or configure logging.
Follow [licensing and attribution](licensing.md) for retained source material.

The handbook requires:

```sh
python3 scripts/check_docs.py
python3 -m unittest discover -s tests -v
python3 scripts/run_examples.py
```

When current runnable platform snippets change, also run
`scripts/check_platform_examples.py` with supported packages installed. New API
sketches remain illustrative until their implementation and installed checks pass.

## Cleanup and completion gates

Before step 12, search maintained source, tests, examples, documentation and
explorer callers across packages for removed APIs. Migrate all active consumers
and rerun installed wheels. Do not retain aliases to hide missed consumers. Old
saved-format readers remain supported.

Run examples in fresh kernels using installed wheels without sibling-source
imports. Test Data independently of Core/EPSM. Required handoffs use real engines;
missing dependencies or binaries fail the dedicated gate, and skipped checks do
not establish interoperability.

Record commands, revisions, Python/engine versions, pass/fail/skip counts and
scope in the owning PR, linked from the final handbook update. Documentation
checks establish documentation correctness, not scientific validity or package
interoperability.

Completion requires AC01–AC11, maintained consumer migration, installed handoffs
and the final handbook update. Merging the contract alone does not complete the
series.

# Logging across packages

This change is being implemented on coordinated `codex/uniform-logging`
branches, with review into `dev`. It is not a released package promise.

## Choose output once

The EPSM application owns the combined console and JSONL destinations:

```python
from epsm import configure_logging, reset_logging

configure_logging(directory="outputs/example")
# INFO goes to stderr. DEBUG is retained in outputs/example/logs/study.jsonl.
configure_logging(console_level="WARNING", package_levels={"epsm_core": "DEBUG"})
configure_logging(enabled=False)  # Stop console and file output.
reset_logging()  # Restore the host application's previous logging settings.
```

No directory means no log file. Console `OFF` can retain a requested DEBUG
file. Repeated setup updates only owned handlers; it does not duplicate output.
Existing foreign handlers within managed namespaces cause a clear conflict.
Unrelated application handlers remain unchanged.

Libraries use ordinary Python logging without requiring EPSM. Imports install
no terminal or file output. Standalone commands offer `--log-level`, including
`OFF`, and retain their command results on stdout.

## Follow the work

Instrumented entrypoints accept optional keyword-only `log_context`. Pass small
identifier mappings, for example `{"study_id": "example"}`. Each operation
creates an `operation_id`; nested operations include `parent_operation_id`.
Threads receive copied context explicitly. Context is not a scientific input,
saved model field or cache-key component.

INFO describes major stages, handoffs and durable artifacts. DEBUG explains
individual choices, conversions, caches and bulk per-building detail. Existing
diagnostics and saved results remain the source of truth. One reporting layer
owns each failure traceback; inner operations emit codes and raise the error.

The [operation event registry](logging-events.json) lists the exact event names and owning entrypoints.

## Event families

Each family uses `.started`, `.completed`, `.failed` and `.cancelled` for
operation lifecycle events. Existing more specific events remain available.

| Owner | Event families |
| --- | --- |
| EPSM | `evaluation`, `building.assemble`, `catalogue.resolve` |
| Data | `catalogue.load`, `catalogue.parametric.load`, `catalogue.detailed.load`, `catalogue.select`, `catalogue.construction.resolve`, `catalogue.renovation.load`, `catalogue.export` |
| Core | `geometry.prepare`, `model.convert`, `model.compile`, `model.write`, `simulation`, `simulation.building`, `simulation.district`, `simulation.results.read`, `simulation.preflight` |
| RC | `energy.rc`, `geometry.gis.*.load` |
| LCA | `lca.assessment`, `lca.renovation`, `lca.report.save`, `lca.report.load` |
| Database | `database.query`, `database.stock.read`, `database.source.ingest`, `database.dataset.process`, `database.dataset.validate`, `database.export` |
| Weather | `weather.compile`, `weather.ingest`, `weather.station.select`, `weather.provider.fetch`, `weather.recover`, `weather.export`, `weather.inspect` |
| Studies | `study.protocol.save` |

Events use the version-1 JSONL format in [Uniform logging](engineering-style.md#uniform-logging).
Timestamps use UTC, durations use a monotonic clock, and JSON rejects nonfinite
numbers or arbitrary object serialization. Credentials, source records and
large arrays do not belong in logs. Exception output is sanitized before emission.

Raw engine output stays separate. Core retains its existing `process.log`,
`eplusout.err` and `diagnostics.json`; structured events identify their paths.
Reconfiguration and resumed work append rather than truncate retained logs.

## Compatibility and checks

The umbrella passes context only when a collaborator's public signature
explicitly supports it, preserving older supported versions. No lower-level
package imports EPSM to log. Workflows, Studio and archived implementations are
outside this rollout; Slurm adoption remains separate.

Tests cover output controls, JSONL, context relationships and thread isolation,
single traceback reporting, normal host logging and installed-package handoffs.
Package tests and physical-result comparisons remain separate from log checks.
See the [verification record](logging-verification.md) for exact revisions, executed
examples and external integrations that could not be checked.

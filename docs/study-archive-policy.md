# Study archive decision

**Decision date: 14 October 2026.** Archive outdated, named studies and their
study-specific workflows. Keep reusable study setup, execution, parametric
designs, global sensitivity analysis and renovation search active. Archived
studies have no reproduction, repair or porting obligation.

## Active tools and archived research

| Keep active | Archive |
| --- | --- |
| `epsm_studies.PaperStudy` and its generic protocol persistence | Historical research protocols and implementations tied to a particular investigation |
| Workflows prepared cases, local execution and Vera transport | Old fixed campaigns, their launcher scripts and study-specific configuration |
| Parametric designs and global sensitivity analysis | Multifamily exploration, basement/weather sensitivity and other named experiments |
| Renovation search and generic evaluation support | Legacy calibration, cohort transfer, archetype diagnosis and their study-specific helpers |
| Small teaching examples of the maintained public APIs | Scripts, tests, fixtures, reports and instructions that exist to run an archived study |

A file belongs in the archive when it implements a particular research question,
fixed selection, calibration protocol or obsolete campaign. A generic lesson may
use an illustrative name or a small Building; that alone does not make it an
archived study. Supported physical calculations, catalogue definitions, source
evidence and independent weather tools remain with their current owners.

## Locations and preservation

Retired Workflows and Studies files move under `archive/2026-10-14/` in their
owning repository, retaining relative paths and source attribution. In Studies this includes the former
`src/epsm_studies/legacy_workflows/` tree. Workflows' forwarding modules and old
study scripts are archived with their supporting files. Data's cohort-study
compatibility forwarder is archived under Data's `docs/archive/2026-10-14/`.

The earlier Studies preservation snapshot at `archive/workflows_2026_10_14/` and
Data transfer at `imports/epsm_data_harmonisation/` remain unchanged. Their
`ARCHIVE.json` and `TRANSFER.json` records are evidence of the original transfers.
Keep these source records even when archived scripts contain paths that no longer
resolve. Archive inventories record the new moves separately.

Archived code is outside supported imports, package entry points and active test
collection. Its instructions describe the historical environment; they are not a
current installation or compatibility promise. Preserve archived source and
results for inspection. Do not repair old source discovery, resource lookup or
imports merely to make a past study runnable. A later research decision can
choose whether any archived work should be reconsidered.

## Current review consequences

The historical campaign CLI's source-root lookup and cohort-transfer references
to removed Data evidence paths are findings about archived implementations.
They do not block the maintained platform, and repairing or reproducing those
studies is outside current work.

The prepared-study runtime finding was addressed during release preparation:
workers now verify observed package and handler identities and the selected
built-in EPSM engine before execution and resume. Each attempt retains its
runtime hash. Custom handlers must declare the identity of any external engine
they use. The earlier offline checkpoint counts predate this fix.

The [harmonisation guide](harmonisation.md), [file map](harmonisation-file-map.md),
[use cases](../use_cases/README.md) and [review register](harmonisation-review.md)
apply this scope. Earlier verification counts and transfer checks remain dated
historical evidence; they do not promise continued execution of archived studies.

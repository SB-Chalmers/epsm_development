# Studio readiness release preparation — 20 October 2026

**Status: IN PROGRESS.** This is the Handbook **0.5.1 candidate** record. It is
not a declaration that the complete platform release is finished. The owner
releases and final EPSM 0.3.1 combination have passed their required checks and
been tagged. Consumer adoption and the handbook release remain pending. The
[15 October release record](archetype-release-2026-10-15.md) remains the dated
evidence for the preceding coordinated release.

## Current ownership

Core owns the physical Building, geometry, validation and neutral `epsm.scene/1`
polygon data. Viewer owns browser rendering, selection, camera/display controls
and optional Python display helpers. All web adapters, authenticated sessions,
forms, project settings and user-requested jobs belong to Studio. Libraries expose
ready-to-consume public operations rather than Studio-specific HTTP layers.

EPSM owns the supported platform manifest and the installed checks connecting
scientific packages. Each package keeps its version, dependency bounds and tests.
The handbook owns these shared instructions and records the exact evidence when
available. See [platform compatibility](platform-compatibility.md) and
[plots and previews](plotting-and-previews.md).

The legacy production Studio application has not been changed by this
preparation. The replacement Studio remains a plan and a minimal frontend
scaffold; SAML integration, project/study APIs, execution and caching are future
implementation gates. Nothing here establishes a replacement deployment.

## Release state

| Component | Prepared scope | Evidence and remaining gate |
| --- | --- | --- |
| Handbook 0.5.1 | Current ownership, private Viewer delivery and central compatibility guidance | Local documentation checks recorded below; final main commit, hosted checks and tag pending |
| Core 0.8.0 | Scene-data boundary and removal of embedded display routes | Published owner source and checks, including the final updated platform cohort, are recorded below |
| Viewer 0.1.0 | Standalone TypeScript renderer, optional Python helpers and self-contained artifacts | Tagged source, all three owner CI jobs and authenticated private release-artifact checks passed |
| EPSM 0.3.1 | Central supported manifest, metadata audit and consumer matrix interface | Published main/tag, checked distributions and durable receipts; scientific, display and metadata checks passed |
| Consumer repositories | Read the central manifest on their next normal CI run | Each repository's reviewed adoption and its own checks remain distinct evidence |
| Database environment | Portable evidence through the owning Database API | The identity and readiness of a proposed “GIS Lake” environment are **unconfirmed** |

## Owner releases

These source tags have been promoted by the release coordinator. The linked
checks identify the reviewed owner runs; the separate final EPSM evidence appears
below. The EPSM foundation at
`9f82d5b94d768e9cf38f03bf8623d69e402b636a` established the manifest interface but
is not the final 0.3.1 release.
The earlier metadata-guard foundation
`b91d3567e3f88b5da97e0597e4a3751419c9ce70` is an ancestor of the final EPSM
release, rather than an outstanding independent feature branch.

| Repository | Published version | Released main commit | Owner checks |
| --- | --- | --- | --- |
| Core | [0.8.0](https://github.com/SB-Chalmers/epsm_core/releases/tag/v0.8.0) | `b197e092eb0423de5a9547873a0f596493ab7536` | [Core checks](https://github.com/SB-Chalmers/epsm_core/actions/runs/39424191033) |
| RC | [0.8.2](https://github.com/SB-Chalmers/epsm_rc/releases/tag/v0.8.2) | `6464f7d832d5ff3093fa754c0dc4d0d2930450dc` | [RC checks](https://github.com/SB-Chalmers/epsm_rc/actions/runs/39423285081) |
| Workflows | [0.3.1](https://github.com/SB-Chalmers/epsm_workflows/releases/tag/v0.3.1) | `c558edfeee9a8bf93aabe07ef3834e99aab20cce` | [Workflows license-patch checks](https://github.com/SB-Chalmers/epsm_workflows/actions/runs/39429171696) |
| Studies | [0.3.0](https://github.com/SB-Chalmers/epsm_studies/releases/tag/v0.3.0) | `16ed6bd0bd63cee588f6e7ad951d71f8f9543ecb` | [Studies checks](https://github.com/SB-Chalmers/epsm_studies/actions/runs/39423762626) |
| Viewer | [0.1.0](https://github.com/SB-Chalmers/epsm_viewer/releases/tag/v0.1.0) | `f2c847b9cd44280b7cf21803acfefa6e49e78b1b` | [Build and installed-wheel checks](https://github.com/SB-Chalmers/epsm_viewer/actions/runs/39425944812) |
| EPSM | [0.3.1](https://github.com/SB-Chalmers/epsm/releases/tag/v0.3.1) | `58327ba60f379a51129bc5cd743f1f7c74e38723` | [Scientific/display checks](https://github.com/SB-Chalmers/epsm/actions/runs/39429999507), [metadata](https://github.com/SB-Chalmers/epsm/actions/runs/39429999530) |

Core's two platform lanes each reported 1,079 passed and eight explicitly optional
skips; those skips are not counted as passing integrations. RC's platform lanes
each reported 583 passed without skips. Workflows 0.3.1 passed all 70 owner tests
on Python 3.11 and 3.13. Studies' two Python lanes passed. Viewer passed its build
job and both installed-wheel lanes. The
[owner publication receipts](studio-readiness-owner-releases-2026-10-20.json)
retain distribution hashes and verified GitHub asset digests. Their release
manifests distinguish local artifact builds from CI verification.
Across these six private GitHub releases, all 27 uploaded asset digests were
verified. Those assets remain separate from source checkouts and from any public
package registry publication.

Archive inspection found that Workflows' first 0.3.0 source tag had no root
license or distribution license metadata. It was left unchanged. The separate
0.3.1 patch includes MIT notices in both distributions and uses the existing
EPSM Development contributors holder notice. Its runtime source is byte-identical
to 0.3.0 apart from the authoritative package version. Public signatures,
scientific behaviour and prepared schema 3 are unchanged. The first complete
EPSM candidate check with Workflows 0.3.0
[passed](https://github.com/SB-Chalmers/epsm/actions/runs/39427470932), alongside its
[metadata check](https://github.com/SB-Chalmers/epsm/actions/runs/39427470984), but
remains historical pre-patch evidence. It is not the final proof for the licensed
0.3.1 combination.

## Final EPSM combination checks

EPSM 0.3.1 is tagged at
[`58327ba60f379a51129bc5cd743f1f7c74e38723`](https://github.com/SB-Chalmers/epsm/tree/v0.3.1).
The [final scientific and display run](https://github.com/SB-Chalmers/epsm/actions/runs/39429999507)
and [metadata guard](https://github.com/SB-Chalmers/epsm/actions/runs/39429999530)
passed. The [compact evidence summary](studio-readiness-platform-evidence-2026-10-20.json)
retains actual versions, revisions, wheel hashes, engine identities and receipt
hashes. It records the licensed Workflows 0.3.1 combination; the earlier green
0.3.0 candidate remains historical evidence above.

Python 3.11.17 and 3.13.16 each passed 246 platform tests without skips. Each lane
also ran five EPSM and six LCA notebooks from fresh kernels. The metadata guard
passed 83 pure tests. Installed handoffs used the actual EnergyPlus 24.2.0
executable and RC, with catalogue and authored archetypes, portable synthetic
records and retained renovation assessments. They did not use a live database
service or establish national data coverage.

For each engine, a two-row grid and six-row paired Jansen design completed with
explicit settings, frozen inputs and retained results. Controlled failure/retry
checks kept the failed attempt; the paired plan had seven attempts and six design
rows. Resume added no attempts, and the baseline remained unchanged. These small
fixtures verify execution, preservation and recovery. They do not validate
sensitivity-index accuracy; the receipt explicitly records
`sensitivity_accuracy_validated: false`.

A separate Python 3.13 display job used installed Core 0.8.0 and Viewer 0.1.0.
The public Core scene passed Python Viewer's public `write_scene` and JavaScript
Viewer's public `prepareScene`: 12 source objects produced 24 drawing triangles
with identities, metadata and input data retained. The scene contract was
`epsm.scene/1`, metres and Z up. Scientific workers did not install Viewer or Node.

The run's feature head was `f86fa11367dfde230aa1ef555a86fa20309befda`.
Its actual tested GitHub PR merge checkout was
`c99b83e330ddea2038d866ea09bf0d89a2ef890e`, which the receipts retain. That checkout
and the final released main share tree
`fedd99461702d9a8d8b88121a6a2475cb9ac94e2`; release promotion preserved the tested
contents rather than relabelling the earlier receipt SHA. Consumer adoption
checks are still running and remain a separate gate.

The [private EPSM release](https://github.com/SB-Chalmers/epsm/releases/tag/v0.3.1)
contains its wheel, source archive, manifest, checksum file and a durable
`release-evidence.zip`. All five asset digests were verified. The evidence archive
retains both compact scientific receipts, display and metadata evidence, and the
source-promotion identities. The distributions were built from a clean immutable
tag checkout and their runtime modules were checked against that released source.

A subsequent authenticated download matched the published wheel's manifest hash
and installed into the isolated cohort environment. Dependency consistency and a
public EPSM Building scene smoke check passed: six objects used `epsm.scene/1`,
with no Viewer or widget modules loaded. This download check is distinct from
the broader installed-package CI evidence above.

## Verified private Viewer delivery

Viewer's private GitHub release contains the npm tarball, Python wheel, source
archive and `SHA256SUMS` from its green CI artifacts. The npm package has
`private: true`; no public npm or PyPI publication was performed. Authenticate an
account that can read the repository, then download the actual release assets:

```sh
gh release download v0.1.0 --repo SB-Chalmers/epsm_viewer \
  --pattern 'epsm_viewer-0.1.0*' --pattern SHA256SUMS --dir viewer-artifacts
```

The [download verification receipt](viewer-release-download-proof-2026-10-20.json)
records release ID `418402614`, all four asset IDs, exact hashes, runtime versions
and isolated install paths. All three distribution files matched `SHA256SUMS`;
all four downloads also matched GitHub's asset digest and size. The tag API
resolved to the released main commit above.

The downloaded wheel installed into a fresh Python 3.11.13 environment with Core
absent. Resources, MIT notices, dependency consistency and fresh-kernel notebook
display passed. Actual JupyterLab 4.6.4 rendering under Chromium 143.0.7499.4
verified WebGL, selection metadata and canvas disposal after `widget.close()`,
with zero page errors or external network requests. The temporary server and
kernel were shut down. A fresh Node 22.23.3 consumer installed the published npm
archive and used its public root and geometry exports. Rebuilding the downloaded
source archive with Node unavailable produced identical wheel member bytes.

## Consumer adoption and active guidance

Consumer adoption reads the released EPSM manifest on the next normal owner CI
run. The consumer itself remains the reviewed checkout; its collaborators use
the captured manifest's exact revisions. The final adoption record must identify
that captured manifest SHA, the checked owner head and resulting main commit.
Runtime release tags remain immutable when later CI or documentation changes
reach main.

The owner follow-ups correct active installation and display guidance without
changing scientific code. Data points its archetype migration guide at the
central version record. Database examples use Core scene data and the separate
Viewer, retaining existing geometry provenance when appending assumptions. RC
installation instructions use the central supported combination. Core and EPSM
guidance names the extracted display operations rather than removed Core display
methods. Each follow-up needs its normal owner checks; an earlier owner run is
not relabelled as checking a later edit.

These reviews and checks are still in progress at this candidate checkpoint.
Their final identities and the subsequent metadata audit are required before the
handbook's release review.

## Energy and database limits

The common purchased-energy boundary covers **space heating and ventilation fan
electricity**. Thermal heating demand remains separate from purchased carrier
energy. DHW, cooling and plug loads are not silently included in that boundary;
an assessment asking for whole-building energy remains incomplete until its
requested coverage is supported. Core owns delivery accounting and engine
capability checks; Studio must present the selected engine's limits before
submission. These software checks do not establish empirical building prediction
accuracy.

“GIS Lake” is not a verified database target or release identity. Confirm its
owning service, versioned evidence API, read-only access and actual integration
checks before describing it as supported. The Studio plan selects portable
processed records with already-computed heights. It does not authorize height
reconstruction, DTCC ingestion, direct IDF authoring or database migration.

## Checks completed locally

The first handbook increment preserves the earlier three Viewer-boundary edits
as commit `d99b315`. On that commit, the required checks passed: 31 Markdown files,
220 local links, 15 Python syntax examples, 35 template doctest examples, all 11
handbook unit tests and both learning notebooks. These are handbook checks, not
engine or database integration evidence. The final 0.5.1 candidate must be checked
again after this record is complete.

The earlier 0.5.1 documentation candidate also passed
`python3 scripts/check_docs.py` (33 Markdown files, 229 local links, 15 Python
syntax examples and 35 template doctest examples), all 11 tests from
`python3 -m unittest discover -s tests -v`, and both learning notebooks from
`python3 scripts/run_examples.py`. API-documentation templates and their renderer
were not changed. Final hosted release checks are still pending.

The Viewer preparation was checked locally with Node 22.23.3: 11 Node geometry
and version tests and six actual Chromium/WebGL tests passed. Its installed wheel
passed 32 tests each under Python 3.11.13 and 3.13.5 with notebook dependencies
present, and both environments passed dependency consistency. An independent npm
consumer installed the tarball successfully. Inspection verified version metadata,
public entrypoints, resources and licenses in the npm tarball, wheel and source
archive. A clean source-archive rebuild with Node unavailable produced identical
wheel member bytes. These earlier candidate results remain separate from the
subsequent hosted and published-artifact checks above.

The final Viewer fixture and schema were captured through an installed Core
0.8.0 wheel from the exact released main commit. The
[tagged provenance record](https://github.com/SB-Chalmers/epsm_viewer/blob/v0.1.0/tests/fixtures/core-scene.provenance.json)
retains its public operations, synthetic geometry assumptions, Core wheel hash
and scene/schema hashes. The final fixture passed schema validation, all 11 Node
checks and all six actual browser checks before the owner CI run.

## Remaining release gates

1. Complete the six consumer adoption reviews and checks. Record their actual
   tested manifest SHA and resulting main commits. No earlier passing run is
   relabelled as checking that adoption.
2. Run the final handbook checks and normal release review, then tag and publish
   its checked source in coordination. The final handbook identity belongs to its
   release tag and publication receipt. Only completed gates replace the current
   **IN PROGRESS** status.

## Handbook publication evidence

The eventual [Handbook 0.5.1 release assets](https://github.com/SB-Chalmers/epsm_development/releases/tag/v0.5.1)
will retain the released tag/main commit and tree, actual tested checkout and
hosted handbook run, final platform metadata reports, consumer identities and
remote source audit references. Its source archive and evidence archive will have
checksums. Publication remains pending until the gates above pass.

The publication receipt records identities learned after this source was checked.
It verifies the source and evidence assets without attempting to hash itself.
Recording that receipt as a release asset avoids another source edit solely to
refer to the source's own future tag or CI run. Identical-tree release promotion
must be verified explicitly, and a failed, skipped or absent required check does
not count as passing evidence.

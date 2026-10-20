# Studio readiness release preparation — 20 October 2026

**Status: IN PROGRESS.** This is the Handbook **0.5.1 candidate** record. It is
not a declaration that the complete platform release is finished. The owner
releases below have been tagged; the final EPSM 0.3.1 cohort, consumer adoption
checks and handbook release still need their evidence. The
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
| Core 0.8.0 | Scene-data boundary and removal of embedded display routes | Tagged source and owner checks recorded below; full updated platform cohort remains separate |
| Viewer 0.1.0 | Standalone TypeScript renderer, optional Python helpers and self-contained artifacts | Tagged source, all three owner CI jobs and authenticated private release-artifact checks passed |
| EPSM 0.3.1 candidate | Central supported manifest, metadata audit and consumer matrix interface | Final reviewed pins, complete installed scientific/display checks and release identity pending |
| Consumer repositories | Read the central manifest on their next normal CI run | Each repository's reviewed adoption and its own checks remain distinct evidence |
| Database environment | Portable evidence through the owning Database API | The identity and readiness of a proposed “GIS Lake” environment are **unconfirmed** |

## Owner releases and private Viewer delivery

These source tags have been promoted by the release coordinator. The linked
checks identify the reviewed owner runs; they do not claim that the new complete
EPSM combination has passed. The EPSM foundation at
`9f82d5b94d768e9cf38f03bf8623d69e402b636a` established the manifest interface but
is not the final 0.3.1 release.

| Repository | Published version | Released main commit | Owner checks |
| --- | --- | --- | --- |
| Core | [0.8.0](https://github.com/SB-Chalmers/epsm_core/releases/tag/v0.8.0) | `b197e092eb0423de5a9547873a0f596493ab7536` | [Core checks](https://github.com/SB-Chalmers/epsm_core/actions/runs/39424191033) |
| RC | [0.8.2](https://github.com/SB-Chalmers/epsm_rc/releases/tag/v0.8.2) | `6464f7d832d5ff3093fa754c0dc4d0d2930450dc` | [RC checks](https://github.com/SB-Chalmers/epsm_rc/actions/runs/39423285081) |
| Workflows | [0.3.1](https://github.com/SB-Chalmers/epsm_workflows/releases/tag/v0.3.1) | `c558edfeee9a8bf93aabe07ef3834e99aab20cce` | [Workflows license-patch checks](https://github.com/SB-Chalmers/epsm_workflows/actions/runs/39429171696) |
| Studies | [0.3.0](https://github.com/SB-Chalmers/epsm_studies/releases/tag/v0.3.0) | `16ed6bd0bd63cee588f6e7ad951d71f8f9543ecb` | [Studies checks](https://github.com/SB-Chalmers/epsm_studies/actions/runs/39423762626) |
| Viewer | [0.1.0](https://github.com/SB-Chalmers/epsm_viewer/releases/tag/v0.1.0) | `f2c847b9cd44280b7cf21803acfefa6e49e78b1b` | [Build and installed-wheel checks](https://github.com/SB-Chalmers/epsm_viewer/actions/runs/39425944812) |

Core's two platform lanes each reported 1,079 passed and eight explicitly optional
skips; those skips are not counted as passing integrations. RC's platform lanes
each reported 583 passed without skips. Workflows 0.3.1 passed all 70 owner tests
on Python 3.11 and 3.13. Studies' two Python lanes passed. Viewer passed its build
job and both installed-wheel lanes. The
[owner publication receipts](studio-readiness-owner-releases-2026-10-20.json)
retain distribution hashes and verified GitHub asset digests. Their release
manifests distinguish local artifact builds from CI verification.

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

The current 0.5.1 documentation candidate also passed
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

## Complete this record before promotion

1. Add final source revisions, declared versions, hosted check URLs and artifact
   identities for each changed package. Record failures, skips and missing
   prerequisites explicitly; do not count a canceled run as passing.
2. Run the complete installed EPSM combination once with required real engine,
   database and notebook prerequisites. Preserve each scientific owner's gates.
   Record the separate Core-to-Viewer display handoff at the final supported pins.
3. Promote remaining reviewed changes through `dev` and normal release merges into `main`,
   then tag and publish checked artifacts in coordination. Consumers adopt the
   resulting manifest on their next normal CI run; no cross-repository fan-out is
   needed.
4. Rerun the handbook checks, record its final main SHA and hosted results, and
   only then replace **IN PROGRESS** with the actual completed release state.

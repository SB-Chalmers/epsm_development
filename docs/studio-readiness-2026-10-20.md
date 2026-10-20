# Studio readiness release preparation — 20 October 2026

**Status: IN PROGRESS.** This is the Handbook **0.5.1 candidate** record. It is
not a declaration that all packages have been merged, tagged or published. Final
release commits, hosted checks and artifact identities remain to be supplied by
the release coordinator. The
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
| Core 0.8 | Scene-data boundary and removal of embedded display routes | Final release SHA and required package evidence pending from release coordinator |
| Viewer 0.1.0 | Standalone TypeScript renderer, optional Python helpers and self-contained artifacts | Local candidate checks below; final Core fixture provenance, remote CI, main SHA and publication pending |
| EPSM platform | Central supported manifest, metadata audit and consumer matrix interface | Final reviewed pins, complete installed scientific checks and release identity pending |
| Consumer repositories | Read the central manifest on their next normal CI run | Each repository's reviewed adoption and its own checks remain distinct evidence |
| Database environment | Portable evidence through the owning Database API | The identity and readiness of a proposed “GIS Lake” environment are **unconfirmed** |

The private [Viewer repository](https://github.com/SB-Chalmers/epsm_viewer) exists.
Its preparation commits are `486b396` and `f87d499`, after the extraction baseline
`adf0252`. These are candidate identities, not released main SHAs. The npm package
has `private: true`; there is no public npm or PyPI publication in this preparation.
Viewer's `docs/release.md` records authenticated GitHub workflow-artifact download
and a future release-asset recipe. CI artifacts expire after 14 days; durable
release assets require an actual checked release.

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
wheel member bytes. These results precede the final Core fixture update and do
not replace hosted checks on the final release commit.

## Complete this record before promotion

1. Add final source revisions, declared versions, hosted check URLs and artifact
   identities for each changed package. Record failures, skips and missing
   prerequisites explicitly; do not count a canceled run as passing.
2. Replace the earlier Viewer fixture candidate provenance with the final Core
   scene/schema SHA and rerun the relevant display checks.
3. Run the complete installed EPSM combination once with required real engine,
   database and notebook prerequisites. Preserve each scientific owner's gates.
4. Promote reviewed changes through `dev` and normal release merges into `main`,
   then tag and publish checked artifacts in coordination. Consumers adopt the
   resulting manifest on their next normal CI run; no cross-repository fan-out is
   needed.
5. Rerun the handbook checks, record its final main SHA and hosted results, and
   only then replace **IN PROGRESS** with the actual completed release state.

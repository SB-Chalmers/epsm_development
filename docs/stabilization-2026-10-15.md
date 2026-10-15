# EPSM stabilization, 15 October 2026

The current software combination is Core/RC 0.3.0, EPSM/Database 0.2.0, LCA
0.2.0, Data 0.4.0, Studies 0.1.0 and smhi2epw 1.1.1. The
[EPSM compatibility manifest](https://github.com/SB-Chalmers/epsm/blob/dev/compatibility.json)
is the executable source-pin record. Each hosted platform run also uploads its
actual source revisions and installed versions. Workflows and Studio are outside
this stabilization.

## Focused changes

| Finding | Change and review |
| --- | --- |
| Handbook examples implied ready Buildings | [Development 13](https://github.com/SB-Chalmers/epsm_development/pull/13) selects illustrative presets and explicit RC policies and adds optional installed-package example checks. Empty drafts remain valid, inspectable objects. |
| RC migration descriptions conflicted | [RC 30](https://github.com/SB-Chalmers/epsm_rc/pull/30) reconciles height provenance, installation and recovery/weather guidance without changing the solver. |
| Shared environment metadata could be stale | [EPSM 6](https://github.com/SB-Chalmers/epsm/pull/6) compares installed metadata with checkout versions and requires public capabilities. Verification is read-only and permits feature branches. |
| Source summaries lost portable evidence | [EPSM 7](https://github.com/SB-Chalmers/epsm/pull/7) retains the complete credential-free record envelope through copying, renovation and saved Buildings/evaluations. Old summary-only files remain readable. |
| Stock conversion returned a legacy model | [Database 5](https://github.com/SB-Chalmers/epsm_db/pull/5) delegates to canonical physical conversion, preserves incomplete drafts and every attempted-record receipt, and provides `to_epsm_legacy` migration. |
| Delivery corrections lacked complete regression evidence | [Database 4](https://github.com/SB-Chalmers/epsm_db/pull/4) reviews the preserved local edits and checks nested roots, unsafe/missing roots, counts, checksums and repeated delivery. The deployed kit relationship is recorded without restarting services. |
| CI used obsolete combinations | [EPSM 8](https://github.com/SB-Chalmers/epsm/pull/8), the
[final manifest and examples](https://github.com/SB-Chalmers/epsm/pull/10), and linked package CI changes test installed wheels with pinned and supported `dev` dependencies on Python 3.11/3.13. Required imports fail explicitly. |
| Installed DB operations depended on a checkout | [Database 7](https://github.com/SB-Chalmers/epsm_db/pull/7) packages owned SQL/inventory files; [Database 8](https://github.com/SB-Chalmers/epsm_db/pull/8) preserves source identity after relocation. SQL and schema version are unchanged. |
| LCA's annual example omitted RC settings | [LCA 7](https://github.com/SB-Chalmers/epsm_lca/pull/7) declares reduction policies and updates integration requirements. All seven public notebooks run with the current combination. |
| Versions and status were ambiguous | [Core 22](https://github.com/SB-Chalmers/epsm_core/pull/22), [RC 32](https://github.com/SB-Chalmers/epsm_rc/pull/32), [EPSM 9](https://github.com/SB-Chalmers/epsm/pull/9) and [Database 9](https://github.com/SB-Chalmers/epsm_db/pull/9) prepare coordinated metadata. [LCA 8](https://github.com/SB-Chalmers/epsm_lca/pull/8) and this handbook separate current verification from historical checkpoints. |

Conversion performs no simulation or weather acquisition. Cell archetype
assignments remain assumptions; construction and system selections stay explicit.
Certificate and subject scope, raw observations, dates, geometry and quality
findings remain in the portable source evidence rather than being treated as
validated physical inputs.

## Verification evidence

The [local wheel evidence](stabilization-evidence-2026-10-15.json) records exact
source commits for the candidate versions, isolated installation, test/example
counts and the three annual RC states in the synthetic stock handoff. Its energy
values belong to that fixture, which differs from the LCA notebook comparison.
The 14 local Database skips and 34 deselections are reported separately from
[required hosted PostGIS checks](https://github.com/SB-Chalmers/epsm_db/pull/9).
Optional third-party integrations and live source assets are not implied to pass.

The required platform route checks record and stock conversion, annual RC,
renovation LCA, saved/reloaded Buildings and evaluations, and public notebooks.
Use a hosted run's conclusion together with its revision receipt when citing a
particular combination. Version numbers alone do not identify tested source.
Release promotion requires the complete final combination to pass on `dev`;
release PRs use normal merge commits, and released history is synchronized back
to `dev`. Existing tags and unpublished work are preserved.

## Remaining work and scientific limits

National ingestion, dataset acceptance and publication are separate stages.
Delivery checks establish archive handling, not completed ingestion, accepted
record quality or a published national dataset. This release performs no national
pipeline restart or live database migration. Package-index publication is outside
the implementation scope.

Provider weather acquisition and live deployment checks need their own evidence.
RC approximations and LCA module boundaries still apply; assumed climate and
removal factors remain assumptions. Neither successful engine execution nor
agreement between engines establishes accuracy against measured buildings.

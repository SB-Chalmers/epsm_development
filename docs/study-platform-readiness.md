# Reusable study platform readiness

**Status: implementation in progress, 21 October 2026.** This campaign prepares
the scientific libraries for Studio. It does not change Studio or establish a
deployed application. The acceptance scenarios below define the required
behaviour; only linked execution receipts establish which checks have passed.

## Ownership and the first complete route

Workflows owns study authoring, deterministic designs, fixed execution plans,
attempts, collection and durable result files. Studies owns the named research
record and a convenient result collection referring to those retained files.
This gives a study its outcomes without creating another storage engine or
making Workflows depend on Studies. EPSM owns Building assembly and combined
evaluations. Core, RC and LCA keep their calculations and result meanings.

The first complete route contains one baseline and two physical alternatives,
each evaluated by RC and EnergyPlus using the same declared weather. Its six
evaluations retain hourly heating, common energy accounting, embodied assessment,
input identities and every attempt. The study can be reopened in a fresh process
and queried by building, physical case, engine, weather and run. General helpers
provide inspection, selection, summaries, pairing and explicit export. Detailed
statistical analysis and paper-specific interpretation remain outside this work.

Sampling and comparison are separate choices. LHS and Monte Carlo produce
candidate cases; a frozen baseline can accompany either design. Parameters have
declared types, units, ranges or categories, distributions, baseline values and
scope. A portfolio declares whether a sampled value is shared across buildings
or sampled independently. Engine pairing reuses the same physical case rather
than creating two independently authored buildings.

## Starting source inventory

These are the confirmed development sources used to create isolated campaign
worktrees. They are source evidence, not a claim about installed or published
packages. Primary working directories contain existing work and remain intact.

| Package | Declared version | Starting development commit | Reuse or remaining need |
| --- | --- | --- | --- |
| Data | 0.6.0 | `065c1f9aab5e5baa881e11dcb19834521181d7de` | Reuse portable constructions, archetypes, profiles and factors; no new catalogue format |
| Core | 0.8.1 | `9dab5030cf1c69af9133490dbadc87f152378920` | Reuse physical models, readiness and EnergyPlus outputs; verify requested result coverage |
| RC | 0.8.3 | `1f97a20b949394e7dc65cf8f2e6898d823d8c445` | Reuse context shading and explicit reduction; preserve hourly heating and its calendar |
| LCA | 0.2.0 | `8d2a56541778f7285a83b69f8670e3b1b8a66fd2` | Reuse assessment boundaries, factors, contributions and incomplete-state reporting |
| Database | 0.3.0 | `2fbc6306cb791469148f1de6cb848f7903337187` | Reuse portable records and evidence; no database migration or new live service |
| Weather | 1.2.0 | `fd21431afdb0c918d7a2745cd49bd8ddba91fc6a` | Reuse EPW/AMY; review the existing batch and scenario-morphing branch separately |
| EPSM | 0.3.1 | `9cc966038c800b1e6258925ee32af4dc01462e67` | Add portable complete evaluation reading/writing and coverage-aware retention |
| Workflows | 0.3.1 | `649634d15a4dc7e92fd1d660626a1ddbbefe3cd0` | Reuse prepared execution; add reusable authoring, expansion and result requirements |
| Studies | 0.3.0 | `587f9088ae44391e01e9012ca78f17ba76bf1208` | Add a study result collection over Workflows artifacts and general evaluation helpers |

The pre-existing weather branch `codex/amy-scenario-morphing` includes batch AMY
and optional SSP/RCP morphing at `a44eb56`. It is an existing candidate to review,
not a release promise or a reason to duplicate its implementation. The campaign
uses Data's freshly fetched lowercase `dev`; older local checkouts can retain a
stale uppercase `DEV` reference and should not determine the starting point.

Current dependency ownership is Data → Core → RC/LCA, followed by EPSM assembly
and evaluation, Workflows execution, and Studies interpretation. Database and
Weather supply independent inputs. Optional integration extras can reference the
application; they do not authorize reverse scientific ownership. Build candidate
wheels first and install them together so optional dependency cycles do not
determine promotion order.

## Acceptance scenarios

Every scenario needs owner-level tests and the relevant installed-package
handoff. Fast fixtures stay small and offline. Real engine, database, provider
and cluster checks run only where their behaviour is being claimed; a missing
required prerequisite fails that gate.

| ID | Required observable behaviour |
| --- | --- |
| SP01 | Author, validate and save a fixed, grid, seeded LHS or seeded Monte Carlo design; reject invalid ranges, categories, distributions and unsupported bindings before execution |
| SP02 | Preview deterministic case counts and identities for one building or a portfolio, including shared/independent sampling and explicit weather mapping |
| SP03 | Freeze a complete baseline; preserve it while alternatives change; pair identical physical cases across engines and preserve baseline relationships |
| SP04 | Require results by metric, resolution, building and run before submission; unsupported requests have actionable diagnostics rather than silent omission |
| SP05 | Retain hourly heating with units, calendar and interval meaning, energy boundaries, assessment modules/contributions and completeness reasons; missing values never become zero |
| SP06 | Interrupt, retry and resume without losing attempts; reject changed input or runtime identities; retain a visible outcome for every case and required result |
| SP07 | Reopen results independently of the original process or working directory; detect missing, malformed or changed artifacts and unsupported stored formats |
| SP08 | Select and summarize by building/run/engine; pair baseline changes and same-input engine comparisons; reject incompatible units, coverage or assessment boundaries |
| SP09 | Execute the six-evaluation route from clean installed candidate wheels, including actual annual RC and EnergyPlus, declared embodied assessment and fresh-process reopening |
| SP10 | Reject incomplete coverage in a required-result gate while keeping successfully computed energy or assessment components available for inspection |

All new public operations need normal, missing-input, boundary and failure tests.
Tests cover serialization and mutation isolation, calendar alignment including
leap years, units/reference area, duplicate/missing pairs, interrupted publication,
and retained failures. Compare physics with justified tolerances and established
owner references; this campaign does not change numerical assumptions merely to
make two engines agree.

## Commit and promotion sequence

1. Record the ownership and acceptance agreements, starting revisions and reuse
   decisions. Work in separate `codex/study-platform-readiness` worktrees; preserve
   unrelated edits and earlier artifacts.
2. Add result requirements and portable evaluations, then study authoring and
   deterministic expansion. Commit each complete observable behaviour with tests,
   documentation and small public examples in its owning repository.
3. Add the Studies result collection, paired comparisons and general helpers.
   Keep detailed analysis out. Commit each tested handoff separately.
4. Extend the existing EPSM compatibility tools to capture an immutable candidate
   cohort, build wheels and run selected installed scenarios. Record actual
   sources, wheel hashes, runtime versions, commands, failures and skips.
5. Complete the six-evaluation route and all required owner and installed checks
   before campaign merges into development. Report statement and branch coverage
   and meaningful untested paths. Run examples from fresh kernels.
6. Review feature PRs into development in dependency order. Check conflicts on
   the feature branches, resolve them without discarding work, then rebuild and
   rerun affected checks against the actual development merge commits. Git cannot
   make the multi-repository merge atomic.
7. Freeze the checked development cohort, finish versions/release notes and open
   release PRs into `main`. Preserve shared history through normal release merges,
   tag each resulting `main` commit, publish from the tags and synchronize released
   history back into development.
8. Verify installed release artifacts and promote EPSM's supported manifest to
   the checked owner identities. Keep candidate records distinct from supported
   releases; publish the final evidence and remaining limits here by reference.

The existing [compatibility contract](platform-compatibility.md) remains the
source of package pins. Candidate receipts capture all actual source revisions;
EPSM's `self` entry resolves to the captured EPSM checkout without a circular
commit hash. Required owner tests, real-engine checks, installed handoffs and
fresh examples remain separate gates. Earlier passing runs cannot be relabelled
as evidence for later conflict resolutions or releases.

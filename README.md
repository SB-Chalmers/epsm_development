# EPSM Development

<!-- EPSM introduction: Pocket CAD -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/brand/epsm_development-dark.png">
  <img src="docs/assets/brand/epsm_development.png" width="64" height="64" alt="EPSM Development — developer handbook">
</picture>

Learn how to build and contribute to EPSM through shared engineering guides, examples and templates.

[Explore the EPSM platform](https://github.com/SB-Chalmers/epsm/blob/main/docs/platform.md)
<!-- /EPSM introduction -->

This is our handbook for building EPSM, the Swedish building-stock research platform. The coding guides, package review, templates, example notebooks and plans are kept here in one repository.

The agreed package names are `epsm`, `epsm_db`, `epsm_data`, `epsm_core`, `epsm_workflows`, `epsm_studies`, `epsm_rc`, `epsm_lca` and `smhi2epw`. This handbook is `epsm_development`; the web application is `epsm_studio`. These names were confirmed on 14 October 2026. The current source boundary adds `epsm_viewer` on 20 October 2026 for 3D browser/notebook display; Core supplies scene data and Studio owns application adapters. See the [plot and preview guide](docs/plotting-and-previews.md), [harmonisation guide](docs/harmonisation.md), and [repository review register](docs/harmonisation-review.md). Dated release and review snapshots retain their original evidence.

The handbook is written for the people who build and use EPSM. Coding agents follow the same instructions. Start with one small task, find the package that owns it, and write a test that shows the behaviour you want.

**Version:** Handbook v0.6.0 candidate, 21 October 2026. The
[study platform campaign](docs/study-platform-readiness.md) records composed
study authoring, owner boundaries, portable results and the staged acceptance
and release gates. Its candidate work does not change Studio.

The preceding handbook source was v0.5.1, 20 October 2026. The
[Studio readiness record](docs/studio-readiness-2026-10-20.md) records the released
owner packages and published EPSM 0.3.1 combination. Its scientific, display and
metadata checks passed, as did the six consumer owner runs, active documentation
follow-ups and final coordinated metadata verification. The handbook's own hosted
checks and release identities belong to its
[publication receipt](https://github.com/SB-Chalmers/epsm_development/releases/tag/v0.5.1)
when published. The [platform compatibility guide](docs/platform-compatibility.md)
defines EPSM's central manifest and how consumers adopt it on their next normal
CI run. Viewer 0.1.0 is available through authenticated private GitHub release
downloads, with its actual installation evidence in the readiness record.

The preceding published handbook was v0.5.0. Its
[archetype release record](docs/archetype-release-2026-10-15.md) identifies its
released Data 0.6.0, Core 0.4.0, Database 0.3.0 and EPSM 0.3.0 combination, exact
verification and manual protection limitation. The
[archetype authoring and application route](docs/archetype-authoring.md) is
implemented in those releases; its
[development verification register](docs/archetype-verification.md) remains dated
historical evidence. The preceding [logging verification](docs/logging-verification.md),
[stabilization record](docs/stabilization-2026-10-15.md) and
[review register](docs/harmonisation-review.md) remain available. Reusable study
and execution tools remain active; outdated named studies and scripts are
archived under the [study archive decision](docs/study-archive-policy.md).
Code labelled **illustrative API** describes a possible user experience and is
not an implemented API.

## Start here

1. Read [How to contribute](CONTRIBUTING.md) for a short guide to making a change.
2. Read [Project layout](docs/project-layout.md) and [Inputs, outputs and package APIs](docs/io-and-api.md) before starting a module.
3. Find your topic in [Engineering and API style](docs/engineering-style.md).
4. Try the [small example notebooks](examples/README.md). Read [Examples and common use cases](docs/examples-and-use-cases.md) when adding an example to a package.
5. Read [Harmonisation](docs/harmonisation.md) for the released APIs and their limits. The [ecosystem review](docs/ecosystem-review.md) and [original roadmap](docs/roadmap.md) preserve the earlier review and its rationale.

Coding agents should also read [AGENTS.md](AGENTS.md).

**License:** This handbook uses the [MIT license](LICENSE). All EPSM projects adopt [the shared MIT licensing policy](docs/licensing.md) for their own code and documentation.

## The basic rules

- **Small, clear responsibilities.** Each package does a few things well and calls the package that owns the next step.
- **Tests first.** Describe a useful behaviour in a test, see it fail, then make it work.
- **Readable code.** Use the names and ideas researchers already work with: buildings, weather, studies, workflows and results.
- **Helpful documentation.** Explain inputs, units, assumptions and examples with the care used in EPSM Core.
- **Useful logs.** Every important operation leaves a clear trace. The application controls where that trace is stored.
- **Friendly inspection.** Printing an object gives a short, useful description. Detailed information is available when requested.

## Find what you need

| If you want to… | Read… |
| --- | --- |
| Know which package should own a feature | [Package responsibilities](docs/engineering-style.md#responsibility-boundaries) |
| Review current packages and file transfers | [Harmonisation guide](docs/harmonisation.md), [file map](docs/harmonisation-file-map.md) and [review register](docs/harmonisation-review.md) |
| Distinguish maintained study tools from archived research | [Study archive decision](docs/study-archive-policy.md) |
| Understand Study, Workflow, Record and Building | [Shared terms and models](docs/terminology-and-models.md) |
| Follow archetype authoring and application work | [Authoring and class diagram](docs/archetype-authoring.md), [implementation series](docs/archetype-implementation.md) and [verification register](docs/archetype-verification.md) |
| Add consistent 2D plots and 3D previews | [Plots and previews](docs/plotting-and-previews.md) |
| Write tests before changing code | [Test-driven development](docs/engineering-style.md#test-driven-development) |
| Write clear instructions | [Writing for people](docs/writing-guide.md) |
| Write clear code and useful docstrings | [Source and documentation](docs/engineering-style.md#human-readable-source) |
| Add friendly docstring examples and generated API pages | [Docstrings and API documentation](docs/docstrings-and-api-docs.md) |
| Apply the shared MIT license and retain source notices | [MIT licensing](docs/licensing.md) |
| Set up a repository and its project information | [Project layout](docs/project-layout.md) |
| Start a feature, experiment or release | [Branches and releases](docs/branches-and-releases.md) |
| Adopt a reviewed package combination without duplicated CI pins | [Platform compatibility](docs/platform-compatibility.md) |
| Prepare reusable study authoring, retained results and paired engines | [Study platform readiness](docs/study-platform-readiness.md) |
| Check the current Core, Viewer and Studio preparation | [Studio readiness record](docs/studio-readiness-2026-10-20.md) |
| Read and write data, or pass it to another package | [I/O modules and package APIs](docs/io-and-api.md) |
| Add a notebook that teaches a package | [Examples guide](docs/examples-and-use-cases.md) |
| Find a shared example of a research task | [Common use cases](use_cases/README.md) |
| Follow the coordinated logging implementation | [Logging across packages](docs/logging.md) |
| Add logging that works across packages | [Uniform logging](docs/engineering-style.md#uniform-logging) |
| Give an object a helpful `repr` | [Representation and inspection](docs/engineering-style.md#object-representation-and-inspection) |
| Start a module or public object | [Templates](docs/templates/README.md) |
| Check the handbook before submitting a change | [Documentation checks](#check-the-handbook) |

## Check the handbook

Use Python 3.11 or newer. No extra packages are needed:

```sh
python3 scripts/check_docs.py
python3 -m unittest discover -s tests -v
python3 scripts/run_examples.py
```

The check verifies local files and heading links, Python example syntax, notebook structure, and the runnable examples in the templates. The small test suite checks that broken links and examples are reported clearly. Future API sketches are checked for syntax only. They are not executed or counted as working platform features.

With the supported EPSM packages installed, also run
`python scripts/check_platform_examples.py` to execute the handbook’s public
authoring snippets. This optional check needs no database, weather or engine;
simulation snippets retain their separately stated prerequisites.

The notebook runner starts each learning notebook with fresh variables using only Python. It runs this handbook's small, plain-Python notebook examples. Package notebooks that use a database, EnergyPlus or notebook display tools need their declared environment and a real notebook runner.

To check the Sphinx templates as well, use an environment with the optional documentation tools:

```sh
python -m pip install -r requirements-docs.txt
python scripts/build_api_example.py
```

This creates an API reference under `build/api-preview/` and treats documentation warnings as errors. The generated files are ignored by Git. CI runs this check separately from the ordinary handbook checks.

## Help improve this handbook

If a rule is hard to understand, bring a small example. Explain what you tried and what was unclear. Improvements to the wording, examples and developer experience are welcome.

Keep changes to the handbook focused. Changing a guideline does not automatically change the software in the other EPSM repositories.

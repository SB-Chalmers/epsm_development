# EPSM Development

Welcome. This is the shared developer handbook for EPSM, our Swedish building-stock research platform. It brings together the engineering guidelines, package review, API design ideas and next steps.

The handbook is for people and coding agents. You do not need to understand the whole platform before contributing. Start with one small task, find the package that owns it, and write a test that shows the behaviour you want.

**Status:** Working draft v0.2, 13 October 2026. The new EPSM interface is still being designed. Code labelled **illustrative API** shows a possible user experience; it is not an API you can use today.

## Start here

1. Read [How to contribute](CONTRIBUTING.md) for a short guide to making a change.
2. Read [Project layout](docs/project-layout.md) and [Inputs, outputs and package APIs](docs/io-and-api.md) before starting a module.
3. Find your topic in [Engineering and API style](docs/engineering-style.md).
4. Try the [small example notebooks](examples/README.md). Read [Examples and common use cases](docs/examples-and-use-cases.md) when adding an example to a package.
5. Read [The ecosystem review](docs/ecosystem-review.md) for the current state, or [The roadmap](docs/roadmap.md) for the proposed next steps.

Coding agents should also read [AGENTS.md](AGENTS.md).

## What we want EPSM development to feel like

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
| Understand Study, Workflow, Record and Building | [Domain vocabulary](docs/engineering-style.md#domain-vocabulary-and-containment) |
| Write tests before changing code | [Test-driven development](docs/engineering-style.md#test-driven-development) |
| Write clear code and useful docstrings | [Source and documentation](docs/engineering-style.md#human-readable-source) |
| Set up a repository and its project information | [Project layout](docs/project-layout.md) |
| Start a feature, experiment or release | [Branches and releases](docs/branches-and-releases.md) |
| Read and write data, or pass it to another package | [I/O modules and package APIs](docs/io-and-api.md) |
| Add a notebook that teaches a package | [Examples guide](docs/examples-and-use-cases.md) |
| Find a shared example of a research task | [Common use cases](use_cases/README.md) |
| Add logging that works across packages | [Uniform logging](docs/engineering-style.md#uniform-logging) |
| Give an object a helpful `repr` | [Representation and inspection](docs/engineering-style.md#object-representation-and-inspection) |
| Start a module or public object | [Templates](docs/templates/README.md) |
| Check the handbook before submitting a change | [Documentation checks](#check-the-handbook) |

## Check the handbook

Use Python 3.11 or newer. No extra packages are needed:

```sh
python3 scripts/check_docs.py
python3 -m unittest discover -s tests -v
```

The check verifies local files and heading links, Python example syntax, notebook structure, and the runnable examples in the templates. The small test suite checks that broken links and examples are reported clearly. Future API sketches are checked for syntax only. They are not executed or counted as working platform features.

To run the learning notebooks from a clean namespace using only Python:

```sh
python3 scripts/run_examples.py
```

This runs this handbook's small, plain-Python notebook examples. Package notebooks that use a database, EnergyPlus or notebook display tools need their declared environment and a real notebook runner.

## Help improve this handbook

If a rule is hard to understand, bring a small example. Explain what you tried and what was unclear. Improvements to the wording, examples and developer experience are welcome.

Keep changes to the handbook focused. Changing a guideline does not automatically change the software in the other EPSM repositories.

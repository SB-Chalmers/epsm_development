# Contributing to EPSM

Welcome to the project. A good contribution can be small: a clearer example, a test for a bug, a better error message or one well-defined feature.

## Choose a small task

Write down the behaviour you want to change and which package owns it. The [responsibility table](docs/engineering-style.md#responsibility-boundaries) can help. If the task crosses packages, describe what one package sends to the next.

Check the [common use cases](use_cases/README.md) for a task that already describes the expected behaviour. The [project guide](docs/project-layout.md) explains where code, tests, examples and project information belong.

You do not have to redesign a whole package to fix one problem. Keep the change small enough that another person can understand and check it.

## Start from dev

`main` holds stable releases. `dev` is the shared home for development. Start a feature or experiment branch from the current `dev`, then send the completed change back to `dev` through a reviewed pull request.

Ordinary feature work does not go straight to `main`. A tested version reaches `main` through a release pull request and gets a version tag. See [branches and releases](docs/branches-and-releases.md) for the commands, release checks and urgent-fix route.

## Work from a test

For a new behaviour or a bug fix:

1. Write a test that shows what the user or researcher needs.
2. Run it and check that it fails for the right reason.
3. Write the code that makes it pass.
4. Improve the code's clarity while keeping the tests passing.
5. Update the docstring and example to match the behaviour.

When reorganizing existing code, first add tests for the behaviour that must stay the same. A change to scientific assumptions needs its own explanation and comparison evidence.

For documentation changes, check the links and examples. You do not need to invent a software test for a spelling fix.

## Make the change easy to understand

Write as you would explain the work to a colleague. Use ordinary words, name the action and give a small example. See [Writing for people](docs/writing-guide.md).

Use clear names. State units and assumptions. Explain the important decisions in docstrings and comments. The [module and object templates](docs/templates/README.md) provide a starting point; replace their instructions with accurate information about your code.

Put reading and writing in the package's I/O module. Keep calculations and model choices in their owning modules. Use the next package's documented public API, and test the data it receives. See [inputs, outputs and APIs](docs/io-and-api.md).

Log important operations using the shared conventions. Keep logging configuration in the application. Give public objects a short representation that helps someone understand their identity and current state.

## Help the reviewer

Describe the problem, the resulting behaviour and how you checked it. Mention anything that is still uncertain. Include the commands and relevant test results, including skipped checks.

For a change to this repository, run:

```sh
python3 scripts/check_docs.py
python3 -m unittest discover -s tests -v
```

For a change to an EPSM package, run the tests that cover the changed behaviour and its data passed between packages. The package's own instructions explain its additional checks.

Add or update a small notebook in `examples/` when a public feature needs a usage example. Teach the package on its own first, then show the next package it connects to. Restart the kernel and run all cells in order. Follow [the examples guide](docs/examples-and-use-cases.md).

## Keep design sketches clearly labelled

The new EPSM interface is still being discussed. If an example uses an API that does not exist yet, label it **illustrative API** and explain what decision it helps us explore.

Please keep questions and examples in the open so the next developer or agent can follow the reasoning.

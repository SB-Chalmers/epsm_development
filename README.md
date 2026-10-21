# epsm_development

[![CI](https://img.shields.io/badge/CI-GitHub_Actions-2088FF?logo=githubactions&logoColor=white)](https://github.com/SB-Chalmers/epsm_development/actions/workflows/ci.yml) [![Releases](https://img.shields.io/badge/releases-GitHub-181717?logo=github&logoColor=white)](https://github.com/SB-Chalmers/epsm_development/releases) [![Issues](https://img.shields.io/badge/issues-GitHub-181717?logo=github&logoColor=white)](https://github.com/SB-Chalmers/epsm_development/issues)

The developer handbook for EPSM, a Swedish building-stock research platform.
Find shared engineering and writing guides, package responsibilities, examples
and templates for contributing to the platform.

## Getting started

Start with [How to contribute](CONTRIBUTING.md), then read the
[engineering guide](docs/engineering-style.md) and try the
[small example notebooks](examples/README.md). Coding agents also follow
[AGENTS.md](AGENTS.md).

To check the handbook locally, use Python 3.11+ and Git. No extra packages are
needed for these checks.

```sh
git clone https://github.com/SB-Chalmers/epsm_development.git
cd epsm_development
python3 scripts/check_docs.py
python3 -m unittest discover -s tests -v
python3 scripts/run_examples.py
```

## Documentation

- [Handbook index and detailed guidance](docs/guide.md)
- [Package responsibilities and engineering style](docs/engineering-style.md)
- [Writing guide](docs/writing-guide.md)
- [Branches and releases](docs/branches-and-releases.md)
- [Examples and common use cases](docs/examples-and-use-cases.md)

## License

[MIT](LICENSE). See the [shared licensing policy](docs/licensing.md) for
EPSM-owned material and retained third-party terms.

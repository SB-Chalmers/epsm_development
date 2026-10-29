# EPSM Development

<!-- EPSM introduction: Pocket CAD -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/welcome/epsm_development-dark.png">
  <img src="docs/assets/welcome/epsm_development.png" width="160" height="160" alt="EPSM Development — An open engineering handbook; the active right page represents shared development guidance.">
</picture>

Welcome to the EPSM developer handbook. Whether you are trying your first
example or contributing a new feature, start here for shared engineering guides,
package responsibilities and small worked examples. Pick one task and find the
package that owns it.

**[Explore the EPSM platform →](https://github.com/SB-Chalmers/epsm/blob/main/docs/platform.md)**
<!-- /EPSM introduction -->

[![CI](https://img.shields.io/badge/CI-GitHub_Actions-2088FF?logo=githubactions&logoColor=white)](https://github.com/SB-Chalmers/epsm_development/actions/workflows/ci.yml) [![Releases](https://img.shields.io/badge/releases-GitHub-181717?logo=github&logoColor=white)](https://github.com/SB-Chalmers/epsm_development/releases) [![Issues](https://img.shields.io/badge/issues-GitHub-181717?logo=github&logoColor=white)](https://github.com/SB-Chalmers/epsm_development/issues)

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
- [Harmonised release record, 29 October 2026](docs/harmonised-release-2026-10-29.md)
- [Examples and common use cases](docs/examples-and-use-cases.md)

## License

[MIT](LICENSE). See the [shared licensing policy](docs/licensing.md) for
EPSM-owned material and retained third-party terms.

## People and support

Developed at Chalmers University of Technology as part of the EPSM research platform.

**Funding**: Swedish Energy Agency (Project ID: P2024-04053)

**Partners**:

- Lindholmen Science Park AB
- Sinom AB
- Stiftelsen Chalmers Industriteknik

**Team**:

- **Lead Developer**: Sanjay Somanath
- **Principal Investigator**: Alexander Hollberg
- **Contributors**: Yinan Yu, Dag Wästberg

<p align="center">
  <img src="docs/assets/welcome/logos.png" width="100%" alt="Chalmers University of Technology, Chalmers Industriteknik, Sinom, Lindholmen Science Park and Swedish Energy Agency logos">
</p>

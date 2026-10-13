# MIT licensing across EPSM

Use the MIT license for EPSM's own software and associated documentation, examples, notebooks and templates. This is the shared policy for every EPSM project, including the umbrella interface, Core, Catalogue, Database, Workflows and future method packages.

Every repository adopts the policy through its own `LICENSE` file, source notices and package metadata. Using EPSM, importing another EPSM package or adding this guide does not automatically license an existing repository or its data.

## What MIT means for users

MIT allows people to use, modify and share the software, including for commercial work. When they distribute copies or substantial portions, they must retain the copyright and permission notices. The software is provided without warranty. These terms come from the [official MIT license](https://opensource.org/license/mit).

MIT does not require a user to publish their own modifications. Research citation is welcome, but it is not an extra condition added to the MIT license. Keep citation instructions separate from the unchanged license text.

## Set up a repository

1. Copy the [MIT license template](templates/LICENSE-MIT.txt.tmpl) to a file named `LICENSE` at the repository root.
2. Replace the year and copyright-holder placeholders with truthful information. Keep existing copyright notices. Use multiple notices when different holders own different contributions.
3. State **MIT** in the README and link to the root `LICENSE` file.
4. Add the MIT identifier to first-party source headers and declare the license in package metadata.
5. Include the license and any required third-party notices in published source archives and wheels. Check the built files before release.

Keep the MIT grant and disclaimer unchanged. Do not add a research-only or noncommercial restriction and continue calling the result MIT.

The copyright holder is the person or organisation that owns the work. An author, project lead or institution listed for attribution is not automatically its holder. Git commit names alone do not settle ownership. Preserve accurate existing notices and establish the holder for new material before publishing it.

This handbook uses the collective notice “EPSM Development contributors” for its original material in [its license](../LICENSE). That label does not transfer ownership or replace notices attached to imported work. Other repositories use their own accurate holder notices; do not copy Core's named holder or this handbook's notice as a placeholder.

## Use consistent source headers

For a new first-party EPSM module, use:

```text
# SPDX-License-Identifier: MIT
# Copyright (c) <year or year range> <actual copyright holder or holders>
# License: See LICENSE at the project root.
```

SPDX is the standard identifier used by tools to recognise a license. `MIT` is its identifier for this license. The header points to the full text; it does not replace the repository's `LICENSE` file. Keep the fuller purpose, author and research information from the [module templates](templates/README.md).

## Declare the license in Python packages

For a package using a build backend that supports the current Python packaging license fields, put this under the existing `[project]` section of `pyproject.toml`:

```toml
[project]
license = "MIT"
license-files = ["LICENSE"]
```

This example describes a distribution containing first-party MIT material. If it bundles material under other licenses, include those notices and use the expression appropriate to the actual distribution. A dependency installed separately is different from code or assets copied into the package.

Check the backend's support before changing metadata. Setuptools supports these fields from version 77.0.0; declare a suitable minimum build dependency when adopting them, as described in its [configuration guide](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html). Replace conflicting legacy license fields or license classifiers. Inspect the built wheel and source archive to confirm their license metadata and included notices. The [Python Packaging User Guide](https://packaging.python.org/en/latest/guides/licensing-examples-and-user-scenarios/) explains the fields and bundled-code cases.

EPSM Development is a handbook rather than a Python distribution, so it does not need a `pyproject.toml` just to declare its license. Its root license and README carry that information.

## Keep source and third-party terms

The common policy applies to material EPSM can license. Keep these distinctions clear:

| Material | What to do |
| --- | --- |
| Original EPSM code, documentation and teaching examples | Use MIT and retain truthful copyright notices. |
| Copied or bundled third-party code, fonts, browser assets or figures | Keep the original license and required notices. Record their source and terms. Do not relabel them as EPSM-owned MIT material. |
| Building records, source datasets, certificates and evidence documents | Record the provider's license, access terms and permission to redistribute. Their terms do not change when they enter EPSM Database. |
| Weather files and downloaded provider data | Keep source and generation information and the terms applying to the supplied data. The weather software's MIT license does not settle those terms. |
| Catalogue definitions, copied tables, factors and supporting evidence | Record their sources and applicable terms. A software license does not establish permission to republish a source table. |
| Simulation outputs, research reports and published study artifacts | State the relevant data/publication terms and any source restrictions. Do not assume the producing software's license settles the output's terms. |

Preserve third-party notices when moving code or assets between packages. For example, Core's bundled Three.js has its own MIT notice; it remains attached even though both projects use MIT.

For incoming contributions to EPSM's own code and documentation, contributors must have the right to submit the material under MIT. Record any imported material and its separate terms in the same change. This policy does not require an additional copyright transfer agreement.

## Adopt the policy in existing repositories

Before the next release, check each repository's root license, source notices, README and package metadata together. Preserve the license history. An existing non-MIT contribution needs the relevant rights before it can be relicensed; changing a metadata string does not supply those rights.

A quick local check on 13 October 2026 found:

| Repository | License declaration found | Adoption work |
| --- | --- | --- |
| EPSM Development | MIT root license added with this guide | Keep templates and notices consistent. |
| EPSM Core | Root MIT license; no `[project]` license fields | Add supported package metadata and check bundled notices in built distributions. |
| EPSM Data, planned Catalogue | No root license or `[project]` license fields found | Establish accurate notices, add the MIT license and metadata, and record data/evidence terms. |
| EPSM Workflows | No root license or `[project]` license fields found | Establish accurate notices, add the MIT license and metadata, and preserve study/source terms. |
| Sweden UBEM, planned EPSM Database | No root license or `[project]` license fields found | Establish accurate notices, add the MIT license and metadata, and keep source-data terms separate. |
| `smhi2epw` | Root MIT license and MIT package declaration | Keep notices and provider-data terms clear; check the published distribution. |

This is a check of declarations, not a full review of every dependency or data source. This change licenses the handbook and supplies the shared policy; it does not edit or relicense the other repositories.

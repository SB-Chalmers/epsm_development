# EPSM harmonisation

**Implementation update, 14 October 2026.** The agreed object model is implemented
on the coordinated `codex/harmonisation` development branches. This page describes
the new APIs and their present limits. It does not declare a released platform or
scientific validation. See the [file map](harmonisation-file-map.md) for ownership
changes and remaining migration work. The [review register](harmonisation-review.md) records per-repository findings and verification.

## Decisions to discuss

The architecture decisions from the earlier review are now accepted: one physical
Building implementation, one Stock implementation, Data-owned construction
classes, direct `building.simulate(...)`, undated renovation trees and one current
catalogue. Remaining questions concern scientific inputs and the next supported
geometry/assessment cases. They do not reopen these package boundaries.

## Package responsibilities

| Package | Owns |
| --- | --- |
| `epsm_data` | Lightweight shared construction classes, current catalogue, sourced operation/HVAC templates, factors and renovation descriptions |
| `epsm_core` | Physical Building and elements, geometry, quantities, physical transformations, readiness, Weather and EnergyPlus calculation |
| `epsm_db` | Database, Stock, BuildingRecord, source evidence, observations, queries and evidence completeness |
| `epsm_rc` | Reduction of the same physical Building to the existing 5R1C calculation |
| `epsm_lca` | Application of material-flow and operational environmental factors under an explicit boundary |
| `epsm` | Researcher-facing Building subclass, record/catalogue adapters, engine dispatch, automatic LCA and Results |
| `epsm_workflows` | Reusable experiment designs, renovation search, prepared local/Vera execution and resume |
| `epsm_studies` | Named study protocols, archived research implementations, analyses and paper outputs |
| `smhi2epw` | Independent weather acquisition, preparation, EPW export and quality reporting |
| `epsm_development` | This handbook, contracts, migration map and development guidance |

Core depends on Data. Data construction imports perform no catalogue loading and
do not depend on Core. EPSM extends Core's Building without copying its physical
schema. Studio replacement is outside this implementation.

## Construction and physical data

The shared graph is `Material → Layer → Component → Element → ConstructionSet`.
An Archetype is a named/classified construction set. HVAC and operation profiles
are separate choices. Layers preserve parallel fractions and constituent
thicknesses; components preserve explicit order. Immutable value objects offer
validated replacement methods. A Building owns independent assignments.

Data's Element is a construction recipe. Core's BuildingElement is an actual
physical wall, roof, floor or window with geometry and an assignment. Material
inventory traverses those physical elements. It does not count thermal zones as
physical material. Window area and equipment counts can be known while mass is
unknown. Thermal equivalents never replace the physical inventory.

Physical snapshots are independent of weather and evaluation services. Core
serializes renovation lineage separately; EPSM's portable Building envelope
retains both the physical state and lineage, assessment settings and source
evidence. Portable DB records omit the live database connection and credentials.

## Current catalogue

The active catalogue stores resolved current values and complete recipes. It does
not keep a runtime chain of prior catalogue releases and overrides. Source
identifiers and derivation notes remain; study-specific validation artifacts are
preserved with Studies. Git history remains intact.

SE.01–SE.05 keep their periods. SE.06 covers **2006–2021 inclusive**. SE.07 covers
**2022 onward**, initialized from independent copies of all SE.06 Advanced
configurations and recipes. SE.07 has no renovation states; an explicit
Existing/Standard/Advanced request is rejected. Copying was a migration check,
not a permanent equality constraint. These copied assumptions are not new
measurement evidence for post-2021 buildings.

## Working with a Building

```python
from epsm import Building, Weather

building = Building()  # Named illustrative reference preset.
blank = Building.empty()
inventory = building.quantities().by_material()
readiness = building.readiness(engine="energyplus")

weather = Weather.from_epw("weather.epw")
result = building.simulate(engine="energyplus", weather=weather)
print(result.energy.scalars)
print(result.lca.status, result.lca.requirements)
print(building.results.latest)
```

The example requires an EPW and EnergyPlus installation. `engine="epsm_rc"` uses
the reduced-order adapter. `Building.from_footprint(...)` and
`Building.from_record(record, ...)` author known inputs and expose missing ones.
The default reference is illustrative, not a measured or calibrated building.

`building.results` is always a collection. Each evaluation freezes its inputs,
retains weather and settings, and contains energy, LCA, quantities and diagnostics.
Editing the Building preserves earlier results. `for_current_state(building)`
filters matching evaluations. Energy and LCA cache identities are separate.

## Renovation and assessment

`child = baseline.renovate(*measures)` applies one bundle transactionally. The
parent stays unchanged. The child retains its parent and path and begins with no
results. Bundles select actual physical elements; component replacements preserve
unaffected occurrences. Like-for-like replacement records removal and installation.
There are no required dates or predefined stage slots.

Assessment settings explicitly choose the reference period, energy boundary,
baseline treatment, modules and sourced factors. Missing factors or quantities
produce incomplete totals. Assessment failure preserves successful energy.
Operational impact uses the reached building over the chosen period; ancestor
buildings receive no inferred operating years. Installed and removed occurrences
are counted along the path, without repeatedly counting retained inventory.

The first common energy objective is **space heating plus ventilation fans**.
Both engines distinguish demand from carrier input. DHW and cooling remain
separate outputs; their delivered-energy boundary is not silently invented.
Supported LCA modules cover declared installation/removal factors and operational
B6. Future replacements and end-of-period demolition need explicit further
methods. A result is not automatically a complete standardized whole-building LCA.

## Workflows and preservation

Workflows provides parametric designs, sensitivity analysis and bounded renovation
tree search. Intermediate alternatives remain candidates; dominated prefixes are
still explored. Incomplete carbon or energy excludes a candidate from the feasible
Pareto set. Search checkpoints retain results and validate configuration identity.

Prepared JSON cases, weather assets and result artifacts support local execution
and SSH/rsync/Slurm staging on Vera. Transport and resume have offline tests; a
live Vera job is a separate deployment verification. Historical studies are
preserved with source commits and hash manifests in Studies. Compatibility routes
keep existing imports available while selected studies are ported.

## Verification and present limits

The implementation checks graph roundtrips, isolated assignment, physical quantity
identity, targeted and like-for-like changes, lineage serialization, independent
energy/LCA caching, missing-factor handling, catalogue boundaries and resumability.
Real local EnergyPlus and RC runs exercise the public Building interface.

The new physical authoring bridge currently supports detached flat-roof geometry
and explicitly supported basement cases. Existing complex Core geometry remains
available through the legacy API; unsupported new-model cases report limitations.
The RC adapter has one conditioned thermal domain and rejects unsupported explicit
shading and boundary configurations. These limits are distinct from scientific
prediction accuracy, which requires its own measured-data study.

Private cross-repository CI requires authenticated dependency access. A local
passing test run is not a claim that hosted CI or a Vera job has run. Intermediate
commits preserve independently reviewable changes; stable branches are not
silently promoted during the development refactor.

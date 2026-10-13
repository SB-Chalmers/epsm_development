# Plots and 3D previews

A researcher should be able to inspect a building, construction or result without learning a different plotting interface in every package. Use `.plot()` for 2D figures and `.view()` for 3D previews where the object has something useful to show.

**Status: shared design rules for adoption.** Existing packages differ in return types and display behaviour. The examples labelled illustrative below describe the intended interface, not methods already available everywhere.

## Keep rendering with the owner

Use a focused `plotting.py` module for a small 2D renderer. Use a `visualization/` package when 2D plots, 3D scenes and style adapters need separate files. Public objects delegate their `.plot()` and `.view()` methods to that implementation.

Each package renders the information it owns. Catalogue draws construction sections and assumptions; Core draws physical geometry and simulation results; Database can show evidence coverage; Weather can show weather series; Workflows can show study outcomes. Add an operation only where it serves a real use case. Packages and modules do not need empty renderers or a meaningless `.view()`.

Rendering may select or arrange already available data. Reuse the owner's geometry, metrics and diagnostic calculations. A plot must not quietly fetch records, choose assumptions or run a simulation to fill missing data. Keep missing values and conflicts visible.

The EPSM wrapper delegates to these renderers. Lower-level packages remain usable without the wrapper. Keep optional plotting/viewer imports local to the operation, and give a clear message describing the required extra if it is missing.

## Make `.plot()` predictable

Adopt these rules for new or redesigned 2D interfaces:

- Return a Matplotlib `Figure`, including for multi-panel plots. A caller can display it, adjust it or save it.
- Default to `show=False`. Do not save a file, open a browser or close a figure as a side effect. Display is an explicit caller choice; notebook display may render the returned figure.
- Give each object one useful default view. Additional `kind` choices belong to that object and are documented; do not build one universal plotting-options object.
- Accept a caller's `ax` for a supported single-panel plot and return `ax.figure`. Reject combinations that cannot use that axis. Do not clear or close a caller's existing plot.
- Use a local style context that restores the caller's settings before the call returns, including when it fails. Never change global Matplotlib settings on import.
- Document the plotted quantity, units, time/area basis, aggregation and handling of absent or conflicting values. Preserve the source data.

**Illustrative API:** a future result interface could be this simple:

```python
figure = result.plot(kind="monthly_heating")
figure.savefig("monthly-heating.svg")
```

Saving is explicit and its path belongs to the caller. For a comparison, use matching metric definitions, units, periods and axes. Show every relevant failed or missing case; do not drop it from a study plot without saying so.

A returned Figure supports Matplotlib's normal inspection and export operations. See [Matplotlib figures and axes](https://matplotlib.org/stable/users/explain/figure/axes_intro.html). New methods should document and test the chosen return type rather than alternate between a Figure, a table and `None`.

## Make `.view()` the 3D entry point

Use `.view()` for a physical 3D preview. Reuse Core's scene construction for Core geometry instead of rebuilding the same surfaces in each package.

Support the simplest notebook route first where the package can do so. Make a browser backend an explicit choice. State what each backend returns, how it displays, whether it writes files or starts a local server, and how the caller closes or cleans up the preview. Do not silently switch backends when a dependency is missing.

**Illustrative API:** the intended choices are:

```python
preview = building.view(backend="notebook")
browser_preview = building.view(backend="browser", launch_browser=False)
```

The exact backend argument and common preview interface still need to be agreed. Existing Core `.view()` returns a `ViewerHandle` and can write files, start a server and launch a browser. Its `.widget()` uses the same scene for a notebook preview. Harmonise those routes through one documented entry point before advertising the illustrative calls.

Show physical scale, axes and orientation. Identify the building, selected geometry and model revision. Explain excluded geometry or incomplete surfaces. A clipped, unloaded or missing part must not appear to be a verified complete model.

`repr()`, `str()` and ordinary object inspection must never start a renderer, write preview files or launch a server. A preview is an explicit operation.

## Use one visual style

Use white backgrounds, dark labels, light grid lines and readable sizes. Default to a sans-serif font available in the rendering environment. Preserve clear labels when a figure is resized or exported.

Use the versioned [palette file](assets/epsm-colours.json) as the reference for both Matplotlib and browser renderers. It is a proposed starting palette, not a claim that the existing packages use it. The category colours draw from the [Okabe–Ito colour guidance](https://jfly.uni-koeln.de/color/), with neutral grey and dark text added.

| Meaning when showing value origin or status | Colour | Additional cue |
| --- | --- | --- |
| Source observation | Blue `#0072B2` | Source label and circle marker; say reported or measured accurately |
| Derived value | Orange `#E69F00` | “Derived” label and triangle marker |
| Assumed value | Purple `#CC79A7` | “Assumed” label and dashed line |
| Missing or not loaded | Grey `#6B7280` | Gap, outline or hatch and a reason |
| Conflict or failure | Vermilion `#D55E00` | Cross marker and the specific conflict/failure label |
| Passed software check | Green `#009E73` | Named check and result; it does not imply scientific accuracy |

Colour must not be the only way to understand the figure. Use labels, markers, line styles or hatches as well. Check text and background contrast in the actual legend and export. A palette choice alone does not establish accessibility.

Keep value origin, execution status, material class and physical surface class separate. A wall's fill may show its material while an outline or label shows an assumed value. Do not use a source-observation colour to suggest that all geometry or thermal inputs are measured. Use a legend for the encoding chosen by that figure.

For numeric fields, use `cividis` as the starting sequential scale and a diverging scale centred on a meaningful reference, usually zero, for signed differences. Show a colourbar and units. Keep the same colour limits for a comparison and explain clipping. Missing values have their own representation, not the colour used for zero. Matplotlib's [colormap guide](https://matplotlib.org/stable/users/explain/colors/colormaps.html) explains these distinctions.

Use the same object names, short identifiers, units and state words as [object representations](engineering-style.md#object-representation-and-inspection) and [the shared glossary](terminology-and-models.md). Keep figures readable; put full provenance and assumptions in their accompanying Result or report rather than filling the title with metadata.

The handbook owns the palette definition. Package renderers own small adapters for their backend. Keep the palette version with those adapters and check it during integration/release work. Packages must not read this checkout at runtime. Once two packages adopt it, agree one small distribution route for the shared style asset rather than maintaining independent colour definitions.

## Check useful behaviour

Start with tests of the returned Figure or scene data. Check labels, units, colour tokens, selected values, missing/conflict cues, no input mutation and no change to global style. Check that a caller-supplied axis survives the call. An export smoke test can draw a small figure with a noninteractive backend.

For 3D, check that the scene matches the owning geometry, keeps identifiers and coordinates, and that a browser preview can close its server and release resources. Use real rendering for an advertised browser or notebook route. Mocking the whole renderer does not establish that the preview works.

Avoid exact image comparisons across platforms for every plot. Use a few reviewed reference images when layout or geometry needs that check. Keep numerical/scientific reference tests separate from rendering tests.

Add a small `examples/` notebook showing the default plot, a labelled comparison and explicit export. Where 3D is useful, add a preview example with setup and cleanup instructions. Docstrings should show a short public call and explain the returned object.

## What needs to change first

The current Catalogue `BuildingArchetype.plot()` returns a Figure but displays by default. Core result charts currently live in demo helpers; `SimulationResult` has no public `.plot()` yet. Core's browser and notebook previews already share scene construction. The packages use separate material, chart and surface colours.

Start by moving reusable result drawing to Core, preserving Catalogue's evidence-aware section drawing, making display choices explicit, and adapting both renderers to the shared palette. Treat return-type or display changes as API changes with tests and migration notes.

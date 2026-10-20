# Plots and 3D previews

A researcher should be able to inspect a building, construction or result without learning a different plotting interface in every package. Use `.plot()` for 2D figures where the object has something useful to show. Core produces `.scene()` data; the separate `epsm_viewer` package displays 3D scenes.

**Status: current viewer ownership updated 20 October 2026; shared 2D design rules remain for adoption.** Existing 2D packages differ in return types and display behaviour. Examples labelled illustrative are not methods already available everywhere. Earlier dated release and review snapshots retain their historical ownership and evidence.

## Keep scientific data with its owner

Use a focused `plotting.py` module for a small 2D renderer. Each package supplies
the geometry, metrics, units and diagnostic calculations it owns. Catalogue can
draw construction sections, Database evidence coverage, Weather weather series,
and Workflows study outcomes. Add a plot only where it serves a real use case.

Core exposes physical geometry and inspection metadata as portable scene data.
`epsm_viewer` owns the TypeScript renderer and optional Python display helpers.
Its input is a neutral `epsm.scene/1` dictionary; it does not import Core, select
assumptions, fetch records or run a simulation. Studio owns adapters between
package APIs and its UI. A scene method in Core remains a data operation, with no
browser, notebook widget, output directory or server.

Rendering may select or arrange loaded data. Preserve missing values and
conflicts. The EPSM wrapper may delegate to existing public operations; lower-level
packages remain usable without it. Optional display dependencies are explicit.
A missing viewer must produce an actionable error, not a silent backend switch.

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

## Pass scene data to the 3D viewer

Core's `GeometrySpec.scene(facade=..., context=...)`, `BuildingSpec.scene()` and
physical `Building.scene()` generate ready-to-consume geometry and metadata.
Core's `scene_data(model, report, diagnostics, preparation)` handles an already
loaded compiled model. Studio uses those public operations rather than copying
physical geometry calculations into a frontend adapter.

Install the separately built `epsm_viewer` Python wheel for browser display;
install its `notebook` extra for notebook display. It is optional and is not
assumed to be published on a package index. With that package installed:

```python
from epsm_core import Footprint, GeometrySpec
from epsm_viewer import scene_widget, view_scene

geometry = GeometrySpec.from_footprint(
    Footprint.rectangle(12, 8), storeys=2, storey_height_m=3,
)
scene = geometry.scene()
widget = scene_widget(scene)  # display(widget) in a live notebook.
widget.close()  # Close when finished inspecting.
with view_scene(scene, directory="output/preview", launch_browser=False) as preview:
    print(preview.url)  # Keep this context open while using the URL.
```

`scene_widget` returns a live widget; `view_scene` returns a context-managed local
server handle; `write_scene(scene, directory=...)` explicitly writes a static
bundle. These helpers belong to Viewer. Core's earlier `.view()`/`.widget()`
methods, `preview_geometry`, and `epsm-core view` are removed by the extraction.
Dated screenshots and validation records of those earlier APIs remain historical
evidence, not verification of the extracted renderer.

Show physical scale, axes and orientation. Identify the building, selected
geometry and model revision. Explain excluded geometry or incomplete surfaces.
A clipped, unloaded or missing part must not appear to be a verified complete
model. `repr()`, `str()` and ordinary object inspection must never start a
renderer, write preview files or launch a server.

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

For 3D, Core checks that exported scenes match its geometry and preserve identifiers, coordinates and units. Viewer checks triangulation, selection, display controls and resource cleanup. Studio checks its package adapters and user flow. Use real rendering for an advertised browser or notebook route; mocking the renderer does not establish that the preview works.

Avoid exact image comparisons across platforms for every plot. Use a few reviewed reference images when layout or geometry needs that check. Keep numerical/scientific reference tests separate from rendering tests.

Add a small `examples/` notebook showing the default plot, a labelled comparison and explicit export. Where 3D is useful, add a preview example with setup and cleanup instructions. Docstrings should show a short public call and explain the returned object.

## What needs to change first

The current Catalogue `BuildingArchetype.plot()` returns a Figure but displays by default. Core result charts currently live in demo helpers; `SimulationResult` has no public `.plot()` yet. Core's scene-data methods now separate physical geometry from Viewer display. The packages use separate material, chart and surface colours.

For 2D adoption, move reusable result drawing to its owner, preserve Catalogue's evidence-aware section drawing and make display choices explicit. Viewer owns browser palette adaptation; it does not move scientific calculations out of Core. Treat return-type or display changes as API changes with tests and migration notes.

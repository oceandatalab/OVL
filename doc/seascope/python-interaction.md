# Python interaction with SEAScope

The optional `seascope` Python package connects to a running instance of the
viewer over the network, so a Python session or a Jupyter notebook can
exchange data with it in both directions: pulling out what you extracted in
the viewer, and pushing your own data in.

<p align="center">
<a href="https://youtu.be/DwC9qHgfz4E?si=aem49yz8r5r9ZD-a"><img src="https://img.youtube.com/vi/DwC9qHgfz4E/mqdefault.jpg" alt="Video: Python interaction example" width="360"></a><br>
<a href="https://youtu.be/DwC9qHgfz4E?si=aem49yz8r5r9ZD-a">▶ Video: Python interaction example</a>
</p>

## Connecting to the viewer

Install the package with `pip install seascope`, then open a connection to
your running SEAScope instance — by default, on the same machine, at
`127.0.0.1:11155`:

```python
import SEAScope.upload

host = '127.0.0.1'
port = 11155

with SEAScope.upload.connect(host, port) as link:
    ...
```

`link` is only valid inside the `with` block; open a new one for each batch of
jobs you send to the viewer.

## Controlling the camera

Move and zoom the globe the same way the mouse does, with
`SEAScope.upload.location` and `SEAScope.upload.altitude` — call them
repeatedly with a short delay to animate a smooth transition:

```python
with SEAScope.upload.connect(host, port) as link:
    SEAScope.upload.location(link, lon, lat)
    SEAScope.upload.altitude(link, altitude)
    SEAScope.upload.zoom_in(link)
    SEAScope.upload.zoom_out(link)
    SEAScope.upload.reset_camera(link)
```

`zoom_in` and `zoom_out` step the altitude by the same amount as the
toolbar's [zoom buttons](features.md#camera-controls); `reset_camera` returns
to the initial location and altitude.

See the [camera notebook](../../notebooks/seascope/features/camera.ipynb) for
a full example.

## Controlling the timeline

Set the [current date and time](features.md#time-navigation) with
`SEAScope.upload.current_datetime`:

```python
import datetime

with SEAScope.upload.connect(host, port) as link:
    SEAScope.upload.current_datetime(link, datetime.datetime(2015, 12, 1))
```

See the [timeline notebook](../../notebooks/seascope/features/timeline.ipynb)
for a full example.

## Controlling rendering

Read a layer's current [rendering configuration](features.md#rendering-and-colormaps)
with `rendering_config_for`, then send back the changed values — colormap,
opacity, filter mode or colour — with `rendering_config`:

```python
target = {
    'granuleLevel': False,
    'sourceId': ...,      # hover over the layer's name in the catalogue for
    'collectionId': ...,  # these three values, given in a tooltip
    'granuleId': 0,
    'variableId': ...,
}

with SEAScope.upload.connect(host, port) as link:
    rcfg = SEAScope.upload.rendering_config_for(link, target)

rcfg['colormap'] = 'rainbow'
rcfg['opacity'] = 0.8

with SEAScope.upload.connect(host, port) as link:
    SEAScope.upload.rendering_config(link, rcfg)
```

See the
[rendering notebook](../../notebooks/seascope/features/rendering.ipynb) for a
full example.

## Retrieving data extracted in the viewer

Data extracted under a polygon or a polyline is fetched with
`SEAScope.lib.get_extracted_data()` — see
[Retrieving the extracted data in the notebook](features.md#retrieving-the-extracted-data-in-the-notebook)
for the full workflow, and the
[extraction notebook](../../notebooks/seascope/features/extraction.ipynb) for
a full example that also sends the modified data back to SEAScope.

## Sending your own data to SEAScope

`SEAScope.lib.utils` builds the objects the viewer expects — a collection, its
granules and variables — and `SEAScope.upload` sends them over the
connection:

```python
from SEAScope.lib.utils import create_collection, create_granule, create_variable, set_field
import SEAScope.upload

collection_id, collection = create_collection('My collection')

with SEAScope.upload.connect(host, port) as link:
    SEAScope.upload.collection(link, collection)

    granule_id, granule = create_granule(collection_id, gcps, start_dt, stop_dt)
    set_field(granule, 'my_field', values)
    SEAScope.upload.granule(link, granule)

    variable = create_variable(collection, 'my_field', ['my_field'], dims=1)
    variable['rendering']['min'] = 0
    variable['rendering']['max'] = 1
    variable['rendering']['colormap'] = 'jet'
    SEAScope.upload.variable(link, variable)
```

* `gcps` — the ground control points of the granule, as a list of
  `{'lon': ..., 'lat': ..., 'i': ..., 'j': ...}` dictionaries
* `start_dt` and `stop_dt` — the time coverage of the granule
* `variable['rendering']` — the same rendering options as in the
  [rendering panel](features.md#rendering-and-colormaps): min, max, colormap,
  colour, opacity and z-index

See the
[trajectory notebook](../../notebooks/seascope/features/trajectory.ipynb) for
a full example, built from scratch rather than from an extraction.

## Learn more

The full API is documented in the
[SEAScope Python bindings documentation](https://seascope.oceandatalab.com/python_api/index.html).

For science-driven, end-to-end examples, see the
[example notebooks](notebooks-example.md), in particular
[Converting data with the IDF converter](../../notebooks/seascope/learn_seascope_converter.ipynb)
and
[Exporting CFOSAT SWIM L2S to SEAScope](../../notebooks/seascope/use_cases/SWN24_CFOSAT_SWIM_L2S_to_SEAScope.ipynb)
for sending data, and
[Sentinel-2 swell](../../notebooks/seascope/use_cases/S2_Swell.ipynb) for retrieving it.

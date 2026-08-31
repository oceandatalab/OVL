# Add Data to SEAScope



## Add compatible samples to SEAScope

### Download samples
You can download data samples from the [SEAScope webpage](https://seascope.oceandatalab.com/data.html)


### Linux
* Download your samples (`*.tar.gz` archive)
* Uncompress the archive
* Copy the content (the folders and files in the sample data directory) into [workspace]/seascope/data

[How to add data to SEAScope on Linux](https://youtu.be/3ZAzgl3v2lo?si=Mlstme382XVkknAp)

### macOS
* Download your samples (`*.zip` archive)
* Drag-n-drop the zipped or unzipped folder onto the “SEAScope” icon
* Alternatively you can copy the content (the folders and files in the data directory) into ~/SEAScope-workspace/data directory

[How to add data to SEAScope on macOS](https://youtu.be/s5X3ewpmcuw?si=1s4V9qxMoJr8qKPV)

### Windows
* Download your samples (`*.zip` archive)
* Uncompress the archive
* Copy the content (the folders and files in the sample data directory) into [workspace]/seascope/data

[How to add data to SEAScope on Windows](https://youtu.be/TsJSg7V7WNU?si=5F5uN4TEA33it1Ui)

## Index

At startup SEAScope builds/updates an index that lists all the granules available in the `data` directory.
If SEAScope detects a change in the `data` directory, it will ask you whether or not the index should be updated. When prompted, agree to rebuild the index.

Alternatively, you can delete the `[workspace]/seascope/index.fb` file (or `~/SEAScope-workspace/index.fb` on macOS) when SEAScope is not running: the file will be regenerated automatically next time you start the application.

## Data format

SEAScope reads netCDF-4 files. What you have to do with your own data depends on
the geometry it is stored in.

### Data on a regular grid

Data on a regular latitude / longitude grid are read natively, provided the file
is netCDF-4 and compliant with the CF conventions, version 1.6 or above. Such a
file can be copied into the data directory as it is. An init file is needed (see exemple)

### Data in sensor geometry

Data in the geometry of the sensor — a swath, rather than a regular grid — have
to be converted into the Intermediate Data Format (IDF). An IDF file is a
netCDF-4 file in which the geolocation is stored as subsampled longitude and
latitude arrays with ground control points, which is what allows SEAScope to draw
the swath on the globe without reprojecting it first.

The full description of the format is given in the
[IDF specifications](https://seascope.oceandatalab.com/docs/idf_specifications_1.5.pdf).

### The IDF converter

The converter is published on PyPI as
[idf-converter](https://pypi.org/project/idf-converter), and is installed in the
Python environment you use with SEAScope:

```sh
pip install idf-converter
```

It is driven by a set of input and output options. The ones you will meet most
often are:

* `path` — the file to read, and the directory to write the granule to
* `collection` — the name of the collection the granule belongs to; the granule
  is then placed in the directory of that collection, under `data`
* `downscale` — produce multi-resolution files, which is worth doing for high
  resolution products
* `variables` — restrict the conversion to the variables you are interested in

Readers also take options specific to the product they handle, such as the
spacing between two ground control points, or the coefficient file needed to turn
brightness temperatures into sea surface temperature.

Worked examples for Sentinel-1, Sentinel-3 SLSTR L1 and SWOT L3 are given in the
[IDF converter notebook](../../notebooks/seascope/learn_seascope_converter.ipynb).

### Load data directly from Python

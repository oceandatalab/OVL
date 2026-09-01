# Jupyter python Notebooks Examples

These notebooks use the SEAScope viewer together with the SEAScope Python
bindings. They are stored with their outputs, so you can read them without
running anything — to execute them yourself you need SEAScope installed (see
[Download and install](download-install.md)) and the `seascope` Python package.

| Notebook | What it does |
| --- | --- |
| **[Converting data with the IDF converter](../../notebooks/seascope/learn_seascope_converter.ipynb)** | Converts your own data to IDF, the format SEAScope reads. |
| **[Exporting CFOSAT SWIM L2S to SEAScope](../../notebooks/seascope/use_cases/SWN24_CFOSAT_SWIM_L2S_to_SEAScope.ipynb)** | Exports a netCDF file to SEAScope. |
| **[Computing Sentinel-1 radial velocities](../../notebooks/seascope/use_cases/Compute_Sentinel-1_radial_velocities.ipynb)** | Retrieves Sentinel-1 data from the viewer and computes radial velocities. |
| **[Sentinel-2 swell](../../notebooks/seascope/use_cases/S2_Swell.ipynb)** | Analyses swell from Sentinel-2 imagery. |
| **[Swell refraction](../../notebooks/seascope/use_cases/SWELL_refrac.ipynb)** | Studies swell refraction from data pulled out of the viewer. |

For minimal, single-feature examples of the Python API itself — controlling
the camera, the timeline or the rendering, and exchanging data — see the
notebooks in [Python interaction with SEAScope](python-interaction.md).

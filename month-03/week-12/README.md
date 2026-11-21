# Week 12: Rasters with Rasterio

## Overview

In Week 12, I learned how to use Rasterio, NumPy, GeoPandas and Matplotlib to work with raster data in Python.

I inspected raster properties, read elevation values, converted pixel positions into map coordinates, sampled elevation at facility locations, calculated NDVI, clipped a raster, performed zonal statistics and reprojected a DEM.

For my independent challenge, I applied these skills to my Lagos Mainland study area in Lagos State, Nigeria.

## Guided practical

I completed the nine guided scripts:

- `inspect_raster.py` — inspected raster metadata.
- `read_values.py` — calculated elevation statistics while handling nodata.
- `pixel_coords.py` — converted between pixels and map coordinates.
- `sample_points.py` — sampled elevation at facility points.
- `ndvi.py` — calculated NDVI from Landsat bands.
- `plot_raster.py` — created the teaching NDVI map.
- `clip_raster.py` — clipped the DEM using ward boundaries.
- `zonal_stats.py` — calculated mean elevation for each ward.
- `reproject_raster.py` — reprojected the DEM to EPSG:4326.

The guided exercises used the Ibadan North teaching datasets.

## Independent challenge: Lagos Mainland

I used Landsat 8 Collection 2 Level-2 imagery downloaded from USGS EarthExplorer.

**Satellite scene:** `LC08_L2SP_191055_20250117_20250128_02_T1`

**Acquisition date:** 17 January 2025

**Scene cloud cover:** 6.21%

**Land cloud cover:** 6.09%

**Study area:** Lagos Mainland, Lagos State, Nigeria

**Coordinate reference system:** EPSG:32631

**Index calculated:** Normalised Difference Vegetation Index (NDVI)

### My results

| Measurement | Result |
|---|---:|
| Valid NDVI pixels | 7,890 |
| Minimum NDVI | -0.102 |
| Maximum NDVI | 0.971 |
| Mean NDVI | 0.149 |

The average NDVI of 0.149 indicates a relatively low positive vegetation signal among the valid pixels, consistent with a mixture of vegetated and non-vegetated surfaces.

I calculated zonal statistics for my Lagos Mainland study-area polygon and saved the results in `my_zonal_stats.csv`.

### Challenge files

- `my_inspect.py` — checked raster metadata and geographic coverage.
- `my_index.py` — calculated Lagos Mainland NDVI with quality masking.
- `my_zonal.py` — calculated mean NDVI within the study-area polygon.
- `my_map.py` — generated the final Lagos Mainland NDVI map.
- `my_zonal_stats.csv` — saved the zonal statistics.
- `my_map.png` — final NDVI map.

## Limitations

The satellite scene's overall cloud-cover percentage does not guarantee that every pixel in Lagos Mainland is usable.

My analysis excluded pixels flagged as unsuitable or failing reflectance checks. Only 7,890 pixels contributed to the NDVI statistics, so the mean should not be interpreted as a complete measurement of vegetation across the entire study area.

I also used a single Lagos Mainland study-area polygon, so the zonal statistics describe the overall area rather than individual wards.

## Data and repository

The raster GeoTIFF files are stored locally and excluded from GitHub. Their sources and filenames are documented in the repository's `data-notes.md`.

The Python scripts, PNG maps and CSV results are included in the Week 12 folder.

## What I learned

This week helped me understand that raster data is a grid of numerical values linked to geographic locations. I learned how to read raster metadata, handle missing pixels, use satellite bands to calculate NDVI and combine raster measurements with vector boundaries.

I can now use Python to extract and summarise information from satellite imagery for a real GIS project.
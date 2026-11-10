# Week 11: Coordinate reference systems and spatial operations

## What this folder contains

This week I used GeoPandas and PyProj to work with coordinate reference systems and perform spatial operations in Python.

The guided scripts cover geographic and projected CRSs, the difference between `to_crs()` and `set_crs()`, coordinate transformation, buffering, spatial joins, facility counts, coverage gaps, nearest-distance analysis, clipping, dissolving, and geometry validation and repair.

For my independent challenge, I used my Lagos Mainland education data from Month 1.

## CRS used

I used **EPSG:32631 — WGS 84 / UTM zone 31N** for my Lagos Mainland analysis.

Both my Lagos Mainland boundary and education point layer were already in EPSG:32631, and GeoPandas also suggested EPSG:32631 as the appropriate UTM CRS.

Using a projected CRS allowed me to measure area and buffer distance in metres and kilometres.

## My own-data results

My Lagos Mainland study boundary covers approximately **23.49 km²**.

My education dataset contains **31 mapped education points**.

A spatial join confirmed that all **31 of 31 education points** were inside the Lagos Mainland study boundary.

I then created a **1 km straight-line buffer** around each mapped education point and dissolved the overlapping buffers into one coverage area.

The analysis found:

- Total study area: 23.49 km²
- Area within 1 km of a mapped education point: 18.83 km²
- Covered percentage: 80.16%
- Area outside the 1 km reach: 4.66 km²
- Uncovered percentage: 19.84%

The result was saved as a GeoPackage in `data/processed/`, and the map was saved as `my_reach_map.png`.

## Geometry validity

I checked the Lagos Mainland boundary for invalid geometry.

The boundary contained **0 invalid geometries before repair and 0 after repair**, so no geometry repair was required.

The boundary geometry is a MultiPolygon.

## Limitation

The 1 km coverage represents **straight-line distance**, not actual walking or driving distance along the road network.

It also depends on the 31 mapped education records in my dataset, so it should not be interpreted as a complete inventory of every education facility in Lagos Mainland.

## How to run

Run the scripts from the repository root using `uv run`.

For example:

```text
uv run month-03/week-11/my_crs.py
uv run month-03/week-11/my_count.py
uv run month-03/week-11/my_reach.py
uv run month-03/week-11/my_validity.py
```
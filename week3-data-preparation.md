# Week 3 — Data Preparation and Quality Checks

## Project

Mapping education facilities recorded in OpenStreetMap within Lagos Mainland LGA, Lagos State.

## Working coordinate system

I used **EPSG:32631 — WGS 84 / UTM Zone 31N**.

This projected coordinate system is appropriate for Lagos and uses metres, making it suitable for measuring distances and areas. The original datasets were in EPSG:4326 and were reprojected rather than simply assigned a new CRS.

## Data preparation

The following work was completed in QGIS:

1. The Lagos Mainland boundary was selected from the Nigeria LGA boundary dataset.
2. Education points were extracted to Lagos Mainland.
3. Education polygons were clipped to the Lagos Mainland boundary.
4. The boundary, point and clipped polygon layers were reprojected to EPSG:32631.
5. The prepared layers were saved in one analysis-ready GeoPackage.

## Data sources

* Education facilities: [HOT OpenStreetMap education facilities for Nigeria](https://data.humdata.org/dataset/hotosm_nga_education_facilities)
* Administrative boundaries: [Nigeria administrative boundaries](https://data.humdata.org/dataset/cod-ab-nga)

## Prepared layers

* `boundary_utm31n` — 1 Lagos Mainland boundary feature
* `education_points_utm31n` — 16 point features
* `education_polygons_utm31n` — 15 polygon features

## Five quality checks

### 1. CRS check

All three prepared layers and the QGIS project use EPSG:32631. The layers display in the correct location and use metres as their measurement unit.

**Decision:** Passed. No CRS problem was found.

### 2. Geometry validity

QGIS Check Validity was run on the point and polygon layers.

* Points: 16 valid, 0 invalid and 0 errors
* Polygons: 15 valid, 0 invalid and 0 errors

**Decision:** Passed. No geometry repair was required.

### 3. Duplicate geometries

The duplicate geometry check returned 16 points and 15 polygons, which are the same as the original prepared feature counts.

**Decision:** No exact duplicate geometries were found.

### 4. Missing attribute values

Two of the 16 point features have no value in the `name` field. Six of the 15 polygon features also have no name.

Many records have NULL values in fields such as `capacity_persons`, `addr_full`, `addr_city`, `source`, `name_en` and `name_yo`.

**Decision:** The missing values were flagged but not filled because no reliable source was available for the missing information.

### 5. Extent and coverage

The prepared features are within the Lagos Mainland boundary. Polygon portions outside the study area were removed through clipping.

The mapped education facilities are unevenly distributed. Several parts of Lagos Mainland have few or no recorded facilities. This may represent gaps in OpenStreetMap coverage and does not prove that those areas have no schools.

**Decision:** The dataset is suitable for mapping facilities recorded in OpenStreetMap, but it should not be treated as a complete official list of every school.

## Problems found and decisions

* Polygon features extending outside Lagos Mainland were clipped to the boundary.
* Some source records still contain administrative labels such as Mushin because clipping changes geometry but does not rewrite attribute values. This was flagged.
* Missing names and other NULL attributes were flagged rather than replaced with guessed information.
* No invalid or exact duplicate geometries were found.

## Analysis-ready output

The analysis-ready data is stored in:

`lagos_mainland_analysis_ready.gpkg`

It contains:

* `boundary_utm31n`
* `education_points_utm31n`
* `education_polygons_utm31n`

The QGIS project is saved as:

`lagos-mainland-schools.qgz`

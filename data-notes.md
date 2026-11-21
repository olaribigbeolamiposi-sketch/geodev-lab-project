# Week 2 Data Notes

## Project
Mapping schools recorded in OpenStreetMap within Lagos Mainland LGA, Lagos State, Nigeria.

## Data Sources

- Education facilities: OpenStreetMap contributors, distributed by HOT through HDX.
  https://data.humdata.org/dataset/hotosm_nga_education_facilities

- Administrative boundaries: Nigeria Subnational Administrative Boundaries on HDX.
  https://data.humdata.org/dataset/cod-ab-nga

## Original Datasets

### Nigeria Education Facilities
- File: education_facilities.gpkg
- Features: 6,229 education records, displayed in QGIS as 3,206 points and 3,023 multipolygons.
- Key columns: id, name, amenity, building, operator_type, capacity_persons, adm1_name, adm2_name, adm2_pcode.
- Includes schools, colleges, universities, and individual education-related buildings.
- Missing names, addresses, capacities, and operator details occur in the data.

### Nigeria LGA Boundaries
- File: nga_admin2.geojson
- Features: 774.
- Geometry: MultiPolygon.
- Key columns: adm2_name, adm2_pcode, adm1_name, area_sqkm, valid_on.
- Optional alternative-name fields contain NULL values.
- The Lagos Mainland record was selected using adm2_name and exported separately.

## Lagos Mainland Outputs

### Boundary
- File: lagos_mainland_boundary.gpkg
- Source: Nigeria administrative boundaries linked above.
- Features: 1.
- Geometry: MultiPolygon.
- Key columns: adm2_name, adm2_pcode, adm1_name, area_sqkm.
- LGA name: Lagos Mainland.
- LGA code: NG025015.

### Education Points
- File: lagos_mainland_education_points.gpkg
- Source: OSM education facilities linked above.
- Features: 16.
- Geometry: Point.
- Key columns: id, name, amenity, operator_type, capacity_persons, adm2_name.
- Amenity values: 14 school, 1 kindergarten, and 1 college.
- Two records have missing names.
- Operator type, capacity, full address, and city are missing for all 16 records.
- All 16 records have Lagos Mainland in the LGA-name field.

### Education Polygons
- File: lagos_mainland_education_polygons.gpkg
- Source: OSM education facilities linked above.
- Features: 15.
- Geometry: MultiPolygon.
- Key columns: id, name, amenity, building, operator_type, adm2_name.
- Amenity values: 10 school, 1 college, 2 university, and 2 NULL.
- Six records have missing names.
- Twelve records are labelled Lagos Mainland; three are labelled Mushin.

## Method

The datasets were opened and their attribute tables inspected in QGIS.

The Lagos Mainland boundary was exported from the national LGA layer. Extract by Location, using the intersect predicate, was then applied separately to the education points and polygons.

Intersect includes features inside, overlapping, or touching the boundary. Polygon geometries were retained whole rather than clipped.

All three local outputs use EPSG:4326 (WGS 84).

## Limitations and Observations

- The local outputs contain 31 education features, not necessarily 31 unique schools.
- Some school-tagged records appear to represent university departments or facilities and need review.
- Point and polygon records may represent the same institution; duplicates have not yet been checked.
- Three intersecting polygons carry a Mushin label. The reason for this boundary/attribute mismatch has not yet been established.
- The earlier Week 1 count of 35 used the stored Lagos Mainland label. The Week 2 count of 31 uses spatial intersection, so the selection methods differ.
- Missing mapped schools cannot be interpreted as proof that no schools exist there. Coverage has not been independently verified.
- NULL means missing information, not zero.
- A NULL value in the source column does not remove the dataset's known provenance from OSM via HDX.

## Current Status

The data has been downloaded, opened in QGIS, inspected, and extracted for the study area. The QGIS project has been saved as lagos-mainland-schools.qgz.

School classification, duplicate checks, and coverage verification remain future work.



## Week 12: Raster data sources

### Guided practical: Ibadan North

The guided exercises used teaching raster datasets.

Files:
- data/raw/dem.tif
- data/raw/landsat/*_SR_B4.TIF
- data/raw/landsat/*_SR_B5.TIF

The DEM was used for elevation inspection, sampling,
clipping, zonal statistics and reprojection.

The Landsat bands were used to calculate NDVI.

The teaching DEM has a resolution of 30 metres and
uses EPSG:32631.

### Independent challenge: Lagos Mainland

Study area: Lagos Mainland, Lagos State, Nigeria.

Source: USGS EarthExplorer
https://earthexplorer.usgs.gov/

Satellite: Landsat 8
Dataset: Collection 2 Level-2

Scene:
LC08_L2SP_191055_20250117_20250128_02_T1

Acquisition date: 17 January 2025
Scene cloud cover: 6.21%
Land cloud cover: 6.09%

Local folder:
data/raw/landsat/lagos_mainland/

Downloaded files:
- LC08_L2SP_191055_20250117_20250128_02_T1_SR_B4.TIF
- LC08_L2SP_191055_20250117_20250128_02_T1_SR_B5.TIF
- LC08_L2SP_191055_20250117_20250128_02_T1_QA_PIXEL.TIF

Band 4 contains red reflectance.
Band 5 contains near-infrared reflectance.
QA_PIXEL identifies pixel quality conditions.

All three rasters use EPSG:32631 and have
30-metre pixel resolution.

### Locally generated raster outputs

- data/processed/ndvi.tif
  Teaching NDVI raster.

- data/processed/dem_ibadan_north.tif
  DEM clipped to the teaching study area.

- data/processed/dem_wgs84.tif
  Teaching DEM reprojected to EPSG:4326.

- data/processed/lagos_mainland_ndvi.tif
  Lagos Mainland NDVI raster.

### Lagos Mainland NDVI results

Valid pixels: 7,890
Minimum NDVI: -0.102
Maximum NDVI: 0.971
Mean NDVI: 0.149

NDVI was calculated using scaled surface reflectance,
with unsuitable pixels excluded using quality flags
and validity checks.

The zonal statistics were calculated for the
Lagos Mainland study-area polygon.

### Limitations

Only valid pixels contributed to the NDVI statistics.
Areas without valid NDVI measurements were excluded.

The scene cloud-cover percentage describes the overall
scene, not necessarily the exact Lagos Mainland area.

NDVI measures vegetation-related reflectance. It is
not a direct percentage of vegetation coverage.

The analysis uses one satellite acquisition date.

### Repository storage

Raster GeoTIFF files remain on my laptop and are
excluded from GitHub.

The repository contains Python scripts, PNG maps,
CSV results, README files and this data documentation.


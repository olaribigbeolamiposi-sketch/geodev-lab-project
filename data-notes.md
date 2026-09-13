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

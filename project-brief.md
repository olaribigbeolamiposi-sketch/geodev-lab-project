# Project Brief: Mapping Schools in Lagos Mainland LGA

## 1. Spatial Question and Study Area

Question: Where are the schools recorded in OpenStreetMap located within Lagos Mainland Local Government Area?

Study area: Lagos Mainland LGA, Lagos State, Nigeria.

## 2. Why It Matters

This project will help users locate mapped schools and understand their distribution within Lagos Mainland LGA. It will provide a simple way to explore available school locations.

The map will represent OpenStreetMap records, which may not include every school in the area.

## 3. Datasets Needed

- Education facilities: education_facilities.gpkg, in GeoPackage format, approximately 2 MB extracted. School records will be selected from this dataset.
- LGA boundaries: nga_admin2.geojson, in GeoJSON format, approximately 5.85 MB extracted. The Lagos Mainland boundary will be selected from this dataset.

## 4. Data Sources and Checks

- Education facilities — OpenStreetMap contributors, distributed by the Humanitarian OpenStreetMap Team through HDX:
  https://data.humdata.org/dataset/hotosm_nga_education_facilities

- LGA boundaries — Nigeria Subnational Administrative Boundaries on HDX:
  https://data.humdata.org/dataset/cod-ab-nga

Both datasets have been downloaded and opened successfully.

The boundary dataset includes Lagos Mainland LGA, with the code NG025015. The education dataset contains 35 records labelled Lagos Mainland, including 28 tagged as schools.

These are preliminary record counts, not a verified total of schools. Some records have missing names or unusual classifications. Their locations and classifications will be reviewed during analysis.

## 5. What I Will Build

I will build an interactive map showing school records within Lagos Mainland LGA. Users will be able to click on a school to view its name and other available details.

The project will include instructions explaining how to repeat the mapping process when updated data becomes available.

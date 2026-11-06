# Week 10: GeoPandas, layers as tables

## What this folder contains

This week I used pandas and GeoPandas to load, inspect, filter, join, map and save tabular and spatial data in Python.

The guided practical includes scripts for exploring tables and vector layers, filtering and sorting population data, converting coordinate data to points, joining population data to wards, creating a map and saving new outputs.

For my independent challenge, I used my Month 1 Lagos Mainland education data. I inspected the education point layer, rebuilt the education points from a CSV using X and Y coordinates, joined the CSV back to the spatial layer using the shared `id` field, and created a map of the education facilities within Lagos Mainland.

## How to run

Run the scripts from the repository root using `uv run`.

Examples:

```text
uv run month-03/week-10/explore_pandas.py
uv run month-03/week-10/explore_layer.py
uv run month-03/week-10/my_explore.py
uv run month-03/week-10/my_points.py
uv run month-03/week-10/my_join.py
uv run month-03/week-10/my_map.py
```

## What I found

My Lagos Mainland education layer contains 31 point records and uses EPSG:32631, WGS 84 / UTM zone 31N.

The CSV coordinates produced the same 31 education points when converted back into a GeoDataFrame using the correct CRS.

The join between my Month 1 education layer and the coordinate table matched 31 of 31 records on the shared `id` field.

The map shows that the education records are unevenly distributed across Lagos Mainland, with visible clusters and areas containing fewer mapped records.

## What went wrong or what I fixed

The teaching join initially matched only 9 of 12 ward records because capitalization, spaces and hyphens differed between the two tables. Cleaning the names in code allowed all 12 records to match.

For my own data, all 31 records matched on the first join because both datasets came from the same prepared Month 1 data and shared the same `id` values. I checked the match count rather than assuming the join was complete.

I also made sure that my X and Y coordinates were assigned EPSG:32631 rather than EPSG:4326 because they are UTM coordinates measured in metres, not longitude and latitude.
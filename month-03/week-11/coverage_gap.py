import geopandas as gpd

wards = gpd.read_file(
    "data/processed/wards.gpkg",
    layer="wards"
).to_crs(epsg=32631)

facilities = gpd.read_file(
    "data/processed/facilities.gpkg",
    layer="facilities"
).to_crs(epsg=32631)

# Make 2 km buffers around all facilities
reach = facilities[["geometry"]].copy()
reach["geometry"] = reach.buffer(2000)

# Merge all overlapping buffers into one coverage shape
reach = reach.dissolve()

# Subtract the covered area from each ward
uncovered = gpd.overlay(
    wards,
    reach,
    how="difference"
)

# Area outside the 2 km reach
uncovered["uncovered_km2"] = (
    uncovered.area / 1_000_000
)

# Keep the ward name and uncovered area
gaps = uncovered[
    ["ward_name", "uncovered_km2"]
].copy()

# Merge the results back onto all wards
result = wards.merge(
    gaps,
    on="ward_name",
    how="left"
)

# Fully covered wards disappeared from the difference result,
# so their uncovered area should be zero
result["uncovered_km2"] = (
    result["uncovered_km2"]
    .fillna(0)
)

# Calculate each ward's total area
result["area_km2"] = (
    result.area / 1_000_000
)

# Calculate percentage of each ward not covered
result["uncovered_pct"] = (
    result["uncovered_km2"]
    / result["area_km2"]
    * 100
)

print(
    result[
        [
            "ward_name",
            "area_km2",
            "uncovered_km2",
            "uncovered_pct"
        ]
    ].round(2)
)
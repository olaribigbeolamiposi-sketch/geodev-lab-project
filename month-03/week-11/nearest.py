import geopandas as gpd

wards = gpd.read_file(
    "data/processed/wards.gpkg",
    layer="wards"
).to_crs(epsg=32631)

facilities = gpd.read_file(
    "data/processed/facilities.gpkg",
    layer="facilities"
).to_crs(epsg=32631)

# Use each ward centroid as a simple stand-in for the ward centre
centres = wards[
    ["ward_name", "geometry"]
].copy()

centres["geometry"] = wards.centroid

# Find the nearest facility to each ward centre
nearest = gpd.sjoin_nearest(
    centres,
    facilities[["name", "geometry"]],
    how="left",
    distance_col="distance"
)

# Convert metres to kilometres
nearest["distance_km"] = (
    nearest["distance"] / 1000
)

print(
    nearest[
        ["ward_name", "name", "distance_km"]
    ].round(2)
)
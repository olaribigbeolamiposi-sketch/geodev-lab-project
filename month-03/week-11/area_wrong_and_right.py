import geopandas as gpd

wards = gpd.read_file(
    "data/processed/wards.gpkg",
    layer="wards"
)

print("CRS:", wards.crs)

# Wrong: area while still in geographic coordinates
wards["area_wrong"] = wards.area
print("\nArea while still in EPSG:4326:")
print(
    wards[
        ["ward_name", "area_wrong"]
    ].head()
)

print("\nSuggested UTM:", wards.estimate_utm_crs())

# Correct: reproject first
wards_utm = wards.to_crs(epsg=32631)

print("\nProjected CRS:", wards_utm.crs)

wards_utm["area_km2"] = (
    wards_utm.area / 1_000_000
)

print("\nCorrect area in square kilometres:")
print(
    wards_utm[
        ["ward_name", "area_km2"]
    ].head()
)

print(
    "\nIbadan North total:",
    round(wards_utm["area_km2"].sum(), 1),
    "km2"
)
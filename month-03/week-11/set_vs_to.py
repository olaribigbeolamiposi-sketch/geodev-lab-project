import geopandas as gpd

wards = gpd.read_file(
    "data/processed/wards.gpkg",
    layer="wards"
)

first = wards.geometry.iloc[0].exterior.coords[0]

print("Original first corner:", first)
print("Original CRS:", wards.crs)

# Correct: actually reproject the coordinates
projected = wards.to_crs(epsg=32631)

projected_first = projected.geometry.iloc[0].exterior.coords[0]

print("\nAfter to_crs:", projected_first)
print("After to_crs CRS:", projected.crs)

# Wrong: only changes the CRS label
wrongly_labelled = wards.set_crs(
    epsg=32631,
    allow_override=True
)

wrong_first = wrongly_labelled.geometry.iloc[0].exterior.coords[0]

print("\nAfter set_crs:", wrong_first)
print("Label now says:", wrongly_labelled.crs)
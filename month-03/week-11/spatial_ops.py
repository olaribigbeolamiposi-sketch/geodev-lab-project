import geopandas as gpd

wards = gpd.read_file(
    "data/processed/wards.gpkg",
    layer="wards"
).to_crs(epsg=32631)

facilities = gpd.read_file(
    "data/processed/facilities.gpkg",
    layer="facilities"
).to_crs(epsg=32631)

# Create a 2 km buffer around every facility
reach = facilities.copy()
reach["geometry"] = facilities.buffer(2000)

print("Buffered", len(reach), "facilities")

# Spatially join each facility to the ward it falls inside
joined = gpd.sjoin(
    facilities,
    wards[["ward_name", "geometry"]],
    how="inner",
    predicate="within"
)

# Count facilities in each ward
counts = (
    joined.groupby("ward_name")
    .size()
    .rename("facility_count")
    .reset_index()
)

# Put the counts back onto every ward
wards = wards.merge(
    counts,
    on="ward_name",
    how="left"
)

# Wards with no facilities should have 0, not NaN
wards["facility_count"] = (
    wards["facility_count"]
    .fillna(0)
    .astype(int)
)

print(wards[["ward_name", "facility_count"]])

print(
    "Total counted:",
    wards["facility_count"].sum(),
    "of",
    len(facilities)
)
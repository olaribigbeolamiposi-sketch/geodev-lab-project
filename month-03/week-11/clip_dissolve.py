import geopandas as gpd

wards = gpd.read_file(
    "data/processed/wards.gpkg",
    layer="wards"
).to_crs(epsg=32631)

roads = gpd.read_file(
    "data/processed/roads.gpkg",
    layer="roads"
).to_crs(epsg=32631)

# Select Agodi ward
agodi = wards[
    wards["ward_name"] == "Agodi"
]

# Clip roads to Agodi
agodi_roads = gpd.clip(
    roads,
    agodi
)

print("Roads in Agodi:", len(agodi_roads))

road_length_km = (
    agodi_roads.length.sum() / 1000
)

print(
    "Road length in Agodi:",
    round(road_length_km, 2),
    "km"
)

# Dissolve all wards into one LGA boundary
lga = wards.dissolve(
    by="lga_name"
)

print(lga[["geometry"]])
print(
    "LGA area:",
    round(lga.area.iloc[0] / 1_000_000, 1),
    "km2"
)
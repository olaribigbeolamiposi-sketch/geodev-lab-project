import geopandas as gpd

boundary = gpd.read_file(
    "lagos_mainland_analysis_ready.gpkg",
    layer="boundary_utm31n"
).to_crs(epsg=32631)

education = gpd.read_file(
    "education_all_points_utm31n.gpkg"
).to_crs(epsg=32631)

# Give the study-area polygon a simple key for grouping
boundary = boundary.copy()
boundary["area_name"] = "Lagos Mainland"

# Spatially join each education point to the boundary
joined = gpd.sjoin(
    education,
    boundary[["area_name", "geometry"]],
    how="inner",
    predicate="within"
)

# Count education points in each polygon
counts = (
    joined.groupby("area_name")
    .size()
    .rename("education_count")
    .reset_index()
)

# Merge the count back to the complete polygon layer
result = boundary.merge(
    counts,
    on="area_name",
    how="left"
)

# Any polygon with no points should show 0 rather than NaN
result["education_count"] = (
    result["education_count"]
    .fillna(0)
    .astype(int)
)

print(
    result[
        ["area_name", "education_count"]
    ]
)

print(
    "Total counted:",
    result["education_count"].sum(),
    "of",
    len(education)
)

# Save a small Week 11 result layer
result.to_file(
    "data/processed/week11_education_count.gpkg",
    layer="education_count",
    driver="GPKG"
)

print("Saved data/processed/week11_education_count.gpkg")
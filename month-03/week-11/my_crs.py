import geopandas as gpd

boundary = gpd.read_file(
    "lagos_mainland_analysis_ready.gpkg",
    layer="boundary_utm31n"
)

education = gpd.read_file(
    "education_all_points_utm31n.gpkg"
)

print("Boundary CRS:", boundary.crs)
print("Education CRS:", education.crs)

print(
    "Suggested UTM for boundary:",
    boundary.estimate_utm_crs()
)

print(
    "Suggested UTM for education:",
    education.estimate_utm_crs()
)

# Make sure both layers use the correct projected CRS
boundary_utm = boundary.to_crs(epsg=32631)
education_utm = education.to_crs(epsg=32631)

print("\nBoundary projected CRS:", boundary_utm.crs)
print("Education projected CRS:", education_utm.crs)

# Measure Lagos Mainland boundary area
boundary_utm["area_km2"] = (
    boundary_utm.area / 1_000_000
)

print(
    "\nLagos Mainland area:",
    round(boundary_utm["area_km2"].sum(), 2),
    "km2"
)

print(
    "Education points:",
    len(education_utm)
)
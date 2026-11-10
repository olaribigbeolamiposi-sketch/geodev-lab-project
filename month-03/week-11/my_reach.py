import geopandas as gpd
import matplotlib.pyplot as plt

boundary = gpd.read_file(
    "lagos_mainland_analysis_ready.gpkg",
    layer="boundary_utm31n"
).to_crs(epsg=32631)

education = gpd.read_file(
    "education_all_points_utm31n.gpkg"
).to_crs(epsg=32631)

boundary = boundary.copy()
boundary["area_name"] = "Lagos Mainland"

# Create 1 km straight-line buffers around education points
reach = education[["geometry"]].copy()
reach["geometry"] = reach.buffer(1000)

# Merge overlapping buffers into one coverage area
reach = reach.dissolve()

# Keep only the coverage inside Lagos Mainland
covered = gpd.overlay(
    boundary[["area_name", "geometry"]],
    reach,
    how="intersection"
)

# Find the parts of Lagos Mainland outside the 1 km coverage
uncovered = gpd.overlay(
    boundary[["area_name", "geometry"]],
    reach,
    how="difference"
)

# Calculate areas in square kilometres
total_area_km2 = boundary.area.sum() / 1_000_000
covered_area_km2 = covered.area.sum() / 1_000_000
uncovered_area_km2 = uncovered.area.sum() / 1_000_000

covered_pct = (
    covered_area_km2 / total_area_km2 * 100
)

uncovered_pct = (
    uncovered_area_km2 / total_area_km2 * 100
)

print("Education points:", len(education))
print("Total area:", round(total_area_km2, 2), "km2")
print("Covered within 1 km:", round(covered_area_km2, 2), "km2")
print("Covered percentage:", round(covered_pct, 2), "%")
print("Outside 1 km reach:", round(uncovered_area_km2, 2), "km2")
print("Uncovered percentage:", round(uncovered_pct, 2), "%")

# Save the uncovered result
uncovered.to_file(
    "data/processed/week11_education_reach.gpkg",
    layer="uncovered_1km",
    driver="GPKG"
)

# Make a map of the result
fig, ax = plt.subplots(figsize=(7, 8))

boundary.plot(
    ax=ax,
    facecolor="none",
    edgecolor="black",
    linewidth=1.5
)

covered.plot(
    ax=ax,
    alpha=0.4
)

education.plot(
    ax=ax,
    markersize=20
)

ax.set_title(
    "1 km straight-line reach of mapped education points\nLagos Mainland"
)
ax.set_axis_off()

fig.savefig(
    "month-03/week-11/my_reach_map.png",
    dpi=150,
    bbox_inches="tight"
)

plt.close(fig)

print("Saved data/processed/week11_education_reach.gpkg")
print("Saved month-03/week-11/my_reach_map.png")
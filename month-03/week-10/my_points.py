import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

table = pd.read_csv("data/raw/education_points.csv")

education_points = gpd.GeoDataFrame(
    table,
    geometry=gpd.points_from_xy(
        table["X"],
        table["Y"]
    ),
    crs="EPSG:32631"
)

print(education_points.head())
print("Rows:", len(education_points))
print("CRS:", education_points.crs)
print("Bounds:", education_points.total_bounds)

education_points.to_file(
    "data/processed/my_education_points.gpkg",
    layer="education_points",
    driver="GPKG"
)

boundary = gpd.read_file(
    "lagos_mainland_analysis_ready.gpkg",
    layer="boundary_utm31n"
)

fig, ax = plt.subplots(figsize=(7, 8))

boundary.plot(
    ax=ax,
    facecolor="none",
    edgecolor="black"
)

education_points.plot(
    ax=ax,
    markersize=20
)

ax.set_title("Education points in Lagos Mainland")
ax.set_axis_off()

plt.close(fig)

print("Saved", len(education_points), "education points")
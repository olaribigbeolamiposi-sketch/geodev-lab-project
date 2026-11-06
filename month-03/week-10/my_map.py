import geopandas as gpd
import matplotlib.pyplot as plt

boundary = gpd.read_file(
    "lagos_mainland_analysis_ready.gpkg",
    layer="boundary_utm31n"
)

education = gpd.read_file(
    "education_all_points_utm31n.gpkg"
)

fig, ax = plt.subplots(figsize=(7, 8))

boundary.plot(
    ax=ax,
    facecolor="none",
    edgecolor="black",
    linewidth=1.5
)

education.plot(
    ax=ax,
    markersize=25
)

ax.set_title("Education facilities in Lagos Mainland")
ax.set_axis_off()

fig.savefig(
    "month-03/week-10/my_map.png",
    dpi=150,
    bbox_inches="tight"
)

print("Saved my_map.png")
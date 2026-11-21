
import geopandas as gpd
import matplotlib.pyplot as plt
import rasterio
from rasterio.plot import plotting_extent

# 1. Load Lagos Mainland boundary
boundary = gpd.read_file(
    "lagos_mainland_analysis_ready.gpkg",
    layer="boundary_utm31n"
)

# 2. Open your Lagos Mainland NDVI raster
with rasterio.open(
    "data/processed/lagos_mainland_ndvi.tif"
) as src:

    # Read the NDVI and exclude nodata pixels
    ndvi = src.read(1, masked=True)

    # Get the correct geographic extent
    extent = plotting_extent(src)

    # Match the boundary CRS to the raster CRS
    boundary = boundary.to_crs(src.crs)

# 3. Create the map
fig, ax = plt.subplots(figsize=(9, 8))

# 4. Display the NDVI raster
image = ax.imshow(
    ndvi,
    cmap="RdYlGn",
    vmin=-0.2,
    vmax=1.0,
    extent=extent,
    origin="upper"
)

# 5. Draw Lagos Mainland boundary
boundary.boundary.plot(
    ax=ax,
    edgecolor="black",
    linewidth=1.5
)

# 6. Add a colour bar
colorbar = fig.colorbar(
    image,
    ax=ax,
    shrink=0.75,
    pad=0.03
)

colorbar.set_label("NDVI")

# 7. Add title and axis labels
ax.set_title(
    "Lagos Mainland Vegetation Index (NDVI)\n"
    "Landsat 8 | 17 January 2025",
    fontsize=13,
    fontweight="bold"
)

ax.set_xlabel("Easting (metres)")
ax.set_ylabel("Northing (metres)")

# 8. Keep map proportions correct
ax.set_aspect("equal")

# 9. Add a source note
fig.text(
    0.5,
    0.02,
    "Source: USGS Landsat 8 Collection 2 Level-2 | "
    "CRS: EPSG:32631",
    ha="center",
    fontsize=9
)

# 10. Save the finished map
output = "month-03/week-12/my_map.png"

fig.savefig(
    output,
    dpi=200,
    bbox_inches="tight"
)

plt.close(fig)

print("Saved:", output)
print("Lagos Mainland NDVI map completed!")

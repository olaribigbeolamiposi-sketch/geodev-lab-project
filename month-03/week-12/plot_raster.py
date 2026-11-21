
import matplotlib.pyplot as plt
import rasterio

# Open the NDVI raster
with rasterio.open("data/processed/ndvi.tif") as src:
    ndvi = src.read(1, masked=True)

# Create the map canvas
fig, ax = plt.subplots(figsize=(7, 8))

# Display NDVI using a colour map
image = ax.imshow(
    ndvi,
    cmap="RdYlGn",
    vmin=-0.2,
    vmax=0.9
)

# Add a colour bar
fig.colorbar(
    image,
    ax=ax,
    label="NDVI"
)

# Add a map title
ax.set_title(
    "Vegetation Index, Ibadan North"
)

# Remove unnecessary axes
ax.set_axis_off()

# Save the map as PNG
fig.savefig(
    "month-03/week-12/ndvi_map.png",
    dpi=150,
    bbox_inches="tight"
)

plt.close(fig)

print("Saved month-03/week-12/ndvi_map.png")

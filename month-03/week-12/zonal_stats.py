
import geopandas as gpd
import rasterio
from rasterio.mask import mask

# Open the teaching elevation raster
with rasterio.open("data/raw/dem.tif") as src:

    # Load wards and match the raster CRS
    wards = gpd.read_file(
        "data/processed/wards.gpkg",
        layer="wards"
    ).to_crs(src.crs)

    # Create an empty list for average elevations
    means = []

    # Calculate average elevation for each ward
    for geom in wards.geometry:

        cells, _ = mask(
            src,
            [geom],
            crop=True,
            filled=False
        )

        mean_value = float(cells.mean())

        means.append(mean_value)

# Add the calculated values to the ward table
wards["mean_elevation_m"] = means

# Print the results
print(
    wards[
        ["ward_name", "mean_elevation_m"]
    ].round(1)
)

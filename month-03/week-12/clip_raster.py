
import geopandas as gpd
import rasterio
from rasterio.mask import mask

with rasterio.open("data/raw/dem.tif") as src:

    # Read wards and match the raster CRS
    wards = gpd.read_file(
        "data/processed/wards.gpkg",
        layer="wards"
    ).to_crs(src.crs)

    # Merge the ward polygons into one boundary
    study_geom = wards.dissolve()

    # Clip the DEM to the study boundary
    clipped, clipped_transform = mask(
        src,
        study_geom.geometry,
        crop=True
    )

    print(
        "Before clip:",
        src.width,
        "x",
        src.height,
        "pixels"
    )

    print(
        "After clip:",
        clipped.shape[2],
        "x",
        clipped.shape[1],
        "pixels"
    )

    # Copy raster settings and update dimensions
    profile = src.profile.copy()

    profile.update(
        height=clipped.shape[1],
        width=clipped.shape[2],
        transform=clipped_transform
    )

    # Save the clipped DEM locally
    with rasterio.open(
        "data/processed/dem_ibadan_north.tif",
        "w",
        **profile
    ) as dst:
        dst.write(clipped)

print("Saved data/processed/dem_ibadan_north.tif")

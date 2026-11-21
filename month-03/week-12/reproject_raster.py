
import rasterio

from rasterio.warp import (
    calculate_default_transform,
    reproject,
    Resampling
)

# We want to convert the DEM to WGS 84
target_crs = "EPSG:4326"

# Open the original DEM
with rasterio.open("data/raw/dem.tif") as src:

    # Calculate the new raster grid
    transform, width, height = calculate_default_transform(
        src.crs,
        target_crs,
        src.width,
        src.height,
        *src.bounds
    )

    # Copy the original raster information
    profile = src.profile.copy()

    # Update information for the new CRS
    profile.update(
        crs=target_crs,
        transform=transform,
        width=width,
        height=height
    )

    # Create the reprojected raster
    with rasterio.open(
        "data/processed/dem_wgs84.tif",
        "w",
        **profile
    ) as dst:

        reproject(
            source=rasterio.band(src, 1),
            destination=rasterio.band(dst, 1),
            src_transform=src.transform,
            src_crs=src.crs,
            dst_transform=transform,
            dst_crs=target_crs,
            src_nodata=src.nodata,
            dst_nodata=src.nodata,
            resampling=Resampling.bilinear
        )

# Check that the new file has the correct CRS
with rasterio.open(
    "data/processed/dem_wgs84.tif"
) as check:

    print("New CRS:", check.crs)
    print("New pixel size:", check.res)

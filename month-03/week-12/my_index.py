
from pathlib import Path

import geopandas as gpd
import numpy as np
import rasterio
from rasterio.mask import mask

# The Lagos Mainland Landsat scene
scene = "LC08_L2SP_191055_20250117_20250128_02_T1"

folder = Path("data/raw/landsat/lagos_mainland")

red_file = folder / f"{scene}_SR_B4.TIF"
nir_file = folder / f"{scene}_SR_B5.TIF"
qa_file = folder / f"{scene}_QA_PIXEL.TIF"

# Load our Lagos Mainland boundary
boundary = gpd.read_file(
    "lagos_mainland_analysis_ready.gpkg",
    layer="boundary_utm31n"
)

# Open the three satellite bands
with rasterio.open(red_file) as red_src, \
     rasterio.open(nir_file) as nir_src, \
     rasterio.open(qa_file) as qa_src:

    # Check that all raster grids match
    for other in (nir_src, qa_src):
        if (
            red_src.crs != other.crs
            or red_src.transform != other.transform
            or red_src.shape != other.shape
        ):
            raise ValueError(
                "The Landsat bands do not share the same grid."
            )

    # Match the boundary to the raster CRS
    boundary = boundary.to_crs(red_src.crs)
    study_area = boundary.geometry.union_all()

    # Extract pixels for Lagos Mainland
    red_raw, transform = mask(
        red_src,
        [study_area],
        crop=True,
        filled=False
    )

    nir_raw, _ = mask(
        nir_src,
        [study_area],
        crop=True,
        filled=False
    )

    qa_raw, _ = mask(
        qa_src,
        [study_area],
        crop=True,
        filled=False
    )

    # Convert arrays to floating-point reflectance
    red = (
        red_raw[0].data.astype("float32")
        * 0.0000275 - 0.2
    )

    nir = (
        nir_raw[0].data.astype("float32")
        * 0.0000275 - 0.2
    )

    # Landsat QA bits 0-5:
    # Fill, dilated cloud, cirrus, cloud,
    # cloud shadow and snow
    qa = qa_raw[0].data
    clear = (qa & 0b00111111) == 0

    # Exclude masked, cloudy and invalid pixels
    valid = (
        ~np.ma.getmaskarray(red_raw[0])
        & ~np.ma.getmaskarray(nir_raw[0])
        & ~np.ma.getmaskarray(qa_raw[0])
        & clear
        & (red_raw[0].data > 0)
        & (nir_raw[0].data > 0)
        & (red >= 0)
        & (nir >= 0)
    )

    total = nir + red
    valid &= np.isfinite(total) & (total > 0)

    # Create an empty NDVI raster
    ndvi = np.full(
        red.shape,
        -9999.0,
        dtype="float32"
    )

    # Calculate NDVI for valid pixels
    ndvi[valid] = (
        (nir[valid] - red[valid])
        / total[valid]
    )

    count = int(valid.sum())

    if count == 0:
        raise ValueError(
            "No valid cloud-free pixels found for Lagos Mainland."
        )

    print("Study area: Lagos Mainland")
    print("Scene:", scene)
    print("Valid pixels:", count)
    print(
        "Minimum NDVI:",
        round(float(ndvi[valid].min()), 3)
    )
    print(
        "Maximum NDVI:",
        round(float(ndvi[valid].max()), 3)
    )
    print(
        "Mean NDVI:",
        round(float(ndvi[valid].mean()), 3)
    )

    # Prepare the output raster metadata
    profile = red_src.profile.copy()

    profile.update(
        driver="GTiff",
        height=ndvi.shape[0],
        width=ndvi.shape[1],
        transform=transform,
        count=1,
        dtype="float32",
        nodata=-9999.0,
        compress="lzw"
    )

    # Save the Lagos Mainland NDVI raster locally
    output = Path(
        "data/processed/lagos_mainland_ndvi.tif"
    )

    output.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with rasterio.open(
        output,
        "w",
        **profile
    ) as dst:
        dst.write(ndvi, 1)

    print("Saved:", output)

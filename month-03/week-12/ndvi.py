
from pathlib import Path
import numpy as np
import rasterio

folder = Path("data/raw/landsat")

# Find Landsat red and near-infrared bands
red_files = sorted(folder.rglob("*_SR_B4.TIF"))

if not red_files:
    raise FileNotFoundError(
        "Landsat Band 4 not found in data/raw/landsat"
    )

red_file = red_files[0]
nir_file = red_file.with_name(
    red_file.name.replace("_SR_B4.TIF", "_SR_B5.TIF")
)

if not nir_file.exists():
    raise FileNotFoundError(
        f"Matching Band 5 not found: {nir_file}"
    )

print("Red band:", red_file.name)
print("NIR band:", nir_file.name)

with rasterio.open(red_file) as red_src:
    with rasterio.open(nir_file) as nir_src:

        if (
            red_src.crs != nir_src.crs
            or red_src.transform != nir_src.transform
            or red_src.shape != nir_src.shape
        ):
            raise ValueError(
                "Band 4 and Band 5 must have matching grids."
            )

        red_raw = red_src.read(1, masked=True)
        nir_raw = nir_src.read(1, masked=True)

        # Convert stored values to reflectance
        red = red_raw.data.astype("float32") * 0.0000275 - 0.2
        nir = nir_raw.data.astype("float32") * 0.0000275 - 0.2

        # Exclude missing and invalid values
        valid = (
            ~np.ma.getmaskarray(red_raw)
            & ~np.ma.getmaskarray(nir_raw)
            & (red_raw.data > 0)
            & (nir_raw.data > 0)
        )

        total = nir + red
        valid &= np.isfinite(total) & (total != 0)

        ndvi = np.full(red.shape, -9999.0, dtype="float32")

        ndvi[valid] = (
            (nir[valid] - red[valid]) / total[valid]
        )

        print("Valid pixels:", int(valid.sum()))

        if valid.any():
            print("NDVI range:",
                  round(float(ndvi[valid].min()), 3),
                  "to",
                  round(float(ndvi[valid].max()), 3))
            print("Mean NDVI:",
                  round(float(ndvi[valid].mean()), 3))

        # Save NDVI as a local GeoTIFF
        profile = red_src.profile.copy()
        profile.update(
            dtype="float32",
            count=1,
            nodata=-9999.0
        )

        output = Path("data/processed/ndvi.tif")
        output.parent.mkdir(parents=True, exist_ok=True)

        with rasterio.open(output, "w", **profile) as dst:
            dst.write(ndvi, 1)

        print("Saved:", output)

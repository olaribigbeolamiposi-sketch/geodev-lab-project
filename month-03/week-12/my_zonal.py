
from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd
import rasterio
from rasterio.mask import mask

# Load your Lagos Mainland boundary
boundary = gpd.read_file(
    "lagos_mainland_analysis_ready.gpkg",
    layer="boundary_utm31n"
)

# Open the NDVI raster you calculated
raster_path = "data/processed/lagos_mainland_ndvi.tif"

results = []

with rasterio.open(raster_path) as src:

    # Match the boundary CRS with the raster CRS
    boundary = boundary.to_crs(src.crs)

    # Process each polygon individually
    for i, geom in enumerate(boundary.geometry):

        # Extract NDVI pixels within the polygon
        cells, _ = mask(
            src,
            [geom],
            crop=True,
            filled=False
        )

        # Remove missing and invalid values
        values = np.ma.masked_invalid(cells[0])
        valid = values.compressed()

        # Keep values in the valid NDVI range
        valid = valid[
            (valid >= -1) & (valid <= 1)
        ]

        # Calculate mean NDVI
        if len(valid) > 0:
            mean_ndvi = round(
                float(valid.mean()), 3
            )
        else:
            mean_ndvi = None

        # Give the polygon a readable name
        if len(boundary) == 1:
            area_name = "Lagos Mainland"
        else:
            area_name = f"Area {i + 1}"

        results.append({
            "area": area_name,
            "valid_pixels": len(valid),
            "mean_ndvi": mean_ndvi
        })

# Convert the results into a table
report = pd.DataFrame(results)

print("\nLAGOS MAINLAND NDVI ZONAL STATISTICS")
print(report.to_string(index=False))

# Save the results as CSV
output = Path(
    "month-03/week-12/my_zonal_stats.csv"
)

report.to_csv(output, index=False)

print("\nSaved:", output)

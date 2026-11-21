
from pathlib import Path

import geopandas as gpd
import rasterio
from rasterio.warp import transform_bounds
from shapely.geometry import box

# Load your Lagos Mainland boundary
boundary = gpd.read_file(
    "lagos_mainland_analysis_ready.gpkg",
    layer="boundary_utm31n"
)

print("Study area: Lagos Mainland")
print("Boundary CRS:", boundary.crs)
print("Boundary bounds:", boundary.total_bounds)

# Combine boundary features
study_area = boundary.geometry.union_all()

print("\nCHECKING AVAILABLE RASTERS")

# Find local teaching raster files
raster_files = [
    path
    for path in Path("data/raw").rglob("*")
    if path.is_file() and path.suffix.lower() == ".tif"
]

for path in raster_files:

    with rasterio.open(path) as src:

        # Transform raster bounds to boundary CRS
        bounds = transform_bounds(
            src.crs,
            boundary.crs,
            *src.bounds
        )

        # Make a rectangle from raster extent
        raster_extent = box(*bounds)

        # Test geographic overlap
        overlaps = study_area.intersects(
            raster_extent
        )

        print("\nFile:", path.name)
        print("CRS:", src.crs)
        print("Resolution:", src.res)
        print("Bounds:", bounds)
        print("Overlaps Lagos Mainland:", overlaps)

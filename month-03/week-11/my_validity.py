import geopandas as gpd

boundary = gpd.read_file(
    "lagos_mainland_analysis_ready.gpkg",
    layer="boundary_utm31n"
)

print("CRS:", boundary.crs)
print("Features:", len(boundary))

# Count invalid geometries before repair
invalid_before = (~boundary.is_valid).sum()

print("Invalid before repair:", invalid_before)

# Make a copy before changing geometry
fixed = boundary.copy()

# Repair any invalid geometries
fixed["geometry"] = fixed.make_valid()

# Count invalid geometries after repair
invalid_after = (~fixed.is_valid).sum()

print("Invalid after repair:", invalid_after)

print("Geometry types after repair:")
print(fixed.geom_type.value_counts())

if invalid_before == 0:
    print("No invalid geometries were found.")
else:
    print(
        "Repaired",
        invalid_before - invalid_after,
        "invalid geometries."
    )
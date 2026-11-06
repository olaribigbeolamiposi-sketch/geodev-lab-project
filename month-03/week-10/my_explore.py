import geopandas as gpd

path = "education_all_points_utm31n.gpkg"

print("Layers:")
print(gpd.list_layers(path))

education = gpd.read_file(path)

print("\nFirst rows:")
print(education.head())

print("\nRows and columns:", education.shape)

print("\nGeometry types:")
print(education.geom_type.value_counts())

print("\nCRS:")
print(education.crs)

print("\nBounds:")
print(education.total_bounds)
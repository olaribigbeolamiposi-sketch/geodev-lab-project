import pandas as pd
import geopandas as gpd

education = gpd.read_file(
    "education_all_points_utm31n.gpkg"
)

table = pd.read_csv(
    "data/raw/education_points.csv"
)

joined = education.merge(
    table[["id", "X", "Y"]],
    on="id",
    how="left"
)

matched = joined["X"].notna().sum()

print("Education features:", len(education))
print("Matched first try:", matched, "of", len(education))

print(
    joined[
        ["id", "X", "Y"]
    ].head()
)
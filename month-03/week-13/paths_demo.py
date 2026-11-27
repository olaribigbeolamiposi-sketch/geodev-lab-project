
from pathlib import Path

# Locate the teaching data folder
folder = Path("data/raw/lga_facilities")

# Check whether the folder exists
print("Folder exists:", folder.exists())

# Find and inspect each CSV file
for path in sorted(folder.glob("*.csv")):
    print(
        path.name,
        "| stem:", path.stem,
        "| suffix:", path.suffix
    )

# Prepare an output folder
output = Path("data/processed/lga_points")
output.mkdir(parents=True, exist_ok=True)

print("Output folder ready:", output)

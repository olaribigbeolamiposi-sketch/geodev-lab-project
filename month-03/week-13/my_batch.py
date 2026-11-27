
"""Batch-process Lagos Mainland education point CSV files."""

import logging
import time
from pathlib import Path

import geopandas as gpd
import pandas as pd


# SETTINGS
SOURCE_FILE = Path("data/raw/education_points.csv")

INPUT_FOLDER = Path("month-03/week-13/my_inputs")
OUTPUT_FOLDER = Path("data/processed/my_lagos_points")

SUMMARY_FILE = Path("month-03/week-13/my_batch_summary.csv")
LOG_FILE = Path("month-03/week-13/my_batch_run.log")

WORKING_CRS = "EPSG:32631"
OVERWRITE = False


# LOGGING
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)


def prepare_inputs():
    """Prepare two real CSVs and one broken test CSV."""

    INPUT_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )

    table = pd.read_csv(SOURCE_FILE)

    midpoint = len(table) // 2

    first = INPUT_FOLDER / "lagos_schools_part1.csv"
    second = INPUT_FOLDER / "lagos_schools_part2.csv"
    broken = INPUT_FOLDER / "broken_coordinates.csv"

    if not first.exists():
        table.iloc[:midpoint].to_csv(
            first,
            index=False
        )

    if not second.exists():
        table.iloc[midpoint:].to_csv(
            second,
            index=False
        )

    # Deliberate failure: no X or Y columns
    if not broken.exists():
        broken.write_text(
            "name,category\nBroken School,school\n",
            encoding="utf-8"
        )

    logging.info("Input files prepared")


def csv_to_points(csv_path):
    """Convert valid Lagos Mainland CSV coordinates to points."""

    table = pd.read_csv(csv_path)

    required = {"X", "Y"}
    missing = required - set(table.columns)

    if missing:
        raise ValueError(
            f"missing coordinate columns: {sorted(missing)}"
        )

    if table.empty:
        raise ValueError("CSV contains no records")

    coordinates = table[["X", "Y"]].apply(
        pd.to_numeric,
        errors="coerce"
    )

    if coordinates.isna().any().any():
        raise ValueError(
            "CSV contains invalid or missing coordinates"
        )

    points = gpd.GeoDataFrame(
        table,
        geometry=gpd.points_from_xy(
            coordinates["X"],
            coordinates["Y"]
        ),
        crs=WORKING_CRS
    )

    return points


def process_one(csv_path):
    """Process one file and return its result."""

    output = OUTPUT_FOLDER / f"{csv_path.stem}.gpkg"

    if output.exists() and not OVERWRITE:
        logging.info(
            "Skipped %s: output already exists",
            csv_path.name
        )

        return {
            "file": csv_path.name,
            "status": "skipped",
            "points": None
        }

    points = csv_to_points(csv_path)

    points.to_file(
        output,
        layer="education_points",
        driver="GPKG"
    )

    logging.info(
        "Converted %s: %d points",
        csv_path.name,
        len(points)
    )

    return {
        "file": csv_path.name,
        "status": "done",
        "points": len(points)
    }


def main():
    """Run the batch and record successes and failures."""

    start = time.perf_counter()

    OUTPUT_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )

    prepare_inputs()

    results = []

    for csv_path in sorted(INPUT_FOLDER.glob("*.csv")):
        try:
            results.append(process_one(csv_path))

        except Exception as error:
            logging.error(
                "Failed %s: %s",
                csv_path.name,
                error
            )

            results.append({
                "file": csv_path.name,
                "status": "failed",
                "points": None
            })

    summary = pd.DataFrame(
        results,
        columns=["file", "status", "points"]
    )

    summary["points"] = summary["points"].astype("Int64")

    summary.to_csv(
        SUMMARY_FILE,
        index=False
    )

    elapsed = time.perf_counter() - start

    logging.info(
        "Finished %d files in %.1f seconds",
        len(results),
        elapsed
    )

    print("\nLAGOS MAINLAND BATCH SUMMARY")
    print(summary.to_string(index=False))
    print("\nSaved:", SUMMARY_FILE)
    print("Log:", LOG_FILE)


if __name__ == "__main__":
    main()

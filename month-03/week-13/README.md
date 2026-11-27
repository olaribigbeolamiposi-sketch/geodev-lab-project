# Week 13: Batch Processing and Automation

## Overview

This week I learned how to automate repetitive GIS tasks using Python functions, pathlib, loops, logging and exception handling.

## Guided practical

I created `paths_demo.py` to locate CSV files and prepare an output folder.

I created `batch_convert.py` to convert six facility CSV files into GeoPackages using GeoPandas.

### What broke?

The first batch processed five files successfully, but `egbeda.csv` failed because it contained the columns `lat` and `lon` instead of `latitude` and `longitude`.

The log recorded:

`Failed egbeda.csv: missing columns: ['latitude', 'longitude']`

The script continued processing the remaining files instead of stopping.

### How I fixed it

I updated the Python code to rename:

- `lat` to `latitude`
- `lon` to `longitude`
- `facility` to `name`

This allowed the script to recognise Egbeda's columns without editing the original CSV.

I also used `OVERWRITE = False` to skip outputs that already existed.

## Independent Challenge: Lagos Mainland

My independent script, `my_batch.py`, automates the conversion of Lagos Mainland education point CSV files into GeoPackages.

It uses the existing `data/raw/education_points.csv` dataset.

The script prepares two CSV subsets and one deliberately broken CSV file to demonstrate error handling.

### Deliberate failure

The file `broken_coordinates.csv` deliberately contains no `X` or `Y` columns.

The script raises a `ValueError` for this file and records the failure in `my_batch_run.log`.

The other valid CSV files can still be processed.

### Automation features

- Reusable Python functions with docstrings
- Settings defined at the top
- Path management using pathlib
- Processing multiple files with a loop
- Error handling using try and except
- Logging successes and failures
- Avoiding unnecessary overwriting
- Saving a summary CSV
- Using `if __name__ == "__main__":`

## Outputs

Guided outputs:

- `batch_summary.csv`
- `batch_run.log`

Independent outputs:

- `my_batch_summary.csv`
- `my_batch_run.log`
- `my_inputs/` containing the independent challenge input CSVs

GeoPackages are written to `data/processed/` and are kept locally.

## Running the scripts

From the repository root:

```powershell
uv run month-03/week-13/paths_demo.py
uv run month-03/week-13/batch_convert.py
uv run month-03/week-13/my_batch.py
```

## What I learned

I learned how to write reusable Python functions and automate the processing of several files.

I also learned that a batch script should not stop because one input file is broken. Instead, it should record the error, continue processing and generate a useful report.

Logging and safe reruns make automation easier to inspect, troubleshoot and reuse.
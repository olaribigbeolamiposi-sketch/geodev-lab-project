import csv

def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    values = []

    for row in rows:
        raw = row[column].strip()

        if raw == "":
            continue

        values.append(float(raw))

    return {
        "smallest": min(values),
        "largest": max(values),
        "count": len(values),
    }

x_result = inspect_column("education_points.csv", "X")
y_result = inspect_column("education_points.csv", "Y")

print("X:", x_result)
print("Y:", y_result)
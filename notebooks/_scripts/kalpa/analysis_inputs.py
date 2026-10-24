"""Shared readers for the cleaned booking output and raw reference/event tables."""

import csv
import gzip
from pathlib import Path

import pandas as pd


def project_root():
    return Path(__file__).resolve().parents[3]


def booking_file(data_dir):
    for name in ("bookings.csv", "bookings_all.csv.gz", "bookings_all.csv", "bookings.csv.gz"):
        path = data_dir / name
        if not path.is_file():
            continue
        opener = gzip.open if path.suffix == ".gz" else open
        with opener(path, "rt", encoding="utf-8", newline="") as file:
            if "test_code" in next(csv.reader(file), []):
                return path
    raise FileNotFoundError(f"No booking-test table found in {data_dir}")


def plan_frame(data_dir, raw_dir):
    path = data_dir / "plan_2026_h1.csv"
    if path.is_file():
        plan = pd.read_csv(path)
        if {"city", "month", "target"}.issubset(plan.columns):
            plan["city"] = plan["city"].replace({"Bangalore": "Bengaluru"})
            return plan[["city", "month", "target"]]
        raise ValueError(f"Expected city, month and target columns in {path}")

    path = raw_dir / "plan" / "plan_2026_H1.csv"
    source = pd.read_csv(path)
    months = [column for column in source.columns if column.startswith("2026-")]
    if not months:
        raise ValueError(f"No 2026 monthly plan columns found in {path}")
    plan = source.melt(id_vars="city", value_vars=months, var_name="month", value_name="target")
    plan["city"] = plan["city"].replace({"Bangalore": "Bengaluru"})
    return plan[["city", "month", "target"]]


def _table_paths(data_dir, raw_dir, name):
    if name == "bookings.csv":
        return [booking_file(data_dir)]
    if name in ("collections.csv", "results.csv"):
        clean = [data_dir / name, data_dir / f"{name.removesuffix('.csv')}_clean.csv.gz"]
        clean = [path for path in clean if path.is_file()]
        if clean:
            return clean[:1]
        raw = sorted((raw_dir / name.removesuffix(".csv")).rglob("*.csv.gz"))
        if raw:
            return raw
    elif name == "tests_catalogue.csv":
        candidates = [data_dir / name, raw_dir / "reference" / name]
        return [path for path in candidates if path.is_file()][:1]
    else:
        raise ValueError(f"Unsupported analysis table: {name}")
    raise FileNotFoundError(f"Could not find {name} in {data_dir} or {raw_dir}")


def table_rows(data_dir, raw_dir, name):
    if name == "plan_2026_h1.csv":
        yield from plan_frame(data_dir, raw_dir).to_dict("records")
        return

    for path in _table_paths(data_dir, raw_dir, name):
        opener = gzip.open if path.suffix == ".gz" else open
        with opener(path, "rt", encoding="utf-8", newline="") as file:
            for row in csv.DictReader(file):
                if name == "bookings.csv":
                    row.setdefault("booking_status", row.get("status_at_export", ""))
                    row.setdefault("source_system", row.get("system", ""))
                yield row

import csv
import gzip
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "notebooks" / "_scripts"))

from kalpa.analysis_inputs import booking_file, plan_frame, table_rows


def test_analysis_inputs_read_normalized_gzip_and_wide_plan(tmp_path):
    clean = tmp_path / "clean"
    raw = tmp_path / "raw"
    clean.mkdir()
    (raw / "plan").mkdir(parents=True)
    (raw / "plan" / "plan_2026_H1.csv").write_text(
        "city,metric,2026-01,2026-02\nBangalore,test_volume_target_2026,100,110\n",
        encoding="utf-8",
    )
    booking_path = clean / "bookings_all.csv.gz"
    with gzip.open(booking_path, "wt", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(
            file, fieldnames=["booking_id", "system", "status_at_export", "test_code"]
        )
        writer.writeheader()
        writer.writerow(
            {"booking_id": "b1", "system": "nova", "status_at_export": "booked", "test_code": "T1"}
        )

    assert booking_file(clean) == booking_path
    plan = plan_frame(clean, raw)
    assert plan.to_dict("records") == [
        {"city": "Bengaluru", "month": "2026-01", "target": 100},
        {"city": "Bengaluru", "month": "2026-02", "target": 110},
    ]
    booking = next(table_rows(clean, raw, "bookings.csv"))
    assert booking["booking_status"] == "booked"
    assert booking["source_system"] == "nova"


def test_migration_helper_counts_active_lines_from_gzipped_input(tmp_path):
    data = tmp_path / "clean"
    output = tmp_path / "outputs"
    raw = tmp_path / "raw"
    data.mkdir()
    (raw / "collections").mkdir(parents=True)
    (raw / "results").mkdir(parents=True)
    cities = ("Ahmedabad", "Bengaluru", "Chennai", "Hyderabad", "Jaipur", "Pune")
    with (data / "plan_2026_h1.csv").open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["city", "month", "target"])
        writer.writeheader()
        writer.writerows(
            {"city": city, "month": f"2026-{month:02}", "target": 20}
            for city in cities
            for month in range(1, 7)
        )
    bookings = data / "bookings_all.csv.gz"
    with gzip.open(bookings, "wt", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["booking_id", "created_at", "slot_at", "city", "channel", "source",
                        "test_code", "status_at_export", "system"],
        )
        writer.writeheader()
        for year, count in (("2025", 100), ("2026", 105)):
            for index in range(count):
                city = cities[index % len(cities)]
                month = index % 6 + 1
                writer.writerow(
                    {
                        "booking_id": f"{year}-{index}",
                        "created_at": f"{year}-{month:02}-01 10:00:00",
                        "slot_at": f"{year}-{month:02}-01 10:00:00",
                        "city": city,
                        "channel": "clinic",
                        "source": "app",
                        "test_code": f"T{index}",
                        "status_at_export": "booked",
                        "system": "legacy",
                    }
                )
        writer.writerow(
            {
                "booking_id": "2026-rescheduled",
                "created_at": "2026-01-01 10:00:00",
                "slot_at": "2026-01-01 10:00:00",
                "city": "Ahmedabad",
                "channel": "clinic",
                "source": "app",
                "test_code": "T-rescheduled",
                "status_at_export": "rescheduled",
                "system": "nova",
            }
        )
    for directory, name, header in (
        (raw / "collections", "part.csv.gz", ["booking_id"]),
        (raw / "results", "part.csv.gz", ["booking_id", "test_code", "result_ts"]),
    ):
        with gzip.open(directory / name, "wt", encoding="utf-8", newline="") as file:
            csv.writer(file).writerow(header)

    subprocess.run(
        [
            sys.executable,
            str(ROOT / "notebooks" / "_scripts" / "analyze_brief_a_b_migration.py"),
            "--data-dir",
            str(data),
            "--output-dir",
            str(output),
            "--raw-dir",
            str(raw),
        ],
        check=True,
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    with (output / "brief_a_h1_overall.csv").open(newline="", encoding="utf-8") as file:
        summary = next(csv.DictReader(file))
    assert summary["y2025_h1_test_lines"] == "100"
    assert summary["y2026_h1_test_lines"] == "105"
    assert summary["actual_yoy_growth_pct"] == "5.0"
    assert summary["rescheduled_lines_excluded"] == "1"

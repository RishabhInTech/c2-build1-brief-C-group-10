import csv
import gzip
import json
import subprocess
import sys
import zipfile
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def csv_bytes(rows):
    if not rows:
        return b""
    import io

    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=rows[0])
    writer.writeheader()
    writer.writerows(rows)
    return gzip.compress(stream.getvalue().encode())


def test_zip_cleaning_and_h1_bridge(tmp_path):
    invoice_rows = [
        {"invoice_id": "INV-2026-000001", "invoice_date": "2026-01-01", "booking_id": "book_1",
         "city": "Jaipur", "channel": "clinic", "amount": "100.00"},
        {"invoice_id": "INV-2026-000002", "invoice_date": "2026-01-02", "booking_id": "book_2",
         "city": "Pune", "channel": "home", "amount": "50.00"},
    ]
    payment_rows = [
        {"payment_id": "pay_abcde12345", "amount_paise": "6000", "notes_invoice_ref": "INV-2026-000001",
         "status": "captured", "created_at_epoch": "1767312000", "method": "upi",
         "settlement_id": "setl_12345678"},
        {"payment_id": "pay_abcde12346", "amount_paise": "5000", "notes_invoice_ref": "INV-2026-000002",
         "status": "captured", "created_at_epoch": "1782950400", "method": "upi",
         "settlement_id": "setl_12345678"},
        {"payment_id": "pay_abcde12347", "amount_paise": "2500", "notes_invoice_ref": "",
         "status": "captured", "created_at_epoch": "1769904000", "method": "card",
         "settlement_id": ""},
    ]
    settlement_rows = [
        {"settlement_id": "setl_12345678", "amount_paise": "6000", "fees_paise": "100",
         "tax_paise": "18", "utr": "utr_1", "created_at_epoch": "1782777600", "status": "processed"},
    ]
    archive = tmp_path / "finance.zip"
    with zipfile.ZipFile(archive, "w") as pack:
        pack.writestr("datapack/invoices/invoices_2026Q1.csv.gz", csv_bytes(invoice_rows))
        pack.writestr("datapack/payments/gateway_export_2026-01.csv.gz", csv_bytes(payment_rows))
        pack.writestr("datapack/payments/settlements_2026Q2.csv.gz", csv_bytes(settlement_rows))
        pack.writestr("datapack/bookings/unused.csv.gz", b"not extracted")

    clean, output, actions = (tmp_path / name for name in ("clean", "output", "actions"))
    subprocess.run(
        [sys.executable, str(ROOT / "clean_brief_c.py"), "--source-dir", str(archive),
         "--output-dir", str(clean)],
        cwd=ROOT, check=True, capture_output=True, text=True,
    )
    subprocess.run(
        [sys.executable, str(ROOT / "analyze_brief_c_reconciliation.py"), "--data-dir", str(clean),
         "--output-dir", str(output), "--action-dir", str(actions)],
        cwd=ROOT, check=True, capture_output=True, text=True,
    )

    summary = json.loads((output / "finance_bridge_summary.json").read_text())
    cohort = summary["invoice_cohort"]
    attempts = summary["payment_attempts_created_in_h1"]
    assert cohort["invoice_count"] == 2
    assert cohort["positive_invoice_balance_rs_by_h1_end"] == "90.00"
    assert cohort["remaining_positive_invoice_balance_rs_by_observation_cutoff"] == "40.00"
    assert cohort["remaining_positive_balance_invoice_count_by_observation_cutoff"] == 1
    assert attempts["unmatched_capture_rows"] == 1
    assert attempts["unmatched_capture_amount_rs"] == "25.00"
    assert summary["settlement_period"]["gross_rs"] == "60.00"
    city = pd.read_csv(output / "finance_outstanding_by_city_channel.csv", dtype=str)
    month = pd.read_csv(output / "finance_outstanding_by_invoice_month.csv", dtype=str)
    ages = pd.read_csv(output / "finance_open_balance_age.csv", dtype=str)
    unmatched = pd.read_csv(output / "finance_unmatched_capture_breakdown.csv", dtype=str)
    assert len(city) == 2
    assert city.set_index("city")["positive_balance_pct_billed_at_cutoff"].to_dict() == {
        "Jaipur": "40.00", "Pune": "0.00"
    }
    assert month["positive_balance_at_cutoff_rs"].tolist() == ["40.00"]
    assert ages["invoice_count"].astype(int).sum() == 1
    assert unmatched["attempts"].astype(int).sum() == 1

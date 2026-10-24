# Brief C: H1 2026 invoice-to-capture reconciliation

**Audience:** COO and Finance controller
**Period:** 1 January–30 June 2026, India time
**Observation cutoff:** 15 July 2026, India time

This follows the H1 volume check: active scheduled test lines grew **4.97% (rounds to 5%)** against **18.32%** implied by plan. The finance bridge below is also H1-based. Monetary figures in this brief are in **crores of rupees**; the audit CSVs retain exact rupee amounts.

## Board sentence

> At H1 2026 close, 11,586 of 162,876 invoices (**₹26.828 crore billed**) carried **₹1.947 crore** in positive balances; after later captures, **₹1.648 crore (6.14% of H1 billings)** remained open across 9,824 invoices on 15 July, while 1,541 H1 captures worth **₹0.267 crore** still lacked a safe invoice match—Finance should prioritize June's open invoices and resolve both exception lists before calling balances lost.

Positive balances are calculated invoice by invoice; overcaptures on other invoices are kept separate and are not used to offset unrelated balances.

## H1 invoice bridge

| H1 2026 item | Rows / invoices | Amount (₹ crore) | Rule |
|---|---:|---:|---|
| Invoices dated 1 Jan–30 Jun | 162,876 invoices | 26.828 | One row per unique invoice ID |
| Captured attempts safely matched by 30 Jun | 151,993 attempts across 151,305 invoices | 24.998 | Captured status; matched attempts summed by invoice |
| Invoices with no matched capture by 30 Jun | 11,571 invoices | 1.945 face value | No captured attempt matched by the H1 cutoff |
| Partially paid invoices by 30 Jun | 15 invoices | 0.002 remaining | Invoice balance after matched captures |
| Positive invoice balances by 30 Jun | 11,586 invoices | 1.947 | Sum of positive invoice balances; no cross-invoice offsets |
| Overcaptured invoices by 30 Jun | 704 invoices | 0.117 above invoice amount | Reported separately |
| H1 no-capture invoices with a later capture | 1,763 invoices | 0.298 face value | Captures observed through 15 Jul 2026 |
| Positive invoice balances still open by 15 Jul | 9,824 invoices | 1.648 | Balance through the observation cutoff |

## H1 payment attempts

| H1 2026 payment activity | Attempts | Amount (₹ crore) | Treatment |
|---|---:|---:|---|
| Captured attempts | 156,458 | 25.712 | Gateway status `captured` |
| Captured attempts with a safe invoice match | 154,917 | 25.446 | Invoice reference rule below |
| Captured attempts without a safe invoice match | 1,541 | 0.267 | Kept as an exception list for Finance |
| Failed attempts | 6,154 | 1.004 | Not counted as receipts |

The invoice-cohort match total and the H1 payment-attempt total differ because the first measures captures attached to invoices issued in H1 by the cutoff, while the second measures attempts created during H1. They are separate views of the bridge and should not be added together.

## What the deeper cuts show

These are follow-up priorities, not evidence of why a patient did or did not pay:

| Cut | Finding | How to use it |
|---|---|---|
| Invoice month | June contributed **₹1.053 crore (54.1%)** of positive balances at H1 close despite representing **16.5%** of H1 billed value. By 15 July, **₹0.755 crore** remained open on June invoices, **45.8%** of the H1 open balance. | Start the Finance review with June's invoice list; the short observation window is consistent with less time to collect, not proof of a June process failure. |
| City and channel | By 15 July, open balances were **5.97%–6.28%** of billed amount across the six cities. Clinic invoices had **₹0.888 crore** open (**6.33%** of clinic billing) and home invoices **₹0.761 crore** (**5.94%**). | No single city dominates on the billed-value rate; review channel differences with the same due-date and payment-coverage caveats. |
| Invoice age | **3,785** open invoices aged 91+ days from invoice date carried **₹0.631 crore (38.3%)** of the balance; **4,019** invoices aged 0–30 days carried **₹0.670 crore (40.6%)**. | Treat this only as age since invoice date. Contractual due dates are not in this pack, so these buckets are not an overdue/DPD analysis. |
| Unmatched captures | Of 1,541 H1 unmatched captures, **959 (62.2%; ₹0.162 crore)** had the standard-length reference shape but no safe invoice match; **582 (37.8%; ₹0.105 crore)** had a 7-digit final segment. UPI accounts for **792 attempts / ₹0.138 crore**, the largest method group. | The first queue is source coverage and reference correctness; the second is malformed-reference investigation. Neither is a confirmed loss. |

The corresponding aggregate, identifier-free tables are [`finance_outstanding_by_invoice_month.csv`](../outputs/brief_c/finance_outstanding_by_invoice_month.csv), [`finance_outstanding_by_city_channel.csv`](../outputs/brief_c/finance_outstanding_by_city_channel.csv), [`finance_open_balance_age.csv`](../outputs/brief_c/finance_open_balance_age.csv), and [`finance_unmatched_capture_breakdown.csv`](../outputs/brief_c/finance_unmatched_capture_breakdown.csv). Exact rupees and row counts are retained. City, channel, age, and month cuts describe distribution only; no supplied field identifies invoice due dates, reversals after the cutoff, or customer cause.

## All-source context

The full supplied files cover invoices dated 30 Dec 2024–30 Jun 2026 and gateway attempts through 15 Jul 2026. Across those full source windows there are **470,776 invoices totaling ₹73.70 crore** and **455,469 captured attempts totaling ₹71.25 crore gross**. Safe invoice matching covers **₹70.52 crore**; **4,588 captured attempts totaling ₹0.73 crore** remain unmatched. These totals are not the H1 bridge and do not form a same-period collection rate.

## Matching and settlement checks

The matching rule is exact `invoice_id` first; otherwise remove hyphens from the trimmed, uppercased reference and match only when the invoice key is unique. No canonical collisions were found. Amount/date similarity is not used to guess identity. Across all source periods, 468,742 of 473,507 gateway rows map to an invoice; 4,765 do not.

The 181 settlement rows dated in H1 show gross **₹25.145 crore**, fees **₹0.515 crore**, tax **₹0.093 crore**, and calculated net **₹24.537 crore**. Captures linked to those settlement IDs total **₹25.753 crore** across supplied payment dates, **₹0.608 crore** above settlement gross. This is a diagnostic, not a bank reconciliation: payment and settlement date windows differ, and the source pack has no independent bank statement or validated clinic cash register.

## Audit and rebuild

The cleaner ([`clean_brief_c.py`](../clean_brief_c.py)) reads the bundled ZIP by default, or an unpacked data-pack folder passed with `--source-dir`. It writes row-level tables locally under the Git-ignored `data/clean/brief_c/`. The analysis script ([`analyze_brief_c_reconciliation.py`](../analyze_brief_c_reconciliation.py)) reads rupee amounts as exact decimals and applies H1 boundaries in `Asia/Kolkata`; H1 closes at 30 June 23:59 IST.

```powershell
python clean_brief_c.py
python analyze_brief_c_reconciliation.py --data-dir data/clean/brief_c --output-dir outputs/brief_c --year 2026 --observation-cutoff 2026-07-15
```

[`finance_bridge_summary.csv`](../outputs/brief_c/finance_bridge_summary.csv) and [`finance_all_period_summary.csv`](../outputs/brief_c/finance_all_period_summary.csv) show crores alongside exact rupee amounts for audit. The JSON summary retains exact rupee values, dates, counts, matching coverage and limitations. Row-level Finance action lists are written under the ignored `data/clean/brief_c/actions/` folder and are not committed.

The reconciliation command also regenerates the four aggregate follow-up tables above. These are grouped summaries and contain no invoice, booking, payment or patient identifiers.

The bridge remains provisional until Finance confirms source completeness, refunds/reversals, cash coverage, and the settlement-to-bank match. A missing captured gateway match does not prove permanent nonpayment.

**SQL handoff gap:** the committed Brief C bridge is currently implemented and validated in Python, not as a Finance-ready SQL reconciliation. Before describing SQL as a second implementation, add `sql/06_brief_c.sql` and reconcile its invoice counts, capture counts, and exact rupee amounts against these outputs.

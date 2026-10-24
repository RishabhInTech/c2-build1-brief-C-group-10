# Brief C: H1 2026 invoice-to-capture reconciliation

**Audience:** COO and Finance controller
**Period:** 1 January–30 June 2026, India time
**Observation cutoff:** 15 July 2026, India time

This follows the H1 volume check: active scheduled test lines grew **4.97% (rounds to 5%)** against **18.32%** implied by plan. The finance bridge below is also H1-based. Monetary figures in this brief are in **crores of rupees**; the audit CSVs retain exact rupee amounts.

## Board sentence

> At H1 2026 close, positive invoice balances totaled **₹1.947 crore** across **11,586 of 162,876 invoices** (**₹26.828 crore billed**): 11,571 had no captured match and 15 were partial; by 15 July, 1,763 of those no-capture invoices had later captures against **₹0.298 crore** in invoice face value, leaving **₹1.648 crore** open across 9,824 invoices, while 1,541 H1 captured attempts worth **₹0.267 crore** had no safe invoice match—Finance should pursue the open invoice list and resolve unmatched captures before calling the difference lost.

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

The bridge remains provisional until Finance confirms source completeness, refunds/reversals, cash coverage, and the settlement-to-bank match. A missing captured gateway match does not prove permanent nonpayment.

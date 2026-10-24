# H1 test volume and booking-system migration

**Stage 1:** compare H1 test volume with plan, then use the migration comparison as a diagnostic. The exact metric and the full city, month and channel breakdown are in [`project-analysis.md`](project-analysis.md).

## H1 result

The handbook's **5% actual growth** is reproduced by counting active booking-test lines by **scheduled test date (`slot_at`)**: H1 2025 had **435,880** lines and H1 2026 had **457,539**, a **4.97%** increase that rounds to 5%. The detailed six-city plan is **515,740** lines, or **18.32%** growth on that baseline. H1 volume reached **88.72% of plan**, a shortfall of **58,201 lines** (13.35 percentage points below plan growth).

This measure aligns the H1 period to when each test is scheduled, which is the relevant month for the plan's test-volume target. It excludes **3,541** superseded lines on records marked `rescheduled`; keeping them would yield 461,080 lines and +5.78%. Booking creation date is a sensitivity, not the plan-aligned cohort: it yields **451,332** versus **436,094** (+3.49%). City, month, channel and migration cuts below all use scheduled dates and the same active-line rule.

## Migration comparison

| Group | H1 2025 | H1 2026 active | H1 plan | Attainment |
|---|---:|---:|---:|---:|
| Chennai and Jaipur (Nova migration) | 125,290 | 120,932 | 146,284 | 82.67% |
| Ahmedabad, Bengaluru, Hyderabad and Pune (legacy) | 310,590 | 336,607 | 369,456 | 91.11% |

The treated cities were already down **3.11%** year over year in January–March, compared with **+9.71%** for controls. In April–June they were down **3.86%** versus **+7.02%**. The pre-adjusted relative change is **+1.93 percentage points**, but the comparison is descriptive: only two cities migrated and the pre-period trends differed. It does not identify a causal migration effect.

## Additional checks

- Clinic lines fell **34,037 (11.86%)** across the six cities; home lines rose **55,696 (37.39%)**. Home growth partly offset clinic decline.
- Every city and month missed plan, although each month exceeded its H1 2025 scheduled volume. March had the largest monthly shortfall (**11,208 lines**).
- For the scheduled H1 cohort, Nova-era collection coverage was **22,856/24,979 bookings (91.5%)**; result matches were **45,056/58,770 test lines (76.7%)**. Legacy result matches were 82.0% in control cities and 82.2% in treated cities. These joins use different grains and are not completion rates; result timestamps are a separate operational measure, not the plan-volume date.
- By result timestamp, the pack contains **356,442** H1 2025 and **378,160** H1 2026 result events; those H1 result dates match **81.04%** and **81.01%**, respectively, of active scheduled test lines. This is a coverage check—not a claim that the remaining tests were never completed. See [`brief_a_h1_result_date_summary.csv`](../outputs/brief_a_h1_result_date_summary.csv).

The files locate the shortfall and show a channel mix shift, but do not establish why clinic volume fell or why the plan was missed. Check the plan definition, local clinic capacity and demand, March and May performance, and booking-to-result timing before naming a cause.

## Reproducibility

```powershell
python analyze_h1_volume.py --data-dir "<path-to-full-cleaned-folder>" --output-dir outputs
python analyze_brief_a_b_migration.py --data-dir "<path-to-full-cleaned-folder>" --output-dir outputs
```

The outputs contain aggregate counts only. The full cleaned tables remain local.

# Project analysis: volume first, money next

## 1. H1 test-volume check

**H1 2026 active scheduled test lines grew 4.97% (about 5%), against 18.32% implied plan growth.** The exact gap is **13.35 percentage points** (13 points using the rounded 5%-versus-18% figures in the handbook). We count each nonblank booking-test line by its scheduled test date (`slot_at`), across Ahmedabad, Bengaluru, Chennai, Hyderabad, Jaipur and Pune, and exclude 3,541 superseded records marked `rescheduled`.

H1 2026 has **457,539** active scheduled test lines versus **435,880** in H1 2025, an increase of **21,659**. The six-city plan is **515,740** lines, equivalent to **18.32% growth** over the scheduled-date baseline. Actual volume reached **88.72% of plan** and finished **58,201 lines short**.

The plan is monthly test-volume targets, so `slot_at` assigns each booked test to the month in which it is scheduled, rather than when the booking was created. Both actual and plan growth use the **435,880 active H1 2025 scheduled lines** as their denominator; neither uses full-year 2025. H1 2026 excludes `booking_status = rescheduled` per the booking identity rule in notebook 03. The target is the sum of the six cities' January–June monthly targets in `plan_2026_h1.csv`.

```text
Active scheduled H1 2026 lines = 461,080 raw lines − 3,541 superseded reschedule lines = 457,539
Actual growth = (457,539 / 435,880 − 1) × 100 = 4.97% (rounds to 5%)
Plan growth   = (515,740 / 435,880 − 1) × 100 = 18.32%
Plan attainment = 457,539 / 515,740 × 100 = 88.72%
Shortfall = 457,539 − 515,740 = −58,201 test lines
Sensitivity: 461,080 / 435,880 − 1 = 5.78% if superseded rows are retained
Booking-created-date sensitivity: 451,332 / 436,094 − 1 = 3.49%
```

Reproduce the primary counts and city/month/channel tables with `analyze_h1_volume.py` using the full cleaned folder:

```powershell
python analyze_h1_volume.py --data-dir "<path-to-full-cleaned-folder>" --output-dir outputs
```

The scheduled-date calculation reproduces the handbook's rounded 5% from the supplied booking extract. It is a booked/scheduled-volume measure, not a count of tests completed by result date; confirm that the plan owner also defines its target on scheduled test lines before board use. The booking-created-date sensitivity is lower because booking creation and scheduled test dates can fall in different months or halves.

### Where the plan gap sits

All six cities finished below plan. Chennai has the largest shortfall after removing superseded rows; Jaipur has the lowest attainment and the largest year-over-year decline.

| City | H1 2025 scheduled lines | H1 2026 active scheduled lines | YoY growth | Plan | Attainment | Lines below plan |
|---|---:|---:|---:|---:|---:|---:|
| Ahmedabad | 76,853 | 84,986 | +10.58% | 90,773 | 93.62% | 5,787 |
| Bengaluru | 99,991 | 107,543 | +7.55% | 120,085 | 89.56% | 12,542 |
| Chennai | 80,195 | 80,718 | +0.65% | 93,912 | 85.95% | 13,194 |
| Hyderabad | 73,162 | 78,575 | +7.40% | 86,421 | 90.92% | 7,846 |
| Jaipur | 45,095 | 40,214 | −10.82% | 52,372 | 76.79% | 12,158 |
| Pune | 60,584 | 65,503 | +8.12% | 72,177 | 90.75% | 6,674 |
| **All cities** | **435,880** | **457,539** | **+4.97%** | **515,740** | **88.72%** | **58,201** |

Every month missed plan, while all six months were above their 2025 scheduled volume. March had the largest monthly shortfall (**11,208 lines**); May was close behind at **11,020**. See [`brief_a_h1_monthly.csv`](../outputs/brief_a_h1_monthly.csv) and [`brief_a_b_city_summary.csv`](../outputs/brief_a_b_city_summary.csv).

| Month | H1 2025 | H1 2026 active | YoY growth | Plan | Attainment | Lines below plan |
|---|---:|---:|---:|---:|---:|---:|
| January | 73,512 | 77,239 | +5.07% | 87,002 | 88.78% | 9,763 |
| February | 72,931 | 80,037 | +9.74% | 86,293 | 92.75% | 6,256 |
| March | 74,300 | 76,674 | +3.20% | 87,882 | 87.25% | 11,208 |
| April | 72,346 | 75,213 | +3.96% | 85,616 | 87.85% | 10,403 |
| May | 71,566 | 73,658 | +2.92% | 84,678 | 86.99% | 11,020 |
| June | 71,225 | 74,718 | +4.90% | 84,269 | 88.67% | 9,551 |

### What changed in the volume mix

| Channel | H1 2025 | H1 2026 active | Change | YoY |
|---|---:|---:|---:|---:|
| Clinic | 286,905 | 252,868 | −34,037 | −11.86% |
| Home | 148,975 | 204,671 | +55,696 | +37.39% |
| **Total** | **435,880** | **457,539** | **+21,659** | **+4.97%** |

Clinic lines fell in every city while home lines rose in every city. The home increase partly offset the clinic decline, leaving modest net growth. This identifies the mix behind the total; it does not establish why clinic volume fell or whether the plan's channel assumptions were realistic. City-channel details are in [`brief_a_h1_channel_by_city.csv`](../outputs/brief_a_h1_channel_by_city.csv).

### What the migration check can and cannot say

The two cities that migrated to Nova reached **82.67%** of plan; the four cities remaining on legacy reached **91.11%**. On scheduled-date volume, the migration group was down **3.11%** year over year in January–March while the comparison group was up **9.71%**. In April–June, the groups were down **3.86%** and up **7.02%**, respectively. The pre-adjusted relative change is **+1.93 percentage points**, but only two cities migrated and their pre-period trend differed. This comparison cannot establish that Nova caused the H1 plan miss.

Collection and result joins are coverage diagnostics at different grains, not completed-test rates. For the scheduled H1 cohort, 2026 Nova bookings had collection matches for **22,856/24,979 bookings (91.5%)** and result matches for **45,056/58,770 test lines (76.7%)**; legacy test-line result matching was about **82%**. These are source-join indicators, not plan volume or completion rates. Result-date diagnostics in [`brief_a_h1_result_date_summary.csv`](../outputs/brief_a_h1_result_date_summary.csv) count 356,442 H1 2025 and 378,160 H1 2026 result events; H1 result timestamps match about **81.0%** of active scheduled lines in either year. The event counts include a few repeated booking-test pairs. Use scheduled dates for plan comparison and result timestamps only for a separately defined completion analysis.

**What we can conclude:** active H1 scheduled test volume grew **4.97% (rounds to 5%)**, well below the plan's implied **18.32%**; all cities and months missed plan, with home growth partly offsetting clinic declines. **What we cannot conclude from these files:** the causal business reason for the clinic decline or plan miss, or that a booked/scheduled test was completed. Next checks are the plan's date definition, March and May city performance, local capacity and marketing, and booking-to-result coverage.

## 2. Finance bridge

After the volume check, the project answers the COO's money question for H1 2026: which invoices had no captured match by 30 June, which H1 captures lacked an invoice match, and how much changed by the 15 July observation cutoff. The H1 bridge, matching rule, settlement gap and Finance action lists are in [`brief-c-analysis.md`](brief-c-analysis.md); all displayed monetary figures are in crores.

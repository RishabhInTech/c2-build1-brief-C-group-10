# Interview bank: the questions this project earns you the right to answer

Each question is tied to the place in the kit where you did the thing. Answer in under a minute, at level three (the number or the mechanism, what moved it, how sure you are). Tags are this programme's own calibration for 0 to 3 year Indian-market roles: [S] staple asked everywhere, [F] frequent in GCC and product screens, [SV] service-major screen opener, [D] differentiator.

## Brief A · H1 volume and plan

| Tag | Question | Where you did it | What a good answer covers |
|---|---|---|---|
| [S] | How did you reproduce the handbook's 5% test-volume growth? | Notebook 01, `docs/project-analysis.md` | Count each nonblank active booking-test line by scheduled test date (`slot_at`) for Jan–Jun in both years. H1 2025 = 435,880; H1 2026 = 457,539; reported actual growth = 5%. Exclude 3,541 superseded H1 2026 reschedule lines. |
| [F] | Why use scheduled date rather than booking creation date? | `docs/approach-log.md`, `outputs/brief_a_h1_overall.csv` | The city plan has monthly test-volume targets, so scheduled month aligns the actual cohort to the target month. Confirm with the plan owner that the target is scheduled volume. |
| [F] | How far below plan were you, and what drove the net growth? | `docs/project-analysis.md`, `outputs/brief_a_h1_channel_by_city.csv` | Plan = 515,740, or 18% estimated growth against the 2025 scheduled baseline; actual attainment = 88.72%, short by 58,201 lines. Home grew 55,696 (+37.39%) while clinic fell 34,037 (-11.86%), netting +21,659 (+5%). Every city and month missed plan. |
| [D] | Does the result-date join tell you how many tests were completed? | `outputs/brief_a_h1_result_date_summary.csv` | No. About 81% of active scheduled lines match an H1 result timestamp; result timing, source coverage and legitimate no-result outcomes can affect that match. Treat it as a coverage diagnostic, not a completion rate or an alternative plan measure. |
| [F] | Did Nova cause the H1 miss? | `docs/brief-a-b-analysis.md`, `outputs/brief_a_b_period_summary.csv` | The data do not establish causation. The treated cities had different pre-period growth, only two cities migrated, and the scheduled-date pre-adjusted estimate is +1.93 percentage points. It is descriptive and should not be framed as a causal effect. |

## pandas

| Tag | Question | Where you did it | What a good answer covers |
|---|---|---|---|
| [S] | What does `merge(how='left', validate='one_to_one', indicator=True)` do, and why would you set all three? | Notebook 01 | LEFT keeps every left row; validate raises on a cardinality violation instead of fanning out silently; indicator shows which side each row came from, which is the anti-join check. |
| [S] | Your join grew the row count. What happened and how do you find out? | Notebook 01, `checks.join_did_not_fan_out` | The right key repeats. Group the right side by key and count; separate retries, true duplicates and a wrong key. |
| [F] | When is `category` the right dtype, and when is it the wrong one? | Notebook 01, `loaders.LEGACY_DTYPES` | Low-cardinality columns: memory and groupby speed. Wrong for ids, and a trap on concat with different category sets. |
| [F] | `groupby().apply()` was slow. What did you do instead? | Notebook 01, `records_from_rows` | Sort once, find group boundaries with `np.unique(return_index=True)`, slice; or use named aggregations and vectorised string ops. Measure before and after. |
| [F] | How do you read a CSV too large for memory? | `notebooks/_scripts/kalpa/loaders.py` | `chunksize`, aggregate per chunk, or filter columns with `usecols` and declare dtypes; or load into a database and query. |
| [D] | Explain `observed=True` in a groupby on categoricals. | Notebook 01 | Without it pandas emits every category combination, including empty ones, which pads results and slows the aggregation. |
| [S] | Mean or median for order value, and why? | Week 1 | A single bulk order drags the mean; the median describes the typical visit. Report both when they disagree, and say why. |
| [D] | What is the difference between `NaN`, `None`, `pd.NA` and `NaT`, and when did it bite you? | 02, 03 | Float NaN, Python None, the nullable-dtype missing marker, and the datetime missing marker; equality tests fail on all of them, so use `isna()`. |

## NumPy

| Tag | Question | Where you did it | What a good answer covers |
|---|---|---|---|
| [F] | What is broadcasting, with an example from your work? | Notebook 01 | Arithmetic between arrays of compatible shapes without copying, such as dividing test counts by visit counts across a column. |
| [D] | Why is the log decomposition of growth exact when the percentage one is not? | Notebook 01, growth tree | `log(a·b·c) = log a + log b + log c`, so growth in a product is the sum of log growths; percentages only add approximately for small changes. |
| [S] | What does setting a seed buy you, and what does it not? | Notebook 01, CONFIG | Reproducible random draws for the same code and library version; it does not make the analysis correct, and a different NumPy version can change the stream. |

## Pydantic and Python

| Tag | Question | Where you did it | What a good answer covers |
|---|---|---|---|
| [F] | What does a pydantic model give you that a DataFrame check does not? | `notebooks/_scripts/kalpa/models.py` | One named contract per record; per-field reasons on rejection; explicit normalization. Cost: per-record Python time, so validate at the boundary. |
| [F] | `field_validator` against `model_validator`: when each? | `notebooks/_scripts/kalpa/models.py` | Field: one value in isolation (an id shape, a case fold). Model: a rule across fields (slot not before creation). |
| [S] | Why a process pool rather than threads for parsing files? | `notebooks/_scripts/kalpa/loaders.py` | CPU-bound work under the interpreter lock runs one thread at a time; processes have their own interpreter. Threads help with I/O waits. |
| [F] | What is a generator and where did you use one? | Notebook 01, `records_from_rows` | A function that yields items lazily, so records need not all be held in memory at once. |
| [D] | How did you make the analysis reproducible? | Notebooks 01–02 | Run the notebooks from a fresh kernel; regenerate clean tables and aggregate outputs from the raw/local pack; keep private row-level files out of Git. |

## Data and statistics

| Tag | Question | Where you did it | What a good answer covers |
|---|---|---|---|
| [S] | The dashboard and Finance disagree. What do you do first? | Notebook 01 and Notebook 02 | Profile both, agree the period and definition, reconcile input = matched + unmatched, then classify the gap into timing, unmatched and amount. |
| [F] | Two systems export the same entity with different ID formats. How do you reconcile them? | Notebook 01; `notebooks/_scripts/kalpa/loaders.py` | Trace examples through both, write the mapping rule, check uniqueness and before/after counts, and list what does not map. |
| [D] | Your bridge balances. Name one way it could balance and still be wrong. | Notebook 02 | Two errors can cancel: a mis-keyed payment counted on the wrong invoice while that invoice's own payment is missing. |
| [F] | Which Finance queue would you investigate first, and why? | Notebook 02, `docs/brief-c-analysis.md` | June had 6,256 positive-balance invoices totaling ₹1.053 crore at H1 close (54.1% of the close balance). Then review 1,541 unmatched captures worth ₹26.68 lakh, led by UPI. These are priorities, not proof of loss or cause. |

## The project itself

| Tag | Question | Where |
|---|---|---|
| [S] | Walk me through the analysis you did on unfamiliar data and one decision you would defend. | approach-log |
| [S] | You have joined a healthcare company; how would you apply what you did in retail to our data? | project-statement, section 5 |
| [F] | What changes when the cost of an error is a missed diagnosis rather than a missed sale? | project-statement, section 5 |
| [F] | What broke, and what did you do? | challenges-log |
| [D] | State your finding in one sentence a COO can carry into a board meeting. | slide 3 |
| [D] | What would make you wrong? | slide 5 |

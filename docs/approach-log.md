# Approach log · Brief c · Group 10

One row per part of the work. At least two approaches in every row. Written when the choice is made, not afterwards; the commit timestamp is the proof. An approach you tried for twenty minutes and abandoned is the best kind of row. Keep the dead notebook cell and link to it.

The panel reads this file before it reads your notebooks. A panellist will cover the "chosen" column and ask you to choose again, aloud.

| # | Part of the work | Approaches considered (two at least) | Chosen | Why this, and not the others | What would have changed the choice | What happened when we tried it | Owner | Date |
|---|---|---|---|---|---|---|---|---|
| 0 | *Example: matching invoice ids to payment references* | *(a) Strip the prefix and match on digits. (b) Match on amount and date within two days. (c) Both, and keep the rows where they disagree.* | *(c)* | *(a) alone matched 91 percent and silently paired two invoices with one payment. (b) alone could not separate same-day same-amount visits. Together they flag what each misses.* | *A shared id in both feeds would have made (a) enough.* | *96 percent matched. The 4 percent became finance's list.* | *example* | *example* |
| 1 | Which table to count tests from | | | | | | | |
| 2 | How to define the period (first half, both years) | | | | | | | |
| 3 | Profiling: what to check in each table | | | | | | | |
| 4 | Duplicates: the identity rule | | | | | | | |
| 5 | Missing values: drop, default, or keep and flag | | | | | | | |
| 6 | Each join: type, key, validation | | | | | | | |
| 7 | The method (tree / ladder / bridge / shuffle / comparison) | | | | | | | |
| 8 | The segmentation (city, channel, type) | | | | | | | |
| 9 | The chart that carries the claim | | | | | | | |
| 10 | The one sentence | | | | | | | |

|10|Handling Notebook 02's repeated kernel crashes|A: Continue troubleshooting Notebook 02. B: Proceed to Notebook 03's independent invoice-payment section|Approach B|Notebook 02 repeatedly crashed, while Notebook 03 could load invoices and payments directly from data/raw/|If Notebook 03 required the missing booking outputs from Notebook 02, continuing with Notebook 02 would have been necessary|Notebook 03's financial section successfully loaded 470,776 invoices and 473,507 payment records. The full pipeline is still incomplete|vysagk|2026-10-24|
|11|Initial invoice and payment investigation|A: Compare total invoice and payment counts. B: Separate captured/failed payments and investigate invoice-payment matches|Approach B|on approach A,their counts will not conclude more payments means more collection|if only one payment is allowed for each invoices then the approach would give much better data|invoices - 470776,payements- 473507(captured 455469,failed 18038). Also the difference of 2731 between count doesnt make sense that collections are more|vysagk|2026-10-24|
|12|Handling multiple payments per invoice|A: Join invoice rows directly to individual payments. B: Group captured payments by invoice reference before comparing amounts|Approach B|when we count the amount after join,it give wrong data, since there is multiple payments for single invoice ie repeated invoice counts|if it was one on one relations|we have 1925 invoices that reffers multiple payements |vysagk|2026-10-24|
|12|Choosing the reporting period for financial comparison|A: Compare all available invoice/payment records. B: Use a defined reporting period and examine later payments separately|A for the preliminary investigation; B identified as necessary for an H1-specific analysis|The initial full-data totals helped identify the overall discrepancy, but did not isolate H1|Establishing the H1 reporting requirement before calculating totals|Full-data difference of ₹2,45,30,936 was observed; H1-specific difference remains uncalculated|vysagk|2026-10-24|

1
## Parts we never had to choose about

<List any part where only one approach was possible, and say why. The panel will ask whether that was true.>

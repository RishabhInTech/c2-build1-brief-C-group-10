# Challenges log · Brief c· Group 10

What broke or surprised us, what we tried, what we changed and why. Entries are dated and written as they happen. A log written on the last evening answers no interview question, and the commit history shows which kind this is.

| # | Phase | What broke or surprised us | What we tried first | What we changed, and why | What we would do differently next time | Who | Date |
|---|---|---|---|---|---|---|---|
| 0 | *Profile and clean* | *Our first join of invoices to payments returned almost no matches.* | *Printed ten ids from each file side by side.* | *Wrote a mapping rule from invoice id to payment reference; kept unmappable rows in a separate list.* | *Profile id formats before writing any join.* | *example* | *example* |
| 1 | Data setup | The SHA-256 verification failed when I checked the files. | I compared the current manifest with the manifest inside the original ZIP file. | I restored the original manifest and refreshed the files from the ZIP. After that, the integrity checks passed. | Next time, I will verify the files after switching Git branches or changing the data setup. | vysagk | 2026-10-24 |
| 2 | Load and Validate — Notebook 02 | The Python kernel kept crashing while validating the booking data. | I checked RAM, disk space, memory events and Python imports to understand the issue. | I changed the workers from `None` to `2` to see if it would stop crashing. But the kernel still crashed, so the exact reason is not confirmed. | Next time, I will try validating smaller batches and monitor memory usage. | vysagk | 2026-10-24 |
| 3 | Clean and Reconcile — Notebook 03 | Section 5 stopped with the error `NameError: bookings is not defined`. | I checked whether `inv`, `pay` and `bookings` were available. | I found that invoice and payment data were available, but bookings was missing. So I ran the existing invoice and payment export lines separately. I verified 470,776 invoice rows and 473,507 payment rows. The full notebook is still incomplete. | Next time, I will check whether the required variables are available before running the export section. | vysagk | 2026-10-24 |
|4|Brief C — Financial analysis|The initial comparison used all available invoice and payment dates, rather than only H1 2026|Compared overall invoice and captured-payment totals|Checked the date ranges and separated July captured payments to understand the timing difference|Define the reporting period before calculating invoice and payment totals|vysagk| 2026-10-24 |

## The entry we are proudest of

<One paragraph on the problem that taught the group the most. This is the story each of you tells in the viva.>

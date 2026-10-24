# Assistant log · Brief c · Group 10

Every use of a coding or chat assistant, one line each. Allowed uses: explaining an error you already tried to read, explaining a concept you then rewrite in your own words, checking English in the write-up without changing meaning. Not allowed: generating analysis, notebooks, cells, charts, slides, write-ups or the video script; asking what the answer or approach should be; pasting Kalpa Health data in.

An empty log next to notebooks that read like a tutorial is a claim the panel will test. Twenty honest lines are fine.

| # | Date | Who | Tool | What we asked (one line) | What we did with the answer |
|---|---|---|---|---|---|
| 1 |oct 24,2026 |vysagk |chatgpt |we asked chatgpt to troubshoot the sha256 error fail | ChatGPT helped troubleshoot Git, ZIP extraction and the SHA-256 failure|
|2|oct 24,2026 |vysagk |ChatGPT |Explanation and troubleshooting of the Notebook 02 kernel failure|Checked memory, disk and OOM logs; restarted the kernel; tested two workers; documented that the issue remained unresolved|
|3|2026-10-24|vysagk|ChatGPT|Explanation of invoice-payment matching and one-to-many relationships.|Understood why multiple payments can match one invoice and why transaction counts don't establish total collections.|
|4|2026-10-24|vysagk|ChatGPT|Explanation of NameError: bookings is not defined in Notebook 03.|Ran a temporary diagnostic cell and confirmed inv=True, pay=True, and bookings=False.|
| 5 | 2026-10-24 | vysagk | ChatGPT | Asked about exporting invoice and payment files when Notebook 03 Section 5 failed | Ran the existing export statements separately and saved both financial CSV files |
| 6 | 2026-10-24 | vysagk | ChatGPT | Asked how to verify the exported invoice and payment files | Verified 470,776 invoice rows, 473,507 payment rows, unique IDs, and captured/failed payment counts |
| 7 | 2026-10-24 | vysagk | ChatGPT | Asked for grammar, formatting and factual review of project logs | Reviewed the corrections and updated the documentation to reflect completed work and unresolved issues |
|8|2026-10-24| vysagk | ChatGPT |Explanation of the invoice–collection difference, payments captured after June 30, and the reporting-period limitation|Checked captured-payment dates and totals, identified 1,794 July transactions worth ₹30,44,791, and understood that the analysis covered the full dataset rather than H1 alone|

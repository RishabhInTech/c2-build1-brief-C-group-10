# Challenges log · Brief C · Group 10

What broke or surprised us, what we tried, what we changed and why. Entries are dated and written as they happen. A log written on the last evening answers no interview question, and the commit history shows which kind this is.

| # | Phase | What broke or surprised us | What we tried first | What we changed, and why | What we would do differently next time | Who | Date |
|---|---|---|---|---|---|---|---|
| 1 | Reconciliation and validation | Some successful payment records did not match any invoice, even after normalising invoice references. | Normalised invoice IDs and payment references, then checked the unmatched payment records. | Kept unmatched payments in a separate report instead of dropping them, so they could be investigated. | Check reference formats and validate join results before calculating outstanding balances. | Me | 2026-10-24 |
## The entry we are proudest of

<One paragraph on the problem that taught the group the most. This is the story each of you tells in the viva.>

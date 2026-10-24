
# Project Statement — Brief C: Money
**Group 10**

## 1. Dr. Menon's Words

> “Which invoices were never paid, which payments match no invoice, and how much of the gap is only timing?”

— Dr Priya Menon, COO, Kalpa Health

## 2. The Question in Our Words

Kalpa Health's billing system records one invoice per visit, while payments arrive through cards, UPI and cash deposits at clinics. The billing and payment systems use different ID formats, and they have not been reconciled since the payment gateway was switched.

Our task is to explain the difference between the amount invoiced and the amount collected, identify invoices with no payment and payments that match no invoice, and determine how much of the difference is explained by payments arriving after the quarter ended.

## 3. The Question Dr. Menon Did Not Ask

[Our group will identify one additional question that could affect the finance controller's decision and explain why it matters.]

## 4. Translation into the Method

| Business question or phrase | Method or concept | What we need to establish |
|---|---|---|
| Which invoices were never paid? | Invoice-level reconciliation | Identify invoices with no matched payment and calculate their count and amount. |
| Which payments match no invoice? | Payment-to-invoice matching | Identify payment records that cannot be linked to an invoice and calculate their count and amount. |
| How much of the gap is only timing? | Quarter-end timing analysis | Identify payments received after the quarter closed and determine how much of the quarter-end gap they explain. |
| Do both sides reconcile? | Reconciliation and validation | Check that the invoiced-to-collected bridge is supported by counts and amounts on both sides. |

[Confirm the method names against the methods taught in Week 1 and Week 2.]

## 5. What Does Not Transfer from Retail

| Retail context | Kalpa Health context | Why the difference matters |
|---|---|---|
| A missed sale may represent one order that was never completed. | An invoice may remain unpaid even after a visit has taken place. | We need to distinguish an unpaid invoice from a payment that arrived later. |
| A shopper chooses a basket of products. | A visit generates an invoice, and payment may arrive through a gateway or as a cash deposit at a clinic. | We must reconcile invoice records with payment records rather than assume that one transaction ID connects them directly. |
| Sales and payment records may be compared using a shared order reference. | Billing and gateway IDs look different, and settlement records can group multiple payments. | Matching rules must be documented and validated rather than relying on ID equality alone. |

## 6. Our Prediction Before Opening the Data

**Date:** [Enter the actual date the group recorded its prediction.]

Before opening the data, we predicted that [write the group's original prediction about the main cause of the invoiced-to-collected gap].

We expected this because [write the reason discussed by the group before examining the data].

This prediction will remain unchanged. After the analysis, we will compare it with the findings and explain whether the evidence supports it.

## 7. Requirements

### Functional Requirements

| ID | Requirement | Evidence of completion |
|---|---|---|
| F1 | Reproduce Dr. Menon's 5% figure or explain why our result differs. | Document the original definition, calculation, denominator and any differences. |
| F2 | Answer the main question with a number and a denominator. | Report the relevant counts and amounts and explain exactly what each number represents. |
| F3 | Provide an actionable list or breakdown. | Produce traceable records of unpaid invoices and payments that match no invoice, with the relevant amounts. |
| F4 | Explain the timing component of the gap. | Quantify payments received after quarter-end that relate to invoices from the quarter, using a documented definition. |

### Non-Functional Requirements

| ID | Requirement | Evidence of completion |
|---|---|---|
| N1 | A cold run in Codespaces must take under 10 minutes. | Record the runtime of a clean run without manual edits. |
| N2 | All reported numbers must be auditable. | Trace each result to source records and documented calculations. |
| N3 | Cleaning decisions must be recorded. | Maintain a dated log of cleaning rules, reasons and their effects. |
| N4 | The reconciliation must be reproducible. | A teammate should be able to follow the documented process and reproduce the reported results. |

### Constraints

| ID | Constraint |
|---|---|
| C1 | Use the tools permitted by the course. |
| C2 | Follow the assignment's restrictions on coding assistants, chat assistants, analysis, notebooks and write-ups. |
| C3 | Use the data as released and work within the assigned timeline and group size. |
| C4 | Do not claim that a payment reached the bank unless the available evidence verifies it. |

## 8. Scope

### In Scope

- Reconcile invoice records with payment records.
- Identify invoices with no matched payment.
- Identify payments that match no invoice.
- Quantify the difference between invoiced and collected amounts.
- Investigate whether payment timing explains part of the quarter-end gap.
- Check settlement records for duplicate or inconsistent entries where the available data permits.
- Report counts and amounts for every bar in the invoiced-to-collected bridge.
- Document matching rules, cleaning decisions and validation checks.

### Out of Scope

- Assuming every unmatched payment is lost money.
- Assuming every unpaid invoice is permanently uncollectible.
- Claiming that settlement records prove bank receipt without bank-level evidence.
- Making unsupported conclusions about fraud or deliberate misconduct.
- Extending the analysis beyond the available data and the agreed project scope.

## 9. Done Looks Like

The project is complete when finance has a bridge from invoiced to collected, with every bar labelled by both count and amount, the two sides reconcile, and the results provide a list of records that finance can investigate.

**Our completion check:** [Record the final reconciliation checks, unresolved differences, and evidence that the reported counts and amounts can be reproduced.]

## 10. Who Signs Off?

| Stakeholder | What they need to verify |
|---|---|
| Dr. Priya Menon, COO | The analysis answers the business question and explains the invoiced-to-collected gap. |
| Finance controller | The counts and amounts reconcile, the calculations are auditable, and the investigation list is usable. |
| Relevant clinic or city managers | The records assigned for follow-up are understandable and actionable. |
| Group 10 | The analysis is reproducible, the assumptions are documented, and the final results are supported by the data. |

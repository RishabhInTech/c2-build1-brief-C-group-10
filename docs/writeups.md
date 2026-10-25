# Individual write-up · Brief C · Group 10

## Group summary

We began by checking the handbook's H1 volume figure, then profiled and cleaned the booking data and used Briefs A and B to understand where the change was coming from. Counting active booking-test lines by scheduled test date gave 435,880 lines in H1 2025 and 457,539 in H1 2026: growth of 4.97%, which rounds to the handbook's 5%. That is well below the plan's implied 18.32% growth. The city, month, channel, and migration cuts helped us describe the gap, but they do not prove what caused it.

We selected Brief C as the main question because it gives the COO a practical Finance decision to take to the board. At 30 June, 11,586 invoices had ₹1.947 crore in positive balances; by 15 July, ₹1.648 crore remained open across 9,824 invoices. Separately, 1,541 H1 captured attempts worth ₹0.267 crore lacked a safe invoice match. We recommend that Finance review the open-balance and unmatched-capture lists before treating any amount as lost. The numbers are auditable, but the conclusion remains provisional until Finance confirms source completeness, due dates, reversals, and bank or cash evidence.

---

## Rishabh

**1. In your own words, what was Dr Menon asking for, and what did she actually need?**

Dr Menon wanted a clear answer about unpaid invoices, payments without invoice matches, and the effect of late receipts. She needed a bridge she could explain without mixing different populations. We show positive balances at 30 June, what remained open on 15 July, and unmatched H1 captures separately. These are Finance follow-up queues, not proof that customers will never pay.

**2. Which part of the work was yours, and what did you produce that the group now depends on?**

I coordinated the analysis, worked through the booking data and H1 growth definition, and built the Brief C cleaning and reconciliation workflow. We first established the 5% volume result, used Briefs A and B as context, then made Brief C the board answer. The two notebooks follow that sequence.

**3. Which approaches did you consider for your part, which did you choose, and why not the others?**

For growth, I compared booking-created date, scheduled test date, and result date. Scheduled date (`slot_at`) best matched the monthly plan and reproduced 4.97%, rounding to 5%. Booking-created date gives a 3.49% sensitivity; result date describes a later event. For invoice matching, I considered exact IDs, fuzzy amount/date matching, and a limited canonical rule. I chose exact matching first, then hyphen removal only when the invoice key was unique. Fuzzy matching could create wrong links, so uncertain cases stay visible for Finance.

**4. Which number do you trust most, what is its denominator, and what would make you stop trusting it?**

I trust the 4.97% growth figure because I can reproduce it: 457,539 active scheduled test lines versus 435,880 in H1 2025. The 2026 count excludes 3,541 superseded reschedule lines. I would revisit it if the plan owner defined another date or grain, or if source files were missing. The invoice balance is auditable too, but has more timing and source caveats.

**5. What broke, what did you try, and what did you change? Point at the challenges-log entry.**

An analysis helper expected plain `bookings.csv` and a long-format plan, but the notebook produced a compressed booking-test export and the supplied plan was wide. I checked the schemas, updated the readers, and reshaped the plan. The analysis now reproduces the aggregate tables. An earlier finance full-pack run was terminated, so that workflow has a passing synthetic test but still needs a fresh full-pack notebook run. See the [challenges log](./challenges-log.md).

**6. What do you understand about a diagnostics business now that you did not before?**

A booked test is not automatically completed, and a payment attempt is not automatically settled. Each event has its own date and grain. Results can be at booking-test level while collections are at booking level, so the wrong denominator misleads. An open invoice is not necessarily overdue or lost when due dates, reversals, or independent cash evidence are missing.

**7. Where did the team work well, where did it not, and what would you change for Build 2?**

We checked the numbers against their definitions, kept row-level Finance data out of Git, and tested matching rules on a small fixture. Integration was weaker: a helper expected a different file shape, and the full notebook cold run remains incomplete. For Build 2, I would agree on schemas, owners, and denominators early, then run the notebooks from a clean environment before polishing slides.

**8. Which idea from Weeks 1 and 2 do you understand better after using it on this data, and what was fuzzy before?**

I understand data grain more concretely. “Count the rows” sounds simple until one system stores one row per booking-test and another nests several tests in a booking. I also see why joins need row-count checks and match rates need explicit denominators. Those ideas mattered when they changed a headline or Finance follow-up list.

**9. Which viva question would you least like to be asked, and what is your answer to it?**

I would least like to be asked whether migration caused the volume shortfall. The comparison is descriptive: only Chennai and Jaipur migrated, their pre-period trends differed from the comparison cities, and local changes are not controlled for. I can report the pattern and its limits, but cannot claim Nova caused the plan miss.

**10. If you had two more days, what would you do first, and why that?**

I would first run both notebooks sequentially from fresh kernels, including the finance pack. Then I would ask Finance to confirm the plan date, due dates, reversal coverage, and bank or clinic-cash evidence. Those checks could change the board conclusion, so they matter more than another chart.

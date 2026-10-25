# Questions to ponder

These questions build the depth the viva tests. Read the whole file once in Scope. Then return to the section for the phase you are in, and write your answers into the logs, not into your head. A question you cannot answer yet goes on the task board as a card.

The point of asking is to find out where your understanding stops. Everyone's stops somewhere. The panel wants to see that you know where yours does.

## How to use the levels

Every question can be answered at five levels. The levels come from the five-whys habit: each level is the answer to "why" asked of the level before. Aim to reach level three on everything, and level five on the one or two things your claim rests on.

| Level | What you can say | Example, brief A |
|---|---|---|
| 1 · Report | The number. | "Active scheduled test lines grew 4.97 percent, which rounds to the handbook's 5 percent: 457,539 versus 435,880." |
| 2 · Explain | What moved it. | "Home lines rose by 55,696 (+37.39%) and clinic lines fell by 34,037 (-11.86%), leaving net growth of 21,659 (+4.97%)." |
| 3 · Confidence | How sure you are, and why. | "The measure is one nonblank booking-test line by `slot_at` month, excludes 3,541 superseded reschedule lines, and compares the same six months. Booking-created-date growth is 3.49%; H1 result-date matching is about 81%, so this is scheduled volume, not confirmed completed volume." |
| 4 · Decide | What to do, and the cost of being wrong. | "Review the plan and investigate Jaipur (76.79% attainment and -10.82% YoY) plus Chennai (the largest absolute city shortfall, 13,194 lines); check clinic demand/capacity and booking-to-result coverage before choosing an intervention. If the plan actually targets completed tests, a scheduled-line comparison could direct action at the wrong gap." |
| 5 · System | Why the organisation produced this problem, and what would stop it recurring. | "A single H1 total hides that home growth is offsetting clinic declines and that every city and month missed plan. Track scheduled volume against plan monthly by city and channel, with a separately defined result-date completion measure and an owner-triggered forecast review; these data describe the gap but do not establish its cause." |

### Brief A · defensible answer

**Board answer:** “H1 active scheduled test volume grew **4.97% (rounds to 5%)**, from **435,880** to **457,539** lines, versus **18.32% implied growth** in the six-city plan. That is **88.72% plan attainment** and a shortfall of **58,201 lines**. Home growth partly offset clinic declines; every city and month still missed plan. We should investigate the clinic decline and the weakest city-plan attainment, while confirming that the plan targets scheduled tests rather than completed lab results.”

Do not call the 13.35 percentage-point difference a causal effect. It is actual growth minus growth implied by plan. Do not claim Nova caused the miss: the migration comparison is descriptive, involves two cities, and has different pre-period trends. The result-date join is a coverage diagnostic, not a completion rate.

---

## Before you open any data (Scope)

### About the business

- What does Kalpa Health sell, who pays for it, and when does the money arrive relative to the service?
- Which of the three numbers in the tree (patients, tests per patient, revenue per test) does Dr Menon's board actually care about, and why that one?
- What does the plan of 18 percent rest on? Who set it, on what data, with what incentive?
- Who in the company loses if your answer is right? Who loses if it is wrong? Have you heard either side?
- What would Dr Menon do differently depending on your answer? If nothing, why is she asking?
- What question did she not ask that she will wish she had?

### About the data

- Which step of the patient journey does each table record? What can that step never tell you?
- Which table is the source of truth for a count of tests, and what makes it so rather than the others?
- What would you expect the row counts and date ranges to be, before looking? Write the guess down.
- Which identifier should link tables, and what will you do when it does not?

### About the method

- Which Week 1 or Week 2 method answers this brief, and what would make it the wrong one?
- What is the smallest version of the analysis that would still answer the question? Could you do it in Excel on a hundred rows?
- What is the denominator of the headline number you expect to produce?

### About the team

- Who owns which part, and what does each part hand to the next?
- What will you do when two of you disagree about a decision?
- What is the first thing that will go wrong, and who will notice?

---

## While profiling and cleaning

### About each table

- How many rows, how many distinct keys, and why do the two differ?
- What share of each column is empty, and is the emptiness random or does it cluster in a city, a month, a system?
- Which columns are text that should be numbers, and what happens to a sum when they stay text?
- What is the earliest and latest date, and does that match the stated time window?
- Which values appear far too often? Which appear exactly once?

### About each decision

- Is this a drop, a default, or a keep-and-flag? What does each do to the headline number?
- Could this rule reject a true row? What would such a row look like?
- Could this rule keep a false row? What would it look like?
- Would the finance controller accept this rule if it were read aloud to her?
- Did input equal clean plus rejected after this step? Did you print both sides?

### About each join

- What question does this join answer: matches only, all of the left, or both sides' orphans?
- What did the row count do, and can you explain every row of the difference?
- Which keys matched more than once, and is that a retry, a real duplicate, or a different entity sharing an id?
- If you had used the other join type, which rows would have vanished, and would anyone have noticed?

### About the identity of things

- When are two bookings the same booking? Write the rule as one sentence.
- When are two patients the same patient?
- When is a payment the payment for this invoice?
- Which of these rules did you invent, and which did the data force on you?

---

## While analysing

### About the comparison

- Compared with what? Same window, same segments, same denominators?
- Is the denominator the thing that was actually at risk of the outcome?
- What would this number be if nothing had changed? That is your baseline. Did you compute it?
- Could the aggregate move one way while every part moves the other? Have you checked?

### About chance

- How often would a difference this large appear by chance alone with numbers this small?
- What does your shuffle assume that might not be true here?
- How many more rows would it take to settle the question, and is that number large or small?
- Is "statistically real" the same as "worth acting on" here? What is the smallest difference Dr Menon would act on?

### About cause

- What else could explain this besides the cause you are testing? Name two.
- Who received the treatment, and were they already different before it?
- What comparison would convince the person who disagrees with you?
- If you could run one experiment next quarter, what would it be?

### About the tree, the ladder, the bridge

- Do the branches multiply back to the total? If not, which branch is missing?
- Which rung of the ladder are you on, and have you really finished the rung below?
- Does every bar in the bridge have a count and an amount, and do both sides reconcile?

---

## While writing the claim

- Can Dr Menon say this sentence aloud to her board without being caught out?
- Does it carry a number, a denominator and a period?
- What is the one caveat that would change it? Is that caveat on the slide?
- What is the action, what does it cost, and what does being wrong cost?
- Which alternative explanation have you ruled out, and which have you only made less likely?
- If a second group with the same data reached a different claim, what would they have done differently?

---

## While preparing to defend

- Which number are you least sure of? What will you say when asked about it?
- Which approach-log row would you least like the panel to pick? Why?
- What did you reject that a reasonable person might have chosen?
- Which of your teammates' parts could you explain alone? Which could you not? Fix the second list before the presentation.
- What did you learn about the business that you did not know before? Say it in one sentence.
- What would you do with two more days, and why that first?

---

## Questions for each aspect, at every stage

Ask these of every part of the work, every time. They are short on purpose.

| Aspect | Ask |
|---|---|
| Business | Who decides, what do they decide, what does it cost them to decide wrong? |
| Data | Which step recorded this, and what can that step not see? |
| Statistics | Compared with what, over what period, with what denominator, how often by chance? |
| Engineering | Would this run again tomorrow, on a fresh machine, by someone else, and give the same number? |
| Ethics | Who is named or ranked by this number, and have they been compared fairly? |
| Team | Who else can explain this, and is it written where they can find it? |
| Self | What am I assuming without noticing, and what would show me I am wrong? |

---

## Systems questions

The analysis is of one half-year. The problem is older. Ask these once, late in the project, and put the answers in your write-up.

- Why did the organisation not already know the answer to this brief?
- Which measurement, report or incentive produced the blind spot?
- What one change to how Kalpa Health measures itself would make this brief unnecessary next year?
- What would that change cost, and who would resist it?
- Where else in the company does the same blind spot probably exist?

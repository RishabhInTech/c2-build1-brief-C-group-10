# Build 1 · Brief C · Invoice-to-capture reconciliation · Group 10

Dr Menon asks which H1 invoices have no captured payment, which captured attempts cannot be matched to an invoice, and how much of the difference reflects timing. Group 10 first checked test-volume growth and explored Brief A/B, then selected Brief C for the board-facing Finance question. Counting active test lines by scheduled date gives **5% actual growth**, against **18% estimated growth** in the plan; the invoice bridge shows what remained open at close and at the later observation cutoff.

## The claim

Test volume grew **5%**; estimated growth in the plan was **18%**. At H1 2026 close, 11,586 of 162,876 invoices (**₹26.828 crore billed**) carried **₹1.947 crore** in positive balances. June accounted for **₹1.053 crore (54.1%)** across 6,256 invoices. By 15 July, **₹1.648 crore** remained open across 9,824 invoices. Separately, 1,541 H1 captures worth **₹26.68 lakh** lacked a safe invoice match; Finance should prioritize June and resolve both exception lists before calling balances lost.

## Members and parts

| Member | Part of the work owned | Notebooks | Approach-log rows |
|---|---|---|---|
| Rishabh | Group 10 analysis coordination, data cleaning, and Brief C reconciliation | 01, 02 | 1–6 |

## How to run

1. Open this repository in a GitHub Codespace.
2. Run `notebooks/01_h1_growth_and_brief_ab.ipynb` from a fresh kernel to profile, load and clean the booking data, then reproduce the scheduled-volume and Brief A/B supporting analysis.
3. Place the approved finance data pack at `data/Build1_DataPack.zip` locally (it is not committed), then run `notebooks/02_brief_c_board_answer.ipynb` from a fresh kernel. The last section prints the bridge and board sentence.
4. The H1 volume result is **5% actual growth** (457,539 / 435,880 active scheduled test lines); the plan estimates **18% growth**. A full-pack cold run has not been timed in a fresh Codespace.

Generated row-level clean data and Finance action lists stay local under the Git-ignored `data/clean/`. Only aggregate outputs are committed.

## Links

| What | Where |
|---|---|
| Video | (https://drive.google.com/drive/folders/13XBpoXcJH9BwpqQXavWTx53xnhjyM8pR?usp=sharing) |
| Slides | [`slides/Group10_Brief_C.pptx`](slides/Group10_Brief_C.pptx) |
| Task board | [GitHub Issues](https://github.com/RishabhInTech/c2-build1-brief-C-group-10/issues) |
| Data pack provenance | [`data/raw/README.md`](data/raw/README.md) |

## The logs

[`docs/approach-log.md`](docs/approach-log.md) · [`docs/decisions-log.md`](docs/decisions-log.md) · [`docs/challenges-log.md`](docs/challenges-log.md) · [`docs/writeups.md`](docs/writeups.md) · [`docs/ai-log.md`](docs/ai-log.md)

## Working agreement

Work on the Group 10 branch and review changes before sharing them. Keep row-level clean finance data and action lists out of GitHub, clear notebook outputs before committing, and keep every reported number tied to its denominator and period.

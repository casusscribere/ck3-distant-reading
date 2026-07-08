# Ted Underwood's distant-reading critique

Reference: Ted Underwood, "A Genealogy of Distant Reading," *Digital Humanities Quarterly* 11.2 (2017). https://digitalhumanities.org/dhq/vol/11/2/000317/000317.html

## The core caution

Underwood warns that distant reading discovers **patterns**, not **arguments**. Word frequencies tell you what a corpus discusses, not what the corpus claims. A high frequency of "authenticity" in a corpus on game studies (the Week 3 case) does not mean the corpus endorses authenticity — it means the corpus argues about authenticity, often skeptically.

## The Underwood pass in this skill

`06_underwood_verify.py` operationalizes the caution. For each top claim:

1. The top three terms by raw frequency
2. The top three concept-network edges by PMI
3. The top three trigrams by document frequency

The script retrieves 3–5 representative passages from the corpus by grep. The report displays the passages alongside the claim and asks the analyst:

> Do these passages support the claim, or do they show the corpus discussing the term in a way that complicates a naive frequency interpretation?

## What this catches

The Week 3 corpus's most important finding — that the corpus *critiques* authenticity rather than endorses it — was invisible at the word-frequency level and only emerged through Underwood-style passage-grounding. Without the verification step, the report would have implied the opposite of what the corpus actually argues.

## What this cannot catch

Even with the verification step, distant reading still can't see:

- **Chronological evolution.** Texts from 2006 and 2024 are pooled into one bag.
- **Argumentative stance per se.** A word used in critique looks identical to a word used in praise. The verification only surfaces passages; the analyst must interpret them.
- **Citation lineage.** A text cited by 14 of the 45 documents in the Week 3 corpus (Friedman) is invisible at the word level if its own text is unreadable.
- **Voice and register.** What makes Hammar's Marxist critique read differently from McCall's pedagogical practice doesn't show up at any of these scales.

Document these limits in the report's final caveat section.

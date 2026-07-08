# Anastasia Salter's Week Four methodology

This skill follows the procedures in Salter's "Reading Across Texts" tutorial:
https://anastasiasalter.net/HumanitiesAI/weekfour.html

## The seven steps in Salter's tutorial

Salter's tutorial prompts:

1. *"I'd like to do some distant reading analysis of a novel. Can you help me through the process?"* — frame the request as scholarly work, not casual summarization.
2. *"I've attached the Project Gutenberg version of our text. Let's start by pre-processing it for analysis."* — preprocessing as Step 0.
3. *"Can you generate a bag of words?"* — Step 1.
4. *"Many of these are common words, can you apply a basic stopwords to remove things like I, the, do, is, our, etc?"* — Step 2.
5. *"Can you visualize the top words as a word cloud?"* — Step 3.
6. *"Using the bag of words and the cleaned text, could you make some determinations about the genre of this work and the themes?"* — Steps 4 and 5.
7. *"Can you visualize the network of character relationships in this text?"* — Step 6 (or concept network for non-fiction).
8. *"Can you visualize the most frequent phrases?"* — Step 7.

## What the skill adds

The skill makes three additions to Salter's bare sequence:

**The provenance-tagged Markdown corpus (Step 0).** Salter's tutorial delegates preprocessing to Claude in chat. The skill instead produces a citable corpus folder with YAML front-matter recording extraction method, page count, OCR confidence, and detected artifacts. The seven steps then run against the markdown corpus rather than against in-memory tokens. This makes results reproducible and auditable.

**The Underwood verification (Step 8).** Non-optional. Salter cites Underwood's 2017 *DHQ* article on distant reading; the skill operationalizes its central caution by grep'ing the corpus for representative passages of every top claim and surfacing them alongside the claim. See `underwood-critique.md`.

**The "what to be suspicious of" footer.** Every report ends with the curation-contingency caveat, the frequency-is-not-stance caveat, and the iterations-are-the-work caveat. Salter's tutorial implies these; the skill makes them explicit.

## Salter's framing of iteration

> "Depending on the text length, you might find that you need to work in sections or iterate your approach: keep refining until you are happy with your results."

This is the operative discipline. The skill's stopword passes, artifact taxonomy, network thresholds, and report regeneration are designed to support iteration rather than hide it.

# Best Practices from Anastasia Salter's *Humanities in the Age of AI*

*Synthesized from the course-level page and Weeks 1, 2, 3, 9, 10, 14, 15, plus the Final Reflection, at https://anastasiasalter.net/HumanitiesAI/. Companion document to `distant_read_writeup.md`, which records the Week 4 distant read of the NEH Week 3 corpus. Each practice below is followed by a candid note on how the previous distant read did or did not honor it.*

## Where the practices come from

Salter's course (ENG 6806, Fall 2025) is structured as three units — Textual, Visual, Procedural — built around primary readings (Mitchell, *Artificial Intelligence*; Bender & Hanna, *The AI Con*; Noble, *Algorithms of Oppression*; Littman, *Code to Joy*) and weekly making exercises. The exercises share a consistent pedagogical stance: the technical artifact is never the deliverable; the deliverable is the critique that grounds the artifact in theory. That stance shows up as a recurring set of methodological habits across the modules, summarized below.

## The recurring practices

### 1. Iterate, and document the iterations

Every text-focused exercise asks for at least five to ten iterations before you treat the output as final. Week 2 ("Interfaces") prescribes ten iterations on a generated poem. Week 4 says explicitly to "keep refining until you are happy with your results." Week 10 says use "at least five other prompts to refine the prototype." Week 1 asks you to compare model output across runs of the same prompt. The expectation is that the first output is a draft, not the answer. Crucially, the iterations are part of what you submit — Week 1 wants you to "document any frustrations and challenges as well as surprises along the way."

*How the Week 3 distant read fared.* This one we honored. The walkthrough recorded five distinct iterations: the JSTOR cover sheet that nearly erased McCall's paper, three rounds of stopword tuning, the TF-IDF surfacing of author surnames as false themes, and the trigram pass that was initially dominated by one e-book's DRM footer. Each correction is in the writeup. If anything we under-narrated the wordcloud and theme stages, which were largely first-pass — given Salter's "ten iterations" framing, those visualizations could have been re-rendered with alternative color groupings or alternative top-N cutoffs to make the interpretive choices visible.

### 2. Pick the model for the task and say so

Week 1 tells students to "try the same prompt with both Claude Sonnet and Claude Opus to see how the responses vary." Week 3 (Research) tells students to "make sure you are using your allocation of queries to Claude Opus 4." Week 4 recommends Opus 4 for distant reading because "it handles large text files and data analysis particularly well." Model selection is a methodological choice that gets documented, not a default that gets ignored.

*How the Week 3 distant read fared.* We used Opus, matching Salter's recommendation, but never said so. A real version of this analysis submitted for discussion would name the model, version, and any switching across the session.

### 3. Be specific in prompts; stage the work into a sequence

Week 9 ("Distant Coding") models this explicitly by breaking a small project into five sequential prompts — dataset → JSON conversion → display → recommendations → styling — rather than asking for the whole thing at once. Week 10 says "describe what you want as concretely as possible." Week 3 says "be as specific in your question and goals as possible when making your initial request." The implicit theory of mind is that LLMs do better on small, well-scoped requests with explicit constraints than on broad, underspecified ones.

*How the Week 3 distant read fared.* The seven-step Salter sequence (preprocess → bag of words → stopwords → wordcloud → themes → network → phrases) naturally enforced this. The opening clarifying question — whether to treat the corpus as one body or comparatively, and what to do about the missing character network — was itself a specificity move before any tool ran.

### 4. Ground every claim in the source

Week 3 (Research) warns: "spend some time looking through the links it has collected to verify if you agree with how the chatbot has contextualized and synthesized the response... be particularly wary of misinterpretation of complex sources, and note where corporate marketing or press releases are treated as authoritative." This is the same instruction Underwood gives in the Week 4 reading — distant patterns must be ground-truthed against passages.

*How the Week 3 distant read fared.* This was the analysis's strongest move. Every claim that survived into the final critique was verified against grep'd passages. The most important finding — that the corpus treats *authenticity* critically rather than approvingly — only emerged from this verification step and would have been the opposite finding if we had trusted frequency alone. This is exactly what Salter wants the discipline to be.

### 5. Familiarity helps you verify

Week 4 is explicit: "You might find it easiest to analyze a text that's in an area that you're familiar with, or that is in an area of interest to you, so that you will have a better capacity to check and verify the output." Distant reading without domain knowledge produces patterns you cannot evaluate.

*How the Week 3 distant read fared.* Mixed. The reader had general familiarity with game studies as a field but not deep familiarity with this specific corpus — useful enough to recognize *Civilization*, *Call of Duty*, *Europa Universalis*, and the *virtual heritage* subfield as plausible findings, but not enough to confidently rank Chapman vs. Champion vs. Hammar in influence, or to know on sight that Kapell & Elliott's edited volume is the citation hub generating the "kapell andrew elliott" trigram noise. A reader who works in this field would have caught more of the citation-trace contamination earlier and weighted the case-study findings against existing knowledge of the literature.

### 6. Tell the truth about what the AI is doing — and what it isn't

Week 2 quotes Leah Henrickson's critique of Racter, the early "computer-authored" book: "The program cannot interpret that which it produces and, indeed, not until a human interprets [its] output can it be assigned any cultural value." The course holds this critique up as still applying to current LLMs. The output is a *cultural object*; the *cultural value* is supplied by the reader. Salter wants this stated in every reflection.

*How the Week 3 distant read fared.* The Verdict section addresses this — "the AI-assisted version accelerated the mechanical parts but did not... substitute for the close-reading step that gives the frequencies meaning." This is the Henrickson move, made about distant reading specifically. The previous writeup also names what the method cannot see at all (chronology, stance, citation lineage, register), which is a related move: refusing to let the visualization carry inferences it cannot support.

### 7. Failure is data; success isn't the point

Week 2: "the emphasis is not on 'success' or 'failure,' but on critiquing the process and products through a theoretical lens." Failed iterations and broken outputs are findings, not embarrassments. The discussion post is more interesting when it admits what didn't work.

*How the Week 3 distant read fared.* The walkthrough lists every iteration that failed, including a bug that nearly lost a whole paper. Appendix C of the writeup is just a chronological log of corrections. This matches Salter's framing.

### 8. Connect findings to theory in the readings

Every Salter discussion prompt insists that the output be tied back to the assigned theoretical reading — Underwood for distant reading, Bender & Hanna on AI hype, Noble on algorithmic bias, Emerson on the interface, Littman on what code "really is." The artifact is the occasion; the discussion is the deliverable.

*How the Week 3 distant read fared.* This is the gap. The Week 3 corpus reading invoked Underwood by name (the pattern/argument distinction, the digitization-artifact warning, the importance of returning to passages) but did not engage Mitchell, Bender & Hanna, Noble, or Emerson at all. A submission-grade version of the writeup would, for instance, run the *authenticity-is-critiqued-not-endorsed* finding through Bender & Hanna's distinction between AI hype and actual capacity, or run the DRM-footer contamination through Emerson's "interfaced" argument about how the digitization platform shapes what becomes readable.

### 9. Choose corpora with intent

Week 14: "Consider selecting texts that share a common theme, genre, author, or time period to make your comparative analysis more meaningful." Corpus design is part of the method. Random or convenience corpora produce confounded results.

*How the Week 3 distant read fared.* This one we could not control — the corpus was your existing folder of Week 3 readings, presumably curated by the workshop instructors. But the writeup should have made the corpus's contingency explicit. The relevant question is "what defines this folder?" — course readings, a specific scholar's curated reading list, a snowball from one edited volume? The findings are findings *about this folder*, not findings about historical game studies as a field. We named this in passing in the critique but did not foreground it.

### 10. Use the AI's affordances strategically

The interface matters. Week 2 leans on Lori Emerson to argue that the interface (chat, artifact, Research mode, Code, agent) is not neutral. Week 3 puts students into Research mode for synthesis tasks. Week 9 uses artifacts because they let users "watch the HTML file evolve as you iterate." Week 14 routes students through Claude Code (or Claude Code Web with a GitHub repo) when the work demands a real Python pipeline rather than chat-window summarization. Week 15 introduces skills and subagents for repeated workflows. The lesson: don't just type into the chat box — pick the affordance for the task.

*How the Week 3 distant read fared.* This was a strength. We routed the work through bash for text extraction and Python for tokenization and TF-IDF, used the visualize tool for word cloud / theme grid / network / phrases charts, and saved the writeup as a markdown deliverable. The chat narration sat on top of an actual pipeline rather than asking Claude to summarize 762,000 words from inside the context window — which it could not have done accurately. If we did this again with Claude Code rather than this interface, we would commit each pipeline script and each intermediate JSON to a repo, so the analysis would be replayable end-to-end rather than reconstructible only from the writeup.

### 11. Treat tooling and labor questions as part of the analysis

Week 3 (Research) and Week 14 both push students to think about "this approach to outsourcing a preliminary query" — who is doing the work, whose labor produced the training data, what gets concealed by the speed of synthesis. *The AI Con* and *Algorithms of Oppression* run as the critical undertow under every exercise.

*How the Week 3 distant read fared.* Largely absent. The previous writeup focused on the epistemics of the method (what frequency can and cannot tell us) but did not address the labor / political-economy register at all. A submission to Salter's course would notice that the corpus itself includes critical-theory texts (Dyer-Witheford & De Peuter on *Games of Empire*, Hammar on hegemonic pasts, Mir & Owens on indigenous representation) and that running an AI-assisted distant read of a corpus partly about ideology critique is itself an act worth narrating.

### 12. Scale up the automation only after understanding the manual version

The course is structured as a deliberate progression — Week 4 you work conversationally; Week 9 you stage prompts to build a small artifact; Week 14 you set up a real pipeline in Claude Code Web; Week 15 you fine-tune your own model. The pedagogical claim is that you should not jump to the most automated approach until you have understood what the less automated one taught.

*How the Week 3 distant read fared.* Honored partly by accident. The walkthrough you requested at the start — "show me the conversational walkthrough" rather than "produce a finished report" — is exactly the Week 4 register. If you wanted to take this further, Week 14 would be the next move: take the same corpus, build it as a GitHub repo, use Claude Code to produce a replayable Python pipeline, and add things distant reading at corpus level cannot do without code (chronological slicing across the 2006–2024 span, sentiment scoring per document, LDA topic modeling, an author citation network to recover the lost Friedman paper). The Week 15 fine-tuning option is also live — train a small story-generator on the corpus and notice what voice it picks up.

### 13. The point of failure is what the method made visible

This is the implicit through-line of all the exercises. The DRM footer that dominated our trigrams, the JSTOR cover sheet that ate McCall, the Friedman scan that left no text — these aren't side problems. They're the visible parts of an infrastructure (publisher DRM, JSTOR ingestion, scanning quality) that normally stays hidden, and distant reading made them legible. Salter's exercises consistently treat what breaks as more informative than what succeeds.

*How the Week 3 distant read fared.* The writeup names the artifacts but treats them as obstacles overcome. A stronger version would treat the DRM footer not as noise to filter out but as evidence — a sign of how academic publishing's enclosures continue to shape what we can read computationally. Likewise, the Friedman 0-word file is not a failed extraction; it is the visible signature of a specific kind of mid-2000s scanning practice that produced thousands of unreadable academic PDFs and that current OCR could partly reverse. Naming this is the kind of move that turns a methodological note into a humanities argument.

## Where to go next

If you wanted to extend this past Week 4 (Salter's distant-reading exercise) into the territory of Weeks 9, 10, and 14, three concrete directions follow from the corpus we already have:

The first is **chronological slicing**. The corpus spans 2006 to 2024. A Week 14-style pipeline could split it into pre-2013 and post-2013 halves (Kapell & Elliott's *Playing with the Past*, 2013, is the field's pivot text) and compute which terms grew, which shrank, and which entered. *Counterfactual*, *procedural*, *empathy*, and *augmented* are good candidates to check.

The second is **author-citation network recovery**. The Friedman paper is unreadable, but it is cited by 14 of the readable documents. Building a graph of citations (extracting reference lists, normalizing author-year keys, edges between papers that cite each other or share citations) would recover the field's intellectual lineage in a way that the body-text analysis cannot — and would surface Friedman, Bogost, Galloway, Murray, and other figures who circulate in the corpus through citation rather than through their own words.

The third is **per-text TF-IDF for stance fingerprinting**. The corpus-level finding that *authenticity* is treated critically is a single average. A per-text TF-IDF would surface which authors lean hardest into the critique (Hammar, Dyer-Witheford, Mir & Owens) versus which treat authenticity as a design target (Champion, McCall on pedagogy). That comparison gets at *which authors do what* — the closest a distant read can come to characterizing argumentative stance.

Any of these is a natural follow-up assignment, and each maps directly onto the methods Salter introduces in the procedural unit.

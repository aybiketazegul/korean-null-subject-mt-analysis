# Error taxonomy

This file defines the error categories used to analyze how machine translation systems resolve Korean null subjects when translating into English.

The taxonomy is based on recurring patterns observed across examples in the dataset.

---

## 1. Incorrect referent selection (subject continuity bias)

The system resolves a null subject by defaulting to the previous grammatical subject, even when discourse structure, event semantics, or pragmatic reasoning favor a different referent.

This reflects a strong preference for surface syntactic continuity over discourse-based interpretation.

---

## 2. Over-specification (invented subject or participants)

The system introduces an explicit subject (often first person) or adds discourse participants that are not specified in the Korean source sentence.

While such outputs may be grammatically well-formed in English, they introduce discourse information absent from the original sentence.

---

## 3. Honorific cue underused or ignored

The system fails to use honorific morphology (e.g., 말씀하셨다, 오셨다) as a constraint on subject selection.

As a result, translations may appear superficially correct while obscuring sociolinguistic cues that guide human reference resolution.

---

## 4. Forced disambiguation

The system resolves a genuinely ambiguous Korean sentence into a single English interpretation, eliminating ambiguity that human readers can maintain in the absence of contextual cues.

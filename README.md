# Korean Null Subjects & Machine Translation

This repository contains a small research dataset used to analyze how Korean null-subject sentences are interpreted by humans and resolved by machine translation systems.

It compares expected human interpretations with outputs from Google Translate and Naver Papago, focusing on reference resolution differences.

---

## What’s inside

- **data/sentences.jsonl**  
  Annotated examples with:
  - Korean sentence
  - expected human interpretation
  - machine translation outputs
  - error type labels

- **analysis/error_taxonomy.md**  
  Definitions of the error categories used in the analysis.

- **scripts/count_error_types.py**  
  A small script that reads the dataset and summarizes counts of each error type.

---

## Usage (optional)

To generate a simple summary of error types:

```bash
python scripts/count_error_types.py

# Dataset schema

Each entry in `sentences.jsonl` represents one Korean sentence analyzed for null-subject reference resolution.

Fields:
- `id`: example number
- `korean_sentence`: original Korean sentence
- `phenomena`: linguistic phenomena involved (e.g. null subject, honorifics)
- `human_expected_interpretation`: expected interpretation by native speakers
- `interpretive_cues`: cues used by humans (discourse, pragmatics, honorifics)
- `mt_outputs`: outputs from Google Translate and Papago
- `error_type`: classification based on the error taxonomy
- `analysis_note`: short explanation of the mismatch

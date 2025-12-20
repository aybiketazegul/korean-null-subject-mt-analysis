import json
from collections import Counter
from pathlib import Path

DATA_PATH = Path("data/sentences.jsonl")

def load_jsonl(path):
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows

def main():
    rows = load_jsonl(DATA_PATH)
    counts = Counter(r["error_type"] for r in rows)

    output_path = Path("analysis/error_type_counts.md")
    with open(output_path, "w", encoding="utf-8") as w:
        w.write("# Error type counts\n\n")
        w.write(f"Total examples: {len(rows)}\n\n")
        for error, count in counts.items():
            w.write(f"- **{error}**: {count}\n")

    print("Summary written to analysis/error_type_counts.md")

if __name__ == "__main__":
    main()

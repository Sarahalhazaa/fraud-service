"""Compare a scored CSV with the golden reference: python scripts/check_golden.py scored.csv"""
import sys

import pandas as pd

scored = pd.read_csv(sys.argv[1] if len(sys.argv) > 1 else "scored.csv")
golden = pd.read_csv("data/golden_scores_v3.csv")
merged = golden.merge(scored, on="transaction_id", suffixes=("_golden", ""))
diff = merged[(merged["score"] - merged["score_golden"]).abs() > 1e-6]
print(f"{len(merged) - len(diff):,}/{len(golden):,} rows match the golden scores")
if len(diff):
    print(f"SKEW: {len(diff)} rows differ. First few:")
    print(diff[["transaction_id", "timestamp", "score_golden", "score"]].head(5).to_string(index=False))
    sys.exit(1)
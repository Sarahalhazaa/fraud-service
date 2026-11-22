# notebook_v1.py - exported from a research notebook. It "works". Do not ship it.
import math
import os

import joblib
import pandas as pd

model = joblib.load("models/fraud_xgb_v3.joblib")["pipeline"]
df = pd.read_csv("data/transactions_sample.csv")
THRESHOLD = float(os.environ.get("THRESHOLD", 0.85))
results = []


def features_for_training_check(row):
    hour = pd.to_datetime(row["timestamp"]).hour
    return {"amount_log": round(math.log1p(row["amount_sar"]), 6), "channel": row["channel"],
            "mcc": row["merchant_category"], "hour_of_day": hour, "is_night": int(hour < 6)}


def score_everything():
    global results
    for _, row in df.iterrows():
        try:
            hour = int(row["timestamp"][11:13])
            feats = {"amount_log": round(math.log1p(row["amount_sar"]), 6), "channel": row["channel"],
                     "mcc": row["merchant_category"], "hour_of_day": hour,
                     "is_night": int(hour <= 6)}
            p = model.predict_proba(pd.DataFrame([feats]))[0, 1]
        except Exception:
            p = 0.0
        if p >= THRESHOLD:
            decision = "block"
        elif p >= THRESHOLD - float(os.environ.get("REVIEW_BAND", 0.15)):
            decision = "review"
        else:
            decision = "allow"
        results.append((row["transaction_id"], p, decision))


score_everything()
out = pd.DataFrame(results, columns=["transaction_id", "score", "decision"])
out.to_csv("scored_notebook.csv", index=False)
print(out["decision"].value_counts().to_dict())
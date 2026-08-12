import json
from pathlib import Path

import pandas as pd


RESULTS_PATH = Path("data/results/evaluation_results.jsonl")


def load_results():
    records = []

    with RESULTS_PATH.open("r", encoding="utf-8") as f:
        for line in f:
            records.append(json.loads(line))

    return records


if __name__ == "__main__":
    results = load_results()

    df = pd.DataFrame(results)

    print("Overall accuracy:")
    print(df["correct"].mean())

    print("\nAccuracy by domain:")
    print(df.groupby("domain")["correct"].mean())

    print("\nAccuracy by difficulty:")
    print(df.groupby("difficulty")["correct"].mean())
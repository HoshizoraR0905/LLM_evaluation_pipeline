import json #works like dict
from pathlib import Path

from src.evaluation.schema import BenchmarkItem


BENCHMARK_PATH = Path("data/benchmark/questions.jsonl")


def load_benchmark():
    records = []

    with BENCHMARK_PATH.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            raw_data = json.loads(line) #load json as dict
            item = BenchmarkItem(**raw_data)
            records.append(item)

    return records


if __name__ == "__main__":
    benchmark = load_benchmark()

    print(f"Loaded {len(benchmark)} questions.")

    for item in benchmark:
        print(
            item.id,
            item.domain,
            item.difficulty,
            item.question,
        )
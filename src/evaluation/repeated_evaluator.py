import json
from pathlib import Path

from src.evaluation.load_benchmark import load_benchmark
from src.evaluation.parser import extract_final_answer
from src.evaluation.evaluator import evaluate_answer
from src.inference.model_client import ask_model


NUM_RUNS = 5

TARGET_IDS = {
    "logic_001", 
    "logic_002", 
    "logic_003", 
    "logic_004", 
    "logic_005", 
    "logic_006", 
    "logic_007", 
    "logic_008", 
    "logic_009", 
    "logic_010", 
}

RESULTS_PATH = Path("data/results/repeated_evaluation_results.jsonl")


if __name__ == "__main__":
    benchmark = load_benchmark()

    selected_items = [
        item for item in benchmark
        if item.id in TARGET_IDS
    ]

    results = []

    for item in selected_items:
        for run in range(1, NUM_RUNS + 1):

            # No cache: every run makes a fresh API call
            response = ask_model(item.question)

            prediction = extract_final_answer(response)

            is_correct = evaluate_answer(
                prediction=prediction,
                reference=item.final_answer,
            )

            print(
                f"{item.id} run={run}: "
                f"prediction={prediction} "
                f"reference={item.final_answer} "
                f"correct={is_correct}"
            )

            results.append({
                "id": item.id,
                "domain": item.domain,
                "topic": item.topic,
                "reasoning_type": item.reasoning_type,
                "run": run,
                "prediction": prediction,
                "reference": item.final_answer,
                "correct": is_correct,
            })

    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)

    with RESULTS_PATH.open("w", encoding="utf-8") as f:
        for result in results:
            f.write(json.dumps(result) + "\n")

    print("\nPer-question empirical accuracy:")

    for item in selected_items:
        item_results = [
            r for r in results
            if r["id"] == item.id
        ]

        num_correct = sum(r["correct"] for r in item_results)
        total = len(item_results)

        print(
            f"{item.id}: "
            f"{num_correct}/{total} = {num_correct / total:.0%}"
        )
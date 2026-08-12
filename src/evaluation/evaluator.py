from src.evaluation.load_benchmark import load_benchmark
from src.evaluation.parser import extract_final_answer
from src.inference.model_client import ask_model, MODEL_NAME

import json
from pathlib import Path
RESULTS_PATH = Path("data/results/evaluation_results.jsonl")
CACHE_PATH = Path("data/cache/model_responses.jsonl")

from fractions import Fraction

import hashlib

def make_cache_key(item, model_name: str) -> str:
    content = f"{model_name}|{item.id}|{item.question}"

    return hashlib.sha256(
        content.encode("utf-8")
    ).hexdigest()


def normalize_string(answer: str) -> str:
    return "".join(answer.strip().lower().split())


def try_parse_number(answer: str):
    answer = answer.strip()

    try:
        if "/" in answer:
            return float(Fraction(answer))

        return float(answer)

    except (ValueError, ZeroDivisionError):
        return None


def evaluate_answer(
    prediction: str,
    reference: str,
    tolerance: float = 1e-6,
) -> bool:
    prediction_num = try_parse_number(prediction)
    reference_num = try_parse_number(reference)

    # If both answers are numeric, compare numerically
    if prediction_num is not None and reference_num is not None:
        return abs(prediction_num - reference_num) <= tolerance

    # Otherwise compare as normalized strings
    prediction_str = normalize_string(prediction)
    reference_str = normalize_string(reference)

    return prediction_str == reference_str


def load_cache():
    cache = {}

    if not CACHE_PATH.exists():
        return cache

    with CACHE_PATH.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            record = json.loads(line)
            cache[record["cache_key"]] = record["response"]

    return cache


def save_cache(cache):
    with CACHE_PATH.open("w", encoding="utf-8") as f:
        for cache_key, response in cache.items():
            record = {
                "cache_key": cache_key,
                "response": response,
            }

            f.write(json.dumps(record) + "\n")


if __name__ == "__main__":
    cache = load_cache()

    benchmark = load_benchmark()

    correct = 0
    results = []

    for item in benchmark:
        cache_key = make_cache_key(item, MODEL_NAME)

        if cache_key in cache:
            response = cache[cache_key]
            print(f"{item.id}: using cached response")

        else:
            response = ask_model(item.question)
            cache[cache_key] = response
            print(f"{item.id}: called API")

        prediction = extract_final_answer(response)

        is_correct = evaluate_answer(
            prediction=prediction,
            reference=item.final_answer,
        )

        print(
            item.id,
            "prediction =", prediction,
            "reference =", item.final_answer,
            "correct =", is_correct,
        )

        if is_correct:
            correct += 1

        result = {
            "id": item.id,
            "domain": item.domain,
            "topic": item.topic,
            "difficulty": item.difficulty,
            "reasoning_type": item.reasoning_type,
            "prediction": prediction,
            "reference": item.final_answer,
            "correct": is_correct,
        }

        results.append(result)

    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)

    print(f"\nNumber of results: {len(results)}")
    print(f"Writing results to: {RESULTS_PATH.resolve()}")

    with RESULTS_PATH.open("w", encoding="utf-8") as f:
        for result in results:
            f.write(json.dumps(result) + "\n")

    accuracy = correct / len(benchmark)
    save_cache(cache)
    print(f"\nAccuracy: {accuracy:.2%}")
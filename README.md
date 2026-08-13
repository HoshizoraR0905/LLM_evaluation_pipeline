# LLM Evaluation Pipeline

A lightweight evaluation framework for studying how large language models perform across mathematical reasoning, commonsense reasoning, domain-specific rule application, and synthetic logic tasks.

The project currently uses Qwen Plus through the DashScope OpenAI-compatible API.

## Goals

This project is designed to study not only whether a model answers correctly, but also:

- how stable its answers are across repeated generations,
- whether failures come from missing knowledge or failed rule composition,
- how performance changes across reasoning types,
- and how evaluation can guide targeted interventions.

## Project Structure

```text
src/
  evaluation/
    evaluator.py
    repeated_evaluator.py
    load_benchmark.py
    parser.py
    schema.py
  inference/
    model_client.py
  analysis/
    analyze_results.py

data/
  benchmark/
    questions.jsonl
  annotations/

experiments/
  qwen_plus_stability_001.jsonl
  qwen_plus_stability_001.md
  qwen_plus_stability_002.jsonl
  qwen_plus_stability_002.md
  qwen_plus_stability_003.jsonl
  qwen_plus_stability_003.md
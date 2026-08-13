# Qwen Plus Stability Experiment 003

## Purpose

Evaluate Qwen Plus on synthetic logic questions where all relevant rules are explicitly provided in-context.

The goal is to separate pure compositional reasoning ability from domain-knowledge retrieval.

## Model

- Model: qwen-plus
- Cache: disabled
- Evaluation: normalized exact-match
- Domain: synthetic logic

## Questions

The experiment included logic questions covering:

- rule composition
- exception handling
- state tracking
- constraint reasoning
- counterfactual reasoning
- rule precedence

## Result

Qwen Plus achieved 100% accuracy on the tested synthetic logic questions.

## Observation

Unlike the Pokemon battle-mechanics questions, the model showed no failures when all relevant rules were explicitly stated in the prompt.

This suggests that the earlier Pokemon failures may not be caused by a general inability to perform logical composition.

Instead, the difficulty may arise from having to retrieve the correct domain-specific rules from model knowledge and then apply or compose them correctly in a concrete scenario.

## Interpretation

The current evidence suggests a distinction between:

1. explicit in-context rule reasoning, where performance is strong, and
2. knowledge-dependent rule application, where performance is less stable.

The synthetic logic questions in this experiment may still be too simple to distinguish stronger reasoning capabilities, so future experiments should introduce more adversarial compositional structure, such as irrelevant rules, nested exceptions, temporal updates, and minimal-pair perturbations.

## Next Steps

- Design harder adversarial synthetic-rule questions.
- Compare explicit-rule reasoning with knowledge-dependent rule reasoning.
- Use minimal pairs to test consistency under small changes in conditions.
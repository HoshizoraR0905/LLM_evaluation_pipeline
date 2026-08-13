## Project Story

This project started as a simple benchmark for mathematical reasoning.

### Stage 1 — Building the Evaluation Pipeline

The first version focused on probability, statistics, linear algebra, and optimization questions.

The initial goal was to build the basic infrastructure:

- benchmark loading and validation,
- model inference through an API,
- structured answer extraction,
- numeric and string-based evaluation,
- caching,
- and result analysis.

Qwen Plus achieved nearly perfect accuracy on these questions.

This revealed an important limitation of the initial benchmark: standard mathematical questions were not sufficiently discriminative for a strong language model.

### Stage 2 — Moving Beyond Standard Mathematics

To find more informative failure cases, the benchmark was expanded to commonsense questions and Pokemon battle mechanics.

These questions differ from standard mathematical problems because they may require:

- identifying unstated assumptions,
- recalling domain-specific rules,
- selecting relevant rules,
- and composing several interacting mechanics.

Repeated sampling revealed substantial instability on some Pokemon questions.

For example, the model frequently selected Thunder Wave against Eelektross despite correctly recognizing Levitate's immunity to Ground-type attacks.

This raised a new question:

> Does the model lack the necessary Pokemon knowledge, or does it know the individual rules but fail to combine them correctly?

### Experiment 001 — Measuring Response Stability

The same questions were sampled repeatedly without using cached responses.

This showed that a single model response can give a misleading picture of performance.

For example:

- `cs_001`: 9/10
- `cs_002`: 10/10
- `pokemon_001`: 2/10
- `pokemon_002`: 3/10

This motivated using empirical accuracy over repeated generations rather than treating each question as deterministically correct or incorrect.

### Experiment 002 — Separating Knowledge Recall from Rule Application

Diagnostic Pokemon questions were created to test the individual rules underlying the failed composite questions.

The model achieved:

- 5/5 on Electric-type immunity to Thunder Wave,
- 5/5 on Levitate immunity to Earthquake,
- 5/5 on basic Trick Room ordering,
- 4/5 on the abstract speed-based ordering of simultaneous weather-setting Abilities,
- but only 2/5 when applying the weather-ordering rule to a concrete Groudon-versus-Kyogre scenario.

These results suggest that at least some failures are not caused by missing knowledge.

Instead, performance appears to degrade as the task moves from rule recall to concrete rule application and multi-rule composition.

### Experiment 003 — Testing Pure In-Context Logic

A synthetic logic benchmark was then introduced.

Unlike Pokemon questions, all necessary rules were explicitly provided in the prompt, removing the need for domain-knowledge retrieval.

The questions tested:

- rule composition,
- exception handling,
- state tracking,
- counterfactual reasoning,
- constraint reasoning,
- and rule precedence.

Qwen Plus achieved 100% accuracy on the tested synthetic logic questions.

This suggests that the observed failures are not simply due to weak logical reasoning in general.

A working hypothesis is that the more difficult setting is:

> retrieve the correct domain knowledge → select the relevant rules → apply them to a concrete situation → compose multiple interacting rules.

### Current Direction

The next experiments will test whether this pattern generalizes beyond Pokemon.

Planned directions include:

- adversarial synthetic-rule systems,
- minimal-pair questions,
- nested exceptions,
- temporal state tracking,
- additional knowledge-plus-reasoning domains,
- prompt interventions,
- and multi-model comparison.
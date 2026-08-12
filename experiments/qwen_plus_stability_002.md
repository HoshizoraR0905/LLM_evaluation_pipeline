# Qwen Plus Stability Experiment 002

## Purpose

Diagnose whether Qwen Plus failures on Pokemon battle-mechanics questions are caused by:

1. missing rule knowledge,
2. failure to apply known rules to concrete cases, or
3. failure to compose multiple interacting rules.

## Model

- Model: qwen-plus
- Cache: disabled
- Samples per question: 5
- Evaluation: normalized exact-match against the benchmark final answer

## Questions

| ID | Skill tested | Accuracy |
|---|---|---:|
| pokemon_003 | Electric-type immunity to Thunder Wave | 5/5 = 100% |
| pokemon_004 | Levitate immunity to Earthquake | 5/5 = 100% |
| pokemon_005 | Basic Trick Room move-order rule | 5/5 = 100% |
| pokemon_006 | Applying simultaneous weather-Ability ordering to Groudon and Kyogre | 2/5 = 40% |
| pokemon_007 | Recall of simultaneous weather-Ability activation order | 4/5 = 80% |

## Observations

Qwen Plus reliably recalled several individual battle rules in isolation:

- Electric-type Pokemon cannot be paralyzed by Thunder Wave.
- Levitate grants immunity to Earthquake under normal conditions.
- Under Trick Room, the slower Pokemon moves first within the same priority bracket.

The model correctly identified the speed-based activation order of simultaneous weather-setting Abilities in 4 out of 5 runs.

However, accuracy dropped to 2 out of 5 when the same rule had to be applied to a concrete Groudon-versus-Kyogre scenario where Kyogre was faster. 

## Interpretation

The results suggest that the observed Pokemon failures are not explained primarily by missing factual knowledge.

Instead, performance appears to degrade as the task moves from:

1. isolated rule recall,
2. to rule application in a concrete scenario,
3. to composition of multiple interacting rules.

This supports the hypothesis that Qwen Plus has a rule-application or rule-composition weakness on these battle-mechanics questions.

The sample size is small, so these results should be treated as diagnostic evidence rather than a precise estimate of model accuracy.

## Next Steps

- Test additional rule-composition questions outside Pokemon to see whether the pattern generalizes.
- Compare baseline prompting with an explicit rule-decomposition prompt.
- Increase the number of repeated samples for selected ambiguous cases if tighter estimates are needed.
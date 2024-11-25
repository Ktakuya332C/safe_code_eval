---
title: Safe Code Eval
tags:
- evaluate
- metric
description: safer variant of the Code Eval
---

# Metric Card for Safe Code Eval

## Metric Description
Safer variant of the Code Eval

## Requirements
- deno : https://deno.com/

## How to Use
```python
import evaluate
safe_code_eval = evaluate.load("ktakuya/safe_code_eval")
```

### Inputs
*List all input arguments in the format below*
- **input_field** *(type): Definition of input, with explanation if necessary. State any default value(s).*

### Output Values

*Explain what this metric outputs and provide an example of what the metric output looks like. Modules should return a dictionary with one or multiple key-value pairs, e.g. {"bleu" : 6.02}*

*State the range of possible values that the metric's output can take, as well as what in that range is considered good. For example: "This metric can take on any value between 0 and 100, inclusive. Higher scores are better."*

#### Values from Popular Papers
*Give examples, preferrably with links to leaderboards or publications, to papers that have reported this metric, along with the values they have reported.*

### Examples
*Give code examples of the metric being used. Try to include examples that clear up any potential ambiguity left from the metric description above. If possible, provide a range of examples that show both typical and atypical results, as well as examples where a variety of input parameters are passed.*

## Limitations and Bias
*Note any known limitations or biases that the metric has, with links and references if possible.*

## Citation
*Cite the source where this metric was introduced.*

## Further References
*Add any useful further references.*

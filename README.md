---
title: Safe Code Eval
colorFrom: blue
colorTo: red
tags:
- evaluate
- metric
description: A safer variant of the Code Eval
---

# Metric Card for Safe Code Eval

## Metric Description
Safer variant of the Code Eval

## Requirements
- deno : https://deno.com/

## How to Use
```python
safe_code_eval = evaluate.load("ktakuya/safe_code_eval")
test_cases = ["assert add(2, 3) == 5"]
candidates = [["def add(a,b): return a*b", "def add(a, b): return a+b"]]
pass_at_k, results = safe_code_eval.compute(references=test_cases, predictions=candidates, k=[1, 2])
print(pass_at_k)  # {'pass@1': 0.5, 'pass@2': 1.0}
```

## Development
```Shell
# lint
isort --profile=black . && black .
# tests
python -m unittest tests.py
```

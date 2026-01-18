# Algorithms

Collection of small algorithm solutions and reference implementations.

## Structure
- `problems/` — implementation per problem
- `tests/` — pytest tests for each problem

## Problems
- `two_sum` — return indices of two numbers that add up to target
- `merge_two_sorted_lists` — merge two sorted linked lists
- `reverse_and_count` — reverse string (lowercased) and count alphabet usage

## How to run tests

Requirements: Python 3.8+ and `pytest`.

Install and run tests:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip pytest
pytest -q
```

Contributions are welcome! Open a PR with new problems, solutions, or improvements.

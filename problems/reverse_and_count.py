"""Reverse a string (lowercased) and count alphabet usage.

Function: reverse_lower_and_count(s: str) -> (reversed_lower: str, counts: dict, total: int)
- Reverses the input string and lowercases it.
- Counts only alphabet characters (a-z) and returns a mapping of letter -> count and total letters.
"""
from collections import Counter
from typing import Dict, Tuple


def reverse_lower_and_count(s: str) -> Tuple[str, Dict[str, int], int]:
    """Return (reversed_lower, counts, total_letters).

    Examples:
        >>> reverse_lower_and_count("Hello, World!")
        ('!dlrow ,olleh', {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}, 10)
    """
    rev = s[::-1].lower()
    counts = Counter(ch for ch in rev if ch.isalpha())
    total = sum(counts.values())
    return rev, dict(counts), total


if __name__ == "__main__":
    print(reverse_lower_and_count("Hello, World!"))

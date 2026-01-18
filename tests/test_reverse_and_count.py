import pytest
from problems.reverse_and_count import reverse_lower_and_count


def test_examples():
    rev, counts, total = reverse_lower_and_count("Hello, World!")
    assert rev == "!dlrow ,olleh"
    assert counts == {"h": 1, "e": 1, "l": 3, "o": 2, "w": 1, "r": 1, "d": 1}
    assert total == 10

    rev2, counts2, total2 = reverse_lower_and_count("")
    assert rev2 == ""
    assert counts2 == {}
    assert total2 == 0

    rev3, counts3, total3 = reverse_lower_and_count("AaBb")
    assert rev3 == "bbaa"
    assert counts3 == {"a": 2, "b": 2}
    assert total3 == 4


def test_non_alpha_only():
    rev, counts, total = reverse_lower_and_count("123!@#")
    assert rev == "#@!321"
    assert counts == {}
    assert total == 0

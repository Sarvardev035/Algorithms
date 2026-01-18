"""Two Sum problem — return indices of the two numbers that add up to target.

Complexity: O(n) time, O(n) space.
"""
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}  # value -> index
    for i, x in enumerate(nums):
        comp = target - x
        if comp in seen:
            return [seen[comp], i]
        seen[x] = i
    raise ValueError("No two-sum solution")


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]

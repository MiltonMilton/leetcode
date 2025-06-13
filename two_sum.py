"""Utility functions for solving the classic 'Two Sum' problem.

This module provides the :func:`two_sum` function which, given a list of
integers ``nums`` and a target integer ``target``, returns the indices of
the two numbers in ``nums`` that add up to ``target``.
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """Return the indices of the two numbers that add up to ``target``.

    The function iterates once through ``nums`` while storing seen values
    and their indices in a dictionary. For each element we check whether
    the complement (``target - num``) has already been seen. If so we
    have found the pair and return their indices.
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            # Complement has been seen before, so return the pair of indices.
            return [seen[complement], i]
        # Record the index of the current number for future lookups.
        seen[num] = i
    # If no pair is found, raise an error to signal failure.
    raise ValueError("No two sum solution")


if __name__ == "__main__":
    example = [2, 7, 11, 15]
    print(two_sum(example, 9))

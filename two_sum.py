"""Two Sum Problem Solver.

This module provides a `two_sum` function which finds two distinct numbers in
an iterable that add up to a specified target.
"""

from typing import Iterable, List, Optional


def two_sum(nums: Iterable[int], target: int) -> Optional[List[int]]:
    """Return indices of the two numbers that add up to the target.

    Parameters
    ----------
    nums : Iterable[int]
        A list of integers.
    target : int
        The desired sum.

    Returns
    -------
    Optional[List[int]]
        A list containing the indices of the two numbers if a pair exists,
        otherwise ``None``.
    """
    lookup = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], i]
        lookup[num] = i
    return None


if __name__ == "__main__":
    # Simple manual test
    print(two_sum([2, 7, 11, 15], 9))

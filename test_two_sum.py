import pytest

from two_sum import two_sum


def test_normal_case():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_duplicate_numbers():
    # duplicates can form the pair
    result = two_sum([3, 3, 4], 6)
    assert result == [0, 1]


def test_no_solution():
    assert two_sum([1, 2, 3], 7) is None

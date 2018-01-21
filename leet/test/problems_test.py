"""Tests for Leet Code problems.

Sanity checks for some of the solved problems. This isn't great practice, but to be more concise ONLY ONE test method
per problem is present.
"""

from leet.problems import four_sum


def test_four_sum():
    t = 0
    S = [1, 0, -1, 0, -2, 2]
    expected = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    assert [sorted(res) for res in four_sum(S, t)] == expected

    S = [-3, -2, -1, 0, 0, 1, 2, 3]
    t = 0
    expected = [[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2], [-2, -1, 0, 3], [-2, -1, 1, 2],
                [-2, 0, 0, 2], [-1, 0, 0, 1]]
    assert [sorted(res) for res in four_sum(S, t)] == expected

    # pierscin: early termination optimization - possible to check while debugging
    very_low_value = -10000
    target = 10
    list_that_sums_to_target = [0, 0, 0, target]
    S = sorted([very_low_value] + list_that_sums_to_target)

    assert sum(S[:5]) < target
    assert [sorted(res) for res in four_sum(nums=S, target=target)] == [[0, 0, 0, 10]]

    list_that_sums_to_target = [-very_low_value, 0, 0, 0]
    S = list_that_sums_to_target + [0]
    target = very_low_value
    assert sum(S[-4:]) > target
    assert [sorted(res) for res in four_sum(nums=S, target=target)] == []

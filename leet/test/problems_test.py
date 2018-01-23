"""Tests for Leet Code problems.

Sanity checks for some of the solved problems. This isn't great practice, but to be more concise ONLY ONE test method
per problem is present.
"""
from copy import deepcopy
from random import randint

from leet.problems import four_sum, remove_nth_from_end, are_parentheses_balanced, merge_two_sorted_lists, \
    generate_parenthesis, swap_pairs, remove_duplicates, next_permutation, divide
from leet.utils import ListNode


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


def test_remove_nth_node():
    singleton_list = [1]
    assert remove_nth_from_end(ListNode.from_list(singleton_list), 1) is None

    some_list = list(range(5))
    linked_list = ListNode.from_list(some_list)

    removed_second_last = ListNode.from_list(some_list[:-2] + some_list[-1:])
    assert remove_nth_from_end(deepcopy(linked_list), 2) == removed_second_last

    removed_tail = ListNode.from_list(some_list[:-1])
    assert remove_nth_from_end(deepcopy(linked_list), 1) == removed_tail

    removed_head = ListNode.from_list(some_list[1:])
    assert remove_nth_from_end(deepcopy(linked_list), 5) == removed_head


def test_are_parentheses_balanced():
    assert are_parentheses_balanced('')
    assert not are_parentheses_balanced('(')
    assert not are_parentheses_balanced(']')
    assert are_parentheses_balanced('{}')
    assert not are_parentheses_balanced('({)}')
    assert not are_parentheses_balanced('({}')
    assert are_parentheses_balanced("[({(())}[()])]")


def test_merge_two_sorted_lists():
    assert merge_two_sorted_lists(ListNode.from_list([1]), ListNode.from_list([])) == ListNode.from_list([1])
    assert merge_two_sorted_lists(ListNode.from_list([]), ListNode.from_list([1])) == ListNode.from_list([1])

    size = 30
    random_list = [randint(0, 10) for _ in range(size)]
    point_of_slicing = randint(0, size)

    l1, l2 = sorted(random_list[:point_of_slicing]), sorted(random_list[point_of_slicing:])
    assert merge_two_sorted_lists(ListNode.from_list(l1), ListNode.from_list(l2)).to_list() == sorted(l1 + l2)


def test_generate_parenthesis():
    assert generate_parenthesis(0) == ['']
    assert generate_parenthesis(1) == ['()']

    generated = generate_parenthesis(3)
    expected_parenthesis = {"((()))", "(()())", "(())()", "()(())", "()()()"}

    assert len(generated) == len(expected_parenthesis)

    for pair in generated:
        assert pair in expected_parenthesis


def test_swap_pairs():
    assert swap_pairs(ListNode.from_list([1])).to_list() == [1]
    assert swap_pairs(ListNode.from_list([1, 2])).to_list() == [2, 1]
    assert swap_pairs(ListNode.from_list([1, 2, 3])).to_list() == [2, 1, 3]
    assert swap_pairs(ListNode.from_list([1, 2, 3, 4])).to_list() == [2, 1, 4, 3]


def test_remove_duplicates():
    for A in [
        [],
        [1],
        [1, 1, 2],
        [1, 1, 2, 2, 3],
        [1, 1, 2, 2, 2, 2, 2, 2, 2, 2],
        [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4]
    ]:
        assert remove_duplicates(A) == len(set(A))


def test_divide():
    MIN_INT, MAX_INT = -2147483648, 2147483647

    for a, b in (
        (0, 1),
        (1, 1),
        (MIN_INT, 1),
        (MIN_INT + 1, -1),
        (randint(100000, 1000000), randint(2, 10))
    ):
        assert divide(a, b) == a // b

    assert divide(MIN_INT, -1) == MAX_INT


def test_next_permutation():
    for A, RESULT in (
        ([], []),
        ([1], [1]),
        ([1, 2, 3], [1, 3, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 1, 5], [1, 5, 1]),
        ([6, 7, 5, 3, 5, 6, 2, 9, 1, 2, 7, 0, 9], [6, 7, 5, 3, 5, 6, 2, 9, 1, 2, 7, 9, 0])
    ):
        next_permutation(A)
        assert A == RESULT

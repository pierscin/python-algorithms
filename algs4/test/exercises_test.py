"""Tests for exercises.

To be more concise, one test is written per one method. This isn't the most readable way and should be refactored later.
"""

from pytest import approx

from algs4.exercises import insert_left_parentheses, infix_to_postfix, rpn, sorted_intersection, local_min


def test_insert_left_parentheses():
    assert insert_left_parentheses('1 + 2 ) * 3 - 4 ) * 5 - 6 ) ) )') == '( ( 1 + 2 ) * ( ( 3 - 4 ) * ( 5 - 6 ) ) )'


def test_infix_to_postfix():
    assert infix_to_postfix('3 + 4') == '3 4 +'
    assert infix_to_postfix('3 + 4 * ( 2 - 1 )') == '3 4 2 1 - * +'
    assert infix_to_postfix('A + B * C + D') == 'A B C * + D +'
    assert infix_to_postfix('( A + B ) * ( C + D )') == 'A B + C D + *'
    assert infix_to_postfix('A * B + C * D') == 'A B * C D * +'
    assert infix_to_postfix('A + B + C + D') == 'A B + C + D +'
    assert infix_to_postfix('3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3') == '3 4 2 * 1 5 - 2 3 ^ ^ / +'


def test_rpn():
    assert rpn('2 7 + 3 / 14 3 - 4 * + 2 / r') == approx(-23.5)


def test_intersection():
    assert sorted_intersection([1], [2]) == []
    assert sorted_intersection([1], [1]) == [1]
    assert sorted_intersection([1, 1], [1]) == [1]
    assert sorted_intersection([1, 2], [2]) == [2]
    assert sorted_intersection([1, 2, 2, 2, 2, 3, 4], [3, 4]) == [3, 4]


def test_local_min():
    assert local_min([1, -1, 2]) == 1
    assert local_min([4, 3, -1, 2]) == 2
    assert local_min([3, -1, 2, 1]) == 1
    assert local_min([1, -1, 2, -2]) == 1
    assert local_min([1, -1, 2, -2, 3]) in {1, 3}

# pierscin: not stable on Travis...
#
# def test_insertion_sort_is_slower_than_its_faster_version():
#     benchmarks = running_time_of((faster_insertion_sort, insertion_sort), [[randint(0, 10) for _ in range(100)]], 10)
#     assert benchmarks[faster_insertion_sort.__name__].total_time < benchmarks[insertion_sort.__name__].total_time

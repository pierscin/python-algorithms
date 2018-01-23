"""Tests for sorting algorithms.

Sanity checks for all "sorts". List to sort is rather small so it won't take long to run quadratic sorts.
"""

from random import randint

from algs4.sorts import selection_sort, insertion_sort, shell_sort


def test_sorting_methods():
    sort_strategies = (selection_sort, insertion_sort, shell_sort)
    TO_SORT = [randint(0,10) for _ in range(100)]
    SORTED = sorted(TO_SORT)

    for sort in sort_strategies:
        A = list(TO_SORT)
        sort(A)
        assert A == SORTED

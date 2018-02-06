import time
from functools import total_ordering
from typing import Sequence, Any, Callable, List


@total_ordering
class LtAsGtWrapper:
    """Wrapper class to use structures with ascending sort order as descending ones, e.g. SortedList as min heap."""

    def __init__(self, x): self.x = x

    def __lt__(self, other): return self.x > other.x

    def __eq__(self, other): return self.x == other.x

    def __str__(self): return str(self.x)


# TODO: min binary search

def binary_search(A: List[int], x: int) -> int:
    NOT_FOUND = -1

    lo, hi = 0, len(A) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if x == A[mid]: return mid
        elif x > A[mid]: lo = mid + 1
        else: hi = mid - 1

    return NOT_FOUND


class Benchmark:
    def __init__(self, name, total_time, tries):
        self.name = name
        self.total_time = total_time
        self.tries = tries
        self.avg_time = total_time / tries


def running_time_of(methods: Sequence[Callable], args: Sequence[Any], tries: int) -> List[Benchmark]:
    """Returns benchmark data for each method listed after specified number of executions and arguments.

    Passing methods and args is tricky, because they should always be a sequence even if there's 1 tested method or
    a tested methods have 1 argument.

    Example:
        Tested methods have single, sequence argument. Notice the double brackets.

        >>> from algs4.sorts import selection_sort, insertion_sort
        >>> from random import randint
        >>> running_time_of((selection_sort, insertion_sort), [[randint(0, 10) for _ in range(100)]], 1000)

    Args:
        methods: sequence of compared methods
        args: arguments unpacked for each method
        tries: number of executions for each method

    Returns:
        A list with Benchmark objects containing test results.
    """
    benchmarks = []
    for m in methods:
        t = 0
        for _ in range(tries):
            copy_of_args = list(args)
            s = time.process_time()
            m(*copy_of_args)
            e = time.process_time()
            t += e - s
        benchmarks.append(Benchmark(m.__name__, t, tries))
    return benchmarks

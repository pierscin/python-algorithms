import time
from typing import Sequence, Dict


class Benchmark:
    def __init__(self, name, total_time, tries):
        self.name = name
        self.total_time = total_time
        self.tries = tries
        self.avg_time = total_time / tries


def running_time_of(methods: Sequence, args: Sequence, tries: int) -> Dict[str, Benchmark]:
    """Returns benchmark data for each method listed after specified number of executions and arguments.

    Passing methods and args is tricky, because they should always be a sequence even if there's 1 tested method or
    a tested methods have 1 argument.

    Example:
        Tested methods have single, sequence argument. Notice the double brackets.

        >>> from algs4.sorts import selection, insertion
        >>> from random import randint
        >>> running_time_of((selection, insertion), [[randint(0, 10) for _ in range(100)]], 1000)

    Args:
        methods: sequence of compared methods
        args: arguments unpacked for each method
        tries: number of executions for each method

    Returns:
        A dict mapping with each method name as key and Benchmark object with results
    """
    benchmarks = dict()
    for m in methods:
        t = 0
        for _ in range(tries):
            s = time.process_time()
            m(*args)  # TODO: args should be copied
            e = time.process_time()
            t += e - s
        benchmarks[m.__name__] = Benchmark(m.__name__, t, tries)
    return benchmarks

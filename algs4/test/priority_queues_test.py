from random import randint

from algs4.priority_queues import MaxHeap, MaxHeapOnList, MaxPqOnSortedList, MinHeap, MinPqOnSortedList


def test_max_priority_queues():
    priority_queues = (MaxHeap(), MaxHeapOnList(), MaxPqOnSortedList())

    values = [randint(0, 10) for _ in range(100)]

    for x in values:
        for pq in priority_queues: pq.push(x)

    for pq in priority_queues: assert len(pq) == len(values)

    values.sort(reverse=True)

    for x in values:
        for pq in priority_queues: assert x == pq.pop_max()

    for pq in priority_queues: assert not pq


def test_min_priority_queues():
    priority_queues = (MinHeap(), MinPqOnSortedList())

    values = [randint(0, 10) for _ in range(100)]

    for x in values:
        for pq in priority_queues: pq.push(x)

    for pq in priority_queues: assert len(pq) == len(values)

    values.sort()

    for x in values:
        for pq in priority_queues: assert x == pq.pop_min()

    for pq in priority_queues: assert not pq

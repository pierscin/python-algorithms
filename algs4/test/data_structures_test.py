"""Test module for data structures properties.

Structures can be divided into 3 categories:
 - built-into Python standard library and implemented - as coding exercise.
 - built-into Python standard library and NOT implemented - those which were basic.
 - implemented by hand.

All of them are tested in this module.
"""

from collections import deque
from random import randint, shuffle

from algs4.data_structures import MinHeap, MaxHeap, MaxHeapOnList, MaxPqOnSortedList, MinPqOnSortedList, Bst


def test_list_have_stack_properties():
    stack = []
    FIRST, LAST = 1, 2

    assert not stack

    stack.append(FIRST)

    assert stack
    assert stack[-1] == FIRST
    assert len(stack) == 1

    stack.append(LAST)

    assert len(stack) == 2

    assert stack[-1] == LAST
    assert stack.pop() == LAST

    assert stack[-1] == FIRST
    assert stack.pop() == FIRST

    assert not stack


def test_collections_deque_shave_queue_and_deque_properties():  # pierscin: list also has them, but performance is worse
    FIRST, SECOND, LAST = 1, 2, 3

    deq = deque()

    assert not deq
    assert len(deq) == 0

    deq.append(FIRST)

    assert deq
    assert len(deq) == 1

    deq.append(SECOND)

    assert len(deq) == 2
    assert deq.popleft() == FIRST

    deq.append(LAST)

    assert deq.popleft() == SECOND
    assert deq.popleft() == LAST
    assert not deq

    deq.append(SECOND)

    assert deq[-1] == deq[0] == SECOND

    deq.appendleft(FIRST)

    assert deq[-1] == SECOND
    assert deq[0] == FIRST

    assert deq.popleft() == FIRST
    assert deq.popleft() == SECOND


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


def test_binary_search_tree():
    bst = Bst()

    assert not bst

    bst.put(1, 2)

    assert len(bst) == 1

    bst.put(1, 2)

    assert len(bst) == 1

    bst.put(1, 1)

    assert len(bst) == 1

    bst.remove_min()

    assert not bst

    unique_keys = [i for i in range(50)]
    shuffle(unique_keys)

    for i, k in enumerate(unique_keys):
        bst.put(k, None)
        assert len(bst) == i + 1

    SIZE_BEFORE_DELETING = len(bst)
    shuffle(unique_keys)

    for i, k in enumerate(unique_keys):
        bst.remove(k)
        assert len(bst) == SIZE_BEFORE_DELETING - (i + 1)

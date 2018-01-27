"""Test module for data structures properties.

Structures can be divided into 3 categories:
 - built-into Python standard library and implemented - as coding exercise.
 - built-into Python standard library and NOT implemented - those which were basic.
 - implemented by hand.

All of them are tested in this module.
"""

from collections import deque
from random import randint

from algs4.data_structures import MinHeap, MaxHeap, MaxHeapOnList, MaxHeapOnSortedList, MinHeapOnSortedList


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


def test_max_heaps():
    heaps = (MaxHeap(), MaxHeapOnList(), MaxHeapOnSortedList())

    values = [randint(0, 10) for _ in range(100)]

    for x in values:
        for heap in heaps: heap.push(x)

    for heap in heaps: assert len(heap) == len(values)

    values.sort(reverse=True)

    for x in values:
        for heap in heaps: assert x == heap.pop_max()

    for heap in heaps: assert not heap


def test_min_heaps():
    heaps = (MinHeap(), MinHeapOnSortedList())

    values = [randint(0, 10) for _ in range(100)]

    for x in values:
        for heap in heaps: heap.push(x)

    for heap in heaps: assert len(heap) == len(values)

    values.sort()

    for x in values:
        for heap in heaps: assert x == heap.pop_min()

    for heap in heaps: assert not heap

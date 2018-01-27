import heapq
from typing import Any


class MinHeap:
    """Minimum heap based on heapq built-in.

    Python's heapq methods are clunky to use - this wrapper feels more natural.
    """

    def __init__(self): self.heap = []

    def __len__(self): return len(self.heap)

    def push(self, x):
        """Push element to the heap."""
        heapq.heappush(self.heap, x)

    def pop_min(self):
        """Pops min element from the heap. Raises IndexError when heap is empty."""
        return heapq.heappop(self.heap)

    def peek_min(self):
        """Get min element value without removing it from the heap."""
        return self.heap[0]


class MaxHeap:
    """Maximum heap based on heapq built-in.

    Python's heapq methods are very clunky to use with min heap, but with max heap it's even worse - there is
    heapq._heappop_max, BUT there isn't heapq._heappush_max... It means that user should always remember to heapify list
    to keep it's max heap invariant. To avoid that, Wrapper class with < and == operator was created - when items are
    pushed to the heap they are wrapped, but are unwrapped before pop.
    """

    class Wrapper:
        """Wrapper class to use heapq's min_heap methods with max_heap."""

        def __init__(self, x): self.x = x

        def __lt__(self, other): return self.x > other.x

        def __eq__(self, other): return self.x == other.x

        def __str__(self): return str(self.x)

    def __init__(self): self.heap = []

    def __len__(self): return len(self.heap)

    def push(self, x: Any):
        """Push element to the heap."""
        heapq.heappush(self.heap, MaxHeap.Wrapper(x))

    def pop_max(self) -> Any:
        """Pops max element from the heap. Raises IndexError when heap is empty."""
        return heapq.heappop(self.heap).x

    def peek_max(self) -> Any:
        """Get max element value without removing it from the heap."""
        return self.heap[0].x


class MyMaxHeap:
    """Max heap implementation from scratch.

    List which stores elements is 1-based - this leads to simpler math in _sink/_swim, but there is helper field N to
    track number of elements in heap.
    """

    def __init__(self):
        self.heap = [None]
        self.N = 0

    def __len__(self):
        return self.N

    def push(self, x: Any):
        """Push element to the heap"""
        self.N += 1

        self.heap.append(x)
        self._swim(self.N)

    def pop_max(self) -> Any:
        """Pops max element from the heap. Raises IndexError when heap is empty."""
        max_val = self.heap[1]

        self.heap[1] = self.heap[self.N]
        self.N -= 1

        self._sink(1)

        self.heap.pop()

        return max_val

    def peek_max(self) -> Any:
        """Get max element value without removing it from the heap."""
        return self.heap[1]

    def _swim(self, n):
        while n > 1 and self.heap[n // 2] < self.heap[n]:
            self.heap[n // 2], self.heap[n] = self.heap[n], self.heap[n // 2]

            n //= 2

    def _sink(self, n):
        while n * 2 <= self.N:
            j = n * 2

            if j + 1 <= self.N and self.heap[j + 1] > self.heap[j]: j += 1  # pierscin: exchange with bigger element

            if self.heap[j] < self.heap[n]: return

            self.heap[j], self.heap[n] = self.heap[n], self.heap[j]

            n = j

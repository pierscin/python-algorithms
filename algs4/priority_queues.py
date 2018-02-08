import heapq
from typing import Iterable, Any

from sortedcontainers import SortedList

from utils import ReverseOrderingWrapper


class MinHeap:
    """Minimum heap based on heapq built-in.

    Python's heapq methods are clunky to use - this wrapper feels more natural.
    """

    def __init__(self): self.heap = []

    def __len__(self): return len(self.heap)

    @classmethod
    def from_iterable(cls, A: Iterable) -> 'MinHeap':
        pq = cls()

        [pq.push(x) for x in A]

        return pq

    def push(self, x):
        """Push element to the heap."""
        heapq.heappush(self.heap, x)

    def pop_min(self):
        """Pop min element from the heap. Raises IndexError when heap is empty."""
        return heapq.heappop(self.heap)

    def peek_min(self):
        """Get min element without removing it."""
        return self.heap[0]


class MaxHeap:
    """Maximum heap based on heapq built-in.

    Python's heapq methods are very clunky to use with min heap, but with max heap it's even worse - there is
    heapq._heappop_max, BUT there isn't heapq._heappush_max... It means that user should always remember to heapify list
    to keep it's max heap invariant. To avoid that, wrapper class (ReverseOrderingWrapper) with < and == operator was created -
    items are wrapped when pushed to the min heap and unwrapped before pop.
    """

    def __init__(self): self.heap = []

    def __len__(self): return len(self.heap)

    def push(self, x: Any):
        """Push element to the heap."""
        heapq.heappush(self.heap, ReverseOrderingWrapper(x))

    def pop_max(self) -> Any:
        """Pop max element from the heap. Raises IndexError when heap is empty."""
        return heapq.heappop(self.heap).x

    def peek_max(self) -> Any:
        """Get max element without removing it."""
        return self.heap[0].x


class MinPqOnSortedList:
    """Min priority queue based on SortedList.

    SortedList keeps ascending order invariant, so ReverseOrderingWrapper is used to mimic descending order of items in max
    priority queue.
    """

    def __init__(self): self.heap = SortedList([])

    def __len__(self): return len(self.heap)

    def push(self, x: Any):
        """Push element to the queue."""
        self.heap.add(ReverseOrderingWrapper(x))

    def pop_min(self) -> Any:
        """Pop min element from queue. Raises IndexError when queue is empty."""
        return self.heap.pop().x

    def peek_min(self) -> Any:
        """Get min element without removing it."""
        return self.heap[-1].x


class MaxPqOnSortedList:
    """Max priority queue based on SortedList."""

    def __init__(self): self.heap = SortedList([])

    def __len__(self): return len(self.heap)

    def push(self, x: Any):
        """Push element to the queue."""
        self.heap.add(x)

    def pop_max(self) -> Any:
        """Pop max element from queue. Raises IndexError when queue is empty."""
        return self.heap.pop()

    def peek_max(self) -> Any:
        """Get max element without removing it."""
        return self.heap[-1].x


class MaxHeapOnList:
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
        """Pop max element from the heap. Raises IndexError when heap is empty."""
        max_val = self.heap[1]

        self.heap[1] = self.heap[self.N]
        self.N -= 1

        self._sink(1)

        self.heap.pop()

        return max_val

    def peek_max(self) -> Any:
        """Get max element without removing it."""
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


class IndexMinPq:
    """Indexed min heap.

    Stores keys which are heap ordered and associates each key with unique index. Key associated with index
    can be changed.
    """

    def __init__(self, max_n: int):
        self.N = 0
        self._max_n = max_n

        self._keys = [None] * (max_n + 1)
        self._pq = [0] * (max_n + 1)
        self._qp = [-1] * (max_n + 1)

    def __len__(self) -> int:
        return self.N

    def __contains__(self, i: int) -> bool:
        return self._qp[i] != -1

    def insert(self, i: int, x: Any) -> None:
        """Insert element x and associate it with index i. Raises ValueError if index is already used."""
        if i in self: raise ValueError("Index is already used.")

        self.N += 1
        self._qp[i] = self.N
        self._pq[self.N] = i
        self._keys[i] = x
        self._swim(self.N)

    def remove_min(self) -> int:
        """Remove min element from the heap and return its index. Raises IndexError when heap is empty."""
        if not self: raise IndexError('Heap is empty.')

        min_idx = self._pq[1]

        self._swap(1, self.N)
        self.N -= 1
        self._sink(1)

        self._qp[min_idx] = -1
        self._keys[min_idx] = None

        return min_idx

    def min_key(self) -> Any:
        """Get min element without removing it."""
        return self._keys[self._pq[1]]

    def change_key(self, i: int, x: Any) -> None:
        """Change key x associated with index i. Raises ValueError if index is already used."""
        if i not in self: ValueError("Index not in pq.")

        self._keys[i] = x
        self._swim(self._qp[i])
        self._sink(self._qp[i])

    def _swim(self, n):
        while n > 1 and self._keys[self._pq[n // 2]] > self._keys[self._pq[n]]:
            self._swap(n, n // 2)

            n //= 2

    def _swap(self, i, j):
        self._pq[i], self._pq[j] = self._pq[j], self._pq[i]
        self._qp[self._pq[i]], self._qp[self._pq[j]] = i, j

    def _sink(self, n):
        while n * 2 <= self.N:
            j = n * 2

            if j + 1 <= self.N and self._keys[self._pq[j]] > self._keys[self._pq[j + 1]]: j += 1

            if not self._keys[self._pq[n]] > self._keys[self._pq[j]]: return

            self._swap(j, n)

            n = j

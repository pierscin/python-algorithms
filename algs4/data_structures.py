import heapq
from typing import Any, Optional

from sortedcontainers import SortedList

from utils import ReverseOrderingWrapper


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


class Bst:
    """Binary Search Tree."""

    class Node:
        """Bst node."""

        def __init__(self, key: Any, val):
            self.key = key
            self.val = val
            self.left, self.right = None, None

    def __init__(self):
        self.root = None

    def __len__(self):
        return self.size(self.root)

    def put(self, key, val: object) -> None:
        """Upsert of value associated with the key."""
        if key is None: raise ValueError('None keys are not permitted')

        self.root = self._put(self.root, key, val)

    def get(self, key) -> object:
        """Get value associated with key or None if such node does not exist."""
        if key is None: raise ValueError('None keys are not permitted')

        return self._get(self.root, key)

    def min(self):
        """Return min key."""
        return self._min(self.root).key

    def max(self):
        """Return max key."""
        return self._max(self.root).key

    def remove_min(self) -> None:
        """Remove node with min key."""
        self.root = self._remove_min(self.root)

    def remove_max(self) -> None:
        """Remove node with max key."""
        self.root = self._remove_max(self.root)

    def remove(self, key) -> None:
        """Remove node with given key."""
        if key is None: raise ValueError('None keys are not permitted')

        self.root = self._remove(self.root, key)

    def size(self, node: Optional['Bst.Node']) -> int:
        if node is None: return 0

        return self.size(node.left) + self.size(node.right) + 1

    def _put(self, node: Optional['Bst.Node'], key, val: object) -> 'Bst.Node':

        if node is None: return Bst.Node(key, val)

        if key > node.key:   node.right = self._put(node.right, key, val)
        elif key < node.key: node.left = self._put(node.left, key, val)
        else: node.val = val

        return node

    def _get(self, node: Optional['Bst.Node'], key) -> object:
        if node is None: return None

        if key > node.key:   return self._get(node.right, key)
        elif key < node.key: return self._get(node.left, key)

        return node.val

    def _min(self, node) -> 'Bst.Node':
        return node if node.left is None else self._min(node.left)

    def _max(self, node) -> 'Bst.Node':
        return node if node.right is None else self._min(node.right)

    def _remove_min(self, node) -> 'Bst.Node':
        """Finds min node and returns it's RIGHT link."""
        if node.left is None: return node.right

        node.left = self._remove_min(node.left)

        return node

    def _remove_max(self, node) -> 'Bst.Node':
        """Finds max node and returns it's LEFT link."""
        if node.right is None: return node.left

        node.right = self._remove_max(node.right)

        return node

    def _remove(self, node: Optional['Bst.Node'], key) -> Optional['Bst.Node']:
        if node is None: return None

        if key > node.key:   node.right = self._remove(node.right, key)
        elif key < node.key: node.left = self._remove(node.left, key)
        else:
            if node.left is None: return node.right
            if node.right is None: return node.left

            # pierscin: Hibbard deletion
            t = node

            node = self._min(t.right)
            node.right = self._remove_min(t.right)
            node.left = t.left

        return node

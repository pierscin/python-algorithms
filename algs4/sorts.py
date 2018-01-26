from random import shuffle
from typing import Sequence


def selection_sort(A: Sequence) -> None:
    """Selection sort implementation.

    Starting from i = 0, find the smallest item in A[i:], exchange it with A[i], increment i.

    Invariants:
     - elements in A[0:i - 1] are in their final positions
     - all objects in A[i:] are >= than those in A[0:i - 1]

    Complexity:
        exchanges: N
        compares: N^2

    Args:
        A: sequence of comparable objects
    """
    for i in range(len(A) - 1):
        j = A.index(min(A[i:]), i)
        A[i], A[j] = A[j], A[i]


def insertion_sort(A: Sequence) -> None:
    """Insertion sort implementation.

    Pick one element and insert it in its place among already sorted part of a sequence (move larger items towards
    the end of an array). Very good for almost sorted sequences.

    Invariants:
     - elements in A[0:i - 1] are sorted

    Args:
        A: sequence of comparable objects
    """
    for i in range(1, len(A)):
        for j in reversed(range(i)):
            if A[j + 1] < A[j]:
                A[j + 1], A[j] = A[j], A[j + 1]
            else:
                break


def shell_sort(A: Sequence) -> None:
    """Shell sort implementation.

    Apply insertion sort for elements with distance h between them. Make h smaller.

    Step is calculated according to h = 3 * h + 1

    Invariants:
     - elements are h-sorted

    Args:
        A: sequence of comparable objects
    """

    h = 1
    while h < len(A) // 3: h = 3 * h + 1

    while h > 0:
        for i in range(h, len(A) + 1 - h):
            for j in reversed(range(0, i, h)):
                if A[j + h] < A[j]:
                    A[j + h], A[j] = A[j], A[j + h]
                else:
                    break
        h //= 3


def merge_sort(A: Sequence) -> None:
    """Merge sort implementation.

    Args:
        A: sequence of comparable objects
    """
    def _merge_sort(lo, hi):
        if lo >= hi: return

        mid = (hi + lo) // 2

        _merge_sort(lo, mid)
        _merge_sort(mid + 1, hi)

        merge(lo, mid, hi)

    def merge(lo, mid, hi):
        l, r = lo, mid + 1
        aux[lo:hi + 1] = A[lo:hi + 1]

        for k in range(lo, hi + 1):
            if l > mid:
                A[k] = aux[r]
                r += 1
            elif r > hi:
                A[k] = aux[l]
                l += 1
            elif aux[r] < aux[l]:
                A[k] = aux[r]
                r += 1
            else:
                A[k] = aux[l]
                l += 1

    aux = list(A)
    _merge_sort(0, len(A) - 1)


def comprehension_quick_sort(A: Sequence):
    """Quick sort implementation using list comprehension.

    Args:
        A: sequence of comparable objects
    """
    shuffle(A)

    def partition(A):
        if not A: return []

        e = A[0]

        left = partition([x for x in A[1:] if x <= e])
        right = partition([x for x in A[1:] if x > e])

        return left + [e] + right

    A[:] = partition(A)


def comprehension_three_way_quick_sort(A: Sequence):
    """Three way quick sort implementation using list comprehension.

    Args:
        A: sequence of comparable objects
    """
    shuffle(A)

    def partition(A):
        if not A: return []

        e = A[0]

        left = partition([x for x in A[1:] if x < e])
        middle = [x for x in A if x == e]
        right = partition([x for x in A[1:] if x > e])

        return left + middle + right

    A[:] = partition(A)


def quick_sort(A: Sequence):
    """Quick sort implementation.

    Args:
        A: sequence of comparable objects
    """
    shuffle(A)

    def partition(lo, hi):
        x = A[lo]
        l, r = lo + 1, hi

        while True:

            while A[l] < x:
                if l != hi: l += 1
                else: break

            while A[r] > x:
                if r != lo: r -= 1
                else: break

            if l >= r: break

            A[l], A[r] = A[r], A[l]
            l, r = l + 1, r - 1

        A[lo], A[r] = A[r], A[lo]

        return r

    def sort(lo, hi):
        if hi <= lo: return

        j = partition(lo, hi)

        sort(lo, j - 1)
        sort(j + 1, hi)

    sort(0, len(A) - 1)


def three_way_quick_sort(A: Sequence):
    """Three way quick sort implementation.

    Args:
        A: sequence of comparable objects
    """
    shuffle(A)

    def sort(lo, hi):
        if hi <= lo: return

        lt, gt, i = lo, hi, lo + 1
        x = A[lo]

        while i <= gt:
            if A[i] < x:
                A[lt], A[i] = A[i], A[lt]
                lt, i = lt + 1, i + 1
            elif A[i] > x:
                A[gt], A[i] = A[i], A[gt]
                gt -= 1
            else:
                i += 1

        sort(lo, lt - 1)
        sort(gt + 1, hi)

    sort(0, len(A) - 1)
